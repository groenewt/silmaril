from config.gate.external.python.morphism.codebase.volume.artifact.manifest.boundary.emit.library import EMIT
from config.gate.external.python.morphism.codebase.volume.boundary.arguments.library import ARGUMENTS
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.input.frame.apply import apply as APPLY


def MAIN() -> int:
    WRITE(EMIT(APPLY(ARGUMENTS())))
    return 0


raise SystemExit(MAIN())
