from config.constants.morphism.ontology.consolidation.shapes.constraint.language.document.value import VALUE as DOCUMENT
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as SYS


def MAIN() -> int:
    SYS.stdout.buffer.write(SYS.stdin.buffer.read() + DOCUMENT)
    return 0


raise SystemExit(MAIN())
