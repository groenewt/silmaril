from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.readback.output.value import Value as Readback
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.value import Value as Receipt

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    receipt: Receipt
    readback: Readback
