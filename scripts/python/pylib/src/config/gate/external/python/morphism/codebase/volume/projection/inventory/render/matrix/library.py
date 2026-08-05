from config.constants.morphism.codebase.volume.projection.inventory.heading.table.template.value import VALUE as TABLE_HEADING
from config.constants.morphism.codebase.volume.projection.inventory.layout.matrix.value import VALUE as LAYOUT
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.projection.inventory.matrix.cell.separator.value import VALUE as CELL_SEPARATOR
from config.constants.morphism.codebase.volume.projection.inventory.matrix.cell.template.value import VALUE as CELL_TEMPLATE
from config.constants.morphism.codebase.volume.projection.inventory.matrix.close.value import VALUE as CLOSE
from config.constants.morphism.codebase.volume.projection.inventory.matrix.column.template.value import VALUE as COLUMN
from config.constants.morphism.codebase.volume.projection.inventory.matrix.head.template.value import VALUE as HEAD
from config.constants.morphism.codebase.volume.projection.inventory.matrix.open.template.value import VALUE as OPEN
from config.constants.morphism.codebase.volume.projection.inventory.matrix.row.terminator.value import VALUE as TERMINATOR
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import UNGROUPED
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import CELL
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import FIELD


def LINE(header: list, row: list) -> str:
    return CELL_SEPARATOR.join(
        CELL_TEMPLATE % CELL(FIELD(row, index)) for index in range(len(header))
    )


def RENDER(title: str, group: str, header: list, rows: list) -> list:
    UNGROUPED(LAYOUT, group)
    width = len(header)
    specification = EMPTY.join(COLUMN % width for _ in range(width))
    heading = LINE(header, header)
    parts = [TABLE_HEADING % CELL(title), OPEN % specification, HEAD % (heading, heading)]
    for row in rows:
        parts.append(LINE(header, row))
        parts.append(TERMINATOR)
    parts.append(CLOSE)
    return parts
