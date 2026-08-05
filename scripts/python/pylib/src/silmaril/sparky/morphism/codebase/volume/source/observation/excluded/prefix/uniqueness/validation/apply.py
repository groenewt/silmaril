from config.gate.external.python.morphism.codebase.volume.source.observation.excluded.prefix.uniqueness.validation.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.excluded.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.excluded.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
