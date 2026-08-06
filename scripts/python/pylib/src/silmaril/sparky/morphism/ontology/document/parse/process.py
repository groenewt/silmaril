from config.constants.morphism.ontology.document.parse.evidence.prefix.value import VALUE as _PREFIX
from config.constants.morphism.ontology.document.parse.evidence.terminator.value import VALUE as _TERMINATOR
from config.constants.morphism.ontology.document.parse.format.value import VALUE as _FORMAT
from config.gate.external.python.resource_description_framework_library.graph.library import DEPENDENCY as _GRAPH
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _PREFIX
        + str(len(_GRAPH().parse(data=_SYS.stdin.buffer.read(), format=_FORMAT.decode()))).encode()
        + _TERMINATOR
    )
    return 0


raise SystemExit(MAIN())
