from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.identities.library import IDENTITIES

VIOLATION = "aggregate_identity_duplicate="


def STATE(state: dict) -> dict:
    seen = [tuple(identity) for identity in IDENTITIES(state)]
    if len(set(seen)) != len(seen):
        raise ValueError(VIOLATION + str(len(seen) - len(set(seen))))
    return state
