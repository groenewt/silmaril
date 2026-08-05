from config.constants.morphism.codebase.volume.artifact.path.separator.value import VALUE as SEPARATOR


def SEGMENTS(path: str) -> list:
    return path.split(SEPARATOR)
