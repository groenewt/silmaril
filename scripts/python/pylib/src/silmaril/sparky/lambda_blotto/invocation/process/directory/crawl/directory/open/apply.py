from config.gate.external.python.lambda_blotto.invocation.process.directory.crawl.directory.open.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
