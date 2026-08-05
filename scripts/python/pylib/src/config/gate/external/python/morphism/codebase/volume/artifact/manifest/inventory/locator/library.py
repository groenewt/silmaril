from config.constants.morphism.codebase.volume.artifact.manifest.inventory.csv.path.key.value import VALUE as CSV_PATH_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.inventory.fragment.key.value import VALUE as FRAGMENT_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.inventory.identifier.key.value import VALUE as IDENTIFIER_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.locus.library import LOCUS

VIOLATION = "manifest_inventory_fragment_absent="


def LOCATOR(identity: str, documents: dict, fragments: dict) -> dict:
    if identity not in fragments:
        raise ValueError(VIOLATION + identity)
    return {
        IDENTIFIER_KEY: identity,
        CSV_PATH_KEY: LOCUS(identity, documents),
        FRAGMENT_KEY: fragments[identity],
    }
