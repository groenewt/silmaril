"""Data-driven validator probes over injected pure combinators."""

from __future__ import annotations

import copy
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from morphism_contracts.digest.policy import capability_errors
from morphism_contracts.json.document import decode_json
from morphism_contracts.mutation.operations import resolve_path


Equal = Callable[[Any, Any], bool]
Validate = Callable[[dict[str, Any], dict[str, Any]], list[str]]
ArtifactSelector = Callable[[dict[str, Any], dict[str, Any]], str | None]
ProvisionalValidator = Callable[
    [dict[str, Any], Any, dict[str, dict[str, Any]], dict[str, Any]], list[str]
]
ContractDigest = Callable[[dict[str, Any], dict[str, Any]], str]
Operation = Callable[..., Any]
Operations = Mapping[str, Operation]


@dataclass(frozen=True, slots=True)
class MechanicContext:
    digest_policy: dict[str, Any]
    artifact_kind_registry: dict[str, Any]
    provisional_validator: ProvisionalValidator
    format_projection: Callable[[str, str], str | None]


def mechanic_format(
    specification: dict[str, Any], context: MechanicContext
) -> list[str]:
    failure = context.format_projection(
        specification["format"], specification["value"]
    )
    return [failure] if failure else []


def mechanic_json(
    specification: dict[str, Any], context: MechanicContext
) -> list[str]:
    try:
        decode_json(
            specification["value"],
            f"mechanic-test:{specification['id']}",
        )
    except ValueError as error:
        return [str(error)]
    return []


def mechanic_digest_support(
    specification: dict[str, Any], context: MechanicContext
) -> list[str]:
    policy = copy.deepcopy(context.digest_policy)
    policy[specification["coordinate"]] = specification["value"]
    return capability_errors(policy)


def mechanic_artifact_kind(
    specification: dict[str, Any], context: MechanicContext
) -> list[str]:
    policy = copy.deepcopy(context.artifact_kind_registry)
    policy["closedEnumeration"] = specification["closedEnumeration"]
    registration = specification["registration"]
    schema_id = registration.get(policy["provisionalCoordinates"]["schema"])
    if not isinstance(schema_id, str):
        schema_id = specification["document"].get("schema")
    if not isinstance(schema_id, str):
        raise ValueError("registered artifact-kind probe has no schema coordinate")
    return context.provisional_validator(
        registration,
        specification["document"],
        {schema_id: specification["schemaDocument"]},
        policy,
    )


def reverse(target: Any) -> None:
    if not isinstance(target, list):
        raise ValueError("registered determinism operation requires an array target")
    target.reverse()


def self_tests(
    index: dict[str, Any],
    documents: dict[str, Any],
    specifications: list[dict[str, Any]],
    artifact_selector: ArtifactSelector,
    validate: Validate,
    equal: Equal,
    operations: Operations,
) -> tuple[list[str], int]:
    failures: list[str] = []
    for specification in specifications:
        label = specification["id"]
        changed_index = copy.deepcopy(index)
        changed = copy.deepcopy(documents)
        try:
            artifact_id = artifact_selector(specification["artifact"], changed_index)
            target = changed_index if artifact_id is None else changed[artifact_id]
            operation = operations[specification["operation"]["kind"]]
            operation(
                target,
                specification,
                equal,
            )
        except (KeyError, TypeError, ValueError) as error:
            failures.append(f"{label}: invalid registered mutation: {error}")
            continue
        diagnostics = validate(changed_index, changed)
        expected_rule = f"[{specification['ruleId']}]"
        if not diagnostics:
            failures.append(f"{label}: mutation was accepted")
        elif not any(item.startswith(expected_rule) for item in diagnostics):
            failures.append(
                f"{label}: expected rule {specification['ruleId']!r} was not emitted"
            )
    return failures, len(specifications)


def mechanic_tests(
    specifications: list[dict[str, Any]],
    context: MechanicContext,
    operations: Operations,
) -> tuple[list[str], int]:
    failures: list[str] = []
    for specification in specifications:
        label = specification["id"]
        kind = specification["kind"]
        try:
            diagnostics = operations[kind](specification, context)
        except (KeyError, TypeError, ValueError) as error:
            failures.append(f"{label}: invalid registered mechanic: {error}")
            continue
        accepted = not diagnostics
        if accepted != specification["accepted"]:
            failures.append(
                f"{label}: expected accepted={specification['accepted']} "
                f"but observed diagnostics={diagnostics!r}"
            )
        expected_rule = specification.get("ruleId")
        if (
            not accepted
            and expected_rule
            and not any(f"[{expected_rule}]" in item for item in diagnostics)
        ):
            failures.append(
                f"{label}: expected rule {expected_rule!r} was not emitted"
            )
    return failures, len(specifications)


def determinism_tests(
    index: dict[str, Any],
    documents: dict[str, Any],
    specifications: list[dict[str, Any]],
    contract_digest: ContractDigest,
    equal: Equal,
    operations: Operations,
) -> tuple[list[str], int]:
    failures: list[str] = []
    baseline = contract_digest(index, documents)
    for specification in specifications:
        changed = copy.deepcopy(index)
        try:
            target = resolve_path(changed, specification["path"], equal)
            operations[specification["operation"]](target)
        except (KeyError, TypeError, ValueError) as error:
            failures.append(
                f"{specification['id']}: invalid registered determinism probe: {error}"
            )
            continue
        observed = contract_digest(changed, documents)
        if specification["expect"] == "same-digest" and observed != baseline:
            failures.append(
                f"{specification['id']}: digest changed under registered non-semantic permutation"
            )
    return failures, len(specifications)
