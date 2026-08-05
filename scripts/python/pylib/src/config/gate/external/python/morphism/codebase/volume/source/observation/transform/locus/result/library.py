from config.constants.morphism.codebase.volume.source.observation.state.paths.key.value import VALUE as PATHS_KEY
from config.constants.morphism.codebase.volume.source.observation.state.prefixes.key.value import VALUE as PREFIXES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS
from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES


def STATE(state: dict) -> dict:
    return {PREFIXES_KEY: PREFIXES(state), PATHS_KEY: PATHS(state)}
