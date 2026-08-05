from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.file.capture.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.serialize.project import PROJECT as SERIALIZE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.derive.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.derive.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.derive.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.derive.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.value import Value as Revision
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    if value.stability.verdict.payload != b"stable":
        issue = Issue(ByteVector(b"unstable-capture"), value.stability.evidence)
        return Frame(Output(issue), Effect(ByteVector(REJECTED)))
    material = FIELD(SERIALIZE(value.pre)).payload + FIELD(SERIALIZE(value.post)).payload + FIELD(value.accumulator.payload).payload + FIELD(value.request.format_evidence).payload
    revision = Revision(ByteVector(SHA256(material).digest()), ByteVector(b"sha256"))
    return Frame(Output(revision), Effect(ByteVector(APPLIED)))
