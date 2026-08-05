from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from config.gate.external.python.stdlib.sys.argv.library import DEPENDENCY as ARGV
from silmaril.sparky.morphism.codebase.volume.projection.inventory.input.value import Value as Input

TITLE_POSITION = 1
LAYOUT_POSITION = 2
GROUP_POSITION = 3


def INPUT(payload: bytes) -> Input:
    return Input(
        ByteVector(payload),
        ARGV[TITLE_POSITION],
        ARGV[LAYOUT_POSITION],
        ARGV[GROUP_POSITION],
    )
