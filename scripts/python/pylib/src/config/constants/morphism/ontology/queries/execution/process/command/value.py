VALUE = (
    "python3",
    "-c",
    r'''import re
import sys

from rdflib import Graph

data = Graph().parse("ontology/silmaril-consolidated.ttl", format="turtle")
executable_blocks = [
    block
    for block in re.split(r"(?m)^(?=# Q\d+:)", open("ontology/queries.sparql", encoding="utf-8").read())
    if "SELECT" in block
]
if len(executable_blocks) != 5:
    raise SystemExit("query-library-shape-drift")
failures = 0
for block in executable_blocks:
    label = block.splitlines()[0].split(":")[0].split()[1]
    rows = len(list(data.query(block)))
    sys.stdout.write("execution-verdict " + label + " rows=" + str(rows) + "\n")
    if label in ("Q1", "Q5") and rows == 0:
        failures = failures + 1
raise SystemExit(failures)
''',
)
