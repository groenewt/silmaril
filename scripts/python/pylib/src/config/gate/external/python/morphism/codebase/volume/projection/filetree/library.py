from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.projection.filetree.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.projection.filetree.manifest.library import MANIFEST
from config.gate.external.python.morphism.codebase.volume.projection.filetree.render.library import RENDER
from config.gate.external.python.morphism.codebase.volume.projection.filetree.vector.library import VECTOR
from silmaril.sparky.morphism.codebase.volume.projection.filetree.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.filetree.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(MANIFEST(PAYLOAD(VALUE(value))))))
