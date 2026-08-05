from config.gate.external.python.lambda_blotto.invocation.process.file.capture.read.one.chunk.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.read.one.chunk.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
