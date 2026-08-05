from config.constants.morphism.codebase.volume.artifact.path.csv.suffix.value import VALUE as CSV_SUFFIX
from config.constants.morphism.codebase.volume.artifact.path.tex.suffix.value import VALUE as TEX_SUFFIX


def TEX_PATH(csv_path: str) -> str:
    return csv_path.removesuffix(CSV_SUFFIX) + TEX_SUFFIX
