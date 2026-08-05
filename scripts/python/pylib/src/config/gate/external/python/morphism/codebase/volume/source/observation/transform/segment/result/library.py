from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.constants.morphism.codebase.volume.source.observation.state.paths.key.value import VALUE as PATHS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS


def STATE(state: dict) -> dict:
    return {PATHS_KEY: PATHS(state), INDICES_KEY: INDICES(state)}
