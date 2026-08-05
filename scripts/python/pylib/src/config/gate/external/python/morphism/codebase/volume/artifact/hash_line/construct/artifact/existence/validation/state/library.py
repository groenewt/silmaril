from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.artifact.library import ARTIFACT
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.stdlib.os.path.isfile.library import DEPENDENCY as ISFILE

VIOLATION = "hash_line_artifact_missing="


def STATE(state: dict) -> dict:
    artifact = ARTIFACT(state)
    if not ISFILE(artifact) and STRICT():
        raise ValueError(VIOLATION + artifact)
    return state
