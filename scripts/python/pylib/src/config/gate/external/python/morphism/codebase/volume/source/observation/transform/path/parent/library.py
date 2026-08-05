from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.pathnames.library import PATHNAMES

VIOLATION = "observation_path_parent="
PARENT_SEGMENT = ".."


def STATE(state: dict) -> dict:
    traversals = [pathname for pathname in PATHNAMES(state) if PARENT_SEGMENT in SPLIT(pathname)]
    if traversals:
        raise ValueError(VIOLATION + traversals[0])
    return state
