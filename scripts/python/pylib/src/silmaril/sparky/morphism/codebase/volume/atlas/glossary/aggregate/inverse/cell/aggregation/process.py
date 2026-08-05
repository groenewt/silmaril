from config.constants.morphism.codebase.volume.atlas.glossary.aggregate.inverse.cell.aggregation.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return SUBPROCESS.run(
        (COMMAND[0], SYS.argv[1], *COMMAND[1:]),
    ).returncode


raise SystemExit(MAIN())

