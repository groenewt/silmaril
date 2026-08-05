from config.constants.morphism.codebase.volume.table.aggregate.source_files.numeric.column.value import VALUE as NUMERIC_COLUMN
from config.constants.morphism.codebase.volume.table.aggregate.state.keyed.key.value import VALUE as KEYED_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.integer.library import INTEGER
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.keyed.library import KEYED


def STATE(state: dict) -> dict:
    return {**state, KEYED_KEY: [[[INTEGER(key[NUMERIC_COLUMN])] + key[NUMERIC_COLUMN + 1:], row] for key, row in KEYED(state)]}
