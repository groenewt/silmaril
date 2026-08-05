"""Cross-document validation for one profile-projected contract bundle."""

from __future__ import annotations

from typing import Any

from morphism_contracts.json.document import unique_by_errors
from morphism_contracts.law.scene import SceneLaws
from morphism_contracts.law.lambda_projection import errors as lambda_projection_errors
from morphism_contracts.law.topology import validate as validate_topology_schema
from morphism_contracts.schema.combinators import Combinators


def _diagnostic(rule_id: str, message: str) -> str:
    return f"[{rule_id}] {message}"


def _require(
    errors: list[str], condition: bool, message: str, rule_id: str | None = None
) -> None:
    if not condition:
        errors.append(_diagnostic(rule_id, message) if rule_id else message)


def _constant_registry_errors(document: Any) -> list[str]:
    """Laws JSON Schema cannot express: canonical order and projection closure."""

    if not isinstance(document, dict):
        return [
            _diagnostic(
                "lambda.constants.document",
                "Lambda invocation constant registry must be an object",
            )
        ]
    entries = document.get("entries")
    projection = document.get("projection")
    if not isinstance(entries, list) or not isinstance(projection, dict):
        return []  # Structural diagnostics are emitted by the registered schema.
    packages = [
        entry.get("package")
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("package"), str)
    ]
    constructors = projection.get("constructors")
    prefix = projection.get("packagePrefix")
    errors: list[str] = []
    _require(
        errors,
        len(packages) == len(entries) and packages == sorted(packages),
        "Lambda invocation constants are not in canonical package order",
        "lambda.constants.order",
    )
    _require(
        errors,
        len(packages) == len(set(packages)),
        "Lambda invocation constant packages are not unique",
        "lambda.constants.unique",
    )
    if isinstance(prefix, str):
        _require(
            errors,
            all(package.startswith(f"{prefix}.") for package in packages),
            "Lambda invocation constant escaped its declared package projection",
            "lambda.constants.package",
        )
    if isinstance(constructors, dict):
        _require(
            errors,
            all(
                isinstance(entry, dict) and entry.get("kind") in constructors
                for entry in entries
            ),
            "Lambda invocation constant kind has no declared constructor",
            "lambda.constants.constructor",
        )
    return errors


class Validator:
    """Pure contract laws closed over a profile and schema combinators."""

    def __init__(self, profile: dict[str, Any], schema: Combinators) -> None:
        self.profile = profile
        self.schema = schema
        self.scene_laws = SceneLaws(profile, schema.digest)

    def provisional_artifact_errors(
        self,
        artifact: dict[str, Any],
        document: Any,
        schema_registry: dict[str, dict[str, Any]],
        policy: dict[str, Any],
    ) -> list[str]:
        artifact_id = artifact.get("id")
        kind = artifact.get("kind")
        if policy.get("closedEnumeration") is True:
            return [
                _diagnostic(
                    "artifact.kind.closed-enumeration",
                    f"{artifact_id}: artifact kind {kind!r} is outside the closed registry",
                )
            ]
        coordinates = policy["provisionalCoordinates"]
        schema_id = artifact.get(coordinates["schema"])
        status = artifact.get(coordinates["status"])
        evidence = artifact.get(coordinates["sourceEvidence"])
        minimum = policy["sourceEvidenceMinimum"]
        if (
            not isinstance(schema_id, str)
            or status != policy["provisionalStatus"]
            or not isinstance(evidence, list)
            or len(evidence) < minimum
            or not all(isinstance(source, str) and source for source in evidence)
        ):
            return [
                _diagnostic(
                    "artifact.kind.provisional-evidence",
                    f"{artifact_id}: artifact kind {kind!r} lacks explicit provisional "
                    f"schema/status/sourceEvidence required by {policy['unknownKind']!r}",
                )
            ]
        target_schema = schema_registry.get(schema_id)
        if not isinstance(target_schema, dict):
            return [
                _diagnostic(
                    "artifact.kind.provisional-schema",
                    f"{artifact_id}: provisional schema {schema_id!r} is not registered",
                )
            ]
        errors: list[str] = []
        _require(
            errors,
            isinstance(document, dict) and document.get("schema") == schema_id,
            f"{artifact_id}: provisional document does not name its registered schema",
            "artifact.kind.provisional-schema",
        )
        errors.extend(
            self.schema.errors(
                document,
                target_schema,
                schema_registry,
                target_schema,
                str(artifact_id),
            )
        )
        return errors

    def validate(
        self, index: dict[str, Any], documents: dict[str, Any]
    ) -> list[str]:
        profile = self.profile
        schema_ids = profile["artifactIds"]
        kind_rules = {row["kind"]: row for row in profile["artifactKinds"]}
        errors: list[str] = []
        _require(
            errors,
            index.get("schema") == schema_ids["contractSet"],
            "index: wrong schema",
        )
        artifacts = index.get("artifacts", [])
        _require(
            errors,
            isinstance(artifacts, list) and bool(artifacts),
            "index: artifacts must be a non-empty array",
        )
        if not isinstance(artifacts, list):
            return sorted(set(errors))

        loaded_profile: Any = None
        for row in artifacts:
            if isinstance(row, dict) and row.get("kind") == "validation-profile":
                loaded_profile = documents.get(row.get("id"))
                break
        uniqueness = unique_by_errors(
            {"contract-set": index, "validation-profile": loaded_profile},
            profile["uniqueBy"],
        )
        if uniqueness:
            return sorted(set(errors + uniqueness))

        artifact_ids = {
            row.get("id") for row in artifacts if isinstance(row, dict)
        }
        _require(
            errors,
            artifact_ids == set(documents),
            "index: registered artifacts and loaded documents differ",
        )
        schema_registry = {
            artifact.get("id"): documents.get(artifact.get("id"), {})
            for artifact in artifacts
            if isinstance(artifact, dict) and artifact.get("kind") == "schema"
        }
        for artifact in artifacts:
            artifact_id = artifact.get("id")
            kind = artifact.get("kind")
            document = documents.get(artifact_id, {})
            if kind == "schema":
                _require(
                    errors,
                    document.get("$schema") == profile["jsonSchemaDialect"],
                    f"{artifact_id}: wrong JSON Schema dialect",
                )
                _require(
                    errors,
                    document.get("$id") == artifact_id
                    and document.get("type") == "object",
                    f"{artifact_id}: schema registration mismatch",
                )
            elif kind in kind_rules:
                rule = kind_rules[kind]
                schema_id = schema_ids[rule["schemaKey"]]
                _require(
                    errors,
                    document.get("schema") == schema_id
                    and document.get(rule["identityField"]) == artifact_id,
                    f"{artifact_id}: instance registration mismatch",
                )
                target_schema = schema_registry.get(schema_id)
                if isinstance(target_schema, dict):
                    errors.extend(
                        self.schema.errors(
                            document,
                            target_schema,
                            schema_registry,
                            target_schema,
                            artifact_id,
                        )
                    )
                else:
                    errors.append(
                        f"{artifact_id}: registered schema {schema_id!r} is absent"
                    )
            else:
                errors.extend(
                    self.provisional_artifact_errors(
                        artifact,
                        document,
                        schema_registry,
                        profile["artifactKindRegistry"],
                    )
                )

        contract_set_schema = schema_registry.get(schema_ids["contractSet"])
        if isinstance(contract_set_schema, dict):
            errors.extend(
                self.schema.errors(
                    index,
                    contract_set_schema,
                    schema_registry,
                    contract_set_schema,
                    "contract-set",
                )
            )
        else:
            errors.append("contract-set: registered schema is absent")

        validate_topology_schema(
            documents.get(schema_ids["topology"], {}),
            errors,
            profile,
            self.schema.exact_equal,
        )
        self.scene_laws.validate_schema(
            documents.get(schema_ids["scene"], {}), errors
        )
        instances_by_kind = {
            kind: [
                documents[row["id"]]
                for row in artifacts
                if row.get("kind") == kind
            ]
            for kind in kind_rules
        }
        for kind, rule in kind_rules.items():
            if rule["cardinality"] == "exactly-one":
                _require(
                    errors,
                    len(instances_by_kind[kind]) == 1,
                    f"contract set: exactly one {kind} is required",
                )
        scenes = instances_by_kind.get("scene", [])
        lexicons = instances_by_kind.get("lexicon", [])
        profiles = instances_by_kind.get("validation-profile", [])
        constant_registries = instances_by_kind.get(
            "lambda-runtime-constants", []
        )
        gateways = instances_by_kind.get("lambda-runtime-gateway", [])
        if len(constant_registries) == 1:
            registry = constant_registries[0]
            errors.extend(_constant_registry_errors(registry))
            if len(gateways) == 1:
                implementation = gateways[0].get("implementation", {})
                projection = registry.get("projection", {})
                _require(
                    errors,
                    implementation.get("constantRegistry") == registry.get("id"),
                    "Lambda gateway does not bind the registered constant projection",
                    "lambda.constants.gateway-registry",
                )
                _require(
                    errors,
                    implementation.get("constantGenerator")
                    == projection.get("generator"),
                    "Lambda gateway and constant registry name different generators",
                    "lambda.constants.gateway-generator",
                )
        if len(profiles) == 1:
            errors.extend(lambda_projection_errors(profiles[0]))
            _require(
                errors,
                self.schema.exact_equal(profiles[0], profile),
                "contract set: loaded validation profile differs from the bootstrap profile",
            )
        if len(scenes) == 1 and len(lexicons) == 1:
            self.scene_laws.validate_scene(scenes[0], lexicons[0], errors)
            self.scene_laws.validate_lexicon(lexicons[0], errors)
        return sorted(set(errors))
