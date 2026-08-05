from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.opened.file.description.occurrence.value import Value as Opened

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    opened: Opened
    issue: Issue
