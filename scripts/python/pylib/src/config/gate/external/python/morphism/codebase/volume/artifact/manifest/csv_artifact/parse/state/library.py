from config.constants.morphism.codebase.volume.artifact.manifest.state.csv.documents.key.value import VALUE as CSV_DOCUMENTS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.document.library import DOCUMENT
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.path.csv.library import CSV_ARTIFACT


def STATE(state: dict) -> dict:
    return {**state, CSV_DOCUMENTS_KEY: {path: DOCUMENT(path) for path in MANIFEST_ARTIFACTS(state) if CSV_ARTIFACT(path)}}
