from config.constants.lambda_blotto.invocation.process.file.capture.scheduler.transition.output.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.scheduler.transition.output.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.value import Value as State

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    state: State
