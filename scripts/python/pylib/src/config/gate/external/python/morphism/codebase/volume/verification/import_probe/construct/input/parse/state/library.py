from config.constants.morphism.codebase.volume.verification.import_probe.state.prefix.key.value import VALUE as PREFIX_KEY
from config.constants.morphism.codebase.volume.verification.import_probe.state.registry.key.value import VALUE as REGISTRY_KEY

EXPECTED = 2
PREFIX_ORIGIN = 1
REGISTRY_ORIGIN = 0
VIOLATION = "import_probe_arguments_expected_2_received="


def STATE(arguments: list) -> dict:
    if len(arguments) != EXPECTED:
        raise ValueError(VIOLATION + str(len(arguments)))
    return {
        REGISTRY_KEY: arguments[REGISTRY_ORIGIN],
        PREFIX_KEY: arguments[PREFIX_ORIGIN],
    }
