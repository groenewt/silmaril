from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.file.capture.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.os.read.value import VALUE as READ
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.conversion.os.error.project import PROJECT as ISSUE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.chunk.value import Value as Chunk
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.output.value import Value as Output
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    try:
        payload = READ(value.opened.descriptor.number.value, value.maximum_count.value)
        end = b"end" if payload == b"" else b"continue"
        return Frame(Output(Chunk(ByteVector(payload), ByteVector(end))), Effect(ByteVector(APPLIED)))
    except OSError as issue:
        return Frame(Output(ISSUE(issue)), Effect(ByteVector(REJECTED)))
