from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.file.capture.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.readback.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.readback.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.readback.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.readback.output.value import Value as Output
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    observed = ByteVector(SHA256(value.receipt.serialized.payload).digest())
    accepted = observed.payload == value.receipt.digest.payload
    return Frame(Output(ByteVector(b"accepted" if accepted else b"rejected"), observed), Effect(ByteVector(APPLIED if accepted else REJECTED)))
