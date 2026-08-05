from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.gate.external.python.stdlib.stat.classifiers.value import BLOCK, CHARACTER, DIRECTORY, FIFO, LINK, REGULAR, SOCKET
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classification.value import Value as Classification
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classify.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classify.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classify.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classify.output.value import Value as Output
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    mode = value.metadata.mode.value
    kind = b"regular" if REGULAR(mode) else b"directory" if DIRECTORY(mode) else b"link" if LINK(mode) else b"block" if BLOCK(mode) else b"character" if CHARACTER(mode) else b"fifo" if FIFO(mode) else b"socket" if SOCKET(mode) else b"unknown"
    return Frame(Output(Classification(ByteVector(kind), ByteVector(b"no-follow"))), Effect(ByteVector(APPLIED)))
