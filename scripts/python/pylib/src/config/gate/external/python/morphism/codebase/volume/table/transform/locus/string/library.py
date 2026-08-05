from config.constants.morphism.codebase.volume.source.observation.state.loci.key.value import VALUE as LOCI_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.loci.library import LOCI


def STATE(state: dict) -> dict:
    return {**state, LOCI_KEY: [str(locus) for locus in LOCI(state)]}
