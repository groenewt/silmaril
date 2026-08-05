"""Pure exact evidence for a registered Scala Lambda process occurrence."""
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

from .artifact import Request, Response
from .locator import Locator
from .kind import (
    DescriptorClosedAfterCapture,
    DescriptorClosedAfterEnumeration,
    DirectoryEnumerationDrifted,
    DirectoryEnumerationStable,
    ExternalProductObserved,
    FileCaptureDrifted,
    FileCaptureStable,
    Provisional,
    Registered,
    RevisionProvisionalCaptured,
    RevisionProvisionalDrifted,
    RevisionProvisionalIncomplete,
    TimestampCurrentUnverified,
    TimestampStale,
)


@dataclass(frozen=True, slots=True)
class CaptureAttempt:
    identity: str
    lineage_identity: str


@dataclass(frozen=True, slots=True)
class DescriptorObservation:
    capture_attempt: CaptureAttempt
    process_local_number: int
    lifecycle: DescriptorClosedAfterCapture | DescriptorClosedAfterEnumeration


@dataclass(frozen=True, slots=True)
class RegularInode:
    device: int
    number: int


@dataclass(frozen=True, slots=True)
class DirectoryInode:
    device: int
    number: int


@dataclass(frozen=True, slots=True)
class SymbolicLinkInode:
    device: int
    number: int


@dataclass(frozen=True, slots=True)
class SpecialInode:
    device: int
    number: int


Inode = RegularInode | DirectoryInode | SymbolicLinkInode | SpecialInode


@dataclass(frozen=True, slots=True)
class OpenedFileDescriptionContext:
    """Capture occurrence context, never a fabricated kernel table identity."""

    capture_attempt: CaptureAttempt
    locator: Locator
    descriptor_process_local_number: int
    evidence_state: Provisional


@dataclass(frozen=True, slots=True)
class OpenedFileDescriptionIdentityEvidence:
    context: OpenedFileDescriptionContext
    gap_identity: str
    evidence: str


@dataclass(frozen=True, slots=True)
class OpenedFileDescriptionOccurrence:
    context: OpenedFileDescriptionContext
    identity_evidence: OpenedFileDescriptionIdentityEvidence
    offset_pre: int
    offset_post: int
    status_flags: int


@dataclass(frozen=True, slots=True)
class DescriptorOpenedDescriptionAssociation:
    relation_identity: str
    descriptor: DescriptorObservation
    opened_description: OpenedFileDescriptionOccurrence


@dataclass(frozen=True, slots=True)
class OpenedDescriptionInodeAssociation:
    relation_identity: str
    opened_description: OpenedFileDescriptionOccurrence
    inode: Inode


@dataclass(frozen=True, slots=True)
class Metadata:
    inode: Inode
    size: int
    modified_ns: int
    changed_ns: int
    link_count: int
    mode: int


@dataclass(frozen=True, slots=True)
class DigestBinding:
    algorithm_identity: str
    algorithm_coordinate: str
    provider_coordinate: str
    host_spelling: str


@dataclass(frozen=True, slots=True)
class FileObservation:
    locator: Locator
    descriptor: DescriptorObservation
    opened_description: OpenedFileDescriptionOccurrence
    descriptor_opened_description: DescriptorOpenedDescriptionAssociation
    opened_description_inode: OpenedDescriptionInodeAssociation
    entry_pre: Metadata
    pre: Metadata
    post: Metadata
    host_octet_count: int
    digest: DigestBinding
    payload_digest: str
    state: FileCaptureStable | FileCaptureDrifted


@dataclass(frozen=True, slots=True)
class DirectoryFrame:
    locator: Locator
    descriptor: DescriptorObservation
    opened_description: OpenedFileDescriptionOccurrence
    descriptor_opened_description: DescriptorOpenedDescriptionAssociation
    opened_description_inode: OpenedDescriptionInodeAssociation
    entry_pre: Metadata
    pre: Metadata
    post: Metadata
    entry_count: int
    state: DirectoryEnumerationStable | DirectoryEnumerationDrifted


@dataclass(frozen=True, slots=True)
class CaptureGap:
    identity: str
    locator: Locator
    evidence: str


@dataclass(frozen=True, slots=True)
class Revision:
    locator: Locator
    digest: DigestBinding
    revision_digest: str
    latest_modified_ns: int
    entry_count: int
    state: RevisionProvisionalCaptured | RevisionProvisionalIncomplete | RevisionProvisionalDrifted
    files: tuple[FileObservation, ...]
    directories: tuple[DirectoryFrame, ...]
    gaps: tuple[CaptureGap, ...]


@dataclass(frozen=True, slots=True)
class OwnedDependencyRevision:
    source: Revision
    product: Revision
    state: TimestampStale | TimestampCurrentUnverified


@dataclass(frozen=True, slots=True)
class ExternalDependencyRevision:
    product: Revision
    state: ExternalProductObserved


@dataclass(frozen=True, slots=True)
class RuntimeEvidence:
    state: Provisional
    gap_identities: tuple[str, ...]
    bsp: Revision
    invocation_sources: Revision
    owned_dependencies: tuple[OwnedDependencyRevision, ...]
    external_dependencies: tuple[ExternalDependencyRevision, ...]


@dataclass(frozen=True, slots=True)
class Execution:
    capability: str
    runtime_shoe: str
    request: Request
    response: Response
    exit_code: int
    evidence: RuntimeEvidence
    request_observation: FileObservation
    response_observation: FileObservation | CaptureGap


class Failure(RuntimeError):
    def __init__(self, execution: Execution) -> None:
        self.execution = execution
        super().__init__(
            "registered Scala Lambda gateway failed: "
            "exit="
            f"{execution.exit_code} "
            f"response={execution.response.locator.canonical.value}"
        )


@dataclass(frozen=True, slots=True)
class ReceiptReadback:
    capability: str
    state: Registered
    request: Request
    response: Response
    request_observation: FileObservation
    response_observation: FileObservation


@dataclass(frozen=True, slots=True)
class McpTool:
    capability: str
    state: Provisional
    tool: str
    argument_field: str
