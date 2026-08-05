from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.os.open.directory.flags.value import VALUE as OPEN_FLAGS
from config.gate.external.python.stdlib.os.open.value import VALUE as OPEN
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.directory.open.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.opened.directory.description.occurrence.value import Value as Opened
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.descriptor.occurrence.value import Value as Descriptor
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.conversion.os.error.project import PROJECT as ISSUE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    try:
        number = OPEN(value.request.locator.value.payload.decode("utf-8", "surrogateescape"), OPEN_FLAGS)
        return Frame(Output(Opened(Descriptor(Natural(number)), value.request)), Effect(ByteVector(APPLIED)))
    except OSError as issue:
        return Frame(Output(ISSUE(issue)), Effect(ByteVector(REJECTED)))
