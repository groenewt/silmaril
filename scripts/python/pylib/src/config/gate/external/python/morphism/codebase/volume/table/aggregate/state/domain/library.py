from config.constants.morphism.codebase.volume.table.aggregate.state.domain.key.value import VALUE as DOMAIN_KEY


def DOMAIN(state: dict) -> list:
    return state[DOMAIN_KEY]
