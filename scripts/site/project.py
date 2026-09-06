"""Project the declared public repository into browsing artifacts.

This build host adapter emits observations, not ontology admission verdicts.
Document structure and browser behavior are supplied by Turtle specifications.
"""
import hashlib
import html
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.compare import to_canonical_graph

ROOT = Path(__file__).resolve().parents[2]
PORTAL = Namespace('urn:silmaril:user:interface:portal:')
INTERFACE = Namespace('urn:silmaril:user:interface:')
PROJECTION = Namespace('urn:silmaril:user:interface:projection:')
GEOMETRY = Namespace('http://www.opengis.net/ont/geosparql#')
SPECIFICATION = Graph().parse(ROOT / 'basicttl/user/interface/portal.ttl')
TRACKED = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')


def write(record):
    path, content = record
    destination = (ROOT / path).resolve()
    if not destination.is_relative_to(ROOT / 'docs'):
        raise ValueError('Projection output escapes docs')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding='utf-8')


def digest(content):
    return hashlib.sha256(content).hexdigest()


def json_text(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n'


def render_elements(root):
    query = str(SPECIFICATION.value(PORTAL.Elements, PORTAL.query))
    rows = list(SPECIFICATION.query(query, initBindings={'root': root}))
    children = defaultdict(list)
    for row in rows:
        children[row.parent].append(row)
    seen = set()

    def element(subject):
        if subject in seen:
            raise ValueError('Cyclic or shared presentation element: ' + str(subject))
        seen.add(subject)
        row = next(row for row in rows if row.subject == subject)
        tag = str(row.tag)
        if not re.fullmatch(r'[a-z][a-z0-9]*', tag) or tag in {'script', 'style', 'object'}:
            raise ValueError('Invalid presentation species')
        attributes = {}
        for attribute in SPECIFICATION.objects(subject, INTERFACE.attribute):
            name = str(SPECIFICATION.value(attribute, INTERFACE.name))
            value = str(SPECIFICATION.value(attribute, INTERFACE.value))
            if not re.fullmatch(r'[a-zA-Z][a-zA-Z0-9-]*', name) or name.lower().startswith('on') or name in attributes:
                raise ValueError('Invalid or repeated attribute')
            if name in {'href', 'src'} and not (value.startswith(('/', '#', 'https://', '{{'))):
                raise ValueError('Invalid destination')
            attributes[name] = value
        opening = '<' + tag + ''.join(' ' + name + '="' + ("{{ '" + value.replace("'", '%27') + "' | relative_url }}" if name in {'href', 'src'} and value.startswith('/') else html.escape(value, quote=True)) + '"' for name, value in sorted(attributes.items())) + '>'
        if tag in {'input', 'img', 'br'}:
            return opening
        points = [(child.horizontal, child.vertical) for child in children[subject]]
        if len(set(points)) != len(points):
            raise ValueError('Sibling chart collision')
        return opening + html.escape(str(row.text)) + ''.join(element(child.subject) for child in children[subject]) + '</' + tag + '>'

    result = element(root)
    if len(seen) != len(rows):
        raise ValueError('Presentation contains unreachable elements')
    return result


def project_portal():
    for row in SPECIFICATION.query(str(SPECIFICATION.value(PORTAL.Artifacts, PORTAL.query))):
        content = render_elements(row.root) if row.root else str(row.content)
        write((str(row.path), content + '\n'))
    labels = {str(SPECIFICATION.value(node, PORTAL.key)): str(SPECIFICATION.value(node, PORTAL.text)) for node in SPECIFICATION.subjects(RDF.type, PORTAL.Label)}
    write(('docs/assets/data/portal.json', json_text(labels)))


def project_catalog():
    source_root = str(SPECIFICATION.value(PORTAL.Catalog, PORTAL.sourceRoot))
    extension = str(SPECIFICATION.value(PORTAL.Catalog, PORTAL.extension))
    files = sorted(path for path in TRACKED if path.startswith(source_root + '/') and path.endswith(extension))
    entries = []
    entities = {}
    triple_count = 0
    class_types = {'http://www.w3.org/2002/07/owl#Class', str(RDFS.Class)}
    property_types = {str(RDF.Property), 'http://www.w3.org/2002/07/owl#ObjectProperty', 'http://www.w3.org/2002/07/owl#DatatypeProperty', 'http://www.w3.org/2002/07/owl#AnnotationProperty'}
    context_scope = str(SPECIFICATION.value(PORTAL.FragmentNamespaceContext, PORTAL.sourceRoot) or '')
    prefixes = sorted((str(SPECIFICATION.value(node, PORTAL.prefix)), str(SPECIFICATION.value(node, PORTAL.namespace))) for node in SPECIFICATION.objects(PORTAL.FragmentNamespaceContext, PORTAL.binding))
    prelude = ''.join('@prefix ' + prefix + ': <' + namespace + '> .\n' for prefix, namespace in prefixes).encode()
    for filename in files:
        path = ROOT / filename
        content = path.read_bytes()
        key = digest(filename.encode())[:20]
        graph = Graph()
        error = None
        context = bool(context_scope and filename.startswith(context_scope + '/'))
        try:
            graph.parse(data=(prelude if context else b'') + content, format='turtle', publicID='https://github.com/groenewt/silmaril/blob/master/' + filename)
        except Exception as failure:
            error = str(failure)
            graph = Graph()
        if any(isinstance(term, BNode) for triple in graph for term in triple):
            graph = to_canonical_graph(graph)

        def term(value):
            if isinstance(value, Literal):
                return {'kind': 'literal', 'value': str(value), 'language': value.language, 'datatype': str(value.datatype or '')}
            if isinstance(value, BNode):
                return {'kind': 'blank', 'value': '_:' + key + ':' + str(value)}
            return {'kind': 'iri', 'value': str(value)}

        triples = [[term(value) for value in triple] for triple in sorted(graph, key=lambda triple: tuple(value.n3() for value in triple))]
        triple_count += len(triples)
        for subject in set(graph.subjects()):
            identifier = term(subject)['value']
            types = sorted(str(value) for value in graph.objects(subject, RDF.type))
            label = str(graph.value(subject, RDFS.label) or identifier.rsplit('#', 1)[-1].rsplit('/', 1)[-1].rsplit(':', 1)[-1])
            entry = entities.setdefault(identifier, {'iri': identifier, 'label': label, 'types': [], 'parents': [], 'files': [], 'kind': 'individual'})
            entry['types'] = sorted(set(entry['types'] + types))
            entry['parents'] = sorted(set(entry['parents'] + [str(value) for value in graph.objects(subject, RDFS.subClassOf)]))
            entry['files'].append(key)
            if class_types.intersection(entry['types']):
                entry['kind'] = 'class'
            elif property_types.intersection(entry['types']):
                entry['kind'] = 'property'
        entries.append({'path': filename, 'key': key, 'digest': digest(content), 'triples': len(triples), 'error': error is not None, 'context': context})
        write(('docs/assets/data/ontology/' + key + '.json', json_text({'path': filename, 'digest': digest(content), 'error': error, 'context': prefixes if context else [], 'source': content.decode('utf-8'), 'triples': triples})))
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    write(('docs/assets/data/ontology.json', json_text({'revision': revision, 'files': entries, 'entities': sorted(entities.values(), key=lambda entry: entry['iri']), 'triples': triple_count, 'errors': sum(entry['error'] for entry in entries)})))
    return {'files': len(entries), 'entities': len(entities), 'triples': triple_count, 'parse_errors': sum(entry['error'] for entry in entries)}


if __name__ == '__main__':
    project_portal()
    print(json_text(project_catalog()))
