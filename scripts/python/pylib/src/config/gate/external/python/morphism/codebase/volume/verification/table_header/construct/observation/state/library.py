from config.constants.morphism.codebase.volume.verification.table_header.state.observed.key.value import VALUE as OBSERVED_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.csv.head.library import HEAD
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.artifact.library import ARTIFACT
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

VIOLATION = "table_header_artifact_missing="


def STATE(state: dict) -> dict:
    artifact = ARTIFACT(state)
    if not LEXISTS(artifact):
        raise ValueError(VIOLATION + artifact)
    return {**state, OBSERVED_KEY: HEAD(artifact)}
