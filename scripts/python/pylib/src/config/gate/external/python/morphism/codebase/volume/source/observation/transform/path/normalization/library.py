from config.constants.morphism.codebase.volume.source.observation.state.paths.key.value import VALUE as PATHS_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.relative.library import RELATIVE
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS


def STATE(state: dict) -> dict:
    return {**state, PATHS_KEY: [RELATIVE(path) for path in PATHS(state)]}
