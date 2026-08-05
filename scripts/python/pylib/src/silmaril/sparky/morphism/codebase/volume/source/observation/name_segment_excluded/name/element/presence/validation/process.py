from config.gate.external.python.morphism.codebase.volume.boundary.read.library import READ
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from config.gate.external.python.morphism.codebase.volume.source.observation.name_segment_excluded.boundary.emit.library import EMIT
from config.gate.external.python.morphism.codebase.volume.source.observation.name_segment_excluded.boundary.input.library import INPUT
from silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.name.element.presence.validation.apply import apply as APPLY


def MAIN() -> int:
    WRITE(EMIT(APPLY(INPUT(READ()))))
    return 0


raise SystemExit(MAIN())
