from config.gate.external.python.lambda_blotto.invocation.process.file.capture.scheduler.transition.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
