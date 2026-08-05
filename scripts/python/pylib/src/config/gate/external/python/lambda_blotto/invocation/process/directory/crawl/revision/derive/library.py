from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.serialize.project import PROJECT as SERIALIZE
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.value import Value as Revision
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    revision = Revision(ByteVector(SHA256(SERIALIZE(value.frame).payload).digest()), ByteVector(b"sha256"))
    return Frame(Output(revision), Effect(ByteVector(APPLIED)))
