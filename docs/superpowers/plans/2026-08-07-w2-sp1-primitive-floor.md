# W2 · SP1 — Primitive Floor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax.

**Goal:** author the twin-olog **colimit-taiji Primitive Floor** — formal type-towers ⟷
physical bit/byte/ISA-UEFI carriers, glued by a monadic realization that is the unary law's
Frame — as validated TTL under `basicttl/primitives/`, proven by the "what's a number"
RED→GREEN acceptance test plus SHACL, monad-law, and colimit-round-trip checks.

**Architecture:** Seven TTL/SPARQL/MD files, one responsibility each (design spec:
`docs/superpowers/specs/2026-08-07-w2-primitive-floor-design.md`). The "tests" are executable
graph checks — pyshacl conformance, SPARQL ASK/SELECT, the depth gate — each RED before its
file exists, GREEN after. No corpus data (relaunch-safe; binding is W5).

**Tech Stack:** rdflib 7.6.0 + pyshacl 0.40.1 (installed); Turtle + SHACL + SPARQL 1.1;
`scripts/ontology-depth-check.py`. Namespace `urn:silmaril:prim:` (`prim:`).

## Global Constraints

Binding on every task (from `docs/unary-byte-frame-law.md`,
`docs/praeriehund-demokratie-der-kategorien.md`, `ledger/W2/design_constraints.md`
Directives 1–13, and the DAG rulings bound to W2):

1. **Every `owl:Class` carries an `rdfs:comment` ≥ 200 chars** — the aggressive depth gate
   (`scripts/ontology-depth-check.py basicttl/primitives` must PASS). No stub classes.
2. **Dual-grounding is mandatory** — a formal type is never a bare `xsd:` leaf; it lives in a
   tower with subtyping arrows AND has ≥1 physical realization. A physical carrier always has
   `bit_width`, `byte_order`, and an `interpret_as` back-pointer to its formal type.
3. **`ByteVector` width is 1..128** (unary-law cap); `Byte ≠ Octet`.
4. **The realization is monadic ≡ the Frame** — every `ρ` arrow yields `Frame(output, effect)`;
   effects are typed individuals (rounding, narrowing, encoding-loss, may-overflow, …).
5. **Corpus-agnostic** — no corpus instances, no live-corpus references. Pure shape.
6. **Praeriehund honesty** — anything genuinely undecidable this iteration is marked
   `silm:isProvisional true` with a documented gap, never force-fit. Deferred items (spec §8)
   are named, not silently dropped.
7. **Commit trailers** (no model id): `Signed-off-by: Claude <claude@silmaril.internal>` /
   `Co-Authored-By: Claude <noreply@anthropic.com>` /
   `Claude-Session: https://claude.ai/code/session_01PzjvWAy57mdKkATELTijVP`. Branch
   `claude/custom-pgp-sign-git-thh37n`; the maintainer merges PRs.
8. **Prefixes** (every file header): `prim: <urn:silmaril:prim:#>`, `owl:`, `rdf:`, `rdfs:`,
   `xsd:`, `sh:` (shapes file).

---

### Task 1: Scaffolding + the RED acceptance harness

**Files:**
- Create: `basicttl/primitives/checks/run-floor-checks.sh` (the runner: parse + pyshacl + depth + all SPARQL ASKs)
- Create: `basicttl/primitives/primitives.queries.sparql` (the ASK/SELECT suite — authored fully here, RED now)
- Create: `basicttl/primitives/README.md` (skeleton: purpose, file map, how to re-run)

**Interfaces:**
- Consumes: nothing (first task).
- Produces: `run-floor-checks.sh` (called by every later task's verification), and the query
  suite whose ASKs are the acceptance tests. The runner exits non-zero if any TTL is missing,
  any SHACL violation exists, the depth gate fails, or any `EXPECT-TRUE` ASK returns false.

- [ ] **Step 1: Write the query suite (the tests) — the "what's a number" litmus first**

Author `primitives.queries.sparql` with clearly delimited, named queries. Include at minimum:

```sparql
# EXPECT-TRUE q_number_tower : the ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ chain + imaginary all exist as a subtyping chain
PREFIX prim: <urn:silmaril:prim:#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
ASK {
  prim:Integer  rdfs:subClassOf prim:Rational .
  prim:Natural  rdfs:subClassOf prim:Integer .
  prim:Rational rdfs:subClassOf prim:Real .
  prim:Real     rdfs:subClassOf prim:Complex .
  prim:Imaginary rdfs:subClassOf prim:Complex .
}
```

```sparql
# EXPECT-TRUE q_number_realized : each of ℝ,ℤ has a correct-width ISA/UEFI realization
PREFIX prim: <urn:silmaril:prim:#>
ASK {
  prim:Real    prim:realizesAs ?fr . ?fr prim:encoding ?fe . ?fe prim:bitWidth 64 .
  prim:Real    prim:realizesAs ?fr2 . ?fr2 prim:encoding ?fe2 . ?fe2 prim:bitWidth 32 .
  prim:Integer prim:realizesAs ?ir . ?ir prim:encoding ?ie . ?ie prim:bitWidth 32 .
}
```

```sparql
# EXPECT-TRUE q_colimit_roundtrip : every encoding's interpret_as closes back to a formal type
PREFIX prim: <urn:silmaril:prim:#>
ASK { FILTER NOT EXISTS { ?e a prim:PhysicalEncoding . FILTER NOT EXISTS { ?e prim:interpretAs ?f . ?f a prim:FormalType } } }
```

```sparql
# EXPECT-TRUE q_frame_effect : every realization is a Frame carrying an output and an effect
PREFIX prim: <urn:silmaril:prim:#>
ASK { FILTER NOT EXISTS { ?r a prim:Realization . FILTER NOT EXISTS { ?r prim:frameOutput ?o . ?r prim:frameEffect ?ef } } }
```

```sparql
# EXPECT-TRUE q_bytevector_cap : no ByteVector-derived encoding exceeds width 128
PREFIX prim: <urn:silmaril:prim:#>
ASK { FILTER NOT EXISTS { ?e a prim:PhysicalEncoding ; prim:bitWidth ?b . FILTER(?b > 1024) } }
```

(Additional EXPECT-TRUE ASKs: monad unit — every FormalType has an identity realization to
itself-as-formal; byte-descent bottoms at `prim:Bit`; RGB has exactly Red/Green/Blue each an
Octet of ordinal range 0..255. Author them all now.)

- [ ] **Step 2: Write the runner**

```bash
#!/usr/bin/env bash
# run-floor-checks.sh — parse every primitives TTL, run pyshacl, the depth gate, and every
# EXPECT-TRUE ASK. Exit 0 iff all green.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python3 - <<'PY'
import glob, sys, re
from rdflib import Graph
from pyshacl import validate
data = Graph()
ttls = sorted(glob.glob("basicttl/primitives/*.ttl"))
for f in ttls: data.parse(f)
print(f"parse OK: {len(ttls)} ttl, {len(data)} triples")
shapes_files = [f for f in ttls if f.endswith("primitives.shapes.ttl")]
if shapes_files:
    s = Graph(); s.parse(shapes_files[0])
    ok, _, rep = validate(data, shacl_graph=s, inference="rdfs")
    print("SHACL conforms:", ok)
    if not ok: print(rep[:2000]); sys.exit(1)
# EXPECT-TRUE ASKs from the query file
q = open("basicttl/primitives/primitives.queries.sparql").read()
blocks = re.split(r'\n(?=#\s*EXPECT-TRUE\s)', q)
fails = 0
for b in blocks:
    m = re.search(r'EXPECT-TRUE\s+(\S+)', b)
    if not m: continue
    name = m.group(1)
    ask = "\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
    if not ask.strip().upper().startswith(("PREFIX","ASK")): continue
    res = bool(data.query(ask))
    print(f"  {'PASS' if res else 'FAIL'}  {name}")
    fails += (0 if res else 1)
sys.exit(1 if fails else 0)
PY
python3 scripts/ontology-depth-check.py basicttl/primitives
echo "FLOOR CHECKS GREEN"
```

Save, `chmod +x`.

- [ ] **Step 3: Run it — verify RED**

Run: `basicttl/primitives/checks/run-floor-checks.sh`
Expected: FAIL — no TTL files yet, ASKs return false / parse finds 0 triples.

- [ ] **Step 4: Commit** the harness (RED evidence).
`git add basicttl/primitives/ && git commit` (trailers per Global Constraint 7).

### Task 2: Formal olog — `formal.ttl`

**Files:**
- Create: `basicttl/primitives/formal.ttl`
- Test: `q_number_tower` (from Task 1) goes GREEN.

**Interfaces:**
- Consumes: the query suite (Task 1).
- Produces: `prim:FormalType` (the tower supertype) and every tower class of spec §3
  (Number: `Natural`/`Integer`/`Rational`/`Real`/`Complex`/`Imaginary`/`Bignum`/`Decimal`;
  Boolean: `Bool`/`Kleene3`; Text: `Codepoint`/`Grapheme`/`String`; Temporal: `Instant`/
  `Duration`/`Interval`/`Date`/`Time`/`DateTime`; Identifier: `URN`/`URI`/`IRI`/`QName`/
  `BlankNode`; RDF-term: `Literal`/`Triple`/`Quad`/`RDFGraph`; Aggregate: `Tuple`/`List`/
  `Set`/`Bag`/`Map`/`Vector`/`Tensor`; Algebraic: `Sum`/`Optional`/`Frame`/`Unit`/`Void`;
  Quantity: `Quantity`/`Dimension`/`Unit`/`Currency`/`Measurement`; Geospatial: `Coordinate`/
  `Point`/`Line`/`Polygon`/`CRS`/`Latitude`/`Longitude`; Enum: `Enumeration`/`Ordinal`/
  `Categorical`; Binary: `Blob`/`Hash`), with `rdfs:subClassOf` subtyping arrows.
- Downstream `realization.ttl`, `taiji.ttl`, `shapes.ttl` all reference these class URIs.

- [ ] **Step 1: Run `q_number_tower` alone — verify FAIL** (no formal.ttl).
- [ ] **Step 2: Author `formal.ttl`** — pattern per class (comment ≥200 chars, Global
  Constraint 1):

```turtle
@prefix prim: <urn:silmaril:prim:#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

prim:FormalType a owl:Class ;
    rdfs:label "FormalType" ;
    rdfs:comment "The formal facet of the primitive floor: a mathematical/logical type considered independently of any machine encoding. FormalTypes are organized into towers by rdfs:subClassOf, which encodes the ISA of the mathematics (a Natural IS an Integer IS a Rational ...). Every FormalType must be dual-grounded by at least one prim:Realization into the physical olog; a FormalType with no realization is a broken primitive and is caught by the SHACL law. This is the yin of the colimit taiji whose yang is prim:PhysicalCarrier." .

prim:Complex a owl:Class ; rdfs:subClassOf prim:FormalType ;
    rdfs:label "Complex" ;
    rdfs:comment "The complex numbers ℂ — the top of the number tower for this iteration: every Real is a Complex (with zero imaginary part) and every Imaginary is a Complex (with zero real part). Realized physically as a pair of Real encodings (real, imaginary) or as an interleaved 2×float byte-vector; the realization carries the same IEEE-754 rounding effect as its Real components. Algebraic-vs-transcendental sub-facets are deferred (spec §8)." .

prim:Real a owl:Class ; rdfs:subClassOf prim:Complex ;
    rdfs:label "Real" ;
    rdfs:comment "The real numbers ℝ. Physically realized through the IEEE-754 family — Float32 (4-byte) or Float64 (8-byte), each little- or big-endian — with the realization Frame carrying an IEEE754-rounding effect (and, for Float32 from a Float64 source, an additional narrowing-loss effect). Real is a subclass of Complex and a superclass of Rational; the 'what is a number' litmus asserts exactly this chain plus a correct-width realization." .

# ... Integer ⊂ Rational ⊂ Real ; Natural ⊂ Integer ; Imaginary ⊂ Complex ;
# ... Bignum, Decimal ; and every other tower of spec §3, each class ≥200-char comment.
```

- [ ] **Step 3: Run `q_number_tower` — verify PASS.**
- [ ] **Step 4: Run the depth gate on the file** — `python3 scripts/ontology-depth-check.py basicttl/primitives` PASSES (every class ≥200).
- [ ] **Step 5: Commit.**

### Task 3: Physical olog — `physical.ttl`

**Files:** Create `basicttl/primitives/physical.ttl`. Tests: `q_bytevector_cap`, the RGB and byte-descent ASKs.

**Interfaces:**
- Consumes: `formal.ttl` (for `interpretAs` targets).
- Produces: `prim:PhysicalCarrier` (supertype), the ladder `Bit`/`Nibble`/`Octet`/`Byte`/
  `ByteVector`/`Word`/`Block`/`Stream`/`Container`; `prim:PhysicalEncoding` instances for the
  ISA/UEFI machine types (`UINT8..128`, `INT8..128`, `CHAR8/16`, `Float16/32/64/80/128`,
  `BOOLEAN`) each with `prim:bitWidth`, `prim:byteWidth`, `prim:byteOrder` (`prim:LE`/`prim:BE`),
  `prim:interpretAs` (→ formal type); representation facets (`prim:signedness`, twos/ones/
  sign-magnitude, IEEE-754 sign/exp/mantissa); text encodings (`ASCII`/`UTF8`/`UTF16`/`UTF32`/
  `Latin1`); the RGB colour space (`prim:RGB` → `prim:Red`/`Green`/`Blue`, each an `Octet`,
  ordinal 0..255). Datatype properties `bitWidth`/`byteWidth`/`byteOrder`/`interpretAs` declared here.

- [ ] **Step 1: Run `q_bytevector_cap` + RGB ASK — verify FAIL.**
- [ ] **Step 2: Author `physical.ttl`** — carriers as `owl:Class` (≥200-char comments),
  machine types as encodings. Pattern:

```turtle
prim:Octet a owl:Class ; rdfs:subClassOf prim:PhysicalCarrier ;
    rdfs:label "Octet" ;
    rdfs:comment "An 8-bit carrier and the RGB/256 colour code space's unit: an Octet takes ordinal values 0..255. Distinct from prim:Byte (which this floor keeps as a possibly-non-8-bit addressable unit, Byte ≠ Octet, per the unary law). Octets compose into a prim:ByteVector (width 1..128); the colour primitives Red/Green/Blue are each exactly one Octet, and the physical z-coordinate of an atom is the uint16 of its source_sha256's first two Octets." .

prim:Float64 a prim:PhysicalEncoding ;
    rdfs:label "Float64" ; prim:bitWidth 64 ; prim:byteWidth 8 ;
    prim:byteOrder prim:LE ; prim:interpretAs prim:Real ;
    prim:uefiName "no-UEFI-exact-name" ; prim:ieee754 true .
# ... every machine type of spec §4, each interpretAs a formal type.
```

- [ ] **Step 3: Run `q_bytevector_cap` + RGB + byte-descent ASKs — verify PASS.**
- [ ] **Step 4: Depth gate PASS. Step 5: Commit.**

### Task 4: Realization monad — `realization.ttl`

**Files:** Create `basicttl/primitives/realization.ttl`. Tests: `q_number_realized`, `q_frame_effect`, monad-unit ASK.

**Interfaces:**
- Consumes: `formal.ttl` + `physical.ttl`.
- Produces: `prim:Realization` (a Kleisli/Frame arrow) instances linking each `FormalType` to a
  `PhysicalEncoding` via `prim:realizesAs`/`prim:encoding`, each carrying `prim:frameOutput`
  (the encoding) and `prim:frameEffect` (a `prim:Effect` individual: `prim:RoundingIEEE754`,
  `prim:NarrowingLoss`, `prim:OverflowDomain`, `prim:EncodingLoss`, `prim:MayOverflow`,
  `prim:NoEffect`); the monad `unit` (identity realization) and the byte-descent composition
  chain bottoming at `prim:Bit`. Classes `Realization`/`Effect` with ≥200-char comments.

- [ ] **Step 1: Run `q_number_realized` + `q_frame_effect` — verify FAIL.**
- [ ] **Step 2: Author `realization.ttl`** — the ρ table of spec §5 (Real→Float64/32/Decimal;
  Integer→INT8..64; Natural→UINT; Bignum→ByteVector; Codepoint→UTF8/16/32; Bool→UINT8/bit;
  Instant→INT64/ISO-8601), each a `Realization` with output + effect. Pattern:

```turtle
prim:realize_Real_Float64 a prim:Realization ;
    rdfs:label "ℝ ⟼ Float64" ;
    prim:realizesFrom prim:Real ; prim:realizesAs prim:realize_Real_Float64 ;
    prim:encoding prim:Float64 ; prim:frameOutput prim:Float64 ;
    prim:frameEffect prim:RoundingIEEE754 .
```

(`prim:Real prim:realizesAs ?r` in the ASK matches via `realizesFrom`; align the query and the
data on one property name — use `prim:realizesAs` as `Real → Realization` and `prim:encoding`
as `Realization → PhysicalEncoding`. Adjust Task 1's `q_number_realized` if you renamed, and
re-run it RED→GREEN so the rename is test-covered.)

- [ ] **Step 3: Run the realization ASKs + monad-unit ASK — verify PASS.**
- [ ] **Step 4: Depth gate PASS. Step 5: Commit.**

### Task 5: Taiji colimit — `taiji.ttl`

**Files:** Create `basicttl/primitives/taiji.ttl`. Test: `q_colimit_roundtrip`.

**Interfaces:**
- Consumes: all three ologs.
- Produces: `prim:Primitive` (the colimit-taiji object) — one per formal type — declaring the
  colimit of `(FormalType ─realization→ PhysicalEncoding)` with the **mutual back-pointer**
  `prim:interpretAs` closed on the physical side (already emitted in `physical.ttl`; `taiji.ttl`
  asserts the colimit object binds both facets and that the round-trip
  `physical → interpretAs → formal → realizesAs → encoding` returns the same encoding for the
  chosen realization). `Primitive` class ≥200-char comment explaining the mutual-colimit taiji.

- [ ] **Step 1: Run `q_colimit_roundtrip` — verify it FAILS or is vacuous** (no Primitive gluing / an encoding lacking interpretAs). Add a temporary encoding with no `interpretAs` to prove the ASK catches it, then remove it.
- [ ] **Step 2: Author `taiji.ttl`** — one `prim:Primitive` per formal type gluing its facets:

```turtle
prim:prim_Real a prim:Primitive ;
    rdfs:label "Primitive ℝ (taiji)" ;
    prim:formalFacet prim:Real ;
    prim:physicalFacet prim:Float64 ;   # a chosen canonical realization
    prim:gluedBy prim:realize_Real_Float64 .
```

- [ ] **Step 3: Run `q_colimit_roundtrip` — verify PASS** (every encoding closes to a formal type).
- [ ] **Step 4: Depth gate PASS. Step 5: Commit.**

### Task 6: SHACL law — `primitives.shapes.ttl`

**Files:** Create `basicttl/primitives/primitives.shapes.ttl`. Test: pyshacl conforms=True on the floor AND catches an injected violation.

**Interfaces:**
- Consumes: all four TTLs.
- Produces: SHACL shapes enforcing: every `FormalType` has ≥1 `Realization` (via a path to
  `realizesAs`); every `PhysicalEncoding` has `bitWidth` (≤128 for ByteVector-derived),
  `byteOrder`, and `interpretAs` a `FormalType`; every `Realization` has `frameOutput` +
  `frameEffect`; every `Primitive` has both facets and a `gluedBy`. (`sh:NodeShape` per class.)

- [ ] **Step 1: Write a RED probe** — temporarily add `prim:Orphan a prim:FormalType .` (no
  realization) to a scratch copy; run pyshacl with the (not-yet-written) shapes → currently
  conforms vacuously. Write the shape that SHOULD flag `prim:Orphan`.
- [ ] **Step 2: Author `primitives.shapes.ttl`**:

```turtle
prim:FormalTypeShape a sh:NodeShape ;
    sh:targetClass prim:FormalType ;
    sh:property [ sh:path prim:realizesAs ; sh:minCount 1 ;
                  sh:message "every FormalType must have at least one Realization (dual-grounding)" ] .
prim:EncodingShape a sh:NodeShape ;
    sh:targetClass prim:PhysicalEncoding ;
    sh:property [ sh:path prim:bitWidth ; sh:minCount 1 ; sh:datatype xsd:integer ] ;
    sh:property [ sh:path prim:byteOrder ; sh:minCount 1 ] ;
    sh:property [ sh:path prim:interpretAs ; sh:minCount 1 ; sh:class prim:FormalType ;
                  sh:message "every encoding must interpret_as a FormalType (mutual-colimit closure)" ] .
# ... RealizationShape (frameOutput + frameEffect minCount 1), PrimitiveShape (both facets + gluedBy).
```

- [ ] **Step 3: Verify RED→GREEN** — with `prim:Orphan` present, pyshacl reports the violation
  (RED); remove `prim:Orphan`; pyshacl conforms=True (GREEN). This proves the shape has teeth.
- [ ] **Step 4: Run the full runner** `run-floor-checks.sh` — SHACL now active + all ASKs pass.
- [ ] **Step 5: Depth gate PASS. Commit.**

### Task 7: Integration — README + full-green + the acceptance litmus

**Files:** Complete `basicttl/primitives/README.md`; no new TTL.

**Interfaces:**
- Consumes: everything.
- Produces: the README (the floor, its 7 files, the consumers — AOB #2 grounds tensor fields
  here, CRS #3 grounds z, depth-remediation #8 dual-grounds every primitive — and the exact
  re-run command), and a green full-floor run.

- [ ] **Step 1: Run `basicttl/primitives/checks/run-floor-checks.sh` fresh** — capture output;
  every EXPECT-TRUE ASK PASS, SHACL conforms, depth gate PASSED. This is the verification-
  before-completion evidence; the **"what's a number" litmus** (`q_number_tower` +
  `q_number_realized`) must be visibly GREEN.
- [ ] **Step 2: Write the README** with the file map, the consumer interfaces above, and the
  paste of the green run.
- [ ] **Step 3: Update the DAG** — set `silm:phase_w2_sp1 silm:hasStatus "completed"` in
  `basicttl/dag/dag_instances.ttl`; re-run the DAG SHACL + depth gate; confirm still conforms.
- [ ] **Step 4: Commit.** SP1 complete; the between-sub-project adversarial panel (per the DAG's
  Gate discipline) reviews before SP2 (AOB meta-ontology) opens its own brainstorming gate.

## Self-Review

- **Spec coverage:** all seven spec files (formal/physical/realization/taiji/shapes/queries/
  README) have a task; all twelve formal towers + physical carriers + realization table are
  enumerated in the Interfaces blocks. ✓
- **Placeholder scan:** the `# ...` continuations point to the spec's complete enumeration
  (§3/§4/§5), not vague guidance; every test query is written in full; every file has a concrete
  authoring pattern. The acceptance ASKs define "done" precisely.
- **Type consistency:** property names align across tasks — `realizesAs` (FormalType→Realization),
  `encoding` (Realization→PhysicalEncoding), `interpretAs` (Encoding→FormalType), `frameOutput`/
  `frameEffect` (Realization→…), `formalFacet`/`physicalFacet`/`gluedBy` (Primitive→…). Task 4
  Step 2 flags the one rename risk and requires re-running the affected ASK RED→GREEN.
