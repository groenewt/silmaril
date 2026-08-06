# Silmaril Ontology

This directory contains the consolidated Silmaril encyclopedia ontology, generated from the distributed TTL files in `basicttl/`.

## Files

| File | Description |
|------|-------------|
| `silmaril-consolidated.ttl` | Merged ontology (30K+ source files) |
| `shapes.ttl` | SHACL validation shapes |
| `queries.sparql` | SPARQL query library |
| `geosparql.sparql` | GeoSPARQL spatial queries |
| `manifest.ttl` | Ontology metadata manifest |

## Regeneration

```bash
export SILMARIL_PYTHON=$(command -v python3)
make -C scripts/python/pylib morphism-ontology-consolidation
cp scripts/python/pylib/build/morphism/ontology/consolidation/{silmaril-consolidated.ttl,shapes.ttl,queries.sparql,geosparql.sparql,manifest.ttl} ontology/
```

Do not edit files in this directory directly. Edit the source files in `basicttl/` and regenerate.

`shapes.ttl` is also generated — shape changes go in the typed consolidation
constants (`scripts/python/pylib/src/config/constants/morphism/ontology/consolidation/`),
never in the output file. CI fails if this directory drifts from a fresh
regeneration.

Known source quirk: many `basicttl/` node IDs carry raw `#`, `>`, `=` and
similar characters that are illegal in Turtle local names; the consolidator
percent-encodes them (`%23` style) during the merge so the consolidated
document parses. A source-level cleanup sweep is a possible follow-up.

## Query Examples

```sparql
# List all papers with concrete anchors
SELECT ?paper ?label WHERE {
    ?paper a owl:NamedIndividual .
    ?paper rdfs:label ?label .
    FILTER (strstarts(str(?paper), str(silm:instances_papers_)))
}
```

## Validation

```bash
# Install pyshacl
pip install pyshacl rdflib

# Validate
python3 -c "
from pyshacl import validate
from rdflib import Graph
data = Graph().parse('ontology/silmaril-consolidated.ttl', format='turtle')
shapes = Graph().parse('ontology/shapes.ttl', format='turtle')
conforms, _, text = validate(data, shacl_graph=shapes, inference='none')
print(text)
"
```

(`inference='none'`: every shape targets asserted types, and RDFS closure is
prohibitively slow at this graph size.)
