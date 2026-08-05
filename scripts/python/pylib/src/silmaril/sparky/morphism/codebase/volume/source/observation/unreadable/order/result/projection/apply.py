from config.gate.external.python.morphism.codebase.volume.source.observation.unreadable.order.result.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
