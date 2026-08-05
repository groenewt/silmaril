from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.request.value import Value as Request

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    request: Request
