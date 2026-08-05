from config.constants.morphism.codebase.volume.atlas.glossary.aggregate.environment.header_source_path.value import VALUE as HEADER_SOURCE_PATH
from config.constants.morphism.codebase.volume.atlas.glossary.aggregate.header.source.parse.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.os.library import DEPENDENCY as OS
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    return SUBPROCESS.run(
        (COMMAND[0], SYS.argv[1], *COMMAND[1:]),
        env=OS.environ | {HEADER_SOURCE_PATH: SYS.argv[2]},
    ).returncode


raise SystemExit(MAIN())

