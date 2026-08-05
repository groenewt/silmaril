from config.constants.lambda_blotto.invocation.process.file.capture.progress.seal.output.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.progress.seal.output.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.plan.value import Value as Plan
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.receipt.value import Value as Receipt

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    receipt: Receipt
    plan: Plan
