from config.constants.morphism.codebase.volume.artifact.path.csv.suffix.value import VALUE as CSV_SUFFIX


def CSV_ARTIFACT(path: str) -> bool:
    return path.endswith(CSV_SUFFIX)
