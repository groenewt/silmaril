from config.gate.external.python.morphism.codebase.volume.lexical.keyed.library import KEYED
from config.gate.external.python.morphism.codebase.volume.lexical.listed.library import LISTED


def UNIQUE(values: list) -> list:
    return LISTED(KEYED(values))
