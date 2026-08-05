from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES
from config.gate.external.python.stdlib.os.path.isabs.library import DEPENDENCY as ISABS

VIOLATION = "observation_prefix_absolute="


def STATE(state: dict) -> dict:
    absolutes = [prefix for prefix in PREFIXES(state) if ISABS(prefix)]
    if absolutes:
        raise ValueError(VIOLATION + absolutes[0])
    return state
