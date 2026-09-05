"""Counterexamples for the public browsing projection, independent of admission."""
import importlib.util
import json
from pathlib import Path

import pytest
from rdflib import Literal, RDF

SOURCE = Path(__file__).with_name('project.py')
SPEC = importlib.util.spec_from_file_location('site_projection', SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_catalog_preserves_blank_nodes_literals_and_parse_failures(tmp_path, monkeypatch):
    source = tmp_path / 'basicttl'
    source.mkdir()
    (source / 'valid.ttl').write_text('@prefix e: <urn:example:> . @prefix owl: <http://www.w3.org/2002/07/owl#> . e:Class a owl:Class . e:subject e:property [ e:text "bonjour"@fr ] .')
    (source / 'invalid.ttl').write_text('e:unbound e:predicate e:object .')
    monkeypatch.setattr(MODULE, 'ROOT', tmp_path)
    monkeypatch.setattr(MODULE, 'TRACKED', ['basicttl/valid.ttl', 'basicttl/invalid.ttl'])
    monkeypatch.setattr(MODULE.subprocess, 'check_output', lambda *arguments, **keywords: 'fixture-revision')
    receipt = MODULE.project_catalog()
    assert receipt == {'files': 2, 'entities': 3, 'triples': 3, 'parse_errors': 1}
    target = tmp_path / 'docs/assets/data'
    catalog = json.loads((target / 'ontology.json').read_text())
    assert any(entry['kind'] == 'class' for entry in catalog['entities'])
    valid = next(entry for entry in catalog['files'] if not entry['error'])
    artifact = target / 'ontology' / (valid['key'] + '.json')
    first = artifact.read_bytes()
    terms = [term for triple in json.loads(first)['triples'] for term in triple]
    assert any(term['kind'] == 'blank' for term in terms)
    assert any(term.get('language') == 'fr' for term in terms)
    MODULE.project_catalog()
    assert artifact.read_bytes() == first


def test_chart_order_and_species_are_projected():
    output = MODULE.render_elements(MODULE.SPECIFICATION.value(MODULE.PORTAL.HomeInclude, MODULE.PORTAL.root))
    assert output.index('A little world') < output.index('journey-diagram') < output.index('A traveler brings a claim')
    assert 'viewBox="0 0 640 200"' in output
    assert '{{ \'/explore/\' | relative_url }}' in output


def test_cyclic_presentation_is_rejected(monkeypatch):
    graph = MODULE.SPECIFICATION.__class__()
    graph += MODULE.SPECIFICATION
    root = graph.value(MODULE.PORTAL.HomeInclude, MODULE.PORTAL.root)
    graph.add((root, MODULE.INTERFACE.child, root))
    monkeypatch.setattr(MODULE, 'SPECIFICATION', graph)
    with pytest.raises(ValueError):
        MODULE.render_elements(root)


def test_repeated_attribute_is_rejected(monkeypatch):
    graph = MODULE.SPECIFICATION.__class__()
    graph += MODULE.SPECIFICATION
    root = graph.value(MODULE.PORTAL.HomeInclude, MODULE.PORTAL.root)
    for identity in ['one', 'two']:
        attribute = MODULE.PORTAL['counterexample:' + identity]
        graph.add((root, MODULE.INTERFACE.attribute, attribute))
        graph.add((attribute, MODULE.INTERFACE.name, Literal('title')))
        graph.add((attribute, MODULE.INTERFACE.value, Literal(identity)))
    monkeypatch.setattr(MODULE, 'SPECIFICATION', graph)
    with pytest.raises(ValueError, match='attribute'):
        MODULE.render_elements(root)
