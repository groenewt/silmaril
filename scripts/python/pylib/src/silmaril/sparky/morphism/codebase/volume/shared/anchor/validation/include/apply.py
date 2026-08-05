from config.gate.external.python.morphism.codebase.volume.shared.anchor.validation.include.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.include.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.include.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
