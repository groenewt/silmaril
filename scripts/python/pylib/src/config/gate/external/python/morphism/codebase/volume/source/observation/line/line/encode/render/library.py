from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.lines.library import RENDERED

EMPTY = ""


def RENDER(state: dict) -> str:
    lines = RENDERED(state)
    return EMPTY.join([lines[index] for index in INDICES(state)])
