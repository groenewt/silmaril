from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.loci.library import LOCI
from config.gate.external.python.stdlib.os.path.islink.library import DEPENDENCY as ISLINK


def STATE(state: dict) -> dict:
    return {**state, INDICES_KEY: [index for index, locus in enumerate(LOCI(state)) if not ISLINK(locus)]}
