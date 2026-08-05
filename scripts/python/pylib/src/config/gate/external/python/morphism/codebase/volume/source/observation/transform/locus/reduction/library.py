from config.constants.morphism.codebase.volume.source.observation.state.loci.key.value import VALUE as LOCI_KEY
from config.constants.morphism.codebase.volume.source.observation.state.pathnames.key.value import VALUE as PATHNAMES_KEY
from config.constants.morphism.codebase.volume.source.observation.state.root.key.value import VALUE as ROOT_KEY

DERIVED = (ROOT_KEY, PATHNAMES_KEY, LOCI_KEY)


def STATE(state: dict) -> dict:
    return {key: value for key, value in state.items() if key not in DERIVED}
