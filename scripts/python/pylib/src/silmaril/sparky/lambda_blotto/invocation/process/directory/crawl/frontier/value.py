from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.directory.work.value import Value as DirectoryWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    directories: tuple[DirectoryWork, ...]
    files: tuple[FileWork, ...]
    observed_children: Natural
