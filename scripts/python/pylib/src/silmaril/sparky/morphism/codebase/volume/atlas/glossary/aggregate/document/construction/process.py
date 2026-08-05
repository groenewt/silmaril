from config.constants.morphism.codebase.volume.atlas.glossary.aggregate.document.construction.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return SUBPROCESS.run(
        (*COMMAND, SYS.argv[1], SYS.argv[2]),
    ).returncode


raise SystemExit(MAIN())

