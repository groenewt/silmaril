from config.constants.morphism.codebase.volume.projection.filetree.census.close.value import VALUE as CLOSE
from config.constants.morphism.codebase.volume.projection.filetree.census.item.template.value import VALUE as ITEM
from config.constants.morphism.codebase.volume.projection.filetree.census.lead.value import VALUE as LEAD
from config.constants.morphism.codebase.volume.projection.filetree.census.open.value import VALUE as OPEN
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.gate.external.python.morphism.codebase.volume.projection.filetree.lexical.cell.library import CELL
from silmaril.sparky.morphism.codebase.volume.projection.filetree.record.value import Value as Record


def ROW(record: Record) -> str:
    return ITEM % (CELL(record.table), CELL(record.relation), CELL(record.column))


def ROWS(records: tuple) -> str:
    return EMPTY.join(ROW(record) for record in records)


def CENSUS(records: tuple) -> str:
    return EMPTY.join((LEAD, OPEN, ROWS(records), CLOSE))
