from config.constants.morphism.provenance.commit.record.document.separator.value import VALUE as _DOCUMENT
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.gate.external.python.stdlib.pathlib.library import DEPENDENCY as _PATHLIB
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_SIGNATURE_TYPE_LINES = _PATHLIB.Path(_SYS.argv[1]).read_bytes()
_VERIFICATION_LINES = _PATHLIB.Path(_SYS.argv[2]).read_bytes()
_MANIFEST = _PATHLIB.Path(_SYS.argv[3]).read_bytes()
_TAIL = _DOCUMENT + b"\n" + _MANIFEST


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        b"\n".join(
            map(
                _FIELD.join,
                zip(
                    _SIGNATURE_TYPE_LINES.splitlines(),
                    _VERIFICATION_LINES.splitlines(),
                ),
            )
        )
    )
    _SYS.stdout.buffer.write(b"\n")
    _SYS.stdout.buffer.write(_TAIL)
    return 0


raise SystemExit(MAIN())
