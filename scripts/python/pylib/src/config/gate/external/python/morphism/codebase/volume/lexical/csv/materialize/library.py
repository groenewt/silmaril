from config.gate.external.python.stdlib.csv.writer.library import DEPENDENCY as WRITER
from config.gate.external.python.stdlib.io.string_io.library import DEPENDENCY as StringIO

LINE_FEED = "\n"


def MATERIALIZE(rows: list) -> str:
    buffer = StringIO()
    writer = WRITER(buffer, lineterminator=LINE_FEED)
    writer.writerows(rows)
    return buffer.getvalue()
