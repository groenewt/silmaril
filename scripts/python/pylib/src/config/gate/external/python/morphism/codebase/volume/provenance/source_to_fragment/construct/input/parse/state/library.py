from config.constants.morphism.codebase.volume.provenance.source_to_fragment.state.contract.key.value import VALUE as CONTRACT_KEY
from config.constants.morphism.codebase.volume.provenance.source_to_fragment.state.root.key.value import VALUE as ROOT_KEY

CONTRACT_ORIGIN = 0
EXPECTED = 2
ROOT_ORIGIN = 1
VIOLATION = "source_to_fragment_arguments_expected_2_received="


def STATE(arguments: list) -> dict:
    if len(arguments) != EXPECTED:
        raise ValueError(VIOLATION + str(len(arguments)))
    return {
        CONTRACT_KEY: arguments[CONTRACT_ORIGIN],
        ROOT_KEY: arguments[ROOT_ORIGIN],
    }
