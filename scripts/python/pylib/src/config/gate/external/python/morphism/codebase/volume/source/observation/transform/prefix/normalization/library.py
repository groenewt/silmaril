from config.constants.morphism.codebase.volume.source.observation.state.prefixes.key.value import VALUE as PREFIXES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES
from config.gate.external.python.stdlib.os.path.normpath.library import DEPENDENCY as NORMPATH


def STATE(state: dict) -> dict:
    return {**state, PREFIXES_KEY: [NORMPATH(prefix) for prefix in PREFIXES(state)]}
