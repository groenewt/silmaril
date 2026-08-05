from config.gate.external.python.lambda_blotto.invocation.process.directory.crawl.receipt.readback.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.readback.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
