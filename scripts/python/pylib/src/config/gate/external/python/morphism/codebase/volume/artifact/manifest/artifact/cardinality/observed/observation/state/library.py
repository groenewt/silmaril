from config.constants.morphism.codebase.volume.artifact.manifest.state.observed.count.key.value import VALUE as OBSERVED_COUNT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.observed.csv.artifacts.library import OBSERVED_CSV_ARTIFACTS


def STATE(state: dict) -> dict:
    return {**state, OBSERVED_COUNT_KEY: len(OBSERVED_CSV_ARTIFACTS(state))}
