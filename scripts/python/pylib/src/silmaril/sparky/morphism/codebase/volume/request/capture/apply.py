from config.gate.external.python.morphism.codebase.volume.request.capture.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.request.capture.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.request.capture.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
