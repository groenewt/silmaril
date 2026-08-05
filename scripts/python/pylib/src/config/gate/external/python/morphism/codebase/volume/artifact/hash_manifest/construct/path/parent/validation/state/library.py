from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.pathnames.library import PATHNAMES
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT

VIOLATION = "hash_manifest_path_parent="
PARENT_SEGMENT = ".."


def STATE(state: dict) -> dict:
    traversals = [pathname for pathname in PATHNAMES(state) if PARENT_SEGMENT in SPLIT(pathname)]
    if traversals and STRICT():
        raise ValueError(VIOLATION + traversals[0])
    return state
