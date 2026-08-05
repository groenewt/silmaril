from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.accumulate.apply import apply as ACCUMULATE
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.accumulate.input.value import Value as AccumulateInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classify.apply import apply as CLASSIFY
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classify.input.value import Value as ClassifyInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.dispatch.apply import apply as DISPATCH
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.dispatch.input.value import Value as DispatchInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.metadata.observe.apply import apply as CHILD_METADATA
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.metadata.observe.input.value import Value as ChildMetadataInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.close.apply import apply as CLOSE
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.close.input.value import Value as CloseInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.apply import apply as OPEN
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.input.value import Value as OpenInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.post.observe.apply import apply as POST
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.post.observe.input.value import Value as PostInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.pre.observe.apply import apply as PRE
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.pre.observe.input.value import Value as PreInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.derive.apply import apply as DERIVE_FRAME
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.derive.input.value import Value as FrameInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frontier.value import Value as Frontier
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.policy.decide.apply import apply as HIDDEN
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.policy.decide.input.value import Value as HiddenInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.end.value import Value as End
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observation.value import Value as Name
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observe.one.apply import apply as NAME
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observe.one.input.value import Value as NameInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.apply import apply as READBACK
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.input.value import Value as ReadbackInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.seal.apply import apply as SEAL
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.seal.input.value import Value as SealInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.apply import apply as REVISION
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.input.value import Value as RevisionInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.accumulate.value import Value as AwaitingAccumulate
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.child.metadata.value import Value as AwaitingChildMetadata
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.classification.value import Value as AwaitingClassification
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.close.value import Value as AwaitingClose
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.dispatch.value import Value as AwaitingDispatch
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.failure.close.value import Value as AwaitingFailureClose
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.frame.value import Value as AwaitingFrame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.hidden.value import Value as AwaitingHidden
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.name.value import Value as AwaitingName
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.open.value import Value as AwaitingOpen
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.post.value import Value as AwaitingPost
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.pre.value import Value as AwaitingPre
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.readback.value import Value as AwaitingReadback
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.revision.value import Value as AwaitingRevision
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.seal.value import Value as AwaitingSeal
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.complete.value import Value as Complete
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.failed.value import Value as Failed
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.transition.receipt.value import Value as TransitionReceipt
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def _frame(state, evidence, evidence_class, transition_identity, scan_identity, attempt, from_state) -> Frame:
    to_state = ByteVector(state.__class__.__name__.encode("utf-8"))
    effect = ByteVector(evidence)
    fields = (scan_identity, attempt, transition_identity, from_state, to_state, effect, evidence_class)
    serialized = ByteVector(b"".join(map(lambda field: FIELD(field).payload, fields)))
    receipt = TransitionReceipt(scan_identity, attempt, transition_identity, from_state, to_state, effect, evidence_class, serialized, ByteVector(SHA256(serialized.payload).digest()))
    return Frame(Output(state, receipt), Effect(effect, evidence_class))

def PROJECT(value: Input) -> Frame:
    state = value.state
    from_state = ByteVector(state.__class__.__name__.encode("utf-8"))
    def transition(next_state, evidence):
        return _frame(next_state, evidence, value.evidence_class, value.transition_identity, value.scan_identity, value.attempt, from_state)
    if isinstance(state, AwaitingOpen):
        request = state.request
        if request.artifact_provenance.evidence_class.payload != value.evidence_class.payload or request.drilldown_provenance.evidence_class.payload != value.evidence_class.payload:
            return transition(Failed(Issue(ByteVector(b"scheduler-evidence-class-mismatch"), value.evidence_class)), REJECTED)
        if request.scan_identity.payload != value.scan_identity.payload or request.attempt.payload != value.attempt.payload:
            return transition(Failed(Issue(ByteVector(b"scheduler-progress-identity-mismatch"), value.transition_identity)), REJECTED)
        valid = request.maximum_entries.value > 0 and request.maximum_depth.value >= request.depth.value and request.hidden_policy.payload in (b"include-all", b"exclude-hidden")
        if not valid:
            return transition(Failed(Issue(ByteVector(b"invalid-crawl-bound-or-policy"), request.hidden_policy)), REJECTED)
        frame = OPEN(OpenInput(request))
        following = Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingPre(frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingPre):
        frame = PRE(PreInput(state.opened))
        if isinstance(frame.output.result, Issue):
            return transition(AwaitingFailureClose(state.opened, frame.output.result), frame.effect.evidence.payload)
        frontier = Frontier((), (), Natural(0))
        accumulator = Accumulator((), ByteVector(b""), frontier, Natural(0), Natural(0), ByteVector(b"uninitialized"), ByteVector(b"stable-count"))
        return transition(AwaitingName(state.opened, frame.output.result, accumulator), frame.effect.evidence.payload)
    if isinstance(state, AwaitingName):
        frame = NAME(NameInput(state.opened, state.accumulator.next_ordinal))
        if isinstance(frame.output.result, Issue):
            following = AwaitingFailureClose(state.opened, frame.output.result)
        elif isinstance(frame.output.result, End):
            following = AwaitingPost(state.opened, state.pre, state.accumulator, frame.output.result)
        else:
            following = AwaitingChildMetadata(state.opened, state.pre, state.accumulator, frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingChildMetadata):
        frame = CHILD_METADATA(ChildMetadataInput(state.opened, state.name))
        following = AwaitingFailureClose(state.opened, frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingClassification(state.opened, state.pre, state.accumulator, state.name, frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingClassification):
        frame = CLASSIFY(ClassifyInput(state.metadata))
        following = AwaitingHidden(state.opened, state.pre, state.accumulator, state.name, state.metadata, frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingHidden):
        frame = HIDDEN(HiddenInput(state.name, state.opened.request.hidden_policy))
        following = AwaitingFailureClose(state.opened, frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingDispatch(state.opened, state.pre, state.accumulator, state.name, state.metadata, state.classification, frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingDispatch):
        frame = DISPATCH(DispatchInput(state.opened.request, state.name, state.metadata, state.classification, state.hidden))
        following = AwaitingAccumulate(state.opened, state.pre, state.accumulator, state.name, state.metadata, state.classification, state.hidden, frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingAccumulate):
        frame = ACCUMULATE(AccumulateInput(state.accumulator, state.name, state.metadata, state.classification, state.hidden, state.dispatch))
        return transition(AwaitingName(state.opened, state.pre, frame.output.result), frame.effect.evidence.payload)
    if isinstance(state, AwaitingPost):
        frame = POST(PostInput(state.opened))
        following = AwaitingFailureClose(state.opened, frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingClose(state.opened, state.pre, state.accumulator, state.end, frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingClose):
        frame = CLOSE(CloseInput(state.opened))
        following = Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingFrame(state.opened.request, state.pre, state.accumulator, state.end, state.post)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingFailureClose):
        frame = CLOSE(CloseInput(state.opened))
        detail = state.issue.detail.payload + b";close:" + (frame.output.result.detail.payload if isinstance(frame.output.result, Issue) else b"applied")
        return transition(Failed(Issue(state.issue.code, ByteVector(detail))), frame.effect.evidence.payload)
    if isinstance(state, AwaitingFrame):
        frame = DERIVE_FRAME(FrameInput(state.request, state.pre, state.post, state.accumulator, state.end))
        following = Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingRevision(frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingRevision):
        frame = REVISION(RevisionInput(state.frame))
        return transition(AwaitingSeal(state.frame, frame.output.result), frame.effect.evidence.payload)
    if isinstance(state, AwaitingSeal):
        frame = SEAL(SealInput(state.frame, state.revision))
        following = Failed(frame.output.result) if isinstance(frame.output.result, Issue) else AwaitingReadback(state.frame, frame.output.result)
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, AwaitingReadback):
        frame = READBACK(ReadbackInput(state.receipt))
        following = Complete(state.frame, state.receipt, frame.output) if frame.output.verdict.payload == b"accepted" else Failed(Issue(ByteVector(b"directory-receipt-readback-rejected"), frame.output.observed_digest))
        return transition(following, frame.effect.evidence.payload)
    if isinstance(state, (Complete, Failed)):
        return transition(state, APPLIED)
    return transition(Failed(Issue(ByteVector(b"unknown-directory-state"), ByteVector(state.__class__.__name__.encode("utf-8")))), REJECTED)
