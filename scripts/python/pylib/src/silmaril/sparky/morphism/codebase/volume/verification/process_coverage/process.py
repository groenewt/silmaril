from config.gate.external.python.morphism.codebase.volume.boundary.argument.library import READ
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.boundary.argument.library import INPUT
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.boundary.emit.library import EMIT
from silmaril.sparky.morphism.codebase.volume.verification.process_coverage.apply import apply as APPLY


def MAIN() -> int:
    WRITE(EMIT(APPLY(INPUT(READ()))))
    return 0


raise SystemExit(MAIN())
