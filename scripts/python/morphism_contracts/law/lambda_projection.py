"""Cross-document laws for the declared validator combinator projection.

This module validates JSON coordinates.  It does not construct Lambda values,
evaluate expressions, bind host handlers, or model a runtime.  Executable
Lambda semantics belong exclusively to the registered Scala gateway.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def _diagnostic(rule: str, message: str) -> str:
    return f"[{rule}] {message}"


def _duplicates(values: Iterable[Any]) -> tuple[Any, ...]:
    seen: set[Any] = set()
    repeated: set[Any] = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        else:
            seen.add(value)
    return tuple(sorted(repeated))


def errors(profile: Mapping[str, Any]) -> list[str]:
    """Validate exact labelled coverage without realizing a Python runtime."""

    root = profile.get("validatorLambda")
    if not isinstance(root, dict):
        return [
            _diagnostic(
                "validator.lambda.registry.shape",
                "validatorLambda must be an object",
            )
        ]

    diagnostics: list[str] = []
    laws = root.get("laws")
    if isinstance(laws, dict) and laws.get("runtimeShoeClosure") is not False:
        diagnostics.append(
            _diagnostic(
                "validator.lambda.runtime-shoe.separation",
                "validator combinators cannot close the runtime-shoe world",
            )
        )

    role_rows = root.get("roles")
    roles = role_rows if isinstance(role_rows, list) else []
    role_keys = tuple(
        row.get("key") for row in roles if isinstance(row, dict)
    )
    role_identities = tuple(
        row.get("identity") for row in roles if isinstance(row, dict)
    )
    if (
        len(role_keys) != len(roles)
        or _duplicates(role_keys)
        or _duplicates(role_identities)
    ):
        diagnostics.append(
            _diagnostic(
                "validator.lambda.role.unique",
                "role keys and identities must be unique",
            )
        )

    policy = root.get("vectorPolicy")
    display = tuple(policy.get("displayOrder", ())) if isinstance(policy, dict) else ()
    if display != role_keys or tuple(profile.get("roleOrder", ())) != display:
        diagnostics.append(
            _diagnostic(
                "validator.lambda.role.order",
                "displayOrder must equal the registered profile role order",
            )
        )

    rows = root.get("combinators")
    combinators = rows if isinstance(rows, list) else []
    coordinates: list[tuple[Any, Any, Any]] = []
    identities: list[Any] = []
    vectors: list[Any] = []
    keys: list[tuple[Any, Any]] = []
    for row in combinators:
        if not isinstance(row, dict):
            continue
        key = (row.get("family"), row.get("operation"))
        keys.append(key)
        coordinates.append((*key, row.get("bindingIdentity")))
        identities.append(row.get("identity"))
        vectors.append(row.get("vectorIdentity"))
        declared_roles = row.get("roles")
        if not isinstance(declared_roles, dict) or set(declared_roles) != set(role_keys):
            diagnostics.append(
                _diagnostic(
                    "validator.lambda.role.coverage",
                    f"combinator {key!r} does not cover labelled roles exactly",
                )
            )
    if any(
        _duplicates(values)
        for values in (keys, coordinates, identities, vectors)
    ):
        diagnostics.append(
            _diagnostic(
                "validator.lambda.combinator.unique",
                "combinator coordinates and identities must be unique",
            )
        )
    if tuple(keys) != tuple(sorted(keys)):
        diagnostics.append(
            _diagnostic(
                "validator.lambda.combinator.order",
                "combinators must use deterministic family/operation order",
            )
        )

    coverage_rows = root.get("coverage")
    coverage = coverage_rows if isinstance(coverage_rows, list) else []
    families: list[Any] = []
    covered: list[tuple[Any, Any, Any]] = []
    for row in coverage:
        if not isinstance(row, dict):
            continue
        family = row.get("family")
        families.append(family)
        bindings = row.get("bindings")
        binding_rows = bindings if isinstance(bindings, list) else []
        entries = tuple(
            (binding.get("operation"), binding.get("bindingIdentity"))
            for binding in binding_rows
            if isinstance(binding, dict)
        )
        if len(entries) != len(binding_rows) or entries != tuple(sorted(entries)) or _duplicates(entries):
            diagnostics.append(
                _diagnostic(
                    "validator.lambda.coverage.order",
                    f"coverage for {family!r} must be sorted and unique",
                )
            )
        covered.extend((family, operation, identity) for operation, identity in entries)
    if tuple(families) != tuple(sorted(families)) or _duplicates(families):
        diagnostics.append(
            _diagnostic(
                "validator.lambda.coverage.family",
                "coverage families must be sorted and unique",
            )
        )
    if set(covered) != set(coordinates):
        diagnostics.append(
            _diagnostic(
                "validator.lambda.coverage.exact",
                "coverage coordinates differ from registered combinators",
            )
        )

    return sorted(set(diagnostics))
