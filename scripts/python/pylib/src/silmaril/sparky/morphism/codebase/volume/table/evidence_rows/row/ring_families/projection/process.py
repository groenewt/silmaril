from config.gate.external.python.morphism.codebase.volume.boundary.read.library import READ
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from config.gate.external.python.morphism.codebase.volume.table.evidence.boundary.emit.library import EMIT
from config.gate.external.python.morphism.codebase.volume.table.evidence.boundary.input.library import INPUT
from silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.apply import apply as APPLY


def MAIN() -> int:
    WRITE(EMIT(APPLY(INPUT(READ()))))
    return 0


raise SystemExit(MAIN())
