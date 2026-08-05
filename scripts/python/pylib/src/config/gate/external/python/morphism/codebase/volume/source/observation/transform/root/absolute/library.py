from config.gate.external.python.morphism.codebase.volume.source.observation.state.root.library import ROOT_OF
from config.gate.external.python.stdlib.os.path.isabs.library import DEPENDENCY as ISABS

VIOLATION = "observation_root_not_absolute="


def STATE(state: dict) -> dict:
    root = ROOT_OF(state)
    if not ISABS(root):
        raise ValueError(VIOLATION + root)
    return state
