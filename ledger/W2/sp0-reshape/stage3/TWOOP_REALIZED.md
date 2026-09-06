# TWOOP_REALIZED — Stage 3a two-operation algebra floor, consolidation record

**Stage:** W2 · SP0 primordial spine-fold · Stage 3a (two-operation floor: Semiring / Ring / Field /
Module / VectorSpace folded into the B4 tower, REDUCTing onto the committed one-operation tower).
**Consolidation session:** independent FINAL pass — run the full runner, verify shapes / negatives /
reducts / additivity, close the two residual gates (V6 manifest re-derive + V7 provenance lane), write
this record.
**Verdict:** **GREEN** — `bash basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` exits 0,
non-vacuous, all gates V0–V8 green (V4 the design-§6 deferral), depth PASSED.

---

## 0. What the consolidation did (honesty first)

The five rung executors (T-RING + semiring/field/module/vector_space siblings) landed all rung atoms
GREEN in isolation, but the FULL merged runner was **RED (exit 1)** on two gates when this pass began:

- **V6 (manifest coverage):** `manifests/spine.yaml` still held the T-2OP-INFRA infra-only checkpoint
  (THEORIES 8, AXIOMS 24, RUNGS 8, SHAPES 23, …) and the `phase_w2_sp0_fold` DAG node
  (`basicttl/dag/dag_instances.ttl`) still stated the pre-fold narrative figures (8 rungs / 23 shapes /
  17 probes / 46 fixtures). T-2OP-INFRA explicitly flagged this re-derive as the consolidation's job.
- **V7 (dual executor/shadow provenance closure):** the 28 new two-operation reshaped records (each
  bearing `@rel:authority "SYN"`) had NO `prov:wasAttributedTo` executor/shadow + `prov:wasGeneratedBy`
  edges. The rung executors minted the D24 provenance QUARTET but omitted the V7 lane. The 29 committed
  one-operation records already carry it via `reviews/{executor,shadow,resolved}/`.

The consolidation closed both **additively and truthfully**:

1. Re-derived `manifests/spine.yaml` COUNT block + the DAG node's 4 gated figures **and** its record-surface
   prose to the fresh on-disk truth (§2).
2. Authored **one new additive file** `reviews/resolved/resolution_lane_twoop.ttl` that stamps the 28
   two-op records with the committed scope-marker class + Draft activity + generic `sp0:spine:fold`
   executor/shadow agents (reused by IRI — bridge-never-duplicate). This is faithful replication of the
   committed one-op lane, not fabricated attribution: each two-op rung genuinely ran as an operator-loop
   executor exec WITH a tandem shadow verdict, and each record was drafted by the SP0 spine-fold.
   See §6 residual note.

No `basicttl/foundation/*` / `fnd:` edit. No committed one-op rung atom edited. No committed
`shapes/algebra.shapes.ttl` edit. No git actions.

---

## 1. Per-rung file inventory + atom counts

Each two-operation rung ships the same per-rung file set (design §6 fan-out, per-rung files avoid a
shared-file write race):

| Rung | spine | shape (1 NodeShape) | probe | fixtures | reduct file |
|---|---|---|---|---|---|
| semiring | `spine/semiring.ttl` | `shapes/semiring.shapes.ttl` → `SemiringDistributivityShape` | `probes/semiring_law.rq` | `fixtures/semiring_{pos,neg}.ttl` | `reducts_twoop_semiring.ttl` |
| ring | `spine/ring.ttl` | `shapes/ring.shapes.ttl` → `RingDistributivityShape` | `probes/ring_distributivity.rq` | `fixtures/ring_{pos,neg}.ttl` | `reducts_twoop.ttl` (T-RING) |
| field | `spine/field.ttl` | `shapes/field.shapes.ttl` → `FieldMultInverseShape` | `probes/field_law.rq` | `fixtures/field_{pos,neg}.ttl` | `reducts_twoop_field.ttl` |
| module | `spine/module.ttl` | `shapes/module.shapes.ttl` → `ModuleScalarActionShape` | `probes/module_law.rq` | `fixtures/module_{pos,neg}.ttl` | `reducts_twoop_module.ttl` |
| vector:space | `spine/vector_space.ttl` | `shapes/vector_space.shapes.ttl` → `VectorSpaceScalarFieldShape` | `probes/vector_space_law.rq` | `fixtures/vector_space_{pos,neg}.ttl` | `reducts_twoop_vector_space.ttl` |

**Two-operation infrastructure (T-2OP-INFRA):** `signatures_twoop.ttl` (sigTwoBinary Σ={+,·,0,1}),
`operations_twoop.ttl` (the four op symbols), `records_twoop.ttl` (the discriminated reified two-op
application record class + additive/multiplicative discriminators), and the runner glob-lockstep
(`checks/run-algebra-checks.sh` loads every `shapes/*.shapes.ttl`).

**Per-rung record breakdown (recomputed on disk, `rec:*:record` rdf:type counts):**

| Rung | theory | model | denotatum | declaration | axiom | theorem | equation | two-op reduct records |
|---|---|---|---|---|---|---|---|---|
| semiring | 1 | 1 | 1 | 1 | 7 | 1 | 2 | 3 |
| ring | 1 | 1 | 1 | 1 | 8 | 1 | 2 | 3 |
| field | 1 | 1 | 1 | 1 | 10 | 1 | 2 | 3 |
| module | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 |
| vector:space | 1 | 1 | 1 | 1 | 3 | 1 | 2 | 2 |
| **two-op total** | **5** | **5** | **5** | **5** | **30** | **5** | **10** | **13** |

The two-op rungs are covered by the whole-spine `manifests/spine.yaml`; they have no separate per-rung
manifests (`EXPECTED_RUNGS` is the 8 one-op rungs only). The 13 two-op reduct/connecting records are
typed `rec:reduct:two:operation:record` and therefore sit OUTSIDE the one-law `rec:reduct:record` count
(REDUCTS stays 7).

---

## 2. Runner GREEN evidence

`bash basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` → **EXIT 0**. Tail:

```
  data: 41 ttl -> 2834 triples; shapes: 28 NodeShape(s); fixtures: 56
  (a) data graph conforms: True
  shapes graphs merged: 6 file(s) -> ['algebra.shapes.ttl','field.shapes.ttl','module.shapes.ttl','ring.shapes.ttl','semiring.shapes.ttl','vector_space.shapes.ttl']
  (b) fixtures: 26 positive, 29 negative, 1 empty control
  (d) V6 count self-check: 19 spine + 8 rung manifest(s), 4 DAG narrative figures; 0 manifest + 0 DAG mismatch(es)
  V0 GREEN: 103 Turtle files parse
  V1 GREEN: no denotatum/domain-class pun; no provenance on any denotatum (declaration-records exempt)
  V2 GREEN: empty.ttl admission REJECT confirmed; all 28 shapes 0-focus-gated in block (c)
  V3 GREEN: 25 sh:SPARQLConstraint clause(s) declared in the shapes graph
  V4 PENDING/DEFERRED: Yoneda-density fixtures are the Pass-2 fan-out (design §6); the spine mints none
  V5 GREEN: all 13 theory records name signature+equation+validation:mode+proof:status
  V6 GREEN: disk == manifests/*.yaml == phase_w2_sp0_fold DAG node
  V7 GREEN: all 57 reshaped records dual-attributed: executor>=1 AND shadow>=1 + prov:wasGeneratedBy
  V8 GREEN: shapes graph valid SHACL; 28 NodeShapes all sh:targetClass, 0 sh:targetNode, 25 sh:sparql
  GATE-LADDER GREEN: 9 gate specs + 9 clause specs; identifiers unique
  ONTOLOGY DEPTH CHECK PASSED   Files checked: 103
  ALGEBRA CHECKS GREEN
  EXIT: 0
```

Non-vacuity: `data graph conforms: True`; 56 fixtures (26 pos / 29 neg / 1 empty); `empty.ttl =>
admission REJECT (0 focus, vacuous)`; every one of the 28 NodeShapes has ≥1 focus node (block (c) —
each two-op shape carries **13 focus node(s)** over `rec:model:record`); V6 disk==manifest==DAG with
**0 mismatch**.

---

## 3. Ring-as-reducts edge inventory (D24 A6)

All reduct/connecting/morphism edges verified to resolve to **defined subjects** — **0 dangling out of
143 reduct-edge objects** (`rel:reduct`, `rel:reduct:source`, `rel:reduct:theory`, `rel:connects`,
`rel:equation`). Each additive/multiplicative reduct TARGET is a **committed one-operation model-record**
reused by IRI (bridge-never-duplicate), e.g. the ring additive reduct target is
`alg:abelian:group:…:model:…:canonical` defined at `spine/abelian_group.ttl:144`; the semiring additive
reduct target is the `commutative_monoid` model-record at `spine/commutative_monoid.ttl:130`.

| Rung | additive reduct → | multiplicative reduct → | gluing / interaction morphism |
|---|---|---|---|
| **Semiring** | commutative_monoid model-record | monoid model-record | distributivity connecting morphism (· distributes over +) |
| **Ring** | abelian_group model-record | monoid model-record | distributivity connecting morphism |
| **Field** | abelian_group model-record | abelian_group (nonzero) model-record | distributivity connecting morphism (mult-comm carried by the abelian multiplicative reduct) |
| **Module** | abelian_group model-record | — | scalar-action morphism (ring acting on the abelian group) |
| **VectorSpace** | module reduct → module model-record | — | scalar-field morphism (Module over a Field) |

This is exactly the D24 A6 decomposition: the semiring↔ring distinction is made **structural** — a
semiring's additive reduct is a commutative_monoid (no additive inverse), a ring's is an abelian_group
(the additive-inverse upgrade); a field's multiplicative reduct is an abelian group (field-mult-comm);
a module is an abelian group + ring scalar-action; a vector space is a module over a field. All 13
records are typed `rec:reduct:two:operation:record` (outside the one-law `ReductShape` gate and the
REDUCTS=7 count).

---

## 4. Per-rung negative-flip demonstration

Every two-op rung has one single-violation-injected negative fixture that flips its characteristic tooth
`True → False` (each confirmed `does NOT conform (tooth bites)` in block (b) of the green run), while the
positive witness conforms:

| Rung | positive (conforms) | negative (tooth bites) | injected single violation |
|---|---|---|---|
| semiring | `semiring_pos.ttl` (saturating B(2) semiring on {0,1,2}, not a ring) | `semiring_neg.ttl` | one multiplicative row 1·2 perturbed 2→1 so x·(y+z) ≠ x·y+x·z → `SemiringDistributivityShape` |
| ring | `ring_pos.ttl` | `ring_neg.ttl` | distributivity violation → `RingDistributivityShape` |
| field | `field_pos.ttl` | `field_neg.ttl` | multiplicative-inverse violation → `FieldMultInverseShape` |
| module | `module_pos.ttl` | `module_neg.ttl` | scalar-action violation → `ModuleScalarActionShape` |
| vector:space | `vector_space_pos.ttl` | `vector_space_neg.ttl` | field-scalars violation → `VectorSpaceScalarFieldShape` |

---

## 5. [S]-token additions

The whole two-operation line is **SYN** (absent from Helios as algebra, `algebra_rings.ttl:30-35`), so
every two-op token is `[S]` and flagged in-line in each file's `rdfs:comment` for the §7.2 sign-off
packet. There are **no two-op `[V]`/`[D]` IRIs** — the `[V]`/`[D]` mentions in the rung comments are
references to shape terminology, not attested tokens. The `[V]`-anchor cross-check therefore reduces to
**reduct-target resolution into the committed one-op tower**, verified in §3 (0 dangling).

`[S]`-tag counts (spine + shapes + reducts per rung): semiring 30, ring 31, field 35, module 26,
vector:space 28. Infra: signatures_twoop 3, operations_twoop 6, records_twoop 6, reducts_twoop 5.

Representative new `[S]` token families (all flagged in-file):

- **signature/operations:** `order:two:binary` (sigTwoBinary profile); `species:sum / species:zero /
  species:one / species:product`; `genus:additive / genus:multiplicative` discriminating roles;
  `order:nullary` (units 0,1).
- **records:** `rec:application:two:operation:record` leaf; `class:discriminator / order:enumeration`;
  `@rel:operation:discriminator`.
- **reducts:** `order:structure` (structure reduct vs one-law forgetful reduct); `class:distributivity /
  genus:distribution / species:gluing` (connecting morphism); `class:action / genus:scalar`
  (scalar-action); `@rel:connects`, `@rel:reduct:source`, `@rel:reduct:theory`.
- **rung subdomains:** `semiring`, `ring`, `field`, `module`, `vector:space` (adjective-first compound),
  plus per-rung theorem tokens (`class:expansion` semiring, `class:absorption` ring, `class:integrity /
  species:divisor` field, `class:annihilation` module, `class:negation / genus:scalar` vector:space).
- **consolidation (T-PROV-2OP):** no NEW vocabulary — `resolution_lane_twoop.ttl` reuses the committed
  scope-marker class, Draft activity and executor/shadow agents by IRI.

---

## 6. Residual issues

1. **V7 lane omitted by the rungs, closed by consolidation (sign-off item).** The five rung executors
   minted the `@rel:authority` quartet but did NOT author the V7 dual-attribution lane; the consolidation
   closed it in `reviews/resolved/resolution_lane_twoop.ttl` using the generic whole-fold
   `sp0:spine:fold` executor/shadow agents (the same agents the one-op tower uses). If the maintainer
   wants **per-rung** executor/shadow agent granularity rather than the generic fold agents, that is a
   §7.2 refinement — but the committed one-op tower itself uses the generic agents, so this lane matches
   the established precedent.
2. **V4 (Yoneda-density) PENDING/DEFERRED** by design §6 (Pass-2 fan-out); the spine mints no V4 fixtures.
   Expected, not a regression.
3. **DAG file edited outside the algebra tree.** `basicttl/dag/dag_instances.ttl` (the
   `phase_w2_sp0_fold` narrative) was updated for the V6 disk==manifest==DAG self-check. This is NOT a
   `basicttl/foundation/*` edit and was explicitly named by T-2OP-INFRA as the consolidation's re-derive
   responsibility; the whole node prose was brought to disk truth so no count claim is left false.
4. **Two-op rungs have no per-rung manifests.** They are covered by the aggregate `spine.yaml`; consistent
   with `EXPECTED_RUNGS` (8 one-op rungs). If per-rung two-op manifests are later desired, `EXPECTED_RUNGS`
   and the manifest set would extend together.

---

## 7. Additive confirmation

- `git diff --stat basicttl/foundation` → **empty** (no `fnd:` / foundation edit; Stage-3c demolition
  untouched).
- Only change outside `basicttl/primordial/type/algebra/**`: `basicttl/dag/dag_instances.ttl` (the
  sanctioned V6 DAG re-derive, §6.3).
- Consolidation additions under the algebra tree: **new** `reviews/resolved/resolution_lane_twoop.ttl`
  (112 triples); **re-derived** `manifests/spine.yaml` (COUNT block to disk truth). All rung/infra atom
  files added by the fan-out remain as authored.
- No committed one-op rung atom edited; no `shapes/algebra.shapes.ttl` edit; no git actions taken.

**Final verdict: GREEN.** The two-operation algebra floor is realized, teeth-proved, reduct-linked to the
one-operation tower, and provenance-closed; the full runner is exit-0 non-vacuous with all gates green
(V4 the design-§6 deferral). The `fnd:` algebra floor can proceed to Stage-3c demolition on this basis.
