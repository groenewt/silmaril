from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.table.library import TABLE
from config.gate.external.python.stdlib.csv.writer.library import DEPENDENCY as WRITER
from config.gate.external.python.stdlib.io.text.library import DEPENDENCY as TEXT_BUFFER

LINE_TERMINATOR = "\n"


def RENDER(state: dict) -> str:
    buffer = TEXT_BUFFER()
    WRITER(buffer, lineterminator=LINE_TERMINATOR).writerows(TABLE(state))
    return buffer.getvalue()
