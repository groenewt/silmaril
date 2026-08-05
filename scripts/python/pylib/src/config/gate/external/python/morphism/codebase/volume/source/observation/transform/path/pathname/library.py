from config.constants.morphism.codebase.volume.source.observation.state.pathnames.key.value import VALUE as PATHNAMES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS


def STATE(state: dict) -> dict:
    return {**state, PATHNAMES_KEY: list(PATHS(state))}
