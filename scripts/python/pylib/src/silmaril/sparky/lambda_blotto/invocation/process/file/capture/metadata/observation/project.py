from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural

def PROJECT(value) -> Metadata:
    return Metadata(Natural(value.st_dev), Natural(value.st_ino), Natural(value.st_mode), Natural(value.st_nlink), Natural(value.st_uid), Natural(value.st_gid), Natural(value.st_size), Natural(value.st_mtime_ns), Natural(value.st_ctime_ns))
