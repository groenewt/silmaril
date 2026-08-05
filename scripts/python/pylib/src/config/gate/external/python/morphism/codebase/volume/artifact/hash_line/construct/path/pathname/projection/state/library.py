from config.constants.morphism.codebase.volume.artifact.hash_line.state.pathname.key.value import VALUE as PATHNAME_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.path.library import PATH_OF


def STATE(state: dict) -> dict:
    return {**state, PATHNAME_KEY: PATH_OF(state)}
