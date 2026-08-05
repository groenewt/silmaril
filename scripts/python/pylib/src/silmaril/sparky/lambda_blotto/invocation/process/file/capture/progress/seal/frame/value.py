from config.constants.lambda_blotto.invocation.process.file.capture.progress.seal.frame.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.progress.seal.frame.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.seal.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.seal.output.value import Value as Output

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    output: Output
    effect: Effect
