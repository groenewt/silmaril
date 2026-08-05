from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.sources.key.value import VALUE as SOURCES_KEY

VIOLATION = "hash_manifest_arguments_empty"


def STATE(arguments: list) -> dict:
    if not arguments:
        raise ValueError(VIOLATION)
    return {SOURCES_KEY: list(arguments)}
