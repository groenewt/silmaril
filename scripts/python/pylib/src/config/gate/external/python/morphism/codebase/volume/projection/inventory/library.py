from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.projection.inventory.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.projection.inventory.render.library import RENDER
from config.gate.external.python.morphism.codebase.volume.projection.inventory.request.library import GROUP
from config.gate.external.python.morphism.codebase.volume.projection.inventory.request.library import LAYOUT
from config.gate.external.python.morphism.codebase.volume.projection.inventory.request.library import TITLE
from config.gate.external.python.morphism.codebase.volume.projection.inventory.table.library import BODY
from config.gate.external.python.morphism.codebase.volume.projection.inventory.table.library import HEADER
from config.gate.external.python.morphism.codebase.volume.projection.inventory.table.library import TABLE
from config.gate.external.python.morphism.codebase.volume.projection.inventory.vector.library import VECTOR
from silmaril.sparky.morphism.codebase.volume.projection.inventory.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.inventory.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    rows = TABLE(PAYLOAD(VALUE(value)))
    return FRAME(
        VECTOR(
            RENDER(
                LAYOUT(value),
                TITLE(value),
                GROUP(value),
                HEADER(rows),
                BODY(rows),
            )
        )
    )
