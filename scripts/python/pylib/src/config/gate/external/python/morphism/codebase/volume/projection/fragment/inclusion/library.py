from config.constants.morphism.codebase.volume.projection.fragment.inclusion.template.value import VALUE as TEMPLATE


def INCLUSIONS(entries: tuple) -> tuple:
    return tuple(TEMPLATE % entry for entry in entries)
