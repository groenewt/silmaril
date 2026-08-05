from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.value import Value as DirectoryFrame

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: DirectoryFrame
