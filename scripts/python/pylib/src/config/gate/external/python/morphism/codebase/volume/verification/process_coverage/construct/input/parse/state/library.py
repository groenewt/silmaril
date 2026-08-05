from config.constants.morphism.codebase.volume.verification.process_coverage.state.coordinate.key.value import VALUE as COORDINATE_KEY
from config.constants.morphism.codebase.volume.verification.process_coverage.state.inventory.key.value import VALUE as INVENTORY_KEY

COORDINATE_ORIGIN = 1
EXPECTED = 2
INVENTORY_ORIGIN = 0
VIOLATION = "process_coverage_arguments_expected_2_received="


def STATE(arguments: list) -> dict:
    if len(arguments) != EXPECTED:
        raise ValueError(VIOLATION + str(len(arguments)))
    return {
        INVENTORY_KEY: arguments[INVENTORY_ORIGIN],
        COORDINATE_KEY: arguments[COORDINATE_ORIGIN],
    }
