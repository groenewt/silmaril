from config.constants.morphism.codebase.volume.source.observation.state.loci.key.value import VALUE as LOCI_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.pathnames.library import PATHNAMES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.root.library import ROOT_OF
from config.gate.external.python.stdlib.os.path.join.library import DEPENDENCY as JOIN


def STATE(state: dict) -> dict:
    root = ROOT_OF(state)
    return {**state, LOCI_KEY: [JOIN(root, pathname) for pathname in PATHNAMES(state)]}
