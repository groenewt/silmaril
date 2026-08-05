from config.gate.external.python.morphism.codebase.volume.source.observation.state.names.library import NAMES
from config.gate.external.python.stdlib.os.path.normpath.library import DEPENDENCY as NORMPATH

VIOLATION = "observation_name_not_canonical="


def STATE(state: dict) -> dict:
    divergent = [name for name in NAMES(state) if NORMPATH(name) != name]
    if divergent:
        raise ValueError(VIOLATION + divergent[0])
    return state
