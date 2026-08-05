from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.pathnames.key.value import VALUE as PATHNAMES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.pathnames.library import PATHNAMES
from config.gate.external.python.morphism.codebase.volume.lexical.relative.library import RELATIVE
from config.gate.external.python.stdlib.os.path.normpath.library import DEPENDENCY as NORMPATH


def STATE(state: dict) -> dict:
    return {**state, PATHNAMES_KEY: [RELATIVE(NORMPATH(pathname)) for pathname in PATHNAMES(state)]}
