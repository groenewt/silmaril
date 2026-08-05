from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.value import Value as DirectoryFrame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.value import Value as Revision

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: DirectoryFrame
    revision: Revision
