from config.constants.morphism.codebase.volume.provenance.source_to_fragment.fragment.missing.selection.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS


def MAIN() -> int:
    return SUBPROCESS.run(COMMAND).returncode


raise SystemExit(MAIN())
