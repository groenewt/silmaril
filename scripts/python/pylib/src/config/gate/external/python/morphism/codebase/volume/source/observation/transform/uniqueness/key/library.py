from config.constants.morphism.codebase.volume.source.observation.state.keys.key.value import VALUE as KEYS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS


def STATE(state: dict) -> dict:
    paths = PATHS(state)
    return {**state, KEYS_KEY: [paths[index] for index in INDICES(state)]}
