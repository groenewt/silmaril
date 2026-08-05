from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.occurrence.serialize.project import PROJECT as OCCURRENCE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.value import Value as Routing
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Routing) -> ByteVector:
    occurrences = ByteVector(b"".join(FIELD(OCCURRENCE(occurrence)).payload for occurrence in value.occurrences))
    fields = (ByteVector(b"lambda-blotto-publication-routing-v4"), value.claim_key, value.volume_route, value.chapter_route, value.appendix_route, occurrences)
    return ByteVector(b"".join(FIELD(field).payload for field in fields))
