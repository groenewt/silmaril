from config.constants.morphism.codebase.volume.artifact.manifest.inventory.tex.path.key.value import VALUE as TEX_PATH_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.state.inventories.key.value import VALUE as INVENTORIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.csv.path.library import CSV_PATH
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventories.library import INVENTORIES
from config.gate.external.python.morphism.codebase.volume.artifact.path.tex.library import TEX_PATH


def STATE(state: dict) -> dict:
    return {**state, INVENTORIES_KEY: [{**inventory, TEX_PATH_KEY: TEX_PATH(CSV_PATH(inventory))} for inventory in INVENTORIES(state)]}
