from config.gate.external.python.morphism.codebase.volume.evidence.status.library import STATUS
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS


def SEARCH(command: tuple) -> int:
    return STATUS(SUBPROCESS.run(command).returncode)
