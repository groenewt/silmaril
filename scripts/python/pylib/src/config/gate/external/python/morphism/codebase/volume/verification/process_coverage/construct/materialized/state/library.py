from config.constants.morphism.codebase.volume.verification.process_coverage.state.materialized.key.value import VALUE as MATERIALIZED_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.csv.rows.library import ROWS
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.column.library import COORDINATES
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.state.coordinate.library import COORDINATE
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

VIOLATION = "process_coverage_materialized_coordinates_missing="


def STATE(state: dict) -> dict:
    coordinate = COORDINATE(state)
    if not LEXISTS(coordinate):
        raise ValueError(VIOLATION + coordinate)
    return {**state, MATERIALIZED_KEY: COORDINATES(ROWS(coordinate))}
