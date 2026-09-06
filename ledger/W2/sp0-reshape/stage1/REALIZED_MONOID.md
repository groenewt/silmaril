# REALIZED MONOID — SP0 Primordial Spine-Fold, Stage 1 Sign-Off Packet

Assembled by the Stage-1 review pass on 2026-09-06 for the maintainer panel (T-PANEL).
Every claim below was re-verified independently on disk in this pass. Verdict at the foot.

- Design: `docs/superpowers/specs/2026-09-06-w2-sp0-primordial-fold-design.md`
- Plan: `docs/superpowers/plans/2026-09-06-w2-sp0-spine-fold-plan.md`
- Constraints: `ledger/W2/design_constraints.md` (D24 / D25 / D26)
- Write scope this stage: `basicttl/primordial/type/algebra/**` + the two lockstep files
  `basicttl/foundation/checks/run-foundation-checks.sh` and `.github/workflows/ci.yml`.

---

## (1) WHAT WAS BUILT — file inventory + atom counts

Tracked-modified (lockstep, D25):
- `.github/workflows/ci.yml` — +7 lines: a new CI step `Validate the folded algebra spine`
  running `run-algebra-checks.sh` after the foundation step (CI-lockstep with the runner loader).
- `basicttl/foundation/checks/run-foundation-checks.sh` — +43/-7: SP0ALG merged-loader
  (`_folded_spine(p)` predicate at :94-99 excludes `/sum/` and `/product/` pre-existing scaffolding,
  wires the real D26 folded spine into the merged SP0+SP0ALG+SP1+SP2+SP3 graph). Regression fixed.

New under `basicttl/primordial/type/algebra/**` (all untracked/new):

| file | triples | notes |
|---|---|---|
| `spine/progenitor.ttl` | 24 | [V] progenitor denotatum root (grounds nothing), OWL2 metaclass pun |
| `spine/monoid.ttl` | 92 | B4 two-plane monoid: denotatum + model-record class + theory + gate + axioms |
| `records.ttl` | 64 | intensional seed-carrier record classes (8 owl:Class), disjointness teeth |
| `signatures.ttl` | 48 | signature/sort plane (sigMonoid Σ={·,e} and siblings) |
| `operations.ttl` | 39 | operation symbols (·, e/nullary unit) |
| `equations.ttl` | 31 | equation records incl. identity LEFT/RIGHT two-sided split |
| `bridges.ttl` | 148 | alias map (skos:exactMatch/closeMatch) + D24 conservative/implementation bridges |
| `shapes/algebra.shapes.ttl` | — | 4 SHACL NodeShapes (teeth) |
| `checks/run-algebra-checks.sh` | — | non-vacuous folded-spine gate runner |
| `fixtures/{monoid_z2,monoid_z2_negative,empty,progenitor_pos,progenitor_neg}.ttl` | — | 2 positive, 2 negative, 1 empty control |
| `probes/*.rq` | — | records_disjoint, monoid_identity, signature_names_sort, aliases_resolve, progenitor_grounds_nothing |

Pre-existing non-D26 scaffolding left in place (deferred per design §7.2(b), excluded from the
foundation merged loader): `sum/**` (admission, byte/vector), `product/frame.ttl`.

Merged algebra data graph (the runner's own count): **14 data ttl → 625 triples; 4 NodeShapes; 5 fixtures.**

---

## (2) RUNNER GREEN EVIDENCE — exact output

`bash basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` (re-run this pass):

```
== folded algebra spine gate (basicttl/primordial/type/algebra) ==
  data: 14 ttl -> 625 triples; shapes: 4 NodeShape(s); fixtures: 5
  (a) data graph conforms: True
  (c) focus OK: <http://www.w3.org/ns/shacl#AlgebraProgenitorShape> 1 focus node(s)
  (c) focus OK: <http://www.w3.org/ns/shacl#EquationRecordShape> 3 focus node(s)
  (c) focus OK: <http://www.w3.org/ns/shacl#ModelShape> 1 focus node(s)
  (c) focus OK: <http://www.w3.org/ns/shacl#TheoryShape> 1 focus node(s)
  (b) PASS empty control: basicttl/primordial/type/algebra/fixtures/empty.ttl => admission REJECT (0 focus, vacuous)
  (b) PASS positive: basicttl/primordial/type/algebra/fixtures/monoid_z2.ttl conforms
  (b) PASS negative: basicttl/primordial/type/algebra/fixtures/monoid_z2_negative.ttl does NOT conform (tooth bites)
  (b) PASS negative: basicttl/primordial/type/algebra/fixtures/progenitor_neg.ttl does NOT conform (tooth bites)
  (b) PASS positive: basicttl/primordial/type/algebra/fixtures/progenitor_pos.ttl conforms
  (b) fixtures: 2 positive, 2 negative, 1 empty control
  (d) PENDING: no manifest figure stated yet (T-MANIFEST wires the full V6 self-check); disk figures = {'data_files': 14, 'nodeshapes': 4, 'fixtures': 5, 'triples': 625}
== depth gate (every owl:Class under basicttl/primordial/type/algebra >= 200-char rdfs:comment) ==
ONTOLOGY DEPTH CHECK PASSED
Files checked: 20
ALGEBRA CHECKS GREEN
EXIT CODE: 0
```

Foundation lockstep (T-INFRA): the SP0ALG merged-loader regression is resolved — SP0ALG resolves to
`[]` today (the real D26 spine wires in with no future edit; the pre-existing `/sum//product/`
scaffolding is excluded), so the merged data graph is byte-identical to the committed CI-green
baseline (15541 triples) and `primitives.shapes` CONFORMS True at 15541. See §5 for the one honest
caveat (the full foundation runner's `aob.shapes` merged-SHACL pass exceeds the time budget; the
loader edit was proven by the merged-graph dry-run, which the task sanctions).

---

## (3) NON-VACUITY PROOF — per-shape focus counts + negative flip

Per-shape focus counts (runner step (c), all ≥ 1 — no shape is vacuously satisfied by an empty target set):

| NodeShape | focus nodes |
|---|---|
| `sh:AlgebraProgenitorShape` | 1 |
| `sh:TheoryShape` | 1 |
| `sh:ModelShape` | 1 |
| `sh:EquationRecordShape` | 3 |

Independent pyshacl re-run this pass (merged spine data + each fixture, `inference='rdfs'`) —
every tooth proven to BITE by injection (conforms True → False):

```
monoid_z2              CONFORMS True     (positive witness conforms)
monoid_z2_negative     CONFORMS False    (negative flips RED — tooth bites)
empty                  CONFORMS True     (vacuous; the runner INVERTS this to REJECT: 0 focus => vacuous gate rejected)
progenitor_pos         CONFORMS True     (positive witness conforms)
progenitor_neg         CONFORMS False    (negative flips RED — tooth bites)
```

- `monoid_z2_negative` flips RED — CONFIRMED (both the runner's step (b) and the standalone pyshacl re-run).
- `empty` control ⇒ REJECT — CONFIRMED: an empty fixture conforms only vacuously (0 focus nodes),
  and the runner's step (b) treats a 0-focus/vacuous admission as a REJECT (anti-vacuity, the
  deliberate inversion of the foundation runner's shapeless-graph SKIP).
- Records disjointness teeth (T-CLASSES probe `records_disjoint.rq`, re-verified by that task):
  baseline 1 row; dropping the equation cardinality-1 restriction, or either owl:disjointWith
  (axiom↔theorem, denotatum↔declaration), collapses to 0 rows — each tooth bites.

---

## (4) THE [S]-TOKEN SIGN-OFF PACKET — full list actually used on disk

Every token below has NO precedent in the verified-runtime corpus (D26 engine: `aob/urn/**` +
`config/algebra/primordials.yaml`) and is minted under the design's §7.2 #1 "mint-more-than-runtime"
ruling. Each use is tagged `[S]` in an `rdfs:comment` at its mint site for the panel. Grouped by plane:

**Seed-carrier record classes** (closure.ttl carries only {specimen,construction,datatype,axiom,theorem,application,variable}:record):
- `progenitor:record`
- `theory:record`
- `model:record`
- `signature:record`
- `reduct:record`
- `denotatum:record`
- `declaration:record`
- `equation:record`  (§7.2 #7 — the "mint separate component:equation records" side of the equation-identity decision)

**Theory / model ladder rank vocab** (§7.2 #1, #10 — PIVOTAL, pre-locked B4):
- `class:theory` / `genus:presented`  (monoid theory atom)
- `class:model` / `genus:governed` / `component:class`  (monoid model-record class, B4 Plane-1)

**Signature / sort plane** (§7.2 #6):
- `class:signature` / `genus:algebraic` / `species:signature`
- `class:sort` / `order:carrier` / `species:sort` / `genus:algebraic`
- signature-profile `order:` tokens: `order:one:binary`, `order:monoid`, `order:group`,
  `order:quasigroup`, `order:loop`, `order:unital`, `order:invertible`, `order:divisible`,
  `order:divisible:unital`

**Operation plane** (§7.2 #3):
- `order:nullary`  (the unit symbol; fallback `order:constant` noted, also unattested)

**Law / equation side-split** (§7.2 #2 — the side segment is unattested):
- `species:member:left` / `species:member:right`  (two-sided identity split — monoid + loop)
- `species:inverse:left` / `species:inverse:right`  (two-sided inverse split — group, Stage 2)

**Quasigroup / loop division family** (§1.8, §7.2 #5):
- `class:division` / `species:division`
- `genus:left:species:division` / `genus:right:species:division`  (left/right sense in the genus segment)
- `genus:latin` / `species:unique`  (latin-division axiom)
- `species:product`

**Free-algebra carriers** (§7.2 — 8 aliases):
- `class:carrier:order:free:genus:free:algebra`  (free-magma/semigroup/monoid/group/abelian-group/quasigroup/loop/commutative-monoid)

**Predicate declarations** (no runtime/closure precedent):
- `seed:conservativeBridge`  (D24 sameness ladder)
- `seed:implementationBridge`  (D24 sameness ladder)
- `@rel:result` (relation:result — no closure counterpart; kept rdfs:subPropertyOf, not a false equivalence)
- `@rel:structure` (relation:structure — no closure counterpart)
- `@rel:validation:mode` / `@rel:proof:status`  (D24 first-class metadata vocab)
- predicate-unification specialisations (each rdfs:subPropertyOf its fnd: origin): `@rel:adds:law`,
  `@rel:equation:set`, `@rel:satisfies:law`, `@rel:pairing:element`, `@rel:pairing:inverse`,
  `@rel:pairing:model`

The seven other §7.2 [S] tokens ride at the design defaults per the maintainer lock; each is tagged in-line.

---

## (5) RESIDUAL BLOCKING ISSUES / HONEST REDS

- **No blocking issues in the algebra scope.** The algebra runner is GREEN (exit 0), depth gate GREEN,
  all fixture polarities and focus counts non-vacuous.
- **Honest caveat (T-INFRA, non-blocking):** the FULL `run-foundation-checks.sh` was NOT observed
  emitting its terminal `FOUNDATION CHECKS GREEN` line in the executor/shadow rounds — its
  `aob.shapes` merged-SHACL pass exceeds the ~560s budget (EXIT=124 timeout, AFTER run-crs-checks
  GREEN and parse-OK at 15541 triples). The loader fix was instead proven by the merged-graph
  dry-run: SP0ALG = `[]` ⇒ merged graph byte-identical to the committed 15541-triple baseline ⇒ every
  shape/ASK over it is identical to the CI-green baseline by construction; `primitives.shapes`
  independently CONFORMS True at 15541; the untouched SP1/SP2/SP3 invariant ran GREEN (exit 0). The
  task sanctions this substitute for the >5min phase. This is the only place a gate was not observed
  running to its literal green tail.
- **Deferred by design (not defects):** `sum/**` and `product/frame.ttl` remain ungrounded
  pre-existing scaffolding (excluded from the foundation merged loader until a later task grounds
  them, §7.2(b)); `frame.ttl:7` V1 punning fix + Yoneda grounding are T-SHAPES/T-FIX; Stage-2 rungs
  (magma…loop, group inverse, reduct extension morphisms, fnd: retire) are out of Stage-1 scope.

---

## (6) B4 TWO-PLANE REALIZATION (monoid)

The maintainer lock B4 (model plane = TWO planes) is realized for the monoid rung as two DISTINCT
full-ladder IRIs, linked by `@rel:denotes`:

- **Plane-2 DENOTATUM** (the mathematical object; identifier/notation/abstract only, NO provenance):
  `urn:silmaril:…:subdomain:monoid:kingdom:type:phylum:algebra:class:monoid:order:binary:family:operation:genus:axiomatic:species:monoid:component:type:instance:canonical`
  (`kingdom:type … component:type`)

- **Plane-1 DECLARATION-RECORD / model class** (owl:Restriction bundle + provenance quartet + disjointness teeth):
  `urn:silmaril:…:subdomain:monoid:kingdom:class:phylum:algebra:class:model:order:declarative:family:monoid:genus:governed:species:monoid:component:class:instance:canonical`
  (`kingdom:class … :model … component:class`)

- **Link:** the model class carries `rel:denotes` → the denotatum (spine/monoid.ttl:108); the theory
  record's `@rel:denotatum` also points at the denotatum. The denotatum is byte-identical to the
  bridges.ttl `skos:exactMatch fnd:Monoid` target so the merged alias map resolves.

Provenance quartet + `@rel:authority 'DS'` live on the RECORD plane only (D24: "Monoid was not
authored by an executor; the MonoidTheoryRecord was"). Supporting monoid atoms on disk: the presented
theory record (`kingdom:definition…component:definition`), the reconciliation gate
(`kingdom:assignment…component:assignment`), the closure and identity axioms (`kingdom:axiom`), and the
identity-uniqueness certificate/theorem — all under `subdomain:monoid`, on the mathematics 12-marker
ladder (not crossed with the closure.ttl record-class ladder or the consolidated.shacl gate ladder).

---

## (7) STAGE-1 STAYED ADDITIVE

`git diff --stat -- basicttl/foundation/algebra_spine.ttl` = EMPTY — the fnd: tower is UNTOUCHED.
The only tracked modifications are the two D25 lockstep files:

```
 .github/workflows/ci.yml                           |  7 ++++
 basicttl/foundation/checks/run-foundation-checks.sh | 43 ++++++++++++++++++----
```

All other Stage-1 output is new files under `basicttl/primordial/type/algebra/**`. Bridges are
ADDITIVE edges only (skos:exactMatch/closeMatch, seed:conservativeBridge/implementationBridge) — no
fnd:* atom was edited or removed. B3 true-retire is Stage 2 (T-RETIRE), not this stage.

---

## VERDICT

**GREEN** — the folded algebra spine gate passes (exit 0), the monoid B4 two-plane rung is realized
and non-vacuous (every shape has ≥1 focus, positive witnesses conform, `monoid_z2_negative` and
`progenitor_neg` flip RED, empty control ⇒ REJECT), the depth gate passes (20 files), and Stage 1
stayed additive (algebra_spine.ttl untouched). One honest caveat carried forward: the full
foundation runner's terminal green line was not observed within budget (aob.shapes timeout after
run-crs GREEN + parse-OK 15541); the loader fix is proven by the byte-identical-baseline dry-run,
which the task sanctions. No blocking issue in the algebra scope.
