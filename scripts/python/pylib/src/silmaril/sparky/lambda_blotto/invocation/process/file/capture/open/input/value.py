from config.constants.lambda_blotto.invocation.process.file.capture.open.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.open.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.open.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.request.value import Value as Request

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    request: Request
    entry: Metadata
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
