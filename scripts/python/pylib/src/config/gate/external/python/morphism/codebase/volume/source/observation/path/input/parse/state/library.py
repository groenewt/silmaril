from config.constants.morphism.codebase.volume.source.observation.state.ignored.empty.value import VALUE as IGNORED_EMPTY
from config.constants.morphism.codebase.volume.source.observation.state.ignored.key.value import VALUE as IGNORED_KEY
from config.constants.morphism.codebase.volume.source.observation.state.paths.key.value import VALUE as PATHS_KEY


def STATE(lines: list) -> dict:
    return {IGNORED_KEY: IGNORED_EMPTY, PATHS_KEY: lines}
