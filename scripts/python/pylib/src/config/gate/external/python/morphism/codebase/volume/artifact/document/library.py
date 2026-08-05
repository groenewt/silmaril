from config.constants.morphism.codebase.volume.artifact.document.encoding.value import VALUE as ENCODING
from config.constants.morphism.codebase.volume.artifact.document.mode.value import VALUE as MODE
from config.constants.morphism.codebase.volume.artifact.document.newline.value import VALUE as NEWLINE
from config.gate.external.python.stdlib.builtins.open.library import DEPENDENCY as OPEN
from config.gate.external.python.stdlib.csv.reader.library import DEPENDENCY as READER


def DOCUMENT(path: str) -> list:
    with OPEN(path, MODE, encoding=ENCODING, newline=NEWLINE) as handle:
        return [row for row in READER(handle)]
