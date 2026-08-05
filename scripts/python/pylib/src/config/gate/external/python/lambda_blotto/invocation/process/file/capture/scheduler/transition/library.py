from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.file.capture.effect.rejected.identity.value import VALUE as REJECTED
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.apply import apply as ACCUMULATE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.input.value import Value as AccumulateInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.close.apply import apply as CLOSE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.close.input.value import Value as CloseInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.entry.stat.apply import apply as ENTRY_STAT
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.entry.stat.input.value import Value as EntryInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.open.apply import apply as OPEN
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.open.input.value import Value as OpenInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.payload.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.post.observe.apply import apply as POST
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.post.observe.input.value import Value as PostInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.pre.observe.apply import apply as PRE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.pre.observe.input.value import Value as PreInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.apply import apply as READ
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.input.value import Value as ReadInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.readback.apply import apply as READBACK
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.readback.input.value import Value as ReadbackInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.seal.apply import apply as SEAL
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.seal.input.value import Value as SealInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.derive.apply import apply as REVISION
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.derive.input.value import Value as RevisionInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.apply import apply as STABILITY
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.input.value import Value as StabilityInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.accumulate.value import Value as AwaitingAccumulate
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.close.value import Value as AwaitingClose
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.entry.value import Value as AwaitingEntry
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.failure.close.value import Value as AwaitingFailureClose
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.open.value import Value as AwaitingOpen
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.post.value import Value as AwaitingPost
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.pre.value import Value as AwaitingPre
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.read.value import Value as AwaitingRead
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.readback.value import Value as AwaitingReadback
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.revision.value import Value as AwaitingRevision
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.seal.value import Value as AwaitingSeal
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.stability.value import Value as AwaitingStability
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.complete.value import Value as Complete
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.failed.value import Value as Failed
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def _frame(state, evidence, evidence_class) -> Frame:
    return Frame(Output(state), Effect(ByteVector(evidence), evidence_class))

def PROJECT(value: Input) -> Frame:
    state = value.state
    if isinstance(state, AwaitingEntry):
        if state.request.provenance.evidence_class.payload != value.evidence_class.payload:
            issue = Issue(ByteVector(b"scheduler-evidence-class-mismatch"), value.evidence_class)
            return _frame(Failed(issue), REJECTED, value.evidence_class)
        if state.request.chunk_size.value <= 0 or state.request.maximum_bytes.value <= 0:
            return _frame(Failed(Issue(ByteVector(b"invalid-bound"), ByteVector(b"chunk-size-and-maximum-bytes-must-be-positive"))), REJECTED, value.evidence_class)
        frame = ENTRY_STAT(EntryInput(state.request))
        return _frame(Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingOpen(state.request, frame.output.result), frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingOpen):
        frame = OPEN(OpenInput(state.request, state.entry))
        return _frame(Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingPre(state.request, state.entry, frame.output.result), frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingPre):
        frame = PRE(PreInput(state.opened))
        if isinstance(frame.output.result, Issue):
            return _frame(AwaitingFailureClose(state.opened, frame.output.result), frame.effect.evidence.payload, value.evidence_class)
        accumulator = Accumulator(ByteVector(b""), Natural(0), ByteVector(b"unbounded"))
        following = AwaitingPost(state.request, state.entry, state.opened, frame.output.result, accumulator) if frame.output.result.size.value == 0 else AwaitingRead(state.request, state.entry, state.opened, frame.output.result, accumulator)
        return _frame(following, frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingRead):
        remaining = state.request.maximum_bytes.value - len(state.accumulator.payload.payload)
        if remaining <= 0:
            issue = Issue(ByteVector(b"invalid-read-state"), ByteVector(b"no-capacity-remains-before-read"))
            return _frame(AwaitingFailureClose(state.opened, issue), REJECTED, value.evidence_class)
        frame = READ(ReadInput(state.opened, Natural(min(state.request.chunk_size.value, remaining))))
        if isinstance(frame.output.result, Issue):
            return _frame(AwaitingFailureClose(state.opened, frame.output.result), frame.effect.evidence.payload, value.evidence_class)
        following = AwaitingPost(state.request, state.entry, state.opened, state.pre, state.accumulator) if frame.output.result.end_identity.payload == b"end" else AwaitingAccumulate(state.request, state.entry, state.opened, state.pre, state.accumulator, frame.output.result)
        return _frame(following, frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingAccumulate):
        frame = ACCUMULATE(AccumulateInput(state.accumulator, state.chunk, state.request.maximum_bytes, state.pre.size))
        accumulator = frame.output.result
        stop = accumulator.bounded_identity.payload == b"bounded" or len(accumulator.payload.payload) >= state.pre.size.value
        following = AwaitingPost(state.request, state.entry, state.opened, state.pre, accumulator) if stop else AwaitingRead(state.request, state.entry, state.opened, state.pre, accumulator)
        return _frame(following, frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingPost):
        frame = POST(PostInput(state.opened))
        return _frame(AwaitingFailureClose(state.opened, frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingClose(state.request, state.entry, state.opened, state.pre, state.accumulator, frame.output.result), frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingClose):
        frame = CLOSE(CloseInput(state.opened))
        return _frame(Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingStability(state.request, state.entry, state.pre, state.accumulator, state.post), frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingFailureClose):
        frame = CLOSE(CloseInput(state.opened))
        issue = Issue(state.issue.code, ByteVector(state.issue.detail.payload + b";close:" + (frame.output.result.detail.payload if isinstance(frame.output.result, Issue) else b"applied")))
        return _frame(Failed(issue), frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingStability):
        frame = STABILITY(StabilityInput(state.pre, state.post, state.accumulator))
        following = AwaitingRevision(state.request, state.entry, state.pre, state.accumulator, state.post, frame.output.result)
        return _frame(following, frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingRevision):
        frame = REVISION(RevisionInput(state.request, state.pre, state.post, state.accumulator, state.stability))
        following = Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingSeal(state.request, state.entry, state.pre, state.accumulator, state.post, state.stability, frame.output.result)
        return _frame(following, frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingSeal):
        frame = SEAL(SealInput(state.request, state.entry, state.pre, state.post, state.accumulator, state.stability, state.revision))
        following = Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingReadback(frame.output.result)
        return _frame(following, frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, AwaitingReadback):
        frame = READBACK(ReadbackInput(state.receipt))
        following = Complete(state.receipt, frame.output) if frame.output.verdict.payload == b"accepted" else Failed(Issue(ByteVector(b"receipt-readback-rejected"), frame.output.observed_digest))
        return _frame(following, frame.effect.evidence.payload, value.evidence_class)
    if isinstance(state, (Complete, Failed)):
        return _frame(state, APPLIED, value.evidence_class)
    return _frame(Failed(Issue(ByteVector(b"unknown-state"), ByteVector(state.__class__.__name__.encode("utf-8")))), REJECTED, value.evidence_class)
