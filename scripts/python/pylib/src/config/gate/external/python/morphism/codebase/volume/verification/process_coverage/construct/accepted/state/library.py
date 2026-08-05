from config.constants.morphism.codebase.volume.verification.process_coverage.state.accepted.key.value import VALUE as ACCEPTED_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.csv.rows.library import ROWS
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.column.library import COORDINATES
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.state.inventory.library import INVENTORY
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

VIOLATION = "process_coverage_accepted_inventory_missing="


def STATE(state: dict) -> dict:
    inventory = INVENTORY(state)
    if not LEXISTS(inventory):
        raise ValueError(VIOLATION + inventory)
    return {**state, ACCEPTED_KEY: COORDINATES(ROWS(inventory))}
