from config.constants.morphism.codebase.volume.verification.import_probe.state.failures.key.value import VALUE as FAILURES_KEY
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.resolution.library import RESOLUTION
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.state.declared.library import DECLARED

COORDINATE_ORIGIN = 0
MODULE_ORIGIN = 1


def STATE(state: dict) -> dict:
    failures = []
    for entry in DECLARED(state):
        resolution = RESOLUTION(entry[MODULE_ORIGIN])
        if resolution:
            failures.append((entry[COORDINATE_ORIGIN], entry[MODULE_ORIGIN], resolution))
    return {**state, FAILURES_KEY: failures}
