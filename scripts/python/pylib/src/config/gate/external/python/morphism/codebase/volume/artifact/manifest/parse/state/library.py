from config.constants.morphism.codebase.volume.artifact.manifest.state.contract.rows.key.value import VALUE as CONTRACT_ROWS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.path.library import CONTRACT_PATH
from config.gate.external.python.morphism.codebase.volume.boundary.locus.read.library import CONTENT
from config.gate.external.python.morphism.codebase.volume.lexical.lines.library import LINES
from config.gate.external.python.morphism.codebase.volume.lexical.listed.library import LISTED
from config.gate.external.python.morphism.codebase.volume.lexical.locus.library import LOCUS
from config.gate.external.python.morphism.codebase.volume.lexical.text.library import TEXT
from config.gate.external.python.stdlib.csv.reader.library import DEPENDENCY as READER


def STATE(state: dict) -> dict:
    lines = LINES(TEXT(CONTENT(LOCUS(CONTRACT_PATH(state)))))
    return {**state, CONTRACT_ROWS_KEY: LISTED(READER(lines))}
