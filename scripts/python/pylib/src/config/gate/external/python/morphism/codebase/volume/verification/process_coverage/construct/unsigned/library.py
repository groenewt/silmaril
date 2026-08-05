from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.state.accepted.library import ACCEPTED
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.state.materialized.library import MATERIALIZED


def UNSIGNED(state: dict) -> list:
    accepted = ACCEPTED(state)
    return [coordinate for coordinate in MATERIALIZED(state) if coordinate not in accepted]
