from config.constants.morphism.codebase.volume.artifact.path.separator.value import VALUE as SEPARATOR


def PATHNAME(segments: list) -> str:
    return SEPARATOR.join(segments)
