from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
