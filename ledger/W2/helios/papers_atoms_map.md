# HELIOS facet map — `papers_00_data_src_specs` (the per-paper AOB atom SOURCE-OF-TRUTH for SP2)

> Präriehund honesty up front. This facet is **17,071 `.spec.yaml` atom files** across **11 categorical
> papers**. I read ~18 files IN FULL spanning 4 papers (09, 11, 19, 20) and every one of the **22
> distinct `type_node` atom families**, then characterized the shared schema and the per-paper
> organization from corpus-wide structured greps (type_node counts, type_urn families, Atlas columns,
> CCO/CPO IRIs, ancestry axes, universal-anchor URNs, filename-suffix families). I did NOT open all
> 17k files; where I state a per-family field list it is from a representative full read plus a
> whole-corpus grep of that field, and I say so. Nothing below is claimed as read that was sampled.

Zip facet root on disk: `/home/user/silmaril/helios/papers_00_data_src_specs/`
(git-ignored WIP; sibling facets under `helios/`: `00_src_specs`, `01_data_src_specs`, `01_src`,
`01_src_specs`, `srcy`. This facet is the **data + src + specs** cut for the papers.)

---

## 0. What this facet IS, in one sentence

It is the **materialized atom instance store** for 11 of the 34 categorical papers: every paper is
exploded into a tree of tiny typed YAML "spec" atoms — one atom per semantic thing (a section, an
olog box, one Yoneda leg, one concrete anchor, one synonym pair, one acronym, one circuit imprint,
one typed key:value attribute) — each carrying a URN identity, a CCO/CPO grounding, a Linnaean
taxonomy placement, an Atlas-column contribution, and an Elixir render target. **This is the real
WIP AOB that Directive 1 says to LIFT, not invent** — but at a *higher* altitude than SP1's byte
floor (see §7 for exactly what SP2 must ADD when it lifts these).

---

## 1. Directory taxonomy (the tree IS the taxonomy)

```
papers_00_data_src_specs/
├── 09_minimal_category_theory/            2,442 atoms  (chapters 1,894 + flat sections 548)
│     chapters/{01_objects_and_arrows … 08_cross_paper_bridges}/  (8 chapters)
│     sections/                            flat wave-D relational/lexical atoms
├── 10_graph_knowledge_graph_category/       137 atoms  (27 + 110)   [3 chapters]
├── 11_base_commutative_diagram/           8,909 atoms  (8,616 + 293)  ← the giant (52% of facet)
│     chapters/{01_core_theorems … 27_governance_shacl_deep_dive}/  (27 chapters)
├── 15_knowledge_graph_growth_around_mittens/ 1,030 atoms  (916 + 114)  [8 chapters]
├── 16_one_integrated_growing_knowledge_graph/  281 atoms  (166 + 115)  [6 chapters]
├── 17_commutative_diagrams_as_governance/    443 atoms  (338 + 105)  [7 chapters, incl. 00_thesis]
├── 18_presheaf_semantics/                  1,275 atoms  (896 + 379)  [7 chapters]
├── 19_mereology_as_colimit/                  886 atoms  (777 + 109)  [14 chapters]
├── 20_functorial_transport/                  483 atoms  (316 + 167)  [8 chapters]
├── 21_ologs_and_typed_english/               997 atoms  (895 + 102)  [8 chapters]
└── 25_sheaf_gluing/                          188 atoms  (89 + 99)    [1 chapter only — WIP stub]
                                            ─────────
                                            17,071 total .spec.yaml
```

Two-level layout inside every paper:
- **`chapters/<NN_slug>/sections/<section>_<companion>.spec.yaml`** — the bulk. Each *paper section*
  (lifted from `src/papers/<paper>/chapters/<ch>/sections/<sec>.tex`) spawns a **companion bundle**
  of atoms (see §3). This is where the ~7k AdditionalAttributes + ConcreteAnchors + Yoneda legs live.
- **`sections/` (flat, paper-root)** — cross-cutting **relational / lexical** atoms not tied to one
  section: Synonym, Antonym, PreferredTerm, Acronym, Citation, Diagram, EnumMembership, Replacement,
  Translation, plus wave-D "replacement" and "local rebuttal witness" atoms.

Every file is `spec_version: 1`. `layer:` is `papers` (15,652) or `base` (1,419 — Citations,
Examples, cross-paper bridges that ground into the base layer).

---

## 2. The universal atom SCHEMA (the AOB envelope)

Every `.spec.yaml` is one atom with this exact top-level shape (verified across all families):

```yaml
# provenance comment: what this atom is, which Wave/pass authored it, which Atlas col it fills,
#                     which CCO/CPO IRI grounds it
spec_version: 1
entity:
  urn:          urn:silmaril:entity#instances.papers.<paper>.<...path...>.<companion>   # the identity
  display_name: <CamelCasePathName>
  layer:        papers | base
  kind_urn:     urn:silmaril:entity#types.prelude.kind_node_instance                    # it's an instance node
  type_node:    <AtomKind>              # one of the 22 families in §4
  type_urn:     urn:silmaril:entity#types.papers.<ORDER>.<family>                        # Linnaean placement
  grounding:    '<≥1 sentence prose: what it asserts + the CPO/CCO process that licenses it>'
  fields:       <family-specific — a mapping OR a list of records; see §4>
  ancestry:
    - {axis: paper,   via: urn:silmaril:entity#papers.<paper>}
    - {axis: phylum,  via: urn:silmaril:entity#types.papers}          # (only on fully-taxonomized atoms)
    - {axis: order,   via: urn:silmaril:entity#types.papers.<order>}
    - {axis: family,  via: urn:silmaril:atom-family:arrow:<family>}
triad_render:
  elixir_module: Silmaril.Instances.Papers.P<NN><Paper>.<...>.<Kind>
  out_paths:
    elixir: lib/silmaril/instances/papers/<paper>/<...>/<companion>.ex
```

### Identity
- **URN is the identity** — `urn:silmaril:entity#instances.papers.<paper>.<path>.<companion>`.
  Sub-atom targets use a `#fragment` (e.g. `…concrete_anchor#domesticcat`). **There is NO `sha256`
  field anywhere in this facet** (grep: 0 hits). Identity is the structured URN, not a content hash —
  this is exactly the gap SP2/SP1 must close (SP1's sha256 identity + `z = uint16(first two
  source_sha256 octets)` CRS are NOT present here; they are added on lift).

### The Linnaean taxonomy (the "type tower" for atoms)
`type_urn` places every atom in **PHYLUM=papers → ORDER → FAMILY**. The four ORDERS observed
(by `type_urn` prefix count): `identity_label` (7,264), `silmaril_wave8` (5,681), `prose` (3,142),
`relational` (984). `ancestry` re-states this as explicit axis edges (`phylum`/`order`/`family`),
but only 256 atoms carry the full 4-axis ancestry; **all 17,071 carry the `paper` axis** (the paper
is the always-present progenitor — the paper-monad).

### CCO/BFO grounding (the upper-ontology anchor)
Every atom names a **CCO (Common Core Ontologies) or CPO (CommonCoreOntologies Process)** IRI in
`cco_grounding_iri` / `cpo_process_iri` / inline in `grounding`. Top IRIs by frequency:
`ont00000649` (3,552), `ont00000686`, `ont00000853` (Descriptive ICE, ~3k across spellings),
`ont00000958`, `ont00001069`, `ont00000005`; processes `ActOfInterpretation`, `SemanticComparing`,
`IsomorphicComparing`, `Classification`, `ActOfJudging`, `ResemblanceComparing`, `ActOfCharacterization`.
This IS the CCO/BFO upper-ontology anchor the W2 lens calls `universal_anchors` — but note it is
**CCO-only here; no BFO IRI and no `universal_anchors:` block** appears (see §6 decision).

### Render target (the triad)
`triad_render.elixir_module` + `out_paths.elixir` — every atom compiles to one Elixir module under
`lib/silmaril/instances/papers/…`. Only the **Elixir** leg of the FP triad (Haskell/Elixir/Scala) is
emitted here; consistent with unary-law framing that Elixir is the instance-render surface.

---

## 3. The atom-family BUNDLE — the protogenitor pattern in action

The single most important structural fact: **one paper section is NOT one atom. It is a colimit of
~6–15 co-located companion atoms**, each a distinct thing modeled as its own file — the literal
"model every distinct thing as its own atom, nothing crammed" (protogenitor) doctrine. Worked example
(`19_mereology…/chapters/07_index_category_anatomy/sections/01_index_category_anatomy_of_J_Mittens`):

```
01_index_category_anatomy_of_J_Mittens.spec.yaml                  → PaperSection (the apex, lists companion_atoms[])
  ├─ …_olog_box.spec.yaml                                         → OlogBox   (typed_in/out_arrows, commuting_law)
  ├─ …_decomposition_step.spec.yaml                               → DecompositionStep (6 zero-math reader steps)
  ├─ …_concrete_anchor.spec.yaml                                  → ConcreteAnchor (bare_symbol → anchor_node map)
  │    ├─ …_concrete_anchor_example.spec.yaml                     → Example   (Mittens/Tartu-clinic domain story)
  │    ├─ …_concrete_anchor_addl_paper_kind.spec.yaml             → AdditionalAttributes (paper_kind = <paper urn>)
  │    ├─ …_concrete_anchor_addl_dunbar_layer.spec.yaml           → AdditionalAttributes (dunbar_layer = 0..N)
  │    ├─ …_concrete_anchor_addl_base_topic.spec.yaml             → AdditionalAttributes (base_topic = <topic>)
  │    └─ …_concrete_anchor_addl_circuit_corner.spec.yaml         → AdditionalAttributes (legacy_circuit_coordinate)
  ├─ …_yoneda_hom_leg.spec.yaml                                   → YonedaHomLeg (list of typed legs, monic_hypothesis)
  │    └─ …_yoneda_hom_leg_example.spec.yaml                      → Example
  ├─ …_cheese_trap_immunity.spec.yaml                             → CheeseTrapImmunity (failure_mode + immunity_mechanism)
  └─ …_circuit_imprint_tensor.spec.yaml                           → CircuitImprintTensor (Leary 8-circuit multi-hot)
```

The **PaperSection apex** carries `companion_atoms: [<urns>]` — the cocone legs. The 4 `addl_*`
variants are the **"universal-metadata projection"** that "already rides the row"; each concrete
anchor is decorated with exactly four typed key:value attributes (`paper_kind`, `dunbar_layer`,
`base_topic`, `circuit_corner`) — 1,776 of each, in lockstep. This is where 7,104 of the 17,071
atoms come from (AdditionalAttributes = the largest family precisely because each anchor spawns 4).

---

## 4. The 22 atom families (`type_node` census + field schema)

Full corpus count of `type_node` (grep over all 17,071):

| # atoms | type_node | ORDER | key `fields` (from full reads) |
|--------:|-----------|-------|--------------------------------|
| 7,104 | **AdditionalAttributes** | identity_label | `attribute_key`, `attribute_value`, `target_atom_urn`, `cco_grounding_iri` |
| 1,757 | **Description** | prose | list of `{description_text, target_atom_urn, register, cco_grounding_iri}` (1 per anchor) |
| 1,645 | **ConcreteAnchor** | silmaril_wave8 | list of `{bare_symbol, anchor_node, anchor_text}` |
| 1,343 | **YonedaHomLeg** | silmaril_wave8 | list of `{leg_name, from_object, to_object, arrow_type, monic_hypothesis, witness_quote, failure_quote_local}` |
| 1,295 | **Example** | prose | `example_text`, `target_atom_urn`, `cco_grounding_iri` |
| 1,292 | **DecompositionStep** | silmaril_wave8 | list of `{step, kind, theorem_index, symbol, reads_as, base_topic, base_topic_cite, concrete_anchor, recap}` (canonical 6 steps) |
| 384 | **Translation** | relational | `source_term/source_dialect → target_term/target_dialect`, `target_atom_urn`, `cpo_process_iri` |
| 367 | **Atom** / **AtomBundle** | silmaril_wave8 | `atoms: [ {kind, type_urn, …inline atom…} ]` — a *bundle* cramming many typed sub-atoms in one file (see §4b) |
| 320 | **CheeseTrapImmunity** | silmaril_wave8 | `failure_mode`, `failure_quote_local`, `failure_quote_witness`, `immunity_mechanism`, `immunity_guard_clause`, `cheese_trap_resistance_score` |
| 319 | **OlogBox** | silmaril_wave8 | `box_name`, `typed_in_arrows[]`, `typed_out_arrows[]`, `commuting_law`, `domain_portability` |
| 315 | **CircuitImprintTensor** | silmaril_wave8 | the tensor block — see §5 |
| 221 | **Synonym** | relational | `left_term`, `right_term`, `synonym_term`, `directionality`, `source/target_atom_urn`, `cpo_process_iri` (SemanticComparing) → **Atlas col 10** |
| 214 | **Antonym** | relational | `left_term`, `right_term`, `antonym_atom_urn`, `source/target_atom_urn`, `cpo_process_iri` (IsomorphicComparing) → **Atlas col 17** |
| 124 | **Citation** | identity_label | `citation_key`, `bib_entry_summary`, `kind`, `role`, `cco_grounding_iri` |
| 90 | **Acronym** | prose | `short_form`, `expansion`, `status`, `cco_grounding_iri` (ont00001238 initialism) → **Atlas col 5** |
| 77 | **EnumMembership** | relational | `enum_type_urn` (→ `universal-anchor:node:enum:*`), `enum_value`, `member_value`, `cpo_process_iri` (Classification) → **Atlas col 9** |
| 56 | **PaperSection** | silmaril_wave8 | `section_title`, `chapter_slug`, `section_slug`, `companion_atoms[]` (the cocone apex) |
| 55 | **PreferredTerm** | relational | `preferred_term`, `less_preferred_term`, `style_guide_reason`, `cpo_process_iri` (ActOfJudging) → **Atlas col 19** |
| 36 | **Diagram** | identity_label | `figure_label`, `caption`, `kind` (free/ref), `cco_grounding_iri` (ont00002004 ICE) |
| 33 | **Replacement** | relational | `deprecated_term`, `replacement_term`, `reason` → **Atlas col 11 ReplacedBy** |
| 23 | **AtomBundle** | silmaril_wave8 | (see Atom row) |
| 1 | **Section** | — | singleton |

### 4b. AtomBundle — the anti-pattern-shaped exception
The `Atom`/`AtomBundle` files (e.g.
`20_functorial_transport/…/02_revised_functorial_transport.spec.yaml`) put a whole companion set
(DecompositionStep×6, ConcreteAnchor×3, YonedaHomLeg×2, CheeseTrapImmunity, OlogBox,
CircuitImprintTensor) **inline in one file** under `atoms: [{kind, type_urn, …}]`. This is the
*crammed* form the split-render seal (unary law §"Split and Consolidated Render Seal") would later
normalize back to one-thing-per-file. Its presence is itself evidence of the WIP tension between the
protogenitor "one atom per file" ideal and pragmatic bundling.

---

## 5. The tensor block — `CircuitImprintTensor` (S/O/P evidence, Leary-cube style)

The W2-lens "tensor block / S-O-P tower evidence" is realized here as the **Leary 8-circuit
multi-hot imprint**, NOT as a byte tensor. Schema:

```yaml
type_node: CircuitImprintTensor
fields:
  imprinted_atom_urn:      <the atom this tensor decorates>
  imprinted_field_name:    <which field carries the claim, e.g. commuting_law / claim_at_corner>
  native_frame_urn:        <the Frame that must witness support>
  active_circuit_urns:     [ 'urn:silmaril:leary-circuit:c3_symbolic_neurosemantic', … ]  # the multi-hot support
  circuit_name_readback:   [ 'C1: Bio-Survival' … 'C8: Quantum Non-Local Integration' ]   # the 8-axis basis
  declared_relation_witness_urns:  []     # relations REJECTED until a native-Frame witness + readback
  relation_readback_receipt_urns:  []
  support_readback_receipt_urn:    <receipt>
  cheese_trap_guard:       '<why the naive binary-cube / Hamming-adjacency reading is rejected>'
```

Load-bearing discipline (verbatim from grounding): *"Binary axes, cube/Hamming adjacency, and inferred
relations are rejected. Additional support and every directed relation require native-Frame witnesses
and readback."* — i.e. the tensor is an **explicit sparse support over an 8-dimensional basis**, and
adjacency/relations may not be *inferred* from coordinates; they must be *witnessed*. This is the
per-atom, per-geometer, nth-axis geometry (the 8 Leary circuits are one geometer's axis system),
directly echoing the unary law's "S/O/P are independently typed nth-dimensional towers; a scalar
triple is not an admissible substitute." The `addl_circuit_corner` attributes retain *legacy*
integer circuit coordinates but explicitly refuse to admit them as C1–C8 support without a witness.

---

## 6. W2-lens findings — what IS and IS NOT here

**Present (the AOB atom source-of-truth):**
- **Atom envelope**: URN identity, type_node/type_urn Linnaean tower, CCO/CPO grounding, ancestry
  axes, Atlas-column contribution, Elixir triad render. (§2)
- **Protogenitor / composability**: one-thing-per-atom companion bundles; PaperSection apex as
  cocone; 4 lock-step `addl_*` metadata projections per anchor. (§3)
- **S/O/P + towers (categorical form)**: YonedaHomLeg (`from_object`/`to_object`/`arrow_type` =
  the hom-profile legs), OlogBox typed_in/out arrows, CircuitImprintTensor multi-hot support. (§5)
- **Synonym/Antonym polysemy**: same term carried as synonym (col 10, SemanticComparing) AND antonym
  (col 17, IsomorphicComparing) — the "structured AND unstructured as synonyms AND antonyms" of
  Directive 1, realized as separate CPO-grounded relational arrows. (§4)
- **CCO upper-ontology anchor**: every atom grounded to a CCO/CPO IRI. (§2)
- **The Atlas ring**: a fixed metadata-column table (cols 5,7,9,10,11,16,17,19 observed — see §4);
  each atom family is the *contributor* to specific Atlas columns.
- **Cheese-trap immunity**: every section carries an explicit failure-mode + immunity-mechanism atom
  (the Präriehund "don't collapse the category" discipline made a first-class atom).

**Absent here — the delta SP2 must ADD on lift (Präriehund: not in this facet):**
- **No `sha256` / content-hash identity** (0 hits). Identity is URN-structural only.
- **No group law** — no `identity`/`compose`/`retract` fields; `retract` appears 4× only in prose.
- **No subatomic octet decomposition, no byte/tensor byte-block, no bit-vector carriers** — nothing
  descends to the Bit→Octet→ByteVector floor. `endian`/`byte_order`/`nth_dim`/`geometer`/`S_tower`:
  **0 hits each**.
- **No `universal_anchors:` block and no BFO IRI** — grounding is CCO/CPO only; the only
  `universal-anchor` URNs are two enum anchors (`node:enum:milestone` ×220, `node:enum:wave_role` ×88).
- **No staged-vs-gated seal field** — "gated" appears 129× but only in prose (admission of a leg
  "after the cannon entry has been gated"); no explicit seal atom.

---

## 7. Relation to SP1 (Primitive Floor) and SP1..SP9

SP1's committed README lists SP2 (AOB meta-ontology) as its **first consumer**: *"grounds each atom's
`tensor`/byte field into the Physical olog + ρ."* This facet is the raw material SP2 consumes, and the
mapping is a clean altitude split:

- **SP1 owns the SUBATOMIC floor** (Bit→Octet→ByteVector, ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ towers, ρ Kleisli-monad
  realization, Frame=Yoneda-point, sha256, endianness, RGB/256). **None of that is in these atoms.**
- **This facet owns the SUPRA-atomic instance layer**: 17k paper-derived atoms whose *categorical*
  structure (Yoneda legs, olog boxes, colimit cocones, cheese-trap immunity, synonym/antonym polysemy,
  CCO grounding) is fully materialized but whose *physical grounding is by-reference only* (URN, not
  bytes).
- **The lift SP2 performs**: attach to each atom (a) a sha256 identity, (b) a group law
  (identity/compose/retract over atoms), (c) the tensor/byte block grounded into SP1's Physical olog
  via ρ, (d) explicit S/O/P byte-schema towers, (e) a `universal_anchors` CCO **and BFO** anchor, (f)
  the staged-vs-gated seal. The CircuitImprintTensor's "witness + readback, no inferred adjacency"
  discipline is already SP1-shaped (it refuses coordinate-inferred relations exactly as the unary law
  refuses a scalar-triple substitute for S/O/P towers) — so SP2 should realize the tensor block by
  binding `active_circuit_urns` support into SP1's Frame(output, effect) rather than re-inventing it.

The **Yoneda / functorial-transport / presheaf / colimit / sheaf-gluing theory that SP1 re-derived**
is here as *content*, one paper each: 18 (presheaf semantics + Yoneda-for-presheaves + density/
cocompletion + Kan restriction), 19 (mereology as colimit — pushout/coequalizer zoo, index-category
anatomy), 20 (functorial transport — pullback vs pushforward, preservation laws), 25 (sheaf gluing —
WIP, 1 chapter only), 09 (Yoneda lemma & representables), 11 (free-monad + Yoneda embedding +
adj/Kan bridges). SP1's `taiji.ttl` literal-Yoneda layer is the *formal skeleton*; these papers are
the *worked corpus* that skeleton must eventually re-cover.

---

## 8. Coverage statement (Präriehund)

- **Structure**: enumerated 100% — full directory tree, all 11 papers, chapter lists, and exact
  per-paper/per-family counts are from exhaustive `find`/`grep` over all 17,071 files.
- **Schema**: read IN FULL ≥1 representative of **every one of the 22 `type_node` families** plus the
  companion-bundle apex, the 4 `addl_*` variants, and an AtomBundle — ~18 files across papers 09, 11,
  19, 20. Field lists per family are corroborated by whole-corpus field greps.
- **Not read**: the individual prose bodies of the other ~17,050 files (they are near-identical
  instances of the sampled schemas, differing in URN/quote/anchor text). I did NOT verify every
  atom's CCO IRI or every Yoneda leg by hand — the IRI/field distributions are from aggregate grep.
- **Referenced-but-outside-this-facet**: `data/atom_family_registry.spec.yaml` (the family contract
  named in AdditionalAttributes comments) and `src/shared/references.bib` are cited by atoms here but
  live in other helios facets (`srcy` / `00_src_specs`); not resolved in this map.
