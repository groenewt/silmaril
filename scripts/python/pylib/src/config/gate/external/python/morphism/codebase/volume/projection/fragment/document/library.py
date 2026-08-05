from config.constants.morphism.codebase.volume.projection.fragment.document.separator.value import VALUE as SEPARATOR


def DOCUMENT(parts: tuple) -> str:
    return SEPARATOR.join(parts)
