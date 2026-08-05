from config.constants.morphism.codebase.volume.projection.inventory.list.close.value import VALUE as LIST_CLOSE
from config.constants.morphism.codebase.volume.projection.inventory.list.item.template.value import VALUE as ITEM
from config.constants.morphism.codebase.volume.projection.inventory.list.open.value import VALUE as LIST_OPEN
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import CELL
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import FIELD


def DETAILS(header: list, row: list, indexes: tuple) -> list:
    if not indexes:
        return []
    parts = [LIST_OPEN]
    for index in indexes:
        parts.append(ITEM % (CELL(header[index]), CELL(FIELD(row, index))))
    parts.append(LIST_CLOSE)
    return parts
