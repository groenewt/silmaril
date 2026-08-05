from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector


def VECTOR(document: str) -> ByteVector:
    return ByteVector(document.encode(ENCODING.decode()))
