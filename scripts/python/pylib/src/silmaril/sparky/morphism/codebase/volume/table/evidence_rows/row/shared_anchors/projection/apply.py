from config.gate.external.python.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.evidence_rows.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.evidence_rows.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
