from config.gate.external.python.morphism.codebase.volume.artifact.manifest.boundary.emit.library import EMIT
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.boundary.input.library import INPUT
from config.gate.external.python.morphism.codebase.volume.boundary.read.library import READ
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.identity.index.existence.validation.apply import apply as APPLY


def MAIN() -> int:
    WRITE(EMIT(APPLY(INPUT(READ()))))
    return 0


raise SystemExit(MAIN())
