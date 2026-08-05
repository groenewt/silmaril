from config.constants.morphism.codebase.volume.artifact.manifest.contract.cardinality.expected.value import VALUE as EXPECTED_CARDINALITY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.cardinality.library import CONTRACT_CARDINALITY
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.morphism.codebase.volume.lexical.representation.library import REPRESENTATION

DISCREPANCY = "!="
VIOLATION = "manifest_contract_cardinality="


def STATE(state: dict) -> dict:
    observed = CONTRACT_CARDINALITY(state)
    if observed != EXPECTED_CARDINALITY and STRICT():
        raise ValueError(VIOLATION + REPRESENTATION(observed) + DISCREPANCY + REPRESENTATION(EXPECTED_CARDINALITY))
    return state
