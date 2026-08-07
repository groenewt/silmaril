# The rebuild plan, authored as ontology

Per the maintainer ruling (Q2, and Message 12: *"this plan will be understood in
shacl and geosparql to ensure we understand these are OUR FRIENDS"*), the
end-to-end v1 rebuild is not a document *about* the work — it **is** the work,
expressed as a typed, inspectable, revisable directed acyclic graph.

| file | role |
|------|------|
| `dag_ontology.ttl` | TBox — the Workflow / Phase / Task / Gate / Artifact / Doctrine / Ruling / Goal / GoverningSkill vocabulary and the `dependsOn` / `hasPhase` / `consumesArtifact` / `producesArtifact` / `provenByGate` / `governedBySkill` / `honorsDoctrine` / `realizesGoal` / `honorsRuling` properties |
| `dag_instances.ttl` | ABox — the concrete graph: base units `S0, G, W1–W5, X`, their 55 phases, the two doctrines, four rulings, four goals, fourteen governing superpowers skills, and the `dependsOn` edges |
| `dag_shapes.ttl` | SHACL — the graph's structural law (every workflow decomposes into phases, produces an artifact, is governed and doctrine-bound; local acyclicity) |
| `dag_queries.sparql` | SPARQL — schedule (ready-set, transitive prerequisites) and coverage (every goal realized, every ruling honored, every workflow doctrine-bound) |

The GeoSPARQL projection of this DAG over the S/O/P-tower coordinate geometry is
**provisional and intentionally deferred**: the tower coordinates do not exist
until `W2` materializes `crs_law.ttl`. Authoring a GeoSPARQL query over geometry
that does not yet exist would be a force-fit — refused per the Praeriehund
doctrine.

## Evidence (verification-before-completion)

```
pip install rdflib pyshacl
python3 - <<'PY'
from rdflib import Graph; from pyshacl import validate
d = Graph(); [d.parse(f"basicttl/dag/{f}") for f in ("dag_ontology.ttl","dag_instances.ttl")]
s = Graph(); s.parse("basicttl/dag/dag_shapes.ttl")
print("conforms:", validate(d, shacl_graph=s, inference="rdfs")[0])
PY
python3 scripts/ontology-depth-check.py basicttl/dag
```

Last run: parse OK · SHACL conforms · goal/ruling/doctrine coverage all zero
unmet · acyclic · depth gate PASSED (3 files).
