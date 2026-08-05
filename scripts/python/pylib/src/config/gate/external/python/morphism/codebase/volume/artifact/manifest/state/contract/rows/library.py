from config.constants.morphism.codebase.volume.artifact.manifest.state.contract.rows.key.value import VALUE as CONTRACT_ROWS_KEY


def CONTRACT_ROWS(state: dict) -> list:
    return state[CONTRACT_ROWS_KEY]
