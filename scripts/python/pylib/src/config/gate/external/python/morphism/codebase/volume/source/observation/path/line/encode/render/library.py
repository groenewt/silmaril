from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS

LINE_FEED = "\n"
EMPTY = ""


def RENDER(state: dict) -> str:
    paths = PATHS(state)
    return EMPTY.join([paths[index] + LINE_FEED for index in INDICES(state)])
