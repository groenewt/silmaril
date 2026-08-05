from config.constants.lambda_blotto.invocation.process.file.capture.gap.descriptor.linearity.value import VALUE as LINEARITY_GAP
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.request.value import Value as Request
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.descriptor.occurrence.value import Value as Descriptor

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    descriptor: Descriptor
    request: Request
    linearity_gap = LINEARITY_GAP
