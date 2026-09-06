# W2 · SP0 — the primordial spine-fold (algebra tower) — PLAN

> **superpowers:writing-plans output.** Executes the SP0 spine-fold design
> (`docs/superpowers/specs/2026-09-06-w2-sp0-primordial-fold-design.md`, read in full) for **Pass 1
> ONLY**: the one-operation algebra tower `magma → semigroup → monoid → commutative-monoid → group →
> abelian-group` + the division sub-family `quasigroup → loop` + the agnostic progenitor theory-root.
> Governing law: `ledger/W2/design_constraints.md` Directives **24** (Seed-Carrier), **25** (fold into
> `basicttl/primordial/type/**`, spine-first, CI lockstep), **26** (LOCKED naming: FULL verified-runtime
> Linnaean-ladder IRIs VERBATIM, natural-language segment order). Maps:
> `ledger/W2/sp0-reshape/refmap/{00_REFMAP_SYNTHESIS,R1_naming_grammar,R2_consolidated_shape,R3_engine_algebra_skills,R4_docs_doctrine_gates}.md`.
> Reference to MATCH: `silmaril.final.consolidated.ttl`; the verified runtime
> `…/scratchpad/refcomp/zip/silmaril/**` (`ontology/{closure.ttl,consolidated.ttl,consolidated.shacl.ttl,primordial.yaml}`);
> the engine `…/scratchpad/refcomp/tar/bash/**` (`aob/urn/**` = canonical full-ladder IRI corpus,
> `config/algebra/primordials.yaml`, `lib/type-dag/algebra.sh`).
> Bite-sized, test-first (RED→GREEN), **zero placeholders**. Every asserted law has a biting SHACL/probe
> tooth proven by probe injection (conforms True→False; every negative fixture flips RED). Counts DERIVED
> from disk, never hard-coded. Commits signed under `basicttl/commit_signing_trust.ttl`.

---

## 0. Governing rulings this plan is built on (verified off disk)

- **IRI grammar (D26, LOCKED).** Every minted typed IRI carries the full 12-marker runtime ladder under
  the fixed head `urn:silmaril:type:graph:instance:instruction:code:property:` — verified verbatim in the
  aob corpus, e.g. group closure axiom on disk at
  `refcomp/tar/bash/aob/urn/silmaril/type/graph/instance/instruction/code/property/domain/mathematics/realm/algebra/subdomain/group/kingdom/axiom/phylum/operation/class/closure/order/binary/family/group/genus/product/species/membership/component/statement/instance/canonical/atom.spec.yaml`.
  Segment order = natural-language; the compound-token ORDER is **LOCKED adjective-first (§7.2 #9, B1):
  `abelian:group` / `commutative:monoid`** (maintainer ruling — verified-runtime + natural-language
  reading). Final marker pair =
  `component:instance` (NOT the drop's `specimen:instance`). Directory PLACEMENT is under
  `basicttl/primordial/type/algebra/**`; the short primordial root `urn:silmaril:primordial:type:` is
  **bridged to, never minted under** (placement ≠ IRI root).
- **Two-ladder ruling (design §4, §7.2 #8; confirmed against `closure.ttl`).** Algebra rungs/axioms/
  equations mint the **mathematics** 12-marker ladder (`…:domain:mathematics:realm:algebra:subdomain:…`).
  The **record CLASSES** they are `rdf:type`'d against, and the **gate/clause** specs, are the reference's
  seed-carrier ladder (`closure.ttl` uses head
  `…:property:grounding:ontology:basic:formal:domain:knowledge:representation:kingdom:specification:phylum:formal:contract:class:…:family:seed:genus:registry:species:{axiom,theorem,specimen,equation,term,variable}:record`).
  These record classes are **REUSED as `rdf:type` targets (bridge-never-duplicate)**, extended with
  parallel algebra record classes built in the SAME descent with the SAME `owl:Restriction` idiom.
- **Mint-more-than-runtime (design §0 one-line reconciliation; §7.2 #1 — PIVOTAL, pre-locked).** The
  runtime carries algebra ONLY as a FLAT `subdomain:group` (1 model type + 4 collapsed two-sided axioms)
  + the abstract `subdomain:primordial` root. The build therefore mints MORE atoms than the runtime shows
  — the group model + its 4 axioms + the progenitor are quoted VERBATIM as `[V]` anchors; every other rung,
  and every stratified plane (theory / signature / operation-symbol / equation-set / reduct), is `[D]`
  DERIVED by extending the grep-confirmed group skeleton, all in the SAME full-ladder grammar. Tokens with
  no runtime precedent are `[S]` and routed to §7.2 sign-off (see design §7.2, carried in T-BRIDGE + the
  PANEL task).
- **CI lockstep is mandatory (D25; verified).** `.github/workflows/ci.yml:27` runs
  `basicttl/foundation/checks/run-foundation-checks.sh`, whose SP0 data glob is `basicttl/foundation/*.ttl`
  ONLY (`run-foundation-checks.sh:70`) — and which ALSO builds the merged SP0+SP1+SP2+SP3 graph.
  `basicttl/primordial/type/**` is in NO runner. Folding here + moving witnesses to `fixtures/` goes
  VACUOUS unless a runner + CI discovery + gates move in lockstep. **B2 fix:** T-INFRA extends
  `run-foundation-checks.sh`'s SP0 loader to also discover `basicttl/primordial/type/algebra/**/*.ttl`
  (excl. `*.shapes.ttl`, `fixtures/**`), so the folded tower lives in the SAME merged graph the alias map
  is validated in — otherwise the `aob:SealedGroup → fnd:Group → new IRI` promise is tested in no single
  graph. That makes `run-foundation-checks.sh` a lockstep file (in write scope).
- **Notation.** `HEAD` = `urn:silmaril:type:graph:instance:instruction:code:property:domain:mathematics:realm:algebra:subdomain:`.
  Every algebra IRI = `HEAD` + a tail. `[V]`=grep-confirmed verbatim; `[D]`=derived from the group
  skeleton; `[S]`=no runtime precedent → §7.2 sign-off. `@P`=`urn:silmaril:type:graph:instance:instruction:code:property`;
  `@rel`=`@P:relation`; `@typ`=`@P:type`.

## Interfaces (whole pass)

**Consumes:** `basicttl/foundation/algebra_spine.ttl` (the `fnd:` tower being folded — composition map
`:99-103,183-195,408-522`, verified); `basicttl/primordial/type/**` (fold target: idiom `shapes.ttl`,
`algebra/product/frame.ttl`, `classes.ttl`, `imports.ttl`); the verified runtime
(`refcomp/zip/silmaril/ontology/closure.ttl` record-class + two-sided reification idiom; `consolidated.shacl.ttl`
gate ladder; `primordial.yaml`); the engine (`refcomp/tar/bash/aob/urn/**` full-ladder atoms;
`config/algebra/primordials.yaml`); `.github/workflows/ci.yml`; `basicttl/commit_signing_trust.ttl`
(reprovisioned `silm:signing_key_claude_2026b`, fp `B6F41C924ED120B6E42A7D5A2D292981114A752A`, ed25519, `silm:trust_policy_agent`).
**Produces:** the reshaped algebra spine under `basicttl/primordial/type/algebra/**` (theory / model /
signature / operation / equation / axiom / reduct records in full-ladder IRIs, all 8 rungs), intensional
record classes, the SHACL tooth set, positive+failing-negative fixtures per shape, gates V0–V8 wiring,
the NEW `run-algebra-checks.sh` runner wired into `ci.yml` in lockstep, the exhaustive alias/bridge map
(keeping SP1/SP2/SP3 `groundsIn*`/`subClassOf fnd:*` refs resolvable), the DAG node, and the executor/
shadow (V7) provenance lane. **Out of scope (Pass 2+):** rings/fields/modules/vector-spaces, set, spaces,
functionality, combinators, logic, group-action, Blotto, the D21 epistemology stratum, render-seal.

## Honesty ledger (design §5.1, gospel)

`skos:exactMatch` engine anchor: **Group** (type-level, `primordials.yaml:456-487`). `seed:conservativeBridge`:
**AlgebraicStructure** (root `:394-404`), **Magma**→group closure axiom, **Semigroup**→associativity,
**Monoid**→identity axiom. **NO engine anchor** (honest-red BUILD, proof-status `asserted`/`literature:backed`,
NOT `finite:checked`-from-engine): **CommutativeMonoid, AbelianGroup, Quasigroup, Loop**. Carriers
(Bit/Octet/ByteVector/Frame) = `seed:implementationBridge`. Every RECORD carries an authority tag +
provenance quartet; no provenance on a mathematical denotatum.

## Task graph / agent assignment (operator loop: executor + tandem shadow, ×2 double-dip, ≥5 agents)

Dependency order: **T-INFRA → T-CLASSES → {T-BRIDGE, T-SIG-OP} → T-PROG → T-MONOID (exemplar, SIGN-OFF
GATE) → {T-MAGMA, T-SEMI, T-CMON, T-GROUP, T-ABEL, T-QGRP, T-LOOP} (parallel) → T-REDUCT → T-SHAPES →
T-FIX → T-GATES → T-MANIFEST → T-PROV → T-RETIRE → T-INTEGRATION → T-PANEL.**
**Build is staged around the maintainer sign-off gate.** *Stage 1* = T-INFRA → T-CLASSES →
{T-BRIDGE, T-SIG-OP} → T-PROG → T-MONOID, materialising the infra + the monoid exemplar rung end-to-end,
self-validating non-vacuously; it stays **additive** (`fnd:` intact, bridges added — the retire needs the
full tower first). Build stops at the realized monoid rung for maintainer sign-off (design §7.3). *Stage 2*
(after sign-off) = the 7 sibling rungs + T-REDUCT…T-PANEL, including **T-RETIRE** (B3(a) true full retire). Each task = one executor E# + one
tandem shadow S# (parallel executors listed run only with their own shadow). All executors write ONLY
under `basicttl/primordial/type/algebra/**` (+ the lockstep files named in T-INFRA:
`run-algebra-checks.sh`, `ci.yml`, `dag_instances.ttl`, and — B2 — `run-foundation-checks.sh` whose SP0
loader is extended to discover the folded tree); if B3 disposition **(c)** is locked (§7.4/§7.2), the SP0
file `basicttl/foundation/algebra_spine.ttl` also enters scope (its `fnd:` rungs demoted to bridge
stubs). No SP1/SP2/SP3 floor is edited; the merged SP0+SP1+SP2+SP3 graph must stay green (design §5.2).

---

## Tasks

### T-INFRA — the algebra runner + CI lockstep (the vacuity trap, highest risk)
**Interfaces.** *Consumes:* `run-foundation-checks.sh` (glob pattern `:70`, depth gate `:143`, count
self-checks `:157-361`, citation gate `:363-560`); `ci.yml:13-27,109-119`. *Produces:*
`basicttl/primordial/type/algebra/checks/run-algebra-checks.sh`; a new step in `ci.yml`; the empty
scaffold `basicttl/primordial/type/algebra/{shapes/algebra.shapes.ttl,manifests/,fixtures/,probes/}`.
**Target files.** `basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` (NEW);
`basicttl/foundation/checks/run-foundation-checks.sh` (EDIT — B2: extend the SP0 loader to discover
`basicttl/primordial/type/algebra/**/*.ttl` excl. `*.shapes.ttl`/`fixtures/**`, so the folded tower is in
the merged graph); `.github/workflows/ci.yml` (EDIT — add step/job); empty `shapes/algebra.shapes.ttl`.
**RED (failing-probe-first).** Author the runner to (a) auto-discover `basicttl/primordial/type/algebra/**/*.ttl`
(except `*.shapes.ttl`, except `fixtures/**`) as the data graph and validate against
`shapes/algebra.shapes.ttl` with pyshacl; (b) iterate `fixtures/` asserting every `positive.ttl` conforms,
every `negative*.ttl` does NOT conform, and `empty.ttl` ⇒ admission REJECT; (c) FAIL any declared shape
with **zero focus nodes** (invert `run-foundation-checks.sh:90-102`'s skip-when-no-shapes: 0-focus =
unexercised = REJECT); (d) recompute every algebra count from disk and assert `== manifest`. First run,
before any records/fixtures exist, must **exit non-zero** ("no fixtures discovered; gate would be vacuous").
That non-zero is the RED probe of record for the runner itself.
**GREEN.** Once T-FIX lands ≥1 positive + ≥1 negative + `empty.ttl` and shapes have focus nodes, the
runner exits 0. Wire it into `ci.yml`: add `- name: Validate the folded algebra spine` running the runner
inside `ontology-floors` (or a sibling job gated identically); keep the ≥200-char `rdfs:comment` depth gate
(`run-foundation-checks.sh:148-149` idiom) over the folded algebra classes. **Probe:** delete a negative
fixture from the glob → runner RED (witnesses cannot go silent). **E1 / S1.**

### T-CLASSES — intensional record-class layer (the OWL the fold target lacks)
**Interfaces.** *Consumes:* `closure.ttl:153-192` (equation-record class = cardinality-1 on `left` AND
`right`; `category:identity` two-member reification), `closure.ttl:431-433` (`axiom:record owl:disjointWith
theorem:record`), the seed-carrier `…:family:seed:genus:registry:species:{axiom,theorem,specimen,datatype}:record`
classes; `shapes.ttl:11-17` (`ClassDeclarationShape`, the targetClass idiom to copy). *Produces:*
`records.ttl` — the algebra record CLASSES.
**Target files.** `basicttl/primordial/type/algebra/records.ttl`.
**RED.** Author a probe `probes/records_disjoint.rq` asserting `theory:record`, `model:record`,
`signature:record`, `equation:record` each exist as `owl:Class` with their cardinality restrictions and the
required `owl:disjointWith` pairs; run it before authoring → 0 rows / fail.
**GREEN.** Mint, in the seed-carrier record ladder (REUSE `closure.ttl`'s `specimen:record` as parent —
bridge-never-duplicate), the algebra record classes: `theory:record` (`owl:Restriction` cardinality-1 on
`@rel:signature` + minCardinality-1 on `@rel:equation` + parent `specimen:record`); `model:record`
(cardinality-1 on `@rel:carrier`, `@rel:operation`); `signature:record`; `equation:record` (cardinality-1
on `@rel:left` AND `@rel:right`, applying the `datatype:record` cardinality-restriction idiom
`closure.ttl:153-169` — the reference has NO `equation:record` class; `left`/`right` are instance triples
`:182-211`); `reduct:record`; REUSE `closure.ttl`'s
`axiom:record`/`theorem:record`/`certificate` verbatim as `rdf:type` targets. Assert
`axiom:record owl:disjointWith theorem:record` (theorem/axiom collapse = SHACL violation, design §2f).
Each class ≥200-char `rdfs:comment`. **Probe:** collapse `equation:record`'s max-1-`left` restriction →
`records_disjoint.rq` RED. **E2 / S2.**

### T-BRIDGE — the alias/bridge map (retire `fnd:` → full-ladder IRIs; keep SP1/SP2/SP3 resolvable)
**Interfaces.** *Consumes:* `algebra_spine.ttl` (the full `fnd:` inventory — rungs `:408-522`, signatures
`sigOneBinary/sigMonoid/sigGroup/sigQuasigroup/sigLoop`, equation-sets `eqsMagma..eqsLoop`, laws
`lawClosure/lawAssociativity/lawIdentity/lawCommutativity/lawInverse/lawLatinDivision`, carriers
`carrierMagma..carrierLoop`, reified-table vocab `addsLaw/hasSignature/hasEquationSet/hasCarrier/satisfiesLaw/
hasIdentityElement`); the engine anchors (`primordials.yaml:394-487`); `closure.ttl` `ns3457:legacy`
seed-bridge idiom; SP2 `aob:SealedGroup rdfs:subClassOf fnd:Group`. *Produces:* `bridges.ttl` — the
exhaustive alias table + engine/seed/primordial-root bridges + `owl:differentFrom` witnesses.
**Target files.** `basicttl/primordial/type/algebra/bridges.ttl`.
**RED.** Probe `probes/aliases_resolve.rq`: for every `fnd:` rung/signature/equation-set/law/carrier name,
assert a bridge edge exists to the corresponding full-ladder IRI; and assert `aob:SealedGroup
rdfs:subClassOf`-reaches the group model class through the map. Run before authoring → RED.
**GREEN.** Author, per design §5.1–5.2: `<full-ladder-IRI> skos:exactMatch fnd:X` for Group (engine
exactMatch); `seed:conservativeBridge` for AlgebraicStructure/Magma/Semigroup/Monoid (to the engine group
type/axiom atoms — quote the `[V]` engine IRIs verbatim); honest-red BUILD (no engine edge, proof-status
`asserted`/`literature:backed`) for CommutativeMonoid/AbelianGroup/Quasigroup/Loop; `seed:implementationBridge`
for carriers. Bridge every `fnd:` local name with `skos:exactMatch`/`rdfs:subClassOf`/`owl:equivalentProperty`
+ a `urn:silmaril:seed:…` legacy edge (ADDITIVE — Stage 1 only adds these edges; the actual stub-reduction
of `algebra_spine.ttl` + the inbound `fnd:*` edge REDIRECT is the B3(a) true-full-retire done in T-RETIRE,
Stage 2, once the whole tower exists); bridge the primordial short root via `schema:seeAlso` (never adopt it
as grammar). Demote reified-table WITNESS vocab to `fixtures/` and re-express its predicates as `@rel:*` with
`owl:equivalentProperty`/`rdfs:subPropertyOf` bridges to `closure.ttl` `ns3:*` (predicate-unification, design
§7.2 obligation 2 — avoids a silent fork). Add `Byte ≠ Octet` `owl:differentFrom` witness (engine OCTET WIDTH
AXIOM `primordials.yaml:341-346`) + a forbidding tooth + a negative fixture. Flag the `[S]` tokens (side
segment placement, `order:nullary`, reduct tokens, quasigroup latin-division, `genus:algebraic`, extension
`genus:obligation`, equation-identity choice) for §7.2 sign-off in an `rdfs:comment` block. **Probe:** drop
the Group `skos:exactMatch` → `aliases_resolve.rq` RED (SP2 `SealedGroup` no longer resolves). **E3 / S3.**

### T-SIG-OP — shared signature + operation-symbol atoms
**Interfaces.** *Consumes:* `algebra_spine.ttl:183-195` (`sigOneBinary`, `sigMonoid`, `sigGroup` operation
symbols verbatim); design §1.7 (signatures), §1.8 (operation-symbols). *Produces:* `signatures.ttl`,
`operations.ttl`.
**Target files.** `basicttl/primordial/type/algebra/signatures.ttl`, `.../operations.ttl`.
**RED.** Probe `probes/signature_names_sort.rq`: every theory-to-be names a signature that names its
operation symbols with declared arities; run before authoring → RED.
**GREEN.** Mint the five shared signature atoms (design §1.7, `kingdom:definition:phylum:specification:
class:signature:order:<profile>:family:operation:genus:algebraic[S]:species:signature:component:definition:
instance:canonical`): sigOneBinary (Σ={·}, magma+semigroup), sigMonoid (Σ={·,e}), sigGroup (Σ={·,e,inv}),
sigQuasigroup (Σ={·,\,/}), sigLoop (Σ={·,\,/,e}). Mint the operation-symbol atoms (design §1.8,
`kingdom:operation:phylum:primitive:class:<op>:order:<arity>:family:operation:genus:<role>:species:<op>:
component:operation:instance:canonical`): product `·` (binary, `genus:composition:species:product`), unit
`e` (`order:nullary`[S] fallback `order:constant`, `genus:neutral:species:identity`), inverse `inv`
(unary, `genus:member:species:inverse`), `\` (binary, `genus:left:species:division`), `/` (binary,
`genus:right:species:division`). Carry `@rel:arity`, `@rel:domain`, `@rel:codomain` (sort = carrier).
**Probe:** strip sigMonoid's unit symbol → `signature_names_sort.rq` RED for the monoid theory. **E4 / S4.**

### T-PROG — the agnostic progenitor theory-root (grounds nothing)
**Interfaces.** *Consumes:* `algebra_spine.ttl:408-411` (`fnd:AlgebraicStructure` grounds-nothing shape,
verified); `primordials.yaml:394-404` (engine `TYPE/ALGEBRA` root, `ABSTRACT true`); design §1.3, §3.
*Produces:* the progenitor record in `spine/progenitor.ttl`.
**Target files.** `basicttl/primordial/type/algebra/spine/progenitor.ttl`.
**RED.** Probe `probes/progenitor_grounds_nothing.rq`: the progenitor carries NO `@rel:signature`, NO
`@rel:addsLaw`, NO `@rel:carrier`, and is NOT a model class; run against an intentionally-over-specified
draft (give the progenitor a signature) → the tooth bites (RED), proving the constraint.
**GREEN.** Mint the progenitor `[V]` (design §1.3): `HEAD` +
`primordial:kingdom:type:phylum:algebra:class:structure:order:axiomatic:family:primordial:genus:algebra:
species:root:component:type:instance:canonical`, ABSTRACT, grounds nothing; magma `rdfs:subClassOf` it;
every other rung reaches it transitively via reduct edges. Bridge `seed:conservativeBridge` to the engine
`TYPE/ALGEBRA` root; `skos:exactMatch fnd:AlgebraicStructure`. Add `AlgebraProgenitorShape` clause: a
progenitor carrying any `@rel:signature`/`@rel:addsLaw`/`@rel:carrier` → RED (re-homes `algebra_spine.ttl:411`
constraint A). **Probe:** the RED draft above; remove the offending edge → GREEN. **E5 / S5.**

### T-MONOID — the fully-worked exemplar rung (END-TO-END) — **MAINTAINER SIGN-OFF GATE**
> The design's §2 worked template. On acceptance of the *realized* monoid rung the maintainer signs off
> the pattern (design §7.3); only then do the sibling rungs (T-MAGMA…T-LOOP) fan out.
**Interfaces.** *Consumes:* T-CLASSES record classes, T-SIG-OP sigMonoid + product/unit, T-PROG progenitor,
T-BRIDGE map; `closure.ttl:129-142` (Yoneda theorem+certificate idiom), `:185-192` (two-member identity
reification); `algebra_spine.ttl:441` (fnd:Monoid, DS-lifted rung). *Produces:* the monoid theory/model/
axioms/equations/theorem/certificate + declaration triad + fixtures + bridges in `spine/monoid.ttl` (+
equation records into `equations.ttl`).
**Target files.** `spine/monoid.ttl`, `equations.ttl` (monoid block), `fixtures/monoid_z2.ttl`,
`fixtures/monoid_z2_negative.ttl`, `shapes/algebra.shapes.ttl` (TheoryShape/ModelShape/EquationRecordShape
first authored here), `probes/monoid_identity.rq`.
**RED.** Author `fixtures/monoid_z2_negative.ttl` = Z/2 under + with a **broken identity row** (e·x ≠ x),
plus `probes/monoid_identity.rq` (for every structure with `@rel:identity:element` e, no reified op row with
e on the left may have result ≠ its right operand, mirroring `algebra_spine.ttl` `q_monoid_identity`). Run
the negative fixture against the shape/probe → conforms=false / rows>0 (RED = tooth bites).
**GREEN.** Mint the complete monoid atom set (design §2 "MONOID rung assembly"): 1 theory record
(`kingdom:definition:phylum:algebra:class:theory:order:declarative:family:monoid:genus:presented:species:
monoid:component:definition:instance:canonical`[S]) naming sigMonoid + its equations + reduct→semigroup +
`@rel:validation:mode "rewrite"` + `@rel:proof:status "literature:backed"` + provenance quartet +
`@rel:authority "DS"` + historical-identity bridges; 1 signature ref; 3 axiom records (closure/assoc/
identity, `family:monoid` off the `[V]` group rank values); the identity split into TWO equation records
(`…species:member:left`/`…:member:right`[S], `closure.ttl:185-192` precedent) + associativity = ONE equation;
1 model class (carrier + identity:element cardinality-1, `owl:disjointWith` the group model); 1 theorem
(identity-uniqueness) + certificate (digest + proof-method, NEVER an axiom); the Declaration/Denotatum/Gate
triad; `fixtures/monoid_z2.ttl` (positive, `finite:checked`); 3 bridges. **Continuity (no silent drop):**
the `q_monoid_is_endo` / `fnd:MonoidIsEndoShape` / `fnd:endoMonoidWitness` "monoid = one-object category"
tooth (`algebra_spine.ttl:445`) is a Pillar-4 category SEAM, outside the one-operation spine — it is
**explicitly DEFERRED to the category fan-out** (recorded here + in design §7.4 so the exemplar rung does
not appear to lose it). **Probe:** remove one identity case → the two-sided (obligation-count 2) tooth
(T-REDUCT) will RED; the broken-row negative already REDs. On GREEN + sign-off, the pattern is locked.
**E6 / S6.**

### T-MAGMA — magma rung (after sign-off)
**Interfaces.** *Consumes:* T-MONOID template, sigOneBinary, closure axiom `[D]`. *Produces:* `spine/magma.ttl`,
magma equations, `fixtures/magma_*`, MagmaShape focus.
**Target files.** `spine/magma.ttl`, `equations.ttl` (magma block), `fixtures/magma_pos.ttl`,
`fixtures/magma_neg.ttl`, `probes/magma_closure.rq`.
**RED.** `fixtures/magma_neg.ttl` = a binary table whose product escapes the carrier (closure violation);
`probes/magma_closure.rq` bites → RED.
**GREEN.** theory (family:magma, sigOneBinary, E={closure}) + closure axiom `[D]` (`HEAD` +
`magma:kingdom:axiom:phylum:operation:class:closure:order:binary:family:magma:genus:product:species:
membership:component:statement:instance:canonical`) + model class + reduct? (magma `rdfs:subClassOf`
progenitor — NOT a reduct, design §1.9) + positive fixture + bridge (`seed:conservativeBridge` to engine
group closure axiom). Re-home the master magma-totality tooth BOTH as an intensional theory-law record AND
a probe+fixture (design §6, D25 no-regression). **E7 / S7 (parallel with T-SEMI…T-LOOP).**

### T-SEMI — semigroup rung
**Interfaces.** *Consumes:* T-MONOID template, sigOneBinary, associativity axiom `[D]`. *Produces:*
`spine/semigroup.ttl`, semigroup equations, fixtures, SemigroupShape focus.
**Target files.** `spine/semigroup.ttl`, `equations.ttl` (semigroup block), `fixtures/semigroup_pos.ttl`,
`fixtures/semigroup_neg.ttl`, `probes/semigroup_assoc.rq`.
**RED.** `fixtures/semigroup_neg.ttl` = a non-associative table `(x·y)·z ≠ x·(y·z)`; `semigroup_assoc.rq`
bites → RED.
**GREEN.** theory (family:semigroup, sigOneBinary, adds associativity) + associativity axiom `[D]`
(`class:associativity:…:family:semigroup:genus:composition:species:equality`, off the `[V]` group value) +
associativity = ONE equation + model + reduct edge semigroup→magma (obligation-count 1) + positive fixture +
`seed:conservativeBridge` to engine associativity axiom. **E8 / S8 (parallel).**

### T-CMON — commutative-monoid rung
**Interfaces.** *Consumes:* T-MONOID template, sigMonoid, commutativity axiom `[D]`. *Produces:*
`spine/commutative_monoid.ttl`, fixtures, CommMonoidShape focus.
**Target files.** `spine/commutative_monoid.ttl`, `equations.ttl` (cmon block), `fixtures/commutative_monoid_pos.ttl`,
`fixtures/commutative_monoid_neg.ttl`, `probes/commmonoid_comm.rq`.
**RED.** `fixtures/commutative_monoid_neg.ttl` = a monoid table with `a·b ≠ b·a`; `commmonoid_comm.rq`
bites → RED.
**GREEN.** theory (subdomain `commutative:monoid`, compound order LOCKED §7.2 #9; sigMonoid; adds
commutativity) + commutativity axiom `[D]` (`subdomain commutative:monoid:…:class:commutativity:…:family:
commutative:monoid:genus:composition:species:equality`) + one equation + model (`owl:disjointWith`
non-comm siblings) + reduct
edge commutative-monoid→monoid (obligation-count 1) + fixtures. **NO engine anchor** → honest-red BUILD,
proof-status `literature:backed`, NOT `finite:checked`-from-engine. **E9 / S9 (parallel).**

### T-GROUP — group rung (the engine exactMatch anchor)
**Interfaces.** *Consumes:* T-MONOID template, sigGroup, inverse axiom `[V]`; `primordials.yaml:456-487`
(engine GROUP + `group::validate`); the 4 `[V]` group axioms quoted in design §1.5. *Produces:*
`spine/group.ttl`, group equations, fixtures, GroupShape focus.
**Target files.** `spine/group.ttl`, `equations.ttl` (group block), `fixtures/group_z3.ttl`,
`fixtures/group_z3_negative.ttl`, `probes/group_inverse.rq`.
**RED.** `fixtures/group_z3_negative.ttl` = Z/3 with a missing/invalid inverse for one element;
`group_inverse.rq` (∃ y: x·y=e AND y·x=e) bites → RED.
**GREEN.** theory (family:group, sigGroup, adds inverse) quoting the four `[V]` group axiom IRIs VERBATIM
(closure/assoc/identity/inverse) as anchors; inverse split into TWO equation records
(`…species:inverse:left`/`…:inverse:right`[S]); model class (`owl:disjointWith` monoid model); reduct edge
group→monoid (obligation-count 1, inverse discharges 2 equations); positive fixture Z/3 (`finite:checked`,
validation-mode `finite:table`); `skos:exactMatch` to the engine group type (`primordials.yaml:441`).
**Probe:** the Z/3 negative REDs; drop one inverse case → the two-sided obligation-count-2 morphism REDs.
**E10 / S10 (parallel).**

### T-ABEL — abelian-group rung
**Interfaces.** *Consumes:* T-GROUP, sigGroup, commutativity axiom (own atom, off group). *Produces:*
`spine/abelian_group.ttl`, fixtures, AbelianShape focus.
**Target files.** `spine/abelian_group.ttl`, `equations.ttl` (abelian block), `fixtures/abelian_group_pos.ttl`,
`fixtures/abelian_group_neg.ttl`, `probes/abelian_comm.rq`.
**RED.** `fixtures/abelian_group_neg.ttl` = a non-commutative group table (e.g. S_3 fragment);
`abelian_comm.rq` bites → RED.
**GREEN.** theory (subdomain `abelian:group`, compound order LOCKED §7.2 #9; sigGroup; adds commutativity
as its OWN atom `…subdomain abelian:group:…:class:commutativity:…:family:abelian:group:genus:composition:
species:equality` — no-cram, NOT reusing the monoid commutativity atom); one equation; model
(`owl:disjointWith` group model);
reduct edge abelian→group (obligation-count 1); fixtures. **NO engine anchor** → honest-red BUILD,
`literature:backed`. **E11 / S11 (parallel).**

### T-QGRP — quasigroup rung (division sub-family off magma)
**Interfaces.** *Consumes:* T-MAGMA, sigQuasigroup, latin-division law `[S]`. *Produces:*
`spine/quasigroup.ttl`, fixtures, QuasigroupShape focus.
**Target files.** `spine/quasigroup.ttl`, `equations.ttl` (quasigroup block), `fixtures/quasigroup_pos.ttl`,
`fixtures/quasigroup_neg.ttl`, `probes/quasigroup_division.rq`.
**RED.** `fixtures/quasigroup_neg.ttl` = a table failing unique left/right division (a Latin-square
violation); `quasigroup_division.rq` bites → RED.
**GREEN.** theory (family:quasigroup, sigQuasigroup {·,\,/}, E={closure, latin-division}) + latin-division
axiom `[S]` (`class:division:…:family:quasigroup:genus:latin:species:unique` — `genus:latin`/`species:unique`
unattested → §7.2 sign-off) + equations + model + reduct edge quasigroup→magma (obligation-count 1) +
fixtures. **NO engine anchor** → honest-red BUILD, `literature:backed`. **E12 / S12 (parallel).**

### T-LOOP — loop rung (quasigroup + identity)
**Interfaces.** *Consumes:* T-QGRP, sigLoop, identity law (own atom). *Produces:* `spine/loop.ttl`,
fixtures, LoopShape focus.
**Target files.** `spine/loop.ttl`, `equations.ttl` (loop block), `fixtures/loop_pos.ttl`,
`fixtures/loop_neg.ttl`, `probes/loop_identity.rq`.
**RED.** `fixtures/loop_neg.ttl` = a quasigroup table with no two-sided identity; `loop_identity.rq` bites → RED.
**GREEN.** theory (family:loop, sigLoop {·,\,/,e}, adds identity) + identity as its OWN atom split into TWO
equation records (`…family:loop:genus:neutral:species:member:left`/`:right`[S]) + model + reduct edge
loop→quasigroup (obligation-count 1, identity discharges 2 equations) + fixtures. **NO engine anchor** →
honest-red BUILD, `literature:backed`. **E13 / S13 (parallel).**

### T-REDUCT — theory-morphism / forgetful reduct edges + obligation-counting morphisms
**Interfaces.** *Consumes:* all 8 rung theories; design §1.6 (two-sided = 2 equations + obligation-counting
extension morphism), §1.9 (reduct edges), §3 (one-law=one-obligation). *Produces:* `reducts.ttl`.
**Target files.** `basicttl/primordial/type/algebra/reducts.ttl`, `probes/obligation_count.rq`,
`probes/one_law_per_rung.rq`.
**RED.** `probes/one_law_per_rung.rq` (each concrete rung adds EXACTLY ONE law over its parent — re-homes
`algebra_spine.ttl:99-103` constraints B no-cram + C at-least-one) and `probes/obligation_count.rq` (a rung
that declares only ONE side of a two-sided law → RED). Author a draft with monoid declaring only
identity-left → `obligation_count.rq` bites → RED.
**GREEN.** Mint the reduct edges (`kingdom:mapping:phylum:composition:class:reduct:order:forgetful[S]:family:
morphism:genus:theory[S]:species:<child>:to:<parent>:component:definition:instance:canonical`): semigroup→magma,
monoid→semigroup, commutative-monoid→monoid, group→monoid, abelian→group, quasigroup→magma, loop→quasigroup
(magma→progenitor is `rdfs:subClassOf`, NOT a reduct). Each reduct carries an obligation count; the two-sided
laws (monoid identity, group inverse, loop identity) carry an obligation-counting **extension morphism**
(`class:extension:…:genus:obligation:species:count:two`[S], design §1.6). `order:forgetful`/`genus:theory`/
`genus:obligation`/`species:count:two` are `[S]` → §7.2 sign-off. **Probe:** the RED draft above; restore
both sides → GREEN. **E14 / S14.**

### T-SHAPES — the full SHACL tooth set (targetClass, one pair per record class)
**Interfaces.** *Consumes:* `shapes.ttl:11-17` (`ClassDeclarationShape` = the min1/max1 coordinate-separation
targetClass idiom to COPY) vs `shapes.ttl:169-177` (`ByteWidthShape`/`OctetOrdinalShape` targetNode = the
anti-pattern the algebra subtree must NOT copy) + `:276-282` (`IdentitySeparationShape` = the `sh:sparql`
non-vacuity/identity-collision idiom); `closure.ttl` 4 targetClass / 0 targetNode, `consolidated.shacl.ttl`
33 targetClass / 0 targetNode + its gate-uniqueness `sh:select`; the fold tree's SHACL prefix labels
(`constraint:`/`model:` = `urn:silmaril:primordial:type:`, `shapes.ttl:1-3` — same IRIs as `sh:`, author
against the actual labels). *Produces:* the complete `shapes/algebra.shapes.ttl`.
**Target files.** `basicttl/primordial/type/algebra/shapes/algebra.shapes.ttl`.
**RED.** Each shape authored against a purpose-built negative fixture (from the rung tasks + T-FIX) that
must flip conforms True→False; before the shape is authored the probe is unexercised (0-focus → REJECT under
T-INFRA's inverted logic).
**GREEN.** Author, ALL with `sh:targetClass` (NEVER `sh:targetNode`), each = (i) min1/max1 property shapes +
(ii) a `sh:sparql` non-vacuity/identity-collision clause: **TheoryShape** (names S/Ω/E), **ModelShape**,
**ReductShape**, **EquationRecordShape** (two-sided = 2 records), **CarrierGroundingShape**, **ProofStatusShape**
(8-value enum), **ValidationModeShape** (4-value enum), **ProvenanceShape**, **BridgeShape**,
**DifferentFromWitnessShape** (Byte≠Octet, model-disjointness), plus **AlgebraProgenitorShape** (grounds
nothing), and the V1 hygiene shape (REFINED, design §4/§7.5: forbid the DENOTATUM/domain-class pun — fix
the `frame.ttl:7` `a owl:Class, model:Product, model:Frame` conflation — and forbid provenance on a
DENOTATUM; but PERMIT a declaration-record that is an `owl:Class` carrying provenance, i.e. the B4
model-record — legal OWL2 metaclass punning, EXEMPT). Theorem/axiom
collapse = a violation (reuse `records.ttl` disjointness). Each shape gets a fixture pair in T-FIX. **Probe:**
switch any shape to `sh:targetNode` on a singleton → its rung's focus set drops to 0 → T-INFRA 0-focus gate
REDs. **E15 / S15.**

### T-FIX — fixtures: 1 positive + 1 failing negative per shape + empty control + finite-table certs
**Interfaces.** *Consumes:* T-SHAPES shape list; `refcomp/zip/silmaril/reports/independent/`
(positive.ttl + negative.01..28.ttl + `validation.log:34` `empty ⇒ REJECT` idiom); `algebra.sh`
`group::validate` Cayley tables. *Produces:* the complete `fixtures/` tree.
**Target files.** `basicttl/primordial/type/algebra/fixtures/**` (per-shape positive+negative already seeded
by the rung tasks; here completed for the record-class shapes without a natural rung home: ProvenanceShape,
BridgeShape, ProofStatusShape, ValidationModeShape, DifferentFromWitnessShape), `fixtures/empty.ttl`,
`fixtures/monoid_z2_cayley.ttl`, `fixtures/group_z3_cayley.ttl` (+ their non-total/assoc-violating negatives).
**RED.** Every negative fixture must, on injection, flip its shape conforms=false / probe rows>0; assert this
in the runner (T-INFRA step (b)). A negative that fails to flip → runner RED.
**GREEN.** One positive (`conforms=true, results=0`) + one failing negative (single-violation injection onto
an otherwise-conformant graph) per shape; ONE `empty.ttl` control asserting `empty ⇒ admission=REJECT`; the
reified Cayley tables as `finite:checked` certificate fixtures (Z/2, Z/3 carrying proof-status
`finite:checked` + validation-mode `finite:table`) + matching non-total/associativity-violating negatives.
All witnesses live UNDER `fixtures/` (outside the ontology data glob — four-planes, design §2e). **Probe:**
weaken a negative to conform → runner RED. **E16 / S16.**

### T-GATES — gates V0–V8 wiring (recognised under the reference's own vocabulary)
**Interfaces.** *Consumes:* `consolidated.shacl.ttl` gate ladder
(`…:core:entity:structure:class:gate:specification` + gate-identity `sh:select` + clause-identity twin);
design §4 V0–V8 crosswalk. *Produces:* the gate/clause spec records + probes; the runner's per-gate assertions.
**Target files.** `basicttl/primordial/type/algebra/gates/gates.ttl`, `.../probes/*.rq`, EDIT
`run-algebra-checks.sh` (per-gate assertions).
**RED.** For each gate a probe that fails until the gate is wired: V0 (Turtle parse), V1 (REFINED §4/§7.5:
denotatum/domain-class pun forbidden — fails on the `frame.ttl:7` pattern — + provenance-on-denotatum
forbidden; declaration-record owl:Class-with-provenance EXEMPT), V2 (`empty ⇒ REJECT`
+ 0-focus REJECT), V3 (`sh:sparql` clauses present), V5 (every model names theory+carrier+operations+laws+a
declared validation MODE), V6 (`N_manifest == N_materialized`), V8 (SHACL-2017 discipline). V4 (Yoneda-density)
and V7 (dual provenance) are wired minimally here / fully in T-PROV.
**GREEN.** Model gates AS `owl:Class` under the reference gate ladder (two-ladder ruling: algebra rungs on the
mathematics ladder, gate/clause specs on the `core:entity` ladder — both verbatim from the reference) with the
gate-identity uniqueness `sh:select` tooth + clause-identity twin. Wire every V0–V8 assertion into
`run-algebra-checks.sh`. V5 = the algebraic-law probe over all 8 rungs. **Probe:** strip a model's
validation-mode → V5 RED; add a second gate with a duplicate identifier → gate-identity RED. **E17 / S17.**

### T-MANIFEST — deep-KV manifests + DAG node + count self-checks
**Interfaces.** *Consumes:* `run-foundation-checks.sh:157-361` (register/count self-check idiom, DERIVED
counts); `basicttl/dag/dag_instances.ttl` (`phase_w2_sp0` node pattern); the engine Flavor-B AOB envelope
(`EVIDENCE:SOURCE:…:LINE`, `GROUNDING:CARRIER`, `PROVENANCE:STATE`, `GAPS`, `RECEIPT`). *Produces:*
`manifests/*.yaml`, a new DAG node, count self-checks in the runner.
**Target files.** `basicttl/primordial/type/algebra/manifests/spine.yaml` (+ per-rung), EDIT
`basicttl/dag/dag_instances.ttl` (add `phase_w2_sp0_fold` node), EDIT `run-algebra-checks.sh` (count
self-check step).
**RED.** Author the count self-check to recompute every figure (theory/model/axiom/equation/reduct/shape/
fixture counts) from disk and assert `== manifest == DAG node`; perturb a manifest figure → RED.
**GREEN.** Manifests in the Flavor-B envelope with DERIVED counts (never hard-coded); a `phase_w2_sp0_fold`
DAG node narrating the shape/probe/rung figures; the runner's self-check gates disk==manifest==DAG. **Probe:**
edit the DAG node's stated shape count → runner RED; restore → GREEN. **E18 / S18.**

### T-PROV — V7 provenance closure lane (executor ≥1 AND shadow ≥1) — BUILD FROM SCRATCH
**Interfaces.** *Consumes:* design §4 (V7 GAP — reference `governance/` is empty, only one-sided PROV
exists); D24 lane lifecycle Draft→ExecutorValidation→ShadowCritique→Resolution→ShadowRevalidation→Accepted;
`commit_signing_trust.ttl`. *Produces:* the review-lane records + the V7 tooth.
**Target files.** `basicttl/primordial/type/algebra/reviews/{executor,shadow,resolved}/`,
`.../receipts/`, `probes/provenance_closure.rq`, EDIT `run-algebra-checks.sh` (V7 assertion).
**RED.** `probes/provenance_closure.rq`: every reshaped RECORD carries `prov:wasAttributedTo` an executor
≥1 AND a shadow ≥1 (both counts), plus `prov:wasGeneratedBy`; run before the shadow half exists → RED.
**GREEN.** Author the executor + tandem-shadow review records per task (this plan's E#/S# assignments), the
resolution records, and receipts; wire the dual-count V7 tooth into the runner. Provenance on every RECORD,
never on a mathematical denotatum. **Probe:** remove a shadow attribution → V7 RED. **E19 / S19.**

### T-RETIRE — B3(a) TRUE FULL RETIRE of the `fnd:` tower (Stage 2, after all 8 rungs exist)
**Interfaces.** *Consumes:* the complete folded tower (all 8 rung denotatum + record atoms, T-BRIDGE map);
`basicttl/foundation/algebra_spine.ttl` (the `fnd:` tower to reduce); the inbound-edge sites — SP2
`basicttl/aob/*.ttl` (`aob:SealedGroup rdfs:subClassOf fnd:Group`, `group_law.ttl`), any SP1
`basicttl/primitives/*.ttl` / SP3 `basicttl/crs/*.ttl` `groundsIn*`/`subClassOf fnd:*` edges (enumerate by
grep before editing); `run-foundation-checks.sh` (merged-graph gate). *Produces:* `algebra_spine.ttl`
reduced to bridge stubs; inbound `fnd:*` references redirected to the new full-ladder IRIs.
**Target files.** `basicttl/foundation/algebra_spine.ttl` (EDIT — strip math content, keep each `fnd:` rung
as a stub `owl:equivalentClass`/`skos:exactMatch` → new IRI); the specific SP1/SP2/SP3 files carrying
inbound `fnd:*` edges (EDIT — redirect to the new IRIs). **This is the sanctioned override of the earlier
"SP1/SP2/SP3 byte-untouched" assumption (maintainer B3(a) lock); touch ONLY the `fnd:*` reference lines.**
**RED.** `probes/retire_no_orphan.rq` + `probes/no_duplicate_content.rq`: (i) no `fnd:` rung still asserts
math content (signature/addsLaw/equation/restriction) — TODO-11 one-place; (ii) every former inbound
`fnd:*` edge now reaches the new IRI (directly or via the surviving stub's `owl:equivalentClass`); (iii)
`aob:SealedGroup` is still a subclass of the group model in the merged graph. Run before the retire → RED
(content still duplicated).
**GREEN.** Reduce each `fnd:` rung in `algebra_spine.ttl` to a stub (identity + one bridge edge to its new
denotatum/record IRI, all math content removed); redirect each inbound `fnd:*` edge to the new IRI (or
leave it pointing at the now-stubbed `fnd:` name, whichever keeps the merged graph green — prefer explicit
redirect for the doctrinally-clean end-state). Re-run `run-foundation-checks.sh` over the merged
SP0+SP1+SP2+SP3 graph: MUST stay green, `aob:SealedGroup` MUST still resolve, no orphaned `fnd:*`
reference. **Probe:** delete a stub's bridge edge → `retire_no_orphan.rq` RED (SealedGroup dangles). **E20a
/ S20a.**

### T-INTEGRATION — full gate green + aliases resolve + CI coherent + commit signed
**Interfaces.** *Consumes:* every prior task; `run-foundation-checks.sh:49` (SP1+SP2+SP3 invariant chain);
`ci.yml`; `commit_signing_trust.ttl`. *Produces:* the green merged pass + the signed reshape commit.
**Target files.** none new (verification + commit only).
**RED.** Before integration, run `run-algebra-checks.sh` + `run-foundation-checks.sh` on the merged graph;
any 0-focus shape, any non-flipping negative, any unresolved `fnd:`/`aob:SealedGroup` reference, or any CI
step drift → RED.
**GREEN (acceptance, design §7.3).** ALL of: (1) V0–V8 pass NON-VACUOUSLY — every shape ≥1 focus node,
every negative fixture flips RED under injection, `empty ⇒ REJECT`; (2) `N_manifest == N_materialized`
recomputed from disk; (3) `aob:SealedGroup rdfs:subClassOf fnd:Group` STILL resolves through the alias map,
and every SP1/SP2/SP3 `groundsIn*`/`subClassOf fnd:*` inbound edge re-validates (merged SP0+SP1+SP2+SP3
graph green via `run-foundation-checks.sh` — now that T-INFRA step 0 extends its SP0 loader to include the
folded tree, so this is exercised in ONE graph, B2); (4) `ci.yml` is coherent — the new algebra runner step present,
the depth gate covers the folded classes, the provenance job green; (5) the reshape commit is signed under
the REPROVISIONED key `silm:signing_key_claude_2026b` (fp `B6F41C924ED120B6E42A7D5A2D292981114A752A`,
ed25519, `keys/claude-2026b.asc`, `silm:trust_policy_agent`; the original `silm:signing_key_claude_2026` /
fp `27044DC5…` was wiped by the reclaim and stays listed as attested) — `keys/trust-manifest.txt` is
GENERATED from the `.ttl` and already in sync. NOTE the provenance `policy-default` fails only on
`bad-signature`/`unknown` (unsigned passes), so a correctly `good`-signed reshape commit is the target and a
BAD signature is worse than none. **Probe:** corrupt the signature → the provenance job
(`ci.yml:109-119`, `fetch-depth:0`) REDs (`bad-signature`). **E20 / S20 (double-dip: validate ×2).**

### T-PANEL — adversarial triple panel (post-build gate)
**Interfaces.** *Consumes:* the whole realized spine; design §7.2 (the 8 token/scope sign-off decisions),
§7.3 (realized-spine acceptance). *Produces:* the panel verdict + the §7.2 sign-off packet.
**Target files.** `ledger/W2/sp0-reshape/panel/verdict.md` (panel output, NOT an ontology edit).
**RED.** The panel actively tries to break each tooth: inject a punning class, a `sh:targetNode` singleton, a
vacuous-conforming empty graph, a one-sided two-sided law, a duplicate gate identifier, an unsigned commit,
a stripped shadow attribution, a hard-coded count — each MUST turn a gate RED.
**GREEN.** Three adversarial reviewers (correctness / doctrine-conformance / naming-lock) each sign that:
the mint-more-than-runtime ruling holds; every `[V]` anchor is byte-verbatim off `aob/urn/**`; every `[S]`
token is in the §7.2 sign-off packet (side-segment placement, `order:nullary`, reduct tokens, latin-division,
`genus:algebraic`, extension `genus:obligation`, equation-identity choice, two-ladder split); no
placeholders; V0–V8 non-vacuous; the honesty ledger (DS/PD/SYN, engine-anchor vs honest-red BUILD) is clean.
The realized monoid rung + 7 siblings are the maintainer sign-off artifact (design §7.3) that authorizes the
Pass-2 fan-out. **E21 / S21 (panel of three).**

---

## Sign-off checkpoint carried into the build (design §7.2 — LOCK before minting)

The build is re-mint-expensive if any of these 8 change post-materialisation; each executor surfaces its
`[S]` uses in an `rdfs:comment` block and the PANEL task assembles the packet: (1) mint-more-than-runtime
[PIVOTAL]; (2) left/right side-segment placement (6 atoms + 2 extension morphisms); (3) `order:nullary`;
(4) reduct tokens `order:forgetful`+`genus:theory`; (5) quasigroup `genus:latin`+`species:unique`;
(6) signature `genus:algebraic` + extension `genus:obligation`/`species:count:two`; (7) equation-identity
(reuse axiom atom vs mint `component:equation`); (8) two-ladder split. **Tokens 1–8 ride at design defaults,
[S]-flagged, into the realized-spine sign-off packet (T-PANEL).** Three decisions are now **LOCKED by the
maintainer** and baked into this plan + design: **(9, B1) compound-token order = `abelian:group` /
`commutative:monoid`** (adjective-first, runtime-canonical); **(10, B4) model-class plane = TWO planes** —
`kingdom:type…component:type` = denotatum (Plane-2, no provenance), `kingdom:class…:model…component:class`
= declaration-record (Plane-1); **(B3) disposition = (a) TRUE FULL RETIRE** — the folded tower is
authoritative, `algebra_spine.ttl` `fnd:` rungs become bridge stubs AND inbound `fnd:*` edges (incl. SP2
`aob:SealedGroup`) are redirected to the new IRIs (Stage-2 retire task, after all rungs exist; merged-graph
green is the hard gate; overrides the prior SP1/SP2/SP3-byte-untouched working assumption). Plus two build
obligations: V7 provenance closure (T-PROV, BUILT from scratch) and predicate-unification (`@rel:*` ↔
`closure.ttl` `ns3:*` `owl:equivalentProperty`/`rdfs:subPropertyOf`, T-BRIDGE).
