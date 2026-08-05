from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS
from config.gate.external.python.stdlib.os.path.islink.library import DEPENDENCY as ISLINK


def STATE(state: dict) -> dict:
    paths = PATHS(state)
    return {**state, INDICES_KEY: [index for index in INDICES(state) if ISLINK(paths[index])]}
