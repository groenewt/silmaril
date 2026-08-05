from config.constants.morphism.codebase.volume.inventory.catalog_claims.projection.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return SUBPROCESS.run(
        (COMMAND[0], SYS.argv[2], *COMMAND[1:]),
        cwd=SYS.argv[1],
    ).returncode


raise SystemExit(MAIN())
