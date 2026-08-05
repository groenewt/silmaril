from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.count.key.value import VALUE as EXPECTED_COUNT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.csv.artifacts.library import EXPECTED_CSV_ARTIFACTS


def STATE(state: dict) -> dict:
    return {**state, EXPECTED_COUNT_KEY: len(EXPECTED_CSV_ARTIFACTS(state))}
