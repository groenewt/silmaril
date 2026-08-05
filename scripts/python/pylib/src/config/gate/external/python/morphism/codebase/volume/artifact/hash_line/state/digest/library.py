from config.constants.morphism.codebase.volume.artifact.hash_line.state.digest.key.value import VALUE as DIGEST_KEY


def DIGEST_OF(state: dict) -> str:
    return state[DIGEST_KEY]
