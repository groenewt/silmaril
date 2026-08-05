from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from config.gate.external.python.stdlib.os.stat.value import VALUE as STAT
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.metadata.observe.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.metadata.observe.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.metadata.observe.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.metadata.observe.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.conversion.os.error.project import PROJECT as ISSUE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.project import PROJECT as METADATA
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    try:
        observed = STAT(value.name.name.payload, dir_fd=value.opened.descriptor.number.value, follow_symlinks=False)
        return Frame(Output(METADATA(observed)), Effect(ByteVector(APPLIED)))
    except OSError as issue:
        return Frame(Output(ISSUE(issue)), Effect(ByteVector(REJECTED)))
