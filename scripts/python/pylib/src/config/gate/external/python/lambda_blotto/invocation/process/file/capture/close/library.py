from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.file.capture.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.os.close.value import VALUE as CLOSE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.close.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.close.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.close.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.close.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.conversion.os.error.project import PROJECT as ISSUE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    try:
        CLOSE(value.opened.descriptor.number.value)
        return Frame(Output(ByteVector(b"closed")), Effect(ByteVector(APPLIED)))
    except OSError as issue:
        return Frame(Output(ISSUE(issue)), Effect(ByteVector(REJECTED)))
