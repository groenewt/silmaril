from config.gate.external.python.morphism.codebase.volume.source.observation.text.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.text.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.text.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
