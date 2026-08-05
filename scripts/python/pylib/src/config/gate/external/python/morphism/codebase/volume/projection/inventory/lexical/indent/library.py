from config.constants.morphism.codebase.volume.projection.inventory.indent.limit.value import VALUE as LIMIT
from config.constants.morphism.codebase.volume.projection.inventory.indent.step.value import VALUE as STEP
from config.constants.morphism.codebase.volume.projection.inventory.indent.template.value import VALUE as TEMPLATE
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY

ORIGIN = 0


def INDENT(depth: int) -> str:
    clamped = depth if depth < LIMIT else LIMIT
    if clamped <= ORIGIN:
        return EMPTY
    return TEMPLATE % (clamped * STEP)
