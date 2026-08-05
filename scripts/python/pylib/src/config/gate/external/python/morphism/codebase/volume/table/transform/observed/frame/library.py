from config.constants.morphism.codebase.volume.source.observation.state.paths.key.value import VALUE as PATHS_KEY
from config.constants.morphism.codebase.volume.source.observation.state.root.key.value import VALUE as ROOT_KEY
from config.constants.morphism.codebase.volume.table.state.root_id.key.value import VALUE as ROOT_ID_KEY
from config.gate.external.python.morphism.codebase.volume.boundary.arguments.library import ARGUMENTS
from config.gate.external.python.morphism.codebase.volume.boundary.root.library import ROOT
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP

LOCATION_POSITION = 0


def STATE(lines: list) -> dict:
    return {ROOT_ID_KEY: ROOT(), ROOT_KEY: ARGUMENTS()[LOCATION_POSITION], PATHS_KEY: [CHOMP(line) for line in lines]}
