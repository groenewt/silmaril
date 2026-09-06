# Stage 2a — RUNGS REALIZED (SP0 primordial spine-fold, W2)

Consolidation record for the folded algebra spine. Eight rungs + the reduct lattice were
fanned out from the signed-off `spine/monoid.ttl` exemplar (B4 two-plane pattern), then
verified together by an independent on-disk pass. **VERDICT: GREEN** — the full runner
`basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` exits 0 with every shape
exercised, every negative fixture biting, and zero cross-rung breakage.

All facts below were reproduced from disk during consolidation (Praeriehund honesty: no gate
is claimed that was not run; figures are RDF-parsed, not asserted).

---

## 1. Per-rung file inventory + atom counts

Eight rungs, four disjoint files each (spine record + positive fixture + single-violation
negative fixture + SPARQL law probe), plus the shared reduct lattice. `monoid` is the
signed-off exemplar (its equation records live in the committed `equations.ttl`, not inline).

| Rung | spine/*.ttl (lines) | pos/neg fixtures | law probe | theory·model·denot·decl·gate | axiom rec | eqn rec |
|------|--------------------:|------------------|-----------|------------------------------|----------:|--------:|
| magma | magma.ttl (169) | magma_{pos,neg}.ttl | magma_law.rq | 1·1·1·1·1 | 1 | 0 |
| semigroup | semigroup.ttl (210) | semigroup_{pos,neg}.ttl | semigroup_law.rq | 1·1·1·1·1 | 2 | 1 |
| monoid *(exemplar)* | monoid.ttl (182) | monoid_z2{,_negative}.ttl | monoid_identity.rq | 1·1·1·1·1 | 2 | 2 *(in equations.ttl)* |
| group | group.ttl (261) | group_{pos,neg}.ttl | group_law.rq | 1·1·1·1·1 | 4 | 2 |
| commutative_monoid | commutative_monoid.ttl (282) | commutative_monoid_{pos,neg}.ttl | commutative_monoid_law.rq | 1·1·1·1·1 | 4 | 4 |
| abelian_group | abelian_group.ttl (339) | abelian_group_{pos,neg}.ttl | abelian_group_law.rq | 1·1·1·1·1 | 5 | 6 |
| quasigroup | quasigroup.ttl (214) | quasigroup_{pos,neg}.ttl | quasigroup_law.rq | 1·1·1·1·1 | 2 | 0 |
| loop | loop.ttl (295) | loop_{pos,neg}.ttl | loop_law.rq | 1·1·1·1·1 | 3 | 2 |

Uniform B4 shape per rung (RDF-parsed): exactly **1 theory:record**, **1 model:record**
(punned owl:Class + rec:declaration:record, carrying the owl:Restriction bundle + provenance
+ owl:disjointWith teeth), **1 denotatum:record** (kingdom:type…component:type, no
provenance), **1 gate** (Plane-3 reconciliation triad). Every denotatum is byte-identical to
its `bridges.ttl` fnd:-alias target (§7).

Shared reduct lattice: **`reducts.ttl` (243 lines)** — 7 forgetful reduct records + 3
obligation extension morphisms (dual-typed rec:equation:record); consolidation probes
`probes/obligation_count.rq` and `probes/one_law_per_rung.rq`; twin fixtures
`fixtures/reduct_{pos,neg}.ttl`.

Equation-record reconciliation (RDF-parsed, sums to the runner's EquationRecordShape focus
count of 21): equations.ttl 3 + reducts.ttl 3 + semigroup 1 + group 2 + commutative_monoid 4
+ abelian_group 6 + loop 2 = **21**. No dangling equation records.

Adjective-first compounds (B1 lock) confirmed on disk: `commutative:monoid`, `abelian:group`.

---

## 2. Runner GREEN evidence

`bash basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` — **exit code 0**. Tail:

```
== folded algebra spine gate (basicttl/primordial/type/algebra) ==
  data: 22 ttl -> 1499 triples; shapes: 4 NodeShape(s); fixtures: 21
  (a) data graph conforms: True
  (c) focus OK: <...#AlgebraProgenitorShape> 1 focus node(s)
  (c) focus OK: <...#EquationRecordShape> 21 focus node(s)
  (c) focus OK: <...#ModelShape> 8 focus node(s)
  (c) focus OK: <...#TheoryShape> 8 focus node(s)
  ... (b) 10 positive PASS, 10 negative PASS (tooth bites), 1 empty control PASS ...
  (b) fixtures: 10 positive, 10 negative, 1 empty control
  (d) PENDING: no manifest figure stated yet (T-MANIFEST wires the full V6 self-check);
      disk figures = {'data_files': 22, 'nodeshapes': 4, 'fixtures': 21, 'triples': 1499}
== depth gate (every owl:Class under .../algebra >= 200-char rdfs:comment) ==
ONTOLOGY DEPTH CHECK PASSED
Files checked: 44
ALGEBRA CHECKS GREEN
```

- **(a) data conformance:** 22 data ttl → 1499 triples conform against
  `shapes/algebra.shapes.ttl` (inference=rdfs). TRUE.
- **(c) non-vacuity (0-focus REJECT):** all 4 declared NodeShapes exercised —
  AlgebraProgenitorShape 1, EquationRecordShape 21, ModelShape 8, TheoryShape 8. No shape
  has zero focus nodes.
- **(e) depth gate:** all 44 files' owl:Classes carry ≥200-char rdfs:comment. PASSED.
- **(d) count coverage:** PENDING by design (manifest figures are the T-MANIFEST deliverable,
  not this stage). Not a failure — it is the runner's own PENDING branch.

---

## 3. Per-rung negative-flip demonstration (RED→GREEN)

Two independent teeth per rung: the SHACL fixture-polarity gate (runner clause (b)) AND the
rung's SPARQL law probe. Both were re-run at consolidation.

**SHACL fixture polarity (runner clause (b)):** every positive fixture merged onto the
conformant base still conforms; every negative flips conforms True→False (its single injected
violation bites); empty.ttl is an admission REJECT (0 focus). 10 positive PASS / 10 negative
PASS / 1 empty PASS — no negative failed to flip.

**SPARQL law probes (pos = 0 rows GREEN, neg = >0 rows RED):**

| Rung | probe | pos rows | neg rows | characteristic violation caught |
|------|-------|---------:|---------:|---------------------------------|
| magma | magma_law.rq | 0 | 1 | closure escapee (e·a=c outside carrier) |
| semigroup | semigroup_law.rq | 0 | 7 | associativity failures |
| monoid | monoid_identity.rq | 0 | 1 | two-sided identity broken |
| group | group_law.rq | 0 | 1 | inverse law violated |
| commutative_monoid | commutative_monoid_law.rq | 0 | 2 | commutativity a·b≠b·a |
| abelian_group | abelian_group_law.rq | 0 | 2 | commutativity a·b≠b·a |
| quasigroup | quasigroup_law.rq | 0 | 4 | Latin-square / unique divisibility |
| loop | loop_law.rq | 0 | 4 | identity + divisibility |
| *reduct* | obligation_count.rq | 0 | 1 | one-sided two-sided-law (missing @rel:right) |
| *reduct* | one_law_per_rung.rq | 0 | 0 (reduct_neg targets the obligation tooth, not adds:law) |

Every rung's negative flips at least one committed SHACL shape (so the runner catches it) AND
its dedicated law probe returns rows. GREEN restored on the positive twin in every case.

---

## 4. Reduct edge + obligation-morphism inventory

Seven forgetful reduct theory-morphisms (`rec:reduct:record`, child ⊢ parent, each carrying
exactly one `@rel:adds:law` — the single law the child adds over its parent, re-homing
algebra_spine.ttl:99-103 constraints B (no-cram ≤1) + C (at-least-one ≥1) into the folded
idiom):

```
reduct semigroup          -> magma        (adds: associativity)
reduct monoid             -> semigroup    (adds: identity)
reduct commutative:monoid -> monoid       (adds: commutativity)
reduct group              -> monoid       (adds: inverse)
reduct abelian:group      -> group        (adds: commutativity)
reduct quasigroup         -> magma        (adds: divisibility / Latin square)
reduct loop               -> quasigroup   (adds: identity)
```

`magma` is the lattice root (no reduct; its parent is the progenitor via `rdfs:subClassOf` on
the model-record class, design §1.9). The lattice is a DAG (monoid and abelian:group each have
two in-edges honoring the diamond).

Three obligation extension morphisms (`@rel:obligation:count 2`, reifying both sides of a
two-sided law as `@rel:left` / `@rel:right`):

```
monoid two-sided identity obligation (count 2)   left-unit e·x=x  + right-unit x·e=x
group  two-sided inverse  obligation (count 2)   x·inv(x)=e       + inv(x)·x=e
loop   two-sided identity obligation (count 2)   left-unit        + right-unit
```

Consolidation teeth (both GREEN over reducts data, 0 rows):
- `obligation_count.rq` — returns any count-2 obligation missing a side; reduct_neg flips it
  RED (1 row).
- `one_law_per_rung.rq` — returns any reduct whose `@rel:adds:law` count ≠ 1 (cram or starve);
  all seven carry exactly one.

Referential integrity: an independent scan of all `rel:reduct` / `owl:disjointWith` /
`rdfs:subClassOf` objects that are algebra IRIs found **zero dangling targets** — every edge
resolves to a defined subject among the 256 defined subjects in the tree. No cross-rung
breakage.

---

## 5. [S]-token list added this stage

`[S]` = a Linnaean-ladder token with no runtime (Helios/aob) precedent; each use is tagged in
an rdfs:comment for the sign-off packet. Per-file `[S]` tag counts (on disk): abelian_group 26,
commutative_monoid 19, group 13, loop 22, magma 8, monoid 8, quasigroup 11, semigroup 11,
progenitor 3, reducts 26.

Distinct `[S]`-flagged tokens/idioms across the stage:

- **`class:theory` / `genus:presented`** (the theory-record plane; §7.2 #1 mint-more-than-runtime, PIVOTAL) — UNATTESTED.
- **`class:model` / `genus:governed` / `component:class`** (B4 Plane-1 declaration-record model class) — UNATTESTED.
- **Structure/uniqueness theorem tokens:** `class:associativity` `genus:generalized` `species:composition` (semigroup generalized-associativity theorem); `class:inverse` `genus:uniqueness` `species:inverse` (group inverse-uniqueness theorem) — UNATTESTED.
- **Two-sided-split side segments:** `species:member:left` / `species:member:right` (monoid, commutative:monoid, loop identity split); `species:inverse:left` / `species:inverse:right` (group, abelian:group inverse split) — UNATTESTED side segments.
- **Quasigroup/loop division tokens:** `genus:latin`, `species:unique`, `class:division` (Latin-square / unique divisibility) — UNATTESTED (0 aob dirs; design §1.5 / §7.2 #5).
- **Obligation-morphism tokens:** `genus:obligation`, `species:count:two`, plus the mapping / rec:equation:record dual-typing (reducts.ttl) — UNATTESTED.
- **D24 first-class metadata vocabularies** (no runtime precedent, D24-defined):
  `@rel:validation:mode` values `finite:table` (finite Cayley-table witness) and `rewrite`
  (equational rewriting); `@rel:proof:status` value `literature:backed`.
- **Plane-type tokens:** `@typ:declaration`, `@typ:certificate`, `@typ:gate`.
- **`@rel:authority 'SYN'`** applied to the fnd:SYN rungs (magma/lawClosure, group/lawInverse —
  the tower axioms with zero Helios basis, algebra_spine.ttl:41,61,114,141).

All are additive mints, flagged in-comment for the sign-off packet; none overwrites a runtime
atom.

---

## 6. Residual blocking issues

**None blocking.** Non-blocking notes carried forward from the executor/shadow rounds:

1. **magma closure has no dedicated SHACL shape yet.** The committed
   `shapes/algebra.shapes.ttl` (Stage-2a state: only TheoryShape / ModelShape /
   EquationRecordShape / AlgebraProgenitorShape) has no closure-specific tooth; a
   `MagmaClosureShape` is a Stage-2 **T-SHAPES** deliverable, out of the rung write scope.
   magma_neg is routed so its single closure escape (e·a=c) trips BOTH `magma_law.rq` AND the
   committed ModelShape identity tooth, so the runner still catches it. Honestly documented in
   the magma fixture headers.
2. **(d) count coverage is PENDING**, not GREEN — no manifest states a figure yet; the full V6
   self-check + manifest are the **T-MANIFEST** deliverable (which also edits the runner).
   Disk figures are reported: data_files 22, nodeshapes 4, fixtures 21, triples 1499.
3. **TODO-11 (bridge-never-duplicate):** 15 documented forward references — denotata are NOT
   re-`skos:exactMatch`'d in the rung files because bridges.ttl already carries the alias.
   Ledger item, not a defect.
4. **Stage 2b retirement pending (by design):** `fnd:*` and `basicttl/foundation/algebra_spine.ttl`
   are left intact (skos:closeMatch bridges only). The B3(a) retire / T-RETIRE stubbing is
   explicitly Stage 2b — Stage 2a is additive.

---

## 7. Additive confirmation

- `git diff --stat basicttl/foundation/algebra_spine.ttl` → **empty** (unchanged).
- `git status --porcelain` → **zero modified or deleted tracked files anywhere**; every change
  is a new untracked file under `basicttl/primordial/type/algebra/**` (7 new spine rungs +
  reducts.ttl + 16 rung fixtures + 2 reduct fixtures + 9 rung probes + 2 consolidation probes).
- No shared/committed file was edited: `shapes/algebra.shapes.ttl`, `equations.ttl`,
  `records.ttl`, `bridges.ttl`, `signatures.ttl`, `operations.ttl`, the runner, and
  `fnd:`/`algebra_spine.ttl` are all untouched.
- **[V] byte-verbatim vs primordials.yaml:** the 5 group [V] anchors (denotatum + closure +
  associativity + identity + inverse) appear byte-exact (alg:/HEAD form) in `spine/group.ttl`;
  every rung's closure axiom is byte-derived from the [V] group closure via
  `subdomain:group→subdomain:<rung>` + `family:group→family:<rung>` (8/8 present); every rung's
  denotatum suffix is byte-identical to its `bridges.ttl` fnd:-alias target (8/8 MATCH,
  adjective-first compounds intact).

**Stage 2a is additive, non-vacuous, and GREEN.**
