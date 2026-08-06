from config.constants.morphism.provenance.commit.classification.good.value import VALUE as _GOOD
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_FAILURE = (
    rb"(?m)^(?!"
    + _GOOD
    + _FIELD
    + rb")[^\n]"
)


def MAIN() -> int:
    document = _SYS.stdin.buffer.read()
    _SYS.stdout.buffer.write(document)
    return 1 if _REGEX.search(_FAILURE, document) else 0


raise SystemExit(MAIN())
