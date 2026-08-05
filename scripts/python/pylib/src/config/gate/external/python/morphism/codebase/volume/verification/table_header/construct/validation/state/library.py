from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.artifact.library import ARTIFACT
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.expected.library import EXPECTED
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.identity.library import IDENTITY
from config.gate.external.python.morphism.codebase.volume.verification.table_header.state.observed.library import OBSERVED

ARTIFACT_MARK = " artifact="
EXPECTED_MARK = " expected="
OBSERVED_MARK = " observed="
VIOLATION = "table_header_mismatch="


def STATE(state: dict) -> dict:
    expected = EXPECTED(state)
    observed = OBSERVED(state)
    if observed != expected:
        raise ValueError(
            VIOLATION
            + IDENTITY(state)
            + ARTIFACT_MARK
            + ARTIFACT(state)
            + EXPECTED_MARK
            + expected
            + OBSERVED_MARK
            + observed
        )
    return state
