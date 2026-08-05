from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.fragment.key.value import VALUE as EXPECTED_FRAGMENT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.rows.library import CONTRACT_ROWS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.fragment_artifact.index.library import FRAGMENT_ARTIFACT_INDEX
from config.gate.external.python.morphism.codebase.volume.lexical.unique.library import UNIQUE
from config.gate.external.python.morphism.codebase.volume.tabular.body.library import BODY
from config.gate.external.python.morphism.codebase.volume.tabular.column.library import COLUMN


def STATE(state: dict) -> dict:
    rows = BODY(CONTRACT_ROWS(state))
    fragments = COLUMN(rows, FRAGMENT_ARTIFACT_INDEX(state))
    return {**state, EXPECTED_FRAGMENT_KEY: UNIQUE(fragments)}
