from config.constants.morphism.codebase.volume.table.evidence_rows.order.ring.value.normalization.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS


def MAIN() -> int:
    return SUBPROCESS.run(COMMAND).returncode


raise SystemExit(MAIN())
