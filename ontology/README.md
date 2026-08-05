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
python3 scripts/consolidate-ontology.py --output-dir ontology/
```

Do not edit files in this directory directly. Edit the source files in `basicttl/` and regenerate.

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
conforms, _, text = validate(data, shacl_graph=shapes, inference='rdfs')
print(text)
"
```
