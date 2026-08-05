from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.request.value import Value as Request
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.value import Value as Stability

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    request: Request
    entry: Metadata
    pre: Metadata
    accumulator: Accumulator
    post: Metadata
    stability: Stability
