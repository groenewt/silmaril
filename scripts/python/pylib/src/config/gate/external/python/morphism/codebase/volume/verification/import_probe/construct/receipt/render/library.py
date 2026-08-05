from config.gate.external.python.morphism.codebase.volume.lexical.csv.materialize.library import MATERIALIZE
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.state.declared.library import DECLARED
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.state.inline.library import INLINE

DECLARED_STATUS = "declared_and_importable"
HEADER = ["coordinate", "module", "status"]
INLINE_STATUS = "inline_recipe_no_module"


def RENDER(state: dict) -> str:
    declared = [[coordinate, module, DECLARED_STATUS] for coordinate, module in DECLARED(state)]
    inline = [[coordinate, module, INLINE_STATUS] for coordinate, module in INLINE(state)]
    return MATERIALIZE([HEADER, *sorted(declared + inline)])
