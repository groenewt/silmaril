from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.ignored.library import IGNORED
from config.gate.external.python.morphism.codebase.volume.source.observation.state.segments.library import SEGMENTS


def STATE(state: dict) -> dict:
    excluded = frozenset(IGNORED(state))
    return {**state, INDICES_KEY: [index for index, segments in enumerate(SEGMENTS(state)) if excluded.isdisjoint(segments)]}
