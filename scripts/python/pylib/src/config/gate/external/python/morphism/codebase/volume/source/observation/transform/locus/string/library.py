from config.constants.morphism.codebase.volume.source.observation.state.loci.key.value import VALUE as LOCI_KEY
from config.constants.morphism.codebase.volume.source.observation.state.paths.key.value import VALUE as PATHS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.loci.library import LOCI
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS


def STATE(state: dict) -> dict:
    return {PATHS_KEY: PATHS(state), LOCI_KEY: [str(locus) for locus in LOCI(state)]}
