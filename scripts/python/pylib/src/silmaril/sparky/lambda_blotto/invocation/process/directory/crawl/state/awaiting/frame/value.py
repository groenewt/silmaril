from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.end.value import Value as End
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.request.value import Value as Request
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    request: Request
    pre: Metadata
    accumulator: Accumulator
    end: End
    post: Metadata
