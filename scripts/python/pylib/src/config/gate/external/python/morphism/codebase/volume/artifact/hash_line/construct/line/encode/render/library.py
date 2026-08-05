from config.constants.morphism.codebase.volume.digest.separator.value import VALUE as SEPARATOR
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.entry.library import ENTRY
from config.gate.external.python.morphism.codebase.volume.lexical.first.library import FIRST
from config.gate.external.python.morphism.codebase.volume.lexical.last.library import LAST

LINE_FEED = "\n"


def RENDER(state: dict) -> str:
    entry = ENTRY(state)
    return FIRST(entry) + SEPARATOR + LAST(entry) + LINE_FEED
