from config.constants.morphism.codebase.volume.artifact.hash_line.state.entry.key.value import VALUE as ENTRY_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.digest.library import DIGEST_OF
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.path.library import PATH_OF


def STATE(state: dict) -> dict:
    return {**state, ENTRY_KEY: [DIGEST_OF(state), PATH_OF(state)]}
