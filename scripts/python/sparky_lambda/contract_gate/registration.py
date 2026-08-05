"""Raw contract documents admitted and projected only inside ContractGate."""

from __future__ import annotations

import json
import os
from pathlib import Path

from ..contract import (
    Artifact,
    CaptureRegistration,
    Contract,
    ContractGateRegistration,
    HostOctetProjection,
    Implementation,
    Laws,
    McpToolRegistration,
    ProcessFileRegistration,
    ReceiptReadbackRegistration,
)
from ..kind import (
    DescriptorClosedAfterCapture,
    DescriptorClosedAfterEnumeration,
    DirectoryEnumerationDrifted,
    DirectoryEnumerationStable,
    ExternalProductObserved,
    FileCaptureDrifted,
    FileCaptureStable,
    Provisional,
    PythonSemanticsAbsent,
    Registered,
    RevisionProvisionalCaptured,
    RevisionProvisionalDrifted,
    RevisionProvisionalIncomplete,
    StateRegistry,
    TimestampCurrentUnverified,
    TimestampStale,
)
from ..locator import Locator
from .location import admit


def _unique(source: Path):
    def unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
        value: dict[str, object] = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"duplicate JSON coordinate {key!r} in {source}")
            value[key] = item
        return value

    return unique


def _loads(text: str, source: Path) -> object:
    return json.loads(text, object_pairs_hook=_unique(source))


def _read(path: Path) -> object:
    return _loads(path.read_text(encoding="utf-8"), path)


def _object(value: object, coordinate: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"Lambda gateway coordinate is not an object: {coordinate}")
    return value


def _string(value: object, coordinate: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"Lambda gateway coordinate is not text: {coordinate}")
    return value


def _integer(value: object, coordinate: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"Lambda gateway coordinate is not positive: {coordinate}")
    return value


def _registered(
    value: object,
    coordinate: str,
    states: StateRegistry,
) -> Registered:
    if value != "registered":
        raise ValueError(f"Lambda gateway coordinate is not registered: {coordinate}")
    return states.registered


def _provisional(
    value: object,
    coordinate: str,
    states: StateRegistry,
) -> Provisional:
    if value != "provisional":
        raise ValueError(f"Lambda gateway coordinate is not provisional: {coordinate}")
    return states.provisional


def _state_coordinates(
    rows: tuple[dict[str, object], ...],
    kind: str,
) -> tuple[str, str]:
    matches = tuple(row for row in rows if row.get("kind") == kind)
    if len(matches) != 1:
        raise ValueError(f"Lambda gateway state kind {kind!r} is not unique")
    row = matches[0]
    return (
        _string(row.get("identity"), f"stateKinds.{kind}.identity"),
        _string(row.get("lineageIdentity"), f"stateKinds.{kind}.lineageIdentity"),
    )


def _states(document: dict[str, object]) -> StateRegistry:
    physical = _object(document.get("physical"), "physical")
    gate = _object(physical.get("contractGate"), "physical.contractGate")
    value = gate.get("stateKinds")
    if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
        raise ValueError("Lambda gateway stateKinds are not object rows")
    rows = tuple(value)
    if len(rows) != 15:
        raise ValueError("Lambda gateway stateKinds cardinality differs from schema")
    registered = _state_coordinates(rows, "registered")
    provisional = _state_coordinates(rows, "provisional")
    descriptor_capture = _state_coordinates(rows, "descriptor-closed-after-capture")
    descriptor_enumeration = _state_coordinates(rows, "descriptor-closed-after-enumeration")
    file_stable = _state_coordinates(rows, "file-capture-stable")
    file_drifted = _state_coordinates(rows, "file-capture-drifted")
    directory_stable = _state_coordinates(rows, "directory-enumeration-stable")
    directory_drifted = _state_coordinates(rows, "directory-enumeration-drifted")
    revision_captured = _state_coordinates(rows, "revision-provisional-captured")
    revision_incomplete = _state_coordinates(rows, "revision-provisional-incomplete")
    revision_drifted = _state_coordinates(rows, "revision-provisional-drifted")
    timestamp_stale = _state_coordinates(rows, "timestamp-stale")
    timestamp_current = _state_coordinates(rows, "timestamp-current-unverified")
    external_observed = _state_coordinates(rows, "external-product-observed")
    python_absent = _state_coordinates(rows, "python-semantics-absent")
    return StateRegistry(
        registered=Registered(*registered),
        provisional=Provisional(*provisional),
        descriptor_closed_after_capture=DescriptorClosedAfterCapture(*descriptor_capture),
        descriptor_closed_after_enumeration=DescriptorClosedAfterEnumeration(*descriptor_enumeration),
        file_capture_stable=FileCaptureStable(*file_stable),
        file_capture_drifted=FileCaptureDrifted(*file_drifted),
        directory_enumeration_stable=DirectoryEnumerationStable(*directory_stable),
        directory_enumeration_drifted=DirectoryEnumerationDrifted(*directory_drifted),
        revision_provisional_captured=RevisionProvisionalCaptured(*revision_captured),
        revision_provisional_incomplete=RevisionProvisionalIncomplete(*revision_incomplete),
        revision_provisional_drifted=RevisionProvisionalDrifted(*revision_drifted),
        timestamp_stale=TimestampStale(*timestamp_stale),
        timestamp_current_unverified=TimestampCurrentUnverified(*timestamp_current),
        external_product_observed=ExternalProductObserved(*external_observed),
        python_semantics_absent=PythonSemanticsAbsent(*python_absent),
    )


def _transport(
    rows: tuple[dict[str, object], ...],
    kind: str,
) -> dict[str, object]:
    matches = tuple(row for row in rows if row.get("kind") == kind)
    if len(matches) != 1:
        raise ValueError(f"Lambda gateway transport kind {kind!r} is not unique")
    return matches[0]


def _transports(document: dict[str, object]) -> tuple[dict[str, object], ...]:
    value = document.get("transports")
    if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
        raise ValueError("Lambda gateway transports are not object rows")
    return tuple(value)


def _implementation(document: dict[str, object]) -> Implementation:
    value = _object(document.get("implementation"), "implementation")
    return Implementation(
        identity=_string(value.get("identity"), "implementation.identity"),
        main_class=_string(value.get("mainClass"), "implementation.mainClass"),
        evaluator=_string(value.get("evaluator"), "implementation.evaluator"),
        digest_port=_string(value.get("digestPort"), "implementation.digestPort"),
    )


def _laws(document: dict[str, object], states: StateRegistry) -> Laws:
    value = _object(document.get("laws"), "laws")
    if value.get("pythonSemantics") is not False:
        raise ValueError("laws.pythonSemantics must be the registered absence value")
    return Laws(
        evaluation_authority=_string(
            value.get("evaluationAuthority"),
            "laws.evaluationAuthority",
        ),
        python_semantics=states.python_semantics_absent,
    )


def _artifact(document: dict[str, object]) -> Artifact:
    physical = _object(document.get("physical"), "physical")
    value = _object(physical.get("artifact"), "physical.artifact")
    return Artifact(
        request_schema_identity=_string(
            value.get("requestSchemaIdentity"),
            "physical.artifact.requestSchemaIdentity",
        ),
        response_schema_identity=_string(
            value.get("responseSchemaIdentity"),
            "physical.artifact.responseSchemaIdentity",
        ),
        framing_identity=_string(
            value.get("framingIdentity"),
            "physical.artifact.framingIdentity",
        ),
    )


def _host_octet_projection(
    document: dict[str, object],
    states: StateRegistry,
) -> HostOctetProjection:
    physical = _object(document.get("physical"), "physical")
    host = _object(physical.get("host"), "physical.host")
    octet = _object(host.get("octet"), "physical.host.octet")
    value = _object(octet.get("projection"), "physical.host.octet.projection")
    return HostOctetProjection(
        identity=_string(value.get("identity"), "projection.identity"),
        byte_schema_identity=_string(value.get("byteSchemaIdentity"), "projection.byteSchemaIdentity"),
        byte_schema_coordinate=_string(value.get("byteSchemaCoordinate"), "projection.byteSchemaCoordinate"),
        framing_identity=_string(value.get("framingIdentity"), "projection.framingIdentity"),
        bit_width=_integer(value.get("bitWidth"), "projection.bitWidth"),
        bit_order_identity=_string(value.get("bitOrderIdentity"), "projection.bitOrderIdentity"),
        bit_order_coordinate=_string(value.get("bitOrderCoordinate"), "projection.bitOrderCoordinate"),
        byte_order_identity=_string(value.get("byteOrderIdentity"), "projection.byteOrderIdentity"),
        byte_order_coordinate=_string(value.get("byteOrderCoordinate"), "projection.byteOrderCoordinate"),
        schema_revision_reference_identity=_string(value.get("schemaRevisionReferenceIdentity"), "projection.schemaRevisionReferenceIdentity"),
        schema_revision_reference_coordinate=_string(value.get("schemaRevisionReferenceCoordinate"), "projection.schemaRevisionReferenceCoordinate"),
        schema_revision_state=_provisional(value.get("schemaRevisionState"), "projection.schemaRevisionState", states),
        schema_revision_evidence_identity=_string(value.get("schemaRevisionEvidenceIdentity"), "projection.schemaRevisionEvidenceIdentity"),
        provenance_identity=_string(value.get("provenanceIdentity"), "projection.provenanceIdentity"),
        provenance_coordinate=_string(value.get("provenanceCoordinate"), "projection.provenanceCoordinate"),
        provenance_state=_provisional(value.get("provenanceState"), "projection.provenanceState", states),
        runtime_shoe=_string(value.get("runtimeShoe"), "projection.runtimeShoe"),
        encoding_identity=_string(value.get("encodingIdentity"), "projection.encodingIdentity"),
        decoding_identity=_string(value.get("decodingIdentity"), "projection.decodingIdentity"),
        comparison_identity=_string(value.get("comparisonIdentity"), "projection.comparisonIdentity"),
        text_codec_identity=_string(value.get("textCodecIdentity"), "projection.textCodecIdentity"),
        document_codec_identity=_string(value.get("documentCodecIdentity"), "projection.documentCodecIdentity"),
        digest_algorithm_identity=_string(value.get("digestAlgorithmIdentity"), "projection.digestAlgorithmIdentity"),
        digest_algorithm_coordinate=_string(value.get("digestAlgorithmCoordinate"), "projection.digestAlgorithmCoordinate"),
        digest_provider_coordinate=_string(value.get("digestProviderCoordinate"), "projection.digestProviderCoordinate"),
        digest_host_spelling=_string(value.get("digestHostSpelling"), "projection.digestHostSpelling"),
        invalid_document_issue_identity=_string(value.get("invalidDocumentIssueIdentity"), "projection.invalidDocumentIssueIdentity"),
        state=_provisional(value.get("state"), "projection.state", states),
        gap_identity=_string(value.get("gapIdentity"), "projection.gapIdentity"),
    )


def _contract_gate(
    document: dict[str, object],
    states: StateRegistry,
) -> ContractGateRegistration:
    physical = _object(document.get("physical"), "physical")
    gate = _object(physical.get("contractGate"), "physical.contractGate")
    capture = _object(gate.get("capture"), "physical.contractGate.capture")
    relations = _object(capture.get("relationIdentities"), "capture.relationIdentities")
    return ContractGateRegistration(
        identity=_string(gate.get("identity"), "physical.contractGate.identity"),
        states=states,
        capture=CaptureRegistration(
            attempt_lineage_identity=_string(capture.get("attemptLineageIdentity"), "capture.attemptLineageIdentity"),
            descriptor_opened_description_relation_identity=_string(relations.get("descriptorOpenedDescription"), "capture.relationIdentities.descriptorOpenedDescription"),
            opened_description_inode_relation_identity=_string(relations.get("openedDescriptionInode"), "capture.relationIdentities.openedDescriptionInode"),
            opened_description_kernel_identity_gap_identity=_string(capture.get("openedDescriptionKernelIdentityGapIdentity"), "capture.openedDescriptionKernelIdentityGapIdentity"),
            non_atomic_snapshot_gap_identity=_string(capture.get("nonAtomicSnapshotGapIdentity"), "capture.nonAtomicSnapshotGapIdentity"),
            entry_stat_unavailable_gap_identity=_string(capture.get("entryStatUnavailableGapIdentity"), "capture.entryStatUnavailableGapIdentity"),
            symbolic_link_payload_not_captured_gap_identity=_string(capture.get("symbolicLinkPayloadNotCapturedGapIdentity"), "capture.symbolicLinkPayloadNotCapturedGapIdentity"),
            directory_payload_not_captured_gap_identity=_string(capture.get("directoryPayloadNotCapturedGapIdentity"), "capture.directoryPayloadNotCapturedGapIdentity"),
            file_payload_not_captured_gap_identity=_string(capture.get("filePayloadNotCapturedGapIdentity"), "capture.filePayloadNotCapturedGapIdentity"),
            file_drift_gap_identity=_string(capture.get("fileDriftGapIdentity"), "capture.fileDriftGapIdentity"),
            special_payload_not_captured_gap_identity=_string(capture.get("specialPayloadNotCapturedGapIdentity"), "capture.specialPayloadNotCapturedGapIdentity"),
            directory_drift_gap_identity=_string(capture.get("directoryDriftGapIdentity"), "capture.directoryDriftGapIdentity"),
            file_revision_drift_gap_identity=_string(capture.get("fileRevisionDriftGapIdentity"), "capture.fileRevisionDriftGapIdentity"),
        ),
    )


def discover(repository: Locator) -> Contract:
    repository_path = Path(os.path.abspath(repository.host_path.lexical))
    root = repository_path / "contracts" / "morphisms"
    index = _object(_read(root / "contract-set.json"), "contract-set")
    artifacts = index.get("artifacts")
    if not isinstance(artifacts, list):
        raise ValueError("contract set artifacts are not a sequence")
    registrations = tuple(
        row
        for row in artifacts
        if isinstance(row, dict) and row.get("kind") == "lambda-runtime-gateway"
    )
    if len(registrations) != 1:
        raise ValueError("contract set must register exactly one lambda-runtime-gateway")
    registration = registrations[0]
    lexical = _string(registration.get("path"), "contract-set.lambda.path")
    identity = _string(registration.get("id"), "contract-set.lambda.id")
    path = (root / lexical).resolve()
    path.relative_to(root.resolve())
    document = _object(_read(path), "lambda-runtime-gateway")
    if _string(document.get("id"), "gateway.id") != identity:
        raise ValueError("Lambda gateway registration and document identity differ")

    transports = _transports(document)
    process = _transport(transports, "process-file")
    process_gaps = process.get("gapIdentities")
    if not isinstance(process_gaps, list) or not all(
        isinstance(item, str) and item for item in process_gaps
    ):
        raise ValueError("process-file gap identities are incomplete")
    readback = _transport(transports, "receipt-readback")
    mcp = _transport(transports, "mcp-tool")
    states = _states(document)
    return Contract(
        identity=identity,
        locator=admit(str(path), repository.host_path.registration),
        implementation=_implementation(document),
        laws=_laws(document, states),
        artifact=_artifact(document),
        contract_gate=_contract_gate(document, states),
        host_octet_projection=_host_octet_projection(document, states),
        process_file=ProcessFileRegistration(
            capability=_string(process.get("capability"), "process-file.capability"),
            runtime_shoe=_string(process.get("runtimeShoe"), "process-file.runtimeShoe"),
            state=_registered(process.get("state"), "process-file.state", states),
            operation_state=_provisional(process.get("operationState"), "process-file.operationState", states),
            gap_identities=tuple(process_gaps),
        ),
        receipt_readback=ReceiptReadbackRegistration(
            capability=_string(readback.get("capability"), "receipt-readback.capability"),
            state=_registered(readback.get("state"), "receipt-readback.state", states),
            request_locator=admit(
                str(repository_path / _string(readback.get("requestPath"), "receipt-readback.requestPath")),
                repository.host_path.registration,
            ),
            response_locator=admit(
                str(repository_path / _string(readback.get("responsePath"), "receipt-readback.responsePath")),
                repository.host_path.registration,
            ),
        ),
        mcp_tool=McpToolRegistration(
            capability=_string(mcp.get("capability"), "mcp-tool.capability"),
            state=_provisional(mcp.get("state"), "mcp-tool.state", states),
            tool=_string(mcp.get("tool"), "mcp-tool.tool"),
            argument_field=_string(mcp.get("argumentField"), "mcp-tool.argumentField"),
        ),
    )
