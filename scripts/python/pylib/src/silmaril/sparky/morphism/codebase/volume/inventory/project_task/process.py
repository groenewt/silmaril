from config.constants.morphism.codebase.volume.inventory.project_task.command.value import VALUE as COMMAND
from config.gate.external.python.morphism.codebase.volume.evidence.status.library import STATUS
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return STATUS(
        SUBPROCESS.run(
            COMMAND,
            cwd=SYS.argv[1],
        ).returncode
    )


raise SystemExit(MAIN())
