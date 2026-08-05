from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.file.capture.effect.rejected.identity.value import VALUE as REJECTED
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.serialize.project import PROJECT as SERIALIZE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.value import Value as Stability
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    same_metadata = SERIALIZE(value.pre).payload == SERIALIZE(value.post).payload
    whole_payload = value.accumulator.bounded_identity.payload == b"unbounded" and len(value.accumulator.payload.payload) == value.post.size.value
    stable = same_metadata and whole_payload
    reason = b"same-descriptor-pre-post-and-whole-payload" if stable else b"metadata-drift-or-incomplete-payload"
    result = Stability(ByteVector(b"stable" if stable else b"unstable"), ByteVector(reason))
    return Frame(Output(result), Effect(ByteVector(APPLIED if stable else REJECTED)))
