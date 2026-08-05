from config.gate.external.python.morphism.codebase.volume.source.observation.state.root.library import ROOT_OF
from config.gate.external.python.stdlib.os.path.isdir.library import DEPENDENCY as ISDIR

VIOLATION = "observation_root_not_directory="


def STATE(state: dict) -> dict:
    root = ROOT_OF(state)
    if not ISDIR(root):
        raise ValueError(VIOLATION + root)
    return state
