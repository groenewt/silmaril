from config.gate.external.python.morphism.codebase.volume.provenance.claim.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.provenance.claim.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.provenance.claim.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
