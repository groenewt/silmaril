from config.gate.external.python.morphism.codebase.volume.source.observation.state.pathnames.library import PATHNAMES
from config.gate.external.python.stdlib.os.path.isabs.library import DEPENDENCY as ISABS

VIOLATION = "observation_path_absolute="


def STATE(state: dict) -> dict:
    absolutes = [pathname for pathname in PATHNAMES(state) if ISABS(pathname)]
    if absolutes:
        raise ValueError(VIOLATION + absolutes[0])
    return state
