from config.constants.lambda_blotto.invocation.process.file.capture.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.constants.lambda_blotto.invocation.process.file.capture.stability.decide.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.stability.decide.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.stability.decide.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.accumulator.value import Value as Accumulator

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    pre: Metadata
    post: Metadata
    accumulator: Accumulator
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
