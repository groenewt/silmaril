from config.constants.morphism.ontology.consolidation.corpus.tally.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return SUBPROCESS.run(COMMAND, cwd=SYS.argv[1]).returncode


raise SystemExit(MAIN())
