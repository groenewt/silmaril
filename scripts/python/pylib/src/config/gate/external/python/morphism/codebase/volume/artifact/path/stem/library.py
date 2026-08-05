from config.constants.morphism.codebase.volume.artifact.path.csv.suffix.value import VALUE as CSV_SUFFIX
from config.gate.external.python.morphism.codebase.volume.artifact.path.name.library import NAME


def STEM(path: str) -> str:
    return NAME(path).removesuffix(CSV_SUFFIX)
