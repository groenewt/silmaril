# Algebra-tower pillar — Helios source-of-truth findings (Directive 18 foundation gate)

> Präriehund honesty banner. This is a **brainstorming-gate RESEARCH note**, not an
> authoring artifact. It reports, with exact `file:line` evidence, what the authored
> Helios `srcy` corpus (git-ignored source-of-truth) actually PROVIDES toward the
> `magma → semigroup → monoid → group → abelian group` tower ("all in between" +
> rings/semirings), and precisely WHERE THE GAP is. Where the source does not author a
> rung, this note says **SYNTHESIZE** and refuses to force-fit a lift that is not there
> (Directive 1: lift, never invent; Directive 18: anchor on algebra grounded in set
> theory). I authored NOTHING in `basicttl/`. Assigned pillar papers read in full:
> `papers/26_adjunctions_free_graphs_governed_algebras/` and `papers/31_path_monoids/`
> (sections + the algebra-bearing chapters); plus a whole-corpus grep sweep for every
> tower term and full reads of the concentrated hits.

---

## 0. One-paragraph verdict (lift-vs-synthesize, brutally honest)

Helios authors **exactly one rung of the tower as a first-class, proved algebraic
structure: the MONOID** (free monoid, endomorphism monoid, endopath monoid, quotient
monoid, graded monoid, finitely-presented monoid — all with universal properties and
proved unit+associativity). It **names "semigroup" once, only as a boundary
counterexample**. It supplies the tower's *laws* (associativity, identity/unit,
commutativity-as-declared-congruence) as reusable, repeatedly-proved teeth. It supplies
the **generative engine** that can MINT any variety — the free⊣forgetful adjunction and
the *presented free algebra on a many-sorted signature-with-equations* theorem
(`F_E(X)=T_Σ(X)/≡_E`). But it **does NOT author Magma, Group, AbelianGroup, Quasigroup,
Loop, Ring, or Field as structures.** "Group"/"abelian group" appear only as an
*external* counterexample (the abelian⊂group inclusion that fails to preserve colimits).
"Semiring" appears only as a *valuation coefficient device* in optimization, never as an
axiomatized ring/semiring rung. **Net: ~1 rung lifted (Monoid), the rest SYNTHESIZE —
but synthesize *through the source's own free-algebra engine*, not by ad-hoc
hand-axiomatization.** The inverse law (Group) is the single tower axiom with **zero**
source basis in Helios.

---

## 1. What the source DEFINES / NAMES per rung, with `file:line`

### MONOID — LIFT (richly authored, proved)
The one fully-present rung. Multiple independent constructions, each with a universal
property or a proved law set:

- **Free monoid (ecosystem).** `helios/srcy/papers/07_the_canonical_question/chapters/05_free_construction_and_quotient/sections/03_ecosystem_free_monoid.tex:17-20`
  defines the carrier `E = Σ_E*`; `:22-24` element = finite word `σ₁:…:σ_n`, unit =
  empty word `ε`, product = total colon concatenation `u:v`. Theorem
  *"Ecosystem free-monoid universal property"* `:38-48`: `(E, :, ε)` is the free monoid
  on `Σ_E`; for every monoid `(M,⋆,e)` and map `g:Σ_E→M` there is a unique monoid
  homomorphism `ĝ:E→M`. Unit + associativity proved `:51-55`; existence/uniqueness
  `:57-71`; quotient-monoid inheritance under a declared congruence `:73-81`. Trace
  quotient `E/≡_I` (independent generators made to commute) `:214-256`.
- **Endopath monoid at an object.** `helios/srcy/papers/31_path_monoids/sections/01_thesis.tex:29-32`
  `M_X = Hom_{C31}(X,X)` under concatenation, identity path as unit.
  `helios/srcy/papers/31_path_monoids/chapters/02_path_monoid_at_an_object/sections/01_endopath_monoid_at_mittens.tex:6-9`
  `M_Mittens = Hom_P(Mittens,Mittens)`, empty path + composable loops, binary op =
  concatenation. Length grading `chapters/02_.../03_length_grading_and_noncommutativity.tex:8-10`:
  `|q∘p|=|q|+|p|`, identity length 0 → **monoid homomorphism to `(ℕ₀,+,0)`**.
- **Endomorphism monoid / "monoid = one-object category".**
  `helios/srcy/papers/21_ologs_and_typed_english/chapters/05_yoneda_for_typed_english/sections/04_monoid_monad_yoneda_binders.tex:2`
  `End_C(X)`; `:36-39` product = composition, unit = `id_X`; `:16-17` cites Joy of Cats
  defining "a monoid as a one-object category at lines 1001–1014".
- **Finite presentation of a monoid.** `helios/srcy/papers/31_path_monoids/chapters/04_quotients_to_finite_presentation/sections/04_finite_presentation_of_mittens_path_monoid.tex:8-11`
  `⟨E_Mittens | R_Mittens⟩` = quotient of the free monoid; `:23-27` one generator, no
  relations → infinite free monoid `{1,a,a²,…}` (finite presentation ≠ finite carrier).
- **Appendix-A notational entry (proved).** `helios/srcy/appendices/35_appendix_a_notational_summary/sections/00_content.tex:76-77`
  `H_F = End_R(F)`, product `g·h=g∘h`, unit `1_F`; `:133` "(H_F,∘,1_F) proved monoid";
  `:78` monad = "a monoid object in the endofunctor category under composition".
- **Shared macro.** `helios/srcy/shared/components/math/olog_yoneda_monoid_monad.tex:46-55`
  `LBHistoryMonoidLaw`: `H=Atom*`, `e=ε`, `⊗`=concat, associativity + two-sided unit.
- **Base whitepaper** section `base/00_whitepaper/sections/00_helios_foundation/02_ecosystem_free_monoid` (the foundation-level free-monoid statement; per `ledger/W2/helios/srcy_map.md:161`).

### SEMIGROUP — NAMED ONLY (synthesize the atom; the law is lifted)
Exactly one occurrence in the whole theory corpus, and it is a *boundary
counterexample*, not a definition:
- `helios/srcy/papers/21_ologs_and_typed_english/chapters/05_yoneda_for_typed_english/sections/04_monoid_monad_yoneda_binders.tex:138`
  — "Associativity without a unit gives only a semigroup, not a monoid."
The **associativity law itself is lifted** (proved for path concatenation
`helios/srcy/papers/31_path_monoids/chapters/01_quiver_free_path_category/sections/02_free_path_category_construction.tex:51-94`;
for colon product `.../07/.../03_ecosystem_free_monoid.tex:51-55`), but no Semigroup
*structure/atom* is authored.

### COMMUTATIVE MONOID — PARTIAL LIFT (instances present; atom synthesize)
- `(ℕ₀,+,0)` as a commutative-monoid grading target:
  `helios/srcy/papers/31_path_monoids/chapters/02_path_monoid_at_an_object/sections/03_length_grading_and_noncommutativity.tex:10`.
- `M_J = ℕ₀^J` coordinatewise addition + zero:
  `helios/srcy/papers/26_adjunctions_free_graphs_governed_algebras/chapters/10_resource_graded_lambda_blotto/sections/01_resource_graded_free_algebra.tex:8`.
- Commutativity as a *declared congruence* (trace monoid `E/≡_I`):
  `.../07/.../03_ecosystem_free_monoid.tex:222-232`.
- **Noncommutativity is the explicit default** (a warning, not a rung):
  `.../31/02/03_length_grading_and_noncommutativity.tex:12-15` (`ba ≠ ab` in the free
  path category; commutativity "can arise only after a relation explicitly identifies
  those words"). So commutativity is a *lifted law/congruence*, but CommutativeMonoid as
  a named tower node must be synthesized.

### MAGMA — SYNTHESIZE (absent by name; the substrate exists)
Zero occurrences of `magma` / `unital magma` in the theory (grep: only spec-atom
noise + `\path{...}` false-positives, no algebraic magma). The *substrate* exists as
the raw term algebra before laws: `T_Σ(X)` /
`helios/srcy/papers/26_adjunctions_free_graphs_governed_algebras/chapters/03_free_functor_on_graphs/sections/03_signature_equations_governed.tex:13-15`
(raw many-sorted syntax, no equations imposed). A free magma is exactly `T_Σ(X)` for a
single binary constructor `Σ={·}` with `E=∅` — reachable from the engine (§2), but the
**named Magma rung is not authored**.

### GROUP — SYNTHESIZE (absent as a structure; only an EXTERNAL counterexample)
No group is defined anywhere. The word appears as a *foreign counterexample* used to
break colimit preservation:
- `helios/srcy/papers/20_functorial_transport/chapters/09_colimit_preservation/sections/03_reflect_versus_preserve.tex:61` "The inclusion of abelian groups into groups…";
  `:65` "…abelianization, which is not an isomorphism"; `:81`, `:148` the abelian
  inclusion is "the standing refutation".
**The inverse/invertibility axiom is never defined for any ontology structure.**
(`invertible` hits everywhere are about *cocone-leg / comparison-map* invertibility,
e.g. `base/00_whitepaper/sections/02_mittens_anchor.tex:76-82`, `papers/20/09/...` — a
morphism-isomorphism question, NOT a group inverse law.) → Group has **zero source
basis in Helios**; it is pure synthesis.

### ABELIAN GROUP — SYNTHESIZE (only the vol-20 counterexample above). No definition.

### QUASIGROUP / LOOP (algebra sense) — SYNTHESIZE (fully absent)
Grep for `quasigroup` / `Moufang` / algebraic `loop`: **zero**. Every `loop` hit is a
Yoneda-loop or control-flow loop (e.g. `papers/05_granite_substrate/sections/02_yoneda_loop.tex`),
never a quasigroup-with-identity.

### SEMIRING — SYNTHESIZE the rung (valuation USE is lifted, not the axioms)
Present only as a *valuation coefficient object* for optimization, never axiomatized as
a two-operation ring/semiring tower rung:
- `helios/srcy/papers/32_optimization_rules/chapters/14_hyper00_intervention_evaluation_economics_protocol.tex:331,367,401,473,546` — "semiring planning", "Pareto-semiring planner", "Semiring coordinates".
- `helios/srcy/appendices/35_appendix_a_notational_summary/sections/00_content.tex:260-271`
  — `S` = "declared scalar or product algebra used to value rewrite histories";
  `J_S` = "semiring-linear functor from rewrite paths to kernels". Explicitly *does not*
  choose a universal semiring interpretation (`:271`).
- `helios/srcy/papers/18_presheaf_semantics/chapters/11_warranted_evidence_presheaf/05_integrated_projection_and_appendices.tex:822` "semiring histories".
No `+`/`×` distributivity axioms, no additive/multiplicative identities as structure.

### RING / FIELD / MODULE — SYNTHESIZE (absent as algebra)
No algebraic `ring`, `field` (only record-`field`), or `module` (only code-module).
Vector spaces appear only incidentally as "ambient vector spaces" in a sheaf-consistency
operator (`appendices/35_.../00_content.tex:504`) — not a defined `VectorSpace` rung.
(This bears on Directive 18's "space constructs" half → near-total synthesize; flagged
for the space pillar.)

---

## 2. The GENERATIVE ENGINE the source DOES author (this is the real lift)

The honest, faithful anchor is not any individual higher rung — it is the machinery that
*mints varieties*. Helios authors this fully; it is the progenitor-of-progenitors.

- **Free⊣forgetful adjunction, graph→governed-algebra.**
  `helios/srcy/papers/26_.../sections/01_thesis.tex:93-101` `L⊣R`,
  `Hom_GovAlg(LG,A) ≅ Hom_Graph(G,RA)`; unit/counit `η:1⇒RL`, `ε:LR⇒1` `:108-122`;
  transpose law `R(f̄)∘η_G=f` `:123-128`.
- **Presented free algebra on a many-sorted signature-with-equations** (THE variety
  engine). `helios/srcy/papers/26_.../chapters/03_free_functor_on_graphs/sections/03_signature_equations_governed.tex:31-42`
  Theorem: `F_E(X) = T_Σ(X)/≡_E` is the free `E`-algebra; unique `E`-homomorphism to
  every `E`-algebra. `≡_E` = least typed substitution congruence closed under every
  constructor (`:16-29`). Counterexample: a non-congruence quotient is not an algebra
  quotient (`:77-92`). **This is precisely how each tower rung should be minted: a rung
  = a signature `Σ` + an equation set `E`; the free-algebra/adjunction machinery already
  authored here generates it.** (Magma: `Σ={·}`, `E=∅`. Semigroup: `+`assoc. Monoid:
  `+`unit laws. Group: `+`inverse. Abelian: `+`commutativity. Semiring/Ring: two
  constructors + distributivity.)
- **Free object is certified one universal-property clause at a time.**
  `helios/srcy/papers/26_.../chapters/03_free_functor_on_graphs/sections/04_free_versus_path_monoid.tex:24-50`
  — six obligations checked separately (term formation, congruence, extension, equation
  compatibility, uniqueness, path-monoid countermodel). **This "add one law/clause at a
  time, never cram" discipline is the source's own justification for Directive 17's
  agnostic-progenitor + one-law-per-child tower shape.**
- **Free path category / free monoid via `Path⊣U`.**
  `helios/srcy/papers/31_.../chapters/04_quotients_to_finite_presentation/sections/03_free_forgetful_adjunction_to_cat.tex:6-29`
  `Path:Graph→Cat ⊣ U:Cat→Graph`; universal property; quotient by relations `R` via
  `π_R`. (A path monoid = free category on a one-object quiver;
  `helios/srcy/papers/26_.../chapters/03_.../04_free_versus_path_monoid.tex:5-13`
  — path monoid only in the one-object case.)
- **Induced monad `T=RL`** from the adjunction:
  `helios/srcy/papers/26_.../chapters/06_kleisli_eilenberg_moore/sections/01_induced_monad.tex:6-10`
  (`μ=RεL`; monad laws from triangle identities). Monad = monoid object in `[C,C]`
  (appendix A above) — ties the monad layer back to the monoid rung.
- **Free structural interpretation (initial-algebra semantics).**
  `helios/srcy/papers/26_.../sections/08_lambda_blotto_free_term_engine.tex:24-44`
  (unique homomorphism `f̂:T_Σλ(X)→A` for every `Σλ`-algebra) and the shared
  `LBFreeMonadUniversalLaw` `helios/srcy/shared/components/math/olog_yoneda_monoid_monad.tex:193-213`.

**Caveat on "governed algebra".** The source's `GovAlg` object is NOT a classical
algebraic structure. `helios/srcy/papers/26_.../chapters/04_governed_algebra_category/sections/01_governed_algebra_definition.tex:6-13`
defines it as the 6-tuple `(A, op, E, V, ℓ, P)` = carrier + operation-interpretation +
satisfied-equations + admission-predicate `V` + lineage `ℓ` + profile `P`. Morphisms
preserve all six coordinates (`chapters/04/sections/02_morphisms_in_GovAlg.tex:5-9`).
So "algebra" in Helios already means *governed* algebra (algebra + validation +
provenance + interface), which is exactly the shape the foundation floor wants the tower
rungs to inhabit — but it is a wrapper, not itself a magma/group.

---

## 3. Maintainer's worked-example patterns that ARE algebra-relevant

- **byte_order agnostic progenitor** (Directive 17's template; from the spec-atom mirror,
  per `ledger/W2/helios/srcy_map.md:268-276`): `byte_order` grounds nothing, children
  `byte_order_{little,big,host,none}` compose under it via `ancestry.via`. **Directly the
  shape the algebra tower should take**: an agnostic `AlgebraicStructure` progenitor
  grounding nothing, each rung a composable child adding exactly one law.
- **Grading, not quotient** (Lambda-Blotto). The free term algebra receives a *grade* by
  a monoid homomorphism into `M_J=ℕ₀^J`, and the grade descends to a quotient ONLY after
  proving cost-preservation `t≡u ⇒ c(t)=c(u)`:
  `helios/srcy/papers/26_.../chapters/10_resource_graded_lambda_blotto/sections/01_resource_graded_free_algebra.tex:74-93`.
  Algebra-relevance: shows the corpus already uses commutative-monoid gradings and the
  congruence-compatibility discipline the tower's quotient rungs will need.
- **Length homomorphism** `|·|: M_X → (ℕ₀,+,0)` (`31/02/03:8-10`) — a worked
  monoid-homomorphism-into-a-commutative-monoid, the exact arrow-shape between two tower
  rungs.

---

## 4. The existing committed floor this tower will re-anchor (SP2), for context

Not authored by me; noted so the maintainer sees the lift-vs-synthesize collision.
`basicttl/aob/` already **synthesized a group in TTL** — it is NOT lifted from Helios:
- `basicttl/aob/aob.queries.sparql:286-317` `q_group_law`: "the sealed group of an atom +
  its companions is a group (identity/compose/inverse)"; `aob:SealedGroup`,
  `aob:groupIdentity` (the BASE atom is the identity), `aob:companionAtom`,
  `aob:composesOnto` (associative), `aob:retracts` (inverse / self-retract as the
  defect witness) `:298-311`; reified `aob:Composition` + `aob:GroupAssociativityShape`
  `:332-342`; data in `basicttl/aob/group_law.ttl` (per `basicttl/crs/checks/run-crs-checks.sh:63`).
Directive 18 asserts "SP2's `group_law` sealed group IS a group in this hierarchy." True —
but **it was invented for the AOB seal, not lifted** (Helios authors no group). So the
foundation's Group rung and SP2's `aob:SealedGroup` are two synthesized things that must
be reconciled at re-anchor time (see Decision D3).

---

## 5. Design DECISIONS this pillar raises for the maintainer

- **D1 — Anchor the whole tower on the Vol-26 presented-free-algebra engine, not on
  hand-axiomatized rungs.** The source authors *"a variety = (signature Σ, equations E),
  minted by `F_E(X)=T_Σ(X)/≡_E` + the free⊣forgetful adjunction"* fully and provably.
  The honest, Directive-1-faithful way to get the tower is to present each rung as a
  `(Σ,E)` theory and generate it through this authored machinery. This turns ~all of the
  tower from "invention" into "instantiation of a lifted engine." **Recommend adopting
  this as the foundation's progenitor-of-progenitors.**

- **D2 — Accept that only Monoid is a genuine rung-lift; the rest is synthesis.** Be
  Präriehund-honest in the design: Monoid = LIFT (proved universal property, many
  witnesses); Semigroup = named-only (law lifted, atom synthesized);
  Magma/CommutativeMonoid/Group/AbelianGroup/Quasigroup/Loop/Semiring/Ring/Field =
  SYNTHESIZE (through D1's engine). Do **not** claim Helios authored a group or a magma.

- **D3 — Reconcile the two synthesized groups.** Decide whether SP2's `aob:SealedGroup`
  (identity/compose/inverse, already committed, already teeth-bearing) IS the canonical
  `Group` rung that the foundation's agnostic `Group` progenitor grounds, or whether the
  foundation mints a fresh agnostic `Group` and `aob:SealedGroup` becomes one *child
  instance* of it. Either way the **inverse law has no Helios basis** and must be
  authored as a foundation axiom atom (the one tower axiom that is pure synthesis).

- **D4 — Tower shape = byte_order progenitor pattern, one law per child (never cram).**
  Mint an agnostic `AlgebraicStructure` progenitor grounding nothing; each rung a
  composable child adding exactly one law (Magma: closure/binary-op; Semigroup: +assoc;
  Monoid: +identity; Group: +inverse; AbelianGroup: +commutativity), with the "all in
  between" branches (CommutativeMonoid off Monoid, Quasigroup/Loop off Magma via
  division/identity) as sibling composable children, and the two-operation line
  (Semiring→Ring→Field, Module/VectorSpace over them) as a parallel progenitor family.
  This is faithful to Directive 17 AND to the source's own "one universal-property clause
  at a time / six obligations checked separately" discipline
  (`26/03/04:24-50`). Each law is its OWN atom; no rung crams two laws into one node.

- **D5 — Set-theory anchor is *ambient Set*, not axiomatized; space constructs are
  essentially absent.** Helios grounds algebra in Set implicitly (free monoid `Σ*`,
  Hom-sets, `ℕ₀`, presheaves `Cᵒᵖ→Set`) but authors **no** ZF/power-set/ordinal/cardinal
  atoms and **no** topological/metric/normed/vector space as a structure (only "ambient
  vector spaces" incidentally, `appendix A:504`). So the "grounded in set theory +
  space constructs" clause of Directive 18 is, for the algebra half, satisfiable by
  anchoring on *ambient Set + the free-algebra engine*; but the **space-constructs half
  is near-total synthesize** and belongs to the space pillar — flag the sequencing so the
  algebra tower's Set anchor is not blocked waiting on space constructs that the source
  never authored.

---

## 6. Coverage statement (Präriehund)

- **Read IN FULL:** the 4 mandatory files (design_constraints Directive 18 etc.),
  `ledger/W2/helios/srcy_map.md`; paper 26 `sections/01_thesis`, `03_olog_node_arrow_law`,
  `08_lambda_blotto_free_term_engine`, chapters `03/{01,03,04}`, `04/{01,02}`, `06/01`,
  `10/01`; paper 31 `sections/01_thesis`, `03_olog_node_arrow_law`, chapters
  `01/02`, `02/{01,03}`, `04/{03,04}`; `21/05/04_monoid_monad_yoneda_binders`;
  `07/05/03_ecosystem_free_monoid`; `shared/components/math/olog_yoneda_monoid_monad.tex`.
- **Whole-corpus grep sweep** for magma/semigroup/quasigroup/loop/monoid/group/abelian/
  semiring/ring/field/lattice/inverse — hits characterized above; the concentrated hits
  read in context.
- **Sampled, not read line-by-line:** appendix A body beyond the algebra rows; the
  spec-atom mirror (byte_order taken from the srcy_map characterization + one atom).
- **Grep false-positives noted:** broad "group"/"free.monoid"/`\path{}` matches inflated
  raw counts; the per-rung claims above rest on the *specific* cited lines only.
