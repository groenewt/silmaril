from config.constants.morphism.codebase.volume.projection.inventory.heading.group.template.value import VALUE as GROUP_HEADING
from config.constants.morphism.codebase.volume.projection.inventory.heading.record.template.value import VALUE as RECORD_HEADING
from config.constants.morphism.codebase.volume.projection.inventory.heading.table.template.value import VALUE as TABLE_HEADING
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import ABSENT_INDEX
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import DETAIL_INDEXES
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import GROUP_INDEX
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import LABEL_INDEX
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import CELL
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import FIELD
from config.gate.external.python.morphism.codebase.volume.projection.inventory.render.element.library import DETAILS
from config.gate.external.python.morphism.codebase.volume.projection.inventory.tree.library import BUCKETS


def RENDER(title: str, group: str, header: list, rows: list) -> list:
    group_index = GROUP_INDEX(header, group)
    label_index = LABEL_INDEX(header, group_index)
    detail_indexes = DETAIL_INDEXES(header, group_index, label_index)
    buckets = BUCKETS(rows, group_index)
    parts = [TABLE_HEADING % CELL(title)]
    for key in sorted(buckets):
        parts.append(GROUP_HEADING % CELL(key))
        for row in buckets[key]:
            if label_index != ABSENT_INDEX:
                parts.append(RECORD_HEADING % CELL(FIELD(row, label_index)))
            parts.extend(DETAILS(header, row, detail_indexes))
    return parts
