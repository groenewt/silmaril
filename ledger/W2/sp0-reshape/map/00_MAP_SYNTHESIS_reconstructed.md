# MAP synthesis — RECONSTRUCTED from session context (2026-09-06 post-reclaim)

> The original 31-shard MAP (~10.6k lines) was lost to the reclaim. This is the actionable synthesis
> reconstructed from the completed-workflow results captured in session. Full evidence regenerable by
> re-running `scratchpad/sp0-reshape-map.js` + `-master.js`. Honest status: conclusions faithful;
> per-line evidence not re-materialized.

## 1. Floor violation inventory (fnd: floor vs Directive 24)
- **A0 punning:** 13 rungs typed `a owl:Class , fnd:PresentedAlgebra` (8 in `algebra_spine.ttl`
  :418,429,441,454,468,482,502,514; 5 in `algebra_rings.ttl` :482,505,530,564,577) — DESIGNED
  collapse; must split theory/model/element/proof.
- **Extensional density:** 486 individuals / 910 distinct names / 102 classes (D23's "~920" = the
  distinct-NAME count). `reanchor.ttl` worst at ~31.5:1; `spaces`/`functionality_epi` 44%/71%
  evidence-in-module. 133 Cayley cells + 35 `fnd:probe*` belong in `fixtures/`.
- **Absent doctrine:** 0 `prov:`, 0 `owl:imports`, 0 `rdfs:seeAlso`, 0 validation-mode, 0 proof-status,
  0 sameness-witness floor-wide; no `fixtures/` dir; 0 materialized negatives.
- **Naming:** 899/910 names uppercase, 60 underscore, 11 compliant. Exemplar: 0/1995 uppercase.
- **Gates:** runner has no V1(OWL-profile/punning), V2(non-vacuity), V4(Yoneda), V6(manifest-coverage),
  V7(provenance) gate; only `inference=rdfs`. `group_action.ttl` was untracked.

## 2. Exemplar template to MATCH (docs/research/anchor/map/, PASS 18 gates, 428 sources)
Suffix-minted per-plane IRIs; DeclarationRecord envelope; 14-field reified GateAssignment with
`gated:through` = an `owl:propertyChainAxiom`; `interpreted:by`/`modeled:within`; axiom/theorem/
certificate records with `depends:on` + `has:certificate` + proof-status + a `sh:sparql` theorem≠axiom
tooth; fixtures = 1 positive + failing negatives; probes in 3 forms (COUNT-equality / zero-row SELECT /
distinction ASK); SHACL targetClass on record classes, targetNode only for singletons; PROV-O receipts;
validate.py runs ~22 ordered invariants. GO BEYOND it: its 28 `alg:theory` records are label-only stubs
— the fnd: fold must carry real (S,Ω,E) individuals.

## 3. Bridge map (fnd: concept → BUILD | BRIDGE | SUPERSEDED)
- **SUPERSEDED-BY-master: ZERO.** Master added no algebra rung/theory; its fnd: delta strengthened 2
  teeth + hardened the aob gate. The 310-file `primordial:type` tree declares NONE of Magma…Field/
  GroupAction/Blotto and is itself extensional + punned (302 class↔metaclass puns, a 3rd CamelCase
  grammar) — so fnd: adopts the EXEMPLAR conventions and bridges to primordial at the primitive/source
  layer only (Directive 25 then folds INTO primordial, fixing its algebra-subtree flaws).
- **BUILD + BRIDGE:** spine `AlgebraicStructure→Magma→Semigroup→Monoid→Group` → bridge (skos:exactMatch/
  conservativeBridge) to prior `silmaril:kind:algebra:{structure,magma,semigroup,monoid,group}` + 14
  prior law individuals (`axiom:magma:closure`, `axiom:semigroup:associativity`, `axiom:monoid:{left,
  right}:identity`, `axiom:group:inverse`).
- **BUILD (no prior term):** CommutativeMonoid, AbelianGroup, Quasigroup, Loop, Semiring; Ring/Field/
  Module/VectorSpace (+ HOMONYM hazard vs engine `silmaril:ring:*`/record `field`/code `module`/data
  `Vector::Integer` → `owl:differentFrom` witness each); GroupAction/GSet + Blotto (both absent in both
  trees). Set = structural/ETCS (prior `kind:algebra:set` closeMatch only). Topology/Metric → bridge to
  prior `kind:algebra:{topology,geometry}`. Functionality/ArrowType/RosarchQueryFrame → implementation-
  bridge to `silmaril:type:Frame`; hold DISTINCT from primordial runtime `family:Frame`.
- **A+B coherence:** survived the rebase; master broke/duplicated nothing on the floor.

## 4. Maintainer design-gate decisions (2026-09-06) → Directive 25
- Root: **fold into `basicttl/primordial/type/**`** (not keep-fnd:-and-bridge).
- Cadence: **spine first** (algebra tower as template) → sign-off → fan out.
- Epistemology (D21): **in-scope** (fan-out, not deferred).
- Technical (delegated): 2 Equation records for two-sided laws; Blotto sub-lane under group-action;
  rename + `owl:differentFrom` for Ring/Field/Module/Vector; master's teeth re-homed intensional +
  fixtures; 29MB consolidated.ttl deferred to W4.
- CI lockstep mandatory (ci.yml `ontology-floors` glob + runner + gates move together;
  `commit_signing_trust.ttl` honored).

## 5. Continuity (preserved / re-expressed / superseded)
- PRESERVED: DS/PD/SYN honesty, class-general probe-injected teeth, universal-property existence+
  completeness, Curry-F pillar, Blotto correction, SP1-3 byte-untouched, master's strengthened teeth.
- RE-EXPRESSED: agnostic-progenitor → theory-root/model-root; one-law-per-child → one-Equation
  extension; authority-tag → proof-status + source-locator; names → lowercase colon-descent; free-
  algebra → Lawvere presentation; groundsIn* → seed bridges.
- SUPERSEDED: class↔theory punning; definition-by-comment; in-module witnesses; merged-graph runner;
  per-project design-gate cadence.
