from silmaril.sparky.morphism.codebase.volume.projection.filetree.ordinal.value import Value as Ordinal
from silmaril.sparky.morphism.codebase.volume.projection.filetree.selection.value import Value as Selection


def INDEX(selection: Selection) -> int:
    return selection.header.index(selection.column)


def DETAIL_INDEXES(ordinal: Ordinal) -> tuple:
    return tuple(index for index in range(len(ordinal.header)) if index != ordinal.group_index)
