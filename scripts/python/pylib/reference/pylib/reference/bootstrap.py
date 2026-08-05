from config.gate.external.python.stdlib.builtins.library import DEPENDENCY as BUILTINS
from config.gate.external.python.stdlib.importlib.library import DEPENDENCY as IMPORTLIB
from config.constants.runtime.module.path.value import VALUE as RUNTIME_MODULE
from config.constants.runtime.symbol.entry.value import VALUE as ENTRY_SYMBOL

def resolve(frame): return BUILTINS.getattr(IMPORTLIB.import_module(RUNTIME_MODULE), ENTRY_SYMBOL)(frame)
