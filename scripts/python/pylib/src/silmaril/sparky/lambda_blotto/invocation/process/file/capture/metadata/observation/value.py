from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    device: Natural
    inode: Natural
    mode: Natural
    link_count: Natural
    user: Natural
    group: Natural
    size: Natural
    modified_nanoseconds: Natural
    changed_nanoseconds: Natural
