from config.gate.external.python.morphism.codebase.volume.provenance.source_to_claim.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_claim.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_claim.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
