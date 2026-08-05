from config.gate.external.python.base.builtins.int.value import VALUE as Integer
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    value: Integer
