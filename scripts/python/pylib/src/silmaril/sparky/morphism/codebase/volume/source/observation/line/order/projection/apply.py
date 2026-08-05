from config.gate.external.python.morphism.codebase.volume.source.observation.line.order.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.line.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.line.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
