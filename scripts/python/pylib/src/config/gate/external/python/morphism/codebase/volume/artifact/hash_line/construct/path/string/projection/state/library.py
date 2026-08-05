from config.constants.morphism.codebase.volume.artifact.hash_line.state.path.key.value import VALUE as PATH_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.pathname.library import PATHNAME


def STATE(state: dict) -> dict:
    return {**state, PATH_KEY: str(PATHNAME(state))}
