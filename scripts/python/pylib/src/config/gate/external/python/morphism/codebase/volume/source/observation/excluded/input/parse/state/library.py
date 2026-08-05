from config.constants.morphism.codebase.volume.source.observation.state.paths.key.value import VALUE as PATHS_KEY
from config.constants.morphism.codebase.volume.source.observation.state.prefixes.key.value import VALUE as PREFIXES_KEY
from config.constants.morphism.codebase.volume.source.observation.state.root.key.value import VALUE as ROOT_KEY
from config.gate.external.python.morphism.codebase.volume.boundary.arguments.library import ARGUMENTS
from config.gate.external.python.morphism.codebase.volume.boundary.root.library import ROOT


def STATE(lines: list) -> dict:
    return {ROOT_KEY: ROOT(), PREFIXES_KEY: ARGUMENTS(), PATHS_KEY: lines}
