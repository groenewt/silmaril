from config.gate.external.python.morphism.codebase.volume.inventory.mix_task.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.mix_task.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.mix_task.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
