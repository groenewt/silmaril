from config.constants.morphism.codebase.volume.artifact.strict.disabled.value import VALUE as STRICT_DISABLED
from config.constants.morphism.codebase.volume.artifact.strict.environment.value import VALUE as STRICT_ENVIRONMENT
from config.gate.external.python.stdlib.os.environ.library import DEPENDENCY as ENVIRONMENT


def STRICT() -> bool:
    return ENVIRONMENT.get(STRICT_ENVIRONMENT) != STRICT_DISABLED
