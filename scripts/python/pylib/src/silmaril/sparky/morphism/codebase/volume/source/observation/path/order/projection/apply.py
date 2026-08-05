from config.gate.external.python.morphism.codebase.volume.source.observation.path.order.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.path.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.path.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
