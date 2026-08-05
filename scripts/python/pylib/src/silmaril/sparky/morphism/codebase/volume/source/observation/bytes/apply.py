from config.gate.external.python.morphism.codebase.volume.source.observation.bytes.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.bytes.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.bytes.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
