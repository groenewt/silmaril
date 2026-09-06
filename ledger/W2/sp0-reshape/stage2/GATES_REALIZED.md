# Stage 2b-i — GATES REALIZED (SP0 primordial spine-fold, W2)

Consolidation record for the **full gate apparatus** wrapped around the built + green 8-rung
algebra tower. Stage 2b-i (T-SHAPES → T-FIX → T-GATES → T-MANIFEST → T-PROV) extended the SHACL
tooth set, completed the fixture tree, asserted gates V0–V8 explicitly in the runner, wired the
V6 disk==manifest==DAG count self-check, and built the V7 dual executor/shadow provenance lane.

**VERDICT: GREEN.** The full runner
`basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` exits **0**, non-vacuous, over
**27 data ttl → 1778 triples · 23 NodeShapes · 46 fixtures**. Every declared shape carries ≥1
focus node, every negative fixture bites, the empty control is an admission REJECT, V6
disk==manifest==DAG holds across all surfaces, V7 dual-attribution closes on all 29 reshaped
records, and the depth gate passes (74 files).

All facts below were reproduced from disk during consolidation (Praeriehund honesty: no gate is
claimed that was not run; figures are RDF-parsed, not asserted). Runner exit code and tail
captured verbatim in §2.

---

## 1. SHACL shape inventory + focus counts

23 NodeShapes, **all `sh:targetClass`, zero `sh:targetNode`** (the design §4 anti-pattern the
0-focus gate detects), carrying **20 `sh:SPARQLConstraint`** clauses. Every shape has ≥1 focus
node over the merged data graph — a 0-focus shape is a runner REJECT (block (c)).

| # | NodeShape | focus nodes | role |
|---|-----------|------------:|------|
| 1 | TheoryShape | 8 | presented Lawvere theory record (sig+eqn cardinality + identity collision) |
| 2 | ModelShape | 8 | B4 Plane-1 model-record class |
| 3 | EquationRecordShape | 21 | two-sided laws split (closure.ttl:185-192 precedent) |
| 4 | ReductShape | 7 | forgetful reduct theory-morphism |
| 5 | CarrierGroundingShape | 8 | set-floor grounding edge (conditional sh:sparql) |
| 6 | ProofStatusShape | 8 | D24 A0 8-value proof:status enum |
| 7 | ValidationModeShape | 8 | D24 A0 4-value validation:mode enum |
| 8 | ProvenanceShape | 16 | provenance quartet+authority on theory + declaration records |
| 9 | ProvenanceClosureShape | 29 | V7 twin: dual executor/shadow attribution on reshaped records |
| 10 | BridgeShape | 8 | every denotatum bridged to its retired fnd: name |
| 11 | DifferentFromWitnessShape | 8 | owl:differentFrom rung-distinctness witness |
| 12 | MagmaClosureShape | 8 | per-law tooth (closure) |
| 13 | SemigroupAssociativityShape | 8 | per-law tooth (associativity) |
| 14 | GroupInverseShape | 8 | per-law tooth (inverse) |
| 15 | CommutativeMonoidCommutativityShape | 8 | per-law tooth (commutativity) |
| 16 | AbelianGroupCommutativityShape | 8 | per-law tooth (commutativity) |
| 17 | QuasigroupDivisionShape | 8 | per-law tooth (division) |
| 18 | LoopIdentityShape | 8 | per-law tooth (identity) |
| 19 | V1DenotatumHygieneShape | 8 | V1 REFINED: no provenance / no multi-domain-pun on a denotatum |
| 20 | V1ClassDeclarationPunShape | 7 | V1 REFINED: ClassDeclaration ≥2 domain-class pun (the frame.ttl:7 fix) |
| 21 | AlgebraProgenitorShape | 1 | agnostic progenitor theory-root grounds nothing |
| 22 | GateIdentityShape | 9 | gate-spec identifier uniqueness (core:entity ladder) |
| 23 | ClauseIdentityShape | 9 | gate-clause identifier uniqueness (core:entity ladder) |

Source: `basicttl/primordial/type/algebra/shapes/algebra.shapes.ttl`. Runner block (c) prints
each `focus OK` line; all 23 ≥1.

---

## 2. Gate crosswalk V0–V8 (+ GATE-LADDER) with GREEN evidence

The runner asserts every gate **by name** (block (f)), so V0–V8 status is reported honestly
rather than inferred from a bare `sh:conforms true`. Verbatim from a fresh
`bash basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` (**exit code 0**):

```
== folded algebra spine gate (basicttl/primordial/type/algebra) ==
  data: 27 ttl -> 1778 triples; shapes: 23 NodeShape(s); fixtures: 46
  (a) data graph conforms: True
  ... (c) focus OK: all 23 shapes >=1 focus ...
  (b) fixtures: 21 positive, 24 negative, 1 empty control
  (d) V6 count self-check: 19 spine + 8 rung manifest(s), 4 DAG narrative figures; 0 manifest + 0 DAG mismatch(es)
== gates V0-V8 (folded algebra gate ladder, design §4) ==
  V0 GREEN: 74 Turtle files parse
  V1 GREEN: no denotatum/domain-class pun; no provenance on any denotatum (declaration-records exempt)
  V2 GREEN: empty.ttl admission REJECT confirmed; all 23 shapes 0-focus-gated in block (c)
  V3 GREEN: 20 sh:SPARQLConstraint clause(s) declared in the shapes graph
  V4 PENDING/DEFERRED: Yoneda-density fixtures are the Pass-2 fan-out (design §6); the spine mints none
  V5 GREEN: all 8 theory records name signature+equation+validation:mode+proof:status
  V6 GREEN: disk == manifests/*.yaml == phase_w2_sp0_fold DAG node (19 spine figures + 8 per-rung manifests + 4 DAG narrative figures all equal a fresh disk recount)
  V7 GREEN: all 29 reshaped records dual-attributed: executor>=1 AND shadow>=1 (prov:wasAttributedTo) + prov:wasGeneratedBy (1 executor agent(s), 1 shadow agent(s))
  V8 GREEN: shapes graph valid SHACL; 23 NodeShapes all sh:targetClass, 0 sh:targetNode, 20 sh:sparql
  GATE-LADDER GREEN: 9 gate specs + 9 clause specs on the core:entity ladder; gate/clause identifiers unique
== depth gate (every owl:Class under basicttl/primordial/type/algebra >= 200-char rdfs:comment) ==
ONTOLOGY DEPTH CHECK PASSED
Files checked: 74
ALGEBRA CHECKS GREEN
EXIT_CODE=0
```

| Gate | Meaning | Status | Evidence |
|------|---------|--------|----------|
| V0 | Syntax — every *.ttl parses | GREEN | 74 Turtle files parse |
| V1 | Hygiene (REFINED §4/§7.5) — no denotatum pun, no provenance on denotatum; declaration-record owl:Class-with-provenance EXEMPT | GREEN | frame.ttl:7 pun fixed; V1DenotatumHygiene + V1ClassDeclarationPun shapes green; model-records not flagged |
| V2 | Non-vacuous — empty ⇒ REJECT + no 0-focus shape | GREEN | empty.ttl admission REJECT; all 23 shapes ≥1 focus |
| V3 | Categorical probes — sh:sparql clauses present | GREEN | 20 sh:SPARQLConstraint declared |
| V4 | Yoneda-density | PENDING/DEFERRED | Pass-2 fan-out (design §6); spine mints none — documented gap, not a failure |
| V5 | Algebraic-law — every theory names sig+eqn+validation:mode+proof:status | GREEN | all 8 theory records complete |
| V6 | Manifest coverage — disk == manifest == DAG | GREEN | 19 spine + 8 rung manifests + 4 DAG figures, 0 mismatch |
| V7 | Provenance closure — executor≥1 AND shadow≥1 + wasGeneratedBy | GREEN | 29 reshaped records dual-attributed; 1 executor + 1 shadow agent |
| V8 | SHACL-2017 discipline — targetClass-only, ≥1 SPARQLConstraint | GREEN | 23/23 targetClass, 0 targetNode, 20 sparql |
| GATE-LADDER | 9 gate + 9 clause specs, unique identifiers | GREEN | on the reference core:entity ladder (consolidated.shacl.ttl:1324) |

V4 is the **only** non-GREEN gate and is an explicit design deferral (Pass-2 fan-out, §6),
recorded as the single open GAP in `manifests/spine.yaml` — it is not a regression.

---

## 3. Fixture inventory (46 total: 21 positive / 24 negative / 1 empty control)

Every shape with a natural negative is exercised by a committed on-disk fixture the runner
validates (block (b)); each negative flips `conforms True→False` under its single injected
violation, each positive stays `True`.

- **Per-rung witnesses (16):** `{magma,semigroup,monoid_z2,commutative_monoid,group,abelian_group,quasigroup,loop}_{pos,neg}` — pos conforms, neg's law violation bites.
- **Finite Cayley-table certificates (4):** `monoid_z2_cayley{,_negative}`, `group_z3_cayley{,_negative}` — the finite:checked evidence-plane witnesses + their non-total / associativity-violating negatives.
- **Gate-apparatus teeth (T-FIX / T-GATES) with dedicated fixtures:** `proof_status_{pos,neg}`, `validation_mode_{pos,neg}`, `provenance_{pos,neg}`, `provenance_closure_{pos,neg}`, `bridge_{pos,neg}`, `different_from_witness_{pos,neg}`, `gate_identity_{pos,neg}`, `clause_identity_{pos,neg}`, `carrier_grounding_{pos,neg}`, `reduct_{pos,neg}`.
- **V1-hygiene negatives:** `v1_class_pun_neg` (re-injects the exact frame.ttl:7 pun), `v1_denotatum_provenance_neg`, `reduct_shape_neg`, `progenitor_neg`.
- **Empty control (1):** `empty.ttl` → admission REJECT (0 focus, vacuous), design §4 empty⇒REJECT.

Runner tally line: `(b) fixtures: 21 positive, 24 negative, 1 empty control` — every negative
bites, empty ⇒ REJECT.

---

## 4. V6 manifest coverage + the phase_w2_sp0_fold DAG node

The V6 self-check recomputes every figure freshly from disk (rdflib over the merged algebra
graph; never hard-coded) and demands **disk == manifest == DAG** across three surfaces:

- **spine.yaml** — 19 canonical COUNT figures (`manifests/spine.yaml`, Flavor-B AOB envelope). All match disk. A missing canonical figure is itself RED (non-vacuity).
- **8 per-rung manifests** — `magma/semigroup/monoid/commutative_monoid/group/abelian_group/quasigroup/loop.yaml`, each a per-rung THEORY/MODEL/DENOTATUM/DECLARATION/AXIOMS/THEOREMS/EQUATIONS/REDUCTS scope. All 8 rungs present; all figures match.
- **DAG node** `urn:silmaril:entity#phase_w2_sp0_fold` (`basicttl/dag/dag_instances.ttl:339`) — 4 narrative figures gated: `rungs=8`, `shapes=23`, `probes=17`, `fixtures=46`, each `disk==manifest==DAG`.

Canonical disk figures (all gated GREEN): theories 8 · models 8 · denotata 8 · declarations 8 ·
signatures 5 · operations 5 · axioms 24 · theorems 6 · certificates 6 · equations 21 · reducts 7
· gate_specs 9 · clause_specs 9 · rungs 8 · **shapes 23** · **probes 17** · **fixtures 46** ·
data_files 27 · triples 1778.

Result line: `(d) V6 count self-check: 19 spine + 8 rung manifest(s), 4 DAG narrative figures;
0 manifest + 0 DAG mismatch(es)`. PROBE OF RECORD: perturb any manifest VALUE or DAG figure ⇒
V6 RED; restore ⇒ GREEN.

---

## 5. V7 dual executor/shadow provenance lane

BUILT in T-PROV (the reference `governance/` layer is empty). The lane lives under
`basicttl/primordial/type/algebra/`:

- `reviews/executor/executor_lane.ttl` — the EXECUTOR `prov:Agent` (`…governance:provenance:class:agent:executor`, a `prov:SoftwareAgent`), the D24 ExecutorValidation lifecycle activity + review record.
- `reviews/shadow/shadow_lane.ttl` — the SHADOW `prov:Agent` (`…class:agent:shadow`), ShadowCritique + ShadowRevalidation.
- `reviews/resolved/resolution_lane.ttl` — the resolved dispositions.
- `receipts/receipts.ttl` — the D24 Modular-Option-A+ Accepted-state seal, dual-signed by both agents, recording that all 29 reshaped records closed executor≥1 AND shadow≥1.

A "reshaped record" = a subject carrying the D24 provenance quartet (`@rel:authority`): the
8 theory + 8 model/declaration + 7 reduct + 6 theorem records = **29** (Plane-2 denotata carry
no authority and are OUT of scope by V1). Each is attributed to ≥1 executor agent AND ≥1 shadow
agent via `prov:wasAttributedTo`, plus a `prov:wasGeneratedBy`. Gated three ways: runner block
(f) V7 dual-count, `ProvenanceClosureShape` (29 foci, block (b)), and
`probes/provenance_closure.rq`. Result: `V7 GREEN: all 29 reshaped records dual-attributed …
(1 executor agent(s), 1 shadow agent(s))`.

---

## 6. Residual issues

- **V4 Yoneda-density (PENDING/DEFERRED):** the spine mints no Yoneda-density fixtures; this is the Pass-2 fan-out (design §6), recorded as the single open GAP in `spine.yaml`. Not a regression, not a blocker for Stage 2b-i.
- **Stale scaffold header (non-blocking, cosmetic):** the pre-T-SHAPES RED-state comment block at the top of `shapes/algebra.shapes.ttl` (originally describing a "PLACEHOLDER (prefixes only)" / "VACUOUS" zero-shape file) may still not fully describe the realized 23-shape tooth set. Comment-only; the runner is unaffected. Flagged by the T-SHAPES shadow; refresh recommended when next editing the file.
- **Per-law scoping (documented reviewer note):** the 7 per-law teeth target `rec:model:record`; all Z/n positive witnesses satisfy every law so none is falsely reddened. A per-rung law-scope marker would be a fan-out refinement, not a spine obligation.
- No functional placeholders or stubs. No signed-off rung atom was edited to force green.

## 7. Additive confirmation

`git diff --stat` over `basicttl/foundation` = **empty**; over SP1/SP2/SP3 = **empty**. The
`fnd:`/`basicttl/foundation/algebra_spine.ttl` tower and SP1/SP2/SP3 are byte-untouched (the
B3(a) true-full-retire is the NEXT stage's T-RETIRE, not this one).

Working-tree scope (`git status`) — only in-scope paths:

- Modified: `basicttl/primordial/type/algebra/{checks/run-algebra-checks.sh, product/frame.ttl, shapes/algebra.shapes.ttl}` + `basicttl/dag/dag_instances.ttl` (the T-MANIFEST-sanctioned DAG-node edit).
- New (all under `basicttl/primordial/type/algebra/**`): `fixtures/**` (new teeth), `gates/gates.ttl`, `manifests/*.yaml`, `probes/{clause_identity,gate_identity,provenance_closure}.rq`, `receipts/receipts.ttl`, `reviews/{executor,shadow,resolved}/*.ttl`.

**V1 fix confirmed:** `product/frame.ttl:7` is now
`family:Frame a ontology:Class, model:ClassDeclaration, model:Product` — the second domain-class
pun (`model:Frame`) is removed, leaving ClassDeclaration + one structural kind (matches the sum/*
sibling pattern). V1ClassDeclarationPunShape green over it; `v1_class_pun_neg.ttl` re-injects the
exact pun to prove the tooth still bites. **Model-records NOT flagged:** the B4 model-record
declaration classes (owl:Class + rec:model:record + rec:declaration:record + provenance) are
`rec:declaration:record` (owl:disjointWith `rec:denotatum:record`), so neither V1 shape targets
them — legal OWL2 metaclass punning, EXEMPT (design §7.5), and V1 stays GREEN with no false flag.

---

*Consolidation pass ran `run-algebra-checks.sh` end-to-end (exit 0, GREEN, non-vacuous) and
verified additive scope via `git diff`/`git status`. No git operations were performed.*
