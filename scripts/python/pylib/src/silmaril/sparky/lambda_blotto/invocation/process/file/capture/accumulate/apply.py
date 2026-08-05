from config.gate.external.python.lambda_blotto.invocation.process.file.capture.accumulate.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.accumulate.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
