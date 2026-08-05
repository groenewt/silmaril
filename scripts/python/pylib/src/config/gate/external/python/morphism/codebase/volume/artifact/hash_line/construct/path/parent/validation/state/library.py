from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.pathname.library import PATHNAME
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT

VIOLATION = "hash_line_path_parent="
PARENT_SEGMENT = ".."


def STATE(state: dict) -> dict:
    pathname = PATHNAME(state)
    if PARENT_SEGMENT in SPLIT(pathname) and STRICT():
        raise ValueError(VIOLATION + pathname)
    return state
