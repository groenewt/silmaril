from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.dependency.library import DEPENDENCIES
from config.gate.external.python.stdlib.importlib.library import DEPENDENCY as IMPORTLIB
from config.gate.external.python.stdlib.importlib.util.library import DEPENDENCY as IMPORTLIB_UTIL

ABSENT = "ModuleNotFoundError: no spec for declared module"
RESOLVED = ""
SOURCELESS = "ImportError: declared module spec carries no source origin"


def RESOLUTION(module: str) -> str:
    try:
        spec = IMPORTLIB_UTIL.find_spec(module)
    except (ImportError, SyntaxError) as error:
        return repr(error)
    if spec is None:
        return ABSENT
    if spec.origin is None:
        return SOURCELESS
    for dependency in DEPENDENCIES(spec.origin, spec.parent):
        try:
            IMPORTLIB.import_module(dependency)
        except (ImportError, SyntaxError) as error:
            return repr(error)
    return RESOLVED
