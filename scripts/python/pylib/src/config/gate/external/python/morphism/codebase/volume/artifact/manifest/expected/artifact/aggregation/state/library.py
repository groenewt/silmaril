from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.artifact.key.value import VALUE as EXPECTED_ARTIFACT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv_artifact.expected.library import CSV_ARTIFACT_EXPECTED
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.body.library import EXPECTED_BODY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.filetree.library import EXPECTED_FILETREE
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.fragment.library import EXPECTED_FRAGMENTS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.table.library import EXPECTED_TABLES
from config.gate.external.python.morphism.codebase.volume.lexical.concatenation.library import CONCATENATION
from config.gate.external.python.morphism.codebase.volume.lexical.unique.library import UNIQUE


def STATE(state: dict) -> dict:
    families = [
        CSV_ARTIFACT_EXPECTED(state),
        EXPECTED_TABLES(state),
        EXPECTED_FRAGMENTS(state),
        EXPECTED_BODY(state),
        EXPECTED_FILETREE(state),
    ]
    return {**state, EXPECTED_ARTIFACT_KEY: UNIQUE(CONCATENATION(families))}
