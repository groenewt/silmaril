# 00 — SYNTHESIS: the algebra ← set-theory ← space foundation floor (Directive 18 brainstorming gate)

> Präriehund honesty banner. This is the SYNTHESIS a brainstorming DESIGN GATE needs, built
> STRICTLY on the five pillar research notes (`01_categorical_base.md`, `02_algebra_tower.md`,
> `03_set_theory.md`, `04_space_constructs.md`, `05_reanchor_surface.md`, all read in full) and
> Directive 18 (`ledger/W2/design_constraints.md:228-261`). It authors NOTHING in `basicttl/`,
> runs no state-changing git, and DECIDES nothing on the maintainer's behalf. Every structural
> claim is tagged **LIFTED** (present in the authored Helios source, with the pillar note that
> carries the `file:line`), **SYNTHESIZED-FROM** (extended from a named authored source — honest
> `SYN`), or **GAP** (not in the source; would be pure invention — flagged hard). Directive 19's
> functionality/typing/combinatory-logic pillar is a co-equal FOURTH strand handled by a separate
> agent; it is referenced where it touches this surface, never designed here.

---

## 0. The one-paragraph verdict the gate is being asked to rule on

Helios authors the **categorical HOME** the algebra tower lives in — completely, at thesis/proof
depth — and authors **exactly one tower rung as a first-class proved structure: the MONOID**. It
does **not** author Magma, Semigroup-as-structure, Group, AbelianGroup, Quasigroup, Loop, Ring,
Field, or Module, and it does **not** author point-set Topological/Metric/Vector/Normed spaces.
What it authors *instead of* those rungs is the thing that makes them cheap and faithful to mint:
the **presented-free-algebra + free⊣forgetful ENGINE** (`F_E(X)=T_Σ(X)/≡_E` over a many-sorted
signature-with-equations), the **agnostic-progenitor pattern** (`byte_order`), the **DS/PD/SYN +
Node-or-Arrow honesty machinery**, and — for space — the **Grothendieck SITE / sheaf** apparatus
plus the **one fully-constructed finite space object** (`𝔗_f`). Set theory is present only as
*ambient structural* `Set` (used, never axiomatized); ZFC/transfinite/material set theory is
absent. The committed floors SP1/SP2/SP3 are **already algebra-shaped**: 15 of 16 re-anchor points
are purely additive edges, and the set/monoid bedrock they point at is the single largest genuine
synthesis. **Net for the gate: this is not a "lift a tower" project; it is a "lift the ENGINE and
the DISCIPLINE, then generate the tower as (Σ,E) atoms under an agnostic progenitor, and add
grounding edges" project.** The forks below are real because the source deliberately stops at
monoid and deliberately declines point-set topology — so *how far to go* and *on which framing* are
genuinely undetermined, while *how to build it* and *that render artifacts are violations* are
already settled by the source.

---

## 1. PROPOSED FOUNDATION STRUCTURE (lifted / synthesized-from / gap)

The proposed floor is `basicttl/algfound/` (name illustrative), organized in three strata that
match Directive 18's bedrock→surface stack: **(A) set-theory floor → (B) algebra tower → (C) space
constructs**, all sitting under the categorical home and governed by the lifted honesty machinery.

### 1.A The set-theory floor (the deepest anchor)

| Construct | Status | Source anchor (via pillar note) |
|---|---|---|
| `Set` as ambient category (codomain of presheaves, `C^op→Set`) | **LIFTED** | 01 §3; 03 §1.1-1.2 (`18/.../01_thesis.tex:24-31,59-68`) |
| Element / membership `x∈P(A)` (as *used*, category of elements `∫P`) | **LIFTED (as usage)** / **GAP (as first-class typed `∈` edge)** | 03 §2.1 (`18/.../04_.../01_category_of_elements.tex:10-20`); no `prim:membership` exists |
| Function = `Set`-morphism (presheaf action `P(f)`, `prim:Map` data) | **LIFTED (categorical)** / **GAP (function-as-morphism object w/ dom/cod/graph)** | 03 §2.2 (`formal.ttl:192-196`) |
| Relation | **LIFTED as typed arrow** (relation-as-subset **deliberately absent**) | 03 §2.3 |
| Product (`Tuple`, terminal `Unit`, Frame `O×E`, CRS `K`) | **LIFTED** | 03 §2.4 (`formal.ttl:168-171,218-222`) |
| Coproduct / disjoint union (`Sum`, initial `Void`; colimit≠disjoint-union authored) | **LIFTED** (two senses — polysemy) | 03 §2.5 (`formal.ttl:198-201,216-217`; paper 19) |
| Power set | **LIFTED only as topos `Ω` (sieve-valued)** / classical `2^X` = **GAP** | 03 §2.6 (`18/.../05_.../02_subobject_classifier.tex:7-52`) |
| Ordinals / cardinals | **LIFTED only finite/counting** (`Ordinal` enum + `Count`/256 successor + `ℕ₀/ℕ⁺`) / transfinite = **GAP** | 03 §2.7 (`formal.ttl:276-282`; `unary-byte-frame-law.md:721-729`) |
| Cardinality-as-object (`hasCardinality`, `Octet`=256, `RGB`=3, `Bit`=2) | **SYNTHESIZED-FROM** implicit carrier comments | 05 §1.3 (`physical.ttl:148,156,453-465`) |

**Framing recommendation (see D-D):** a **structural (ETCS-flavored)** floor, lifted, and largely
a **recognition/consolidation of what SP1 already materializes** (03 §4), with exactly three
gap-fills: membership edge, function-as-morphism object, universal-construction coproduct/product
held distinct from the data `Sum`/`Tuple`.

### 1.B The algebra tower (magma → abelian group, "all in between") as agnostic-progenitor atoms

The tower is proposed as an agnostic `AlgebraicStructure` progenitor (Directive 17 pattern lifted
from `byte_order`, 02 §3 / 05 §2.3) grounding nothing, with **each rung its own atom adding exactly
one law/clause, never crammed** — this shape is itself LIFTED from the source's "one
universal-property clause at a time / six obligations checked separately" discipline
(`26/03/04_free_versus_path_monoid.tex:24-50`, 02 §2).

| Rung | Status | Source anchor (via pillar note) |
|---|---|---|
| The MINTING ENGINE — free⊣forgetful adjunction `L⊣R` + presented free algebra `F_E(X)=T_Σ(X)/≡_E` on a many-sorted signature-with-equations | **LIFTED (the real anchor)** | 02 §2 (`26/sections/01_thesis.tex:93-128`; `26/03/03_signature_equations_governed.tex:31-42`) |
| GovAlg wrapper `(A,op,E,V,ℓ,P)` = carrier+op+equations+admission+lineage+profile | **LIFTED (the rung *shape*)** | 02 §2 (`26/04/01_governed_algebra_definition.tex:6-13`) |
| **Magma** (`Σ={·}`, `E=∅`; free magma = `T_Σ(X)`) | **SYNTHESIZED-FROM** the engine (substrate lifted, named rung GAP) | 02 §1 MAGMA (`26/03/03_...tex:13-15`) |
| **Semigroup** (+ associativity) | **SYNTHESIZED-FROM** engine; **law LIFTED** (assoc proved for concat/paths), atom named-only in source | 02 §1 SEMIGROUP (`21/05/04_...tex:138`; `31/01/02_...tex:51-94`) |
| **Monoid** (+ two-sided unit) | **LIFTED** — the one genuine rung (free/endopath/endomorphism/finitely-presented/graded monoids, proved universal properties) | 01 §4.1; 02 §1 MONOID (`07/05/03_ecosystem_free_monoid.tex:17-71`; `31/...`; `appendix A:76-77,133`) |
| **CommutativeMonoid** (+ commutativity, off Monoid) | **SYNTHESIZED-FROM**; instances LIFTED (`(ℕ₀,+,0)`, `M_J=ℕ₀^J`, trace congruence); noncommutativity is the authored default | 02 §1 COMM-MONOID (`31/02/03_...tex:10`; `26/10/01_...tex:8`) |
| **Group** (+ inverse) | **GAP for the inverse law** (zero Helios basis); rung SYNTHESIZED-FROM engine + SP2 `SealedGroup` | 02 §1 GROUP / §5 D3 (only external counterexample `20/09/03_...tex:61-81`) |
| **AbelianGroup** (+ commutativity, off Group) | **GAP** (only the vol-20 abelian⊂group counterexample) | 02 §1 ABELIAN |
| **Quasigroup / Loop** (off Magma, via division/identity) | **GAP** (fully absent) | 02 §1 QUASIGROUP/LOOP |
| **Semiring → Ring → Field** (two-operation parallel progenitor line) | **GAP as rungs**; valuation *usage* LIFTED; number-tower ℤ/ℚ/ℝ/ℂ is a set-inclusion chain awaiting ops | 02 §1 SEMIRING/RING; 05 §1.1 (`appendix A:260-271`; `formal.ttl:36-68`) |
| **Module / VectorSpace** (module over a field; = algebra∩space seam) | **GAP as rung** (only "ambient vector spaces" incidental) | 02 §1 RING/FIELD/MODULE; 04 §1.7, D5 |

**Präriehund pin:** the lexeme "algebra" in the corpus already means **F-algebra / Eilenberg–Moore
T-algebra** (01 §4.2) — a *different* sense from the universal-algebra tower. Do not let the
presence of the word "algebra" masquerade as tower coverage. Same for "group" (group-object vs
SP2 sealed group). These are SP6 glossary-polysemy teeth, not naming accidents.

### 1.C The space constructs

| Construct | Status | Source anchor (via pillar note) |
|---|---|---|
| **Site** = category of regions + Grothendieck topology (point-free space) + **presheaf/sheaf** | **LIFTED (the progenitor "space")** | 04 §1.1 (`25/01/00_...tex:1-90`, `01_site_of_mittens_history.tex:110-135`) |
| Sheaf condition (equalizer form), descent, Čech / open cover | **LIFTED** | 04 §1.5 (`19/05/02_sheaf_condition_for_part_of.tex`; `06/01/01_cover_definition.tex:5-16`) |
| **Perceptual tessellation `𝔗_f`** = finite weighted 2-complex + shortest-path metric (canonical worked space object; already in `crs/geometers.ttl`) | **LIFTED** | 04 §1.2 (`00_helios_foundation/05_carrier_towers_triad.tex:185-233`) |
| Non-Riemannian metric + product-cell partition theorem (+ refusal teeth) | **LIFTED** | 04 §1.3 (`41/05/perceptual_color_towers.tex:49-250`) |
| **MetricSpace** atom (via Lawvere enrichment over `([0,∞],≥,+)` — ties to CommutativeMonoid) | **SYNTHESIZED-FROM** `𝔗_f` + metric-feature usage; enriched def only in the mirror | 04 §1.4, D4 (`06/03/03_metric_structure.tex:53-69`) |
| Cell complex as *shape* | **LIFTED as shape**, **NEGATIVE finding**: corpus explicitly refuses point-set topology on it | 04 §1.6 (`19/05/03_cell_complex_pasting.tex:11-13,69-74`) |
| **TopologicalSpace `(X,τ)`**, open-set axioms | **GAP / actively refused** — only the Site exists | 04 §3, D2 |
| **VectorSpace / NormedSpace / InnerProductSpace** | **GAP as atoms** (usage only; inner product *refused* for colour) | 04 §1.7, D5 |
| Simplicial-sets-on-Δ, manifolds, fiber bundles, sheaf Laplacian, persistent homology | **GAP** — present ONLY in the mirrored external `compass_artifact` (appendix 39), never authored | 04 §2, D1 |

---

## 2. GAP ANALYSIS — in the source vs synthesize/extend vs pure invention

**IN THE SOURCE (LIFTABLE, faithful, `DS`/`PD`):**
- The categorical home: category quadruple `(O,hom,id,∘)` + laws, functors, natural
  transformations, diagrams, Yoneda, colimits/pushout/coequalizer (01 §1, §3).
- The honesty machinery: Node-or-Arrow admission grammar + minimality contract + DS/PD/SYN
  authority trichotomy; **the render-artifact-as-violation rule is already authored**
  (`01_olog_contract.tex:21-22`) — this directly discharges Directive 18's CSS/HTML clause (01 §2, §6.6).
- The tower: **Monoid** (many proved witnesses) and the **minting engine** (`F_E(X)=T_Σ(X)/≡_E` +
  free⊣forgetful adjunction) and the **agnostic-progenitor pattern** (02 §1-§2).
- Structural `Set` and most of a structural set floor already materialized in SP1 (03 §4); products,
  coproducts/disjoint-union (data + universal), finite ordinals/cardinals, size-as-hypothesis.
- Space: **Site/sheaf** and **`𝔗_f`** (both already partly in `basicttl/`), cover/Čech, the
  non-Riemannian partition theorem, metric-space *usage* (04 §1).

**MUST BE SYNTHESIZED / EXTENDED (honest `SYN`, but generated *through a lifted engine or template*,
not hand-invented):**
- Every tower rung except Monoid: Magma, Semigroup-atom, CommutativeMonoid, Group, AbelianGroup,
  and (if in scope) Quasigroup/Loop/Semiring/Ring/Field/Module — each as a `(Σ,E)` child of the
  agnostic progenitor, minted through the engine. The *shapes* are lifted; the *rung atoms* are new.
- The three set-floor gap-fills: first-class membership edge, function-as-morphism object,
  universal-construction coproduct/product distinct from data `Sum`/`Tuple` (03 §4, D-SET-2).
- Cardinality-as-object over the carriers; the `Monoid(ByteVector,concat)` object (05 §1.3, §5.1).
- `MetricSpace` atom (anchored on `𝔗_f`, enriched route), `VectorSpace` atom (at the algebra seam).
- `aob:SealedGroup`'s missing group teeth if the re-anchor is to be teeth-proven (05 §2.1, D-G).

**PURE INVENTION (no source anchor at all → candidate NON-GOALS for v1, honest-red deferrals):**
- The **inverse law** for Group — the single tower axiom with *zero* Helios basis (02 §1 GROUP).
  (Liftable as standard mathematical fact, cf. the Directive-19 Curry precedent, but not from any
  Helios paper.)
- **Material / ZFC set theory**: first-class extensionality/pairing/union/power-set-as-`2^X`,
  transfinite ordinals/cardinals, universe objects (03 §2.6-2.7, D-SET-1/D-SET-3).
- **Point-set** Topological/Metric/Vector/Normed spaces *as axiomatized `(X,τ)`/`(X,d)` sets*, and
  the full classical space tower (simplicial-sets-on-Δ, cellular sheaves + Laplacian, bundles,
  manifolds) — present only in the **mirrored external `compass_artifact`** (04 §2, D-F). The
  authored corpus *actively refuses* point-set topology (04 §1.6).

---

## 3. RE-ANCHOR PLAN (SP1/SP2/SP3 → the foundation)

**Headline (05 §0, §4):** the floors are already algebra-shaped; **15 of 16 re-anchor points are
purely ADDITIVE** (new grounding edges, nothing rebuilt). Concrete attach points:

**SP1 `basicttl/primitives/` (all additive):**
- `prim:Octet`/`prim:RGB`/`prim:Bit` → **finite Set** (card 256/3/2) — additive edge; MINT the Set +
  `hasCardinality` objects (the bedrock, currently implicit in comments) — 05 §1.3.
- `prim:ByteVector` under concat → **Monoid** (free monoid on Octet = `Vec(Oct)`) — additive edge;
  MINT the Monoid object; cleanest lift (matches the authored free/history monoid) — 05 §1.3, 01 §5.
- number tower `prim:Natural…prim:Complex` → **set-inclusion chain** (additive) + **ring/field line**
  (synth ops, depth-gated) — 05 §1.1.
- formal thin category `prim:SubtypeArrow…` → **Category / Poset** (additive) — 05 §1.2.
- `prim:Vector`/`prim:Tensor`/`prim:CRS`/`prim:Coordinate` → seed **vector/metric/space** (additive
  edge; synth the space objects) — 05 §1.4.
- `realization.ttl` ρ-functor + `taiji.ttl` Yoneda/Frame → the functor/presheaf layer the
  **Directive-19** pillar re-anchors onto (flagged, not designed here) — 05 §1.5.

**SP2 `basicttl/aob/`:**
- `aob:SealedGroup` → **Group** — additive edge `subClassOf algfound:Group`, **but the one item
  needing real new teeth**: it is a monoid-with-inverses (assoc + identity + a genuine inverse
  materialized) yet lacks a general binary-operation object, closure/totality, the two-sided-inverse
  *universal*, and the abelian-vs-nonabelian flag (05 §2.1, D-G). Directive 18 singles this out
  ("its `group_law` sealed group IS a group in this hierarchy"), so the re-anchor is load-bearing.
- `aob:HashDigest` → element of **product/power set** `Octet³²` (additive) — 05 §2.2.
- `aob:ByteOrderProgenitor` → **coproduct / agnostic-progenitor** — additive, AND the *template* for
  the tower's own shape — 05 §2.3.
- `aob:aobValue → prim:Primitive` → inherits SP1 anchoring **transitively, zero work** — 05 §2.4.

**SP3 `basicttl/crs/` (all additive):**
- `crs:TaggedByteCarrier`/`Q_A`/`Q_G`/`owl:disjointWith` → **product set** + **coproduct/disjoint
  union** — 05 §3.1.
- `crs:ForgetfulTagFrame` → **set function (surjection)** onto the quotient — 05 §3.1.
- `crs:UrnRoleTower`/K_S/K_O/K_P → **functors `Ordinal→URN`** = graded structures — 05 §3.2.
- `crs:CarrierProduct` K + five πⱼ + joint-faithfulness → **categorical product with its universal
  property** — arguably the cleanest re-anchor (already a product) — 05 §3.3.
- geometers/planes → finite-dim **coordinate spaces** (additive edge; metric/topology = the space
  GAP) — 05 §3.4; `crs:CoordinateDerivation`/z/OrderProjection → Kleisli **functions**/permutation
  action — 05 §3.5.

**Edge mechanism (05 D6):** prefer a new `algfound:groundsInAlgebra` object property for the
carrier→Set/Monoid groundings (a carrier *is* a Set under a forgetful grounding, not a *subtype* —
same shape as `ForgetfulTagFrame`), reserving `rdfs:subClassOf` for genuine is-a edges (e.g.
`aob:SealedGroup rdfs:subClassOf algfound:Group`). Sequencing: **land `basicttl/algfound/` as the
new deepest floor, then add edges** — do not rebuild (see D-C).

---

## 4. THE GENUINE MAINTAINER DESIGN DECISIONS (the brainstorming forks)

Each fork below is open *because the source genuinely leaves it open*. Items the source or Directive
18 already settles are collected in §5 as PINS, not offered as forks.

### D-A — FRAMING: universal-algebra-first, category-theory-first, or a taiji?
- **Opt 1 — Universal-algebra-first:** explicit `magma…abelian-group` signatures over set-theory
  carriers, hand-axiomatized. *Tradeoff:* matches Directive 18's literal wording and is legible to
  corpus-agnostic consumers, BUT leans on the (unauthored) material set floor and hand-axioms — least
  faithful to how Helios actually builds structures.
- **Opt 2 — Category-theory-first:** the corpus's native idiom — monoids as one-object categories,
  monoid-objects, everything via the free⊣forgetful adjunction over `Set`. *Tradeoff:* maximally
  faithful (01 §4.1b, 02 §2), enrichment-agnostic, BUT obscures the named tower the maintainer asked
  for and pushes work onto consumers who want "a group."
- **Opt 3 — TAIJI via the engine (RECOMMENDED, Präriehund-grounded):** a rung IS a universal-algebra
  presentation `(Σ,E)`, and it is MINTED by the lifted categorical engine `F_E(X)=T_Σ(X)/≡_E` +
  free⊣forgetful adjunction. The two faces are one object: the UA signature is the *what*, the
  free-algebra machinery is the *how*. *Why:* both note 01 and note 02 independently converge here —
  the source authors the engine fully and provably, so this turns ~all of the tower from "invention"
  into "instantiation of a lifted engine" (02 D1). Faithful to Directive 18's wording AND to Helios.

### D-B — DEPTH for v1 (how far up the tower + which spaces), under corpus-agnostic v1 + YAGNI
- **Opt 1 — Consumer-only:** author only the rungs a committed floor hangs on: **Monoid** (SP1/SP3
  `Vec(Oct)`, lift-supported) + **Group** (SP2 `SealedGroup`) + the ring/field line for the number
  tower. *Tradeoff:* minimal invention, but violates Directive 18's explicit "all in between as
  first-class citizens."
- **Opt 2 — Full spine as atoms, teeth only where consumed (RECOMMENDED):** mint the **entire
  `Magma→Semigroup→Monoid→CommutativeMonoid→Group→AbelianGroup` spine** as agnostic-progenitor `(Σ,E)`
  atoms (each nearly free via the engine — this is *why* the engine is the anchor), but **prove teeth
  only where a consumer exists** (Monoid = `PD`; Group = the `SealedGroup` teeth). *Tradeoff:* honors
  "all in between" and Directive 17 at low cost, while keeping unconsumed rungs as declared-`SYN`
  atoms rather than force-proved. Spaces IN for v1: **site/sheaf** (lift, largely done) + **`𝔗_f`/cell
  complex** (lift) + **MetricSpace** (synth, `𝔗_f`-anchored, enriched route) + **VectorSpace** at the
  algebra seam. Spaces DEFER: point-set `(X,τ)`, simplicial-sets-on-Δ, manifolds, bundles, Laplacian,
  persistent homology (04 D6).
- **Opt 3 — Full spine + two-operation line + spaces, all teeth-proved:** also mint
  Quasigroup/Loop/Semiring/Ring/Field/Module and axiomatize spaces now. *Tradeoff:* completeness, but
  most of it is pure `SYN`/invention with no v1 consumer — YAGNI violation, and drags in the inverse
  law and material-set gaps prematurely.
- **Recommendation:** Opt 2. The engine makes the full *spine* cheap and faithful; Quasigroup/Loop
  and the ring/field/module line become progenitor children that stay declared-`SYN` (honest-red) until
  a consumer (the number tower is the first ring/field candidate) pulls them GREEN.

### D-C — SEQUENCING: additive re-anchor vs rebuild
- **Opt 1 — Additive re-anchor after the foundation lands (RECOMMENDED):** land `basicttl/algfound/`
  as a new floor, then add grounding edges from SP1/SP2/SP3. *Tradeoff:* 15/16 surface items are
  already additive (05 §4), nothing green is put at risk; the only real build (`SealedGroup` teeth) is
  itself additive.
- **Opt 2 — Rebuild the floors on the foundation.** *Tradeoff:* maximal coherence, but throws away
  proven teeth for no evidenced need — the notes find no committed structure that *must* be rebuilt.
- **Recommendation:** Opt 1. Strongly evidenced (05 D1); formally still the maintainer's call.

### D-D — SET-THEORY depth: structural-liftable vs material-synthesized; new artifact vs consolidation
- **Opt 1 — Structural (ETCS-flavored) floor, as a recognition/consolidation of SP1 (RECOMMENDED):**
  an object `Set` = the codomain with elements/functions/products/coproducts/terminal/initial/subobject
  classifier, re-labeling and consolidating what `formal.ttl`/`taiji.ttl` already carry, plus the three
  gap-fills. Ordinals/cardinals = finite/counting only (anchored on the `Count`/256 authority); power
  set = topos `Ω` (sieve-valued), not `2^X`. *Tradeoff:* fully faithful and low-invention (03 D-SET-1/2).
- **Opt 2 — Material (ZFC-flavored) floor:** first-class `∈`, extensionality, `2^X`, transfinite
  ordinals/cardinals. *Tradeoff:* matches the literal Directive-18 word-list, but is **not in the
  source** — pure invention against a structural corpus that polices the `presheaf≠set` collapse.
- **Opt 3 — Parallel new set floor SP1 then re-anchors onto.** *Tradeoff:* cleaner separation, more
  duplication and invention than Opt 1.
- **Recommendation:** Opt 1, with the material floor recorded as an explicit honest-red deferral (not
  a silent build). Pin the `presheaf≠set` / `X≡Hom(-,X)`-is-shorthand guard (03 D-SET-6): the set floor
  sits beneath the category layer as its CARRIER, it does not flatten it.

### D-E — POSITION: beneath SP1 (new deepest floor) vs beside it
- **Opt 1 — Beneath, as the new deepest floor `basicttl/algfound/` (RECOMMENDED):** SP1/SP2/SP3
  ground downward into it. *Tradeoff:* matches Directive 18's "bedrock→surface" stack and the additive
  re-anchor plan.
- **Opt 2 — Beside SP1, as a co-deepest ground.** *Tradeoff:* Directive 18 itself offers this ("beneath
  SP1 **or beside it as the deepest ground**", `:245`) — genuinely open — but "beside" complicates the
  single-descent story and the `groundsInAlgebra` edge direction.
- **Recommendation:** Opt 1, subject to the D-D guard that "deepest floor" means *carrier beneath*, not
  *flattener of*, the category layer.

### D-F — Is the mirrored appendix-39 `compass_artifact` a legitimate lift source for the classical space tower?
- **Opt 1 — Honest-red external REFERENCE (RECOMMENDED):** treat it like the Directive-19 Curry paper —
  cite-able orientation, not authored progenitor. The real space lift is the authored **site/sheaf**.
- **Opt 2 — Legitimate lift target:** mint Top/metric-as-enriched-cat/simplicial-sets/bundles/manifolds
  from it. *Tradeoff:* it is the only place the full tower exists, but it is a copied external survey,
  and the authored papers *deliberately decline* point-set topology (04 §1.6) — lifting from it would
  contradict the authored theory and stretch Directive 1 ("lift from Helios, never invent") past its
  meaning.
- **Recommendation:** Opt 1. This is the space pillar's central gating question (04 D1); genuinely the
  maintainer's to settle.

### D-G — Reconcile the two synthesized groups (`aob:SealedGroup` vs the foundation `Group`)
- **Opt 1 — `SealedGroup` IS the canonical `Group` rung** the agnostic progenitor grounds. *Tradeoff:*
  reuses committed teeth, but bends the sealed-group's cocone-leg semantics into the general group op.
- **Opt 2 — Mint a fresh agnostic `Group`; `SealedGroup` becomes one child instance.** *Tradeoff:*
  cleaner separation and a reusable `Group`, at the cost of a second group object to keep coherent.
- **Either way:** the **inverse law has no Helios basis** and must be authored as a foundation axiom
  atom — the one tower axiom that is pure synthesis (02 D3, 05 §5.3). And a decision is owed on whether
  the re-anchor is **teeth-proven** (synthesize binary-op/closure/two-sided-universal/abelian-flag) or
  **edge-only** (bare `subClassOf`) — Directive 18's singling-out argues teeth-proven (05 D4).
- **Recommendation:** Opt 2 (agnostic `Group` progenitor, `SealedGroup` as a child), teeth-proven,
  since Directive 18 makes this re-anchor load-bearing.

---

## 5. PINS — what the source or Directive 18 already SETTLES (not forks)

1. **Tower shape = agnostic progenitor, one law per child, NEVER crammed.** Lifted from `byte_order`
   (Directive 17) AND from the source's "one universal-property clause at a time / six obligations
   separately" discipline (02 §2, 05 §2.3). Not open.
2. **Render/CSS/HTML artifacts are VIOLATIONS, realized AS violations.** Directive 18 + the already
   authored olog-contract rule "a rendered artifact is admissible only when it witnesses the governed
   diagram rather than replacing it" (`01_olog_contract.tex:21-22`, 01 §2/§6.6). Not open.
3. **Adopt the corpus's own honesty machinery:** DS/PD/SYN authority + minimality contract +
   Node-or-Arrow admission on every rung (data, equations, existence/smallness hypothesis, authority
   class) (01 §2, §6). Not open.
4. **Monoid is the ONE genuine rung-lift; everything above is `SYN`.** Do not let the corpus's
   F-algebra/T-algebra sense of "algebra" masquerade as universal-algebra coverage (01 §4.2, 02 D2).
   Not open.
5. **The engine (`F_E(X)=T_Σ(X)/≡_E` + free⊣forgetful) is authored and IS the progenitor-of-
   progenitors.** Whatever framing D-A picks, the minting machinery is a lift, not a design choice
   (02 §2). Not open.
6. **The descent into `Set` must happen; only its DEPTH is a fork.** The corpus takes `Set` as
   ambient and never descends; that descent is precisely the foundation's job (03 §1.2). Whether/how
   deep = D-D; *that* it is authored = pinned.
7. **Polysemy load for SP6 (reference through the glossary, never bare):** `algebra` (F-/T-algebra vs
   universal-algebra), `group` (group-object vs sealed group), `coproduct/disjoint-union` (data `Sum`
   vs universal construction), `space` (site vs point-set), `vector` (List vs vector-space element),
   `Ordinal` (enum vs von-Neumann). These are teeth to carry, not decisions to make (01 §6.4, 02 §4,
   03 D-SET-5, 04 D5).
8. **Directive 19's functionality/typing/combinatory-logic pillar is a co-equal fourth strand**
   (arrows over B/C/W/K/I, §4 variance, §5 implication-taiji, §6 quarantine), re-anchoring on SP1's
   ρ-functor + Frame/Yoneda. Referenced here; designed by its own pillar (05 §5.5, Directive 19).

---

## 6. Coverage statement (Präriehund)

- **Read IN FULL for this synthesis:** all five pillar notes (`01`–`05`) and Directive 18
  (`design_constraints.md:228-261`), plus Directive 19 (`:263-297`) for the fourth-strand boundary.
- **Evidence provenance:** every `file:line` in §1-§3 is carried from the pillar note cited beside it;
  this synthesis re-cites via the notes rather than re-opening the corpus, per its synthesis scope.
- **Honest limits inherited from the pillars:** the "only Monoid is authored / rest is SYN" verdict,
  the "point-set topology is refused / classical tower is mirror-only" verdict, and the "material set
  theory is absent" verdict are the pillars' grep-verified negatives (01 §7, 02 §6, 03 §7, 04 §5, 05
  §7); no pillar exhaustively re-read all 34 papers, so a hidden magma/metric/vector-space paper cannot
  be ruled out with certainty — flagged, not asserted away.
- **Decides nothing:** every §4 fork is left to the maintainer with options + tradeoffs +
  Präriehund-grounded recommendation; §5 pins only what the source/Directive already fixes.
