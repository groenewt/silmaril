# The rebuild plan, authored as ontology

Per the maintainer ruling (Q2, and Message 12: *"this plan will be understood in
shacl and geosparql to ensure we understand these are OUR FRIENDS"*), the
end-to-end v1 rebuild is not a document *about* the work — it **is** the work,
expressed as a typed, inspectable, revisable directed acyclic graph.

| file | role |
|------|------|
| `dag_ontology.ttl` | TBox — the Workflow / Phase / Task / Gate / Artifact / Doctrine / Ruling / Goal / GoverningSkill vocabulary and the `dependsOn` / `hasPhase` / `consumesArtifact` / `producesArtifact` / `provenByGate` / `governedBySkill` / `honorsDoctrine` / `realizesGoal` / `honorsRuling` / `hasStatus` properties |
| `dag_instances.ttl` | ABox — the concrete graph: base units `S0, G, W1–W5, X`, their 53 phases, the two doctrines, nine rulings, four goals, fourteen governing superpowers skills, the `dependsOn` edges, and a live `hasStatus` per workflow/phase (`completed` / `in-progress` / `pending`) so the DAG records where the build actually stands, not just its intent. **W2 is decomposed into its nine approved sub-projects** (SP1 Primitive Floor → … → SP9 render seal); the brainstorming rulings (`corpus_agnostic_iteration`, `dual_grounding_floor`, `colimit_taiji_monadic`, `aob_sauce_glossary_polysemy`, `unary_grammar_jepa_twin`) bind W2. |
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

Last run: parse OK (630 triples) · SHACL conforms · goal/ruling/doctrine coverage
all zero unmet (all nine rulings honored) · acyclic · depth gate PASSED (3 files) ·
status snapshot S0/G/W1 completed, W2 in-progress, W3/W4/W5/X pending.
