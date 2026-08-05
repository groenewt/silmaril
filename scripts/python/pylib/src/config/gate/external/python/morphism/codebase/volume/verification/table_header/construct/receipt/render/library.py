from config.gate.external.python.morphism.codebase.volume.lexical.csv.materialize.library import MATERIALIZE
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.artifact.library import ARTIFACT
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.expected.library import EXPECTED
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.identity.library import IDENTITY
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.observed.library import OBSERVED

HEADER = ["table_id", "artifact", "expected_header", "observed_header", "status"]
STATUS = "header_identical"


def RENDER(state: dict) -> str:
    receipt = [
        IDENTITY(state),
        ARTIFACT(state),
        EXPECTED(state),
        OBSERVED(state),
        STATUS,
    ]
    return MATERIALIZE([HEADER, receipt])
