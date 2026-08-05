from config.gate.external.python.morphism.codebase.volume.table.state.rows.library import ROWS
from config.gate.external.python.morphism.codebase.volume.table.encode.library import ENCODE_TABLE


def RENDER(state: dict) -> str:
    return ENCODE_TABLE(ROWS(state))
