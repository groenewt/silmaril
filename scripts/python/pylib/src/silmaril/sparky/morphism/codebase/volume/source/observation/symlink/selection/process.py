from config.gate.external.python.morphism.codebase.volume.boundary.read.library import READ
from config.gate.external.python.morphism.codebase.volume.boundary.root.library import ROOT
from config.gate.external.python.morphism.codebase.volume.boundary.write.library import WRITE
from config.gate.external.python.morphism.codebase.volume.source.observation.symlink.boundary.emit.library import EMIT
from config.gate.external.python.morphism.codebase.volume.source.observation.symlink.boundary.input.library import INPUT
from config.gate.external.python.stdlib.os.chdir.library import DEPENDENCY as CHDIR
from silmaril.sparky.morphism.codebase.volume.source.observation.symlink.selection.apply import apply as APPLY


def MAIN() -> int:
    CHDIR(ROOT())
    WRITE(EMIT(APPLY(INPUT(READ()))))
    return 0


raise SystemExit(MAIN())
