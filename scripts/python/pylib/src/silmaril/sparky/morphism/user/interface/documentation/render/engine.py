"""Source-document projection for Jekyll; active-red host adapter, not Frame admission."""
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import subprocess

from config.gate.external.python.resource_description_framework_library.library import DEPENDENCY as DESCRIPTION


def MAIN() -> int:
    root = Path(os.environ['SILMARIL_REPOSITORY_ROOT']).resolve()
    graph = DESCRIPTION.Graph().parse(root / 'basicttl/user/interface/documentation.ttl')
    document = DESCRIPTION.Namespace('urn:silmaril:user:interface:documentation:')
    extension = str(graph.value(document.RepositoryCatalog, document.extension) or '.md')
    registered = {str(path) for path in graph.objects(None, document.path)}
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    for filename in sorted(path for path in tracked if path.endswith(extension) and path not in registered):
        subject = document['source:' + hashlib.sha256(filename.encode()).hexdigest()]
        identity = re.sub(r'[^a-zA-Z0-9-]', '-', filename[:-len(extension)])
        content = (root / filename).read_text(encoding='utf-8')
        title = re.search(r'^#\s+(.+)$', content, flags=re.M)
        for predicate, value in [(DESCRIPTION.RDF.type, document.Source), (document.path, DESCRIPTION.Literal(filename)), (document.identity, DESCRIPTION.Literal(identity)), (document.title, DESCRIPTION.Literal(title.group(1) if title else filename))]:
            graph.add((subject, predicate, value))
    output = []
    for row in graph.query(str(graph.value(document.Registry, document.query))):
        path = (root / str(row.path)).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError('Document source is missing or escapes the repository: ' + str(row.path))
        content = path.read_text(encoding='utf-8')
        content = re.sub(r'\A---\n.*?\n---\n', '', content, count=1, flags=re.S)
        graph.add((row.subject, document.content, DESCRIPTION.Literal(content)))
        graph.add((row.subject, document.digest, DESCRIPTION.Literal(hashlib.sha256(path.read_bytes()).hexdigest())))
    for row in graph.query(str(graph.value(document.Content, document.query))):
        output.append({'identity': str(row.identity), 'source': str(row.path), 'title': str(row.title), 'content': str(row.content), 'digest': str(row.digest)})
    target = root / 'docs/_data/documentation.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    index = root / 'docs/assets/data/documents.json'
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text(json.dumps([{key: item[key] for key in ['identity', 'source', 'title', 'digest']} for item in output], ensure_ascii=False))
    for item in output:
        target = root / 'docs/documents' / (item['identity'] + '.md')
        target.parent.mkdir(parents=True, exist_ok=True)
        metadata = {'layout': 'document-frame', 'title': item['title'], 'permalink': '/documents/' + item['identity'] + '/', 'document_source': item['source'], 'document_digest': item['digest']}
        target.write_text('---\n' + '\n'.join(key + ': ' + json.dumps(value, ensure_ascii=False) for key, value in metadata.items()) + '\n---\n{% raw %}\n' + item['content'] + '\n{% endraw %}\n')
    for row in graph.query(str(graph.value(document.Templates, document.query))):
        target = (root / str(row.path)).resolve()
        if not target.is_relative_to(root / 'docs'):
            raise ValueError('Template target escapes docs')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(str(row.content))
    return 0


raise SystemExit(MAIN())
