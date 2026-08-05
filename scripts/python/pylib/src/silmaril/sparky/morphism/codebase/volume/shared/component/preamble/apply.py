from config.gate.external.python.morphism.codebase.volume.shared.component.preamble.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.preamble.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.preamble.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
