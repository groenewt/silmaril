from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.accumulate.value import Value as AwaitingAccumulate
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.child.metadata.value import Value as AwaitingChildMetadata
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.classification.value import Value as AwaitingClassification
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.close.value import Value as AwaitingClose
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.dispatch.value import Value as AwaitingDispatch
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.failure.close.value import Value as AwaitingFailureClose
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.frame.value import Value as AwaitingFrame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.hidden.value import Value as AwaitingHidden
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.name.value import Value as AwaitingName
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.open.value import Value as AwaitingOpen
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.post.value import Value as AwaitingPost
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.pre.value import Value as AwaitingPre
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.readback.value import Value as AwaitingReadback
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.revision.value import Value as AwaitingRevision
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.seal.value import Value as AwaitingSeal
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.complete.value import Value as Complete
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.failed.value import Value as Failed

Value = AwaitingOpen | AwaitingPre | AwaitingName | AwaitingChildMetadata | AwaitingClassification | AwaitingHidden | AwaitingDispatch | AwaitingAccumulate | AwaitingPost | AwaitingClose | AwaitingFailureClose | AwaitingFrame | AwaitingRevision | AwaitingSeal | AwaitingReadback | Complete | Failed
