from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.os.fsencode.value import VALUE as FSENCODE
from config.gate.external.python.stdlib.os.listdir.value import VALUE as LISTDIR
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.end.value import Value as End
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observation.value import Value as Name
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observe.one.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observe.one.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observe.one.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observe.one.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.conversion.os.error.project import PROJECT as ISSUE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    try:
        names = sorted(map(FSENCODE, LISTDIR(value.opened.descriptor.number.value)))
        total = len(names)
        limit = value.opened.request.maximum_entries.value
        if value.ordinal.value >= total or value.ordinal.value >= limit:
            bounded = b"bounded" if total > limit else b"unbounded"
            return Frame(Output(End(Natural(total), ByteVector(bounded))), Effect(ByteVector(APPLIED)))
        observed = Name(ByteVector(names[value.ordinal.value]), value.ordinal, Natural(total))
        return Frame(Output(observed), Effect(ByteVector(APPLIED)))
    except OSError as issue:
        return Frame(Output(ISSUE(issue)), Effect(ByteVector(REJECTED)))
