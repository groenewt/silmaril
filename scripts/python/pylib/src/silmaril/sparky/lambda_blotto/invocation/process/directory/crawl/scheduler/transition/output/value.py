from config.constants.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.output.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.output.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.value import Value as State
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.transition.receipt.value import Value as TransitionReceipt

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    state: State
    receipt: TransitionReceipt
