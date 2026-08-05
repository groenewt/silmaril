from config.constants.morphism.codebase.volume.artifact.manifest.state.contract.cardinality.key.value import VALUE as CONTRACT_CARDINALITY_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.rows.library import CONTRACT_ROWS
from config.gate.external.python.morphism.codebase.volume.lexical.cardinality.library import CARDINALITY
from config.gate.external.python.morphism.codebase.volume.tabular.body.library import BODY


def STATE(state: dict) -> dict:
    return {**state, CONTRACT_CARDINALITY_KEY: CARDINALITY(BODY(CONTRACT_ROWS(state)))}
