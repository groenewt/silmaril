"""Source-document projection for Jekyll; active-red host adapter, not Frame admission."""
import hashlib
import json
import os
from pathlib import Path
import re
import sys

from config.gate.external.python.resource_description_framework_library.library import DEPENDENCY as DESCRIPTION


def MAIN() -> int:
    root = Path(os.environ['SILMARIL_REPOSITORY_ROOT']).resolve()
    graph = DESCRIPTION.Graph().parse(root / 'basicttl/user/interface/documentation.ttl')
    document = DESCRIPTION.Namespace('urn:silmaril:user:interface:documentation:')
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
    for row in graph.query(str(graph.value(document.Templates, document.query))):
        target = (root / str(row.path)).resolve()
        if not target.is_relative_to(root / 'docs'):
            raise ValueError('Template target escapes docs')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(str(row.content))
    return 0


raise SystemExit(MAIN())
