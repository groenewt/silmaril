from config.constants.morphism.user.interface.constructor.hypertext.markup.language.render.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS


def MAIN() -> int:
    """
    Unary byte-frame arrow for hypertext markup language rendering.

    Type carriers (primordial ontology):
      - COMMAND : prim:ByteVector  (command tuple as byte-vector)
      - Output  : prim:ByteVector  (generated HTML written to stdout)
      - Effect  : prim:ProcessExitStatus ⊆ prim:Integer (ℤ, two's-complement INT64)

    The return carrier prim:Integer encodes the subprocess exit status.
    Per the universal unary byte-frame law, this callable consumes
    exactly one typed input and produces exactly one output coordinate
    and one effect coordinate.
    """
    return SUBPROCESS.run(COMMAND).returncode


raise SystemExit(MAIN())
