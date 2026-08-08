# HELIOS facet map — `helios/00_src_specs` (the RENDER + TYPE layer)

> W2 mapping ledger. Facet: the maintainer's authored SOURCE-OF-TRUTH for the
> **typed-component-grammar render engine** + the **type system** that drives it.
> This is the `base_templates` lineage ("ba/templates" sealed set) plus its
> `types/` spec corpus, corroboration tests, and the Elixir/BEAM + bash render
> legs. Präriehund honesty on coverage is stated per-section; nothing sampled is
> claimed as fully read.
>
> Zip root on disk: `/home/user/silmaril/helios/00_src_specs/` (git-ignored;
> resolved into submodules by the maintainer — do NOT commit).

---

## 0. Census (the tree IS the taxonomy)

- **672 files, 192 directories, 6.6 MB.**
- By extension: **454 `.j2`** (Jinja2 templates — the render grammar), **115
  `.yaml`** (`.spec.yaml` type specs), **35 `.beam`** + **11 `.exs`** + 1 `.ex`
  (Elixir/BEAM render leg + tests), **26 `.sh`** (bash render leg + scripts),
  **12 `.avsc`** (Avro schemas), **5 `.xml`** (libvirt/idea), plus `.app`,
  `.lock`, `.json`, `.config`, `.fetch`, `.gitignore` build detritus.
- Five top-level roots: **`templates/`** (the render grammar — the bulk),
  **`types/`** (the type system — 115 `.spec.yaml`), **`scripts/`** (bash render
  drivers + per-atom rendered output), **`test/`** (Elixir corroboration +
  round-trip), **`.elixir_ls/`** (ElixirLS build cache — 35 `.beam`, ignore).

Note vs. the brief's "~569 j2 / ~192 types": this facet holds **454 `.j2`** and
**115 `.spec.yaml`**; "192" matches the **directory** count, not the type count.
The larger `.j2` totals in the brief count the whole `base_templates` submodule
(frontier + sealed + yml/sql/allura frontier sets named in `SEAL.md` §Frontier)
which are NOT all present in this zip slice — only the sealed + colimit + papers
+ fp_triad + atomic_mirror grammar is here. Coverage stated honestly below.

---

## 1. Directory taxonomy (full structure — no truncation)

```
00_src_specs/
├── templates/                         THE TYPED COMPONENT GRAMMAR (454 .j2)
│   ├── _universal_macros.j2           HUB — imports+re-exports EVERY registry macro (7 legs B1..B7)
│   ├── _global_constants.j2           canonical URN-refs (charset/EOL/indent/comment/format/impl) — declarative constants only
│   ├── SEAL.md                        the frontier→sealed contract (ba/templates seal events + inventory)
│   ├── _test_b3.j2 / _test_b3b.j2     probe templates
│   ├── papers-theorems-emit.sh.j2     paper theorem emitter
│   ├── _registries/                   PER-CONCERN MACRO FILES (46) — the dispatch spine
│   │   ├── comment_prefix / sentinel / format_concrete / impl_concrete / lang_convention
│   │   ├── ttl_{subject,grounds,descriptions,predicates,escape}   (B4 ttl leg)
│   │   ├── shacl_{constraint,target,shape}                        (B5 shacl leg)
│   │   ├── sparql_{curie,lookup,emit_prefix,emit_clauses,assemble} (B2 sparql leg)
│   │   ├── linkml_{anchors,predicates,emit,family}                (B3 linkml leg)
│   │   ├── yoneda_{json,family_slug,grounding,validate,manifest}  (B1 yoneda leg)
│   │   ├── atlas_{csv_cells,row_emit,inverse_derivation,glossary_naming}  (B6 atlas leg)
│   │   └── globals_{text_format,render_stamp,env_exports}         (B7 globals leg)
│   ├── _urn/identity.j2               urn_for / identity_stamp / universal_base / quark(_block) / encoding_stamp
│   ├── _tensor/render.j2              THREE-AXIS tensor block render (space / time / value)
│   ├── _ancestry/render.j2           ancestry {axis, via} two-axis render
│   ├── _avsc/schema.j2               Avro field/record/discovery-manifest macros
│   ├── _validate/{urn_grammar,domain_invariants}.j2   URN grammar regex + StrictUndefined enforcement
│   ├── _text/escape.j2 · _markdown/{badges,links,tables}.j2 · _cat/nodes.j2   leaf helpers
│   ├── colimit/                       THE ATOM-EMISSION ENGINE (the "verb" render)
│   │   ├── verb.{atlas.csv,ttl,shacl.ttl,sparql,linkml.yaml,yoneda_manifest,ex,sh,scala,hs}.j2  10 PROJECTION LEGS
│   │   ├── verb_impl.ex.j2 · verb.ex.j2 · _impl/ex/{_module_header,_run_function,_module_footer}.ex.j2
│   │   └── _body/
│   │       ├── {atlas,ttl,shacl,linkml,yoneda}/   per-format × per-atom-family bodies + dispatcher.j2
│   │       │     atlas=27 · ttl=25 · shacl=25 · linkml=25 · yoneda=18 atom-family files each
│   │       ├── sparql/{q1..q5}.j2                 5 canonical SPARQL queries
│   │       ├── {ex,sh,scala,hs}.j2                per-language body dispatchers
│   │       └── *.{ex,sh}.j2                       ~14 concrete primitive bodies (ldap/parity/count/csv/regex/file_presence…)
│   ├── fp_triad/                      THE FP-TRIAD render (Haskell · Elixir · Scala + bash)
│   │   ├── fp_module.{ex,hs,scala,sh}.j2 · atom_emit.{ex,hs,scala}.j2
│   │   ├── _macros/{tensor,field_types}.j2 · _tensor_macros.j2   S/O/P + cardinality→container macros
│   │   └── _{body,bootstrap,envelope,evidence,per_record}/{ex,hs,scala,sh}.j2   composition-not-inheritance layers
│   ├── atomic_mirror/                 THE AOB ATOM DISINTEGRATION grammar (".d/" mirror)
│   │   ├── README.md.j2 · ticket.json.j2 · claim.json.j2 · dag.atomic-mirror-two-roots.yaml.j2
│   │   ├── _macros/{avro_codec,citations,dag_nodes,envelope,provenance,rdf_triples,shacl_claims}.j2
│   │   ├── atomic_evaluation/{cells,claims,dimensions,examples,kernel_bind,leahry,morphisms,yoneda}.yaml.j2
│   │   │   + examples/{_eigenstate,_needs}/… + dunbar/gamma_propagation.yaml.j2
│   │   ├── contracts/{atlas,linkml,silmaril}[/ _clause/…]  three epistemology projections per atom
│   │   └── schemas/*.avsc             _atom_common + 6 fs_* + 4 text_* concrete Avro atom schemas
│   ├── papers/                        THE 34-PAPER render (LaTeX + diagrams)
│   │   ├── paper.tex.j2 · section.tex.j2 · rule_card.tex.j2
│   │   ├── _envelope/{titlepage,preamble,identity_header,appendix,bibliography,bundle}.j2
│   │   ├── _body/{section_header,section_prose,cross_reference}.j2
│   │   ├── _appendix/  (20 appendices: atom_inventory, urn_registry, theorems_*, benchmarks, defense_questions…)
│   │   ├── _per_section/{atom_box,theorem_emit,tikz_namespace,colimit_stamp,visual_lexicon/…}
│   │   └── _diagrams/  (adjunction, olog, string, knot, sankey, lattice/hasse, free_monad, euler,
│   │        sequence, taxonomy, fp_triple, conceptual/{yoneda_position,granite_yoneda_loop,…},
│   │        live_data/{growing_knowledge_graph,kg_full_render,urn_namespace_tree,dag_topology,…})
│   ├── avro/ · core/avro/             Avro envelope schemas (dag_node/edge/state, receipt, entity, render_artifact, shacl_report)
│   ├── dialect/ · projection/         entity→{linkml,jsonschema,ttl,smoke} generic projections
│   ├── contracts/                     atom_as_kernel_reality · finalattack_integration · mythology_index · phylum_order_yoneda
│   ├── AtlasContract/                 Apache-Atlas glossary contract (definition.md.j2)
│   ├── generic/                       bashattack/dag · cloud_init · libvirt · podman  (infra codegen)
│   ├── unix/                          hook.sh.j2 · script.sh.j2 + _body/{header,env_setup,libraries,functions,main}
│   ├── silmaril_env/                  .claude/settings.json render (env-lock)
│   └── .claude/ .idea/                editor/tooling config
├── types/                            THE TYPE SYSTEM (115 .spec.yaml)
│   ├── silmaril_wave8/               25 ATOM-FAMILY type specs (the render's input grammar)
│   ├── papers/                       5 categorical groupings of the same 25:
│   │   ├── claim_atom/ (theorem_unit) · identity_label/ (citation,diagram,additional_attributes)
│   │   ├── prose/ (acronym,description,example) · structural_atom/ (paper_section)
│   │   └── relational/ (synonym,antonym,translation,preferred_term,replacement,enum_membership)
│   └── primitives/                   THE LAYERED PRIMITIVE TAXONOMY (bash/elixir ops, CCO-grounded)
│       ├── layer_minus1_kernel/      file_{read_write,deletion,stat_test,metadata_mode}, glob, mktemp  (+elixir file_stat)
│       ├── layer_minus1_universal_factory_charter/  detail_kv, env_binding, error_handling
│       ├── layer_0_src/              awk, grep, head/tail, tr/param-subst, proc, time, background/subst/heredoc
│       ├── layer_2_domain/           ssh_authentication, ssh_key_management
│       └── foundation/               composition, compression(brotli/gzip/zstd), conditional, duckdb,
│                                     file_locking, hash, loop, proc, resource_limit, set_control, telephone_emit
├── scripts/                          render_all_wave8.sh · render_check_rules.sh + silmaril/wave8/*.sh (25 rendered bash atoms)
├── test/                             ExUnit: wave8_round_trip · algebra · silmaril/wave8/checks/{colimit_corroboration,
│                                     dispatcher_scope_count,includes_corroboration} · products/{bls,factory,pyfun,storm,users}
└── .elixir_ls/                       ElixirLS build cache (35 .beam — ignore)
```

---

## 2. The template grammar — how it is built

### 2a. Composition, not inheritance (StrictUndefined)
The grammar has **no `{% extends %}` anywhere**. Every template is assembled by
`{%- from '…' import … -%}` + `{%- include '…' -%}`. The single hub
`_universal_macros.j2` imports every registry macro and **re-exports** each via
`{%- set X = X -%}` so any downstream `{% from '_universal_macros.j2' import X %}`
resolves. The hub is organized as **seven Phase-B migration legs** (B1 yoneda,
B2 sparql, B3 linkml, B4 ttl, B5 shacl, B6 atlas, B7 atomic_mirror/globals),
each fenced by unique `START/END` marker comments so parallel B-agents edit only
their own block (no merge race on the hub). Documented cycle-avoidance: the ttl-
variant `turtle_escape`/`urn_slug` are deliberately NOT re-exported (they collide
with the universal `turtle_escape`), and `dag_node` is imported direct-from-home
by its one caller to avoid a parser cycle.

### 2b. StrictUndefined enforcement (the "fail render, don't emit garbage" law)
Two mechanisms:
- **Missing-tensor tripwire** (`_tensor/render.j2` L162-164): if a field lacks a
  complete three-axis tensor, the macro emits
  `{{ none.__avogadro_missing_complete_three_axis_tensor__ }}` — a deliberate
  attribute-access-on-None that Jinja StrictUndefined turns into a hard render
  failure. "Avogadro" = the scale metaphor (every one of billions of atoms must
  carry a complete tensor).
- **URN grammar enforcement** (`_validate/urn_grammar.j2`): `validate_urn_string`
  references `none['VALIDATE_URN_STRING_FAILED_…']` when a URN fails the
  prefix/charset check — same StrictUndefined trip. It also emits an optional
  bash-runtime `grep -qE '<regex>'` guard (`exit 2` on fail). The URN grammar
  regex is called out as the **one bootstrap-paradox primitive exemption**: it
  cannot be a Node-ref because URN-validity is the rule that defines all Node-refs.

### 2c. Registries + dispatch (the macro spine)
`_registries/` is 46 single-concern macro files. Each output **format** (atlas,
ttl, shacl, sparql, linkml, yoneda) has its own registry cluster of
prefix/curie/predicate/emit helpers. Dispatch is two-level:
1. **Format orchestrator** `colimit/verb.<fmt>.j2` — emits the prefix/preamble
   for one format, then `{%- include 'colimit/_body/<fmt>/dispatcher.j2' -%}`.
2. **Family dispatcher** `colimit/_body/<fmt>/dispatcher.j2` — reads
   `family_slug(entity)` and `{%- include -%}`s the one atom-family body
   (`if fs == 'color_atom' … elif fs == 'synonym_atom' …`). Accepts both the
   `_atom` and bare slug (`'color_atom' or 'color'`). No default fallback in the
   yoneda leg — a missing `cco_grounding_iri`/`cpo_process_iri` deliberately
   surfaces as `iri=no` on the telemetry wire (fallbacks were REMOVED 2026-05-20
   after they masked ungrounded specs).

### 2d. header / section / table / svg / mount macros
This slice's macro vocabulary is the **atom/paper** grammar, not the HEEx web
`_spine` (header/section/table/svg/mount) named in `JUNGLE_MAP.md` §base_templates
— that HEEx spine is NOT in this zip (it lives elsewhere in the submodule). The
functional equivalents here:
- **header/identity** → `_urn/identity.j2::universal_base` (the 7-tuple
  `cat_node × lang_edge × econ_state × urn × encoding_urn × hash × quark`),
  `identity_stamp`, `encoding_stamp`, `nl_indent_stamp`, plus
  `globals_render_stamp::globals_header_stamp`.
- **section** → `papers/_body/section_{header,prose}.j2`,
  `papers/_per_section/*` (atom_box, theorem_emit, colimit_stamp).
- **table** → `_markdown/tables.j2` (tech_row/pattern_row),
  `atlas_row_emit::emit_row` (the 16-column Atlas glossary CSV row),
  `atlas_csv_cells::cell`.
- **svg/diagram** → `papers/_diagrams/**` (TikZ/string/olog/sankey/hasse/knot/
  free_monad/live_data KG renders) — the visual grammar.
- **mount** → the `colimit/verb.*` orchestrators are the "mount points": each is
  an independently-parseable document root for one projection format.

---

## 3. The type system (`types/`) — what drives the render

### 3a. Atom-family spec shape (`types/silmaril_wave8/*.spec.yaml`, 25 families)
The render's input grammar. Read in full: `color_atom`, `antonym_atom`,
`typed_hom_triple`; schema-sampled across all 25 (identical envelope, byte_order
grep confirms all 25 share the tensor block). Canonical shape:

```yaml
spec_version: 1
entity:
  urn: urn:silmaril:entity#types.papers.silmaril_wave8.<name>
  display_name: <PascalName>            # → rdfs:label everywhere
  layer: papers
  type_node: Atom
  type_urn: urn:silmaril:entity#types.papers.atom
  grounding: <≥1-sentence CCO-anchored prose>   # → rdfs:comment / owl:Class body
  fields:                               # ordered list; each field a FULL tensor
    - name: <field>
      tensor_space: urn:silmaril:universal-anchor:node:<facet>:<anchor>   # ← universal_anchor ref
      type_urn: urn:silmaril:entity#types.layer_0_src.string_node
      description: <prose>
      tensor:                           # THE THREE-AXIS TENSOR BLOCK (§4)
        space: {cardinality, dimensions, bounded, max_size, bit_width, byte_width, alignment}
        time:  {dynamics, ordering, monotonic, lifetime, byte_order, arithmetic}
        value: {interpret_as, domain:{kind, range_min?, range_max?, finite_set?}, read_via?, write_via?}
  atom_family_urn: urn:silmaril:atom-family:<node|arrow>:<name>
  top_kind: <node|arrow>                # THE PROGENITOR SPLIT: node atoms vs arrow atoms
  ancestry: [{axis: prelude, via: urn:…types.prelude.node}]   # {axis, via} two-axis
  kind_urn: urn:silmaril:entity#types.prelude.kind_node_type_def
triad_render:                            # WHERE the render lands (colimit discipline)
  elixir_module: Silmaril.Wave8.<Name>Atom
  bash_namespace: silmaril::wave8::<name>_atom
  out_paths: {elixir: lib/…/<name>.ex, bash: scripts/…/<name>.sh}
```

The 25 families (= the AOB atom taxonomy, both `top_kind`s):
`concrete_anchor, olog_box, chapter, paper_section, function_atom, lemma_atom,
theorem_unit, citation_atom, diagram_atom, description_atom, acronym_atom,
color_atom, shape_atom, example_atom, additional_attributes_atom,
decomposition_step, cheese_trap_immunity, circuit_imprint_tensor,
typed_hom_triple, yoneda_hom_leg` (nodes/arrows) + the **relational/polysemy**
set `synonym_atom, antonym_atom, translation_atom, preferred_term_atom,
replacement_atom, enum_membership_atom`.

### 3b. `types/papers/` — the 5-way categorical grouping
The same 25 families re-filed under **claim_atom / identity_label / prose /
relational / structural_atom** — a second axis over the atom set. `relational/`
holds exactly the polysemy families (synonym **and** antonym side-by-side).

### 3c. `types/primitives/` — the layered primitive taxonomy (CCO-grounded)
A DIFFERENT, richer spec shape (read in full: `telephone_emit/emit_record`,
`compression_algorithms/zstd`). This is the **six-axis ancestry** progenitor
lattice:

```yaml
metadata: {schema_version, layer, kind_urn: …kind_primitive_atom, authored_by, authored_at}
spec:
  urn: urn:silmaril:entity#primitives.<order>.bash.<species>
  top_kind: arrow
  ancestry:                       # SIX taxonomic ranks — the "phylum/order" lattice
    - {axis: phylum,           value: urn:…phyla.foundation}
    - {axis: class,            value: …kind_primitive_atom}
    - {axis: order,            value: compression_algorithms}   # the operation family
    - {axis: family,           value: bash}
    - {axis: language_binding, value: bash}
    - {axis: species,          value: zstd}
  surface_syntax: {bash: '<the literal one-line command>'}
  instance_scope: <telephone|…>
  invariant: <byte-level behavioral contract — lossless round-trip stated explicitly>
  cco_grounding_iri:   cco:ont00001158       # ← UNIVERSAL ANCHOR (load-bearing)
  cco_grounding_label: Act of Data Transformation
  why_arrow: <CCO-parent justification prose>
```

Layer ladder (directory-encoded): `layer_minus1_kernel` (raw syscalls: file
read/write/delete/stat/glob/mktemp) → `layer_minus1_universal_factory_charter`
(kv-emit, env-binding, error-handling discipline) → `layer_0_src` (text/proc/
time transforms) → `layer_2_domain` (ssh) → `foundation` (compression, hashing,
duckdb, locking, **telephone_emit**). Each species carries a **CCO IRI** — this
is the ISA/UEFI/`whats-a-number`-depth grounding demanded by Directive 3, but
realized at the **operation** level (Act of Data Transformation, Act of
Communication) rather than the numeric-tower level (which lives in SP1's floor).

---

## 4. The AOB atom shape — W2 lens (deep)

### 4a. The three-axis tensor block (`_tensor/render.j2` + `fp_triad/_macros/tensor.j2`)
Every field carries a **space × time × value** tensor, each axis a bag of
**discriminator-Node refs** (`{type_node: <PascalName>, type_urn: urn:…prelude.<slug>}`):
- **space**: `cardinality` (CardinalityOne/Many/Maybe → drives HS `[]`/`Maybe`,
  Elixir `.t()`/`MapSet`/`[]`, Scala `Option`/`Set`/`Vector` in `field_types.j2`),
  `dimensions` (the geometer axis — 0 for scalar prose), `bounded`, `max_size`
  (element count, explicitly "NOT bit width"), `bit_width`, `byte_width`,
  `alignment`.  ← this is the **byte-vector layout** (Directive 3/9 physical facet).
- **time**: `dynamics` (Snapshot/Stream/Mutable), `ordering` (Positional/
  Unordered/Timestamped), `monotonic`, `lifetime` (Immutable/…), **`byte_order`**
  (the endianness discriminator — see §7 z/endianness), `arithmetic` (None/…).
- **value**: `interpret_as` (Utf8/…), `domain` (`kind` Opaque/…, `range_min`,
  `range_max`, `finite_set`), `read_via` / `write_via`.

The tensor render is **defensive**: missing any of space/time/value trips the
Avogadro-None StrictUndefined failure. Discriminators render as
`type_node=… type_urn=…`; a bare legacy string renders with a
`(pre-three-axis; migrate to {type_node,type_urn} dict)` warning — the migration
is visible in the artifact.

### 4b. The AOB identity + atom schema (`atomic_mirror/schemas/_atom_common.avsc`)
The Avro **AtomCommon** record is the concrete atom identity carrier — included
by composition into every per-type schema (`fs_binary, fs_device, fs_dir,
fs_regular, fs_symlink, fs_unreadable, text_json, text_markdown, text_script,
text_turtle, text_yaml`). Fields:
`atom_iri, atom_type (enum T1..T14 — the 14-type taxonomy), source_path,
**source_sha256**, qualified_name, emit_triples, parent_atom (nullable — the
compositional parent), traceback_to (IRI of a Leahry axiom L1..L18), co_owners[],
provenance (hand_authored_specimen | hand_edited_source | ba_jinja2_rendered),
rendered_by (<template>.j2), rendered_at_utc`.
→ **sha256 identity** = `source_sha256`; `urn_for(kind, sha256, ns)` (in
`_urn/identity.j2`) mints `<ns>:atomic_mirror/<kind>/<sha256>` — the content-
addressed atom URN.

### 4c. Subatomic decomposition — the ".d/" atomic mirror
`atomic_mirror/README.md.j2` documents the law: **every source file gets a
sibling `<file>.d/` directory that disintegrates it into its contracts +
projections** (Cook's 2026-04-17 ruling). The `.d/` tree = `ticket.json` +
`claim.json` (SHACL) + `contracts/{linkml,atlas,silmaril}` (three epistemology
projections of the SAME atom — Directive 1's "mole of glossaries": Apache-Atlas
glossary vs LinkML object-schema vs Silmaril-URN, distinct epistemologies of one
term) + `atomic_evaluation/{cells,leahry,dimensions,morphisms,yoneda,examples,
claims,kernel_bind}.yaml`. Invariant #1: source is truth, every `.d/` file is a
**projection**; #4/#5: byte-identical re-emit (the render-seal round-trip, S5).

### 4d. `cells.yaml` = the 9-cell geometer matrix; `leahry.yaml` = the reflex tower
- `cells` = a **{forge, unix, joy} × {bit, byte, word} 9-cell matrix** — echoes
  the `quark` 9-cell in `_urn/identity.j2` (`_QUARK_CATEGORY_URNS = {cat, econ,
  lang} × _QUARK_AXIS_URNS = {node_or_arrow, shape, color}`). This is the
  **geometer/glossary axis** structure (see §8).
- `leahry.yaml` = **18 axes** = 2 self-axes (L1 dominance↔submission, L2
  hostility↔affection) + **16 reflexes L3..L18** arranged as **8 octants ×
  {moderate, extreme} ≅ 2⁴ MBTI cube** (`cube_coord: 0000..1111`). Each atom's
  `traceback_to` points at one L1..L18 axiom — the Leahry interpersonal-circumplex
  grounding of atom "personality".

### 4e. Progenitor / composability
- **`top_kind: node | arrow`** is the primordial progenitor split — every family
  declares itself a node-atom or an arrow-atom; the dispatchers branch on it
  (yoneda manifest is defined ONLY over node-kind families; arrow atoms emit a
  `_not_a_node_atom` sentinel). This is the "model every distinct thing as its
  own atom" law.
- **`atom_family_urn: urn:silmaril:atom-family:<node|arrow>:<name>`** — every
  family is its own addressable atom.
- `parent_atom` (nullable) in AtomCommon = the composition pointer; `co_owners[]`
  = shared ownership; nothing crammed — each concern is a separate `.d/` file.

---

## 5. The projection family (the render seal) — W2 lens

**10 projection legs** from one atom spec (`colimit/verb.<leg>.j2`):
`atlas.csv, ttl, shacl.ttl, sparql, linkml.yaml, yoneda_manifest, ex, hs, scala,
sh`. Each leg is an independently-parseable document root; each re-`{% include %}`s
a per-family body from `colimit/_body/<leg>/`. Per-leg atom-family coverage:
atlas **27**, ttl/shacl/linkml **25** each, yoneda **18** (node-only), sparql =
5 fixed queries, and the language legs (ex/sh/scala/hs) dispatch through
`fp_triad`. This IS the **SP5 format taxonomy** (one atom → RDF/Turtle, SHACL,
SPARQL, LinkML, Apache-Atlas CSV, Avro, LaTeX, and the four FP-triad languages)
and the **SP4 projection packet** (each projection is a functor from the atom
category to a format category).

**The colimit / render-seal law** (`scripts/render_all_wave8.sh`,
`test/silmaril/wave8/checks/colimit_corroboration_test.exs`,
`dispatcher_scope_count_test.exs`): every spec MUST render into BOTH an Elixir
component AND a bash script, and **the two must do the same thing** — "that's the
colimit property that ensures the node/arrow reality is preserved." Tests verify
functional equivalence at the data-atom level (`make + is` round-trip) AND at the
check-rule level (same input → same exit code + same violations). The
`dispatcher_scope_count` test guards that the bash leg and elixir leg **enumerate
the identical file set** (`bash_count == ex_count`) AND that the absolute count
== `SIL_EXPECTED_TEMPLATE_COUNT` — catching "joint dispatcher drift" where both
legs silently narrow scope together. This is the two-witness (bash ⟷ beam)
colimit that SP9's split↔consolidated render seal generalizes.

**nth-dimensional effect/loss taxonomy** — NOT materialized in this facet. The
tensor `space.dimensions` field is the per-atom dimensional coordinate (0 for
scalar prose atoms here), and each realization carries a `frameEffect`, but the
explicit 5-class **loss taxonomy** lives in SP1's floor (`q_frame_effect`,
realization effects) and SP4's projection-packet spec, not in `00_src_specs`.
Stated honestly per Präriehund.

---

## 6. universal_anchors — the CCO/BFO upper-ontology anchor (load-bearing)

`_registries/linkml_anchors.j2::_ANCHORS` is the **11-anchor universal_anchors
table** — the Layer-0 projection every field's `tensor_space` points into. Each
anchor = `{primitive: StringNode|IntNode|BoolNode|EnumNode, pattern: <regex>,
curie_prefix}`. The 11:
```
node:identifier:paper_slug   (^[0-9]+[a-z]?_[a-z0-9_]+$, silm)
node:identifier:urn_literal  (^urn:silmaril:…, silm)
node:identifier:cco_grounding_iri  (^cco:ont[0-9]{8}$, cco)     ← CCO anchor
node:identifier:env_locked_path    (^/home/tristan/…, silm)
node:counter:cardinality (IntNode) · node:flag:boolean (BoolNode)
node:literal:prose_short · node:literal:prose_long (StringNode)
node:enum:milestone (MilestoneEnum: chapter_skeleton…render_all_legs_ok)
node:enum:wave_role (WaveRoleEnum: builder|polisher)
arrow:identifier:cpo_process_iri   (^cceo:[A-Za-z0-9_]+$, cceo) ← CPO/CCO arrow anchor
```
`linkml_range(anchor)` derives the LinkML `range:` (uri|string|integer|boolean|
<enum>) — a pattern starting `^cco:`/`^cceo:`/`^urn:` → `range: uri`. **CCO/CPO
is the load-bearing upper-ontology anchor**: node atoms ground via
`cco_grounding_iri` (`cco:ont########`), arrow atoms via `cpo_process_iri`
(`cceo:…`), resolved in `${SIL_CPO_TTL_FILE}`. `yoneda_grounding.j2` holds the
per-family **CCO default grounding table** (25 families → `cco:ont…`, e.g.
color→ont00000686 "Information Content Entity", synonym/antonym/translation/
replacement→ont00001158 "Act of Data Transformation", typed_hom_triple/
yoneda_hom_leg→ont00000402 "Act of Communication"). The ttl/shacl legs emit the
CCO/CPO prefixes (`cco: <https://www.commoncoreontologies.org/>`, `cceo:
…/cpo#>`). No literal `bfo:` prefix appears in this slice — BFO is reached
transitively THROUGH CCO (CCO is BFO-conformant), consistent with the maintainer's
"CCO/BFO anchor" being routed via CCO here.

---

## 7. z byte-order / endianness progenitor — decision answer

**`byte_order` is a first-class discriminator axis** on the tensor `time` block.
In this facet every wave8 atom field carries
`byte_order: {type_node: ByteOrderNone, type_urn:
urn:silmaril:entity#types.prelude.byte_order_none}` — because all 25 wave8
families are **UTF-8 prose/identifier atoms** (byte-order-agnostic: a UTF-8 string
has no endianness). `ByteOrderNone` is thus the **agnostic progenitor sitting in
the `None` slot**; its BE/LE siblings are the other children of the
`types.prelude.byte_order_*` discriminator-Node family (the progenitor pattern:
one endianness-agnostic parent with `byte_order_none` + big/little children).
The **children are NOT instantiated in `00_src_specs`** — no atom here is a
multi-byte numeric that would select BE or LE. The BE/LE realizations belong to
SP1's physical floor / the numeric-tower atoms, not the prose-atom render layer.
So: the **axis and its agnostic progenitor are present and load-bearing here**
(`render_tensor_time` renders `byte_order` for every field); the concrete BE/LE
children are defined in the prelude discriminator tables consumed here but
authored in the floor. Präriehund: I did not find a BE/LE-selecting atom in this
slice.

---

## 8. geometer / glossary axes vs towers — decision answer

The "dimension is per-geometer; axes are nth" axiom is realized structurally, NOT
by jumping to S/O/P towers:
- **space.dimensions** is the per-atom dimensional coordinate — the render carries
  it verbatim (`dimensions: 0` for scalar prose atoms). Each atom declares its own
  dimension; the render never assumes a tower.
- The **quark 9-cell** (`_urn/identity.j2`): `category ∈ {cat, econ, lang}` ×
  `axis ∈ {node_or_arrow, shape, color}` — a 3×3 geometer grid stamped on every
  identity block. This is the a,b / x,y-style low-dimensional axis system.
- The **atomic_mirror `cells` 9-cell**: `{forge, unix, joy} × {bit, byte, word}`
  — another geometer plane (substrate × granularity).
- **S/O/P towers** appear as the **typed_hom_triple / yoneda_hom_leg** arrow
  families: `typed_hom_triple` = `{source_urn (S), target_urn (O), cpo_process_iri
  (P)}` — the Subject/Object/Predicate tower composed into one arrow atom. The
  atlas leg emits it as `term_slug(src ~ '_to_' ~ dst)` with the CPO IRI as the
  predicate. So the tower is built compositionally FROM per-geometer axes, exactly
  the "we can't just jump to towers" discipline — the S/O/P tower is an
  arrow-family atom assembled from the universal anchors, not a primitive.
- The **six-axis primitive ancestry** (phylum/class/order/family/language_binding/
  species) is the nth-axis taxonomic tower for the primitive corpus — a per-
  geometer Linnaean lattice, each rank its own axis.

---

## 9. telephone twin (Directive 6) — decision answer

**Located and characterized in this facet.** The telephone is a concrete
primitive family:
`types/primitives/foundation/telephone_emit/bash/emit_record.spec.yaml`
- `urn: primitives.telephone.bash.emit_record`, `instance_scope: telephone`,
  `top_kind: arrow`, order-axis `telephone_emit`.
- **Surface syntax**: invokes the PATH-installed **`cheese_text`** binary with the
  full flag set: `--scope --event --detail (k=v;k=v) --dunbar-layer (0/1/2)
  --handle --correlation-id`.
- **Wire mechanism**: record lands on the **L0 ring buffer**, the **Classifier**
  tags it, the **OcfAppender** persists it to `logs/hooks/*.avro`; exit 0 on
  accepted emission, non-zero if the daemon is down AND the L1 fallback also fails.
- **CCO grounding**: `cco:ont00000402` "Act of Communication" — the canonical
  sender→channel→receivers shape.

The **"twin"** appears three ways here: (1) the **`--dunbar-layer` cohort
visibility** (0/1/2) ties telephone emission to the Dunbar/federation gossip layer
(`atomic_mirror/atomic_evaluation/dunbar/gamma_propagation.yaml.j2`); (2)
**`cheese_text` / `cheese_trap_immunity`** — the telephone binary is named for
the same "cheese" mythology as the `cheese_trap_immunity` atom family (the mouse/
mitten federation folklore); (3) the **bash⟷elixir colimit twin** — every
telephone/atom render has a bash leg and an Elixir leg that must agree (§5). This
is Directive 6's "twin mention": the byte/color substrate ↔ agent-gossip link is
carried by `telephone_emit` emitting content-addressed Avro atoms onto the wire,
grounded as Act of Communication, ready to be tightened into the ologs-of-ologs
Yoneda realization (the `yoneda.yaml` "representability statement" per atom is the
hook). I did not find a literal file named `telephone`-`twin`; the twinning is the
cheese_text↔cheese_trap naming + the dunbar-layer + the bash/beam colimit.

---

## 10. Yoneda / functorial-transport / presheaf / colimit / sheaf-gluing — SP1 grounding

This facet is where SP1's re-derived theory is **operationalized as a render**:
- **Yoneda**: `colimit/verb.yoneda_manifest.j2` + `_body/yoneda/*` + each atom's
  `atomic_evaluation/yoneda.yaml` "representability statement" =
  `yo: A ↦ Hom(−,A)` made a concrete emitted manifest (the representable presheaf
  as a YAML fibre). `yoneda_hom_leg` / `typed_hom_triple` families ARE the hom-set
  arrows. `_registries/yoneda_validate.j2::validate_hom_arrow` type-checks each
  hom. `papers/_diagrams/conceptual/{yoneda_position,granite_yoneda_loop}.j2`
  render the Yoneda position visually.
- **Functorial transport**: the **10 projection legs** are functors atom-cat →
  format-cat; the **bash⟷beam colimit corroboration** is the naturality witness
  (same atom transported two ways must agree). `fp_triad` transports one atom into
  Haskell/Elixir/Scala/bash preserving the tensor structure (`field_types.j2`
  cardinality→container is the functorial action on the space axis).
- **Presheaf**: `yoneda_manifest` = the presheaf-as-data; `yoneda_json.j2` serializes it.
- **Colimit**: `colimit/` is the entire engine namespace — "verb" render = the
  colimit that glues the per-format legs; `templates/colimit/_body/{atlas,ttl,
  shacl,sparql,linkml,yoneda}/` are the cocone legs; `papers/_appendix/
  live_colimit_snapshot.j2` + `_per_section/colimit_stamp.j2` render the live
  colimit. `contracts/phylum_order_yoneda.md.j2` documents the phylum/order/Yoneda
  gluing.
- **Sheaf-gluing**: the atomic-mirror `.d/` invariant (byte-identical re-emit
  across projections, S5) is the sheaf condition — the three epistemology
  contracts (`atlas/linkml/silmaril`) must glue on overlaps to the one source atom.
  `SEAL.md` frontier→sealed is the section-restriction map.

---

## 11. Relation to / correction of the committed SP1 floor (SP1..SP9)

`00_src_specs` is the **render+type engine** (`base_templates` lineage); the
committed `basicttl/primitives/` floor is **SP1 the Primitive Floor**. Their
relationship:

- **SP1 (Primitive Floor)** — this facet is the DOWNSTREAM CONSUMER of the floor:
  the tensor `space.{bit_width,byte_width,alignment}` + `time.byte_order` +
  `value.interpret_as/domain` fields are exactly the coordinates the floor's
  physical olog (`Bit→ByteVector`, ISA/UEFI, RGB) and monadic realization
  (`frameOutput/frameEffect`) supply. The floor authors the numeric towers ONCE;
  `00_src_specs` atoms reference discriminator-Node URNs (`types.prelude.*`) into
  it. **Correction the render layer forces on the floor**: the floor's per-type
  reflexive-carrier discipline must expose these `prelude` discriminator Nodes
  (byte_order_none/be/le, cardinality_one/many, interpret_as_utf8, dynamics_*,
  lifetime_*) as first-class typed nodes — this facet CONSUMES them by URN and
  will StrictUndefined-fail if the floor omits any (the Avogadro tripwire is the
  enforcement teeth reaching back into SP1).
- **SP2 (AOB meta-ontology)** — the AtomCommon Avro schema + `top_kind` node/arrow
  progenitor + `atom_family_urn` + `.d/` disintegration + Leahry/cells/quark are
  the concrete AOB atom shape SP2 must lift (Directive 1: "lift the existing one,
  don't invent"). `source_sha256` is the sha256 identity; `parent_atom` the
  composition.
- **SP3 (S/O/P CRS)** — `typed_hom_triple {source_urn, target_urn,
  cpo_process_iri}` is the S/O/P carrier; `z`/byte-order is the tensor axis.
- **SP4 (projection packet)** — the 10 verb legs ARE the projection family; the
  per-realization frameEffect seeds the loss classes (loss taxonomy itself is
  floor-side, §5).
- **SP5 (file+format taxonomy)** — the format legs + `atomic_mirror/schemas/*.avsc`
  (fs_binary/device/dir/regular/symlink/unreadable + text_json/markdown/script/
  turtle/yaml) = the file/format leaf-datatype taxonomy.
- **SP6 (glossary polysemy)** — the three-epistemology `contracts/{atlas,linkml,
  silmaril}` + synonym-AND-antonym relational families = the "mole of glossaries"
  (Directive 1: one term as synonym in one glossary, antonym in another).
- **SP7 (SHACL law)** — `_registries/shacl_{shape,constraint,target}.j2` +
  `verb.shacl.ttl.j2` + `claim.json` render the SHACL law (`sh:closed false`,
  `sh:Violation` severity, pattern-from-anchor).
- **SP8 (depth remediation)** — every atom's `grounding` prose + the CCO
  `why_arrow` are the ≥200-char depth content the remediation demands, authored
  at the render-input layer.
- **SP9 (render seal)** — the bash⟷beam colimit corroboration + `.d/`
  byte-identical re-emit (S5) + `SEAL.md` frontier→sealed = the per-atom
  split↔consolidated reversibility SP9 generalizes.

---

## 12. Coverage statement (Präriehund honesty)

- **Read IN FULL**: `_universal_macros.j2`, `_global_constants.j2`,
  `_urn/identity.j2`, `_tensor/render.j2`, `_ancestry/render.j2`, `_avsc/schema.j2`,
  `_validate/urn_grammar.j2`, `fp_triad/_macros/{tensor,field_types}.j2`,
  `_registries/{linkml_anchors,yoneda_grounding,shacl_shape}.j2`,
  `colimit/_body/{atlas,yoneda}/dispatcher.j2`, `colimit/_body/{ttl/color_atom,
  atlas/typed_hom_triple}.j2`, `colimit/verb.ttl.j2`, `projection/_body/ttl.j2`,
  `atomic_mirror/{README.md,schemas/_atom_common.avsc,atomic_evaluation/leahry.yaml}.j2`,
  `SEAL.md`, `render_all_wave8.sh`, `dispatcher_scope_count_test.exs`, and the
  spec files `silmaril_wave8/{color_atom,antonym_atom,typed_hom_triple}.spec.yaml`,
  `primitives/{telephone_emit/emit_record,compression_algorithms/zstd}.spec.yaml`.
- **Directory tree**: enumerated IN FULL (every dir + every `.j2`/`.spec.yaml`/
  `.avsc`/`.sh`/`.exs` path listed via find).
- **SCHEMA-sampled, not every leaf read**: the 25 wave8 specs share one envelope
  (verified via byte_order grep hitting all 25 identically) — I read 3 in full and
  characterized the rest from the shared schema. The ~120 per-format×per-family
  `colimit/_body/<fmt>/*.j2` bodies (atlas 27, ttl/shacl/linkml 25, yoneda 18): I
  read the dispatchers in full + 2 representative bodies (color, typed_hom_triple);
  the remaining bodies are the same emit-macro-per-family pattern, characterized
  from the schema NOT read line-by-line. The 25 `types/primitives/**` specs: 2 read
  in full, remainder characterized from the shared six-axis-ancestry schema. The
  `papers/**` (~90 files) and `generic/`/`unix/`/`avro/` infra: enumerated + purpose
  inferred from names + the few read; not each read in full.
- **NOT opened**: `.elixir_ls/**` (35 `.beam` build cache), `.idea/**`,
  `.claude/settings.local.json`, the `products/*_integration_test.exs` bodies
  (named/purpose-inferred only).
```
