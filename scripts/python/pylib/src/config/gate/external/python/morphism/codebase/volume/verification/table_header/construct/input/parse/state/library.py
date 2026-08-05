from config.constants.morphism.codebase.volume.verification.table_header.state.artifact.key.value import VALUE as ARTIFACT_KEY
from config.constants.morphism.codebase.volume.verification.table_header.state.expected.key.value import VALUE as EXPECTED_KEY
from config.constants.morphism.codebase.volume.verification.table_header.state.identity.key.value import VALUE as IDENTITY_KEY

ARTIFACT_ORIGIN = 0
EXPECTED = 3
EXPECTED_ORIGIN = 2
IDENTITY_ORIGIN = 1
VIOLATION = "table_header_arguments_expected_3_received="


def STATE(arguments: list) -> dict:
    if len(arguments) != EXPECTED:
        raise ValueError(VIOLATION + str(len(arguments)))
    return {
        ARTIFACT_KEY: arguments[ARTIFACT_ORIGIN],
        IDENTITY_KEY: arguments[IDENTITY_ORIGIN],
        EXPECTED_KEY: arguments[EXPECTED_ORIGIN],
    }
