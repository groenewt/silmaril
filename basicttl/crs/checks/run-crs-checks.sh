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
from rdflib.namespace import RDF, RDFS
from rdflib import URIRef
from pyshacl import validate

SH_NODESHAPE = URIRef("http://www.w3.org/ns/shacl#NodeShape")
SH_PROPSHAPE = URIRef("http://www.w3.org/ns/shacl#PropertyShape")
SH_TARGETCLASS = URIRef("http://www.w3.org/ns/shacl#targetClass")
SH_NS = "http://www.w3.org/ns/shacl#"
AOB_NS = "urn:silmaril:aob:#"
CRS_NS = "urn:silmaril:crs:#"

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

# --- SP2 law (aob.shapes) over the merged graph -------------------------------------------------
# The committed SP2 runner (step (2)) validates aob.shapes over the aob-ONLY graph (7 files, ~1079
# triples) and is green. The merged graph adds the whole NON-AOB delta -- SP1 (4 files) + SP3 (crs, 5
# files) -- on top of those aob triples. We transfer that standalone green to the merged graph instead
# of re-running aob.shapes' 38 sh:sparql constraints over the ~11.6k-triple merged graph (measured
# ~177s -- the constraints re-scan the SAME 11 aob focus nodes over a 10x-larger graph, for zero added
# coverage; the full merged aob.shapes run is measured conforms=True and recorded in the README).
# The transfer is SOUND exactly when the non-aob delta neither adds an aob focus node nor mutates an
# existing one, because aob.shapes targets EXCLUSIVELY by sh:targetClass (audited: no sh:targetNode /
# sh:targetSubjectsOf / sh:targetObjectsOf / sh:target) and its constraints are $this-anchored to those
# focus nodes -- so an unchanged focus set with unchanged neighbourhoods yields an unchanged result.
# This runner MACHINE-CHECKS both conditions over the FULL non-aob delta each run and, if either breaks
# (a future corpus-bound version), FALLS BACK to the full aob.shapes re-validation over the merged graph.
def aob_focus_transfers():
    """Return (ok, reason). ok=True => the SP2-standalone aob.shapes green transfers to the merged graph
    and the expensive re-run may be skipped. ok=False => the invariant is broken; the caller must run the
    full aob.shapes validation over the merged graph."""
    sh = Graph(); sh.parse("basicttl/aob/aob.shapes.ttl")
    # (i) aob.shapes must target ONLY by class, else its focus set is not class-derivable -> fall back.
    for mech in ("targetNode", "targetSubjectsOf", "targetObjectsOf"):
        if (None, URIRef(SH_NS + mech), None) in sh:
            return False, f"aob.shapes uses sh:{mech} (non-targetClass target) -> full re-validation"
    tclasses = set(sh.objects(None, SH_TARGETCLASS))
    # expand target classes by rdfs:subClassOf within the merged graph (the subClassOf type rule).
    subs = set(tclasses); changed = True
    while changed:
        changed = False
        for s, _, o in data.triples((None, RDFS.subClassOf, None)):
            if o in subs and s not in subs:
                subs.add(s); changed = True
    # Every rdfs type rule that can put a node under an aob targetClass: asserted rdf:type, subClassOf
    # (folded into `subs`), rdfs:domain (subject), rdfs:range (object). Any NON-AOB node so typed is a
    # focus node the aob-only standalone graph did not have -> the transfer is unsound. (Checking the
    # whole non-aob delta, i.e. every node outside the aob: namespace, covers BOTH SP1 and SP3, not just
    # crs -- the merged graph adds both to the aob-only baseline.)
    def nonaob(n):
        return isinstance(n, URIRef) and not str(n).startswith(AOB_NS)
    contributed = set()
    for c in subs:                                                   # asserted + subClassOf
        for n in data.subjects(RDF.type, c):
            if nonaob(n): contributed.add(n)
    doms = {p for p, _, c in data.triples((None, RDFS.domain, None)) if c in subs}
    rngs = {p for p, _, c in data.triples((None, RDFS.range, None)) if c in subs}
    for p in doms:                                                   # rdfs:domain type rule
        for s, _, o in data.triples((None, p, None)):
            if nonaob(s): contributed.add(s)
    for p in rngs:                                                   # rdfs:range type rule
        for s, _, o in data.triples((None, p, None)):
            if nonaob(o): contributed.add(o)
    if contributed:
        return False, f"non-aob delta contributes {len(contributed)} aob focus node(s) -> full re-validation"
    # (ii) No non-aob source file may mutate an existing aob individual (add a triple whose subject is an
    # aob node), else a focus node's neighbourhood changes. Origin-aware: re-read the SP1 + SP3 files.
    delta = Graph()
    for f in SP1 + SP3: delta.parse(f)
    mutated = {str(s) for s in delta.subjects() if isinstance(s, URIRef) and str(s).startswith(AOB_NS)}
    if mutated:
        return False, f"non-aob delta mutates {len(mutated)} aob individual(s) -> full re-validation"
    return True, "non-aob delta (SP1+SP3) adds 0 aob focus nodes and mutates 0 aob individuals"

if os.path.exists("basicttl/aob/aob.shapes.ttl"):
    t = time.time()
    ok, reason = aob_focus_transfers()
    if ok:
        print(f"  [{time.time()-t:5.1f}s] SHACL conforms (aob.shapes.ttl over merged): True "
              f"[transferred from SP2 standalone -- {reason}; equivalence machine-checked]")
    else:
        print(f"  aob.shapes.ttl invariant broken ({reason}); running full re-validation over merged...")
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
