# W2 · SP0 — the Foundation floor (plan)

> **superpowers:writing-plans output.** Executes the SP0 design
> (`docs/superpowers/specs/2026-08-31-w2-sp0-foundation-design.md`) with Directive 20 RESOLVED
> (MAXIMAL depth, all teeth-proved, four pillars). Bite-sized, test-first (RED→GREEN), zero
> placeholders. Every asserted law has a biting tooth proven by probe injection (conforms/ASK
> True→False). Every `owl:Class` ≥200-char `rdfs:comment`. Every atom carries a `DS`/`PD`/`SYN`
> authority tag (Praeriehund honesty ledger, design §0). Corpus-agnostic v1. Namespace
> `fnd: <urn:silmaril:fnd:#>`. Floor dir `basicttl/foundation/`.

## Interfaces (see design §8 for detail)
**Consumes:** SP1 `basicttl/primitives/*` (Set carriers, `prim:Frame`, ρ-monad, `RealizationTransport`,
Yoneda), SP2 `basicttl/aob/*` (`aob:SealedGroup`, `aob:ByteOrderProgenitor`, `aob:HashDigest`), SP3
`basicttl/crs/*` (`crs:CarrierProduct`, towers); Helios (engine, Monoid, Site/sheaf, `𝔗_f`, honesty
machinery); Curry 1936 (F, B/C/W/K/I, §4/§5/§6 — cite, never commit). **Produces:** the four-pillar
bedrock; the minting engine; the logic sub-floor; SP6 polysemy seeds; the additive re-anchor edges.

## Honesty ledger (design §0 — gospel)
LIFTED from Helios: structural `Set`, Monoid, the minting engine, agnostic-progenitor pattern,
Site/sheaf + `𝔗_f`, DS/PD/SYN + Node-or-Arrow machinery, the Frame/ρ/Yoneda apparatus. Everything
above Monoid + two-operation line + quasigroup/loop + module/vector + ALL point-set spaces +
combinators/`F_n`/Γ + the group inverse law + the logic sub-floor = **SYN, cited standard-math fact**
(Directive-19 Curry precedent). Tag every atom. SYN atoms honest-red where no v1 consumer, still
teeth-proved (maximal choice).

## Tasks (test-first; each = one file/concern with biting teeth)

**T1 — scaffold + merged-graph runner.** Create `basicttl/foundation/` + `checks/run-foundation-checks.sh`
(parse SP0+SP1+SP2+SP3 → pyshacl over the merged graph vs `foundation.shapes.ttl` + re-run SP1
`run-floor-checks`, SP2 `run-aob-checks`, SP3 `run-crs-checks` invariants + `scripts/ontology-depth-check.py
basicttl/foundation` + every fnd ASK) + empty `foundation.shapes.ttl`/`foundation.queries.sparql`/`README.md`.
**RED→GREEN:** runner GREEN on the empty fnd graph with SP1+SP2+SP3 still green. **Probe:** break the
SP3 load path → runner RED (proves it re-validates all prior floors).

**T2 — `engine.ttl` (§1 the minting engine, LIFTED).** `fnd:Signature`, `fnd:EquationSet`,
`fnd:PresentedAlgebra` (`F_E(X)=T_Σ(X)/≡_E`), `fnd:freeForgetful` (`L⊣R`, η/ε), `fnd:GovAlg` wrapper.
**Tooth `q_engine_presents`:** every rung resolves to a `fnd:PresentedAlgebra` with `Σ`+`E`; a rung
claiming a law not in its `E` → RED. **Probe:** a presented-algebra whose carrier is not `F_E`-produced → RED.

**T3 — `set_theory.ttl` (§2 structural Set floor).** `fnd:Set`, `fnd:elementOf` (`1→A`), `fnd:Function`
(dom/cod/graph), `fnd:Relation`, `fnd:product`/`fnd:coproduct` (universal) + `fnd:Unit`/`fnd:Void`,
`fnd:PowerObject` (`Ω`), `fnd:Cardinality`. **Teeth:** `q_set_carrier`, `q_membership_typed`,
`q_universal_product`, **`q_presheaf_not_set`** (PIN guard: presheaf `owl:sameAs` its element-set → RED).

**T4 — `algebra_spine.ttl` (§3 one-operation spine + quasigroup/loop, all teeth-proved).** Agnostic
`fnd:AlgebraicStructure` progenitor (grounds nothing) → `fnd:Magma → fnd:Semigroup → fnd:Monoid →
fnd:CommutativeMonoid → fnd:Group → fnd:AbelianGroup` (each +1 law) + `fnd:Quasigroup`/`fnd:Loop`. Each
a `fnd:PresentedAlgebra`. **Teeth (one per rung):** `q_semigroup_assoc`, `q_monoid_identity`,
`q_commmonoid_comm`, `q_group_inverse` (SYN inverse law, cited; reuse SP2 inverse-teeth pattern),
`q_abelian_comm`, `q_quasigroup_division`; progenitor teeth (grounds-nothing; a rung minus its law → RED;
no cram); **`q_monoid_is_endo`** (Monoid ≅ one-object category ≅ `F(X,X)` — the Pillar-4 seam).
**Probes:** non-associative → RED; inverse that doesn't undo → RED; non-commutative "abelian" → RED.

**T5 — `algebra_rings.ttl` (§3 two-operation line + module/vector, all teeth-proved).** `fnd:Semiring →
fnd:Ring → fnd:Field` (distributivity / additive-inverse / multiplicative-inverse) + `fnd:Module` (over
a ring) → `fnd:VectorSpace` (over a field). **Teeth:** `q_ring_distrib`, `q_field_mult_inverse`,
`q_module_scalar`, `q_vectorspace_axioms`. **Probe:** non-distributive "ring" → RED; a "field" with a
non-invertible nonzero element → RED.

**T6 — `spaces.ttl` (§4 spaces, LIFTED core + SYN point-set, all teeth-proved).** `fnd:Site` +
`fnd:Presheaf`/`fnd:Sheaf` + `fnd:Cover` + `fnd:sheafCondition`/`fnd:descent` (LIFTED);
`fnd:PerceptualTessellation` (`𝔗_f`, LIFTED); `fnd:TopologicalSpace`/`fnd:MetricSpace`/`fnd:NormedSpace`/
`fnd:InnerProductSpace` (SYN). **Teeth:** `q_sheaf_glues`, `q_topology_axioms`, `q_metric_triangle`,
`q_vectorspace_axioms` (shared). **Probe:** τ not closed under finite intersection → RED; d violating
the triangle inequality → RED; local sections agreeing on overlaps with no unique glue → RED.

**T7 — `functionality.ttl` (§5 Curry F + variance, all teeth-proved).** `fnd:Functionality` (Curry F =
the Frame; RECOGNIZE `prim:Frame`, don't rebuild), `fnd:functionalityOf`/`fnd:typesAsArrow`, the effect
coordinate (ρ-monad Kleisli), `fnd:VarianceBifunctor` `F(dom,cod)` (covariant codomain reuses SP1
`RealizationTransport`; **contravariant domain = NEW teeth**), `fnd:selfApplicationGuard`. **Teeth:**
`q_frame_is_functionality`, **`q_functor_variance`** (domain-widening or codomain-narrowing accepted →
RED), **`q_no_untyped_self_apply`** (ungated `χχ` as a proposition → RED; resolves to `silm:isProvisional`).

**T8 — `combinators.ttl` (§5 combinatory substrate, all teeth-proved).** `fnd:Combinator` agnostic
progenitor → `fnd:B`/`fnd:C`/`fnd:W`/`fnd:K`/`fnd:I` + the `fnd:F_n` ladder (`F_0=I`,`F_1=F`,
`F_{n+1}=(C·BB_{n+1})F_1F_n`) + `fnd:Compositor` (Γ). SYN, cited-from-Curry. **Teeth:** `q_combinator_reduces`
(each combinator's defining reduction — `Kxy=x`, `Ix=x`, `Wxy=xyy`, `Cxyz=xzy`, `Bxyz=x(yz)` — RED on a
wrong reduction), `q_fn_ladder` (the `F_n` recurrence holds; a broken rung → RED), progenitor teeth
(grounds-nothing; no cram).

**T9 — `logic.ttl` (§5 logic sub-floor + Curry–Howard taiji, all teeth-proved).** `fnd:Proposition`
(`P_r`), `fnd:Negation` (`N`), `fnd:Implication` (`⊃`), `fnd:ProofTerm`; the K/C/W implication laws; the
**functionality↔implication taiji** (Directive-16 polysemy: exponential `B^A` ↔ `A⊃B`, `F'` per Curry
Thm 5.8). **Teeth:** `q_implication_kcw` (the K/C/W laws hold), **`q_curry_howard`** (the exponential and
implication senses coincide on a witness; divergence → RED). **Probe:** a "proof term" whose type isn't
the implication it claims → RED.

**T10 — `reanchor.ttl` (§7 additive re-anchor).** The `fnd:groundsInSet`/`fnd:groundsInAlgebra`/
`fnd:groundsInSpace`/`fnd:functionalityOf` edges from SP1/SP2/SP3 (additive, rebuild nothing);
`aob:SealedGroup rdfs:subClassOf fnd:Group` (the ONE real build — teeth-prove binary-op/closure/
two-sided-inverse-universal/abelian-flag; SP2 SealedGroup becomes a child of the fresh agnostic
`fnd:Group`). **Teeth:** `q_reanchor_additive` (every prior-floor grounding is an edge, no prior triple
removed — SP1/SP2/SP3 diff empty), `q_sealedgroup_is_group` (the SealedGroup satisfies the full group
teeth). **Probe:** a `fnd:groundsInAlgebra` edge onto a non-matching structure → RED.

**T11 — integration, depth, DAG.** README + probe register; depth gate green (every `owl:Class`
≥200-char comment, every SYN atom tagged); full `run-foundation-checks.sh` GREEN with SP1+SP2+SP3
untouched+green; add a `silm:phase_w2_sp0` (foundation) node to `basicttl/dag/dag_instances.ttl` with
`hasStatus "completed"` + honest inline evidence (real counts, DS/PD/SYN breakdown) and the right
`dependsOn` edges (SP1/SP2/SP3 depend on it, or it precedes them per Directive 18 bedrock→surface);
confirm the DAG parses+conforms.

## Verification (evidence-first)
Every shape RED-before/GREEN-after, each proven to bite by a documented probe. Depth gate on every
`owl:Class`. Value-type checks use `sh:in`/`sh:sparql`, never range-inference-vacuous `sh:class` (SP1
defang discipline). The runner keeps the merged SP0+SP1+SP2+SP3 graph green. Then the adversarial triple
panel (completeness / honesty / doctrine), with an explicit **honesty** angle auditing the DS/PD/SYN
tags (no SYN atom masquerading as LIFTED; the corpus's point-set-topology refusal honored; Curry cited
not committed) and a **doctrine** angle probing every rung/space/combinator/logic tooth + the
grounds-nothing progenitor discipline + the additive re-anchor (SP1/SP2/SP3 untouched).

## Non-goals (design §9)
Material/ZFC set theory; the appendix-39 classical-space tower (reference-only); corpus instances (W5);
a full proof assistant for the logic floor (teeth check laws, not proofs). Built to be relaunched.
