from config.gate.external.python.morphism.codebase.volume.table.mix_tasks.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.mix_tasks.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.mix_tasks.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
