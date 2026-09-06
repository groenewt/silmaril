# Stage 2 — T-RETIRE outcome record (SP0 primordial spine-fold, W2)

## VERDICT: **BLOCKED as a spine-only op** — resolved by maintainer decision to FOLD THE WHOLE ALGEBRA FLOOR, THEN demolish.

> **MAINTAINER DECISION (post-analysis):** because the fnd: algebra floor is structurally inseparable
> (§6), a green demolition requires folding the ENTIRE fnd: algebra+spaces floor into the new tower in
> the same effort. The maintainer chose exactly that: **fold the whole floor now (rings/fields/modules/
> vector-spaces + spaces into the new B4 tower), then demolish the fnd: algebra floor green, then seal v1
> (T-INTEGRATION + T-PANEL).** Executed as Stage 3a (two-operation fold) -> 3b (spaces fold) -> 3c
> (whole-floor demolition + merged-validation wiring) -> 3d (integration + panel). This record's
> BLOCKED status refers only to the abandoned spine-only demolition; the whole-floor path supersedes it.

## VERDICT (spine-only attempt): **BLOCKED** — the full demolition was NOT realized this pass; the tree is left at the additive-green baseline (byte-clean vs HEAD).

Definitive-pass record for **T-RETIRE** — the retire of the `fnd:` one-operation algebra
spine (`basicttl/foundation/algebra_spine.ttl` rung classes → thin stubs +
`foundation.shapes.ttl` spine teeth removed + `reanchor.ttl` edges redirected), with the merged
SP0+SP0ALG+SP1+SP2+SP3 graph required to stay green.

**Praeriehund honesty (absolute):** every conforms/exit figure below was produced by actually
running the validation in this sandbox and observing the terminal line — none is asserted from
memory or carried over from a prior report. The demolition was **not** written to the tree,
because an independently-reproduced cascade drives the canonical **HARD GATE** (`foundation.shapes.ttl`
over the merged graph) **RED** within the declared Pass-1 write scope. Rather than leave a RED
merged graph or fake green, the tree is left in the additive-green state (identical to committed
HEAD `10cc8844`), and this record documents the blocker with fresh evidence.

- Working tree: `git status --porcelain` empty → every file byte-identical to HEAD. SP1/SP2/SP3,
  the fan-out foundation files, and the new tower rung atoms are all untouched.
- Files written by this pass: **none** under `basicttl/` (only this ledger record).

---

## 1. What a correct demolition requires (the target deliverable)

DEMOLISH (spine only): stub the 9 rung classes `fnd:{AlgebraicStructure, Magma, Semigroup,
Monoid, CommutativeMonoid, Group, AbelianGroup, Quasigroup, Loop}` to
`owl:Class + owl:deprecated true + owl:equivalentClass <new model-record> + skos:exactMatch <new
denotatum> + ≥200-char comment` (strip `hasSignature`/`hasEquationSet`/`hasCarrier`/`addsLaw`/
`satisfiesLaw` + the `fnd:PresentedAlgebra` typing + all spine witnesses); remove the 13 spine
teeth from `foundation.shapes.ttl` (PresentedAlgebra/SetCarrier/MagmaClosure/SemigroupAssoc/
MonoidIdentity/CommMonoidComm/GroupInverse/AbelianComm/QuasigroupDivision/LoopIdentity/
AlgebraProgenitor/MonoidIsEndo/QuasigroupTotality + the SealedGroupIsGroup spine branch);
redirect the spine re-anchor edges in `reanchor.ttl` (re-home `aob:SealedGroup` onto the new
group model-record; redirect `prim:ByteVector fnd:groundsInAlgebra fnd:Monoid`).

PRESERVE (un-folded fan-out): `algebra_rings.ttl` / `spaces.ttl` / `logic.ttl` /
`functionality.ttl` / `combinators.ttl` / `set_theory.ttl` and ALL their `foundation.shapes`
teeth (Ring/Field/Module/VectorSpace/Metric/Topology/Functionality/Combinator/Logic…), which
reference the spine class IRIs that survive as stubs.

On the current (additive/HEAD) tree TODO-11 is **not yet** satisfied: `fnd:Magma…fnd:Loop` each
still assert `fnd:hasSignature`/`hasEquationSet`/`hasCarrier`/`addsLaw`/`satisfiesLaw` and are
typed `fnd:PresentedAlgebra` (`algebra_spine.ttl:418–525`) — i.e. the algebra math content is
duplicated across the `fnd:` spine AND the new tower. The retire exists precisely to collapse
that to one place; it is the retire that is blocked.

---

## 2. The blocker — a genuine cascade onto the HARD GATE (independently reproduced)

The HARD GATE (design §5.2; `run-foundation-checks.sh` steps 2–4) validates the merged graph
against `foundation.shapes.ttl`. That shapes graph contains **`fnd:ReanchorAdditiveShape`**
(`foundation.shapes.ttl:1706`) — a PRESERVED fan-out re-anchor tooth (it targets the subjects of
`fnd:groundsInAlgebra`: `prim:ByteVector`, `prim:Integer`, `prim:Rational`, `prim:Real`), **not**
a spine tooth. Its constraint fires RED when a `fnd:groundsInAlgebra` edge lands on a target
carrying **no raw `fnd:hasSignature`**:

```
SELECT $this WHERE {
  $this <urn:silmaril:fnd:#groundsInAlgebra> ?alg .
  FILTER NOT EXISTS { ?alg <urn:silmaril:fnd:#hasSignature> ?sig }
}
```

`reanchor.ttl:147` grounds `prim:ByteVector fnd:groundsInAlgebra fnd:Monoid`. Demolishing
`fnd:Monoid` strips its `fnd:hasSignature` (stub recipe + TODO-11 "stubs assert none"), so the
tooth bites. The new tower's monoid records carry **`rel:signature`**, not `fnd:hasSignature`
(verified: `spine/monoid.ttl:70`), and `fnd:hasSignature owl:equivalentProperty relation:signature`
(`bridges.ttl:281`) does **not** propagate under `pyshacl inference='rdfs'`.

### 2.1 Empirical proof (focused `fnd:ReanchorAdditiveShape` test over the real 17,141-triple merged graph)

| scenario | edge / stub state | conforms | note |
|---|---|---|---|
| S0 baseline | `ByteVector→fnd:Monoid`, `fnd:Monoid` has `fnd:hasSignature` | **True (GREEN)** | current HEAD state |
| S1 | stub `fnd:Monoid` (strip `hasSignature`), keep edge | **False (RED)** | the cascade — focus node `prim:ByteVector` |
| S2 | stub + redirect `ByteVector` → new monoid **theory record** (`rel:signature`) | **False (RED)** | `owl:equivalentProperty` bridge invisible under rdfs |
| S3 | stub + redirect `ByteVector` → new monoid **denotatum** | **False (RED)** | same |
| S4 | stub + redirect `ByteVector` → `fnd:Ring` (fan-out, keeps `hasSignature`) | True (GREEN) | **semantically WRONG** (ByteVector is a free monoid, not a ring) |
| S5 | stub + **drop** the `ByteVector` grounding edge | True (GREEN) | **removes a prior triple** (additive doctrine) + fails runner ASK `q_reanchor_additive` |
| S6 | stub + redirect + re-inject raw `fnd:hasSignature` on new denotatum | True (GREEN) | **violates TODO-11** (re-duplicates `fnd:` math content) |

Exact S1 violation (pyshacl report):

```
Constraint Violation in SPARQLConstraintComponent
  Source Shape: fnd:ReanchorAdditiveShape
  Focus Node:  prim:ByteVector
  Message: additive re-anchor: fnd:groundsInAlgebra target carries no fnd:hasSignature.
```

### 2.2 Why this is out of Pass-1 scope

The clean, correct fix is: redirect `ByteVector` onto the new tower's monoid record **and** make
`fnd:ReanchorAdditiveShape` new-tower-aware (read `rel:signature`, or the `owl:equivalentClass`/
`owl:equivalentProperty` bridge). But `fnd:ReanchorAdditiveShape` is a PRESERVED **fan-out
re-anchor tooth** — it also protects the surviving `Integer→fnd:Ring`, `Rational/Real→fnd:Field`
edges, so it cannot be deleted, and rewriting its logic to be new-tower-aware is exactly the
**Pass-2 fan-out reanchor work** the task defers. Every green option inside the declared write
scope (`algebra_spine.ttl`, `foundation.shapes.ttl` spine teeth, `reanchor.ttl`,
`bridges.ttl`-for-SealedGroup) is doctrine-violating (S4 wrong / S5 removes a prior triple /
S6 breaks TODO-11). This is precisely the task's stated STOP trigger: *"If a fan-out shape breaks
ONLY because a spine content it read is gone → STOP and report it (do not delete fan-out teeth)."*

A secondary coverage gap compounds it: the "re-home SealedGroup so its group-hood is covered by
the NEW GroupInverseShape/ModelShape" clause cannot be satisfied **within the HARD GATE**, because
the new tower's `algebra.shapes.ttl` is never validated over the merged SP0+…+SP3 graph (the HARD
GATE validates only foundation/primitives/crs/aob shapes; `*.shapes.ttl` never enters the data
graph). Removing the spine `SealedGroupIsGroupShape`/`GroupInverseShape`/`MonoidIdentityShape`
teeth therefore leaves `aob:SealedGroup` un-toothed in the merged graph unless a new-tower-aware
group tooth is added to `aob.shapes.ttl`/`foundation.shapes.ttl` **or** `algebra.shapes.ttl` is
added to the merged validation set — again outside the declared write scope.

Both cascades require an in-lockstep scope expansion (per D25 CI-lockstep) touching the fan-out
re-anchor tooth (and, for the runner, `foundation.queries.sparql` ASKs + `README.md`/
`dag_instances.ttl` count self-checks) — i.e. a maintainer-approved decision this pass does not
hold.

---

## 3. Merged-graph green evidence (the ADDITIVE-BASELINE state actually left in the tree)

This is the state of the tree (= committed HEAD `10cc8844`, byte-clean). It is the honest
fallback: green, not half-demolished/RED. All lines observed live this pass.

**HARD GATE — merged SP0(9) + SP0ALG(20) + SP1(4) + SP2(7) + SP3(5) → 17,141 triples,
`inference='rdfs'` (built exactly as `run-foundation-checks.sh` builds it):**

```
[547.6s] SHACL conforms (foundation.shapes.ttl over merged): True
[ 13.1s] SHACL conforms (primitives.shapes.ttl over merged): True
[  4.7s] SHACL conforms (crs.shapes.ttl over merged): True
[198.3s] SHACL conforms (aob.shapes.ttl over merged): True
=== [BASELINE] ALL 4 CONFORM=TRUE (GREEN) ===
```

**`run-algebra-checks.sh` (the new tower, unaffected by the retire):**

```
V0 GREEN (74 files) · V1 · V2 · V3 · V5 · V6 · V7 · V8 GREEN  (V4 Yoneda = documented Pass-2 deferral)
disk==manifest==DAG across all surfaces (27 data ttl → 1778 triples · 23 NodeShapes · 46 fixtures)
ONTOLOGY DEPTH CHECK PASSED — Files checked: 74
ALGEBRA CHECKS GREEN
ALG_EXIT=0
```

**`run-crs-checks.sh` (the SP1+SP2+SP3 invariant):**

```
FLOOR CHECKS GREEN (SP1 standalone; 21 ASKs)
AOB CHECKS GREEN (SP2 standalone; SHACL conforms True; 13 ASKs)
SHACL conforms (crs.shapes.ttl over merged): True
SHACL conforms (primitives.shapes.ttl over merged): True
CRS CHECKS GREEN
CRS_EXIT=0
```

> Environmental note (not demolition-caused): the FULL `run-foundation-checks.sh` cannot reach its
> terminal `FOUNDATION CHECKS GREEN` line in this sandbox regardless of the retire, because step 6
> (the citation gate) resolves ~113 `helios/srcy/**/*.tex` files that are gitignored
> (`.gitignore:62-63`) and absent from this checkout. The HARD GATE isolates the merged-graph SHACL
> validation (steps 2–4) from that gate by design, and it is the merged-graph SHACL result above
> that is the "merged graph is green" claim.

---

## 4. Item-by-item against the T-RETIRE checklist

1. **What was demolished:** nothing — the demolition was not written to the tree (a completed
   demolition drives the HARD GATE RED, §2). The target would have been: 9 rung classes → stubs,
   spine witnesses stripped, 13 spine teeth removed, `reanchor.ttl` edges redirected.
2. **Merged green evidence:** §3 — all four shape sets `conforms=True` over the 17,141-triple
   merged graph, on the additive-baseline state left in the tree.
3. **SealedGroup re-home:** NOT performed. `aob:SealedGroup rdfs:subClassOf fnd:Group`
   (`reanchor.ttl:163`) is intact. Re-home cannot be toothed within the HARD GATE (§2.2).
4. **Fan-out preserved:** YES (trivially — untouched). Files referencing spine classes
   (`algebra_rings.ttl`, `spaces.ttl`, `reanchor.ttl`, `foundation.shapes.ttl`) all resolve.
5. **TODO-11 satisfied:** NO. `fnd:Magma…fnd:Loop` still assert full math content
   (`algebra_spine.ttl:418–525`); the retire that would collapse it to one place is blocked.
6. **Residual issue / blocker:** the `prim:ByteVector → fnd:Monoid` / `fnd:ReanchorAdditiveShape`
   cascade (§2) plus the SealedGroup-re-tooth coverage gap (§2.2). Resolving either within a green
   HARD GATE requires editing the PRESERVED fan-out re-anchor tooth (Pass-2 fan-out reanchor work)
   and/or adding the new tower's group shapes to the merged validation — a maintainer-approved
   D25-lockstep scope expansion beyond the declared Pass-1 write scope.

---

## 6. Structural conclusion — the fnd: algebra floor is INSEPARABLE (why v1 AND v2 blocked, and why v3 would too)

Inspecting `foundation.shapes.ttl` shows the block is not a stray reanchor edge but the floor's
topology: the one-operation SPINE and the two-operation FAN-OUT (Ring/Field/Module/VectorSpace/
Semiring) are a single tightly-woven whole, so the spine cannot be demolished green in isolation.

- **Class-general teeth span BOTH.** `fnd:MintingEngineShape` targets **every** `fnd:PresentedAlgebra`
  (spine rungs AND fan-out rungs) and requires each to carry `fnd:hasSignature`/`hasEquationSet`/
  `hasCarrier`/`mintedVia`; stubbing the spine rungs (which strips exactly those) reddens it.
  `fnd:AlgebraProgenitorShape` quantifies over **every** rung's `fnd:addsLaw` (one-law-per-child) —
  the stubs carry none. `fnd:ReanchorAdditiveShape` protects `ByteVector→Monoid` AND `Integer→Ring`,
  `Rational/Real→Field` in one tooth.
- **Fan-out is DEFINED on the spine.** A `fnd:Ring` is an additive `fnd:AbelianGroup` + a
  multiplicative `fnd:Monoid` + distributivity; `algebra_rings.ttl`/`spaces.ttl` reference the spine
  classes structurally, and the ring/field teeth reuse the spine's genuine-inverse / associativity
  discipline. Retiring the spine's *content* (not just its name) removes what the fan-out is built on.
- **The new shapes never see the merged graph.** `algebra.shapes.ttl` is validated only by
  `run-algebra-checks.sh` over the algebra subtree; the HARD GATE validates the merged graph against
  `foundation/primitives/crs/aob` shapes only. So demolishing the foundation spine teeth leaves the
  merged graph's algebra content (SealedGroup, the fan-out rungs) un-toothed unless the new shapes are
  wired into the merged validation AND the fan-out witnesses are migrated into the new idiom.

**Therefore a green TRUE FULL DEMOLITION of the spine entails folding the ENTIRE fnd: algebra floor —
rings, fields, modules, vector-spaces, spaces — into the new tower in the SAME pass** (so the
class-general teeth + the fan-out definitions move with it), which is the whole of Pass-2's algebra
fan-out, explicitly deferred by design §6. There is no green-preserving way to demolish only the
one-operation spine. The green-preserving forms of "retire" are: (a) DEPRECATION-BRIDGE (mark the
fnd: spine `owl:deprecated` + `owl:equivalentClass` → new IRIs; keep witnesses/teeth so the floor
stays green; the new tower is the authoritative source of truth; physical deletion follows the Pass-2
fan-out fold), or (b) SHIP the additive-green v1 now and make the full demolition its own Pass-2
project. Escalated to the maintainer.

## 5. Reproduction

- HARD GATE: `python3 <scratchpad>/hardgate.py BASELINE` (merges SP0+SP0ALG+SP1+SP2+SP3 exactly as
  `run-foundation-checks.sh`; validates the four shape sets, `inference='rdfs'`).
- Cascade: `python3 <scratchpad>/cascade_test.py` (S0–S6 over the real merged graph, focused on
  `fnd:ReanchorAdditiveShape`).
- Runners: `bash basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` (ALG_EXIT=0),
  `bash basicttl/crs/checks/run-crs-checks.sh` (CRS_EXIT=0).
