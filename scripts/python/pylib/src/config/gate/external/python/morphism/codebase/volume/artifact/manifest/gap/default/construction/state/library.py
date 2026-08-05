from config.constants.morphism.codebase.volume.artifact.manifest.gap.empty.value import VALUE as EMPTY_GAPS
from config.constants.morphism.codebase.volume.artifact.manifest.state.gaps.key.value import VALUE as GAPS_KEY


def STATE(state: dict) -> dict:
    if GAPS_KEY in state:
        return state
    return {**state, GAPS_KEY: EMPTY_GAPS}
