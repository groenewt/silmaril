from config.constants.morphism.codebase.volume.projection.filetree.element.close.value import VALUE as CLOSE
from config.constants.morphism.codebase.volume.projection.filetree.element.field.template.value import VALUE as FIELD
from config.constants.morphism.codebase.volume.projection.filetree.element.join.template.value import VALUE as JOIN
from config.constants.morphism.codebase.volume.projection.filetree.element.open.value import VALUE as OPEN
from config.constants.morphism.codebase.volume.projection.filetree.element.table.template.value import VALUE as TABLE
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.gate.external.python.morphism.codebase.volume.projection.filetree.lexical.cell.library import BREAKABLE
from config.gate.external.python.morphism.codebase.volume.projection.filetree.lexical.cell.library import CELL
from silmaril.sparky.morphism.codebase.volume.projection.filetree.cell.value import Value as Cell
from silmaril.sparky.morphism.codebase.volume.projection.filetree.padding.value import Value as Padding


def WIDTH(padding: Padding) -> int:
    return len(padding.header) - len(padding.row)


def PADDED(padding: Padding) -> tuple:
    return tuple(padding.row) + (EMPTY,) * WIDTH(padding)


def VALUE(cell: Cell) -> str:
    return cell.row[cell.shape.group_index]


def FIELDS(cell: Cell) -> str:
    return EMPTY.join(
        FIELD % (CELL(cell.shape.header[index]), BREAKABLE(cell.row[index]))
        for index in cell.shape.detail_indexes
    )


def PROVENANCE(cell: Cell) -> str:
    return JOIN % (CELL(cell.shape.record.relation), CELL(cell.shape.record.column), BREAKABLE(VALUE(cell)))


def ELEMENT(cell: Cell) -> str:
    return EMPTY.join((TABLE % CELL(cell.shape.record.table), OPEN, PROVENANCE(cell), FIELDS(cell), CLOSE))
