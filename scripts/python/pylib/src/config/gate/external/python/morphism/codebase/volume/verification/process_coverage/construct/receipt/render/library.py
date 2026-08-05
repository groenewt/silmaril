from config.gate.external.python.morphism.codebase.volume.lexical.csv.materialize.library import MATERIALIZE
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.state.materialized.library import MATERIALIZED

HEADER = ["coordinate", "status"]
STATUS = "accepted_and_materialized"


def RENDER(state: dict) -> str:
    receipt = [[coordinate, STATUS] for coordinate in MATERIALIZED(state)]
    return MATERIALIZE([HEADER, *receipt])
