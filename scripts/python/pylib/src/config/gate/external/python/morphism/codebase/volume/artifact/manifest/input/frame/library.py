from config.gate.external.python.morphism.codebase.volume.artifact.manifest.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.input.frame.state.library import STATE
from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.frame.value import Value as Frame


def PROJECT(arguments: list) -> Frame:
    return FRAME(ENCODE(STATE(arguments)))
