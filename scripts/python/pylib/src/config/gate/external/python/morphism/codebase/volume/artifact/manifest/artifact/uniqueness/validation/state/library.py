from config.gate.external.python.morphism.codebase.volume.artifact.duplicates.library import DUPLICATES
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "artifact_path_duplicated="
JOINER = ","


def STATE(state: dict) -> dict:
    repeated = DUPLICATES(MANIFEST_ARTIFACTS(state))
    if repeated and STRICT():
        raise ValueError(VIOLATION + JOINER.join(repeated))
    return state
