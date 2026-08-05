from config.gate.external.python.stdlib.csv.writer.library import DEPENDENCY as WRITER
from config.gate.external.python.stdlib.io.text.library import DEPENDENCY as TEXT_BUFFER

LINE_TERMINATOR = "\n"


def ENCODE_TABLE(rows: list) -> str:
    buffer = TEXT_BUFFER()
    WRITER(buffer, lineterminator=LINE_TERMINATOR).writerows(rows)
    return buffer.getvalue()
