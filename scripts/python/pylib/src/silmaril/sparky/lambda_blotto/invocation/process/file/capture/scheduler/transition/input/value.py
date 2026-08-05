from config.constants.lambda_blotto.invocation.process.file.capture.scheduler.transition.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.scheduler.transition.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.scheduler.transition.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.value import Value as State
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    state: State
    evidence_class: ByteVector
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
