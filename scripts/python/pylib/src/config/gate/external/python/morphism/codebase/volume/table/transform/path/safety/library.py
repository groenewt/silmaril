from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS
from config.gate.external.python.stdlib.os.path.isabs.library import DEPENDENCY as ISABS

VIOLATION = "table_path_unsafe="
PARENT_SEGMENT = ".."


def STATE(state: dict) -> dict:
    unsafe = [path for path in PATHS(state) if ISABS(path) or PARENT_SEGMENT in SPLIT(path)]
    if unsafe:
        raise ValueError(VIOLATION + unsafe[0])
    return state
