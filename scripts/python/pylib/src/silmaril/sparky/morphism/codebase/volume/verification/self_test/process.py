from config.constants.morphism.codebase.volume.verification.self_test.process.command.value import VALUE as COMMAND
from config.constants.morphism.codebase.volume.verification.self_test.process.expected.value import VALUE as EXPECTED
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return SUBPROCESS.run(
        (
            COMMAND,
            SYS.argv[1],
            "=",
            EXPECTED,
        )
    ).returncode


raise SystemExit(MAIN())
