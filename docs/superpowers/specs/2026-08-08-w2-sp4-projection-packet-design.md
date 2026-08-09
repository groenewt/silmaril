# W2 · Sub-project 4 — the projection packet (the render fibration + nth-dim loss) — design

> **Batch design doc** (superpowers:brainstorming output; Directive 14 cadence — authored up
> front with SP2/SP3/SP5–SP9 for one maintainer review pass, no per-project Socratic gate).
> Design-only — NO `.ttl`/`.sparql`/implementation authored here. **THIS ITERATION's v1** —
> corpus-agnostic (zero live-corpus binding; that is the re-runnable W5), built to be re-run and
> relaunched, not permanent (Directive 13). This overwrites the prior SP4 draft, which invented a
> flat "12 target surfaces + 5 loss classes" packet; SP4 now **LIFTS the authored Helios
> structures** (Directive 1 — lift, do not invent).

**Goal.** Author the **full projection family** the maintainer authored in Helios — not a flat
list of emitters, and not a flat 5-way loss enum. The family has three lifted layers, and the
loss is an **nth-dimensional effect/loss taxonomy** (a progenitor tree of `prim:Effect`
descendants), NOT a flat 5:

1. the **7-leg × 3-fibre render fibration** (`helios/01_data_src_specs/triad_fibration.spec.yaml`):
   one atom projects to **7 render legs** grouped into **3 epistemic fibres**, each fibre defined
   by a coherence law;
2. the **Vol 06 five carrier-coordinate projections** `π_A,π_G,π_S,π_O,π_P` out of the five-factor
   carrier `K = K_A×K_G×K_S×K_O×K_P` — jointly faithful, **no positional S→R/O→G/P→B map** — with
   the **three-language renderer/readback identity** `V_ℓ R̂_ℓ = id_K` (`ℓ ∈ {Haskell,Elixir,Scala}`)
   as the per-leg reversibility law (`helios/srcy/papers/06_topology_jepa/sections/01_thesis.tex`);
3. the **nth-dimensional effect/loss taxonomy** seeded by SP1's realization effects, made concrete
   by the two authored lossy projections — the **syntactic-acceptance projection**
   (`triad_projection_validation.spec.yaml`) and the **4-state precedence collapse dropping
   timestamp/progress** (`wave_barrier_projection.spec.yaml`) — plus the **rank-zero S:P:O fold**
   below the full ℕ grading tower and the **S:P:O↔S:O:P reindex** effect
   (`helios/srcy/.../projection/source_dimension_planes.tex`), with reversibility governed by the
   **exact reassimilation criterion** of Vol 11 (Vol 30 disintegration↔reassimilation bridge).

Per-leg reversibility is the atom SP9 (render seal) consumes. Every asserted law gets a biting
tooth (§4).

**Binding sources** (gospel): `docs/unary-byte-frame-law.md` (Split↔Consolidated render seal;
Frame = Yoneda point; byte-stream carrier closure; the split/consolidate inverse-pair with
`consolidate(split(g))==g`), `docs/praeriehund-demokratie-der-kategorien.md`,
`ledger/W2/design_constraints.md` (Directives 1–14), the **committed SP1 floor**
(`basicttl/primitives/{formal,physical,realization,taiji}.ttl` + `primitives.{shapes.ttl,
queries.sparql}`), and the git-ignored Helios source-of-truth read in full for SP4:
`helios/01_data_src_specs/{triad_fibration,triad_projection_validation,wave_barrier_projection}.spec.yaml`,
`helios/srcy/papers/06_topology_jepa/sections/01_thesis.tex`,
`helios/srcy/shared/components/diagrams/patterns/projection/source_dimension_planes.tex`,
`helios/srcy/papers/11_base_commutative_diagram/chapters/21_bridges_avogadro_disint_canonq_visual/sections/02_bridge_disintegration_reassimilation.tex`.
Maps: `ledger/W2/helios/{data_specs_contracts,srcy,render_types}_map.md`.

Namespace: `prj: <urn:silmaril:prj:#>` (full-lexical URN idiom, unary law), grounding onto
`prim: <urn:silmaril:prim:#>` (SP1). External spellings (`GeoSPARQL`, `LinkML`, `Atlas`, `SHACL`,
`SPARQL`) survive only as immutable bridge evidence, never as internal identity.

---

## 1. Goal (precisely) — three lifted claims, each becoming graph structure with teeth

1. **The projection family IS the authored render fibration.** `triad_fibration.spec.yaml` declares
   `total_legs: 7`, `total_fibres: 3`. SP4 materialises exactly those 7 `prj:RenderLeg` individuals
   (`sh`, `ex`, `atlas`, `linkml`, `ttl`, `shacl`, `sparql`), each carrying its authored `fmt`
   (`bash`, `elixir`, `atlas_csv`, `linkml_yaml`, `rdf_turtle`, `shacl_turtle`, `sparql_query`), and
   the 3 `prj:RenderFibre` individuals (`econ` = {sh,ex}, `lang` = {atlas,linkml}, `math` =
   {ttl,shacl,sparql}). Each leg is a **Frame/Kleisli arrow of the SP1 realization monad one level
   up** — `Atom → Frame(output: surface bytes, error|effect: loss)` — reusing SP1's Frame
   (`prim:Frame prim:isYonedaPoint true`), so a render leg is Yoneda evaluation of the atom at the
   target's representable, **not** a bare emitter. **A fibre is defined by its coherence law, not by
   membership**: `econ` iff `byte_equal_stdout` (bash & elixir emit byte-identical stdout), `lang`
   iff `schema_instance_match`, `math` iff `pyshacl_validation_passes` (the "math fibre's defining
   property"). These three coherence laws are the fibre-level teeth.

2. **The categorical projection family is Vol 06's five jointly-faithful carrier projections.** The
   bridge functor `B: O_adm → K` carries the admitted olog into the five-factor carrier
   `K = K_A×K_G×K_S×K_O×K_P` (Atlas RGB, Graph RGB, and the three independent S/O/P towers). SP4
   materialises the five product projections `π_A,π_G,π_S,π_O,π_P` as first-class `prj:CarrierProjection`
   arrows, asserts they are **jointly faithful and jointly reflect isomorphisms** (Vol 06
   Theorem five-projections-jointly-faithful), and asserts the **negative law**: there is NO
   positional `S→R`, `O→G`, `P→B` map — Atlas/Graph RGB (`Q_A ∩ Q_G = ∅`) and the S/O/P towers are
   disjoint carriers (SP1/SP3 fidelity). The three-language legs `ℓ ∈ {Haskell,Elixir,Scala}` each
   carry an assembled renderer `R̂_ℓ: K → Y_ℓ` and a typed readback `V_ℓ: Y_ℓ → K`; the **projectionwise
   renderer-readback law** `π_j V_ℓ R̂_ℓ = π_j (j∈{A,G,S,O,P})` gives, by joint faithfulness,
   `V_ℓ R̂_ℓ = id_K` — the **per-leg reversibility identity**. This is the exact structure SP9 seals.

3. **The nth-dimensional effect/loss taxonomy is a progenitor tree, NOT a flat 5.** `prj:LossEffect`
   is an **agnostic progenitor** `rdfs:subClassOf prim:Effect` (the projection cost stays inside the
   SP1 Frame monad), with explicit children via `ancestry.via` (the endianness-style progenitor
   pattern, Directive 1): `prj:ParseAcceptanceLoss`, `prj:StatePrecedenceCollapse`,
   `prj:GradingTowerCollapse`, `prj:RoleOrderReindex`, plus the SP1-seeded numeric/encoding children
   `prj:PrecisionLoss`, `prj:RangeLoss`, `prj:LexicalEncodingLoss` (each `prj:lossSeededBy` an SP1
   `prim:Effect` individual). The tree is **open** (SP1's extensible-`prim:Effect` discipline: a new
   loss kind is minted only when a concrete consumer needs one) — so "not a flat 5" is structural,
   not a slogan. The two authored lossy projections instantiate it concretely (§2.3). The neutral
   `prj:Lossless` (seeded by `prim:NoEffect`) is the zero, the reversibility witness.

Corpus-agnostic: pure shape, **zero corpus instances** (exactly SP1). One tiny witness graph is
authored only to keep the ASK suite non-vacuous, mirroring SP1's litmus discipline.

---

## 2. Architecture — the fibration is a cocone of Frame-legs; loss is the failure of ε to be iso

Nothing categorical is invented; SP1's machinery (colimit taiji, Frame/Kleisli monad ρ, literal
Yoneda) is reused one level up, and Vol 06 / Vol 11 supply the projection-specific theorems.

```
                    triad_fibration (7 legs / 3 fibres)          Vol 06 carrier projections
   Atom  ──π_leg──▶ Surface(leg)   leg ∈ {sh,ex,atlas,linkml,      K = K_A×K_G×K_S×K_O×K_P
   (SP2/SP3          ttl,shacl,sparql}                              │   │   │   │   │
    over SP1)        = byte Stream/Container (SP1 carrier)          π_A π_G π_S π_O π_P   (jointly faithful,
     │               frameOutput = X (surface bytes)                                      NO S→R/O→G/P→B)
     │               frameEffect = Y (a prj:LossEffect)         three legs ℓ∈{Hs,Ex,Scala}:
     │                                                          R̂_ℓ:K→Y_ℓ ,  V_ℓ:Y_ℓ→K
     └─ fibres: econ{sh,ex}      coherence = byte_equal_stdout      π_j V_ℓ R̂_ℓ = π_j  ⇒  V_ℓ R̂_ℓ = id_K
                lang{atlas,linkml} coherence = schema_instance_match           (the reversibility identity → SP9)
                math{ttl,shacl,sparql} coherence = pyshacl_validation_passes
```

- **The packet is a cocone of Frame-legs out of the atom, with fibre coherence laws.** The 7 legs
  are the cocone legs; the 3 fibres partition them, each fibre carrying a defining coherence law
  (`prj:CoherenceLaw`). This is a real category (composition + identity reused from SP1's
  thin-category discipline), not a bag of emitters. `econ` legs must agree byte-for-byte on stdout
  (the bash⟷elixir colimit twin); `math` legs must agree under `pyshacl`.
- **Loss = the failure of the projection to round-trip; its *kind* is a typed effect.** A projection
  is **reversible iff it is a retraction** — it carries a `prj:section` witness and its coherence
  yields `V_ℓ R̂_ℓ = id_K`, so `π_leg ∘ s_leg = id`. The exact *kind* of failure is the `prj:LossEffect`
  its `prj:frameEffect` names, and those effects are **lifted from SP1's realization effects** — the
  same honest-cost vocabulary that grounds "what is a number" grounds "what does this projection
  drop." **Non-invertibility is information, never suppressed** (Vol 11, §2.2).
- **Twin-olog / ologs-of-ologs (Directive 2/6).** Each target surface `Surface(leg)` is itself an
  olog (a format's schema is a small category), so `π_leg` is an olog morphism — the turtle stacks
  one level. SP4 records this as the real edge `π_leg` into SP1's already-Yoneda-closed Frame; it
  does **not** re-materialise a second presheaf category (YAGNI — §6).

### 2.1 The five carrier-coordinate projections and the three-language readback (Vol 06)

The bridge functor `B: O_adm → K`, `K = K_A×K_G×K_S×K_O×K_P`. The two RGB factors retain the
complete tagged **Atlas** and **Graph** byte triples (`Q_A`, `Q_G`, disjoint); the last three retain
the independent **Subject / Object / Predicate** towers (SP3 `K_S/K_O/K_P`). The five projections
`π_A,π_G,π_S,π_O,π_P` are **jointly faithful** (Vol 06 Thm) — the joint-faithfulness fact is the
tooth that makes `V_ℓ R̂_ℓ = id_K` provable and forbids any positional colour↔role collapse. The
three-language readback obligation `π_j V_ℓ R̂_ℓ = π_j` must hold for **all three legs at one
versioned contract** ("matching filenames, successful dispatch, or agreement on a digest cannot
replace it" — Vol 06 thesis). SP4 records this as `prj:carrierRoundTrip` per language leg; SP9
consumes it as the reversibility seal atom.

### 2.2 The reversibility law = Vol 11's exact reassimilation criterion (feeds SP9)

Reversibility is not a decorative boolean. Vol 11 (bridge to Vol 30 disintegration↔reassimilation)
proves: for a disintegration datum `Dis(A) = (D, λ)`, reassimilation forms `Rea(D,λ) = colim D`, and
the comparison morphism `ε_A : colim D → A` (with `ε_A ∘ ι_i = λ_i`) is an **isomorphism iff the
selected cocone (A,λ) is colimiting**. Thus **"disintegration and reassimilation are inverse only on
a declared subcategory carrying selected colimiting presentations; outside that boundary the
comparison arrow remains visible; failure to be invertible is information, not a sentence to
suppress."** SP4 lifts this directly:

- `prj:reversible true` **iff** the projection carries a `prj:section` AND its `prj:comparisonMorphism`
  (`prj:ε`) is `prj:isIso true` (the retraction law); this is exactly `ε_A` being an iso.
- a **non-invertible** projection is NOT dropped — it records its `prj:comparisonMorphism` with
  `prj:isIso false`, a `prj:obstruction` (the typed `prj:LossEffect` it incurs), and a receipt. This
  is the "explicit obstruction loss + receipt" of the Vol 11 four-lane proof surface, and it is the
  honest hand-off to SP9 (a lossy leg is declared non-invertible, never silently forced).

### 2.3 The nth-dim loss taxonomy, made concrete by the two authored lossy projections

`prj:LossEffect` (agnostic progenitor `⊂ prim:Effect`) → children, each with `ancestry.via` →
`prj:LossEffect` and each `prj:lossSeededBy` an SP1 `prim:Effect`:

| loss child | authored source it is lifted from | what the projection drops | SP1 seed |
|---|---|---|---|
| `prj:ParseAcceptanceLoss` | `triad_projection_validation.spec.yaml` (per-family `[success, failure]` counters; observed baseline `{success:404, failure:73}`) | a leg that fails to parse (turtle/shacl `rdflib.parse`, sparql `prepareQuery`, linkml `id`-or-`name`) is a **projection loss** — the syntactic-acceptance surface | `prim:EncodingLoss` (surface syntax cannot carry the atom) |
| `prj:StatePrecedenceCollapse` | `wave_barrier_projection.spec.yaml` (`predecessor_state_precedence: failed > done > started_but_not_complete > silent`; `kind: precedence_projection`) | the roster→**4-state lattice** collapse: `timestamp_semantics: truthiness_only`, `progress_event_semantics: ignored` — timestamp magnitude and progress detail **deliberately lost** (nth-dim → lower-dim) | `prim:OrderingCanonicalization` + minted `prj:DimensionCollapse` |
| `prj:GradingTowerCollapse` | `source_dimension_planes.tex` (RED: "rank-zero incidence only; no computed ℕ grading tower"); Vol 11 `.yur` bridge ("the **lossy rank-zero S:P:O fold** below the full Lambda-Vector term") | the full ℕ-graded Lambda-Vector term folded to rank-0 subject–predicate–object incidence | minted `prj:GradingLoss` (`⊂ prim:Effect`) |
| `prj:RoleOrderReindex` | `source_dimension_planes.tex` (`car-orders`: declared orders **S:P:O** external vs **S:O:P** internal role) | the reorder between external rank-0 order `S:P:O` and internal role vector `S:O:P` — a materialized effect/loss *between* projections | `prim:OrderingCanonicalization` |
| `prj:PrecisionLoss` | Vol 06 five-projection round-trip; WKT/geometry surfaces | numeric/temporal grid rounding when the surface carries a narrower encoding | `prim:RoundingIEEE754`, `prim:NarrowingLoss`, `prim:Base10Precision`, `prim:EpochPrecision` |
| `prj:RangeLoss` | bounded surface fields | a bounded surface field cannot hold the full domain/cardinality | `prim:OverflowDomain`, `prim:MayOverflow` |
| `prj:LexicalEncodingLoss` | text/identifier surfaces (bnode relabel, charset) | text/identifier surrogate/normalization/charset loss in the target syntax | `prim:EncodingLoss` |

The **native Frame** discipline is the through-line: the projection carries "project-owned semantic
identity and ordering rather than a wall-clock timestamp; **no timestamp field**"
(`source_dimension_planes.tex` `car-frame`). `StatePrecedenceCollapse` is exactly the projection
dropping the timestamp axis — the concrete nth-dim loss the maintainer named. Minted effects
(`prj:DimensionCollapse`, `prj:GradingLoss`) are honest per SP1's extensible-effect rule and each is
a real `prim:Effect` individual, not a dodge.

### 2.4 The projection edge-key (the projection-role taxonomy)

`source_dimension_planes.tex` fixes **once** four projection-edge roles reused by every dimensional
view (Honeycomb / Sparky / GraphAtlas), so legends never drift. SP4 lifts them as the four
`prj:EdgeRole` individuals: `prj:InformationSource` (violet solid), `prj:ExecutedProcess` (teal
solid), `prj:AdmittedQualityReadback` (green solid), `prj:RefusalNonImplication` (red dashed). The
discipline "**colour is never the sole carrier: line style and lane words repeat each role**"
(Directive 8, visual discipline) is recorded as a law: every `prj:EdgeRole` carries ≥2 independent
discriminators (`prj:lineStyle` + `prj:laneWord`), not colour alone. `prj:RefusalNonImplication` is
the render→loss boundary — the "does not imply / no promotion" edge that marks the non-invertible /
unpromotable projection.

---

## 3. File layout (one file per concern — STRICTNESS Rule 14; `urn:` namespace)

Directory: `basicttl/projection/`. Categorical grounding in the data ttls; teeth in the
shapes/query files (SP1's split). Every `owl:Class` carries a ≥200-char `rdfs:comment` (depth gate).

| file | responsibility |
|------|----------------|
| `basicttl/projection/fibration.ttl` | the **7-leg × 3-fibre** triad_fibration TBox lifted from `triad_fibration.spec.yaml`: `prj:RenderLeg` (7 individuals + `prj:fmt`), `prj:RenderFibre` (3 + `prj:fibreOf`), `prj:CoherenceLaw` (byte_equal_stdout / schema_instance_match / pyshacl_validation_passes) + `prj:coherenceCheck`; each leg a Frame/Kleisli arrow (`prj:frameOutput`/`prj:frameEffect`), each `owl:Class` dual-grounded into the SP1 colimit taiji |
| `basicttl/projection/carrier.ttl` | the **Vol 06 five carrier-coordinate projections**: `prj:Carrier` = `K_A×K_G×K_S×K_O×K_P`, the bridge functor `prj:B`, `prj:CarrierProjection` (`π_A,π_G,π_S,π_O,π_P`) with `prj:jointlyFaithful true`; the **negative law** (no `S→R`/`O→G`/`P→B`, `Q_A∩Q_G=∅`); the three language legs (`prj:RendererReadback` for Haskell/Elixir/Scala) + the `π_j V_ℓ R̂_ℓ = π_j` obligation → `prj:carrierRoundTrip` |
| `basicttl/projection/loss.ttl` | the **nth-dim effect/loss taxonomy**: `prj:LossEffect` agnostic progenitor `⊂ prim:Effect` + the 7 children with `ancestry.via` + `prj:lossSeededBy` (SP1 effects); the minted `prj:DimensionCollapse`/`prj:GradingLoss`; the `prj:Lossless` zero; the two authored lossy projections (`prj:parseAcceptanceProjection`, `prj:waveBarrierProjection`) as concrete instances with `prj:incursLoss` + `prj:droppedAxis` (timestamp/progress, ℕ-grading) |
| `basicttl/projection/reversibility.ttl` | the **Vol 11 reassimilation criterion**: `prj:comparisonMorphism` (`ε`, `prj:isIso`), the **retraction law** (`reversible ⟺ section ∧ ε iso ∧ Lossless`), `prj:obstruction` + `prj:receipt` for non-invertible legs (never suppressed); `prj:reversible` per leg = the SP9 seal atom; disintegration↔reassimilation inverse-only-on-colimiting-subcategory |
| `basicttl/projection/edge_key.ttl` | the **projection-role edge-key**: 4 `prj:EdgeRole` individuals (info/source, executed process, admitted quality/readback, refusal/non-implication), each with `prj:lineStyle` + `prj:laneWord` (colour-never-sole-carrier law, Directive 8) |
| `basicttl/projection/projection.shapes.ttl` | SHACL law (§4) — one `sh:NodeShape` per invariant, each proven to bite (`sh:sparql`/`sh:in`, defang-proof per SP1's lesson) |
| `basicttl/projection/projection.queries.sparql` | the EXPECT-TRUE ASK suite (§4), each with an inline DATA CONTRACT comment |
| `basicttl/projection/checks/run-projection-checks.sh` + `README.md` | the runner (parse + pyshacl over merged SP1(+SP2+SP3)+SP4 graph + depth gate + every ASK, re-running the SP1 shapes/ASKs) + floor doc, consumer list, how-to-re-run |

The runner loads the **SP1 four data TTLs + SP2/SP3 data TTLs + SP4 five data TTLs into one graph**
and validates against `projection.shapes.ttl` **and** re-runs SP1's shapes/ASKs, because SP4 adds
`⊂ prim:FormalType`/`⊂ prim:Effect` classes that fall under SP1's `prim:DualGroundingShape` /
`q_universality` — SP4 is not green unless it keeps the SP1 floor green.

## 4. Verification plan (evidence-first; every asserted law has a biting tooth)

Each shape is RED before authoring, GREEN after; each ASK is `EXPECT-TRUE`, non-vacuous (positive
ASKs FAIL on the empty graph; `NOT EXISTS` ASKs FAIL under injection), and **proven to bite by a
documented probe injection** (`True→False` / `conforms=True→False`), in the SP1 idiom. Depth gate:
every `owl:Class` ≥200-char `rdfs:comment`.

**EXPECT-TRUE ASKs (`projection.queries.sparql`):**

| ASK | asserts (lifted from) | probe of record (must be CAUGHT) |
|---|---|---|
| `q_fibration_seven_three` (litmus #1) | exactly **7** `prj:RenderLeg` (with the 7 authored `fmt`s) and **3** `prj:RenderFibre`, each fibre's legs matching `triad_fibration.spec.yaml` | delete `prj:leg_sparql`, or add an 8th leg → False |
| `q_fibre_coherence` | each fibre carries its authored `prj:CoherenceLaw`: econ=`byte_equal_stdout`, lang=`schema_instance_match`, math=`pyshacl_validation_passes` | strip econ's coherence, or swap two → False / `FibreCoherenceShape` fires |
| `q_leg_is_frame` | every `prj:RenderLeg` carries a `prj:frameOutput` (a `prim:Stream`/`prim:Container`) AND a `prj:frameEffect` (a `prj:LossEffect`) — it IS a Frame | a leg missing `frameEffect` → False / `LegFrameShape` fires |
| `q_five_carrier_projections` (litmus #2) | exactly **5** `prj:CarrierProjection` (`π_A,π_G,π_S,π_O,π_P`), `prj:jointlyFaithful true` over the carrier `K_A×K_G×K_S×K_O×K_P` | delete `π_P`, or drop joint-faithfulness → False |
| `q_no_positional_role_map` | there is **NO** `prj:positionalMap` from any S/O/P tower to any RGB channel (`S→R`/`O→G`/`P→B`), and `Q_A ∩ Q_G = ∅` | inject `prj:π_S prj:positionalMap prj:red` → False / `NoPositionalMapShape` fires |
| `q_carrier_round_trip` | each language leg `ℓ∈{Haskell,Elixir,Scala}` satisfies `π_j V_ℓ R̂_ℓ = π_j` for all `j∈{A,G,S,O,P}` (`prj:carrierRoundTrip`), i.e. `V_ℓ R̂_ℓ = id_K` | drop Scala's readback, or a per-`j` obligation → False |
| `q_loss_progenitor_tree` | `prj:LossEffect ⊂ prim:Effect` is the agnostic progenitor; every loss child has `ancestry.via = prj:LossEffect` (not flat) | make a child descend from `prim:Effect` directly (bypass the progenitor) → False |
| `q_loss_seeded_from_effects` | every `prj:LossEffect` child `prj:lossSeededBy` ≥1 SP1 `prim:Effect` (genuinely lifted from the floor, not free-floating) | a loss child with no seeding effect → False |
| `q_wave_barrier_drops_timestamp` | `prj:waveBarrierProjection` declares `prj:StatePrecedenceCollapse`, the 4-state precedence `failed>done>started_but_not_complete>silent`, and `prj:droppedAxis` = {timestamp, progress} | remove the `droppedAxis` timestamp, or the precedence order → False |
| `q_parse_acceptance_projection` | `prj:parseAcceptanceProjection` declares `prj:ParseAcceptanceLoss` over the 4 authored families (turtle/shacl/sparql/linkml) with per-family success/failure semantics | drop the linkml family, or the loss decl → False |
| `q_rank_zero_fold_recorded` | the `prj:GradingTowerCollapse` + `prj:RoleOrderReindex` (S:P:O↔S:O:P) effects exist and are `⊂ prim:Effect` | delete `prj:RoleOrderReindex`, or its S:P:O/S:O:P orders → False |
| `q_reversible_iff_retraction` | `prj:reversible true` **iff** `prj:section` present AND `prj:comparisonMorphism` `prj:isIso true` AND coherence `prj:Lossless` (Vol 11 criterion) | mark a lossy leg reversible with no section → False / `RetractionShape` fires |
| `q_noninvertibility_recorded` | every non-reversible projection records `prj:comparisonMorphism` (`isIso false`) + `prj:obstruction` (a `prj:LossEffect`) + `prj:receipt` — non-invertibility is information, never dropped | a lossy leg with no obstruction/receipt → False |
| `q_edge_key_four_roles` | exactly **4** `prj:EdgeRole` (info/source, executed process, admitted quality/readback, refusal/non-implication), each with `prj:lineStyle` + `prj:laneWord` (colour-never-sole) | a role carrying only a colour, or a 5th role → False / `EdgeRoleShape` fires |
| `q_reversibility_feeds_seal` | every `prj:RenderLeg` declares a boolean `prj:reversible` + (if reversible) a `prj:section`, so SP9 reads the seal atom for all legs | a leg with no `reversible` declaration → False |
| `q_projection_dual_grounded` | every SP4 `owl:Class` dual-grounds into SP1 over the merged graph (SP1 floor kept green) | inject `ex:Orphan ⊂ prim:FormalType` → SP1 `DualGroundingShape` fires / `q_universality` False |

**SHACL mirrors (`projection.shapes.ttl`):** `prj:LegFrameShape` (output+effect present),
`prj:FibreCoherenceShape` (each fibre's authored coherence law), `prj:CarrierProjectionShape`
(5 projections, jointly faithful), `prj:NoPositionalMapShape` (no S→R/O→G/P→B; `sh:sparql`
`FILTER NOT EXISTS`), `prj:LossSeedingShape` (every `LossEffect` seeded + `⊂ prim:Effect` + progenitor
ancestry), `prj:RetractionShape` (reversible ⟺ section ∧ ε-iso ∧ Lossless), `prj:ObstructionShape`
(non-reversible ⟹ obstruction + receipt), `prj:EdgeRoleShape` (4 roles, ≥2 discriminators each) —
each a `sh:sparql`/`sh:in` constraint (never a bare `sh:class` where an `rdfs:range` would make it
vacuous, per SP1's defang lesson). **Reused SP1 tooth:** each new packet/loss `owl:Class` sits under
`prim:DualGroundingShape`; an ungrounded class flips SP1's `q_universality` false — SP4 satisfies it
directly (each class carries its own `prim:Realization` + reflexive carrier + `prim:Primitive`).

## 5. Interfaces

### Consumes — from SP1 (committed floor), named precisely
- **Realization monad + effect family (SEEDS the nth-dim loss tree):** `prim:Effect` and its
  individuals `prim:RoundingIEEE754`, `prim:NarrowingLoss`, `prim:Base10Precision`,
  `prim:EpochPrecision`, `prim:OverflowDomain`, `prim:MayOverflow`, `prim:EncodingLoss`,
  `prim:OrderingCanonicalization`, `prim:NoEffect`; `prim:Realization`, `prim:realizesAs`,
  `prim:encoding`, `prim:frameOutput`, `prim:frameEffect`.
- **Frame + Yoneda (a render leg = Yoneda evaluation):** `prim:Frame` (`prim:isYonedaPoint true`);
  `prim:Primitive`, `prim:formalFacet`, `prim:physicalFacet`, `prim:gluedBy`, `prim:rhoObject`.
- **Byte carrier ladder (surfaces are byte streams/containers):** `prim:Stream`, `prim:Container`,
  `prim:ByteVector`, `prim:byteDescendsTo`, `prim:Bit`.
- **RGB code space (the K_A / K_G carrier factors):** `prim:Red`, `prim:Green`, `prim:Blue`, each an
  Octet ordinal 0..255 (`q_rgb`), kept disjoint from the S/O/P towers.
- **Number/Real (PrecisionLoss):** `prim:Real`, `prim:Float32`, `prim:Float64`.
- **SP1 law kept green:** `prim:DualGroundingShape` / `q_universality` (SP4 classes satisfy it).

### Consumes — from SP2 (AOB meta-ontology, same batch — PROVISIONAL spellings)
- The **`aob:AOBAtom` + tensor block + multi-format emitter seam** (SP2 §5 hands SP4 the emitter
  seam feeding the render legs, and the `grounding`-claim Frame **effects** that seed the loss
  tree). **The AOB atom is the DOMAIN of every render leg** (the atom → 7 legs fan-out — every seed
  atom's `rendered_legs: [sh, ex, atlas.csv, ttl, shacl.ttl, sparql, linkml.yaml]`). Exact
  class/property spellings are a forward reference PROVISIONAL until SP2 is reviewed in this batch
  (Praeriehund — §6 Q0).

### Consumes — from SP3 (S/O/P-tower CRS law, same batch — PROVISIONAL spellings)
- The **three independent S/O/P towers `K_S/K_O/K_P`** as the domains of `π_S,π_O,π_P`, and the
  disjoint **Atlas/Graph carriers `Q_A,Q_G`** (`Q_A∩Q_G=∅`) as the domains of `π_A,π_G`; SP3's
  `crs:*` geometry + its `TransitionMap` **typed loss effects** as additional loss seeds
  (chart→chart transitions are π_L projections/retractions). PROVISIONAL pending SP3 review (§6 Q0).

### Produces — for higher sub-projects (named, consistent with the DAG)
- **SP5 (file + format taxonomy):** the **7 leg `fmt`s** (`bash`, `elixir`, `atlas_csv`,
  `linkml_yaml`, `rdf_turtle`, `shacl_turtle`, `sparql_query`) ARE the format-axis leaves SP5
  classifies; the `prj:coherenceCheck` per fibre is the format-family invariant.
- **SP6 (glossary polysemy):** the `lang`/`math` fibre surfaces carry the mole-of-glossaries
  collisions; the `atlas` leg's synonym/antonym Atlas columns are where SP6's polysemy is
  mime-confirmed.
- **SP7 (SHACL executable law):** the **`math` fibre's coherence = `pyshacl_validation_passes`** is
  exactly SP7's aggregate law surface; SP4's projection-law shapes (`RetractionShape`,
  `LossSeedingShape`, …) feed SP7.
- **SP8 (basicttl depth remediation):** basicttl content renders through these 7 legs; each
  `*_atom.ttl` projects across the fibration.
- **SP9 (render seal):** **the headline hand-off** — the **per-leg `prj:reversible` + `prj:section`
  + `prj:comparisonMorphism`** IS the split↔consolidated inverse-pair atom SP9 seals (`ε_A` iso ⟺
  colimiting cocone = SP9's `consolidate(split(g))==g`). The Vol 06 `V_ℓ R̂_ℓ = id_K` identity is the
  reversible-leg section; the lossy legs are declared non-invertible (obstruction + receipt), never
  silently forced. The nth-dim loss tree is the vocabulary SP9's seal reports drift in.

## 6. Non-goals (this iteration; YAGNI deferrals) and genuine open questions

**Non-goals / YAGNI:** corpus-agnostic — pure shape, **zero corpus instances** (live rendering is
W5). **No serializer/renderer code, no execution** — SP4 is the *ontology of the projection family*;
the actual per-format emitters, the `check-triad-coherence.sh` gate execution, and the base_templates
macro *execution* are the **W3 render pipeline** (`phase_w3_5` reversible render pipeline, `phase_w3_6`
subatomic per-format renderers). No per-value loss *measurement* (type-level classification only;
measurement is W5). No second presheaf category re-materialised at the projection level (the leg is
the `π_leg` edge into SP1's already-Yoneda-closed Frame). No projection-composition algebra beyond
the identity + retraction law SP9 needs. The `.contract` unary-law decomposition of the two lossy
projections (their `operations`/`frame_plan`/`external_boundaries`) is NOT re-authored here — SP4
lifts their **loss semantics** (the taxonomy), not their pylib module decomposition (that is the
sparky pipeline). Built to be **challenged and relaunched**, not final (Directive 13).

**Open questions for the maintainer (Praeriehund — flagged, not invented):**
- **Q0 — SP2/SP3 handles (same batch).** The AOB atom identity (domain) and the SP3 `K_S/K_O/K_P` +
  `Q_A/Q_G` carriers are forward references into designs reviewed in this same batch; their exact
  spellings are PROVISIONAL, pinned once SP2/SP3 are reviewed.
- **Q1 — is the projection family EXACTLY the 7-leg fibration, or 7 legs × 5 carrier projections?**
  `triad_fibration` gives 7 surface legs; Vol 06 gives 5 carrier-coordinate projections `π_A..π_P`.
  I have modeled **both** as one family (the 7 legs are the *surfaces*; the 5 π are the *carrier
  coordinates each surface must preserve* via `V_ℓ R̂_ℓ = id_K`). Confirm they are two axes of one
  family, not a single flat list — this is the "NOT a flat 5" ruling made structural.
- **Q2 — how open is the nth-dim loss tree this iteration?** I lifted **7 loss children** (4 concrete
  from the authored lossy projections + 3 SP1-seeded numeric/encoding). SP1's effect family gives
  the numeric/encoding seeds; `DimensionCollapse`/`GradingLoss` are minted for the timestamp-drop
  and rank-zero-fold. Is this the intended set for v1, or should more be lifted from Vol 34's
  architecture-incorporation ledger (the nth-dim loss accounting) now vs W5?
- **Q3 — the two authored lossy projections: instances or subclasses?** `triad_projection_validation`
  and `wave_barrier_projection` are authored `.contract`s (one `admitted_green`, one `active_red`).
  I model each as a **named projection instance** carrying its loss decl, not as a new `prj:RenderLeg`
  (they are *validators/observers over* the fibration, not an 8th render leg). Confirm they are
  loss-taxonomy witnesses, not legs.
- **Q4 — Atlas/Graph RGB carriers: SP4 or SP3?** `π_A,π_G` project onto the Atlas/Graph RGB byte
  triples (`Q_A,Q_G`, disjoint). Vol 06 puts them in the same carrier `K` as the S/O/P towers. Are
  `Q_A/Q_G` authored by SP3 (alongside `K_S/K_O/K_P`) and merely *consumed* here, or does SP4 author
  the RGB-carrier projection factors? I assume SP3 authors the carriers, SP4 authors the projections.
- **Q5 — reversibility granularity for SP9.** Is `prj:reversible` a single boolean per leg, or a
  **per-carrier-coordinate partial section** (a leg reversible on `π_S` but lossy on `π_A`)?
  Per-`π_j` granularity gives SP9 a finer seal (matching Vol 06's per-`j` obligation) but more
  structure. I have a single boolean + per-leg `incursLoss`; confirm that is enough for the SP9 seal.
