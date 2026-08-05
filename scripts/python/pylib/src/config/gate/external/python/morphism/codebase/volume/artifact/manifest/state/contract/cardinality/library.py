from config.constants.morphism.codebase.volume.artifact.manifest.state.contract.cardinality.key.value import VALUE as CONTRACT_CARDINALITY_KEY


def CONTRACT_CARDINALITY(state: dict) -> int:
    return state[CONTRACT_CARDINALITY_KEY]
