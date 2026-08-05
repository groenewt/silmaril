from config.gate.external.python.morphism.codebase.volume.table.shared_anchors.aggregate.uniqueness.result.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.shared_anchors.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.shared_anchors.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
