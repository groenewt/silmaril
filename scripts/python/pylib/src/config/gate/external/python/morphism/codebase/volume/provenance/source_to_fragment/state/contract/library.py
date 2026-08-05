from config.constants.morphism.codebase.volume.provenance.source_to_fragment.state.contract.key.value import VALUE as CONTRACT_KEY


def CONTRACT(state: dict) -> str:
    return state[CONTRACT_KEY]
