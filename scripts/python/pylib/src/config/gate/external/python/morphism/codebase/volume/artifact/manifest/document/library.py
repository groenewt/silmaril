from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from config.gate.external.python.stdlib.json.library import DEPENDENCY as JSON

TERMINATOR = "\n"


def DOCUMENT(value: object) -> ByteVector:
    payload = JSON.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=False,
    )
    return ByteVector((payload + TERMINATOR).encode(ENCODING.decode()))
