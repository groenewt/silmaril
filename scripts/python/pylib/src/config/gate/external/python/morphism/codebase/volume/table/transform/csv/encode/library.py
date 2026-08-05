from config.gate.external.python.morphism.codebase.volume.table.state.rows.library import ROWS
from config.gate.external.python.stdlib.csv.writer.library import DEPENDENCY as WRITER
from config.gate.external.python.stdlib.io.text.library import DEPENDENCY as TEXT_BUFFER

LINE_TERMINATOR = "\n"


def RENDER(state: dict) -> str:
    buffer = TEXT_BUFFER()
    WRITER(buffer, lineterminator=LINE_TERMINATOR).writerows(ROWS(state))
    return buffer.getvalue()
