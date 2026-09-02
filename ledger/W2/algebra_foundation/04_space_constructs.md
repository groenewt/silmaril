# 04 — Space Constructs (topological / metric / vector / sheaf-theoretic spaces)

> W2 algebra/set-theory foundation design-gate RESEARCH note. Pillar 3 of Directive 18
> ("SPACE CONSTRUCTS"). Präriehund honesty banner: this reports, with `file:line`
> evidence, what the Helios authored SOURCE-OF-TRUTH under `helios/srcy/` actually
> PROVIDES toward the space-constructs pillar, and where the genuine gaps and decisions
> are. It authors NOTHING in `basicttl/` and decides nothing on the maintainer's behalf.
> Where the source declines to build a construct, that refusal is reported AS a finding,
> not force-fitted into a lift.

Paths below are relative to `/home/user/silmaril/`. Assigned papers read in full:
`helios/srcy/papers/25_sheaf_gluing/`, `.../06_topology_jepa/`,
`.../41_cheese_progenitor_topology/`, `.../19_mereology_as_colimit/`, plus the
whitepaper carrier-towers section and appendix 39. Corpus grepped for
`topolog|metric space|vector space|open set|neighborhood|sheaf|presheaf|simplicial|cell complex|tessellat`.

---

## 0. Headline (the one-paragraph truth)

The Helios corpus is **rich in space constructs used categorically, and deliberately
poor in space constructs axiomatized as (X, τ) / (X, d) sets.** Its genuine, authored
notion of "space" is the **Grothendieck SITE** (a category of regions + a coverage/
topology) carrying a **presheaf/sheaf**, plus **one fully-constructed finite space
object** — the native-Frame perceptual tessellation `𝔗_f = (V_f, E_f, F_f, w_f, ℓ_f, ε_f)`,
a weighted 2-dimensional triangular (simplicial) complex with a shortest-path metric.
Metric and vector spaces appear as **first-class USAGE** (metric feature codomains,
finite-dimensional sheaf stalks, normed observation/signal spaces) but are **never
axiomatized as their own atoms** in the authored papers. The corpus **explicitly
REFUSES point-set topology** on its objects (Mittens is a colimit, "not a topological
space"). The full classical tower (`Top`, metric-space-as-enriched-category, simplicial
sets as presheaves on Δ, cellular sheaves + sheaf Laplacian, fiber bundles, manifolds,
CRS) exists as an **explicit design ONLY in appendix 39, a COPIED EXTERNAL research
artifact** ("PyBrain common library" compass_artifact), not in the maintainer's authored
34-paper body. That external-vs-authored split is the pillar's central honesty question.

---

## 1. What the source DEFINES (genuine, authored lifts)

### 1.1 The SITE + Grothendieck topology + presheaf + sheaf  — the deepest genuine "space"

This is the strongest, most axiomatic space construct in the authored corpus. A **site**
is a category of regions/opens with a coverage; it IS a generalized (point-free) topology.

- **Site as three separated typed objects** (substrate ≠ site ≠ sheaf):
  `papers/25_sheaf_gluing/chapters/01_sheaf_basics_local_sections/sections/00_hyper00_typed_substrate_site_sheaf.tex:1-90`.
  - Region category `C_H` with arrows = inclusions `U→W ⟺ U⊆W`, coverage admitting jointly
    covering families `{U_i ↪ U}` (`:35-48`).
  - Latent sheaf as a **functor** `F : C_H^op → V` "satisfying the chosen sheaf-gluing
    condition" (`:50-60`), restriction `r^F_{W,U} : F(W) → F(U)` contravariant.
  - **Uses `Op(X_Mittens)` — the category of OPENS of a space** `X_Mittens` — as the running
    site `(Op(X_Mittens), J_cov)` (`:70-90`). This is the closest the authored corpus comes to
    naming a topological space, but note (`:78-90`) it explicitly declines to identify
    `X_Mittens` with a substrate or with "every possible region category."
- **Pretopology GENERATES a Grothendieck topology** (a real theorem, with proof):
  `papers/25_sheaf_gluing/chapters/01_sheaf_basics_local_sections/sections/01_site_of_mittens_history.tex:110-135`
  (`thm:25-c01-site-admissibility`): finite meet-semilattice of Frame-regions; identity /
  pullback-stable / composite-closed families ⟹ the sieves containing such a family form a
  Grothendieck topology; **"membership … not pairwise naming alone, is the exact cover-admission
  predicate."** `:199` "Grothendieck topology ≠ arbitrary surjection."
- **Sheaf condition in equalizer form** (authored twice):
  - `papers/19_mereology_as_colimit/chapters/05_atomic_colimit_constructions/sections/02_sheaf_condition_for_part_of.tex`
    — `F(U)` = equalizer of `∏_i F(U_i) ⇉ ∏_{i,j} F(U_i∩U_j)`; the apex is a section iff local
    sections agree on overlaps and glue uniquely. Explicitly scoped: "*does not claim* a full
    sheaf-on-a-site construction (deferred to Volume 25)."
- **Finite-dimensional vector-space stalks / linear sheaf**:
  `papers/25_sheaf_gluing/chapters/03_descent_and_amalgamation/chapter.tex:278-290,385` — "every
  stalk `F(U)` is a finite-dimensional vector space; every restriction map is linear";
  products are "finite-dimensional product vector spaces." (This is the seam where the sheaf
  pillar touches the vector-space pillar.)
- Already committed downstream: `basicttl/25_sheaf_gluing.ttl` exists (SP1-derived). The sheaf
  floor is the one space construct SP1 already re-derived.

**Verdict: LIFT (directly).** The site/Grothendieck-topology/presheaf/sheaf apparatus is
authored, proved, and running-example-anchored. It is the natural PROGENITOR "space" for the
pillar — a space as *a category with a gluing law*, which is exactly the sheaf-floor ontology
SP1 already carries.

### 1.2 The perceptual tessellation `𝔗_f` — the one fully-constructed finite space object

`base/00_whitepaper/sections/00_helios_foundation/05_carrier_towers_triad.tex:185-233`
(`def:whitepaper-frame-perceptual-tessellation`):
- `𝔗_f = (V_f, E_f, F_f, w_f, ℓ_f, ε_f)` — a finite native-Frame **triangular complex**:
  sampled colour vertices `V_f`, edges `E_f`, **triangular faces `F_f`** (2-simplices),
  perceptual edge weights `w_f : E_f → ℝ≥0`, lightness-fibre declaration `ℓ_f`,
  approximation-error receipt `ε_f`.
- A **shortest-path graph metric** `d_f^𝔗(u,v) = min_{paths} Σ w_f(v_i, v_{i+1})` (`:196-201`).
- Lightness fibres `L_{f,λ}`, black apex `b_f`, intrinsic neutral representative by
  `arg min_{v∈L_{f,λ}} d_f^𝔗(b_f, v)` (`:206-214`).
- **Honesty teeth carried in the definition itself**: "not identifying the mesh with colour
  space itself"; without `(w_f, ℓ_f, ε_f)` "the triangles are a presentation mesh and no
  perceptual claim is admitted" (`:214-216`); "does not assert that perceptual colour space is
  globally triangular, flat, Euclidean, or Riemannian" (`:233-237`).
- **Already lifted by SP3**: `basicttl/crs/geometers.ttl` header names
  `T_f=(V_f,E_f,F_f,w_f,l_f,e_f)` (`def:whitepaper-frame-perceptual-tessellation`) as "the
  archetype that DIMENSION IS PER-Frame/PER-geometer." So this construct is already load-bearing
  in a committed floor.

**Verdict: LIFT.** This is the corpus's canonical, fully-worked space object — a metric +
simplicial/cell complex in one. It should anchor the metric-space and cell-complex atoms the
way Mittens anchors the categorical papers.

### 1.3 Non-Riemannian perceptual metric + product-cell tessellation (paper 41)

`papers/41_cheese_progenitor_topology/chapters/05_eight_circuit_cube/perceptual_color_towers.tex`:
- Perceptual metric from Bujack et al. 2022/2025: shortest paths from black apex, metric-derived
  neutral axis, hue = equal-lightness shortest-path class, saturation = direct metric distance
  (`:92-131`, `def:41-towers-leary-colour-family`, `:117-128`).
- **Diminishing-returns theorem** `thm:41-colour-nonriemannian-obstruction` (`:49-66`): observed
  strict inequality `d(A,C) < d(A,B)+d(B,C)` on a minimizing path ⟹ the metric is NOT Riemannian
  path-length. Bounded refusal, proved.
- **Tessellation as a PRODUCT-CELL partition, explicitly NOT a painted circuit cube**
  (`subsubsec:41-colour-tessellation`, `:190-250`): base stratum = TOWERS-address hue×saturation ×
  Leary-support product; landmark cell = deterministic direct-metric cell;
  `thm:41-towers-leary-partition` (`:214-236`) proves the cells are **pairwise disjoint and
  covering** (a genuine partition / cover theorem with a no-collapse readback). Corollary
  (`:238-250`): the Leary fibre indexes a coproduct AFTER minimization, doesn't move a chromatic
  boundary.
- Paper 08 carries the negative side: `papers/08_visual_discipline/chapters/13_perceptual_colour_authority/chapter.tex:425,443`
  — "no inner product, and hence no Riemannian tensor" on colour speed (an authored *refusal* of
  inner-product structure on colour).

**Verdict: LIFT (as metric-space worked example + honesty teeth).** Real metric + real
partition/cover theorem, but the non-Euclidean/non-Riemannian/no-inner-product refusals are
part of the lift.

### 1.4 Metric structure on the latent space (paper 06)

`papers/06_topology_jepa/chapters/03_latent_space_representable/sections/03_metric_structure.tex`:
- Metric feature spaces `(A_k, δ_k)` are named as **metric spaces** (`:53`), positive weights
  `w_k`, product feature space `A = ∏ A_k` with `δ_Q(a,b) = Σ w_k δ_k(a_k,b_k)` (`:60-65`), and
  a pulled-back **pseudometric** `d_Q(X,Y) := δ_Q(q(X),q(Y))` on typed hypotheses (`:66-69`).
- Exact **Yoneda identity pseudometric** `d_Y` (0 iff naturally isomorphic, else 1), descends to
  the **discrete metric** on iso-classes (`def:profile-distance :35-46`, `prop … :75-86`).
- **Calibration distortion theorem** `thm:topology-jepa-calibration-distortion` (`:110-139`) +
  separation certificate corollary — genuine metric-space reasoning (triangle inequality, product
  metric, positive-definiteness).
- Honesty tooth (`:167-174`): raw Euclidean/cosine geometry is "only a numerical score" without a
  trained calibrator; "Yoneda's lemma supplies none of these metric … assumptions."

**Verdict: LIFT (metric space as USAGE).** Metric spaces are used correctly as feature codomains;
this justifies a first-class `MetricSpace` atom but does not itself axiomatize one.

### 1.5 Open cover / patch cover / Čech (paper 06)

`papers/06_topology_jepa/chapters/01_patch_cover_cocone/sections/01_cover_definition.tex`:
- Visual patch cover = jointly-surjective family `U = {U_i}`, `⋃ U_i = |I_Mittens|` (`:5-14`);
  **"literally an open cover after giving the finite support the discrete topology"** (`:15-16`).
- Intersection-closed spatial support poset `P_I(U)` (opens + nonempty intersections, arrows =
  inclusions, `:34-40`), Čech incidence category `Cech(U)` (`:42-53`); in `Set` intersection =
  pullback, union = pushout (`:104-119`).
- Overlap compatibility + triple-overlap **cocycle** descent datum
  (`.../02_overlap_compatibility.tex:22-56`, `:47-51` cocycle equation).

**Verdict: LIFT (cover/Čech = topological covering apparatus, discrete-topology honest caveat).**

### 1.6 Cell-complex pasting — DEFINED then DISCLAIMED (critical honesty finding)

`papers/19_mereology_as_colimit/chapters/05_atomic_colimit_constructions/sections/03_cell_complex_pasting.tex`:
- 0-cells (part-observation legs), 1-cells (overlap inclusions), 2-cells (joint witnesses),
  colimit apex = **geometric-realization analogue** (`:22-64`).
- BUT: "This view is an *analogy*, not an identity — the page does not assert that Mittens is a
  topological space" (`:11-13`); "**This page makes no claim about a point-set topology on
  Mittens**" (`:69-74`); `principle` Analogy-as-shape-not-identity (`:91-97`); the cheese-igniter
  question (`:134-139`): the failure mode is "analogy-as-identity collapse — treating the
  cell-complex picture as if it asserted a topological structure."

**Verdict: NEGATIVE finding.** The corpus builds the SHAPE of a cell complex but explicitly
refuses to import a topology. This is the sharpest evidence that the authored theory is
*deliberately not* point-set-topological.

### 1.7 Vector / normed spaces as scattered USAGE (no atom)

- "not a point of a Euclidean vector space": `papers/06_topology_jepa/chapters/03_latent_space_representable/sections/01_yoneda_embedding.tex:22`.
- "linear global sections … vector space, every restriction is linear":
  `.../03_latent_space_representable/sections/04_linear_global_sections.tex:26`.
- finite-dim vector spaces / spectral change-of-basis: `papers/27_kan_extensions/chapters/05_spectral_conjugacy_transport/chapter.tex:8`.
- "normed observation space": `papers/22_cco_style_ontology/chapters/04_scientific_occurrents_and_wave_observation/sections/03_wave_observation_certificate.tex:10,20`;
  "normed signal space `Y_ℓ`": `base/00_whitepaper/sections/00_helios_foundation/07_science_wave_bfo_safety.tex:49-50`.
- inner-product (Gram matrix of graph eigenmodes): `base/00a_node_arrow_corpus_spine/chapters/08_lambda_blotto_node_arrow_engine/chapter.tex:452-456`.
- real spectral vector space: `papers/12_cat_example_clarified/chapters/01_reality_tunnel_entry_points/sections/06_material_channel_noncollapse.tex:1,106`.

**Verdict: USAGE only — no `VectorSpace`/`NormedSpace`/`InnerProductSpace` atom is defined.**

---

## 2. What the source does NOT author — the full classical tower lives in a MIRRORED source

`appendices/39_appendix_e_research_source_mirror/sections/specs/domains/archive/compass_artifact_wf-25c14076-d62e-4844-be3c-f0bef57590bd_text_markdown.md.tex`
is a **copied external research artifact** (header `:1-3`: "Generated by mix research.render …
Source file: research/specs/domains/archive/compass_artifact_…markdown"). It is a "PyBrain common
library" design survey, NOT the maintainer's authored categorical theory. It contains — verbatim,
as external prose — the **entire** Directive-18 space tower:
- `Top` category, forgetful `Top→Set` with discrete/indiscrete adjoints; **metric space as a
  Lawvere enriched category over `([0,∞], ≥, +)`** with the triangle inequality as composition
  (`:199-202`).
- **Simplicial sets as presheaves on the simplex category Δ**, `sSet = Fun(Δ^op, Set)` a presheaf
  topos, Quillen-equivalent to `Top` (`:203-206`).
- Persistent homology as a functor `(ℝ,≤) → Vec` (`:207-210`).
- **Sheaves on `Open(X)`, cellular sheaves + sheaf Laplacian `L = δ*δ`** (Hansen-Ghrist),
  sheaf neural networks (`:212-215`).
- **Fiber bundles underlie coordinate transformations** (`:216`).
- `Vec_k` as an abelian / compact-closed monoidal category; embeddings as "vector spaces with
  metric structure"; **affine spaces as torsors over vector spaces** (`:120-149`).
- Algebra tower + `(Group, Ring, Field, VectorSpace, Manifold, CRS)` protocols and a
  `C_Brain`/six-pillar olog design (`:8-9`, `:94-158`).

**This is the crux.** Directive 18's space tower is present in the corpus *only* here, in a
mirrored external document — while the authored papers (§1.6) deliberately decline point-set
topology. Under Directive 1 ("LIFT from Helios, never invent"), whether this mirror is a
legitimate lift target is a **maintainer decision, not mine to make** (see §4, D1).

---

## 3. Gap table — Directive 18 space pillar vs authored source

| Directive-18 construct | Authored source status | Lift / Synthesize |
|---|---|---|
| **Topological space (X, τ), open-set axioms** | ABSENT & actively refused (§1.6; `neighborhood`=0 hits, `open set`=4 hits all in sheaf-site context). Only the **Grothendieck site** (§1.1) exists. | Site = **LIFT** as progenitor "space"; (X,τ) point-set = **SYNTHESIZE** as a leaf (or lift from mirror §2, honesty-flagged). |
| **Sheaf / presheaf on a space** | DEFINED, proved, running (§1.1, §1.6); `basicttl/25_sheaf_gluing.ttl` already exists. | **LIFT (direct).** |
| **Metric space (X, d, 3 axioms)** | USAGE only (§1.3, §1.4); `𝔗_f` graph-metric (§1.2). No axiomatized atom. Lawvere enriched-cat def only in mirror §2. | **SYNTHESIZE** the atom, anchored on `𝔗_f` + metric-feature usage; enriched-cat route ties to algebra tower. |
| **Vector / normed / inner-product space** | USAGE only (§1.7); refused for colour (`:425` p08). `Vec_k` def only in mirror §2. | **SYNTHESIZE** (VectorSpace = module over field ⇒ sits on algebra tower; see D5). |
| **Simplicial / cell complex** | `𝔗_f` is a real finite 2-complex (§1.2); cell-pasting shape authored but topology disclaimed (§1.6). Δ / face-degeneracy only in mirror §2. | `𝔗_f`/cells = **LIFT (as complex, not as topology)**; general simplicial-set = **SYNTHESIZE / defer**. |
| **Tessellation `T_f`** | DEFINED (§1.2) + product-cell partition theorem (§1.3); already lifted by SP3. | **LIFT (direct).** |
| **Manifold / fiber bundle / CRS** | "manifold atlas", "local TOWERS topology" named only in passing (`05_carrier_towers_triad.tex:146,171`); full defs only in mirror §2. `basicttl/crs/` already exists (SP3) as S/O/P towers, not a differential manifold. | CRS = **LIFT (SP3 done)**; manifold/bundle = **DEFER** (likely out of v1 depth). |

---

## 4. Design decisions this pillar raises for the maintainer

**D1 — Is the mirrored appendix 39 a legitimate lift source, or external structure the authored
theory deliberately declined?** The full classical space tower (Top, metric-as-enriched-cat,
simplicial sets, cellular sheaves, bundles, manifolds) exists in the corpus ONLY as a copied
`compass_artifact` research doc (§2), while the authored 34-paper body **refuses point-set
topology** (§1.6). This is a direct Directive-1 tension: "lift, never invent" — but lifting from a
mirrored external survey is neither "authored Helios theory" nor "invention." Recommend surfacing
this as the pillar's gating question; my read (Präriehund, marked as inference) is that appendix 39
should be treated as an **honest-red external REFERENCE** (cite-able orientation, like the Curry
paper in Directive 19), not as the authored progenitor — with the authored **site/sheaf** notion
(§1.1) as the real lift.

**D2 — Anchor the pillar on the SITE (point-free topology), not on (X, τ).** The corpus's genuine,
authored notion of space is a **category + coverage** (§1.1), and it is already ontology-native and
already partly in `basicttl/`. Recommend: the progenitor "space" atom = a **site** (category of
regions + Grothendieck topology + sheaf gluing law); the classical topological space `(X, τ)` with
open-set closure axioms becomes a **specialization leaf** (a site on a poset of opens), never the
progenitor. This matches Directive 17 (agnostic progenitor everywhere) and reuses the SP1 sheaf
floor rather than bolting on a disjoint point-set layer.

**D3 — `𝔗_f` is the canonical worked space object; carry its refusal teeth.** The perceptual
tessellation (§1.2) is the one fully-constructed finite space (metric + 2-complex + fibres +
error receipt) and is ALREADY load-bearing in `basicttl/crs/geometers.ttl`. Recommend it as the
anchoring example for the metric-space + cell-complex atoms — but its authored honesty teeth
("not the colour space itself"; not globally triangular/flat/Euclidean/Riemannian; no perceptual
claim without `(w_f, ℓ_f, ε_f)`; §1.3 non-Riemannian; §1.7/p08 no inner product) MUST be modeled
as active constraints, not dropped. A tessellation that claims to BE the space is a cheese-master
violation (paper 19's analogy-as-identity collapse, §1.6).

**D4 — Metric space via Lawvere enrichment ties the pillar to the algebra tower.** A metric space
is an enriched category over the commutative monoid `([0,∞], ≥, +)` (mirror §2, `:202`). Since the
algebra-tower pillar already builds `CommutativeMonoid`, modeling `MetricSpace` as **enriched over
that monoid** (rather than a bare `(X, d, axioms)` set) makes the space pillar *ground on* the
algebra pillar — more Directive-18-coherent (algebra ← set theory; spaces built from both).
Decision: enriched route vs bare-set route. (Präriehund: the enriched route is my recommendation,
but it is a design choice, not something the authored papers state.)

**D5 — Where does `VectorSpace` live (algebra tower vs space construct)?** A vector space is a
module over a field = abelian group (algebra tower) + scalar action. It legitimately belongs to
BOTH pillars — a polysemy (Directive 16) to be held as one atom with two glossary senses, not
duplicated. Decision needed on its home progenitor (recommend: algebra-tower `Module`/`VectorSpace`
citizen, cross-referenced from the space pillar), so the finite-dim sheaf stalks (§1.1) and the
metric-feature codomains (§1.4) re-anchor onto it.

**D6 — v1 depth cut.** Concrete recommendation for how far the space pillar goes in v1:
IN — site/Grothendieck-topology/presheaf/sheaf (lift, largely done), tessellation `𝔗_f`/cell
complex (lift), metric space (synthesize, `𝔗_f`-anchored), vector space (synthesize at the
algebra seam). OUT / DEFER — general simplicial sets on Δ, manifolds, fiber bundles, sheaf
Laplacian, persistent homology (all mirror-only, no authored anchor). Point-set `(X,τ)` as an
optional leaf under the site progenitor if the maintainer wants the literal Directive-18 wording
honored. This is a maintainer call; I am reporting the boundary, not setting it.

---

## 5. Präriehund honesty ledger (what I did NOT find / did not force)

- No axiomatized `TopologicalSpace`, `MetricSpace`, `VectorSpace`, `NormedSpace`, or
  `InnerProductSpace` atom exists in the authored papers. Reported as gaps, not lifted.
- The corpus **actively refuses** point-set topology on its objects (§1.6) and Riemannian /
  inner-product structure on colour (§1.3, §1.7). I report these refusals as findings; I did not
  paper over them to manufacture a topological-space lift.
- The classical tower's presence in appendix 39 is a **mirrored external artifact** (§2); I flag
  it as such rather than presenting it as authored Helios theory.
- `neighborhood/neighbourhood` = 0 hits corpus-wide; `open set` = 4 hits (all sheaf-site);
  `metric space` = 32, `vector space` = 24, `simplicial` = 21, `cell complex` = 20 — space
  vocabulary is thin and concentrated in the site/sheaf and tessellation constructs, exactly as
  reported above.
