from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.counts.key.value import VALUE as COUNTS_KEY


def COUNTS(state: dict) -> list:
    return state[COUNTS_KEY]
