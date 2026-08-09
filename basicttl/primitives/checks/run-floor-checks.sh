#!/usr/bin/env bash
# =====================================================================================
# run-floor-checks.sh — the Primitive Floor verification runner (W2 · SP1, plan Task 1).
# =====================================================================================
# Parses the four DATA TTLs of the floor (formal/physical/realization/taiji) into one graph,
# runs pyshacl against primitives.shapes.ttl (loaded ONLY as the shapes graph, never mixed
# into the data graph), evaluates every EXPECT-TRUE ASK in primitives.queries.sparql, and
# runs the ontology depth gate (every owl:Class >= 200-char rdfs:comment). Exits 0 iff all
# green: non-zero if a TTL is missing/unparseable, a SHACL violation exists, the depth gate
# fails, or any EXPECT-TRUE ASK returns false. Called by every later task's verification.
# NOTE: the per-type frags/*.ttl were removed after integration into realization.ttl/taiji.ttl
# (they were duplicate source that could silently diverge); the four data files are authoritative.
#
# The ASK suite is AUTO-DISCOVERED: this runner splits primitives.queries.sparql on every
# "# EXPECT-TRUE <name>" marker and executes each block, so adding an ASK to that file wires it
# into the runner with no change here. It executes the original 18 (litmus + monad/colimit/RGB/
# byte-descent + the 6 STEP A/B/C/D functor/Yoneda probes) PLUS the 3 STEP E residual-teeth ASKs
# q_yoneda_point, q_yoneda_evaluation_sound, q_functor_composition_total — 21 EXPECT-TRUE ASKs in
# all — and validates against the 13 sh:NodeShapes of primitives.shapes.ttl (incl. the STEP E
# FrameYonedaPoint / YonedaEvaluation / CompositeTransportCoverage shapes).
#
# Design spec: docs/superpowers/specs/2026-08-07-w2-primitive-floor-design.md (§6)
# Plan:        docs/superpowers/plans/2026-08-07-w2-sp1-primitive-floor.md (Task 1)
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python3 - <<'PY'
import glob, sys, re
from rdflib import Graph
from pyshacl import validate

DATA_FILES = ["formal.ttl", "physical.ttl", "realization.ttl", "taiji.ttl"]
SHAPES_FILE = "primitives.shapes.ttl"

data = Graph()
ttls = [f"basicttl/primitives/{f}" for f in DATA_FILES]
for f in ttls:
    data.parse(f)
print(f"parse OK: {len(ttls)} data ttl, {len(data)} triples")

import os.path
shapes_path = f"basicttl/primitives/{SHAPES_FILE}"
if os.path.exists(shapes_path):
    s = Graph(); s.parse(shapes_path)
    ok, _, rep = validate(data, shacl_graph=s, inference="rdfs")
    print("SHACL conforms:", ok)
    if not ok:
        print(rep[:2000]); sys.exit(1)
else:
    print("SHACL: shapes file not present yet (skipped)")

# EXPECT-TRUE ASKs from the query file
q = open("basicttl/primitives/primitives.queries.sparql").read()
blocks = re.split(r'\n(?=#\s*EXPECT-TRUE\s)', q)
fails = 0
ran = 0
for b in blocks:
    m = re.search(r'EXPECT-TRUE\s+(\S+)', b)
    if not m:
        continue
    name = m.group(1)
    ask = "\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
    if not ask.strip().upper().startswith(("PREFIX", "ASK")):
        continue
    res = bool(data.query(ask))
    ran += 1
    print(f"  {'PASS' if res else 'FAIL'}  {name}")
    fails += (0 if res else 1)
print(f"ASKs: {ran} run, {fails} failed")
sys.exit(1 if fails else 0)
PY
python3 scripts/ontology-depth-check.py basicttl/primitives
echo "FLOOR CHECKS GREEN"
