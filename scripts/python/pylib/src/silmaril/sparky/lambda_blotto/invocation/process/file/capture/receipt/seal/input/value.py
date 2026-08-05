from config.constants.lambda_blotto.invocation.process.file.capture.receipt.seal.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.receipt.seal.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.receipt.seal.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.request.value import Value as Request
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.value import Value as Revision
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.value import Value as Stability

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    request: Request
    entry: Metadata
    pre: Metadata
    post: Metadata
    accumulator: Accumulator
    stability: Stability
    revision: Revision
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
