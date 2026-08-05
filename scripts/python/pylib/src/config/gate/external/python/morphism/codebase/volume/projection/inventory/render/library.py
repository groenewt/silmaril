from config.constants.morphism.codebase.volume.projection.inventory.layout.filetree.value import VALUE as FILETREE
from config.constants.morphism.codebase.volume.projection.inventory.layout.keyed.value import VALUE as KEYED
from config.constants.morphism.codebase.volume.projection.inventory.layout.matrix.value import VALUE as MATRIX
from config.constants.morphism.codebase.volume.projection.inventory.layout.unknown.message.value import VALUE as UNKNOWN
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.gate.external.python.morphism.codebase.volume.projection.inventory.render.filetree.library import RENDER as FILETREE_RENDER
from config.gate.external.python.morphism.codebase.volume.projection.inventory.render.keyed.library import RENDER as KEYED_RENDER
from config.gate.external.python.morphism.codebase.volume.projection.inventory.render.matrix.library import RENDER as MATRIX_RENDER

RENDERERS = {
    FILETREE: FILETREE_RENDER,
    KEYED: KEYED_RENDER,
    MATRIX: MATRIX_RENDER,
}


def RENDER(layout: str, title: str, group: str, header: list, rows: list) -> str:
    if layout not in RENDERERS:
        raise ValueError(UNKNOWN % layout)
    return EMPTY.join(RENDERERS[layout](title, group, header, rows))
