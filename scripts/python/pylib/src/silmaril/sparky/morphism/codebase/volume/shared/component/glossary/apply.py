from config.gate.external.python.morphism.codebase.volume.shared.component.glossary.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.glossary.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.glossary.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
