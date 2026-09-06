#!/usr/bin/env bash
# =====================================================================================
# run-algebra-checks.sh — the folded algebra-spine verification runner (W2 · SP0, T-INFRA).
# =====================================================================================
# The algebra tower is folded into basicttl/primordial/type/algebra/** (D25 placement), minting the
# full runtime Linnaean-ladder IRIs (D26) in the D24 Seed-Carrier stratified idiom (theory / model /
# signature / operation / equation / reduct records + proof-status + validation-mode + provenance +
# fixtures). The committed run-foundation-checks.sh globs ONLY basicttl/foundation/*.ttl for its SP0
# slice, so the folded tree is in NO runner unless one is authored + wired into ci.yml IN LOCKSTEP
# (design §4; D25 CI-lockstep). This runner is that gate. It is deliberately NON-VACUOUS: it REJECTS
# the states a naive `sh:conforms true` would pass silently.
#
# It proves, over the algebra subtree, FIVE things:
#
#   (a) DATA CONFORMANCE. Auto-discover every basicttl/primordial/type/algebra/**/*.ttl EXCEPT the
#       shapes graph (*.shapes.ttl) and EXCEPT fixtures/** (evidence plane, D24 four-planes) as the
#       data graph, and validate it against shapes/algebra.shapes.ttl with pyshacl (inference=rdfs).
#   (b) FIXTURE POLARITY (witnesses cannot go silent). Iterate fixtures/** — every POSITIVE fixture,
#       merged onto the conformant data graph, MUST still conform; every NEGATIVE fixture MUST NOT
#       conform (its single injected violation must bite); the empty.ttl control MUST be an admission
#       REJECT (a vacuous 0-focus graph, never a silent pass). A negative that fails to flip -> RED.
#   (c) NON-VACUITY (0-focus REJECT). Every declared NodeShape MUST have >= 1 focus node over the
#       data graph. A shape with zero focus nodes is UNEXERCISED = REJECT — the inversion of
#       run-foundation-checks.sh:90-102 (which SKIPS a shapeless graph; here 0-focus is a failure).
#   (d) COUNT COVERAGE (V6). Recompute every algebra figure from disk and assert it equals the
#       manifest (manifests/*.yaml). While no manifest states a figure this is reported PENDING (the
#       full self-check is wired by T-MANIFEST, which also edits this runner); a STATED figure that
#       disagrees with disk -> RED.
#   (e) DEPTH. Every owl:Class under the folded algebra tree carries a >= 200-char rdfs:comment
#       (scripts/ontology-depth-check.py), the same depth gate idiom run-foundation-checks.sh:143
#       applies to the foundation floor (design §4 / ci step).
#
# Exits 0 IFF all hold. RED PROBE OF RECORD: on the FIRST run — before any fixtures or shapes exist —
# fixture discovery is empty, so the runner prints "no fixtures discovered; gate would be vacuous" and
# exits non-zero. That non-zero IS the runner's own RED: witnesses cannot be absent AND the gate green.
#
# Design spec: docs/superpowers/specs/2026-09-06-w2-sp0-primordial-fold-design.md (§4)
# Plan:        docs/superpowers/plans/2026-09-06-w2-sp0-spine-fold-plan.md (Task T-INFRA)
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

ALG="basicttl/primordial/type/algebra"
SHAPES="${ALG}/shapes/algebra.shapes.ttl"

echo "== folded algebra spine gate (${ALG}) =="
python3 - "$ALG" "$SHAPES" <<'PY'
import glob, os, sys, re
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS
from pyshacl import validate

ALG, SHAPES = sys.argv[1], sys.argv[2]
SH = "http://www.w3.org/ns/shacl#"
SH_NODESHAPE   = URIRef(SH + "NodeShape")
SH_TARGETCLASS = URIRef(SH + "targetClass")
SH_TARGETNODE  = URIRef(SH + "targetNode")

def norm(p):        return p.replace(os.sep, "/")
def is_shapes(p):   return p.endswith(".shapes.ttl")
def is_fixture(p):  return "/fixtures/" in norm(p)
def tail(iri, n=4): return ":".join(str(iri).split(":")[-n:])

# ---- discovery ---------------------------------------------------------------------------------
data_files = sorted(f for f in glob.glob(f"{ALG}/**/*.ttl", recursive=True)
                    if not is_shapes(f) and not is_fixture(f))
fixture_files = sorted(f for f in glob.glob(f"{ALG}/fixtures/**/*.ttl", recursive=True)
                       if not is_shapes(f))

problems = 0

# ---- (b, vacuity trap) the RED probe of record: no fixtures => gate would be vacuous ------------
if not fixture_files:
    print("  REJECT: no fixtures discovered; gate would be vacuous "
          "(witnesses missing -> the algebra teeth prove nothing). This is the T-INFRA RED probe of "
          "record; it clears once T-FIX/T-MONOID land >= 1 positive + >= 1 negative + empty.ttl.")
    sys.exit(1)

# ---- shapes graph must declare >= 1 NodeShape --------------------------------------------------
if not os.path.exists(SHAPES):
    print(f"  REJECT: shapes graph {SHAPES} absent"); sys.exit(1)
shapes = Graph(); shapes.parse(SHAPES)
declared = sorted(set(shapes.subjects(RDF.type, SH_NODESHAPE)), key=str)
if not declared:
    print("  REJECT: no NodeShape declared in shapes/algebra.shapes.ttl; gate would be vacuous")
    sys.exit(1)

# any targetNode shape is the design's anti-pattern (§4): all algebra shapes MUST use targetClass
for sh_node in declared:
    if list(shapes.objects(sh_node, SH_TARGETNODE)):
        print(f"  REJECT: shape <{tail(sh_node)}> uses sh:targetNode (anti-pattern; use sh:targetClass "
              "so the 0-focus gate can count focus nodes)")
        problems += 1

# ---- build the data graph ----------------------------------------------------------------------
base = Graph()
for f in data_files:
    base.parse(f)
print(f"  data: {len(data_files)} ttl -> {len(base)} triples; "
      f"shapes: {len(declared)} NodeShape(s); fixtures: {len(fixture_files)}")

# ---- (a) data conformance ----------------------------------------------------------------------
ok, _, rep = validate(base, shacl_graph=shapes, inference="rdfs")
print(f"  (a) data graph conforms: {ok}")
if not ok:
    print(rep[:3000]); problems += 1

# ---- (c) non-vacuity: every NodeShape MUST have >= 1 focus node ---------------------------------
# subclass closure so an rdfs-subclass instance still counts as a focus node of its ancestor's shape.
children = {}
for s, _, o in base.triples((None, RDFS.subClassOf, None)):
    children.setdefault(o, set()).add(s)
def descendants(c):
    seen, stack = set(), [c]
    while stack:
        x = stack.pop()
        for y in children.get(x, ()):
            if y not in seen:
                seen.add(y); stack.append(y)
    return seen
for sh_node in declared:
    tcs = list(shapes.objects(sh_node, SH_TARGETCLASS))
    if not tcs:
        continue  # non-targetClass shapes (e.g. targetNode, already rejected above) are not focus-counted
    focus = set()
    for tc in tcs:
        for c in {tc} | descendants(tc):
            focus |= set(base.subjects(RDF.type, c))
    if not focus:
        print(f"  (c) REJECT 0-focus: <{tail(sh_node)}> targets "
              f"{[tail(t) for t in tcs]} with ZERO focus nodes (unexercised)")
        problems += 1
    else:
        print(f"  (c) focus OK: <{tail(sh_node)}> {len(focus)} focus node(s)")

# ---- (b) fixture polarity ----------------------------------------------------------------------
pos = neg = emp = 0
for fx in fixture_files:
    name = os.path.basename(fx).lower()
    if "empty" in name:
        eg = Graph(); eg.parse(fx)
        # an admissible focus over ANY declared shape's target class
        efocus = 0
        for sh_node in declared:
            for tc in shapes.objects(sh_node, SH_TARGETCLASS):
                for c in {tc} | descendants(tc):
                    efocus += len(set(eg.subjects(RDF.type, c)))
        if efocus == 0:
            print(f"  (b) PASS empty control: {fx} => admission REJECT (0 focus, vacuous)")
            emp += 1
        else:
            print(f"  (b) FAIL empty control: {fx} has {efocus} focus node(s); not an empty submission")
            problems += 1
        continue
    g = Graph(); g += base; g.parse(fx)
    okf, _, repf = validate(g, shacl_graph=shapes, inference="rdfs")
    if "neg" in name:                       # negative (…neg…/…negative…)
        neg += 1
        if okf:
            print(f"  (b) FAIL negative: {fx} CONFORMED (its injected violation did not bite)")
            problems += 1
        else:
            print(f"  (b) PASS negative: {fx} does NOT conform (tooth bites)")
    else:                                    # positive (…pos…/…positive…/any other witness)
        pos += 1
        if okf:
            print(f"  (b) PASS positive: {fx} conforms")
        else:
            print(f"  (b) FAIL positive: {fx} did NOT conform")
            print(repf[:2000]); problems += 1
print(f"  (b) fixtures: {pos} positive, {neg} negative, {emp} empty control")
if pos == 0:
    print("  REJECT: no POSITIVE fixture discovered; gate would be vacuous"); problems += 1
if neg == 0:
    print("  REJECT: no NEGATIVE fixture discovered; a conforms-true-only gate is vacuous"); problems += 1
if emp == 0:
    print("  REJECT: no empty.ttl admission control discovered (design §4 empty => REJECT)"); problems += 1

# ---- (d) count coverage vs manifest (V6) -------------------------------------------------------
# recompute every algebra figure from disk; assert it equals the value the manifest STATES. While no
# manifest states a figure the check is PENDING (the full self-check + manifest are T-MANIFEST, which
# also edits this runner). A stated figure disagreeing with disk -> RED.
def type_count(t):
    return len(set(base.subjects(RDF.type, URIRef(t))))
disk = {
    "data_files":   len(data_files),
    "nodeshapes":   len(declared),
    "fixtures":     len(fixture_files),
    "triples":      len(base),
}
manifest_files = sorted(glob.glob(f"{ALG}/manifests/*.yaml"))
stated_any = False
for mf in manifest_files:
    txt = open(mf, encoding="utf-8").read()
    for key, truth in disk.items():
        for m in re.finditer(rf'(?m)^\s*{re.escape(key)}\s*:\s*(\d+)\s*$', txt):
            stated_any = True
            got = int(m.group(1))
            ok_c = (got == truth)
            print(f"  (d) {'OK  ' if ok_c else 'MISMATCH'} {key}: disk={truth} manifest({os.path.basename(mf)})={got}")
            if not ok_c:
                problems += 1
if not manifest_files or not stated_any:
    print(f"  (d) PENDING: no manifest figure stated yet (T-MANIFEST wires the full V6 self-check); "
          f"disk figures = {disk}")

sys.exit(1 if problems else 0)
PY

# ---- (e) depth gate over the folded algebra classes (design §4 / run-foundation-checks.sh:143) ---
echo "== depth gate (every owl:Class under ${ALG} >= 200-char rdfs:comment) =="
python3 scripts/ontology-depth-check.py "${ALG}"

echo "ALGEBRA CHECKS GREEN"
