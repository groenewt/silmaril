from config.constants.morphism.codebase.volume.source.observation.symlink.discovery.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return SUBPROCESS.run(COMMAND, cwd=SYS.argv[1]).returncode


raise SystemExit(MAIN())
