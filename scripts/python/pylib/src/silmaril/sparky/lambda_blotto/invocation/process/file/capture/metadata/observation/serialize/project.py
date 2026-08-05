from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Metadata) -> ByteVector:
    fields = (value.device, value.inode, value.mode, value.link_count, value.user, value.group, value.size, value.modified_nanoseconds, value.changed_nanoseconds)
    return ByteVector(b"".join(field.value.to_bytes(16, "big", signed=False) for field in fields))
