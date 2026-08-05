from config.constants.morphism.codebase.volume.artifact.manifest.inventory.unique.count.value import VALUE as UNIQUE
from config.gate.external.python.morphism.codebase.volume.artifact.path.stem.library import STEM

VIOLATION = "inventory_csv_path_not_unique="
DELIMITER = "="
JOINER = ","


def LOCUS(identity: str, documents: dict) -> str:
    candidates = [path for path in documents if STEM(path) == identity]
    if len(candidates) != UNIQUE:
        raise ValueError(VIOLATION + identity + DELIMITER + JOINER.join(candidates))
    return candidates[0]
