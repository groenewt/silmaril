from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.observed_keys.library import OBSERVED_KEYS
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.reference_keys.library import REFERENCE_KEYS

VIOLATION = "aggregate_required_set_mismatch missing="


def STATE(state: dict) -> dict:
    missing = [key for key in REFERENCE_KEYS(state) if key not in OBSERVED_KEYS(state)]
    if missing:
        raise ValueError(VIOLATION + ','.join(missing))
    return state
