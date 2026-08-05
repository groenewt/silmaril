from config.gate.external.python.lambda_blotto.invocation.process.file.capture.post.observe.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.post.observe.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.post.observe.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
