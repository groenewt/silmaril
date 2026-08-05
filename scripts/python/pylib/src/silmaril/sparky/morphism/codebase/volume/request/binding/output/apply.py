from config.gate.external.python.morphism.codebase.volume.request.binding.output.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.request.binding.output.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.request.binding.output.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
