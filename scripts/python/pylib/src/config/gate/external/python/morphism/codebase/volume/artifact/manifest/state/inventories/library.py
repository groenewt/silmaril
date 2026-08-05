from config.constants.morphism.codebase.volume.artifact.manifest.state.inventories.key.value import VALUE as INVENTORIES_KEY


def INVENTORIES(state: dict) -> list:
    return state[INVENTORIES_KEY]
