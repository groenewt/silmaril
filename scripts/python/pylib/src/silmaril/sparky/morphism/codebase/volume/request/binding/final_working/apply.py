from config.gate.external.python.morphism.codebase.volume.request.binding.final_working.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.request.binding.final_working.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.request.binding.final_working.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
