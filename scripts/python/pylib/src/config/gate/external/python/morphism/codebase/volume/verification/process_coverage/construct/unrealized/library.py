from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.state.accepted.library import ACCEPTED
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.state.materialized.library import MATERIALIZED


def UNREALIZED(state: dict) -> list:
    materialized = MATERIALIZED(state)
    return [coordinate for coordinate in ACCEPTED(state) if coordinate not in materialized]
