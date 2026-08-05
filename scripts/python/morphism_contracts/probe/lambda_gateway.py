"""Deterministic laws for the declared Scala Lambda gateway projection."""

from __future__ import annotations

import copy
from dataclasses import dataclass

from morphism_contracts.law.lambda_projection import errors as projection_errors
from sparky_lambda import Client
from sparky_lambda.contract import Contract
from sparky_lambda.contract_gate.host.octet import (
    DecodingRejected,
    EncodingEqual,
    EncodingUnequal,
    Projection,
    decode,
    equivalent,
    observe_encoding,
)
from sparky_lambda.contract_gate.location import repository as repository_locator
from sparky_lambda.contract_gate.test_support import responses
from sparky_lambda.jvm import Requirement as JVMRequirement
from sparky_lambda.kind import Provisional, TimestampStale
from sparky_lambda.locator import Locator


@dataclass(frozen=True, slots=True)
class PreserveProjection:
    pass


@dataclass(frozen=True, slots=True)
class ReverseCombinators:
    pass


@dataclass(frozen=True, slots=True)
class DuplicateCombinator:
    pass


@dataclass(frozen=True, slots=True)
class DriftCoverage:
    pass


@dataclass(frozen=True, slots=True)
class ReverseCoverageBindings:
    pass


@dataclass(frozen=True, slots=True)
class ReverseCoverageFamilies:
    pass


@dataclass(frozen=True, slots=True)
class CloseRuntimeShoes:
    pass


@dataclass(frozen=True, slots=True)
class ReverseRoleOrder:
    pass


@dataclass(frozen=True, slots=True)
class DropCombinatorRole:
    pass


Mutation = (
    PreserveProjection
    | ReverseCombinators
    | DuplicateCombinator
    | DriftCoverage
    | ReverseCoverageBindings
    | ReverseCoverageFamilies
    | CloseRuntimeShoes
    | ReverseRoleOrder
    | DropCombinatorRole
)


@dataclass(frozen=True, slots=True)
class ValidProbe:
    label: str
    mutation: Mutation


@dataclass(frozen=True, slots=True)
class InvalidProbe:
    label: str
    rule: str
    mutation: Mutation


Probe = ValidProbe | InvalidProbe


def _apply(profile, mutation: Mutation) -> None:
    if isinstance(mutation, PreserveProjection):
        return
    if isinstance(mutation, ReverseCombinators):
        profile["validatorLambda"]["combinators"].reverse()
        return
    if isinstance(mutation, DuplicateCombinator):
        rows = profile["validatorLambda"]["combinators"]
        rows.append(copy.deepcopy(rows[0]))
        return
    if isinstance(mutation, DriftCoverage):
        binding = profile["validatorLambda"]["coverage"][0]["bindings"][0]
        binding["bindingIdentity"] = f"{binding['bindingIdentity']}:drift"
        return
    if isinstance(mutation, ReverseCoverageBindings):
        rows = profile["validatorLambda"]["coverage"]
        target = next(row for row in rows if len(row["bindings"]) > 1)
        target["bindings"].reverse()
        return
    if isinstance(mutation, ReverseCoverageFamilies):
        profile["validatorLambda"]["coverage"].reverse()
        return
    if isinstance(mutation, CloseRuntimeShoes):
        profile["validatorLambda"]["laws"]["runtimeShoeClosure"] = True
        return
    if isinstance(mutation, ReverseRoleOrder):
        profile["validatorLambda"]["vectorPolicy"]["displayOrder"].reverse()
        return
    if isinstance(mutation, DropCombinatorRole):
        roles = profile["validatorLambda"]["combinators"][0]["roles"]
        del roles[next(iter(roles))]
        return
    raise TypeError(f"unregistered Lambda projection mutation: {type(mutation).__name__}")


def _expect(profile, probe: Probe) -> str | None:
    candidate = copy.deepcopy(profile)
    _apply(candidate, probe.mutation)
    diagnostics = projection_errors(candidate)
    if isinstance(probe, ValidProbe):
        if diagnostics:
            return f"{probe.label}: valid projection was rejected: {diagnostics!r}"
        return None
    expected = f"[{probe.rule}]"
    if not any(item.startswith(expected) for item in diagnostics):
        return f"{probe.label}: expected {probe.rule!r}; observed {diagnostics!r}"
    return None


def _gateway_readback(repository: Locator) -> str | None:
    contract = Contract.discover(repository)
    readback = Client.readback(repository)
    projection = Projection.registered(contract)
    request_encoding = observe_encoding(readback.request, projection)
    request = decode(readback.request, projection)
    response_encoding = observe_encoding(readback.response, projection)
    response = decode(readback.response, projection)
    if isinstance(request, DecodingRejected):
        return f"gateway-readback: request decoding rejected: {request.issue_evidence}"
    if isinstance(response, DecodingRejected):
        return f"gateway-readback: response decoding rejected: {response.issue_evidence}"
    if not isinstance(projection.state, Provisional) or not projection.gap_identity:
        return "gateway-readback: host octet projection lost its provisional gap"
    if request_encoding.host_octet_count <= 0 or response_encoding.host_octet_count <= 0:
        return "gateway-readback: artifact host-octet observation is empty"
    return None


def _gateway_mcp_registration(repository: Locator) -> str | None:
    """Check the typed provisional registration without inventing a handler."""

    contract = Contract.discover(repository)
    registration = contract.mcp_tool
    mcp = Client.mcp(repository)
    if mcp.capability != registration.capability:
        return "gateway-mcp-registration: capability differs from contract"
    if mcp.tool != registration.tool:
        return "gateway-mcp-registration: tool differs from contract"
    if mcp.argument_field != registration.argument_field:
        return "gateway-mcp-registration: argument field differs from contract"
    if mcp.state != registration.state or not isinstance(mcp.state, Provisional):
        return "gateway-mcp-registration: provisional state was collapsed"
    return None


def _gateway_process_execution(repository: Locator) -> tuple[str | None, int]:
    """Run equal requests through the actual Scala process boundary."""

    contract = Contract.discover(repository)
    readback = Client.readback(repository)
    projection = Projection.registered(contract)
    executions = []
    try:
        process = Client.jvm(repository)
        with responses(repository, "sparky-lambda-probe-") as locators:
            response_artifacts = (
                process.response(locators.first),
                process.response(locators.second),
            )
            for response in response_artifacts:
                executions.append(process.invoke(readback.request, response))
            observed = tuple(decode(response, projection) for response in response_artifacts)
            encoded = tuple(
                observe_encoding(response, projection) for response in response_artifacts
            )
            repeated = equivalent(response_artifacts[0], response_artifacts[1], projection)
            fixture = equivalent(response_artifacts[0], readback.response, projection)
    except JVMRequirement as issue:
        evidence = "; ".join(issue.observation.observations)
        return (
            f"gateway-process: registered JVM shoe is unavailable: {evidence}",
            len(executions),
        )
    except (OSError, RuntimeError, ValueError) as issue:
        return (
            f"gateway-process: registered Scala invocation failed: {issue}",
            len(executions),
        )

    expected = decode(readback.response, projection)
    if any(isinstance(item, DecodingRejected) for item in observed):
        return "gateway-process: live Scala response decoding was rejected", len(executions)
    if isinstance(expected, DecodingRejected):
        return "gateway-process: immutable receipt decoding was rejected", len(executions)
    if not isinstance(repeated, EncodingEqual):
        return "gateway-process: equal requests emitted different bytes", len(executions)
    if not isinstance(fixture, EncodingUnequal):
        return (
            "gateway-process: live occurrence collapsed into immutable receipt occurrence",
            len(executions),
        )
    if encoded[0].host_octet_count != encoded[1].host_octet_count:
        return "gateway-process: equal artifacts emitted different host-octet counts", len(executions)
    registration = contract.process_file
    if any(
        execution.evidence.state != registration.operation_state
        or execution.evidence.gap_identities != registration.gap_identities
        for execution in executions
    ):
        return "gateway-process: live execution lost provisional gap evidence", len(executions)
    if not any(
        isinstance(dependency.state, TimestampStale)
        for dependency in executions[0].evidence.owned_dependencies
    ):
        return "gateway-process: stale owned product evidence was lost", len(executions)
    directory_revisions = tuple(
        revision
        for dependency in executions[0].evidence.owned_dependencies
        for revision in (dependency.source, dependency.product)
        if revision.directories
    )
    non_atomic_gap = contract.contract_gate.capture.non_atomic_snapshot_gap_identity
    if any(
        not any(gap.identity == non_atomic_gap for gap in revision.gaps)
        for revision in directory_revisions
    ):
        return "gateway-process: directory revision lost its snapshot gap", len(executions)
    return None, len(executions)


def tests(repository, profile, documents, schema) -> tuple[list[str], tuple[tuple[str, int], ...]]:
    """Generate projection mutations from registered profile coordinates."""

    del documents, schema
    repository_value = repository_locator(str(repository))
    probes: tuple[Probe, ...] = (
        ValidProbe("registered-projection", PreserveProjection()),
        InvalidProbe("duplicate-combinator", "validator.lambda.combinator.unique", DuplicateCombinator()),
        InvalidProbe("combinator-order", "validator.lambda.combinator.order", ReverseCombinators()),
        InvalidProbe("coverage-drift", "validator.lambda.coverage.exact", DriftCoverage()),
        InvalidProbe("coverage-order", "validator.lambda.coverage.order", ReverseCoverageBindings()),
        InvalidProbe("coverage-family-order", "validator.lambda.coverage.family", ReverseCoverageFamilies()),
        InvalidProbe("runtime-shoe-closure", "validator.lambda.runtime-shoe.separation", CloseRuntimeShoes()),
        InvalidProbe("role-order", "validator.lambda.role.order", ReverseRoleOrder()),
        InvalidProbe("role-coverage", "validator.lambda.role.coverage", DropCombinatorRole()),
    )
    failures = [
        failure
        for probe in probes
        if (failure := _expect(profile, probe)) is not None
    ]
    readback_laws = (_gateway_readback(repository_value),)
    mcp_registration_laws = (_gateway_mcp_registration(repository_value),)
    process_failure, process_executions = _gateway_process_execution(repository_value)
    process_execution_laws = (process_failure,)
    gateway_laws = readback_laws + mcp_registration_laws + process_execution_laws
    failures.extend(failure for failure in gateway_laws if failure is not None)
    return failures, (
        ("lambda-projection-probes", len(probes)),
        ("lambda-readback-probes", len(readback_laws)),
        ("lambda-mcp-registration-probes", len(mcp_registration_laws)),
        ("lambda-process-executions", process_executions),
    )
