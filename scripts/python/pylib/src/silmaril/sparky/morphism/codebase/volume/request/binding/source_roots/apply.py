from config.gate.external.python.morphism.codebase.volume.request.binding.source_roots.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.request.binding.source_roots.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.request.binding.source_roots.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
