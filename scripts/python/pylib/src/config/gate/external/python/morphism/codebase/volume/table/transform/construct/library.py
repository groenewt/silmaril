from config.constants.morphism.codebase.volume.table.state.rows.key.value import VALUE as ROWS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.line.input.parse.record.library import RECORD


def STATE(lines: list) -> dict:
    return {ROWS_KEY: [RECORD(line) for line in lines]}
