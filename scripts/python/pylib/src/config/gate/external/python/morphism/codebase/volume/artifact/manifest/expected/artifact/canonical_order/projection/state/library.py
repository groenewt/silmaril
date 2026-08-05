from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.artifact.key.value import VALUE as EXPECTED_ARTIFACT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.artifact.library import EXPECTED_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.lexical.order.library import ORDER


def STATE(state: dict) -> dict:
    return {**state, EXPECTED_ARTIFACT_KEY: ORDER(EXPECTED_ARTIFACTS(state))}
