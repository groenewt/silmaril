from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.accumulate.value import Value as AwaitingAccumulate
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.close.value import Value as AwaitingClose
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.entry.value import Value as AwaitingEntry
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.failure.close.value import Value as AwaitingFailureClose
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.open.value import Value as AwaitingOpen
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.post.value import Value as AwaitingPost
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.pre.value import Value as AwaitingPre
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.read.value import Value as AwaitingRead
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.readback.value import Value as AwaitingReadback
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.revision.value import Value as AwaitingRevision
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.seal.value import Value as AwaitingSeal
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.stability.value import Value as AwaitingStability
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.complete.value import Value as Complete
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.failed.value import Value as Failed

Value = AwaitingEntry | AwaitingOpen | AwaitingPre | AwaitingRead | AwaitingAccumulate | AwaitingPost | AwaitingClose | AwaitingFailureClose | AwaitingStability | AwaitingRevision | AwaitingSeal | AwaitingReadback | Complete | Failed
