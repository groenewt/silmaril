from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.unrealized.library import UNREALIZED
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.unsigned.library import UNSIGNED

UNREALIZED_VIOLATION = "process_coverage_accepted_process_not_materialized="
UNSIGNED_ORIGIN = 0
UNSIGNED_VIOLATION = "process_coverage_materialized_process_not_accepted="


def STATE(state: dict) -> dict:
    unsigned = UNSIGNED(state)
    if unsigned:
        raise ValueError(UNSIGNED_VIOLATION + unsigned[UNSIGNED_ORIGIN])
    unrealized = UNREALIZED(state)
    if unrealized:
        raise ValueError(UNREALIZED_VIOLATION + unrealized[UNSIGNED_ORIGIN])
    return state
