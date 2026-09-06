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
import yaml
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

# ---- (d) count coverage vs manifest AND DAG (V6, T-MANIFEST) ------------------------------------
# Recompute EVERY algebra figure freshly from disk (rdflib over the merged algebra data graph; the shapes
# graph; probes/*.rq; fixtures/**) and assert disk == manifests/*.yaml == the phase_w2_sp0_fold DAG node.
# Nothing is hard-coded: the manifest and the DAG node STATE figures, this block RECOMPUTES them and
# demands equality across all three surfaces. A stated figure that disagrees with a fresh disk recount ->
# RED (V6). Every surface is NON-VACUOUS: a required figure that is MISSING (empty match set != {truth})
# is itself RED, so a silently-dropped count cannot pass. PROBE OF RECORD: perturb any manifest VALUE, or
# the DAG node's shape/probe/rung/fixture figure -> V6 RED; restore -> GREEN.
REC_ = ("urn:silmaril:type:graph:instance:instruction:code:property:grounding:ontology:basic:formal:"
        "domain:knowledge:representation:kingdom:specification:phylum:formal:contract:class:class:order:"
        "declared:family:seed:genus:registry:species:")
TYP_  = "urn:silmaril:type:graph:instance:instruction:code:property:type:"
CORE_ = "urn:silmaril:type:graph:instance:instruction:code:property:core:entity:"
GATE_SPEC_   = URIRef(CORE_ + "structure:class:gate:specification")
CLAUSE_SPEC_ = URIRef(CORE_ + "structure:class:gate:clause:specification")
def type_count(t):
    return len(set(base.subjects(RDF.type, URIRef(t))))
def rec_count(leaf):
    return type_count(REC_ + leaf + ":record")
def rung_count(rung, leaf):
    # per-rung recompute by the mathematics-ladder subdomain segment (compounds: 'commutative:monoid')
    return sum(1 for s in set(base.subjects(RDF.type, URIRef(REC_ + leaf + ":record")))
               if f":subdomain:{rung}:kingdom:" in str(s))

disk = {
    "theories":     rec_count("theory"),
    "models":       rec_count("model"),
    "denotata":     rec_count("denotatum"),
    "declarations": rec_count("declaration"),
    "signatures":   rec_count("signature"),
    "operations":   len({s for s in set(base.subjects()) if ":kingdom:operation:" in str(s)}),
    "axioms":       rec_count("axiom"),
    "theorems":     rec_count("theorem"),
    "certificates": type_count(TYP_ + "certificate"),
    "equations":    rec_count("equation"),
    "reducts":      rec_count("reduct"),
    "gate_specs":   len(set(base.subjects(RDF.type, GATE_SPEC_))),
    "clause_specs": len(set(base.subjects(RDF.type, CLAUSE_SPEC_))),
    "rungs":        rec_count("theory"),        # one theory record per concrete rung (progenitor excl.)
    "shapes":       len(declared),
    "probes":       len(glob.glob(f"{ALG}/probes/*.rq")),
    "fixtures":     len(fixture_files),
    "data_files":   len(data_files),
    "triples":      len(base),
}
RUNG_KEYMAP = {"THEORY": "theory", "MODEL": "model", "DENOTATUM": "denotatum", "DECLARATION": "declaration",
               "AXIOMS": "axiom", "THEOREMS": "theorem", "EQUATIONS": "equation", "REDUCTS": "reduct"}
EXPECTED_RUNGS = {"magma", "semigroup", "monoid", "commutative:monoid", "group", "abelian:group",
                  "quasigroup", "loop"}

manifest_files = sorted(glob.glob(f"{ALG}/manifests/*.yaml"))
v6_mismatch = 0            # figure-level disagreements (manifest or DAG) — drives gate V6
spine_counts = {}          # figures parsed from the spine.yaml COUNT block
rung_scopes_seen = set()

if not manifest_files:
    print("  (d) REJECT: no manifests/*.yaml discovered; the V6 self-check would be vacuous "
          "(T-MANIFEST must state disk-derived figures)")
    problems += 1

def yaml_counts(doc):
    return (doc.get("MATERIALIZATION", {}) or {}).get("COUNT", {}) or {}

for mf in manifest_files:
    try:
        doc = yaml.safe_load(open(mf, encoding="utf-8")) or {}
    except Exception as e:
        print(f"  (d) REJECT: manifest {os.path.basename(mf)} is not valid YAML: {e}")
        v6_mismatch += 1; continue
    scope = (((doc.get("ATOM", {}) or {}).get("SCOPE", {}) or {}).get("VALUE"))
    cblock = yaml_counts(doc)
    if scope is None:
        print(f"  (d) REJECT: {os.path.basename(mf)} declares no ATOM:SCOPE:VALUE")
        v6_mismatch += 1; continue
    if not cblock:
        print(f"  (d) REJECT: {os.path.basename(mf)} states no MATERIALIZATION:COUNT figure (vacuous)")
        v6_mismatch += 1; continue
    for fkey, fnode in cblock.items():
        try:
            val = int((((fnode or {}).get("CARDINALITY", {}) or {}).get("NOTATION", {}) or {}).get("VALUE"))
        except (TypeError, ValueError):
            print(f"  (d) MALFORMED {os.path.basename(mf)}:{fkey} (no CARDINALITY:NOTATION:VALUE integer)")
            v6_mismatch += 1; continue
        if scope == "spine":
            ck = fkey.lower()
            if ck not in disk:
                print(f"  (d) UNKNOWN spine figure {os.path.basename(mf)}:{fkey}")
                v6_mismatch += 1; continue
            truth = disk[ck]; spine_counts[ck] = val
        else:
            leaf = RUNG_KEYMAP.get(fkey)
            if leaf is None:
                print(f"  (d) UNKNOWN rung figure {os.path.basename(mf)}:{fkey}")
                v6_mismatch += 1; continue
            truth = rung_count(scope, leaf); rung_scopes_seen.add(scope)
        ok_c = (val == truth)
        print(f"  (d) {'OK  ' if ok_c else 'MISMATCH'} {os.path.basename(mf)}[{scope}]:{fkey} "
              f"disk={truth} manifest={val}")
        if not ok_c:
            v6_mismatch += 1

# spine.yaml must state EVERY canonical figure (a missing figure is a silently-dropped count -> RED)
missing_spine = [k for k in disk if k not in spine_counts]
if missing_spine:
    print(f"  (d) REJECT: spine.yaml omits figure(s) {sorted(missing_spine)} (non-vacuity: every "
          f"canonical count must be stated + gated)")
    v6_mismatch += 1
# every one-operation rung must have a per-rung manifest
missing_rungs = EXPECTED_RUNGS - rung_scopes_seen
if missing_rungs:
    print(f"  (d) REJECT: no per-rung manifest for {sorted(missing_rungs)}")
    v6_mismatch += 1

# --- the phase_w2_sp0_fold DAG node: disk == DAG for the shape/probe/rung/fixture narrative figures ---
DAG_FILE = "basicttl/dag/dag_instances.ttl"
DAG_NARRATIVE = {"rungs": r'(\d+)\s+rungs', "shapes": r'(\d+)\s+shapes',
                 "probes": r'(\d+)\s+probes', "fixtures": r'(\d+)\s+fixtures'}
dag_mismatch = 0
try:
    _dg = Graph(); _dg.parse(DAG_FILE)
    _fold = URIRef("urn:silmaril:entity#phase_w2_sp0_fold")
    dagtext = " ".join(str(o) for p in (RDFS.comment, RDFS.label) for o in _dg.objects(_fold, p))
    if not dagtext.strip():
        print(f"  (d) REJECT: phase_w2_sp0_fold DAG node absent/empty in {DAG_FILE}")
        dag_mismatch += 1
    for ck, rx in DAG_NARRATIVE.items():
        hits = set(int(m) for m in re.findall(rx, dagtext))
        if not hits:
            print(f"  (d) DAG MISSING: phase_w2_sp0_fold states no '{ck}' figure (vacuous)")
            dag_mismatch += 1; continue
        if hits != {disk[ck]}:
            print(f"  (d) DAG MISMATCH {ck}: DAG={sorted(hits)} disk={disk[ck]}")
            dag_mismatch += 1
        else:
            print(f"  (d) DAG OK {ck}: disk={disk[ck]} == manifest={spine_counts.get(ck)} == DAG "
                  f"(disk==manifest==DAG)")
except Exception as e:
    print(f"  (d) REJECT: could not read the phase_w2_sp0_fold DAG node: {e}")
    dag_mismatch += 1

problems += v6_mismatch + dag_mismatch
print(f"  (d) V6 count self-check: {len(spine_counts)} spine + {len(rung_scopes_seen)} rung manifest(s), "
      f"4 DAG narrative figures; {v6_mismatch} manifest + {dag_mismatch} DAG mismatch(es)")

# ================================================================================================
# (f) GATES V0-V8 (T-GATES) — assert each gate of the folded ladder EXPLICITLY. The gate/clause SPEC
# records ride the reference core:entity gate ladder (gates/gates.ttl, consolidated.shacl.ttl:1324);
# the gate-identity / clause-identity uniqueness teeth (GateIdentityShape / ClauseIdentityShape) are
# already exercised by the SHACL validation (a) + fixture polarity (b). Here every gate is a NAMED,
# direct assertion so the runner reports V0-V8 status honestly (Praeriehund: never claim a gate that
# did not run). V0/V1/V2/V3/V5/V8 are asserted GREEN here; V4 (Yoneda-density) is the fan-out
# deferral; V6 (manifest coverage) rides block (d); V7 (dual provenance) is the T-PROV build.
# ================================================================================================
print("== gates V0-V8 (folded algebra gate ladder, design §4) ==")
REL  = "urn:silmaril:type:graph:instance:instruction:code:property:relation:"
REC  = ("urn:silmaril:type:graph:instance:instruction:code:property:grounding:ontology:basic:formal:"
        "domain:knowledge:representation:kingdom:specification:phylum:formal:contract:class:class:order:"
        "declared:family:seed:genus:registry:species:")
PRIM = "urn:silmaril:primordial:type:"
CORE = "urn:silmaril:type:graph:instance:instruction:code:property:core:entity:"
GATE_SPEC   = URIRef(CORE + "structure:class:gate:specification")
CLAUSE_SPEC = URIRef(CORE + "structure:class:gate:clause:specification")
GATE_ID     = URIRef(CORE + "property:data:gate:identifier")
CLAUSE_ID   = URIRef(CORE + "property:data:clause:identifier")

def gate(v, ok, detail):
    global problems
    if ok is True:
        print(f"  {v} GREEN: {detail}")
    elif ok is None:
        print(f"  {v} PENDING/DEFERRED: {detail}")
    else:
        print(f"  {v} RED: {detail}"); problems += 1

# --- V0 SYNTAX: every *.ttl under the tree parses as Turtle -------------------------------------
all_ttl = sorted(glob.glob(f"{ALG}/**/*.ttl", recursive=True))
v0_bad = []
for f in all_ttl:
    try:
        Graph().parse(f)
    except Exception as e:
        v0_bad.append(f"{f}: {e}")
gate("V0", not v0_bad, f"{len(all_ttl)} Turtle files parse" if not v0_bad else "; ".join(v0_bad[:3]))

# --- V1 HYGIENE (REFINED, design §4/§7.5): no denotatum pun / no provenance on a denotatum;
#     a declaration-record owl:Class carrying provenance is EXEMPT (never scanned here) -----------
prov_preds = [URIRef(REL + p) for p in ("created", "modified", "version", "state", "authority")]
DENOT = URIRef(REC + "denotatum:record")
v1_bad = []
for d in set(base.subjects(RDF.type, DENOT)):
    for p in prov_preds:
        if list(base.objects(d, p)):
            v1_bad.append(f"denotatum <{tail(d)}> carries provenance {str(p).split(':')[-1]}")
CLASSDECL = URIRef(PRIM + "ClassDeclaration")
for cd in set(base.subjects(RDF.type, CLASSDECL)):
    doms = {t for t in base.objects(cd, RDF.type)
            if str(t).startswith(PRIM) and str(t) != PRIM + "ClassDeclaration"}
    if len(doms) >= 2:
        v1_bad.append(f"ClassDeclaration <{tail(cd)}> punned into {sorted(tail(x) for x in doms)}")
gate("V1", not v1_bad,
     "no denotatum/domain-class pun; no provenance on any denotatum (declaration-records exempt)"
     if not v1_bad else "; ".join(v1_bad[:3]))

# --- V2 NON-VACUOUS: empty => REJECT + no 0-focus shape (biting logic in blocks (b)/(c)) --------
gate("V2", emp >= 1,
     f"empty.ttl admission REJECT confirmed; all {len(declared)} shapes 0-focus-gated in block (c)"
     if emp >= 1 else "no empty.ttl admission control discovered")

# --- V3 CATEGORICAL PROBES: sh:sparql / sh:select clauses present in the shapes graph -----------
SH_SPARQL = URIRef(SH + "SPARQLConstraint")
n_sparql = len(set(shapes.subjects(RDF.type, SH_SPARQL)))
gate("V3", n_sparql >= 1, f"{n_sparql} sh:SPARQLConstraint clause(s) declared in the shapes graph")

# --- V4 YONEDA-DENSITY: Pass-2 fan-out (design §6) ---------------------------------------------
gate("V4", None, "Yoneda-density fixtures are the Pass-2 fan-out (design §6); the spine mints none")

# --- V5 ALGEBRAIC-LAW: every theory names signature + equation(s) + validation:mode + proof:status
THEORY = URIRef(REC + "theory:record")
SIGP, EQP = URIRef(REL + "signature"), URIRef(REL + "equation")
VMODE, PSTAT = URIRef(REL + "validation:mode"), URIRef(REL + "proof:status")
theories = sorted(set(base.subjects(RDF.type, THEORY)), key=str)
v5_bad = []
for t in theories:
    if not list(base.objects(t, SIGP)):  v5_bad.append(f"<{tail(t)}> no signature")
    if not list(base.objects(t, EQP)):   v5_bad.append(f"<{tail(t)}> no equation")
    if not list(base.objects(t, VMODE)): v5_bad.append(f"<{tail(t)}> no validation:mode")
    if not list(base.objects(t, PSTAT)): v5_bad.append(f"<{tail(t)}> no proof:status")
v5_ok = (len(theories) >= 1) and not v5_bad
gate("V5", v5_ok,
     f"all {len(theories)} theory records name signature+equation+validation:mode+proof:status"
     if v5_ok else ("no theory records" if not theories else "; ".join(v5_bad[:4])))

# --- V6 MANIFEST COVERAGE: disk == manifest == DAG (block (d) is authoritative) -----------------
v6_total = v6_mismatch + dag_mismatch
gate("V6", v6_total == 0,
     f"disk == manifests/*.yaml == phase_w2_sp0_fold DAG node "
     f"({len(spine_counts)} spine figures + {len(rung_scopes_seen)} per-rung manifests + 4 DAG "
     f"narrative figures all equal a fresh disk recount)"
     if v6_total == 0 else
     f"{v6_mismatch} manifest + {dag_mismatch} DAG figure(s) disagree with disk (block (d))")

# --- V7 PROVENANCE CLOSURE: executor>=1 AND shadow>=1 + wasGeneratedBy on every reshaped record ---
# BUILT (T-PROV): the reference governance/ layer is empty; the executor + tandem-shadow review lane
# lives under reviews/{executor,shadow,resolved}/ + receipts/. A "reshaped record" is a subject that
# carries the D24 provenance quartet (@rel:authority) — the 8 theory + 8 model/declaration + 7 reduct
# + 6 theorem records; Plane-2 denotata carry no @rel:authority and are OUT of scope (V1: no
# provenance on a denotatum). Each MUST be attributed to >= 1 EXECUTOR agent AND >= 1 SHADOW agent
# (prov:wasAttributedTo) plus a prov:wasGeneratedBy. This is the authoritative dual-count; the
# shapes-graph ProvenanceClosureShape (block (b)) and probes/provenance_closure.rq are its twins.
PROVNS  = "http://www.w3.org/ns/prov#"
GPROV   = "urn:silmaril:type:graph:instance:instruction:code:property:governance:provenance:"
WAT     = URIRef(PROVNS + "wasAttributedTo")
WGB     = URIRef(PROVNS + "wasGeneratedBy")
EXEC_CLASS   = URIRef(GPROV + "class:agent:executor")
SHADOW_CLASS = URIRef(GPROV + "class:agent:shadow")
AUTHORITY    = URIRef(REL + "authority")
if not os.path.isdir(f"{ALG}/reviews"):
    gate("V7", None,
         "reviews/ absent; the dual executor/shadow provenance lane is the T-PROV deliverable (design §4 V7 GAP)")
else:
    reshaped    = sorted(set(base.subjects(AUTHORITY, None)), key=str)
    execs_all   = set(base.subjects(RDF.type, EXEC_CLASS))
    shadows_all = set(base.subjects(RDF.type, SHADOW_CLASS))
    v7_bad = []
    for r in reshaped:
        att = set(base.objects(r, WAT))
        if not (att & execs_all):            v7_bad.append(f"<{tail(r)}> no executor attribution")
        if not (att & shadows_all):          v7_bad.append(f"<{tail(r)}> no shadow attribution")
        if not list(base.objects(r, WGB)):   v7_bad.append(f"<{tail(r)}> no prov:wasGeneratedBy")
    v7_ok = (len(reshaped) >= 1) and (len(execs_all) >= 1) and (len(shadows_all) >= 1) and not v7_bad
    gate("V7", v7_ok,
         f"all {len(reshaped)} reshaped records dual-attributed: executor>=1 AND shadow>=1 "
         f"(prov:wasAttributedTo) + prov:wasGeneratedBy "
         f"({len(execs_all)} executor agent(s), {len(shadows_all)} shadow agent(s))"
         if v7_ok else
         ("; ".join(v7_bad[:4]) if v7_bad else
          f"reshaped={len(reshaped)} executor_agents={len(execs_all)} shadow_agents={len(shadows_all)}"))

# --- V8 SHACL-2017 DISCIPLINE: shapes graph loaded, targetClass-only, >=1 SPARQLConstraint -------
n_targetnode  = sum(1 for s in declared if list(shapes.objects(s, SH_TARGETNODE)))
n_targetclass = sum(1 for s in declared if list(shapes.objects(s, SH_TARGETCLASS)))
v8_ok = (len(declared) >= 1) and (n_targetnode == 0) and (n_targetclass == len(declared)) and (n_sparql >= 1)
gate("V8", v8_ok,
     f"shapes graph valid SHACL; {len(declared)} NodeShapes all sh:targetClass, 0 sh:targetNode, {n_sparql} sh:sparql"
     if v8_ok else f"targetNode={n_targetnode}, targetClass={n_targetclass}/{len(declared)}, sparql={n_sparql}")

# --- gate-ladder self-check: the V0-V8 gate/clause SPEC records exist with UNIQUE identifiers ----
gate_specs   = sorted(set(base.subjects(RDF.type, GATE_SPEC)), key=str)
clause_specs = sorted(set(base.subjects(RDF.type, CLAUSE_SPEC)), key=str)
gate_ids     = [str(o) for g in gate_specs   for o in base.objects(g, GATE_ID)]
clause_ids   = [str(o) for c in clause_specs for o in base.objects(c, CLAUSE_ID)]
ladder_ok = (len(gate_specs) >= 9 and len(clause_specs) >= 9
             and len(gate_ids) == len(set(gate_ids)) == len(gate_specs)
             and len(clause_ids) == len(set(clause_ids)) == len(clause_specs))
gate("GATE-LADDER", ladder_ok,
     f"{len(gate_specs)} gate specs + {len(clause_specs)} clause specs on the core:entity ladder; "
     f"gate/clause identifiers unique (reference uniqueness teeth GateIdentityShape/ClauseIdentityShape)"
     if ladder_ok else
     f"gates={len(gate_specs)} clauses={len(clause_specs)} "
     f"gate_ids={len(gate_ids)}/{len(set(gate_ids))} clause_ids={len(clause_ids)}/{len(set(clause_ids))}")

sys.exit(1 if problems else 0)
PY

# ---- (e) depth gate over the folded algebra classes (design §4 / run-foundation-checks.sh:143) ---
echo "== depth gate (every owl:Class under ${ALG} >= 200-char rdfs:comment) =="
python3 scripts/ontology-depth-check.py "${ALG}"

echo "ALGEBRA CHECKS GREEN"
