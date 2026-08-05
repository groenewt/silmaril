from config.gate.external.python.morphism.codebase.volume.source.observation.state.names.library import NAMES

VIOLATION = "observation_name_contains_separator="
SEPARATOR = "/"


def STATE(state: dict) -> dict:
    compound = [name for name in NAMES(state) if SEPARATOR in name]
    if compound:
        raise ValueError(VIOLATION + compound[0])
    return state
