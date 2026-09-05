"""Validated tree projection; active-red host execution, not Frame admission.

Species, text, attributes and chart queries are ontology-owned. This engine
serializes query rows only. Physical carrier and scheduler admission remain
unproved, including for this exposed callable and its dependency bindings.
"""
from config.constants.morphism.user.interface.constructor.hypertext.markup.language.render.format.value import VALUE as FORMAT
from config.gate.external.python.resource_description_framework_library.library import DEPENDENCY as DESCRIPTION
from config.gate.external.python.shapes.constraint.language.library import DEPENDENCY as VALIDATION
from config.gate.external.python.standard.library.hypertext.markup.language.library import DEPENDENCY as LANGUAGE
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
    elements = list(graph.query(str(graph.value(projection.Elements, projection.query))))
    attributes = {}
    for row in graph.query(str(graph.value(projection.Attributes, projection.query))):
        attributes.setdefault(row.subject, []).append(
            ' ' + str(row.name) + '="' + LANGUAGE.escape(str(row.value), quote=True) + '"'
        )
    children = {}
    for row in elements:
        children.setdefault(row.parent, []).append(row)
    roots = children.get(None, [])
    if len(roots) != 1:
        SYSTEM.stderr.write("The projection requires exactly one document root.\n")
        return 1
    pending = [(roots[0], False)]
    output = []
    while pending:
        row, closing = pending.pop()
        if closing:
            output.append("</" + str(row.tag) + ">")
        else:
            output.append("<" + str(row.tag) + "".join(attributes.get(row.subject, [])) + ">")
            output.append(LANGUAGE.escape(str(row.text), quote=False))
            pending.append((row, True))
            for child in reversed(children.get(row.subject, [])):
                pending.append((child, False))
    SYSTEM.stdout.write("".join(output) + "\n")
    return 0


raise SystemExit(MAIN())
