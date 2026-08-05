from config.constants.morphism.codebase.volume.projection.inventory.heading.directory.template.value import VALUE as DIRECTORY
from config.constants.morphism.codebase.volume.projection.inventory.heading.element.template.value import VALUE as ELEMENT
from config.constants.morphism.codebase.volume.projection.inventory.heading.file.template.value import VALUE as FILE
from config.constants.morphism.codebase.volume.projection.inventory.heading.table.template.value import VALUE as TABLE_HEADING
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import ABSENT_INDEX
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import DETAIL_INDEXES
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import GROUP_INDEX
from config.gate.external.python.morphism.codebase.volume.projection.inventory.columns.library import LABEL_INDEX
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import CELL
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.cell.library import FIELD
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.indent.library import INDENT
from config.gate.external.python.morphism.codebase.volume.projection.inventory.render.element.library import DETAILS
from config.gate.external.python.morphism.codebase.volume.projection.inventory.tree.library import BUCKETS
from config.gate.external.python.morphism.codebase.volume.projection.inventory.tree.library import COMMON
from config.gate.external.python.morphism.codebase.volume.projection.inventory.tree.library import SEGMENTS

LEAF_OFFSET = 1


def RENDER(title: str, group: str, header: list, rows: list) -> list:
    group_index = GROUP_INDEX(header, group)
    label_index = LABEL_INDEX(header, group_index)
    detail_indexes = DETAIL_INDEXES(header, group_index, label_index)
    buckets = BUCKETS(rows, group_index)
    parts = [TABLE_HEADING % CELL(title)]
    previous = ()
    for path in sorted(buckets):
        segments = SEGMENTS(path)
        leaf = len(segments) - LEAF_OFFSET
        for depth in range(COMMON(previous, segments), leaf):
            parts.append(DIRECTORY % (INDENT(depth), CELL(segments[depth])))
        parts.append(FILE % (INDENT(leaf), CELL(segments[leaf])))
        for row in buckets[path]:
            if label_index != ABSENT_INDEX:
                parts.append(ELEMENT % (INDENT(leaf + LEAF_OFFSET), CELL(FIELD(row, label_index))))
            parts.extend(DETAILS(header, row, detail_indexes))
        previous = segments
    return parts
