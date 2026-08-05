from config.constants.morphism.codebase.volume.artifact.hash_line.state.artifact.key.value import VALUE as ARTIFACT_KEY
from config.constants.morphism.codebase.volume.artifact.hash_line.state.path.key.value import VALUE as PATH_KEY

VIOLATION = "hash_line_arguments_expected_2_received="
EXPECTED = 2
ARTIFACT_ORIGIN = 0
PATH_ORIGIN = 1


def STATE(arguments: list) -> dict:
    if len(arguments) != EXPECTED:
        raise ValueError(VIOLATION + str(len(arguments)))
    return {ARTIFACT_KEY: arguments[ARTIFACT_ORIGIN], PATH_KEY: arguments[PATH_ORIGIN]}
