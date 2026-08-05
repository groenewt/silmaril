from config.gate.external.python.lambda_blotto.invocation.process.directory.crawl.revision.derive.library import PROJECT
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.derive.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
