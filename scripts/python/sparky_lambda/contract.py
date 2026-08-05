"""Pure exact registered coordinates for the Scala Lambda gateway."""
#```python
#EXAMPLE OF OUR FUNCTIONAL RESTRICTION. LITERAL AND STRICT "ONE INPUT,One output"-> IF IT Cannot meet this criterion (this applies to any function anywhere where it receives ONE DEFINED TYPE PER iNPUT, THEN OUTPUT)< IF THIS CANNOT BE ACHIEVED WE CANNOT "CONSTRUCT A FRAME" AROUND OUR BYTE STREAM NOR CAN WE EVEN CLAIM "SUCCESS". PLEASE BE MINDFUL I HAVE FULL OVERVIEW OF THE CODEBASE AND ITS RATHER DISAPPOINT HOW MUCH LEXICAL, SEMANTIC AND TOPOLOGICAL RICHNESS WE LOSE BC THIS RULE IS NOT STRICTLY (and LIKE OUR CONFIG/{CONSTANTS,GATE *THERE ARE SO MANY JAVE VIOLATIONS!* } enforced. BAD RULE ENFORCE MENT IS WHAT GETS US KILLED
#T=Typevar('ANormalizedTypeUrn')
#X=Typevar('BNormalizedTypeUrn')
#Y=Typevar('CNormalizedTypeUrn')
#DEF somefunction(sometypekindbytestream:T)-> (someoutputsometypekindbytestream:X, someerroroutputsometypekindbytestream:Y):
#return SOMECALLABLE(sometypekindbytestream)
#T->(X,Y) IS A EXTREMELY STRICT HYGEINE RULE FOR IDK MAYBE 1) TO ACCOMPLISH MY FUCKING GOAL 2) TO FUCKING ENSURE PROPER SUBATOMIC MODELING 3) TO AVOID ANY AND ALL "BULLSHJT" bc like it has one parameter in, or it doesnt ;;;  It has only an effect (and implictly _error)( or it doesnt we are nto returning/workign with underfine sets. ARE URN TYPE DRIVE SWALLOWS ALL TO CREATE YONEDA POINTS (AGAIN SOMETHIGN YOU CAN SEARCH!)
#MORE AT /home/tristan/site_stage/cpg-highway/docs/campaigns/unary-byte-frame-law.md
#```

from __future__ import annotations

from dataclasses import dataclass

from .kind import PythonSemanticsAbsent, Provisional, Registered, StateRegistry
from .locator import Locator


@dataclass(frozen=True, slots=True)
class Implementation:
    identity: str
    main_class: str
    evaluator: str
    digest_port: str


@dataclass(frozen=True, slots=True)
class Laws:
    evaluation_authority: str
    python_semantics: PythonSemanticsAbsent


@dataclass(frozen=True, slots=True)
class Artifact:
    request_schema_identity: str
    response_schema_identity: str
    framing_identity: str


@dataclass(frozen=True, slots=True)
class HostOctetProjection:
    identity: str
    byte_schema_identity: str
    byte_schema_coordinate: str
    framing_identity: str
    bit_width: int
    bit_order_identity: str
    bit_order_coordinate: str
    byte_order_identity: str
    byte_order_coordinate: str
    schema_revision_reference_identity: str
    schema_revision_reference_coordinate: str
    schema_revision_state: Provisional
    schema_revision_evidence_identity: str
    provenance_identity: str
    provenance_coordinate: str
    provenance_state: Provisional
    runtime_shoe: str
    encoding_identity: str
    decoding_identity: str
    comparison_identity: str
    text_codec_identity: str
    document_codec_identity: str
    digest_algorithm_identity: str
    digest_algorithm_coordinate: str
    digest_provider_coordinate: str
    digest_host_spelling: str
    invalid_document_issue_identity: str
    state: Provisional
    gap_identity: str


@dataclass(frozen=True, slots=True)
class ProcessFileRegistration:
    capability: str
    runtime_shoe: str
    state: Registered
    operation_state: Provisional
    gap_identities: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ReceiptReadbackRegistration:
    capability: str
    state: Registered
    request_locator: Locator
    response_locator: Locator


@dataclass(frozen=True, slots=True)
class McpToolRegistration:
    capability: str
    state: Provisional
    tool: str
    argument_field: str


@dataclass(frozen=True, slots=True)
class CaptureRegistration:
    attempt_lineage_identity: str
    descriptor_opened_description_relation_identity: str
    opened_description_inode_relation_identity: str
    opened_description_kernel_identity_gap_identity: str
    non_atomic_snapshot_gap_identity: str
    entry_stat_unavailable_gap_identity: str
    symbolic_link_payload_not_captured_gap_identity: str
    directory_payload_not_captured_gap_identity: str
    file_payload_not_captured_gap_identity: str
    file_drift_gap_identity: str
    special_payload_not_captured_gap_identity: str
    directory_drift_gap_identity: str
    file_revision_drift_gap_identity: str


@dataclass(frozen=True, slots=True)
class ContractGateRegistration:
    identity: str
    states: StateRegistry
    capture: CaptureRegistration


@dataclass(frozen=True, slots=True)
class Contract:
    identity: str
    locator: Locator
    implementation: Implementation
    laws: Laws
    artifact: Artifact
    contract_gate: ContractGateRegistration
    host_octet_projection: HostOctetProjection
    process_file: ProcessFileRegistration
    receipt_readback: ReceiptReadbackRegistration
    mcp_tool: McpToolRegistration

    @classmethod
    def discover(cls, repository: Locator) -> "Contract":
        from .contract_gate.registration import discover

        return discover(repository)

    def require_capability(self, capability: str) -> None:
        registered = (
            self.process_file.capability,
            self.receipt_readback.capability,
            self.mcp_tool.capability,
        )
        if registered.count(capability) != 1:
            raise ValueError(f"gateway capability {capability!r} is not unique")
