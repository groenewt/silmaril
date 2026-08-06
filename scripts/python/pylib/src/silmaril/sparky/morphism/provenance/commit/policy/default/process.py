from config.constants.morphism.provenance.commit.classification.bad.signature.value import VALUE as _BAD_SIGNATURE
from config.constants.morphism.provenance.commit.classification.unknown.value import VALUE as _UNKNOWN
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_FAILURE = (
    rb"(?m)^(?:"
    + _BAD_SIGNATURE
    + rb"|"
    + _UNKNOWN
    + rb")"
    + _FIELD
)


def MAIN() -> int:
    document = _SYS.stdin.buffer.read()
    _SYS.stdout.buffer.write(document)
    return 1 if _REGEX.search(_FAILURE, document) else 0


raise SystemExit(MAIN())
