from config.constants.morphism.codebase.volume.lexical.position.absent.value import VALUE as ABSENT_POSITION
from config.gate.external.python.stdlib.builtins.enumerate.library import DEPENDENCY as ENUMERATE


def POSITION(values: list, value: str) -> int:
    for offset, candidate in ENUMERATE(values):
        if candidate == value:
            return offset
    return ABSENT_POSITION
