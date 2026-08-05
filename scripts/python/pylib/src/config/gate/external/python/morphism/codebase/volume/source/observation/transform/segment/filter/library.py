from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.names.library import NAMES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.segments.library import SEGMENTS


def STATE(state: dict) -> dict:
    excluded = frozenset(NAMES(state))
    return {**state, INDICES_KEY: [index for index, segments in enumerate(SEGMENTS(state)) if not excluded.isdisjoint(segments)]}
