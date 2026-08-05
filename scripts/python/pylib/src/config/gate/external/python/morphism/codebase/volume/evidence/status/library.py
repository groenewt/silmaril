from config.constants.morphism.codebase.volume.evidence.search.absent.status.value import VALUE as ABSENT

SUCCESS = 0


def STATUS(status: int) -> int:
    if status == ABSENT:
        return SUCCESS
    return status
