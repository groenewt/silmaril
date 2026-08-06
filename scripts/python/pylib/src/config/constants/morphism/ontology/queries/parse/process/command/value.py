VALUE = (
    "python3",
    "-c",
    r'''import re
import sys

from rdflib.plugins.sparql import prepareQuery

executable_blocks = [
    block
    for block in re.split(r"(?m)^(?=# G?Q\d+:)", open("ontology/queries.sparql", encoding="utf-8").read())
    if "SELECT" in block
]
geographic_blocks = [
    block
    for block in re.split(r"(?m)^(?=# G?Q\d+:)", open("ontology/geosparql.sparql", encoding="utf-8").read())
    if "SELECT" in block
]
if len(executable_blocks) != 5 or len(geographic_blocks) != 2:
    raise SystemExit("query-library-shape-drift")
for block in executable_blocks + geographic_blocks:
    prepareQuery(block)
    sys.stdout.write("parse-verdict " + block.splitlines()[0].split(":")[0].split()[1] + " ok\n")
''',
)
