from config.constants.morphism.codebase.volume.projection.inventory.group.absent.message.value import VALUE as GROUP_ABSENT
from config.constants.morphism.codebase.volume.projection.inventory.group.present.message.value import VALUE as GROUP_PRESENT
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY

ABSENT_INDEX = -1


def GROUP_INDEX(header: list, group: str) -> int:
    if group not in header:
        raise ValueError(GROUP_ABSENT % (group, header))
    return header.index(group)


def UNGROUPED(layout: str, group: str) -> str:
    if group != EMPTY:
        raise ValueError(GROUP_PRESENT % (layout, group))
    return group


def LABEL_INDEX(header: list, group_index: int) -> int:
    for index in range(len(header)):
        if index != group_index:
            return index
    return ABSENT_INDEX


def DETAIL_INDEXES(header: list, group_index: int, label_index: int) -> tuple:
    return tuple(
        index
        for index in range(len(header))
        if index != group_index and index != label_index
    )
