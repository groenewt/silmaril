from config.constants.morphism.codebase.volume.artifact.manifest.state.contract.path.key.value import VALUE as CONTRACT_PATH_KEY


def CONTRACT_PATH(state: dict) -> str:
    return state[CONTRACT_PATH_KEY]
