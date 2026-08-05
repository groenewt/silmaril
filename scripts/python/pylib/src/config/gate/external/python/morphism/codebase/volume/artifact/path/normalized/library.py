from config.constants.morphism.codebase.volume.artifact.path.current.value import VALUE as CURRENT
from config.constants.morphism.codebase.volume.artifact.path.vacant.value import VALUE as VACANT

NOISE = (CURRENT, VACANT)


def NORMALIZED(segments: list) -> list:
    return [segment for segment in segments if segment not in NOISE]
