from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.accumulate.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.accumulate.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.accumulate.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.accumulate.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.frame.value import Value as Child
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.directory.work.value import Value as DirectoryWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frontier.value import Value as Frontier
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.serialize.project import PROJECT as SERIALIZE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    child = Child(value.name, value.metadata, value.classification, value.hidden, value.dispatch)
    dispatch_identity = value.dispatch.reason if hasattr(value.dispatch, "reason") else value.dispatch.state.request.locator.value if isinstance(value.dispatch, FileWork) else value.dispatch.request.locator.value
    child_material = FIELD(value.name.name).payload + FIELD(SERIALIZE(value.metadata)).payload + FIELD(value.classification.kind).payload + FIELD(value.hidden.decision).payload + FIELD(dispatch_identity).payload
    directories = value.accumulator.frontier.directories + ((value.dispatch,) if isinstance(value.dispatch, DirectoryWork) else ())
    files = value.accumulator.frontier.files + ((value.dispatch,) if isinstance(value.dispatch, FileWork) else ())
    frontier = Frontier(directories, files, Natural(value.accumulator.frontier.observed_children.value + 1))
    initialized = value.accumulator.initialized_identity.payload == b"initialized"
    drift = value.accumulator.drift_identity.payload == b"drift" or (initialized and value.accumulator.expected_total.value != value.name.observed_total.value)
    expected = value.accumulator.expected_total if initialized else value.name.observed_total
    serialized_children = ByteVector(value.accumulator.serialized_children.payload + FIELD(ByteVector(child_material)).payload)
    result = Accumulator(value.accumulator.children + (child,), serialized_children, frontier, Natural(value.name.ordinal.value + 1), expected, ByteVector(b"initialized"), ByteVector(b"drift" if drift else b"stable-count"))
    return Frame(Output(result), Effect(ByteVector(APPLIED)))
