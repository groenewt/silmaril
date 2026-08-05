from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.boundary.argument.library import INPUT
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.boundary.emit.library import EMIT
from config.gate.external.python.morphism.codebase.volume.boundary.argument.library import READ
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.input.parse.apply import apply as APPLY


def MAIN() -> int:
    WRITE(EMIT(APPLY(INPUT(READ()))))
    return 0


raise SystemExit(MAIN())
