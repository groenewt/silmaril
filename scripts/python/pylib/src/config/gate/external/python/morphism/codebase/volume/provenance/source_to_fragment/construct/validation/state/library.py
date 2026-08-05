from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.state.relation.library import RELATION
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.state.root.library import ROOT
from config.gate.external.python.stdlib.os.path.join.library import DEPENDENCY as JOIN
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

ARTIFACT_ORIGIN = 1
FRAGMENT_ORIGIN = 2
ROOT_VIOLATION = "source_to_fragment_generated_root_missing="
VIOLATION = "source_to_fragment_locus_missing="


def STATE(state: dict) -> dict:
    root = ROOT(state)
    if not LEXISTS(root):
        raise ValueError(ROOT_VIOLATION + root)
    for entry in RELATION(state):
        for locus in (entry[ARTIFACT_ORIGIN], entry[FRAGMENT_ORIGIN]):
            resolved = JOIN(root, locus)
            if not LEXISTS(resolved):
                raise ValueError(VIOLATION + resolved)
    return state
