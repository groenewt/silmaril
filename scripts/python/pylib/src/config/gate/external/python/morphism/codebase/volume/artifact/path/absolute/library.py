from config.constants.morphism.codebase.volume.artifact.path.separator.value import VALUE as SEPARATOR


def ABSOLUTE(path: str) -> bool:
    return path.startswith(SEPARATOR)
