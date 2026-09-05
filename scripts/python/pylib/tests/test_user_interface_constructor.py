"""Projection regressions; these host tests do not establish Frame admission."""
import os
from pathlib import Path
import subprocess
import sys
from xml.etree import ElementTree

import pytest
from rdflib import BNode, Graph, Literal, Namespace, RDF


REPOSITORY = Path(__file__).resolve().parents[4]
SOURCE = REPOSITORY / "scripts/python/pylib/src"
INTERFACE = Namespace("urn:silmaril:user:interface:")
ARCHITECTURE = Namespace("urn:silmaril:user:interface:architecture:")
PROJECTION = Namespace("urn:silmaril:user:interface:projection:")
LANGUAGE = Namespace("urn:silmaril:user:interface:hypertext:markup:language:")
STYLE = Namespace("urn:silmaril:user:interface:cascading:style:sheet:")
STATUS = Namespace("urn:silmaril:user:interface:build:status:")
GEOMETRY = Namespace("http://www.opengis.net/ont/geosparql#")


@pytest.fixture
def specification():
    graph = Graph()
    for path in sorted((REPOSITORY / "basicttl/user/interface").glob("*.ttl")):
        graph.parse(path)
    return graph


def render(graph, directory, family="hypertext.markup.language"):
    ontology = directory / "specification with spaces.ttl"
    graph.serialize(ontology, format="turtle")
    return subprocess.run(
        [sys.executable, "-m", "silmaril.sparky.morphism.user.interface.constructor." + family + ".render.process"],
        env={**os.environ, "PYTHONPATH": str(SOURCE), "PYTHONUTF8": "1", "SILMARIL_ONTOLOGY_PATH": str(ontology)},
        capture_output=True, text=True, timeout=30,
    )


def test_statuses_are_readable_and_do_not_claim_live_success(specification, tmp_path):
    result = render(specification, tmp_path)
    assert result.returncode == 0, result.stderr
    root = ElementTree.fromstring(result.stdout)
    assert root.tag == "section"
    assert root.attrib["aria-label"] == "Build verification"
    assert [node.text for node in root.findall("./ul/li/span[1]")] == ["Ontology", "Provenance", "Scripts"]
    assert [node.text for node in root.findall("./ul/li/span[2]")] == ["Not checked"] * 3
    assert root.find("a").attrib["href"] == "https://github.com/groenewt/silmaril/actions"
    assert "pass" not in result.stdout.lower()


def test_chart_coordinates_control_reading_order(specification, tmp_path):
    for name, ordinal in [("ontology", 2), ("scripts", 0)]:
        specification.set((ARCHITECTURE[name + ":geometry"], GEOMETRY.asWKT,
                           Literal(f"<{PROJECTION.Flow}> POINT (0 {ordinal})", datatype=GEOMETRY.wktLiteral)))
    result = render(specification, tmp_path)
    assert result.returncode == 0, result.stderr
    root = ElementTree.fromstring(result.stdout)
    assert [node.text for node in root.findall("./ul/li/span[1]")] == ["Scripts", "Provenance", "Ontology"]


def test_literal_text_is_escaped_and_unicode_is_preserved(specification, tmp_path):
    value = 'Schrödinger & <script>alert("meow")</script>'
    specification.set((ARCHITECTURE.heading, INTERFACE.text, Literal(value)))
    result = render(specification, tmp_path)
    assert result.returncode == 0, result.stderr
    root = ElementTree.fromstring(result.stdout)
    assert root.find("h2").text == value
    assert root.find(".//script") is None


@pytest.mark.parametrize("family", ["hypertext.markup.language", "cascading.style.sheet"])
def test_rdf_serialization_order_does_not_change_output(specification, tmp_path, family):
    first = render(specification, tmp_path, family)
    reordered = Graph()
    for triple in reversed(list(specification)):
        reordered.add(triple)
    second = render(reordered, tmp_path, family)
    assert first.returncode == second.returncode == 0, first.stderr + second.stderr
    assert first.stdout == second.stdout


@pytest.mark.parametrize("mutation", ["cycle", "orphan", "collision", "attribute", "state", "override", "geometry", "declaration", "tag", "destination", "missing_state"])
def test_invalid_specification_fails_without_output(specification, tmp_path, mutation):
    if mutation == "cycle":
        specification.add((ARCHITECTURE.checks, INTERFACE.child, ARCHITECTURE.build))
    elif mutation == "orphan":
        specification.remove((ARCHITECTURE.build, INTERFACE.child, ARCHITECTURE.heading))
    elif mutation == "collision":
        specification.set((ARCHITECTURE['scripts:geometry'], GEOMETRY.asWKT,
                           Literal(f"<{PROJECTION.Flow}> POINT (0 0)", datatype=GEOMETRY.wktLiteral)))
    elif mutation == "attribute":
        attribute = BNode()
        specification.add((ARCHITECTURE.runs, INTERFACE.attribute, attribute))
        specification.add((attribute, RDF.type, INTERFACE.Attribute))
        specification.add((attribute, INTERFACE.name, Literal("href")))
        specification.add((attribute, INTERFACE.value, Literal("https://example.com/")))
    elif mutation == "state":
        specification.set((ARCHITECTURE['ontology:state'], STATUS.state, STATUS.Pass))
    elif mutation == "override":
        specification.add((ARCHITECTURE['ontology:state'], INTERFACE.text, Literal("Passed")))
    elif mutation == "geometry":
        specification.set((ARCHITECTURE['heading:geometry'], GEOMETRY.asWKT, Literal("POINT (0 NaN)", datatype=GEOMETRY.wktLiteral)))
    elif mutation == "declaration":
        declaration = BNode()
        specification.add((STYLE['rule:0'], STYLE.declaration, declaration))
        specification.add((declaration, RDF.type, STYLE.Declaration))
        specification.add((declaration, STYLE.name, Literal("--color-accent")))
        specification.add((declaration, STYLE.value, Literal("red")))
    elif mutation == "tag":
        specification.set((LANGUAGE.Heading, PROJECTION.tag, Literal("script")))
    elif mutation == "missing_state":
        specification.remove((ARCHITECTURE['ontology:state'], STATUS.state, None))
        specification.add((ARCHITECTURE['ontology:state'], INTERFACE.text, Literal("Passed")))
    elif mutation == "destination":
        specification.set((ARCHITECTURE['runs:attribute:href'], INTERFACE.value, Literal('javascript:alert(1)')))
    result = render(specification, tmp_path)
    assert result.returncode != 0
    assert result.stdout == ""


def test_style_values_are_projected_from_specification(specification, tmp_path):
    specification.set((STYLE['rule:0:declaration:--color-accent'], STYLE.value, Literal("#123456")))
    result = render(specification, tmp_path, "cascading.style.sheet")
    assert result.returncode == 0, result.stderr
    assert "--color-accent: #123456;" in result.stdout


def test_legacy_turtle_is_parseable():
    assert len(Graph().parse(REPOSITORY / "basicttl/ui_constructor.ttl")) > 0
