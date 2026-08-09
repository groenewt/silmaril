# helios/srcy — SOURCE CORPUS map (W2 facet)

> Präriehund honesty banner. This maps the maintainer's authored SOURCE-OF-TRUTH
> under the git-ignored `/home/user/silmaril/helios/srcy/`. Do NOT commit it. The
> tree IS the taxonomy and is captured in full below; the theory papers were read
> at thesis/foundation depth; the ~1,900 rendered spec-atom `.tex` files and ~270
> `_aob_*` atom files were **sampled broadly, not read individually** — coverage is
> stated per-section. Where I sampled, I say so and never claim I read the whole.

## 0. What this facet IS

`helios/srcy/` is the LaTeX **source corpus** of the "Helios / Silmaril local
encyclopedia": 34 categorical papers + 3 base volumes + 5 appendices + shared
build infrastructure + copied source witnesses, all projected by one aggregate
build `projections/local_encyclopedia.tex`. It is the **authored theory that SP1
re-derived** — the colimit / monad / functor / Yoneda / presheaf / sheaf floor of
the Primitive-Floor README exists here first, as prose-and-diagram category theory
anchored on a running example (`Mittens`, a governed colimit object).

- Total: **7,261 files, 1,117 dirs.** Extensions: **5,317 `.tex`**, **1,882 `.yaml`**,
  30 `.md`, plus `.csv/.tsv/.bib/.j2/.sparql/.sh`.
- Root: `/home/user/silmaril/helios/srcy` (the encyclopedia's `src/` — every
  `\input{src/...}` in the build resolves here).

### Top-level tree
```
srcy/
├── papers/            34 paper volumes (01–34, 41)  — the categorical theory
├── base/              3 base volumes (00 whitepaper, 00a node–arrow spine, 00b cocone register)
├── appendices/        5 appendices (35 A .. 39 E)
├── node_arrow/        Silmaril_NodeArrow_Corpus_Monograph_v12.md (7,466 lines) + manifest.yaml
├── projections/       local_encyclopedia.tex (the aggregate volume-input build)
├── shared/            preamble, components, corpus_index, frontmatter, taxonomy, acronyms, term_authority, references.bib
└── source_witnesses/  copied byte-sealed source (cannon_*, gpt_ontology, rebuttal_round00)
```
(Note: `helios/` also contains sibling facets `00_src_specs/`, `01_src/`,
`01_src_specs/`, `01_data_src_specs/`, `papers_00_data_src_specs/` — OUT OF SCOPE
for this facet; mapped by other agents.)

---

## 1. The authoring machinery (this is load-bearing for W2)

Every mathematical/identifier occurrence in the papers is wrapped in a **4-argument
tagging macro** — this is the single most important structural fact of the corpus:

```latex
\SilTaggedMath{<expr>}{<URN-style occurrence id>}{<label>}{<description>}
\SilTaggedIdentifier{<text>}{<id>}{<label>}{<description>}
```

e.g. `\SilTaggedMath{\Hom_{\C}(A,B)}{p09.e000859}{hom-set from A to B in category C}{collects
precisely the morphisms with domain A and codomain B...}`. Each occurrence carries
its own stable id (`p09.e000859`, `v14-mig-math-0074`, `sem-v00-hf04-...`), a label,
and a ≥1-sentence description. **This is the corpus's realization of "the Frame is
the Yoneda point" / page-local semantic occurrence receipts**: every symbol is a
content-addressed atom with an inspectable profile, not raw typography. This is the
prose ancestor of SP1's per-triple DATA-CONTRACT discipline and the unary law's
"every occurrence is a typed navigable coordinate."

Each paper directory is itself an olog fragment with a fixed schema:
```
papers/NN_name/
├── paper.tex          \part + abstract + contractbox(es) + \input sections/00_content
├── metadata.tex       (usually a stub)
├── sections/          00_content, 01_thesis, 02_mittens_anchor, 03_olog_node_arrow_law,
│                      04_shared_diagram, 05_cannon_or_gpt_absorption, 06_closure,
│                      07..12 per-paper (per_leg_yoneda_profile, cheese_trap_face_closure,
│                      formal_appendices, capture_to_implementation_receipts, _diagram_audit)
└── chapters/          NN_name/{chapter.tex, sections/*.tex}   (deep-drilled variants)
```
The recurring section spine — **thesis → Mittens anchor → Node-or-Arrow law →
shared diagram → source absorption → per-leg Yoneda profile → cheese-trap closure**
— is the fixed publication contract every volume obeys.

---

## 2. FULL taxonomy — the paper volumes (papers/)

34 volumes (numbering skips to 41 for the cheese progenitor). File counts show
depth; the largest are the most drilled.

| Vol | slug | file-ct | what it establishes (W2 relevance) |
|----|------|-----|-----|
| 01 | orientation | 133 | corpus orientation, progenitor framing |
| 02 | music | 124 | (texture volume) |
| 03 | silmaril_federation | 80 | federation; gossip/replication (telephone-twin substrate) |
| 04 | forge | 62 | forge/template layer |
| 05 | granite_substrate | 77 | substrate |
| 06 | topology_jepa | 85 | **JEPA context–target interface; "five projections"; two anchors (Mittens identity + JEPA patch)** |
| 07 | the_canonical_question | 68 | the Bishop limerick / canonical question frame |
| 08 | visual_discipline | 72 | diagram/colour discipline (colour never sole carrier) |
| 09 | minimal_category_theory | 70 | **objects/arrows/identity/composition/associativity; the admission grammar** |
| 10 | graph_knowledge_graph_category | 74 | graph → KG → category |
| 11 | base_commutative_diagram | 129 | the base commuting-diagram governance; nth-dim bridge |
| 12 | cat_example_clarified | 36 | worked cat example |
| 13 | incoming_outgoing_profiles | 39 | **incoming/outgoing Hom-profiles (Yoneda two-sided)** |
| 14 | yoneda_lemma | 30 | **covariant/contravariant Yoneda; identity-by-representable-interface** |
| 15 | knowledge_graph_growth_around_mittens | 61 | KG growth |
| 16 | one_integrated_growing_knowledge_graph | 49 | single growing graph |
| 17 | commutative_diagrams_as_governance | 62 | commuting diagrams = governance law |
| 18 | presheaf_semantics | 66 | **presheaf P:Cᵒᵖ→Set as assertional population; contravariant pullback action** |
| 19 | mereology_as_colimit | 86 | **pushout/coequalizer as atomic gluing; colimit ≠ disjoint union** |
| 20 | functorial_transport | 72 | **ontology→schema as functor F; preserves id/∘; Σ⊣Δ⊣Π data migration** |
| 21 | ologs_and_typed_english | 82 | olog ↔ typed English readable layer |
| 22 | cco_style_ontology | 65 | **CCO-as-governed-growth; BFO upper stratification (universal anchor policy)** |
| 23 | rdf_style_data | 42 | RDF triple data layer |
| 24 | shacl_validation_and_path_constraints | 49 | **SHACL shapes + path constraints (SP1/SP7 ancestor)** |
| 25 | sheaf_gluing | 46 | **local records glue iff restrictions agree on overlaps; local→global** |
| 26 | adjunctions_free_graphs_governed_algebras | 80 | **free⊣forgetful; raw graph→governed algebra via adjunction; unit/counit** |
| 27 | kan_extensions | 33 | **Lan_A ⊣ ... ; migration is universal, not a rename table; unit η** |
| 28 | evidence_provenance_rule_of_three | 63 | **promotion needs 3 independent source legs; evidence as typed nodes/arrows** |
| 29 | avogadro_style_governance | 35 | Avogadro-scale governance |
| 30 | disintegration_reassimilation | 26 | split↔reassemble (render-seal ancestor) |
| 31 | path_monoids | 63 | path monoid / free category on graph |
| 32 | optimization_rules | 20 | optimization rules |
| 33 | yoneda_generalized_ontology | 16 | **"to model an object categorically is to know it by admissible arrows"; two-sided Hom(-,X),Hom(X,-)** |
| 34 | final_answer_canonical_question | 18 | synthesis; architecture incorporation ledger (nth-dim loss) |
| 41 | cheese_progenitor_topology | 24 | **the "cheese/progenitor" warning: a category is a useful servant, dangerous master; byte-sealed cheese source witness (SHA-256 pinned)** |

Common per-paper front matter: `\begin{contractbox}` defines **Lambda Blotto =
discrete Colonel Blotto** (finite integer allocation game `X_i={x∈ℕ₀^J : Σx_j=B_i}`,
payoff `M(x,y)=Σ w_j sgn(x_j−y_j)`, minimax/exploitability certificate) — "Lambda"
names the engine (eigen-towers + closed lambda term + Spark/Joern "Sparky"
map–shuffle–reduce machine) that *moves the same game*, never relaxes it.

---

## 3. FULL taxonomy — base volumes (base/)

### `base/00_whitepaper/` — Helios foundation (16 numbered section-groups + drilled chapters)
`sections/00_helios_foundation/` and `00_categorical_prelude/` are the **directly
W2-load-bearing** files (read in full):
- `00_helios_foundation/04_olog_yoneda_points.tex` — presented olog `O = Path(G)/∼R`
  is a category; **Yoneda point law** `Nat(yA,F) ≅ F(A), η ↦ η_A(1_A)`. This is the
  exact theorem SP1's `taiji.ttl` materialises (representables + `yonedaObject` +
  `NaturalitySquare` + "Frame IS the Yoneda point").
- `00_helios_foundation/05_carrier_towers_triad.tex` — **THE S/O/P + colour source.**
  Defines `Oct={0..255}`, `RGB={R,G,B}`, `Vec(Oct)=∐ₙ Octⁿ`; two **disjoint
  nominal carriers** `Q_A={aTag}×RGB×Vec(Oct)`, `Q_G={gTag}×RGB×Vec(Oct)` with
  `Q_A ∩ Q_G = ∅` (Atlas vs Graph, same payload, distinct outer tag → tag-erasure
  is a many-to-one forgetful map, not equality). **Subject/Object/Predicate live in
  three independent tower categories `K_S,K_O,K_P` — there are NO positional maps
  `S→R`, `O→G`, `P→B`.** Terminal drill cites the live Scala Taiji tree
  `.../primordial/geometry/taiji/Taiji` with `Color/{Red,Green,Blue}/Value.scala`
  each descending independently from the octet-vector carrier.
- `00_helios_foundation/06_frame_sort_separation.tex` — **the word "frame" is 6
  disjoint sorts**: `F_cap` (capture/provenance keys), `F_auth` (authoring/build/lens
  variants), `𝔽_lin=(F,id,ρ,parent,kind,meta,≺,succ)` (native lineage/time carrier),
  `P_I` (JEPA image spatial regions), `Frame(O,E):=O×E` (**output×effect — the unary
  law's `Frame(output:X, error/effect:Y)`**), `T_vid` (video time). Capture-time ≠
  native-Frame-time. This is the source of SP1's Frame monad / the design_constraints
  `T → Frame(output:X, error|effect:Y)` law.
- `00_helios_foundation/07_science_wave_bfo_safety.tex` — **the CCO/BFO upper-anchor
  policy** (= `universal_anchors`). BFO bridge functor `U: O_sci → B` separating
  continuants `C` / occurrents `P` / temporal regions `T`; CCO information-artifact
  extension with `c ≠ χ_h ≠ h` (content ≠ inscription-quality ≠ material bearer). BFO
  and CCO are **bridge vocabularies, not additional concrete proof anchors**.
- Other foundation sections: `01_accessibility_clause` (research-access cost / feasible
  inquiry — the economic thesis), `02_ecosystem_free_monoid`, `03_graph_atlas_dag_traces`,
  `08_information_acid_fluid_transport`.
- `00_categorical_prelude/`: `00_threshold_and_thesis`, `01_olog_contract`,
  `02_mittens_seed`, `03_node_arrow_bridge` (admission factors prose through typed
  graph structure), `04_soul_spine`, `05_spec_materialization`, `06_opening_contract`.
- Whitepaper section-groups 01–16: signature calculus, twelve-leg deep dive, publish-gate
  failures, sous-profile law, cheese-trap face catalog, **free-monad algebra book**,
  **Yoneda profile drill**, cross-paper bridges, diagram-law catalog, negative-regression
  atlas, worked-examples book, spine inheritance contracts, **limit–colimit zoo**,
  per-leg Yoneda profiles, formal appendices, r14 progressive family closure.

### `base/00a_node_arrow_corpus_spine/` — the admission law
11 chapters: node typology, arrow typology, **forbidden shortcut catalog**, per-leg
representable views, cross-paper bridges, **admission term normal forms**, capture
provenance contract, **lambda_blotto node–arrow engine**, architecture capability
boundaries, page-local semantic readback, r14 progressive family closure. Its thesis
carries the **telephone twin** (§5 below): "Telephone/Pythagoras and Sparky/Rosetta
do not replace a language leg's own render receipt."

### `base/00b_source_node_cocone_register/` — the cocone accounting surface
Registers every source **leg slot** of the Mittens source-diagram functor
`D_Mittens` and which volumes populate each. Explicitly names the **ecosystem
closure families**: "the independent S/O/P tower product and Atlas/Graph RGB byte
pair; the canonical Lambda-Blotto/discrete-Colonel-Blotto model, with δ as its
operational transition; an optional project-authored projection/readback interface
and its micro-partition comparison." Chapter 01 = "index category J (Mittens anatomy)."

---

## 4. FULL taxonomy — appendices, shared, witnesses

### appendices/ (5)
- **35 A — notational_summary** (`sections/00_content.tex`, 2,229 lines): the master
  notation glossary/legend.
- **36 B — minimal_categorical_commitments** (1,182 lines + `01_hyper00_proof_certification`,
  `02_e_monad_morphism_strength`): the minimal categorical axioms + a **monad
  morphism/strength** appendix (the monadic-realization ancestor of SP1's Kleisli layer).
- **37 C — node_arrow_foundation** (2,108 lines): the formal node–arrow mathematical
  foundation (free category on typed directed multigraph, presentation `⟨G|R⟩`).
- **38 D — research_phases**: the `2026-05-13_3_agent_dag` research runs (agent
  01/02/03 traces, claim indices, relation candidates, coordinator evaluation) +
  `_round2` + `_final`. Marked **explicit projection debt** in `corpus_index.yaml`.
- **39 E — research_source_mirror**: **THE AOB / SPEC-ATOM MIRROR** (§6). Rendered
  `.tex` mirror of the real spec system: `specs/types/` (prelude, foundation,
  layer_0_src, layer_minus1_kernel, layer_minus2_isa {x86,arm,riscv},
  layer_minus3_uefi, layer_2_domain, papers, pybrain_herodotus), `specs/atoms/`
  (271 `_aob_*` atom files: core/{aio,entity,service,...}, dag/{scheduler,executor,...},
  foundation/{logging,trace}), `specs/data/research/` (per-source citation_targets/
  claims/terms for avro, i-jepa, v-jepa, fong_spivak, lecun, linkml, spivak_ologs,
  w3c_rdf11/shacl/sparql11, etc.), `specs/{shapes,linkml,ontology,glue,engine,
  integration,domains}`. **1,931 `.spec.yaml.tex` + 271 atoms — sampled, not
  exhaustively read.** Also marked projection debt.

### shared/
- `preamble.tex`, `metadata.tex`, `acronyms.yaml` (BFO→Basic Formal Ontology,
  CCO→Common Core Ontologies, DAG, CRDT, CUDA...), `term_authority.yaml` (citation
  authority per sensitive name; Mittens = `local_colimit_anchor`, Felis catus = taxonomy
  leg only, NOT Mittens identity), `references.bib` + `research_appendix.bib`.
- `corpus_index.yaml` + `corpus_index/` — the **ledger**: one entry per src file,
  classes {projected_entry_content, generated_research_mirror, shared_build_support,
  source_witness, held_auxiliary}; per-paper `owned_files` manifests.
- `components/` — the LaTeX component grammar: `math/` (incl. `lambda_blotto_model.tex`
  — telephone), `diagrams/` (grammar, patterns, legends, styles; incl.
  `patterns/projection/source_dimension_planes.tex` and `perceptual_color_towers_3d.tex`),
  `boxes/environments.tex` (thesis/contractbox/principle envs), `acronyms/`, `code/`,
  `design/colors.tex`, `navigation/` (projection_registry, volume_projection),
  `accessibility/`, `layout/`, `standards/`, `text/`.
- `frontmatter/` — `lambda_blotto_formal_preamble.tex` (fixes the game/spectral/
  lambda/frame/Gremlin objects for all volumes) + `poem_preface.tex`.
- `taxonomy/` — the CSV witness tables: `taxon_nodes.csv`, `taxon_edges.csv` (ITIS
  hierarchy), `mittens_type_leg.csv` (Mittens `has_type_classification_leg` Felis catus
  TSN 183798, with explicit `invalid_identity_*` columns = negative-regression guards),
  `catus_collision_index.csv`, `taxonomy_quality_flags.csv`, `taxonomy_validation_rules.md`.

### source_witnesses/ (byte-sealed copied source, 13 families)
`cannon_{bootstrap,cheese,language,observation,paradigm,physics,runtime,soul,tax,
templates,workflow}`, `gpt_ontology` (6 files incl. the v90 Yoneda hom-profile
manifest, v100 governed ontology), `rebuttal_round00` (the `gippidy00.md` adversarial
challenge). `cannon_cheese/cheese.md` = 53,986 bytes, SHA-256
`caca30a0…1961`, included byte-identically into Vol 41 (Präriehund: source witnesses
supply *pressure*, never authority; they are not promoted merely by appearing).

### node_arrow/
`Silmaril_NodeArrow_Corpus_Monograph_v12.md` (7,466 lines, SHA-256 `e0b7806a…7207`,
imported 2026-05-13) + `manifest.yaml`. The standalone monograph that states the
founding law: **"everything admissible is a node or an arrow"**; the corpus is a
diagram `D:J→C_Corpus` and the artifact is a **cocone** `λ_j:D(j)→W` with
`W=ObservedProjection(ColimCandidate(D))` (honest: not literally the colimit). Carries
Lambek fixed point `X≅F(X)`, coalgebra `ξ:X→F(X)`, bialgebra distributive law, and the
`Σ_F⊣Δ_F⊣Π_F` migration triad — the whole SP1 vocabulary in one place.

---

## 5. W2-LENS extractions (what SP1 grounds into / corrects)

- **AOB atom shape.** The AOB atoms are literal here: `appendix E specs/atoms/`
  holds 271 `_aob_*.yaml.tex` (e.g. `_aob_entity_register`, `_aob_entity_transition`,
  `_aob_entity_generate_id`, `_aob_entity_add_tag`). Every atom spec carries
  `entity.{urn,kind_urn,layer,ancestry[axis/via],citations[note/source],grounding,
  display_name}` + `triad_render.{bash_namespace, elixir_module, haskell_module,
  scala_package, out_paths.{bash,elixir,haskell,scala}}`. The URN idiom
  `urn:silmaril:entity#types.prelude.byte_order_little` = SP1/SP2's full-lexical URN.
  `sha256` identity appears as the byte-seal of every source witness and the
  `SHA-256 digest = 256-bit digest of the UTF-8 bytes of one canonical URN` gloss in
  `source_dimension_planes.tex`.
- **Progenitor / protogenitor pattern (the "model every distinct thing as its own
  atom").** Directly present as spec families where an **agnostic progenitor node**
  has explicit children: `byte_order` → `byte_order_{little,big,host,none}`;
  `arithmetic` → `{none,saturate,trap,wrap}`; `cardinality` → `{one,maybe,many,
  unresolved}`; `charset` → `{ascii,latin1,utf8,utf16be,utf16le}`; `domain_kind` →
  `{continuous,discrete,enum,opaque}`; `dynamics` → `{mutable,snapshot,stream,
  observation_collapse}`; `edge_rel` → `{calls,cites,composes,consumes,emits,
  implements,needs,wants}`; `comment_prefix` → `{hash,double_dash,double_slash,
  percent,semicolon}`. Each child's `ancestry.via` points at the agnostic parent URN.
  **Endianness is exactly the maintainer's worked example**: `byte_order` is the
  agnostic progenitor, `byte_order_little`/`byte_order_big` its BE+LE children,
  grounded in `feedback_tensor_three_axis_space_time_value.md`.
- **ISA/UEFI dual grounding (Directive 3).** `appendix E specs/types/` is layered
  `layer_minus3_uefi` (uefi_boolean, uefi_char8/char16, uefi_common_data_type,
  calling conventions x64/aarch64/riscv), `layer_minus2_isa` (isa_byte→{armv8,riscv},
  isa_word→{armv8,riscv}, isa_call_conv, x86 cpuid leaves / call-gate descriptor),
  `layer_minus1_kernel`, `layer_0_src`, `prelude`, `layer_2_domain`. This is the
  physical facet ISA/UEFI machine-type tower the depth floor bottoms out into.
- **Full projection family + nth-dimensional effect/loss.** Vol 06 (topology_jepa)
  = "five projections" (typed olog / Yoneda / carrier-projection / functional-programming
  charts, JEPA context–target). `shared/components/diagrams/patterns/projection/
  source_dimension_planes.tex` fixes the **projection edge-key** (information/source,
  executed process, admitted quality/readback, refusal/non-implication) reused by
  Honeycomb / Sparky / GraphAtlas dimensional views, and defines rank-0 `S:P:O`
  external order vs internal role order `S:O:P` (a materialized effect/loss between
  projections). nth-dim loss bridges: `papers/11_base_commutative_diagram/.../
  02_bridge_disintegration_reassimilation.tex` and
  `papers/34_final_answer.../12_architecture_incorporation_ledger.tex`.
- **Geometer/glossary axes vs towers.** The carrier-towers section keeps colour
  channels (a,b / R,G,B) STRICTLY separate from S/O/P role towers — "no implicit
  positional maps." The `perceptual_color_towers_3d.tex` + TOWERS terminal drill give
  per-frame perceptual geometry `(V_f,E_f,F_f,w_f,ℓ_f,ε_f)` — dimension is per-Frame/
  per-geometer, never a jump straight to S-O-P towers.
- **universal_anchors = CCO/BFO.** `07_science_wave_bfo_safety.tex` + Vol 22: BFO
  upper stratification (continuant/occurrent/temporal-region; object≠process,
  quality≠bearer, ICE≠its subject, identifier≠designatum, measurement≠literal), CCO
  as mid-level reusable infrastructure. Policy = **bridge vocabularies only, not
  concrete proof anchors** — load-bearing but non-authoritative.
- **Telephone twin (Directive 6).** `Telephone` appears 121× (top in
  `lambda_blotto_model.tex`, `source_dimension_planes.tex`, the node–arrow spine
  thesis, Vol 41). It is the **candidate render/comparator + rejection machinery**
  (target manifests, hashes, checker readback, comparator readback = its
  receipt-construction gate), twinned with **Sparky/Rosetta** and named alongside
  **Pythagoras**. It is the counterfactual/comparison twin of the render engine —
  exactly the "twin mention" Directive 6 wants realized at Yoneda tightness. (Präriehund:
  I did not open `lambda_blotto_model.tex` in full — this is from the spine thesis +
  grep context; the precise Telephone/Pythagoras olog is in `base/00a` and Vol 41.)
- **Yoneda / functorial-transport / presheaf / colimit / sheaf-gluing (the SP1 floor).**
  All present as authored theorems: Yoneda point law (whitepaper §04, Vol 14, Vol 33);
  presheaf `P:Cᵒᵖ→Set` assertional population (Vol 18); ontology→schema functor +
  `Σ⊣Δ⊣Π` (Vol 20, monograph); pushout/coequalizer colimit gluing, colimit≠disjoint-
  union (Vol 19); sheaf local→global gluing on overlap agreement (Vol 25); free⊣forgetful
  adjunction (Vol 26); Lan universal migration with unit η (Vol 27); path monoids /
  free category (Vol 31); monad morphism & strength (App B).

---

## 6. How this GROUNDS / CORRECTS the SP1..SP9 floor

SP1 (`basicttl/primitives/README.md`) is a **machine-checked re-derivation** of what
srcy authored in prose+diagrams:

- **SP1 Primitive Floor** — srcy is its literal source. taiji.ttl's twin-olog colimit
  = the Atlas/Graph disjoint-carrier + Mittens-cocone construction (whitepaper §05,
  Vol 19, monograph). The Frame monad = `Frame(O,E):=O×E` frame-sort (§06). The
  literal-Yoneda layer (representables, `NaturalitySquare`, "Frame IS the Yoneda point")
  = Yoneda point law (§04) + Vol 14/33. Kleisli/monad-law layer = App B monad
  morphism/strength. **Correction srcy forces on a naive floor:** the whitepaper's
  `Q_A∩Q_G=∅` and "no positional `S→R/O→G/P→B` maps" say the floor must NOT collapse
  colour channels into S/O/P roles — SP1 keeps RGB (`q_rgb`) and S/O/P separate, which
  is faithful to this.
- **SP2 AOB meta-ontology** — the AOB atom shape (`_aob_*` + `entity.{urn,ancestry,
  citations,grounding}` + `triad_render`) is authored in appendix E; SP2 must lift THIS
  shape, not invent one. The progenitor/child ancestry (`byte_order`→little/big) is the
  protogenitor pattern SP2 formalizes.
- **SP3 S/O/P CRS** — grounded by whitepaper §05 (three independent tower categories,
  octet/Vec(Oct) carriers) and 00b's "independent S/O/P tower product + Atlas/Graph RGB
  byte pair." The `z`/sha256 identity idiom appears in `source_dimension_planes.tex`.
- **SP4 projection packet / loss** — Vol 06 five projections + the projection edge-key +
  `S:P:O` vs `S:O:P` order effect + nth-dim bridges (Vol 11/34).
- **SP5 file+format taxonomy** — appendix E `specs/types/prelude/format*` (avro/json/
  ex/hs...), charset/comment_prefix/byte_order progenitor families.
- **SP6 glossary polysemy** — `term_authority.yaml` (per-name citation authority,
  same term = different epistemology), the frame-sort separation (one word "frame" = 6
  sorts), cheese-trap negative-regression (Felis catus ≠ Mittens).
- **SP7 SHACL law** — Vol 24 (SHACL + path constraints) + appendix E `specs/shapes/`.
- **SP8 basicttl depth remediation** — the ≥200-char described occurrence macro is the
  authored precedent for the depth-comment discipline.
- **SP9 render seal** — Vol 30 disintegration↔reassimilation + `local_encyclopedia.tex`
  split/aggregate projection = the split↔consolidated reversibility.

**Net:** srcy is the theory; SP1..SP9 are the executable, teeth-bearing TTL/SHACL/SPARQL
re-derivation. srcy's honesty constraints (cocone `W=ObservedProjection(...)` not
`colim`; witnesses are pressure not authority; no positional colour/role collapse;
telephone/Sparky comparators don't replace per-leg receipts) are the corrections that
keep SP1 from over-claiming.

---

## 7. Coverage statement (Präriehund)

- **Tree/taxonomy: FULL** (7,261 files / 1,117 dirs enumerated; every paper, base
  volume, appendix, shared subdir, witness family named).
- **Read IN FULL:** the 4 mandatory repo files; paper 09 paper.tex + thesis; theses of
  papers 14/18/20/25/26/27/33 + 22/28/06; whitepaper foundation §04/05/06/07 +
  categorical-prelude §03; node–arrow monograph head (Parts I–II); `local_encyclopedia.tex`;
  `source_dimension_planes.tex`; the `byte_order_little` spec; corpus_index + taxonomy CSVs.
- **SAMPLED (broad, characterized by schema, NOT read individually):** the ~1,931
  `.spec.yaml.tex` + 271 `_aob_*` atom files in appendix E (schema lifted from
  `byte_order_little`, the atom listing, and the layer tree); the chapters/ deep-drill
  subtrees of each paper (structure confirmed, prose not exhaustively read); the 13
  source-witness families (sizes + roles, cheese witness header only); appendix A/B/C/D
  bodies (line counts + section headings, not full prose).
- **NOT opened in full:** `lambda_blotto_model.tex`, the 7,466-line monograph past Part II,
  App D agent-trace CSVs. Telephone-twin detail is from spine-thesis context + grep, not a
  full read of its olog — flagged PROVISIONAL for the precise Telephone/Pythagoras diagram.
