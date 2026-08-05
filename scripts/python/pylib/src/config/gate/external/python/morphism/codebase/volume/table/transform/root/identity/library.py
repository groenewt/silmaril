from config.gate.external.python.morphism.codebase.volume.table.state.root.identity.library import ROOT_ID

VIOLATION = "table_root_identity_empty"
EMPTY = ""


def STATE(state: dict) -> dict:
    if ROOT_ID(state) == EMPTY:
        raise ValueError(VIOLATION)
    return state
