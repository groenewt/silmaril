from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.output.value import Value as Output
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    observed = ByteVector(SHA256(value.receipt.serialized.payload + value.receipt.revision.digest.payload).digest())
    accepted = observed.payload == value.receipt.digest.payload
    return Frame(Output(ByteVector(b"accepted" if accepted else b"rejected"), observed), Effect(ByteVector(APPLIED if accepted else REJECTED)))
