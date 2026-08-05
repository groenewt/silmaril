from config.constants.lambda_blotto.invocation.process.file.capture.gap.format.evidence.value import VALUE as FORMAT_GAP
from config.constants.lambda_blotto.invocation.process.file.capture.gap.payload.bound.value import VALUE as PAYLOAD_GAP
from config.constants.lambda_blotto.invocation.process.file.capture.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.provenance.value import Value as Provenance
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.locator.value import Value as Locator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    locator: Locator
    provenance: Provenance
    attempt: ByteVector
    chunk_size: Natural
    maximum_bytes: Natural
    format_evidence: ByteVector
    source_evidence = SOURCE_EVIDENCE
    payload_gap = PAYLOAD_GAP
    format_gap = FORMAT_GAP
