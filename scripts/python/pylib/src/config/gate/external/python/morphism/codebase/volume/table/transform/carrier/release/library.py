from config.constants.morphism.codebase.volume.source.observation.state.pathnames.key.value import VALUE as PATHNAMES_KEY

RELEASED = (PATHNAMES_KEY,)


def STATE(state: dict) -> dict:
    return {key: value for key, value in state.items() if key not in RELEASED}
