#!/usr/bin/env bash
# =====================================================================================
# run-foundation-checks.sh — the four-pillar Foundation floor verification runner (W2 · SP0, T1).
# =====================================================================================
# SP0 (basicttl/foundation) is the BEDROCK — the deepest floor, the four-pillar taiji (set theory /
# algebra tower / space constructs / functionality-typing) onto which SP1 (basicttl/primitives),
# SP2 (basicttl/aob) and SP3 (basicttl/crs) re-anchor ADDITIVELY (design §7). Being the bedrock, SP0
# is NOT green unless ALL THREE committed floors above it stay green — both on their own graphs AND
# over the single merged graph into which SP0's classes are ground. This runner proves five things:
#
#   1. The committed SP3 floor still passes  (basicttl/crs/checks/run-crs-checks.sh), which ITSELF
#      transitively re-runs the committed SP1 floor (run-floor-checks.sh) and SP2 floor
#      (run-aob-checks.sh) standalone AND the merged SP1 + SP2 + SP3 graph (crs.shapes + the SP1
#      dual-grounding tooth + SP2 aob.shapes + all 10 crs / 21 SP1 / 13 SP2 ASKs + crs depth). This
#      single call IS the SP1 + SP2 + SP3 invariant (the plan's "re-run SP1/SP2/SP3 invariants").
#   2. SP0 + SP1 + SP2 + SP3 parsed into ONE merged graph conforms to foundation.shapes.ttl
#      (the SP0 law — skipped while it declares no shape, e.g. at T1).
#   3. The prior-floor laws STILL conform once SP0 is mixed in: primitives.shapes.ttl and
#      crs.shapes.ttl re-run OVER the SP0-augmented merged graph (catches an SP0 atom that would
#      regress a prior tooth — e.g. an ungrounded re-anchor edge), and aob.shapes.ttl fully
#      re-validated over that same merged graph.
#   4. Every EXPECT-TRUE ASK of all four suites (foundation / SP1 / SP2 / SP3) holds over the
#      SP0-augmented merged graph.
#   5. Every owl:Class under basicttl/foundation carries a >= 200-char rdfs:comment (the depth gate).
#
# Exits 0 iff ALL green; non-zero if any prior floor regresses, any SP0/SP1/SP2/SP3 data TTL is
# missing or unparseable (THIS is the T1 probe of record: break the SP3 — or any prior — load path
# -> a prior runner fails AND the SP0 merged parse fails -> RED, proving the runner genuinely
# re-validates every floor beneath it), a SHACL violation exists over the merged graph, any
# EXPECT-TRUE ASK returns false, or the depth gate fails.
#
# The SP0 DATA TTLs are AUTO-DISCOVERED: every basicttl/foundation/*.ttl EXCEPT the shapes graph
# (foundation.shapes.ttl is loaded ONLY as the shapes graph, never mixed into the data graph), so
# each later task's new data file (engine / set_theory / algebra_spine / algebra_rings / spaces /
# functionality / combinators / logic / reanchor) wires itself in with no edit here. The foundation
# ASK suite is auto-discovered the same way SP1/SP2/SP3 do it: split foundation.queries.sparql on
# every "# EXPECT-TRUE <name>" marker and execute each block.
#
# Design spec: docs/superpowers/specs/2026-08-31-w2-sp0-foundation-design.md (§6)
# Plan:        docs/superpowers/plans/2026-08-31-w2-sp0-foundation-plan.md (Task T1)
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# ---- (1) the three committed prior floors, re-validated -------------------------------------------
# run-crs-checks.sh IS the SP3 invariant: it re-runs SP1 (run-floor-checks) + SP2 (run-aob-checks)
# standalone AND the merged SP1+SP2+SP3 graph (all prior shapes + all prior ASKs + crs depth gate).
# If the SP3 (or SP1/SP2) load path is broken, this call fails -> the foundation floor is RED.
echo "== SP1 + SP2 + SP3 prior floors (untouched + green; run-crs-checks re-runs all three) =="
bash basicttl/crs/checks/run-crs-checks.sh

# ---- (2)+(3)+(4) the merged SP0 + SP1 + SP2 + SP3 graph: foundation law + prior laws + every ASK --
echo "== merged graph (SP0 + SP1 + SP2 + SP3): pyshacl + every EXPECT-TRUE ASK =="
python3 - <<'PY'
import glob, os.path, re, sys, time
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
from pyshacl import validate

SH_NODESHAPE   = URIRef("http://www.w3.org/ns/shacl#NodeShape")
SH_PROPSHAPE   = URIRef("http://www.w3.org/ns/shacl#PropertyShape")

SP1 = [f"basicttl/primitives/{f}" for f in
       ["formal.ttl", "physical.ttl", "realization.ttl", "taiji.ttl"]]
SP2 = [f"basicttl/aob/{f}" for f in
       ["meta.ttl", "upper_anchor.ttl", "octet_descent.ttl", "tensor_block.ttl",
        "value_colimit.ttl", "group_law.ttl", "evidence_glossary.ttl"]]
# SP3 data = every basicttl/crs/*.ttl EXCEPT its shapes graph.
SP3 = sorted(f for f in glob.glob("basicttl/crs/*.ttl") if not f.endswith(".shapes.ttl"))
# SP0 data = every basicttl/foundation/*.ttl EXCEPT its shapes graph (shapes never enter data).
SP0 = sorted(f for f in glob.glob("basicttl/foundation/*.ttl") if not f.endswith(".shapes.ttl"))

t0 = time.time()
data = Graph()
for f in SP0 + SP1 + SP2 + SP3:
    if not os.path.exists(f):
        print(f"  LOAD FAIL: {f} missing (a floor load path is broken)")
        sys.exit(1)
    data.parse(f)
print(f"  [{time.time()-t0:5.1f}s] parse OK: SP0={len(SP0)} + SP1={len(SP1)} + SP2={len(SP2)} + "
      f"SP3={len(SP3)} data ttl -> {len(data)} triples")

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

# --- (2) the SP0 law over the merged graph ------------------------------------------------------
validate_over_merged("basicttl/foundation/foundation.shapes.ttl", "foundation.shapes.ttl")
# --- (3) the prior-floor laws re-run over the SP0-augmented merged graph -------------------------
# primitives.shapes carries prim:DualGroundingShape (an ungrounded class in the merge -> RED) and
# crs.shapes carries the SP3 law; re-running both over the SP0-inclusive merge is what keeps
# "SP1/SP2/SP3 green over the merged graph" true once SP0 atoms (and, at T10, the re-anchor edges)
# join the graph.
validate_over_merged("basicttl/primitives/primitives.shapes.ttl", "primitives.shapes.ttl")
validate_over_merged("basicttl/crs/crs.shapes.ttl", "crs.shapes.ttl")

# Validate the complete merged graph. A namespace-based transfer cannot prove
# equivalence: blank nodes, new individuals within the same namespace, inferred
# types and changes to related nodes can all change a constraint result.
validate_over_merged("basicttl/aob/aob.shapes.ttl", "aob.shapes.ttl")

# --- (4) every EXPECT-TRUE ASK of all four suites over the SP0-augmented merged graph ------------
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

run_asks("basicttl/foundation/foundation.queries.sparql", "foundation")
run_asks("basicttl/primitives/primitives.queries.sparql", "SP1")
run_asks("basicttl/aob/aob.queries.sparql", "SP2")
run_asks("basicttl/crs/crs.queries.sparql", "SP3")

sys.exit(1 if problems else 0)
PY

# ---- (5) the depth gate over the SP0 files --------------------------------------------------------
echo "== depth gate (every owl:Class under basicttl/foundation >= 200-char rdfs:comment) =="
python3 scripts/ontology-depth-check.py basicttl/foundation

# ---- (5b) the register self-check: shapes-on-disk == tooth-register rows == DAG figure == README ----
# Catches the class of stale-register / stale-DAG / stale-README drift that W3a/W3b/Fix-B closed: the
# sh:NodeShape count in foundation.shapes.ttl MUST equal the number of rows in that file's tooth-register
# header, the sh:NodeShape figure the phase_w2_sp0 node cites in basicttl/dag/dag_instances.ttl, AND every
# sh:NodeShape figure the README narrates. Symmetrically the runnable-ASK count in foundation.queries.sparql
# (blocks that actually parse+execute, i.e. the runner's own "foundation ASKs: N run") MUST equal every
# EXPECT-TRUE ASK figure the README narrates. Any future tooth or ASK added (or removed) without refreshing
# the register, the DAG, OR the README prose -> RED here. This is the Fix-B extension: README's own
# NodeShape+ASK figures were previously OUTSIDE all gate coverage (only the probe count was README-gated),
# so a 36->37 / 33->34 move refreshed the gated figures but left README's prose stale; both figure classes
# are now gated against disk exactly the way the probe count already is. Every gate is NON-VACUOUS: if the
# expected README figure pattern matches zero times, that is itself RED (a silently-dropped figure).
echo "== register self-check (sh:NodeShape AND EXPECT-TRUE ASK: disk == register rows == DAG == README) =="
python3 - <<'PY'
import re, sys
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS
SH_NODESHAPE = URIRef("http://www.w3.org/ns/shacl#NodeShape")
sh = "basicttl/foundation/foundation.shapes.ttl"
g = Graph(); g.parse(sh)
disk = len(set(g.subjects(RDF.type, SH_NODESHAPE)))
reg = len(re.findall(r'^#\s+T\d+\s+fnd:[A-Za-z]+Shape', open(sh).read(), re.M))
dg = Graph(); dg.parse("basicttl/dag/dag_instances.ttl")
sp0 = URIRef("urn:silmaril:entity#phase_w2_sp0")
com = str(next(dg.objects(sp0, RDFS.comment)))
dagfigs = set(int(m) for m in re.findall(r'(\d+)\s+sh:NodeShape', com))

# runnable foundation ASK count == the runner's own "foundation ASKs: N run" (parse+execute-eligible blocks)
q = open("basicttl/foundation/foundation.queries.sparql").read()
ask_disk = 0
for b in re.split(r'\n(?=#\s*EXPECT-TRUE\s)', q):
    if not re.search(r'EXPECT-TRUE\s+\S+', b):
        continue
    body = "\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
    if body.strip().upper().startswith(("PREFIX", "ASK")):
        ask_disk += 1

# README-narrated figures (Fix-B: gate them against disk the way the probe count is)
rd = open("basicttl/foundation/README.md", encoding='utf-8').read()
rd_shape = set(int(m) for m in re.findall(r'(\d+)\*{0,2}\s+(?:SHACL\s+)?`?sh:NodeShape', rd))
rd_ask   = set(int(m) for m in re.findall(r'(\d+)\*{0,2}\s+EXPECT-TRUE\s+ASK', rd))

print(f"  foundation.shapes sh:NodeShape on disk: {disk}")
print(f"  tooth-register header rows:             {reg}")
print(f"  phase_w2_sp0 DAG sh:NodeShape figure:   {sorted(dagfigs)}")
print(f"  README sh:NodeShape figures:            {sorted(rd_shape)}")
print(f"  runnable foundation ASKs on disk:       {ask_disk}")
print(f"  README EXPECT-TRUE ASK figures:         {sorted(rd_ask)}")
if disk != reg:
    print(f"  MISMATCH: register rows ({reg}) != disk shapes ({disk})"); sys.exit(1)
if dagfigs != {disk}:
    print(f"  MISMATCH: DAG figure {sorted(dagfigs)} != disk shapes ({disk})"); sys.exit(1)
if not rd_shape:
    print(f"  MISMATCH: no README sh:NodeShape figure found (gate would be vacuous)"); sys.exit(1)
if rd_shape != {disk}:
    print(f"  MISMATCH: README sh:NodeShape figures {sorted(rd_shape)} != disk shapes ({disk})"); sys.exit(1)
if not rd_ask:
    print(f"  MISMATCH: no README EXPECT-TRUE ASK figure found (gate would be vacuous)"); sys.exit(1)
if rd_ask != {ask_disk}:
    print(f"  MISMATCH: README ASK figures {sorted(rd_ask)} != runnable foundation ASKs ({ask_disk})"); sys.exit(1)
print(f"  [OK] {disk} sh:NodeShape == register rows == DAG == README; "
      f"{ask_disk} runnable foundation ASKs == README ASK figures")
PY

# ---- (5c) the probe self-check: stated fnd:probe* count == on-disk grep union ----------------------
# The README probe register + the phase_w2_sp0 DAG node each STATE a count of named fnd:probe* injection
# identifiers. That figure must equal the true on-disk union:
#   grep -rhoE 'fnd:probe[A-Za-z0-9]+' basicttl/foundation | sort -u | wc -l
# A tooth whose probe is added (or removed) without refreshing BOTH stated figures -> RED here (the same
# stale-doc drift class the register self-check closes for sh:NodeShape). The on-disk union is computed
# dynamically below and compared against both stated figures; no probe count is hardcoded in this comment.
echo "== probe self-check (stated fnd:probe* count == on-disk grep -rhoE union) =="
python3 - <<'PY'
import re, sys, glob, os
from rdflib import Graph, URIRef
from rdflib.namespace import RDFS
probe = set()
for f in glob.glob("basicttl/foundation/**/*", recursive=True):
    if os.path.isfile(f):
        try:
            probe |= set(re.findall(r'fnd:probe[A-Za-z0-9]+', open(f, encoding='utf-8', errors='replace').read()))
        except Exception:
            pass
disk = len(probe)
# stated figure in the phase_w2_sp0 DAG node rdfs:comment
dg = Graph(); dg.parse("basicttl/dag/dag_instances.ttl")
sp0 = URIRef("urn:silmaril:entity#phase_w2_sp0")
com = str(next(dg.objects(sp0, RDFS.comment)))
dag_fig = set(int(m) for m in re.findall(r'(\d+)\s+named\s+fnd:probe', com))
# stated figure at README.md:95 (the "**NN** named ... fnd:probe*" line)
rd = open("basicttl/foundation/README.md", encoding='utf-8').read()
rd_fig = set(int(m) for m in re.findall(r'\*\*(\d+)\*\*\s+named', rd))
print(f"  on-disk fnd:probe* union:  {disk}  ({sorted(probe)})")
print(f"  phase_w2_sp0 DAG figure:   {sorted(dag_fig)}")
print(f"  README.md stated figure:   {sorted(rd_fig)}")
if dag_fig != {disk}:
    print(f"  MISMATCH: DAG figure {sorted(dag_fig)} != on-disk union {disk}"); sys.exit(1)
if rd_fig != {disk}:
    print(f"  MISMATCH: README figure {sorted(rd_fig)} != on-disk union {disk}"); sys.exit(1)
print(f"  [OK] {disk} named fnd:probe* on disk == DAG figure == README figure")
PY

# ---- (5d) the COUNT self-check: EVERY stated figure == its freshly-recomputed disk value ------------
# Fix-B: close the STALE-COUNT class TOTALLY. The register self-check (5b) already gates sh:NodeShape +
# EXPECT-TRUE-ASK and the probe self-check (5c) gates the fnd:probe* union; this step extends that
# discipline to the WHOLE count surface the hostile review found stale (DS/PD/SYN ledger, ObjectProperty,
# both triple totals, distinct-subject total). It RECOMPUTES each figure freshly from disk (rdflib over the
# merged SP0+SP1+SP2+SP3 graph for triples/subjects/authority/class/property counts; the foundation shapes
# graph for sh:NodeShape; foundation.queries.sparql for the runnable-ASK count; a grep union for fnd:probe*)
# and asserts that value is stated -- and stated CORRECTLY -- in BOTH the silm:phase_w2_sp0 DAG node AND
# basicttl/foundation/README.md. For each figure the SET of every labelled occurrence in each surface must
# equal {recomputed}: a single stale occurrence (or a missing one -> empty set != {truth}, so every gate is
# NON-VACUOUS) -> RED, printing the offending figure/surface. So no count in either surface can drift from
# disk again without the runner going RED. PROBE OF RECORD: perturb any stated figure (e.g. the DAG's
# "15376 triples" or README's "528 SYN") -> RED here; restore the true value -> GREEN. Both were exercised.
echo "== count self-check (every stated figure == freshly-recomputed disk value, in BOTH the DAG node AND README) =="
python3 - <<'PY'
import glob, os, re, sys
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, OWL

FND = "urn:silmaril:fnd:#"
SH_NODESHAPE = URIRef("http://www.w3.org/ns/shacl#NodeShape")
AUTH = URIRef(FND + "authority")
DS, PD, SYN = URIRef(FND + "DS"), URIRef(FND + "PD"), URIRef(FND + "SYN")

SP1 = [f"basicttl/primitives/{f}" for f in ["formal.ttl", "physical.ttl", "realization.ttl", "taiji.ttl"]]
SP2 = [f"basicttl/aob/{f}" for f in ["meta.ttl", "upper_anchor.ttl", "octet_descent.ttl", "tensor_block.ttl",
       "value_colimit.ttl", "group_law.ttl", "evidence_glossary.ttl"]]
SP3 = sorted(f for f in glob.glob("basicttl/crs/*.ttl") if not f.endswith(".shapes.ttl"))
SP0 = sorted(f for f in glob.glob("basicttl/foundation/*.ttl") if not f.endswith(".shapes.ttl"))

g0 = Graph()
for f in SP0:
    g0.parse(f)
gm = Graph()
for f in SP0 + SP1 + SP2 + SP3:
    gm.parse(f)

def tagcount(tag):  # subject-level, fnd-namespace scoped
    return len([s for s in gm.subjects(AUTH, tag) if str(s).startswith(FND)])

def typecount(t):
    return len([s for s in gm.subjects(RDF.type, t) if str(s).startswith(FND)])

fnd_subjects = set(s for s in gm.subjects() if isinstance(s, URIRef) and str(s).startswith(FND))

R = {}
for b in re.split(r'\n(?=#\s*EXPECT-TRUE\s)', open("basicttl/foundation/foundation.queries.sparql").read()):
    if not re.search(r'EXPECT-TRUE\s+\S+', b):
        continue
    body = "\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
    if body.strip().upper().startswith(("PREFIX", "ASK")):
        R['ask'] = R.get('ask', 0) + 1

probe = set()
for f in glob.glob("basicttl/foundation/**/*", recursive=True):
    if os.path.isfile(f):
        try:
            probe |= set(re.findall(r'fnd:probe[A-Za-z0-9]+', open(f, encoding='utf-8', errors='replace').read()))
        except Exception:
            pass

recomputed = {
    'sp0_triples':    len(g0),
    'merged_triples': len(gm),
    'subjects':       len(fnd_subjects),
    'ds':             tagcount(DS),
    'pd':             tagcount(PD),
    'syn':            tagcount(SYN),
    'classes':        typecount(OWL.Class),
    'objprop':        typecount(OWL.ObjectProperty),
    'dataprop':       typecount(OWL.DatatypeProperty),
    'nodeshape':      len(set(Graph().parse("basicttl/foundation/foundation.shapes.ttl").subjects(RDF.type, SH_NODESHAPE))),
    'ask':            R.get('ask', 0),
    'probe':          len(probe),
}

# per-figure extraction regex; 'ask' is surface-specific (README labels the foundation count EXPECT-TRUE,
# reserving bare "N ASKs" for the SP1/SP2 figures on the run-crs line; the DAG uses a bare "34 ASKs").
COMMON = {
    'classes':        r'(\d+)\*{0,2}\s+fnd\W{1,4}owl:Class(?![A-Za-z])',
    'objprop':        r'(\d+)\*{0,2}\s+fnd\W{1,4}owl:ObjectProperty',
    'dataprop':       r'(\d+)\*{0,2}\s+fnd\W{1,4}owl:DatatypeProperty',
    'subjects':       r'(\d+)\*{0,2}\s+distinct fnd subjects',
    'ds':             r'(?<![A-Za-z])(\d+)\*{0,2}\s+DS\b',
    'pd':             r'(?<![A-Za-z])(\d+)\*{0,2}\s+PD\b',
    'syn':            r'(?<![A-Za-z])(\d+)\*{0,2}\s+SYN\b',
    'sp0_triples':    r'SP0-only\s*=\s*\*{0,2}(\d+)',
    'merged_triples': r'merged SP0\+SP1\+SP2\+SP3\s*=\s*\*{0,2}(\d+)',
    'nodeshape':      r'(\d+)\*{0,2}\s+(?:`?sh:NodeShape|SHACL teeth)',
    'probe':          r'(\d+)\*{0,2}\s+named\W{1,3}fnd:probe',
}
ASK_RE = {'DAG': r'(?<![A-Za-z])(\d+)\*{0,2}\s+ASKs?\b',
          'README': r'(?<![A-Za-z])(\d+)\*{0,2}\s+EXPECT-TRUE ASKs?'}

dg = Graph(); dg.parse("basicttl/dag/dag_instances.ttl")
sp0node = URIRef("urn:silmaril:entity#phase_w2_sp0")
dagtext = str(next(dg.objects(sp0node, RDFS.comment))) + "\n" + str(next(dg.objects(sp0node, RDFS.label)))
rdtext = open("basicttl/foundation/README.md", encoding='utf-8').read()
surfaces = {'DAG': dagtext, 'README': rdtext}

bad = 0
for key in sorted(set(list(COMMON) + ['ask'])):
    truth = recomputed[key]
    for surf, txt in surfaces.items():
        pat = ASK_RE[surf] if key == 'ask' else COMMON[key]
        got = set(int(m) for m in re.findall(pat, txt))
        ok = (got == {truth})
        print(f"  {'OK  ' if ok else 'MISMATCH'} {key:15s} {surf:6s} disk={truth:<6d} stated={sorted(got)}")
        if not ok:
            bad += 1
if bad:
    print(f"  {bad} figure(s) drifted from disk (or absent) in the DAG node / README -> RED")
    sys.exit(1)
print("  [OK] all 12 recomputed figures == their stated values in BOTH the phase_w2_sp0 DAG node AND README")
PY

# ---- (6) the citation gate: file-resolution AND quote-in-range (design s0 exact-resolvable bar) -----
# Design s0 requires every DS/PD atom's Helios citation to be an EXACT, RESOLVABLE helios/srcy/.../*.tex
# file:line - and "that bar is itself teeth-checked". fnd:AuthorityHonestyShape enforces the coarse form
# IN THE GRAPH (a DS/PD atom with no helios/srcy citation -> RED; an ellipsis / duplicated .tex segment ->
# RED), but SPARQL cannot read the FILESYSTEM. This gate closes what only bash can, in TWO tiers:
#
#   (a) FILE RESOLUTION (the original bar): every helios/srcy/*.tex path cited in a foundation rdfs:comment
#       must exist on disk (test -f). A citation pointing at a non-existent .tex -> RED.
#
#   (b) QUOTE-IN-RANGE (the strengthening that closes the ':line-suffix-ignored' hole the hostile reviewer
#       named at run-foundation-checks.sh:202). The old gate DROPPED the :line suffix and only tested the
#       file - so a citation whose quoted phrase is REAL in the source but drifted to the WRONG lines passed
#       silently. Now: for every single-quoted phrase 'QUOTE' immediately followed by a Helios line-range
#       citation - full (helios/srcy/.../F.tex:START-END), short (F.tex:START-END, resolving F against the
#       comment's current full path), or bare (:START-END, inheriting the current full path), and accepting
#       comma-multi-range specs like :2,16-17,36-39 - the gate tokenizes QUOTE (lowercase, non-alphanumeric
#       runs -> spaces; this tolerates LaTeX \macro{...} noise and line-wrapping in the source) and searches
#       the cited file for an in-order occurrence of those tokens within a bounded line-span. If the quote's
#       tokens ARE present in the file but the match starts OUTSIDE [START-2, END+2] of the cited range, the
#       citation has DRIFTED: the gate prints the atom + citation + the line(s) where the quote really lives
#       and EXITS NON-ZERO (RED). If the quote is not present in the cited file at all, it is an atom
#       gloss/notation/paraphrase rather than a verbatim line-claim (e.g. "e.g. 'eta: 1 => RL ...'", or a
#       recognition slogan) - there is no source line for it to drift FROM, so it keeps the file-resolution
#       -only check, exactly as the task specifies for citations with no adjacent verbatim quote. Two skips
#       keep the gate honest and false-positive-free: a quote prefaced by "e.g." (an illustrative rendering,
#       not a lift) and a quote that itself contains an external "... at lines 1001-1014" reference (a
#       nested quote-of-a-quote citing an outside work, not the Helios file). This is the load-bearing
#       enforcement (SPARQL cannot read files); a lighter in-graph proxy lives in fnd:AuthorityHonestyShape.
#
# PROBE OF RECORD: (a) point one citation at a non-existent .tex -> RED; restore -> GREEN. (b) drift one
# quoted citation's line-range by ~50 lines -> RED (quote found, but outside range); restore the true
# range -> GREEN. Both were exercised.
echo "== citation gate (every helios/srcy .tex resolves on disk AND every quoted line-range contains its quote AND every DS/PD helios citation carries an exact :line) =="
python3 - <<'PY'
import glob, os, re, sys
from rdflib import Graph, URIRef
from rdflib.namespace import RDFS

# (a) A cited Helios source path: helios/srcy/.../<file>.tex . The char class excludes whitespace, quotes and
# the <>* placeholder characters (so documentation prose like "helios/srcy/<paper>/.../<file>.tex" in a
# shape comment is never mistaken for a real citation), and stops at the .tex extension.
PATH_RE = re.compile(r'helios/srcy/[^\s"\'<>*)]+?\.tex')

# (c) exact-line bar (design s0, strengthened): EVERY helios/srcy citation on a DS/PD-tagged atom MUST pin
# its line(s) with a ':START(-END)?' suffix. A bare-file citation (no :line) is the ':line-suffix-ignored'
# hole the earlier CONTAINS('helios/srcy/') check let through. This regex captures the optional line spec so
# a None group is a BARE-FILE citation. SPARQL cannot iterate each citation, so this per-citation, DS/PD-
# scoped sweep is the load-bearing enforcement; fnd:AuthorityHonestyShape carries the in-graph proxy.
HELIOS_LINE = re.compile(r'helios/srcy/[^\s",;)]*?\.tex(:\d[\d,\-]*)?')
FND_AUTHORITY = URIRef("urn:silmaril:fnd:#authority")
DS_PD = {URIRef("urn:silmaril:fnd:#DS"), URIRef("urn:silmaril:fnd:#PD")}

# (b) quote + line-range extraction.
QUOTE    = re.compile(r"(?<![A-Za-z0-9])'([^']{4,}?)'(?![A-Za-z0-9])")   # a genuine quote, not a possessive '
SPECPART = r'(?:\d+(?:-\d+)?)(?:,\d+(?:-\d+)?)*'                          # 199  |  30-48  |  2,16-17,36-39
FULL     = re.compile(r'(helios/srcy/[^\s"\'<>*)]+?\.tex):(' + SPECPART + r')')
SHORT    = re.compile(r'(?<![/\w])([A-Za-z0-9_]+\.tex):(' + SPECPART + r')')
BARE     = re.compile(r'(?<![\w/:]):(' + SPECPART + r')(?!\d)')
LINESREF = re.compile(r'\blines?\s+\d')                                  # nested "... at lines 1001-1014" ref
SPAN     = 9                                                             # max source lines a quote may span

def parse_spec(spec):
    out = []
    for part in spec.split(','):
        if '-' in part:
            a, b = part.split('-'); out.append((int(a), int(b)))
        else:
            out.append((int(part), int(part)))
    return out

def norm(text):
    return re.sub(r'[^a-z0-9]+', ' ', text.lower()).split()

_TOKS = {}
def toks_of(path):
    if path not in _TOKS:
        out = []
        for i, line in enumerate(open(path, encoding='utf-8', errors='replace').read().splitlines(), 1):
            for t in norm(line):
                out.append((t, i))
        _TOKS[path] = out
    return _TOKS[path]

def match_startlines(qtokens, toks):
    # every start-line L at which qtokens appears as an in-order subsequence within lines [L, L+SPAN]
    n, m, starts = len(toks), len(qtokens), []
    if not m:
        return starts
    for i in range(n):
        if toks[i][0] != qtokens[0]:
            continue
        L0 = toks[i][1]; j = 1; k = i + 1
        while k < n and j < m:
            if toks[k][1] > L0 + SPAN:
                break
            if toks[k][0] == qtokens[j]:
                j += 1
            k += 1
        if j == m:
            starts.append(L0)
    return starts

def inrange(L, rngs):
    return any(a - 2 <= L <= b + 2 for a, b in rngs)

missing, drift, bareline, checked_files, checked_quotes, checked_dspd = [], [], [], 0, 0, 0
for f in sorted(glob.glob("basicttl/foundation/*.ttl")):
    g = Graph(); g.parse(f)
    for subj, _, obj in g.triples((None, RDFS.comment, None)):
        s = str(obj)
        # (a) file resolution
        for m in PATH_RE.finditer(s):
            checked_files += 1
            if not os.path.isfile(m.group(0)):
                missing.append((f, str(subj), m.group(0)))
        # (c) exact-line: every helios/srcy citation on a DS/PD atom MUST carry a :line
        if DS_PD & set(g.objects(subj, FND_AUTHORITY)):
            for m in HELIOS_LINE.finditer(s):
                checked_dspd += 1
                if not m.group(1):
                    bareline.append((f, str(subj), m.group(0)))
        # (b) quote-in-range: order all quote + citation events, track the comment's current full path
        ev = [(m.start(), 'Q', m.group(1)) for m in QUOTE.finditer(s)]
        fsp = []
        for m in FULL.finditer(s):
            ev.append((m.start(), 'F', (m.group(1), m.group(2)))); fsp.append((m.start(), m.end()))
        ssp = list(fsp)
        for m in SHORT.finditer(s):
            if any(a <= m.start() < b for a, b in fsp):
                continue
            ev.append((m.start(), 'S', (m.group(1), m.group(2)))); ssp.append((m.start(), m.end()))
        for m in BARE.finditer(s):
            if any(a <= m.start() < b for a, b in ssp):
                continue
            ev.append((m.start(), 'B', m.group(1)))
        ev.sort()
        curpath = None
        for idx, (pos, kind, val) in enumerate(ev):
            if kind == 'F':
                curpath = val[0]
            if kind != 'Q':
                continue
            q = val
            if re.search(r'\be\.?g\.?\b', s[max(0, pos - 9):pos]):   # illustrative rendering, not a lift
                continue
            if LINESREF.search(q):                                    # nested external page/line reference
                continue
            cite = None                                               # (path, spec) of the adjacent citation
            for j in range(idx + 1, len(ev)):
                _, k2, v2 = ev[j]
                if k2 == 'Q':
                    break
                if k2 == 'F':
                    cite = (v2[0], v2[1]); break
                if k2 == 'S':
                    cite = (curpath, v2[1]) if (curpath and os.path.basename(curpath) == v2[0]) else None
                    break
                if k2 == 'B':
                    cite = (curpath, v2) if curpath else None
                    break
            if not cite or not cite[0]:
                continue                                              # no resolvable adjacent Helios citation
            path, spec = cite
            if not os.path.isfile(path):
                continue                                              # (a) already flags a missing file
            starts = match_startlines(norm(q), toks_of(path))
            if not starts:
                continue                                              # gloss/notation, not a verbatim line-claim
            checked_quotes += 1
            if not any(inrange(L, parse_spec(spec)) for L in starts):
                drift.append((f, str(subj), q, path, spec, sorted(set(starts))))

bad = False
if missing:
    bad = True
    print(f"  CITATION RESOLUTION FAILED: {len(missing)} cited helios/srcy file(s) do NOT exist on disk:")
    for f, su, p in missing:
        print(f"    {f}: <{su}> cites non-resolving {p}")
if drift:
    bad = True
    print(f"  CITATION LINE-RANGE DRIFT: {len(drift)} quoted citation(s) whose quote IS in the cited file")
    print(f"  but OUTSIDE the cited range (the ':line-suffix-ignored' hole at run-foundation-checks.sh:202):")
    for f, su, q, p, spec, starts in drift:
        print(f"    {f}: <{su}>")
        print(f"        quote '{q[:72]}'")
        print(f"        cited {os.path.basename(p)}:{spec} but the quote really begins at line(s) {starts}")
if bareline:
    bad = True
    print(f"  DS/PD BARE-FILE CITATION (no :line): {len(bareline)} helios/srcy citation(s) on a DS/PD-tagged")
    print(f"  atom carry a bare file with NO ':START(-END)?' line suffix (design s0 exact-line bar):")
    for f, su, p in bareline:
        print(f"    {f}: <{su}> cites bare-file {p} (append the true :line, or retag fnd:SYN)")
if bad:
    sys.exit(1)
print(f"  [OK] {checked_files} helios/srcy .tex citations resolve on disk; "
      f"{checked_quotes} quoted line-range citations confirmed to contain their quote (+/-2 lines); "
      f"{checked_dspd} DS/PD helios citations all carry an exact :line")
PY

echo "FOUNDATION CHECKS GREEN"
