from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.loci.library import LOCI
from config.gate.external.python.stdlib.os.path.isfile.library import DEPENDENCY as ISFILE


def STATE(state: dict) -> dict:
    loci = LOCI(state)
    return {**state, INDICES_KEY: [index for index in INDICES(state) if ISFILE(loci[index])]}
