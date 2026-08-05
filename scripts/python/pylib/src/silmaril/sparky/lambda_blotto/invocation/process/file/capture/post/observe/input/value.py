from config.constants.lambda_blotto.invocation.process.file.capture.post.observe.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.post.observe.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.post.observe.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.opened.file.description.occurrence.value import Value as Opened

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    opened: Opened
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
