"""Validated style projection; active-red host execution, not Frame admission.

Selectors, declarations and chart queries are ontology-owned. Host iteration
and dependency bindings still require physical carrier and scheduler proofs.
"""
from config.constants.morphism.user.interface.constructor.cascading.style.sheet.render.format.value import VALUE as FORMAT
from config.gate.external.python.resource_description_framework_library.library import DEPENDENCY as DESCRIPTION
from config.gate.external.python.shapes.constraint.language.library import DEPENDENCY as VALIDATION
from config.gate.external.python.standard.library.operating.system.library import DEPENDENCY as ENVIRONMENT
from config.gate.external.python.standard.library.system.library import DEPENDENCY as SYSTEM


def MAIN() -> int:
    graph = DESCRIPTION.Graph()
    graph.parse(ENVIRONMENT.environ["SILMARIL_ONTOLOGY_PATH"], format=FORMAT.decode())
    conforms, evidence, report = VALIDATION.validate(graph, shacl_graph=graph)
    if not conforms:
        SYSTEM.stderr.write(report)
        return 1
    projection = DESCRIPTION.Namespace("urn:silmaril:user:interface:projection:")
    rows = list(graph.query(str(graph.value(projection.Styles, projection.query))))
    if not rows:
        SYSTEM.stderr.write("The projection requires at least one style rule.\n")
        return 1
    output = []
    previous = None
    for row in rows:
        if row.subject != previous:
            if previous is not None:
                output.append("}")
            output.append(str(row.selector) + " {")
            previous = row.subject
        output.append("  " + str(row.name) + ": " + str(row.value) + ";")
    output.append("}")
    SYSTEM.stdout.write("\n".join(output) + "\n")
    return 0


raise SystemExit(MAIN())
