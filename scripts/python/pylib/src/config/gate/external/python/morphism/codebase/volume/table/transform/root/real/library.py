from config.constants.morphism.codebase.volume.source.observation.state.root.key.value import VALUE as ROOT_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.root.library import ROOT_OF
from config.gate.external.python.stdlib.os.path.realpath.library import DEPENDENCY as REALPATH


def STATE(state: dict) -> dict:
    return {**state, ROOT_KEY: REALPATH(ROOT_OF(state))}
