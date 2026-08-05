from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.decision.value import Value as Decision
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.policy.decide.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.policy.decide.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.policy.decide.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.policy.decide.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    hidden = value.name.name.payload.startswith(b".")
    if value.policy.payload not in (b"include-all", b"exclude-hidden"):
        issue = Issue(ByteVector(b"invalid-hidden-policy"), value.policy)
        return Frame(Output(issue), Effect(ByteVector(REJECTED)))
    include = value.policy.payload == b"include-all" or not hidden
    evidence = b"hidden-included-explicitly" if hidden and include else b"hidden-excluded-explicitly" if hidden else b"visible-included"
    return Frame(Output(Decision(ByteVector(b"include" if include else b"exclude"), ByteVector(evidence))), Effect(ByteVector(APPLIED)))
