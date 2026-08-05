from config.constants.lambda_blotto.invocation.process.file.capture.gap.descriptor.linearity.value import VALUE as LINEARITY_GAP
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    number: Natural
    linearity_gap = LINEARITY_GAP
