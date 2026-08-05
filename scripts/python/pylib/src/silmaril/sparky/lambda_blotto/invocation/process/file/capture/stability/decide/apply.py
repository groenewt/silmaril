from config.gate.external.python.lambda_blotto.invocation.process.file.capture.stability.decide.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.stability.decide.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
