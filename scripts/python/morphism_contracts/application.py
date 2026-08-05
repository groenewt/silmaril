"""Application projection for morphism contract validation."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Iterable

from morphism_contracts.configuration import Configuration
from morphism_contracts.contract.bundle import Bundle
from morphism_contracts.contract.validation import Validator
from morphism_contracts.probe.lambda_gateway import tests as lambda_gateway_tests
from morphism_contracts.mutation.operations import (
    append_copy,
    fill_preserving_length,
    remove_matching,
    set_value,
)
from morphism_contracts.probe.execution import (
    MechanicContext,
    determinism_tests,
    mechanic_artifact_kind,
    mechanic_digest_support,
    mechanic_format,
    mechanic_json,
    mechanic_tests,
    reverse,
    self_tests,
)
from morphism_contracts.schema.combinators import (
    Combinators,
    date_time_error,
    uri_error,
    uri_reference_error,
)
from morphism_contracts.twin.readback import errors as twin_readback_errors


class Application:
    """One fully bound validator projection over a repository and profile."""

    def __init__(self, repo: Path) -> None:
        self.configuration = Configuration.load(repo)
        self.profile = self.configuration.profile
        self.schema = Combinators(
            self.profile["digestPolicy"], self._format_projection
        )
        self.validator = Validator(self.profile, self.schema)

    def _format_projection(self, declared_format: str, value: str) -> str | None:
        operations = {
            "date-time": date_time_error,
            "uri": uri_error,
            "uri-reference": uri_reference_error,
        }
        return operations[declared_format](value)

    def _artifact_for(
        self, selector: dict[str, Any], index: dict[str, Any]
    ) -> str | None:
        if selector.get("contractSet") is True:
            return None
        if "schemaKey" in selector:
            return self.profile["artifactIds"][selector["schemaKey"]]
        matches = [
            row["id"]
            for row in index.get("artifacts", [])
            if row.get("kind") == selector.get("kind")
        ]
        if len(matches) != 1:
            raise ValueError(
                f"artifact selector {selector!r} resolved {len(matches)} values"
            )
        return matches[0]

    def _contract_digest(
        self, index: dict[str, Any], documents: dict[str, Any]
    ) -> str:
        return Bundle(index, documents).digest(self.profile, self.schema.digest)

    def _self_test_entry(
        self, index: dict[str, Any], documents: dict[str, Any]
    ) -> tuple[list[str], tuple[tuple[str, int], ...]]:
        failures, mutation_count = self_tests(
            index,
            documents,
            self.profile["selfTests"],
            self._artifact_for,
            self.validator.validate,
            self.schema.exact_equal,
            self._mutation_projection(),
        )
        context = MechanicContext(
            digest_policy=self.profile["digestPolicy"],
            artifact_kind_registry=self.profile["artifactKindRegistry"],
            provisional_validator=self.validator.provisional_artifact_errors,
            format_projection=self._format_projection,
        )
        mechanic_failures, mechanic_count = mechanic_tests(
            self.profile["mechanicTests"], context, self._mechanic_projection()
        )
        determinism_failures, determinism_count = determinism_tests(
            index,
            documents,
            self.profile["determinismTests"],
            self._contract_digest,
            self.schema.exact_equal,
            self._determinism_projection(),
        )
        lambda_failures, lambda_counts = lambda_gateway_tests(
            self.configuration.repo,
            self.profile,
            documents,
            self.schema,
        )
        failures.extend(mechanic_failures)
        failures.extend(determinism_failures)
        failures.extend(lambda_failures)
        return failures, (
            ("invalid-mutations", mutation_count),
            ("mechanic-probes", mechanic_count),
            ("determinism-probes", determinism_count),
        ) + lambda_counts

    def _twin_readback_entry(
        self, index: dict[str, Any], documents: dict[str, Any]
    ) -> tuple[list[str], tuple[tuple[str, int], ...]]:
        scene_id = next(
            row["id"]
            for row in index["artifacts"]
            if row.get("kind") == "scene"
        )
        scene = documents[scene_id]
        dispatch = {
            row["key"]: (row["primary"], set(row["schemes"]))
            for row in self.profile["twinSchemeDispatch"]
        }
        adapters = {
            row["key"]: row["adapterIdentity"]
            for row in self.profile["twinSchemeDispatch"]
        }
        policy = self.profile["twinReadback"]
        errors = twin_readback_errors(
            scene,
            self.configuration.repo,
            policy,
            dispatch,
            adapters,
            self.profile["relationPredicates"],
        )
        return errors, (
            ("source-evidence-files", len(policy["files"])),
            ("location-roots", len(scene["locationSources"])),
            ("adapters", len(dispatch)),
        )

    @staticmethod
    def _determinism_projection() -> dict[str, Any]:
        return {
            "reverse": reverse,
        }

    @staticmethod
    def _mechanic_projection() -> dict[str, Any]:
        return {
            "artifact-kind": mechanic_artifact_kind,
            "digest-support": mechanic_digest_support,
            "format": mechanic_format,
            "json": mechanic_json,
        }

    @staticmethod
    def _mutation_projection() -> dict[str, Any]:
        return {
            "append-copy": append_copy,
            "fill-preserving-length": fill_preserving_length,
            "remove-matching": remove_matching,
            "set": set_value,
        }

    @staticmethod
    def _render_counts(counts: tuple[tuple[str, int], ...]) -> str:
        return " ".join(f"{name}={count}" for name, count in counts)

    def run(self, argv: Iterable[str]) -> int:
        arguments = list(argv)
        try:
            bundle = Bundle.load(self.configuration)
        except ValueError as error:
            print(f"morphism-contracts: FAIL: {error}", file=sys.stderr)
            return 1

        errors = self.validator.validate(bundle.index, bundle.documents)
        if errors:
            print("morphism-contracts: FAIL", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1

        if arguments == ["self-test"]:
            failures, counts = self._self_test_entry(
                bundle.index, bundle.documents
            )
            if failures:
                print("morphism-contracts self-test: FAIL", file=sys.stderr)
                for failure in failures:
                    print(f"- accepted invalid mutation: {failure}", file=sys.stderr)
                return 1
            print(
                "morphism-contracts self-test: PASS "
                f"({self._render_counts(counts)})"
            )
        elif arguments == ["twin-readback"]:
            twin_errors, counts = self._twin_readback_entry(
                bundle.index, bundle.documents
            )
            if twin_errors:
                print("morphism-contracts twin-readback: FAIL", file=sys.stderr)
                for error in twin_errors:
                    print(f"- {error}", file=sys.stderr)
                return 1
            print(
                "morphism-contracts twin-readback: PASS "
                f"({self._render_counts(counts)})"
            )
        elif arguments:
            print(
                "usage: validate-morphism-contracts.py [self-test|twin-readback]",
                file=sys.stderr,
            )
            return 2

        print(
            "morphism-contracts: PASS "
            f"digest={bundle.digest(self.profile, self.schema.digest)} "
            f"artifacts={len(bundle.documents)}"
        )
        return 0


def run(repo: Path, argv: Iterable[str]) -> int:
    try:
        application = Application(repo)
    except (KeyError, TypeError, ValueError) as error:
        print(f"morphism-contracts: FAIL: {error}", file=sys.stderr)
        return 1
    return application.run(argv)
