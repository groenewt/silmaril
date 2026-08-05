from config.constants.morphism.codebase.volume.table.evidence.state.family.key.value import VALUE as FAMILY_KEY
from config.constants.morphism.codebase.volume.table.evidence.state.identifier.key.value import VALUE as IDENTIFIER_KEY
from config.constants.morphism.codebase.volume.table.evidence.state.label.key.value import VALUE as LABEL_KEY
from config.constants.morphism.codebase.volume.table.evidence.state.name.key.value import VALUE as NAME_KEY
from config.constants.morphism.codebase.volume.table.evidence.state.records.key.value import VALUE as RECORDS_KEY
from config.gate.external.python.morphism.codebase.volume.boundary.arguments.library import ARGUMENTS
from config.gate.external.python.morphism.codebase.volume.boundary.root.library import ROOT

IDENTIFIER_POSITION = 0
LABEL_POSITION = 1
NAME_POSITION = 2


def STATE(lines: list) -> dict:
    arguments = ARGUMENTS()
    return {FAMILY_KEY: ROOT(), IDENTIFIER_KEY: arguments[IDENTIFIER_POSITION], LABEL_KEY: arguments[LABEL_POSITION], NAME_KEY: arguments[NAME_POSITION] if len(arguments) > NAME_POSITION else arguments[LABEL_POSITION], RECORDS_KEY: list(lines)}
