from config.constants.morphism.codebase.volume.table.aggregate.gdb_evidence.numeric.column.value import VALUE as NUMERIC_COLUMN
from config.constants.morphism.codebase.volume.table.aggregate.state.domain.key.value import VALUE as DOMAIN_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.integer.library import INTEGER
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.domain.library import DOMAIN

WIDTH = 12
PADDING = "0"


def STATE(state: dict) -> dict:
    return {**state, DOMAIN_KEY: [row[:NUMERIC_COLUMN] + [str(INTEGER(row[NUMERIC_COLUMN])).rjust(WIDTH, PADDING)] + row[NUMERIC_COLUMN + 1:] for row in DOMAIN(state)]}
