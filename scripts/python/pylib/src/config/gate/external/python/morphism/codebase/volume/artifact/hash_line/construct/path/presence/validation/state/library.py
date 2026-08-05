from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.path.library import PATH_OF
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "hash_line_path_empty"
EMPTY = ""


def STATE(state: dict) -> dict:
    if PATH_OF(state) == EMPTY and STRICT():
        raise ValueError(VIOLATION)
    return state
