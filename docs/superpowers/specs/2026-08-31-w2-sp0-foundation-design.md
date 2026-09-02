# W2 · SP0 — the Foundation floor (algebra ⟵ set-theory · spaces · functionality/typing) — design

> **superpowers:brainstorming output** (design-first HARD GATE). Materialises Directive 18 (ontology
> anchors on ALGEBRA ⟵ SET THEORY + space constructs) + Directive 19 (the FOURTH pillar:
> functionality/typing over combinatory logic; the Frame IS Curry's `F`). Design-only — NO
> `.ttl`/`.sparql` authored here. Built on the four-pillar research
> (`ledger/W2/algebra_foundation/00_synthesis.md` + notes `01`–`06`), all read in full. Maintainer
> decisions RESOLVED (Directive 20): **MAXIMAL depth, all teeth-proved, across every pillar.**
> Corpus-agnostic v1 (Directive 13), built to be relaunched. Namespace `fnd: <urn:silmaril:fnd:#>`.

**Goal.** Author the deepest floor `basicttl/foundation/` — the bedrock the whole ontology stands
on — as a **taiji of four co-equal pillars**: (1) **Set theory** (structural/ETCS carriers), (2) the
**algebra tower** (the full magma→abelian-group spine + two-operation line + quasigroup/loop +
module/vector, every rung a `(Σ,E)` presented-algebra atom minted through the LIFTED free⊣forgetful
engine), (3) **space constructs** (LIFTED Site/sheaf + `𝔗_f`; SYN point-set Top/Metric/Vector/Normed),
(4) **functionality/typing** (Curry's `F` = the Frame arrow; B/C/W/K/I + `F_n` + Γ; the §4 variance
bifunctor; the §5 implication taiji; the §6 paradox-quarantine) + a **logic sub-floor** (P/N/⊃ + proof
terms). SP1/SP2/SP3 then **re-anchor additively** onto it. Set theory carries the CARRIERS, the algebra
tower the OBJECTS/OPERATIONS, functionality the ARROWS, spaces the topology/geometry.

**Binding sources** (gospel): `docs/unary-byte-frame-law.md` (the Frame law + closed-λ substrate),
`docs/praeriehund-demokratie-der-kategorien.md`, `ledger/W2/design_constraints.md` (Directives 1–20),
the committed floors `basicttl/{primitives,aob,crs}/*`, the Helios corpus under `helios/srcy/` (esp.
papers 09/14/18/19/25/26/31/33/41 + appendix B + the `00_whitepaper` foundation), and H. B. Curry,
*First Properties of Functionality in Combinatory Logic*, Tôhoku Math. J. **41** (1936) 371–401
(**cite, never commit**; Directive 19).

---

## 0. The honesty ledger (Praeriehund — load-bearing, per Directive 20)

Every foundation atom carries an authority tag, in the **corpus's own trichotomy** (Node-or-Arrow
authority — the three evidence-class constructors DirectSource/ProvedDerivation/DeclaredSynthesis at
`helios/srcy/appendices/37_appendix_c_node_arrow_foundation/sections/00_content.tex:1704`, kept separate
in the Routers-End-at-Sources subsubsection at `…/00_content.tex:1956`; the coarser binary
direct-source-vs-declared-synthesis pole the `DS`/`SYN` tags name is at `…:240`):
**`DS`** (direct-source — verbatim Helios, and the atom's `rdfs:comment` MUST carry the exact
`helios/srcy/.../*.tex` file:line), **`PD`** (proof-derived from a Helios file:line), or **`SYN`**
(**declared project synthesis** — the corpus's own sense, which covers BOTH cited standard-mathematical
fact AND a maintainer/project-directive pattern; cite the real provenance, and do NOT pretend it is a
Helios-paper lift). What is genuinely **LIFTED (DS/PD)** from Helios *papers*: structural `Set`, the
**Monoid**, the **minting engine** `F_E(X)=T_Σ(X)/≡_E` + the free⊣forgetful adjunction (`L ⊣ R` with the
forgetful `R:GovAlg→Graph`, DS; the `Graph→Set` descent is a SEPARATE SYN bridge, not a paper-26 lift),
**Site/sheaf +
`𝔗_f`** + the non-Riemannian partition theorem, the DS/PD/SYN + Node-or-Arrow honesty machinery (DS,
cite appendix 37), and (Directive 19) the Frame/ρ/Yoneda apparatus the arrow pillar recognizes.
**SYN (declared project synthesis):** (a) the **agnostic-progenitor pattern** — it is NOT in the
authored `helios/srcy` papers (only the appendix-39 `byte_order` mirror, which is reference-only); it
is the maintainer's `byte_order` worked-example + **Directive 17**, so it is SYN cited to Directive 17,
NEVER DS; (b) the universal-object gap-fills (terminal `Unit` / initial `Void` / `product` /
`coproduct` as universal constructions — standard CT) and the `Graph→Set` underlying-vertex-set
forgetful bridge `fnd:graphUnderlyingSet` (standard math, the SYN second step of the descent
`R:GovAlg→Graph` → `Graph→Set`, NOT a paper-26 lift); (c) every rung above Monoid, the two-operation
line, quasigroup/loop, module/vector, ALL point-set spaces, the combinators/`F_n`/Γ, the group
**inverse law**, and the entire logic sub-floor — cited to standard mathematics (the Directive-19 Curry
precedent). SYN atoms are teeth-proved per the maximal choice, honest-red where no v1 consumer exists.
The corpus's explicit **refusal of point-set topology** (`helios/srcy/papers/19/.../05/03_cell_complex_pasting.tex:11-13,69-74`)
is the recorded reason those space atoms are SYN, not LIFTED. The external appendix-39
`compass_artifact` survey is **reference-only** (cite, never author-from). **The DS tag's own bar
(exact Helios file:line in the atom comment) is itself teeth-checked** — an atom tagged DS/PD without a
`helios/srcy/.../*.tex` file:line in its comment is a defect.

---

## 1. The shared MECHANISM — the minting engine (LIFTED; the real anchor)

Every algebra rung is not hand-axiomatised in isolation; it is a **presented algebra** minted through
the engine Helios authors fully and provably
(`helios/srcy/papers/26/sections/01_thesis.tex:93-128`;
`26/03/03_signature_equations_governed.tex:31-42`):

- `fnd:Signature` (a many-sorted `Σ` = sorts + typed operation symbols with arities) — SYN shape lifted
  from the source's signature-with-equations discipline.
- `fnd:EquationSet` (`E` = a set of equations/laws over `Σ`).
- `fnd:PresentedAlgebra` = `F_E(X) = T_Σ(X)/≡_E` — the free `Σ`-algebra on generators `X` quotiented
  by the congruence `≡_E`. **LIFTED**.
- `fnd:freeForgetful` — the adjunction `L ⊣ R` (free construction left-adjoint to the forgetful functor
  `R:GovAlg→Graph`, which forgets a governed algebra to its inspectable underlying **graph** —
  `Hom_GovAlg(LG,A) ≅ Hom_Graph(G,RA)`, paper 26 `01_thesis.tex:93-128`), unit `η`/counit `ε`.
  **LIFTED (DS)**. The further descent `Graph→Set` (the underlying-vertex-set forgetful functor,
  `fnd:graphUnderlyingSet`) is a SEPARATE **SYN** bridge (standard math, NOT a paper-26 lift), so a
  carrier lands in the structural `Set` floor by the two-step `R:GovAlg→Graph` (DS) then `Graph→Set`
  (SYN) — never a single DS `R:GovAlg→Set`.
- `fnd:GovAlg` wrapper `(A, op, E, V, ℓ, P)` = carrier + operations + equations + admission + lineage +
  profile — the rung SHAPE (`26/04/01_governed_algebra_definition.tex:6-13`). **LIFTED**.

**Tooth `q_engine_presents`** (EXPECT-TRUE): every `fnd:AlgebraicStructure` rung resolves to a
`fnd:PresentedAlgebra` with a `Σ` and an `E`; a rung asserting a law not in its `E`, or claiming a
carrier not produced by `F_E`, → SHACL `conforms=False`. This is what makes "the tower is minted, not
invented" a graph fact.

---

## 2. Pillar 1 — Set theory (structural / ETCS carriers)

The deepest carrier. Structural, not material (Directive 20 pin; `03_set_theory.md` D-SET-1).

- `fnd:Set` — object of the category of sets (the presheaf codomain). **LIFTED** (`18_presheaf_semantics`).
- `fnd:elementOf` — first-class membership edge `x ∈ A` via `1 → A` (global element). **SYN** gap-fill.
- `fnd:Function` — a `Set`-morphism as a first-class object with `dom`/`cod`/graph. **SYN** gap-fill
  (fills 03's flagged function-as-morphism gap; = the arrow pillar's `F(A,B)` at the set level).
- `fnd:Relation` — a subobject of a product. **SYN**.
- `fnd:product` / `fnd:coproduct` (universal, distinct from the DATA `prim:Tuple`/`prim:Sum`) with
  terminal `fnd:Unit` (`1`) and initial `fnd:Void` (`0`). **LIFTED** (usage) + **SYN** (universal-object
  gap-fill).
- `fnd:PowerObject` — the topos `Ω` (sieve-valued subobject classifier), NOT classical `2^X`.
  **LIFTED** as `Ω` / **GAP** as `2^X` (deferred, honest-red).
- `fnd:Cardinality` — finite/counting cardinal as an object (`Octet`=256, `RGB`=3, `Bit`=2); `hasCardinality`.
  **SYN-FROM** SP1 carrier comments. Transfinite = honest-red deferral.

**Teeth:** `q_set_carrier` (every foundation carrier is a `fnd:Set` under a grounding);
`q_membership_typed` (an `∈` edge whose element is not `1→A` typed → RED); `q_universal_product`
(a `fnd:product` without its two projections + universal factoriser → RED — the same universal-property
discipline SP1/SP2 use). **PIN guard** `q_presheaf_not_set`: the set floor is the CARRIER beneath the
category layer, it does NOT flatten it (`X ≡ Hom(-,X)` is shorthand, not identity) — probe: asserting a
presheaf `owl:sameAs` its set of elements → RED.

---

## 3. Pillar 2 — the algebra tower (MAXIMAL, all teeth-proved)

An agnostic `fnd:AlgebraicStructure` progenitor (grounds nothing) with each rung its own atom adding
**exactly one law**, never crammed (Directive 17). Each rung = a `fnd:PresentedAlgebra` (§1). The
one-operation spine, the two-operation line, and the division/module structures are three
progenitor sub-families.

**One-operation spine** (`Σ = {·}`):
| rung | law added (over parent) | authority |
|---|---|---|
| `fnd:Magma` | closure/totality only (`E=∅`) | SYN (engine substrate LIFTED) |
| `fnd:Semigroup` | associativity | SYN atom; **law PD** (assoc proved for concat/paths) |
| `fnd:Monoid` | two-sided identity | **LIFTED** (the one genuine rung-lift) |
| `fnd:CommutativeMonoid` | commutativity | SYN (instances LIFTED: `(ℕ₀,+,0)`, `M_J`) |
| `fnd:Group` | two-sided inverse | SYN; **inverse law = the one zero-Helios-basis axiom, cited math fact** |
| `fnd:AbelianGroup` | commutativity (off Group) | SYN |
| `fnd:Quasigroup` / `fnd:Loop` | Latin-square division / + identity (off Magma) | SYN |

**Two-operation line** (`Σ = {+, ·}`, a parallel progenitor):
`fnd:Semiring → fnd:Ring → fnd:Field` (distributivity; additive-inverse; multiplicative-inverse). SYN;
the number tower `prim:Natural…prim:Complex` re-anchors here as the first ring/field consumer.

**Module/vector (algebra ∩ space seam):** `fnd:Module` (over a ring) → `fnd:VectorSpace` (over a field).
SYN. `fnd:VectorSpace` is shared with Pillar 3.

**Teeth (one per rung, probe-injected):** each `q_<rung>_law` is EXPECT-TRUE and its shape bites when
the defining law is violated — e.g. `q_group_inverse` RED on a "group" whose inverse does not undo the
op (reusing the SP2 sealed-group inverse-teeth pattern); `q_semigroup_assoc` RED on a non-associative
witness; `q_abelian_comm` RED on a non-commutative witness; `q_ring_distrib` RED on a non-distributive
witness. **Progenitor teeth** (Directive 17 pattern from SP3): the agnostic `fnd:AlgebraicStructure`
grounds no concrete operation; a rung minus its added law is REJECTED; no rung crams two laws.
**Interlock tooth** `q_monoid_is_endo`: `fnd:Monoid` ≅ one-object category ≅ `F(X,X)` endo-functionality
(the seam to Pillar 4).

**Präriehund pin (SP6 polysemy):** the corpus lexeme "algebra" means F-algebra/Eilenberg–Moore
T-algebra — a DIFFERENT sense from this universal-algebra tower; "group" = group-object vs SP2 sealed
group. These are glossary-scoped polysemy teeth (Directive 16), not naming accidents.

---

## 4. Pillar 3 — space constructs (LIFTED core + SYN point-set, all teeth-proved)

- `fnd:Site` = category of regions + Grothendieck topology (point-free space) + `fnd:Presheaf`/`fnd:Sheaf`.
  **LIFTED** (`25_sheaf_gluing`, `01_site_of_mittens_history.tex:110-135`).
- `fnd:sheafCondition` (equalizer form), `fnd:descent`, `fnd:Cover`/Čech. **LIFTED**.
- `fnd:PerceptualTessellation` = `𝔗_f` (finite weighted 2-complex + shortest-path metric; already in
  `crs/geometers.ttl`). **LIFTED** (`00_helios_foundation/05_carrier_towers_triad.tex:185-233`).
- non-Riemannian metric + product-cell partition theorem + refusal teeth. **LIFTED** (`41/05`).
- `fnd:TopologicalSpace (X,τ)` (open-set axioms), `fnd:MetricSpace (X,d)` (Lawvere-enriched over
  `([0,∞],≥,+)` — ties to CommutativeMonoid), `fnd:NormedSpace`/`fnd:InnerProductSpace`. **SYN**, cited
  standard math (corpus refuses point-set topology — recorded).

**Teeth:** `q_sheaf_glues` (local sections agreeing on overlaps glue to a unique global — RED if the
uniqueness/agreement fails); `q_topology_axioms` (τ closed under arbitrary union + finite intersection,
contains ∅/X — RED on a violating family); `q_metric_triangle` (d satisfies identity/symmetry/triangle —
RED on a violating triple); `q_vectorspace_axioms` (the 8 vector-space axioms over a `fnd:Field`).

---

## 5. Pillar 4 — functionality / typing (Curry's F) + the logic sub-floor

**The arrow layer.** The Frame is RECOGNIZED as Curry's `F` (not rebuilt); 3½ of 4 SP1 re-anchors are
additive (`06c`).

- `fnd:Functionality` = Curry `F`; `fnd:functionalityOf`/`fnd:typesAsArrow` — `F(X,Y)` = the type of
  functions X→Y. **LIFTED-FROM-CURRY** (§1); carrier LIFTED (`prim:Frame`, `unary-byte-frame-law.md:28-38`).
  `F(X,X)` = the Monoid rung = one-object category (seam to Pillar 2). The **effect** coordinate =
  Curry's `F` in the ρ-monad's Kleisli category (**SYN-FROM** Curry ⊕ the ρ-monad — an honest
  enrichment of Curry's bare 2-place F).
- `fnd:Combinator` agnostic progenitor with children `fnd:B`/`fnd:C`/`fnd:W`/`fnd:K`/`fnd:I` (compose /
  swap / duplicate / constant / identity) + the n-ary `fnd:F_n` ladder (Def 2.1: `F_0=I`, `F_1=F`,
  `F_{n+1}=(C·BB_{n+1})F_1F_n`) + the `fnd:Compositor` `Γ`. **SYN, cited-from-Curry, teeth-proved**
  (maximal choice; the corpus substrate is named-variable λ, so these have no Helios carrier — honest).
- `fnd:VarianceBifunctor` `F(dom,cod)` — CONTRAVARIANT in domain, COVARIANT in codomain (Curry §4:
  `FXY, U⊆X, Y⊆V ⟹ FUV`). Covariant codomain **reuses SP1's proved `RealizationTransport`**;
  contravariant domain is **NEW SYN teeth** (SP1 has none; the unary-law input-coordinate collision is
  recorded as an SP6 polysemy tooth, `prim:Frame` stays the product). `q_functor_variance` RED when a
  domain-widening or codomain-narrowing is accepted.
- `fnd:selfApplicationGuard` — the §6 paradox quarantine: an ungated self-application `χχ` (`χ≡[f]N(ff)`)
  resolves to `silm:isProvisional`, never a naive proposition. **LIFTED** discipline (six ways in `06c`)
  + SYN wiring. `q_no_untyped_self_apply` RED on an ungated `χχ` treated as a proposition.

**Logic sub-floor** (full, per the maximal choice — Curry §5–§6):
- `fnd:Proposition` (`P_r`), `fnd:Negation` (`N`), `fnd:Implication` (`⊃`) + `fnd:ProofTerm`; the K/C/W
  implication laws as teeth. **SYN, cited-from-Curry**.
- **The functionality↔implication taiji** (Directive 16 polysemy): ONE lexeme, arrow-sense (exponential
  `B^A`) ↔ implication-sense (`A ⊃ B`), with `F' ≡ [x,y,z](u)(xu ⊃ y(zu))` (Curry Thm 5.8) proving they
  coincide. `q_curry_howard` RED if the exponential and implication senses diverge on a witness.

---

## 6. File layout (`basicttl/foundation/`, one concern per file — Rule 14)

| file | pillar / concern |
|---|---|
| `engine.ttl` | §1 the minting engine (Signature/EquationSet/PresentedAlgebra/freeForgetful/GovAlg) |
| `set_theory.ttl` | §2 structural Set floor (Set/element/Function/Relation/product/coproduct/Ω/Cardinality) |
| `algebra_spine.ttl` | §3 one-operation spine Magma…AbelianGroup + Quasigroup/Loop |
| `algebra_rings.ttl` | §3 two-operation line Semiring/Ring/Field + Module/VectorSpace |
| `spaces.ttl` | §4 Site/sheaf/𝔗_f (LIFTED) + TopologicalSpace/MetricSpace/Normed/Inner (SYN) |
| `functionality.ttl` | §5 Curry F + variance bifunctor + F(X,X)=Monoid seam + selfApplicationGuard |
| `combinators.ttl` | §5 B/C/W/K/I + F_n ladder + Γ compositor |
| `logic.ttl` | §5 P_r/N/⊃ + proof terms + the Curry–Howard taiji |
| `reanchor.ttl` | §7 the `fnd:groundsIn*` edges from SP1/SP2/SP3 (additive) |
| `foundation.shapes.ttl` | all SHACL teeth |
| `foundation.queries.sparql` | all EXPECT-TRUE ASKs (inline DATA CONTRACT each) |
| `checks/run-foundation-checks.sh` + `README.md` | runner (parse SP0+SP1+SP2+SP3 merged → pyshacl + re-run SP1/SP2/SP3 invariants + depth gate + every ASK) + floor doc |

The runner validates the **merged SP0+SP1+SP2+SP3 graph** and keeps all prior floors green.

---

## 7. Re-anchor plan (SP1/SP2/SP3 → SP0, ADDITIVE — 15/16 points)

Edge mechanism: a new `fnd:groundsInSet`/`fnd:groundsInAlgebra`/`fnd:groundsInSpace`/`fnd:functionalityOf`
object property (a carrier IS a Set / IS a Monoid under a forgetful grounding — NOT a subtype),
reserving `rdfs:subClassOf` for genuine is-a (`aob:SealedGroup rdfs:subClassOf fnd:Group`). Land
`basicttl/foundation/` first, THEN add edges — rebuild nothing.

- **SP1:** `prim:Octet`/`RGB`/`Bit` → finite `fnd:Set` (card 256/3/2); `prim:ByteVector`/concat →
  `fnd:Monoid` (free monoid on Octet); number tower → set-inclusion chain + `fnd:Ring`/`fnd:Field`;
  `prim:Frame` → `fnd:Functionality` (Curry F); `RealizationTransport` → the covariant leg of
  `fnd:VarianceBifunctor`; ρ-monad → functionality composition; `isYonedaPoint` → Frame=F applied.
- **SP2:** `aob:SealedGroup` → child of the agnostic `fnd:Group` (the ONE real build — teeth-prove
  binary-op/closure/two-sided-inverse-universal/abelian-flag); `aob:HashDigest` → element of `Octet³²`;
  `aob:ByteOrderProgenitor` → `fnd:coproduct`/agnostic-progenitor template; `aob:aobValue → prim:Primitive`
  inherits transitively.
- **SP3:** `Q_A`/`Q_G`/disjointWith → `fnd:product` + `fnd:coproduct`; `ForgetfulTagFrame` → set
  surjection; role towers → functors `Ordinal→URN` (graded); `CarrierProduct K` → categorical product;
  geometers/planes → finite-dim coordinate/`fnd:VectorSpace` (metric/topology via Pillar 3);
  `CoordinateDerivation`/z → Curry-F-typed Kleisli functions.

---

## 8. Interfaces

**Consumes:** SP1 (`prim:*` — Set carriers, Frame, ρ, RealizationTransport, Yoneda), SP2
(`aob:SealedGroup`, `aob:ByteOrderProgenitor`, `aob:HashDigest`), SP3 (`crs:CarrierProduct`, towers),
Helios (the engine, Monoid, Site/sheaf, `𝔗_f`, honesty machinery), Curry 1936 (F, combinators, §4/§5/§6).
**Produces:** the four-pillar bedrock every later floor grounds in; the minting engine future rungs
reuse; the logic sub-floor W-level provenance/rule-of-three can consume; the SP6 polysemy seeds
("algebra"/"group"/functionality↔implication); the re-anchor edges that make SP1–SP3 foundation-grounded.

---

## 9. Non-goals (this iteration; honest-red deferrals)

Material/ZFC set theory (first-class `2^X`, transfinite ordinals/cardinals, universe objects — structural
floor only); the appendix-39 `compass_artifact` classical-space tower (simplicial-sets-on-Δ, manifolds,
fiber bundles, sheaf Laplacian, persistent homology — reference-only, not authored); corpus instances
(pure shape, zero corpus binding — W5); live proof-checking of the logic floor (the teeth check the
laws, not a full proof assistant). Built to be relaunched (Directive 13).
