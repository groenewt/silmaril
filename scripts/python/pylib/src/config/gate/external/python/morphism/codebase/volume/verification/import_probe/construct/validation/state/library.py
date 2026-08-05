from config.gate.external.python.morphism.codebase.volume.verification.import_probe.state.failures.library import FAILURES

FIELD_SEPARATOR = " "
RECORD_SEPARATOR = "; "
VIOLATION = "import_probe_declared_module_not_importable="


def STATE(state: dict) -> dict:
    failures = FAILURES(state)
    if failures:
        raise ValueError(VIOLATION + RECORD_SEPARATOR.join(FIELD_SEPARATOR.join(failure) for failure in failures))
    return state
