from config.constants.morphism.codebase.volume.source.observation.state.segments.key.value import VALUE as SEGMENTS_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS


def STATE(state: dict) -> dict:
    return {**state, SEGMENTS_KEY: [SPLIT(path) for path in PATHS(state)]}
