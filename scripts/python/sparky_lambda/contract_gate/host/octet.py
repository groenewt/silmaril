"""Named provisional width-eight host projection for invocation artifacts."""

from __future__ import annotations
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

import json
from dataclasses import dataclass
from pathlib import Path

from ...artifact import Request, Response
from ...contract import Contract, ContractGateRegistration
from ...kind import Provisional
from ...locator import Locator
from ...transport import DigestBinding, FileObservation
from ..capture import CapturedFileDrifted, CapturedFileStable, file


@dataclass(frozen=True, slots=True)
class Projection:
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
    digest: DigestBinding
    invalid_document_issue_identity: str
    state: Provisional
    gap_identity: str
    contract_gate: ContractGateRegistration

    @classmethod
    def registered(cls, contract: Contract) -> "Projection":
        value = contract.host_octet_projection
        return cls(
            identity=value.identity,
            byte_schema_identity=value.byte_schema_identity,
            byte_schema_coordinate=value.byte_schema_coordinate,
            framing_identity=value.framing_identity,
            bit_width=value.bit_width,
            bit_order_identity=value.bit_order_identity,
            bit_order_coordinate=value.bit_order_coordinate,
            byte_order_identity=value.byte_order_identity,
            byte_order_coordinate=value.byte_order_coordinate,
            schema_revision_reference_identity=value.schema_revision_reference_identity,
            schema_revision_reference_coordinate=value.schema_revision_reference_coordinate,
            schema_revision_state=value.schema_revision_state,
            schema_revision_evidence_identity=value.schema_revision_evidence_identity,
            provenance_identity=value.provenance_identity,
            provenance_coordinate=value.provenance_coordinate,
            provenance_state=value.provenance_state,
            runtime_shoe=value.runtime_shoe,
            encoding_identity=value.encoding_identity,
            decoding_identity=value.decoding_identity,
            comparison_identity=value.comparison_identity,
            text_codec_identity=value.text_codec_identity,
            document_codec_identity=value.document_codec_identity,
            digest=DigestBinding(
                algorithm_identity=value.digest_algorithm_identity,
                algorithm_coordinate=value.digest_algorithm_coordinate,
                provider_coordinate=value.digest_provider_coordinate,
                host_spelling=value.digest_host_spelling,
            ),
            invalid_document_issue_identity=value.invalid_document_issue_identity,
            state=value.state,
            gap_identity=value.gap_identity,
            contract_gate=contract.contract_gate,
        )


@dataclass(frozen=True, slots=True)
class Encoding:
    projection: Projection
    operation_identity: str
    locator: Locator
    schema_identity: str
    framing_identity: str
    text_codec_identity: str
    document_codec_identity: str
    host_octet_count: int
    digest: DigestBinding
    payload_digest: str
    observation: FileObservation


@dataclass(frozen=True, slots=True)
class DecodingAccepted:
    projection: Projection
    operation_identity: str
    locator: Locator
    schema_identity: str
    framing_identity: str
    text_codec_identity: str
    document_codec_identity: str
    host_octet_count: int
    digest: DigestBinding
    payload_digest: str
    observation: FileObservation


@dataclass(frozen=True, slots=True)
class DecodingRejected:
    projection: Projection
    operation_identity: str
    locator: Locator
    schema_identity: str
    framing_identity: str
    text_codec_identity: str
    document_codec_identity: str
    host_octet_count: int
    digest: DigestBinding
    payload_digest: str
    issue_identity: str
    issue_evidence: str
    observation: FileObservation


@dataclass(frozen=True, slots=True)
class EncodingEqual:
    projection: Projection
    operation_identity: str
    left: Encoding
    right: Encoding


@dataclass(frozen=True, slots=True)
class EncodingUnequal:
    projection: Projection
    operation_identity: str
    left: Encoding
    right: Encoding


def _unique(source: Path):
    def unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
        value: dict[str, object] = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"duplicate JSON coordinate {key!r} in {source}")
            value[key] = item
        return value

    return unique


def _decode_document(payload: bytes, locator: Locator) -> None:
    json.loads(
        payload.decode("utf-8"),
        object_pairs_hook=_unique(Path(locator.host_path.lexical)),
    )


def _capture(
    artifact: Request | Response,
    projection: Projection,
) -> CapturedFileStable:
    if artifact.framing_identity != projection.framing_identity:
        raise ValueError("artifact framing differs from host octet projection")
    captured = file(
        artifact.locator,
        projection.digest,
        projection.contract_gate,
    )
    if isinstance(captured, CapturedFileDrifted):
        raise ValueError(f"{captured.gap_identity}: {captured.gap_evidence}")
    if captured.observation.digest != projection.digest:
        raise ValueError("host octet digest binding differs from ContractGate capture")
    return captured


def _encoding(
    artifact: Request | Response,
    projection: Projection,
    captured: CapturedFileStable,
) -> Encoding:
    observation = captured.observation
    return Encoding(
        projection=projection,
        operation_identity=projection.encoding_identity,
        locator=artifact.locator,
        schema_identity=artifact.schema_identity,
        framing_identity=artifact.framing_identity,
        text_codec_identity=projection.text_codec_identity,
        document_codec_identity=projection.document_codec_identity,
        host_octet_count=observation.host_octet_count,
        digest=observation.digest,
        payload_digest=observation.payload_digest,
        observation=observation,
    )


def observe_encoding(artifact: Request | Response, projection: Projection) -> Encoding:
    """Observe one encoded artifact without claiming Python produced it."""

    return _encoding(artifact, projection, _capture(artifact, projection))


def decode(
    artifact: Request | Response,
    projection: Projection,
) -> DecodingAccepted | DecodingRejected:
    """Return an exact receipt; decoded JSON syntax never leaves this adapter."""

    captured = _capture(artifact, projection)
    payload = captured.payload
    observation = captured.observation
    try:
        _decode_document(payload, artifact.locator)
    except (UnicodeError, ValueError) as issue:
        return DecodingRejected(
            projection=projection,
            operation_identity=projection.decoding_identity,
            locator=artifact.locator,
            schema_identity=artifact.schema_identity,
            framing_identity=artifact.framing_identity,
            text_codec_identity=projection.text_codec_identity,
            document_codec_identity=projection.document_codec_identity,
            host_octet_count=observation.host_octet_count,
            digest=observation.digest,
            payload_digest=observation.payload_digest,
            issue_identity=projection.invalid_document_issue_identity,
            issue_evidence=f"{type(issue).__name__}: {issue}",
            observation=observation,
        )
    return DecodingAccepted(
        projection=projection,
        operation_identity=projection.decoding_identity,
        locator=artifact.locator,
        schema_identity=artifact.schema_identity,
        framing_identity=artifact.framing_identity,
        text_codec_identity=projection.text_codec_identity,
        document_codec_identity=projection.document_codec_identity,
        host_octet_count=observation.host_octet_count,
        digest=observation.digest,
        payload_digest=observation.payload_digest,
        observation=observation,
    )


def equivalent(
    left: Request | Response,
    right: Request | Response,
    projection: Projection,
) -> EncodingEqual | EncodingUnequal:
    """Compare exact captured host-octet revisions, not decoded documents."""

    left_encoding = observe_encoding(left, projection)
    right_encoding = observe_encoding(right, projection)
    equal = (
        left_encoding.payload_digest == right_encoding.payload_digest
        and left_encoding.host_octet_count == right_encoding.host_octet_count
        and left_encoding.digest == right_encoding.digest
    )
    result = EncodingEqual if equal else EncodingUnequal
    return result(
        projection=projection,
        operation_identity=projection.comparison_identity,
        left=left_encoding,
        right=right_encoding,
    )
