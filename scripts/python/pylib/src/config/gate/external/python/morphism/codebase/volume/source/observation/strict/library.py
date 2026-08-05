from config.constants.morphism.codebase.volume.source.observation.strict.enabled.value import VALUE as STRICT_ENABLED
from config.constants.morphism.codebase.volume.source.observation.strict.environment.value import VALUE as STRICT_ENVIRONMENT
from config.gate.external.python.stdlib.os.environ.library import DEPENDENCY as ENVIRONMENT


def STRICT() -> bool:
    return ENVIRONMENT.get(STRICT_ENVIRONMENT) == STRICT_ENABLED
