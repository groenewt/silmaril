from config.constants.morphism.codebase.volume.verification.import_probe.state.registered.key.value import VALUE as REGISTERED_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.csv.rows.library import ROWS
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.column.library import REGISTRATIONS
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.state.registry.library import REGISTRY
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

VIOLATION = "import_probe_registry_missing="


def STATE(state: dict) -> dict:
    registry = REGISTRY(state)
    if not LEXISTS(registry):
        raise ValueError(VIOLATION + registry)
    return {**state, REGISTERED_KEY: REGISTRATIONS(ROWS(registry))}
