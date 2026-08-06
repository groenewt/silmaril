from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.constants.morphism.provenance.commit.signature.type.absent.value import VALUE as _ABSENT
from config.constants.morphism.provenance.commit.signature.type.other.value import VALUE as _OTHER
from config.constants.morphism.provenance.commit.signature.type.pretty.good.privacy.value import VALUE as _PRETTY_GOOD_PRIVACY
from config.constants.morphism.provenance.commit.signature.type.secure.shell.value import VALUE as _SECURE_SHELL
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_PRETTY_GOOD_PRIVACY_HEADER = rb"(?m)^commit ([0-9a-f]{40})\n(?:[^\n]+\n)*?gpgsig(?:-sha256)? -----BEGIN PGP SIGNATURE-----\n(?:[^\n]+\n)*\n"
_SECURE_SHELL_HEADER = rb"(?m)^commit ([0-9a-f]{40})\n(?:[^\n]+\n)*?gpgsig(?:-sha256)? -----BEGIN SSH SIGNATURE-----\n(?:[^\n]+\n)*\n"
_OTHER_HEADER = rb"(?m)^commit ([0-9a-f]{40})\n(?:[^\n]+\n)*?gpgsig(?:-sha256)? [^\n]*\n(?:[^\n]+\n)*\n"
_ABSENT_HEADER = rb"(?m)^commit ([0-9a-f]{40})\n(?:[^\n]+\n)*\n"
_PRETTY_GOOD_PRIVACY_LINE = b"\\1" + _FIELD + _PRETTY_GOOD_PRIVACY + b"\n"
_SECURE_SHELL_LINE = b"\\1" + _FIELD + _SECURE_SHELL + b"\n"
_OTHER_LINE = b"\\1" + _FIELD + _OTHER + b"\n"
_ABSENT_LINE = b"\\1" + _FIELD + _ABSENT + b"\n"
_RESIDUE = (
    rb"(?m)^(?![0-9a-f]{40}"
    + _FIELD
    + rb"(?:"
    + _PRETTY_GOOD_PRIVACY
    + rb"|"
    + _SECURE_SHELL
    + rb"|"
    + _OTHER
    + rb"|"
    + _ABSENT
    + rb")\n)[^\n]*\n?"
)


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(
            _RESIDUE,
            b"",
            _REGEX.sub(
                _ABSENT_HEADER,
                _ABSENT_LINE,
                _REGEX.sub(
                    _OTHER_HEADER,
                    _OTHER_LINE,
                    _REGEX.sub(
                        _SECURE_SHELL_HEADER,
                        _SECURE_SHELL_LINE,
                        _REGEX.sub(
                            _PRETTY_GOOD_PRIVACY_HEADER,
                            _PRETTY_GOOD_PRIVACY_LINE,
                            _SYS.stdin.buffer.read(),
                        ),
                    ),
                ),
            ),
        )
    )
    return 0


raise SystemExit(MAIN())
