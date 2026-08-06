VALUE = (
    "python3",
    "-c",
    r'''import re
import sys

declarations = {
    "silm": "urn:silmaril:entity#",
    "cco": "https://www.commoncoreontologies.org/",
    "cceo": "https://www.commoncoreontologies.org/cpo#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "sh": "http://www.w3.org/ns/shacl#",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "sf": "http://www.opengis.net/ont/sf#",
}
for path in sys.stdin.read().splitlines():
    content = open(path, encoding="utf-8").read()
    if not content.lstrip():
        continue
    for match in re.finditer(r"@prefix\s+(\w+):\s+<([^>]+)>\s+\.", content):
        if match.group(1) not in declarations:
            declarations[match.group(1)] = match.group(2)
for name in sorted(declarations):
    sys.stdout.write("@prefix " + name + ": <" + declarations[name] + "> .\n")
''',
)
