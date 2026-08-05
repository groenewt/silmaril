from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: OSError) -> Issue:
    code = value.__class__.__name__.encode("utf-8")
    detail = str(value).encode("utf-8")
    return Issue(ByteVector(code), ByteVector(detail))
