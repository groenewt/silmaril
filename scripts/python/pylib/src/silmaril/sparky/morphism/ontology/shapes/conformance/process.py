from config.constants.morphism.ontology.shapes.conformance.format.value import VALUE as _FORMAT
from config.constants.morphism.ontology.shapes.conformance.inference.value import VALUE as _INFERENCE
from config.constants.morphism.ontology.shapes.conformance.shapes.graph.keyword.value import VALUE as _SHAPES_GRAPH_KEYWORD
from config.gate.external.python.resource_description_framework_library.graph.library import DEPENDENCY as _GRAPH
from config.gate.external.python.shapes_constraint_language_library.validate.library import DEPENDENCY as _VALIDATE
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    _FRAME = _VALIDATE(
        _GRAPH().parse(data=_SYS.stdin.buffer.read(), format=_FORMAT.decode()),
        inference=_INFERENCE.decode(),
        **{_SHAPES_GRAPH_KEYWORD.decode(): _GRAPH().parse(_SYS.argv[1], format=_FORMAT.decode())},
    )
    _SYS.stdout.buffer.write(_FRAME[2].encode())
    return int(not _FRAME[0])


raise SystemExit(MAIN())
