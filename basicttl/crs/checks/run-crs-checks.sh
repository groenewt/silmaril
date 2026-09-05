#!/usr/bin/env bash
# =====================================================================================
# run-crs-checks.sh — the S/O/P-tower CRS law verification runner (W2 · SP3, plan Task T1).
# =====================================================================================
# SP3 (the N-dimensional Coordinate Reference System realized as the Subject/Object/Predicate
# URN towers) grounds ONTO the two committed, green floors below it — SP1 (basicttl/primitives)
# and SP2 (basicttl/aob) — and is NOT green unless BOTH of those floors stay green, both on
# their own graphs AND over the single merged graph into which SP3's classes dual-ground
# (SP1 prim:DualGroundingShape / q_universality). This runner therefore proves four things:
#
#   1. The committed SP1 floor still passes on its OWN graph  (basicttl/primitives/checks/run-floor-checks.sh).
#   2. The committed SP2 floor still passes on its OWN graph  (basicttl/aob/checks/run-aob-checks.sh).
#   3. SP1 + SP2 + SP3 parsed into ONE merged graph conforms to:
#        * crs.shapes.ttl        (the SP3 law — skipped while it declares no shape, e.g. at T1),
#        * primitives.shapes.ttl (the SP1 law re-run OVER the merged graph — catches an ungrounded
#          crs class: this is the tooth T11 injects against),
#        * aob.shapes.ttl        (the SP2 law re-run over the merged graph),
#      and every EXPECT-TRUE ASK of all three query suites (crs / SP1 / SP2) holds over the merged graph.
#   4. Every owl:Class under basicttl/crs carries a >= 200-char rdfs:comment (the depth gate).
#
# Exits 0 iff ALL green; non-zero if any SP1/SP2/SP3 data TTL is missing or unparseable (this is the
# T1 probe of record: break the SP1 load path -> the merged parse fails -> RED, proving the runner
# genuinely re-validates the floors), a SHACL violation exists over the merged graph, any EXPECT-TRUE
# ASK returns false, or the depth gate fails.
#
# The SP3 DATA TTLs are AUTO-DISCOVERED: every basicttl/crs/*.ttl EXCEPT the shapes graph
# (crs.shapes.ttl is loaded ONLY as the shapes graph, never mixed into the data graph), so each later
# task's new data file (carriers/towers/geometers/derivation) wires itself in with no edit here.
# The crs ASK suite is auto-discovered the same way SP1/SP2 do it: split crs.queries.sparql on every
# "# EXPECT-TRUE <name>" marker and execute each block.
#
# Design spec: docs/superpowers/specs/2026-08-08-w2-sp3-sop-tower-crs-law-design.md (§3, §4)
# Plan:        docs/superpowers/plans/2026-08-09-w2-sp3-sop-tower-crs-law-plan.md (Task T1)
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# ---- (1) + (2) the committed SP1 + SP2 floors, re-validated on their OWN graphs ---------------
echo "== SP1 primitive floor (standalone, untouched + green) =="
bash basicttl/primitives/checks/run-floor-checks.sh
echo "== SP2 AOB floor (standalone, untouched + green) =="
bash basicttl/aob/checks/run-aob-checks.sh

# ---- (3) the merged SP1 + SP2 + SP3 graph: crs law + SP1 law + SP2 law + every ASK -----------
echo "== merged graph (SP1 + SP2 + SP3): pyshacl + every EXPECT-TRUE ASK =="
python3 - <<'PY'
import glob, os.path, re, sys, time
from rdflib import Graph
from rdflib.namespace import RDF
from rdflib import URIRef
from pyshacl import validate

SH_NODESHAPE = URIRef("http://www.w3.org/ns/shacl#NodeShape")
SH_PROPSHAPE = URIRef("http://www.w3.org/ns/shacl#PropertyShape")

SP1 = [f"basicttl/primitives/{f}" for f in
       ["formal.ttl", "physical.ttl", "realization.ttl", "taiji.ttl"]]
SP2 = [f"basicttl/aob/{f}" for f in
       ["meta.ttl", "upper_anchor.ttl", "octet_descent.ttl", "tensor_block.ttl",
        "value_colimit.ttl", "group_law.ttl", "evidence_glossary.ttl"]]
# SP3 data = every basicttl/crs/*.ttl EXCEPT the shapes graph (shapes never enter the data graph).
SP3 = sorted(f for f in glob.glob("basicttl/crs/*.ttl") if not f.endswith(".shapes.ttl"))

t0 = time.time()
data = Graph()
for f in SP1 + SP2 + SP3:
    if not os.path.exists(f):
        print(f"  LOAD FAIL: {f} missing (SP1/SP2 floor load path is broken)")
        sys.exit(1)
    data.parse(f)
print(f"  [{time.time()-t0:5.1f}s] parse OK: SP1={len(SP1)} + SP2={len(SP2)} + SP3={len(SP3)} data ttl -> {len(data)} triples")

problems = 0

def validate_over_merged(shapes_path, label):
    global problems
    if not os.path.exists(shapes_path):
        print(f"  {label}: shapes file absent (skipped)"); return
    s = Graph(); s.parse(shapes_path)
    has_shapes = (None, RDF.type, SH_NODESHAPE) in s or (None, RDF.type, SH_PROPSHAPE) in s
    if not has_shapes:
        print(f"  {label}: no shapes declared yet (skipped)"); return
    t = time.time()
    ok, _, rep = validate(data, shacl_graph=s, inference="rdfs")
    print(f"  [{time.time()-t:5.1f}s] SHACL conforms ({label} over merged): {ok}")
    if not ok:
        print(rep[:2500]); problems += 1

# --- crs law (SP3) + SP1 law (incl. prim:DualGroundingShape -- the T11 dual-grounding tooth) over merged.
validate_over_merged("basicttl/crs/crs.shapes.ttl", "crs.shapes.ttl")
validate_over_merged("basicttl/primitives/primitives.shapes.ttl", "primitives.shapes.ttl")

# Validate the complete merged graph. A namespace-based transfer cannot prove
# equivalence: blank nodes, new individuals within the same namespace, inferred
# types and changes to related nodes can all change a constraint result.
validate_over_merged("basicttl/aob/aob.shapes.ttl", "aob.shapes.ttl")


def run_asks(query_path, label):
    global problems
    if not os.path.exists(query_path):
        print(f"  {label} ASKs: query file absent (skipped)"); return
    q = open(query_path).read()
    fails = ran = 0; t0 = time.time()
    for b in re.split(r'\n(?=#\s*EXPECT-TRUE\s)', q):
        m = re.search(r'EXPECT-TRUE\s+(\S+)', b)
        if not m:
            continue
        ask = "\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
        if not ask.strip().upper().startswith(("PREFIX", "ASK")):
            continue
        res = bool(data.query(ask)); ran += 1
        print(f"    {'PASS' if res else 'FAIL'}  {label}:{m.group(1)}")
        fails += (0 if res else 1)
    print(f"  [{time.time()-t0:5.1f}s] {label} ASKs: {ran} run, {fails} failed")
    problems += fails

run_asks("basicttl/crs/crs.queries.sparql", "crs")
run_asks("basicttl/primitives/primitives.queries.sparql", "SP1")
run_asks("basicttl/aob/aob.queries.sparql", "SP2")

sys.exit(1 if problems else 0)
PY

# ---- (4) the depth gate over the SP3 files ---------------------------------------------------
echo "== depth gate (every owl:Class under basicttl/crs >= 200-char rdfs:comment) =="
python3 scripts/ontology-depth-check.py basicttl/crs

echo "CRS CHECKS GREEN"
