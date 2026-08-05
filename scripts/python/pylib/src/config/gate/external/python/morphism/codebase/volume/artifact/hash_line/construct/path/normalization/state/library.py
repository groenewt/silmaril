from config.constants.morphism.codebase.volume.artifact.hash_line.state.pathname.key.value import VALUE as PATHNAME_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.pathname.library import PATHNAME
from config.gate.external.python.morphism.codebase.volume.lexical.relative.library import RELATIVE
from config.gate.external.python.stdlib.os.path.normpath.library import DEPENDENCY as NORMPATH


def STATE(state: dict) -> dict:
    return {**state, PATHNAME_KEY: RELATIVE(NORMPATH(PATHNAME(state)))}
