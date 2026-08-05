from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.payloads.key.value import VALUE as PAYLOADS_KEY


def PAYLOADS(state: dict) -> list:
    return state[PAYLOADS_KEY]
