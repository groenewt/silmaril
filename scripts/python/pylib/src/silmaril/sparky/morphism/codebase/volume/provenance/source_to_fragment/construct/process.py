from config.gate.external.python.morphism.codebase.volume.boundary.argument.library import READ
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.boundary.argument.library import INPUT
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.boundary.emit.library import EMIT
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.apply import apply as APPLY


def MAIN() -> int:
    WRITE(EMIT(APPLY(INPUT(READ()))))
    return 0


raise SystemExit(MAIN())
