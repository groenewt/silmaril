from config.gate.external.python.morphism.codebase.volume.request.binding.repository.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.request.binding.repository.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.request.binding.repository.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
