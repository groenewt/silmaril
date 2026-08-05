from config.gate.external.python.morphism.codebase.volume.lexical.last.library import LAST
from config.gate.external.python.morphism.codebase.volume.lexical.octets.library import OCTETS


def ORDINAL(entry: list) -> bytes:
    return OCTETS(LAST(entry))
