from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from silmaril.sparky.morphism.codebase.volume.verification.import_probe.input.value import Value as Input


def INPUT(arguments: list) -> Input:
    return Input(ENCODE(arguments))
