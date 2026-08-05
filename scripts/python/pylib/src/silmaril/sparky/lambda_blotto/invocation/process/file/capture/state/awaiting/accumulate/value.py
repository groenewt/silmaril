from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.opened.file.description.occurrence.value import Value as Opened
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.chunk.value import Value as Chunk
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.request.value import Value as Request

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    request: Request
    entry: Metadata
    opened: Opened
    pre: Metadata
    accumulator: Accumulator
    chunk: Chunk
