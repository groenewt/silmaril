from config.constants.morphism.codebase.volume.table.state.rows.key.value import VALUE as ROWS_KEY
from config.gate.external.python.morphism.codebase.volume.table.state.rows.library import ROWS


def STATE(state: dict) -> dict:
    return {ROWS_KEY: sorted(ROWS(state))}
