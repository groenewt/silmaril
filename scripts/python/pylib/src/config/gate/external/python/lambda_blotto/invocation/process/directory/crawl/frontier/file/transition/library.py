from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frontier.file.transition.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frontier.file.transition.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frontier.file.transition.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frontier.file.transition.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.apply import apply as FILE_TRANSITION
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.input.value import Value as FileInput
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    transitioned = FILE_TRANSITION(FileInput(value.work.state, value.work.evidence_class))
    return Frame(Output(FileWork(transitioned.output.state, value.work.evidence_class)), Effect(ByteVector(APPLIED), value.work.evidence_class))
