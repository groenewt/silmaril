from config.constants.morphism.codebase.volume.source.observation.state.loci.key.value import VALUE as LOCI_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.loci.library import LOCI
from config.gate.external.python.stdlib.os.path.normpath.library import DEPENDENCY as NORMPATH


def STATE(state: dict) -> dict:
    return {**state, LOCI_KEY: [NORMPATH(locus) for locus in LOCI(state)]}
