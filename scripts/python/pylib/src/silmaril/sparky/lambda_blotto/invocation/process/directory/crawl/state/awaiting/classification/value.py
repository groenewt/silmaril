from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observation.value import Value as Name
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.opened.directory.description.occurrence.value import Value as Opened
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    opened: Opened
    pre: Metadata
    accumulator: Accumulator
    name: Name
    metadata: Metadata
