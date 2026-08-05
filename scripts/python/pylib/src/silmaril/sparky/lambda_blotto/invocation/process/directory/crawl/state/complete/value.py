from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.value import Value as DirectoryFrame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.output.value import Value as Readback
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.value import Value as Receipt

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: DirectoryFrame
    receipt: Receipt
    readback: Readback
