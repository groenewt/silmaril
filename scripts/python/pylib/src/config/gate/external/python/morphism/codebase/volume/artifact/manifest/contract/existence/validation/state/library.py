from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.path.library import CONTRACT_PATH
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

VIOLATION = "manifest_contract_absent="


def STATE(state: dict) -> dict:
    locus = CONTRACT_PATH(state)
    if not LEXISTS(locus) and STRICT():
        raise ValueError(VIOLATION + locus)
    return state
