from config.gate.external.python.lambda_blotto.invocation.process.file.capture.entry.stat.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.entry.stat.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.entry.stat.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
