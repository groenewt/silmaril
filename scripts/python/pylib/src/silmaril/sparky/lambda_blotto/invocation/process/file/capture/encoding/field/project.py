from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: ByteVector) -> ByteVector:
    return ByteVector(len(value.payload).to_bytes(8, "big") + value.payload)
