from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.accumulator.value import Value as Accumulator
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    remaining = value.maximum_bytes.value - len(value.accumulator.payload.payload)
    appended = value.chunk.payload.payload[:remaining]
    payload = value.accumulator.payload.payload + appended
    bounded = b"bounded" if len(payload) >= value.maximum_bytes.value and value.expected_size.value > len(payload) else b"unbounded"
    result = Accumulator(ByteVector(payload), Natural(value.accumulator.chunk_count.value + 1), ByteVector(bounded))
    return Frame(Output(result), Effect(ByteVector(APPLIED)))
