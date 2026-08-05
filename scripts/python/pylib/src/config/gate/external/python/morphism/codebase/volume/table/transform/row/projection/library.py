from config.constants.morphism.codebase.volume.table.state.rows.key.value import VALUE as ROWS_KEY
from config.gate.external.python.morphism.codebase.volume.table.state.root.identity.library import ROOT_ID
from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.loci.library import LOCI
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS

OBSERVED = "observed"
NO_GAP = ""


def STATE(state: dict) -> dict:
    identity = ROOT_ID(state)
    paths = PATHS(state)
    loci = LOCI(state)
    return {**state, ROWS_KEY: [[identity, paths[index], loci[index], OBSERVED, NO_GAP] for index in INDICES(state)]}
