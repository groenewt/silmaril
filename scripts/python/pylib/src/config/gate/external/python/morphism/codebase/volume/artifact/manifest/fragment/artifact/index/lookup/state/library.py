from config.constants.morphism.codebase.volume.artifact.manifest.contract.column.fragment_artifact.value import VALUE as FRAGMENT_ARTIFACT_COLUMN
from config.constants.morphism.codebase.volume.artifact.manifest.state.fragment_artifact.index.key.value import VALUE as FRAGMENT_ARTIFACT_INDEX_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.rows.library import CONTRACT_ROWS
from config.gate.external.python.morphism.codebase.volume.lexical.position.library import POSITION
from config.gate.external.python.morphism.codebase.volume.tabular.header.library import HEADER


def STATE(state: dict) -> dict:
    header = HEADER(CONTRACT_ROWS(state))
    return {**state, FRAGMENT_ARTIFACT_INDEX_KEY: POSITION(header, FRAGMENT_ARTIFACT_COLUMN)}
