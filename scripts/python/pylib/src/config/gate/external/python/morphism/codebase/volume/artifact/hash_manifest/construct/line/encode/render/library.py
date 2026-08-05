from config.constants.morphism.codebase.volume.digest.separator.value import VALUE as SEPARATOR
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.entries.library import ENTRIES
from config.gate.external.python.morphism.codebase.volume.lexical.first.library import FIRST
from config.gate.external.python.morphism.codebase.volume.lexical.last.library import LAST

LINE_FEED = "\n"
EMPTY = ""


def RENDER(state: dict) -> str:
    return EMPTY.join([FIRST(entry) + SEPARATOR + LAST(entry) + LINE_FEED for entry in ENTRIES(state)])
