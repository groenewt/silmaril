# W1 DISCOVERY LEDGER — `forge/base_templates` (the Jinja2 render-template forge for the AOB projection legs)

Synthesizer: W1 Task 1. Framing law read in full first: `docs/praeriehund-demokratie-der-kategorien.md` (129 lines) + `docs/unary-byte-frame-law.md` (765 lines). AOB cross-reference source read in full: `ledger/W1/base_agents.md` (the committed deep AOB reference).
Method: this map MERGES 29 per-slice fragment maps (`t1-frag-000…028`) that together read all 1118 files IN FULL to EOF; the fragment manifests were unioned, sorted by path, and every one of the 1118 `sha256/bytes` pairs was recomputed and verified byte-for-byte against the working tree (zero mismatches) before this map was written. Nothing here contradicts a fragment; where fragments recorded a conflict or a transient observation, the resolution is stated in §7. Quotes are verbatim; every inference is marked; genuinely-unresolvable unknowns are carried into the honest-gap register (§6) verbatim, never force-fit (Präriehund discipline).

> Orientation. `forge/base_templates` is a **git submodule** (root `.git` is a 48-byte gitlink file → `gitdir: ../../.git/modules/forge/base_templates`) holding the **Jinja2 template corpus** that renders the *projection/emitter legs* of the Silmaril AOB (Atom-Oriented-Bundle) system. It is the RENDER side of the machinery whose ATOM side is documented in `ledger/W1/base_agents.md`: where `base_agents` holds the `.aob.dir` dense-node atoms and the `corpus/*.shacl.ttl` CorpusAtoms, `base_templates` holds the Jinja2 that *emits* those atoms' fan-out legs — `.sh / .ex / .scala / .hs / .atlas.csv / .linkml.yaml / .shacl.ttl / .sparql / .ttl / .sql` (the projection family of `base_agents.md` §F). Almost every file is a `.j2` template; the corpus's own recurring law is **"the registry owns the grammar, the assembler owns the layout, the leaf emits one bare term"** and **"a render is LIVE CODE — graded on EXECUTION, not presence"** (GROUND LAW VIII).

---

## 1. Corpus identity

| coordinate | value |
|---|---|
| repo | `forge/base_templates` (git submodule of the `silmaril` superproject) |
| pinned commit (brief) | `eb3d916b0db5c1429e0ce5abaac7b6b75aadea18` |
| verified working-tree HEAD | `eb3d916b0db5c1429e0ce5abaac7b6b75aadea18` (submodule AND superproject `git rev-parse HEAD` both equal the pin; verified at synthesis time) |
| commit subject | `templates` (committed `2026-08-06T17:12:03-05:00`, per fragment 000's read-only `git log -1`) |
| file count | **1118** files (the coverage-check total) |
| total bytes | **4,719,835** — of which `templates/erl_crash.dump` is **2,796,063** (59%); the 1117 text templates total 1,923,772 bytes |
| license | **BSD 3-Clause**, `Copyright (c) 2026, Tristan Groenewold` (`LICENSE`, 1505 B). Observation (fragment 000): the doctrine footer of `docs/praeriehund-demokratie-der-kategorien.md:128` reads `Apache 2.0`; this submodule ships BSD-3-Clause. Recorded as a difference, no conclusion imported. |
| README | 35 bytes, whole content `# base_templates` / `Base GA Templates`. "GA" is not expanded anywhere in the corpus (inference, marked: plausibly "GraphAtlas" per the doctrine's project naming — inference only, the file does not say it). |
| binary / zero-byte | one binary: `templates/erl_crash.dump` (BEAM `erl_crash_dump:0.5`); three zero-byte files: `templates/integration/macros/avsc/_preamble.avsc.j2`, `templates/logs/fuseki-request.log`, `templates/logs/fuseki.log`. |
| largest text files | `_registries/shacl_shape.j2` (35,497 B, 533 lines), `_universal_macros.j2` and `papers/_universal_macros.j2` (33,612 B each), `_registries/linkml_family.j2` (29,562 B), `_registries/sql_tier_schema.j2` (26,445 B). |

The `.git` gitlink file is inventoried as a corpus file because the shared coverage check uses `find … -not -path "*/.git/*"`, which does NOT exclude a bare `.git` regular file (nothing follows `.git` in the path). Its content is the single line `gitdir: ../../.git/modules/forge/base_templates`.

---

## 2. The taxonomy tree as found (full directory account, from the inventory — never eyeballed)

Root of `forge/base_templates` (3 root entries + `templates/`):

```
forge/base_templates/
├── .git            (gitlink file, 48 B)
├── LICENSE         (BSD-3-Clause, 1505 B)
├── README.md       (35 B)
└── templates/      (1115 files — the Jinja2 template root)
```

`templates/` second-level directories and root files (file counts from the manifest):

| files | dir | what it is (from the fragments) |
|------:|-----|---------------------------------|
| 244 | `integration/` | POSIX/syscall + storage macro primitives, one file = one URN-stamped macro, across language lanes `macros/bash` (95), `macros/ex` (32), `macros/python` (30), `macros/haskell` (30), `macros/scala` (27), `macros/heex` (14), `macros/liveview` (4), plus `avsc/ttl/shacl_ttl/linkml_yaml/atlas_csv/avsc_spec_yaml/elixir` preambles, the `_outcome_emit_*` / `_wire_emit_rule_outcome` wire macros, and `ba-envelope-v2.avsc.j2` |
| 214 | `colimit/` | the "colimit" render family — `_body/linkml` (33), `_body/atlas` (27), `_body/shacl` (26), `_body/ttl` (25), `_body/yoneda` (18), `_body/sparql` (5), `_impl/ex` (3), the paired rule-kind `_body/*.{ex,sh}.j2` legs (anchor_dictionary, block_comment_scan, canonical_set_shadow, count_floor, count_ratio, csv_emitter, file_presence, ldap_*, parity, regex_window), the `_body/{ex,hs,sh,scala}.j2` projection assemblers, and ~55 colimit-root emitters (`aob_*`, `dim_*`, `fact_*`, `ring_l*`, `verb.*`, `tier.*`, `l1_segment`, `l3_parquet_archive`, `catalog`, `broadcast_record`, `read_avro_view`) each in one or more of the projection legs |
| 111 | `_registries/` | the macro **registries** — the single-source-of-truth grammar owners (dim_*/fact_* row+census emitters, atlas_* entity/typedef emitters, sql_* star/tier layers, sparql_* clause emitters, shacl_* shape emitters, ttl_* triple emitters, linkml_* class emitters, yoneda_* manifest fibre, aob_* family registry, globals_*, format/impl/lang/comment/sentinel maps, semantic_render_target) |
| 85 | `papers/` | LaTeX/paper render family — `_appendix` (12), `_body` (3), `_diagrams` (25, incl. per-kind dispatchers), `_envelope` (6), `_per_section` (13), plus `paper.tex.j2`, `section.tex.j2`, `rule_card.tex.j2`, and its OWN `papers/_universal_macros.j2` hub (distinct file from the top-level hub) |
| 79 | `atomic_mirror/` | the ".d/ atomic-mirror" generator templates — README, `_macros/` (atom_iri, dag_nodes, envelope_header, provenance, rdf_triples, shacl_claims, traceback), `atomic_evaluation/` (cells, claims, dimensions, dunbar/gamma_propagation, examples + `_eigenstate`/`_needs` atom families, kernel_bind, leahry, morphisms, yoneda), `contracts/` (atlas/linkml/silmaril clause families), `schemas/` (11 `.avsc` Avro schemas: `_atom_common`, `fs_*`, `text_*`), `donor_ingest/`, `ticket.json.j2`, `dag.atomic-mirror-two-roots.yaml.j2` |
| 77 | `plugins/sql/` | DuckDB/SQLite SQL leaves — `graph/` (21), `ontology/` (20), `vector/` (19), `lake/` (7), `state/` (6), `sink/` (3), `_ddl.sql.j2` |
| 58 | `heex/` | Phoenix HEEx panel templates — `_anchors/` (constants, flags, `_macros/`, `_registries/`, `_universal.heex.j2`) and `panel/` (chart, code, dashboard, data, form, glass, graph, hero, journey, kpi, layer, leary, masked, nav, page, panel, picker, spatial, stack, stepper, tab, terminal, tree, workbench) |
| 54 | `sql/` | SQL render leaves + `_body/` component macros + `_registry/sql_component_registry.j2` + `_macros.sql.j2` + dialect trees (`duckdb`, `postgres`, `sqlite`, `star`, `tier`, `components`, `archive`) |
| 39 | `fp_triad/` | the FP-Triad+Ba render family (`_body/{ex,hs,scala,sh}`, `_bootstrap`, `_classification`, `_envelope`, `_evidence`, `_macros`, `_per_record`, `atom_emit.*`, `fp_module.*`, `structured_classification.{ex,hs,scala}.j2` + two `.eex` twins) |
| 19 | `_migration/` | `divergent/` content-addressed archive of removed corpus_kg/liveview macros (16-hex bucket dirs) + `j2_migration_gaps.csv` + `j2_migration_manifest.csv` |
| 16 | `unix/` | bash `script`/`hook` generator templates + `_body/` macro atoms + citation fragments |
| 16 | `ducklake/` | `macros/{bash,ex}` corpus-cite + ducklake catalog macros (14 of 16 byte-identical to `corpus_kg/`) |
| 14 | `corpus_kg/` | `macros/{bash,ex}` corpus-cite preamble/postamble + evidence/filebar/headpin/pin cite legs |
| 10 | `generic/` | `bashattack/` (dag), `cloud_init/`, `libvirt/`, `podman/` infra templates |
| 8 | `contracts/` | `_body/` doctrine macros + `atom_as_kernel_reality`, `finalattack_integration`, `mythology_index`, `phylum_order_yoneda` heads |
| 8 | `avro/` | Avro `.avsc.j2` schemas (`_ba_envelope`, `dag_*`, `entity`, `receipt`, `render_artifact`, `shacl_report`) |
| 6 | `.idea/` | JetBrains IDE residue (registers `templates/` as a *Java* module — recorded, no conclusion) |
| 5 | `projection/` | `aob_node_to_ex`, `entity_to_ttl`, `_body/{aob_classification_ex,smoke,ttl}` |
| 5 | `_tensor/` | three-axis tensor block render macros (assembler + space/time/value/discriminator_ref) |
| 4 | `silmaril_env/` | `claude_settings.json.j2` + `_body/{comment_block,env_block,hooks_block}` |
| 4 | `dialect/` | jsonschema/linkml `_body` + entity heads |
| 3 | `api_coverage/` | atlas endpoint entities/typedef callers + `linkml_cli/render/_doc_caller_linkml.j2` |
| 3 | `_markdown/` | badges, links, tables macro splits |
| 3 | `_callers/` | tier_classification bash/haskell/scala thin callers |
| 2 | `logs/` | two zero-byte Fuseki logs |
| 2 | `_urn/` | `identity.j2` (quark machinery + `universal_base`), `stamps.j2` (the URN mint + stamp grammar) |
| 2 | `_canon/` | `dewey_template_contract.j2` (the Dewey law), `silmaril_node_kind.j2` |
| 2 | `AtlasContract/` | `_body/md.j2` + `definition.md.j2` |
| 1 each | `core/avro/`, `config/modules/`, `_validate/`, `_text/`, `_dispatch/`, `_cat/`, `_avsc/`, `_ancestry/` | single-file directories (see §3) |
| — | `templates/templates/SEAL.md` | a nested `templates/` holding one `SEAL.md` (the seal record; see §6 fragment-027 gap) |

**Root-level `templates/` files** (13): `_universal_macros.j2`, `_global_constants.j2`, `_test_b3.j2`, `_test_ducklake_catalog_registry_sqlite_fixture.j2`, `_test_ducklake_catalog_sql_fixture.j2`, `_drv_donor_{atlas,bash,ex,sql_ddl,sql_dml}.j2`, `papers-theorems-emit.sh.j2`, `templates.iml`, `erl_crash.dump`.

---

## 3. The macro grammar (universal macros, registries, `_dispatch`, `_urn`, `_canon`, `semantic_render_target`)

### 3.1 `_universal_macros.j2` — the SINGLE SOURCE OF TRUTH hub (528 lines, 0 own macros)

`templates/_universal_macros.j2` header: `_universal_macros.j2 — SINGLE SOURCE OF TRUTH for shared rendering macros.` It **defines ZERO macros of its own** (measured: no `{% macro %}` in all 528 lines). It is entirely `{%- from '<file>' import <names> -%}` seams plus `{%- set X = X -%}` re-exports, so `{% from '_universal_macros.j2' import X %}` resolves every name. Its concurrency law (verbatim): *"Phase B macro-migration anchor blocks (one per leg) — Each B-agent edits ONLY its own START/END marker pair … no race on this hub file."* The hub is organized into base seams (lines 6–20) + eleven anchor blocks B1…B11:

- **Base seams**: `comment_char` (`_registries/comment_prefix.j2`); `sentinel_string` (`sentinel.j2`); `format_concrete` / `impl_concrete`; `lang_convention` + 9 `fp_*` helpers (`lang_convention.j2`); `latex_escape, turtle_escape` (`_text/escape.j2`); `file_link, gospel_ref, section_hr` (`_markdown/links.j2`); `tech_row, pattern_row` (`_markdown/tables.j2`); `badge, horizon_badge, trust_badge` (`_markdown/badges.j2`); `cat_node, lang_edge, econ_state` (`_cat/nodes.j2`); the 7 URN names `urn_for, identity_stamp, universal_base, quark_block, quark, nl_indent_stamp, encoding_stamp` (`_urn/identity.j2`); `avsc_*` (`_avsc/schema.j2`); `urn_grammar_regex, validate_urn_string` (`_validate/urn_grammar.j2`); the 5 `render_*` tensor names (`_tensor/render.j2`); `render_ancestry_entry, render_ancestry_block` (`_ancestry/render.j2`).
- **B1 yoneda** → `yoneda_json.j2`, `yoneda_family_slug.j2`, `yoneda_grounding.j2`, `yoneda_validate.j2`, `yoneda_manifest.j2`.
- **B2 sparql** → `sparql_curie.j2`, `sparql_lookup.j2`, `sparql_emit_prefix.j2`, `sparql_emit_clauses.j2`, `sparql_assemble.j2`.
- **B3 linkml** → `linkml_anchors.j2` (`curie as linkml_curie`, …), `linkml_predicates.j2` (`emit_slot`), `linkml_emit.j2` (`emit_class`), `linkml_family.j2` (`family_slug` + the six per-tier class emitters).
- **B4 ttl** → `ttl_subject.j2`, `ttl_grounds.j2`, `ttl_descriptions.j2`, `ttl_predicates.j2`, `ttl_escape.j2` (`slugify` ONLY — the ttl-variant `turtle_escape`/`urn_slug` are NOT re-exported; they collide with the universal `turtle_escape`).
- **B5 shacl** → `shacl_constraint.j2` (`pattern_for`), `shacl_target.j2` (`curie as shacl_curie`, `predicate_curie as shacl_predicate_curie`), `shacl_shape.j2` (12 emitters incl. the per-tier ring shapes), `shacl_fact_glossary_term.j2`.
- **B6 atlas** → `atlas_csv_cells.j2`, `atlas_row_emit.j2`, `atlas_inverse_derivation.j2`, `atlas_glossary_naming.j2`, `atlas_typedef.j2` (`j_object/j_array/j_scalar/j_kv` = the shared JSON-emitter SoT), `atlas_entity.j2`, `atlas_tier_archive_typedef.j2`, `atlas_donor_entity.j2`, `atlas_species_entity.j2`, `atlas_live_post.j2`, `atlas_tensor_type_entity.j2`.
- **semantic_render_target** (lines 275–287) → the 8 names of `_registries/semantic_render_target.j2` (see §3.6). This is the ONE hub occurrence of the string `semantic_render_target`.
- **B7** → `globals_text_format.j2` (`indent, line_ending`), `globals_render_stamp.j2` (`globals_header_stamp, encoding_sidecar`), `globals_env_exports.j2`.
- **B8 sql-star** → `sql_dialect.j2` → `sql_table.j2` → `sql_star_schema.j2`; `sql_tier_schema.j2`, `sql_tier_dml.j2`, `sql_glossary_star.j2`, `sql_tensor_field_star.j2`, `sql_star_dml.j2` (`lit as star_lit` — collision-aliased).
- **B9 bash leg emitters** → 14 `dim_*_bash` / `fact_*_bash` `<grain>_row`+`<grain>_script`, plus `sh_escape.j2`, `tier_classification_bash.j2` (aliased `node_*`), `broadcast_record_tier_classification_bash.j2` (aliased `bcast_*` — two macro names `tier_case_arm`/`tier_classification_adapter` collide across the bash tier files and are imported UNDER ALIASES so both bodies stay hub-reachable).
- **B10 ex fact-join modules** → 7 `fact_*_ex.j2` (`_pair` + `_module`), `dim_ex.j2` (`dim_ex_module, dim_id_term`), 10 `dim_*_ex.j2`.
- **B11 scala tier adapter** → `broadcast_record_tier_classification_scala.j2` (`tier_case_arm as scala_tier_case_arm, tier_classification_object`).

Note (fragment 023): `papers/_universal_macros.j2` is a **separate** 33,612-byte hub for the papers family — same byte-size as the top-level hub but a distinct file with its own paper-family re-exports.

### 3.2 `_registries/` — what the registries bind (grammar owners)

The registries are the "registry owns the grammar, assembler owns the layout" SoT. Representative bindings (verbatim macro sets recorded in fragments 001–003):

- **`atlas_typedef.j2`** — the canonical Atlas typedef-MODEL JSON emitter and the shared JSON-emitter SoT (`j_kv, j_kv_int, j_kv_bool, j_scalar, j_object, j_array, typedef_array, atlas_typedefs_model`). Determinism law: *"Key order in the dict IS the byte order (callers pass ordered dicts)"*; the six AtlasTypesDef categories emit in fixed order `['enumDefs','structDefs','classificationDefs','entityDefs','relationshipDefs','businessMetadataDefs']`. Imported by every atlas entity/typedef registry.
- **`atlas_entity.j2`** — the entity-INSTANCE emitter (`atlas_entity, atlas_entity_bulk, fact_render_entity, fact_field_entity, rebirth_star_dataset_entity, rebirth_star_dataset_bulk`). TEMPLATE LAW: *"the entity/bulk body is a rendered artifact, so it routes THROUGH a macro — never hand-inlined … 3 agents can render identically (the determinism / anti-lie quorum)."* LINEAGE law: only built-in Process inputs/outputs relationshipAttributes drive the L0→L1→L2→L3→L3.5 chain.
- **`atlas_donor_entity.j2`, `atlas_lineage_entity.j2`, `atlas_species_entity.j2`, `atlas_tensor_type_entity.j2`, `atlas_tier_archive_typedef.j2`, `atlas_live_post.j2`** — per-grain Atlas projections; each carries an anti-fabrication law (`absent optional widths are honestly DROPPED (P4), never defaulted to 0 — a fabricated width is the same sin as a magic number`) and a grounded-namespace triple `{what, where-declared, why}`.
- **`aob_constants.j2` / `aob_family.j2` / `aob_linkml_emit.j2` / `aob_shacl_props.j2`** — the AOB family registry (three families `witness_body / relation_witness / completion_receipt`), a two-level `AOB_SLOT_DEFS` + `AOB_FAMILIES` map projected to LinkML and SHACL. `relation_witness` (predicate type + endpoints + direction + evidence + gap URNs as first-class evidence-bearing relation nodes) is the registry-side mirror of the ledger's FORM-3 relation grammar.
- **`dim_*_bash.j2` / `fact_*_bash.j2`** — turn one rebirth_star grain into a runnable shell program that PRINTS rows AND COMPUTES a runtime census; `dim_*_ex.j2` are one-macro binders onto `dim_ex.j2::dim_ex_module` (which computes primary-key UNIQUENESS as a falsifiable `unique?/0`); `fact_*_ex.j2` compute star-/lineage-join integrity (`joined?/integral?` + enumerated dangling FK sets). Shared "(none)" P4 token: optional fields are printed as `(none)` so absence is visible.
- **`globals_render_stamp.j2`** — the stamp grammar of the storage-leg registries: `globals_header_stamp(comment_urn)` emits two lines, `globals_urn_refs: tab_width=… file_encoding=… …` and `globals_concrete: indent=…-space, encoding=…, …`; `encoding_sidecar()` emits the key=value sidecar for comment-impossible files.
- **`comment_prefix.j2` / `sentinel.j2` / `format_concrete.j2` / `impl_concrete.j2` / `lang_convention.j2`** — sealed underscore-prefixed lookup tables (`_COMMENT_PREFIX_MAP`, `_SENTINEL_MAP`, `_FORMAT_CONCRETE_MAP` 12 entries, `_IMPL_CONCRETE_MAP` 11 entries, `_LANG_CONVENTIONS` 4 formats) each co-located with its single lookup macro (Jinja2 refuses to import `_`-prefixed names).
- **`shacl_shape.j2`** (533 lines) — the canonical SHACL-emitter hub: generic `emit_property/emit_node_shape/emit_rstar_shape/emit_enum_property/emit_typed_property` plus one named macro per memory-pyramid ring node-type (`emit_aob_node_shape, emit_broadcast_record_shape, emit_read_avro_view_shape, emit_l1_segment_shape, emit_l0_ram_ring_shape, emit_l3a_parquet_archive_shape, emit_ducklake_catalog_shape`). The `aob_node` shape's `poetics_cell` slot is closed `sh:in (mythos ethos dianoia lexis melos opsis)`.
- **`sql_dialect.j2 → sql_table.j2 → sql_star_schema.j2`** and **`sql_tier_schema.j2` / `sql_tier_dml.j2` / `sql_glossary_star.j2` / `sql_tensor_field_star.j2` / `sql_star_dml.j2`** — the SQL DDL/DML stack; sqlite-vs-duckdb divergence lives ONLY in `sql_dialect.j2`; `sql_tier_schema.j2` adds `node_fk_def` (the URN node→node tier-lineage FK the star's surrogate-key model lacked).
- **`sparql_*` / `ttl_*` / `linkml_*` / `yoneda_*`** — clause emitters, triple emitters, class emitters, and the yoneda-manifest fibre (`HOM_MATRIX` 17 node-families with `validate_hom_arrow` emitting `OK` / `GAP:…` verdicts — the Präriehund honest-gap idiom in template form).

### 3.3 `_dispatch/` — the one dispatch file, type→macro seam verbatim

`templates/_dispatch/dim_term_species_script.sh.j2` (whole file, 8 lines) is the corpus's only `_dispatch/` file — a self-declared *"thin NON-MACRO dispatcher … Adds ZERO macro logic; it only binds the render context (term_species rows + comment_urn) to the existing `_registries/dim_term_species_bash.j2` grammar. This is the Canonical 'non-macro helper template (branch-only)' seam."* Its type→macro seam:
```
{%- from '_universal_macros.j2' import dim_term_species_script -%}
{{- dim_term_species_script(term_species, comment_urn) -}}
```
Other dispatch-shaped seams live inside slice files rather than in `_dispatch/`: the atom-family `type→{% include %}` seams of `atomic_mirror/_macros/envelope_header.j2` (`kind ∈ {yaml,sh,py,json}`) and `traceback.j2` (`kind ∈ {jsonld,yaml,nt}`); the `linkml/dispatcher.j2`, `shacl/dispatcher.j2`, `ttl/dispatcher.j2`, `atlas/dispatcher.j2`, `yoneda/dispatcher.j2` family-slug include chains; the `sh.j2` / `_run_function.ex.j2` rule.kind switches; and the `papers/_diagrams/*/dispatch.j2` paper-kind dispatchers.

### 3.4 `_urn/` — the URN mint + stamp grammar verbatim

`templates/_urn/stamps.j2` owns the four quark-free stamp emitters; the URN-mint grammar is the entire body of `urn_for`:
```
urn_for(kind, sha256, ns)  →  {{ (ns ~ ':atomic_mirror/' ~ kind ~ '/' ~ sha256) | tojson }}
```
i.e. `<ns>:atomic_mirror/<kind>/<sha256>`, JSON-quoted (the same `silmaril:atomic_mirror/<kind>/<rel_path>` grammar `atomic_mirror/_macros/atom_iri.j2` mints as an IRI). `identity_stamp` emits the 4-line `urn:/encoding_urn:/hash:/password:` block; `nl_indent_stamp` and `encoding_stamp` emit the indent/encoding stamp blocks (the latter resolving `format_concrete(format_urn)` / `impl_concrete(impl_urn)` through the registries). `templates/_urn/identity.j2` owns the **quark machinery**: `quark_block` iterates `_QUARK_CATEGORY_URNS × _QUARK_AXIS_URNS` (the 3×3 CAT/ECON/LANG × node-or-arrow/shape/color grid) and `universal_base(node_id, node_kind_urn, edges, state_value, state_range, urn, encoding_urn, hash, password, quark, comment_urn, sentinel_urn)` emits the `── universal base (CAT × LANG × ECON × identity) ──` block.

### 3.5 `_canon/` — the Dewey law verbatim

`templates/_canon/dewey_template_contract.j2` legislates the on-disk path law: *"The on-disk path is the denormalized URN walk: dots and underscores become path separators, and the final segment becomes the filename."* Its `dewey_walk_from_urn(urn)` is the complete filter chain (verbatim):
```
{{ urn | replace('urn:silmaril:entity#', '') | replace('urn:silmaril:type:', 'type:')
       | replace('urn:silmaril:glossary:', 'glossary:') | replace('urn:silmaril:', '')
       | replace(':', '/') | replace('.', '/') | replace('_', '/') }}
```
plus `dewey_template_path_from_urn`, `dewey_path_from_segments`, `template_locus(family, rel_path) → templates/{{ family }}/{{ rel_path }}`. `_canon/silmaril_node_kind.j2` holds only two caller-supplied lookups (`sm_class_for_node_kind`, `sm_root_for_node_kind`) — it deliberately *"must not redefine the enum/root map"* (values come from `config/constants/universal.exs` + the canon seed; see §6 gap).

### 3.6 `semantic_render_target` — the full-render contract

`templates/_registries/semantic_render_target.j2` (`_registries/semantic_render_target.j2 -- semantic full-render contract.`) is the sole DEFINITION site of the semantic-render contract; the string `semantic_render_target` occurs in exactly three corpus files — this definition site plus the two `_universal_macros.j2` hubs (root and `papers/`) that import and re-export it. It binds four column/field lists + four `_csv()` join macros:

- `semantic_render_target_columns` (**25**, verbatim): `schema_version,entity_urn,source_urn,render_target,graph_module,lambda_contract,topology_contract,effect_monad,semantic_subject,semantic_predicate,semantic_object,verb,adverb,adjective,relation_type,evidence_locus,input_path,input_sha256,input_bytes,output_path,output_sha256,output_bytes,artifact_hash,row_status,trust_scope`
- `atlas_glossary_columns` (**21**, verbatim): `GlossaryName,TermName,ShortDescription,LongDescription,Examples,Abbreviation,Usage,AdditionalAttributes,TranslationTerms,ValidValuesFor,Synonyms,ReplacedBy,ValidValues,ReplacementTerms,SeeAlso,TranslatedTerms,IsA,Antonyms,Classifies,PreferredToTerms,PreferredTerms`
- `full_atlas_proof_columns` = the two concatenated (**46**).
- `required_semantic_render_fields` (**17**): `render_target,graph_module,lambda_contract,topology_contract,effect_monad,semantic_subject,semantic_predicate,semantic_object,verb,adverb,adjective,input_path,input_sha256,input_bytes,output_path,output_sha256,output_bytes`

It is re-exported through the top-level hub (lines 275–287, 8 names) and its only observed consumer is `colimit/verb.atlas.csv.j2` (via `atlas_glossary_columns_csv`, fragment 011). The `semantic_subject/semantic_predicate/semantic_object` triple is the same S·P·O coordinate family as the AOB FORM-3 relation grammar (`base_agents.md` §A.1) and the unary-law's S/O/P towers; the 21 `atlas_glossary_columns` are byte-identical (names + order) to the ledger's §C 21-column Atlas ring.

### 3.7 `_global_constants.j2`, `_tensor/`, `_validate/urn_grammar.j2`

- **`_global_constants.j2`** (declarative constants only, 0 macros): 7 canonical URN-refs to prelude discriminator-Nodes + their decoded concretes (`GLOBAL_TO_IMPLEMENTTABSPACES='2'`, `GLOBAL_FILE_ENCODING='utf-8'`, `GLOBAL_LINE_ENDING='LF'`, `LANG/LC_ALL='en_US.UTF-8'`, `PYTHONUTF8='1'`, `PYTHONIOENCODING='utf-8'`); the V4 comment-prefix/format/impl URN discriminators (`COMMENT_HASH/DOUBLE_SLASH/DOUBLE_DASH/PERCENT`, `FORMAT_SH/SCALA/HS`, `IMPL_BASH/JVM/GHC/BEAM`, `SENTINEL_UNSTAMPED_URN`); and `ALARM_PATH_DUNBAR_IMMEDIATE = 'Dunbar-immediate'`.
- **`_tensor/`**: `render.j2` is the three-axis ASSEMBLER `render_tensor_block` (fail-closed: an incomplete tensor raises `UndefinedError` via the `__avogadro_missing_complete_three_axis_tensor__` guard under StrictUndefined); `space.j2`/`time.j2`/`value.j2` render the three axes (cardinality/dimensions/bounded/max_size/bit_width/byte_width/alignment · dynamics/ordering/monotonic/lifetime/byte_order/arithmetic · interpret_as/domain/read_via/write_via); `discriminator_ref.j2` renders `{type_node, type_urn}` discriminator refs.
- **`_validate/urn_grammar.j2`** — the URN grammar regex (EXEMPT from the no-primitive rule as the bootstrap-paradox source of truth), verbatim:
```
^urn:(avogadro|silmaril):(leaf|file|art|func|integration|fd|syscall|need|call|entity|atomic_mirror)([:#]([A-Za-z0-9_][A-Za-z0-9_./-]*(::[A-Za-z0-9_][A-Za-z0-9_./-]*)*)?)?(@([^/@[:space:]]+(/[^/@[:space:]]+)*))?(/(fd|needs|wants|calls|callers|interface|implementation|process_model|syscall_budget|avogadro|trichotomy|emits|consumes|fut)(/([^/[:space:]]+))?)?$
```
with `validate_urn_string(varname, ctx, urn_value, emit_bash_check)` doing render-time StrictUndefined enforcement + optional bash-runtime `grep` check. Observation (fragment 004 G4): its render-time prefix check also accepts `urn:users:`, which the regex does not admit — both quoted, source does not reconcile.

---

## 4. Per-directory deep accounts (merged from fragments)

**`_registries/` (111 files, fragments 001–003).** The grammar-owner layer. Universal design laws stated across nearly every file: (a) *registry owns grammar / assembler owns layout*; (b) GROUND LAW VI — *"NOTHING is inlined except the POSIX shebang"* (imports, never inline literals); (c) GROUND LAW VIII — *"a render is LIVE CODE … graded on EXECUTION, not presence"* (the dim/fact/tier/broadcast emitters render runnable bash/ex/scala/hs programs that COMPUTE a census/verdict when run); (d) P4 honest-absence — optional fields render the visible `(none)` token, never a hidden drop, and never a fabricated value ("a fabricated width is the same sin as a magic number"); (e) StrictUndefined fail-closed on required fields; (f) cross-leg EXECUTION consensus (the Set-0 gate runs each leg as live code and asserts `diff <(bash) <(./hs) <(scala)` == empty). Intra-slice dependency spine (each edge named by the importing source): `atlas_typedef.j2` ← `atlas_entity.j2` ← {donor/lineage/species/tensor_type entity registries}; `aob_constants.j2` ← `aob_family.j2` ← {aob_linkml_emit, aob_shacl_props}; `comment_prefix.j2::comment_char` ← every storage-leg emitter.

**`colimit/` (214 files, fragments 006–011).** The colimit render family — every AOB atom fans out to `atlas/linkml/shacl/ttl/yoneda/sparql` leaf bodies plus the `_body/{ex,hs,sh,scala}` projection assemblers and the paired rule-kind `_body/*.{ex,sh}` legs (block_comment_scan, canonical_set_shadow, count_floor/ratio, csv_emitter, file_presence, ldap_*, parity, regex_window, anchor_dictionary). The colimit-root emitters (`aob_node/aob_relation_witness/aob_witness_body/aob_completion_receipt`, `dim_*`, `fact_*`, `ring_l0..l35`, `l1_segment/l3_parquet_archive/read_avro_view/catalog/broadcast_record`, `verb.*`, `tier.*`) each render one node-type in one or more legs. Dispatchers (`linkml/shacl/ttl/atlas/yoneda/dispatcher.j2`) dispatch by `{% include %}` of a per-family template, never by direct macro call. The memory-pyramid tier spine recurs verbatim: `aob_node → broadcast_record → l1_segment → read_avro_view → parquet_archive → ducklake_catalog` = L0→L1→L2→L3→L3.5.

**`integration/macros/` (244 files, fragments 015–021).** One file = one URN-stamped POSIX/syscall/storage macro, across seven language lanes. No `{% macro %}` blocks — macro identity is the line-1 URN stamp (`{# urn:silmaril:macro#integration.macros.<lane>.<family>.<snake_name> #}`) and the signature is the `{{ }}` placeholder set. Inputs/outputs are URN-typed (`urn:silmaril:entity#types.kingdom.atom.phylum.<facet>.class.kind_node_type_def.instance.<type>`, facet `domain`/`src` — the same entity-URN grammar the ledger §A.2 shows on a `corpus:ValueNode`). A `{{{ var }}}` / `${{{ var }}}` triple-brace idiom emits a second live substitution layer (bash `${var}` / Elixir `#{var}`) — whose renderer/config is not in the corpus (§6 gaps 017/020).

**`atomic_mirror/` (79 files, fragments 004–006).** The ".d/ atomic mirror" generator — every source file gets a sibling `.d/` tree disintegrating it into contracts + projections (the 9-cell `{forge,unix,joy}×{bit,byte,word}` matrix, three eigenstates `expected=matter / unexpected=anti-matter / unknown=γ|unknown⟩` each ≥3 entries — the RULE OF THREE / SPACE Axiom 2). The γ-unknown eigenstate MUST propagate to Dunbar layer 0 (`alarm_path: Dunbar-immediate`) and cannot be silently swallowed — the Präriehund honest-gap discipline encoded as a render contract. `_macros/` holds the split-one-concern macros (atom_iri, dag_nodes, envelope_header, provenance, rdf_triples, shacl_claims, traceback); `schemas/` holds the 11 Avro `.avsc` file-type schemas.

**`fp_triad/` (39 files, fragment 013).** The Haskell/Elixir/Scala/Bash render family (the doctrine's FP triad `Haskell, Elixir, Scala` + Ba). Objective parse probe recorded: `_body/hs.j2` and `_body/scala.j2` raise `TemplateSyntaxError` (endif-inside-for) at hs.j2:30 / scala.j2:24, while `ex.j2`/`sh.j2` parse OK — matching the "SILMARIL FORK 2026-05-18" fork-fix comments present in ex/sh and absent in hs/scala.

**`papers/` (85 files, fragments 022–023).** LaTeX render family with per-diagram-kind dispatchers over `urn:silmaril:entity#types.papers.*` discriminator URNs, a `latex_label_slug` variant family (3/4/6-char replace-sets), and its own `papers/_universal_macros.j2` hub.

**`plugins/sql/` + `sql/` (131 files, fragments 024–027).** DuckDB/SQLite/Postgres/DuckLake SQL leaves; `plugins/sql/{graph,ontology,vector,lake,state,sink}` query families; `sql/` render leaves import a single `_body/*` or `_registries/*` macro inside a `{% filter trim %}` wrapper. `unix/` holds the bash `script`/`hook` generator macro definitions.

**`heex/` (58 files, fragments 014,015,020).** Phoenix HEEx panels; leaves import `heex/_anchors/_universal.heex.j2 as u` and call family macros; the `_anchors/` tree holds the flags/mythic/journey/graph constant + macro registries.

**Smaller families**: `_migration/divergent/**` (content-addressed archive of removed corpus_kg/liveview macros, each bucket dir = first 16 hex of the file's own sha256, with `j2_migration_{gaps,manifest}.csv` as the corpus's own Präriehund register — every removed divergence named as an explicit gap with `next_action: reconcile against sm_NodeKind canon and forge/type spec shape`); `corpus_kg/` + `ducklake/` (14 of 16 ducklake files byte-identical to corpus_kg); `avro/` + `core/avro/` (Avro schemas); `generic/` (cloud_init/libvirt/podman/bashattack infra); `contracts/`, `dialect/`, `projection/`, `silmaril_env/`, `api_coverage/`, `AtlasContract/`, `_markdown/`, `_callers/`.

---

## 5. Cross-corpus references to the AOB shape (`ledger/W1/base_agents.md`)

`base_templates` is the RENDER side; `base_agents` is the ATOM side. The templates project atoms to the emitter fan-out; the cross-references below are cited from the ledger only where a template names the shared coordinate (cite, never re-derive):

- **21-column Atlas glossary ring** — `_registries/atlas_row_emit.j2::emit_row` (16 populated positions, columns 13/14/16/19/21 always empty), `atlas_glossary_naming.j2::glossary_name`, `atlas_csv_cells.j2`, `atlas_inverse_derivation.j2` (AdditionalAttributes/SeeAlso), and `semantic_render_target.j2::atlas_glossary_columns` all project the ledger §C ring `GlossaryName, TermName, …, Antonyms, Classifies, PreferredToTerms, PreferredTerms`.
- **The per-field `tensor` block** (Byte-Stream Carrier Closure) — `_tensor/{render,space,time,value}.j2` render exactly the ledger §B.2 `tensor: space:{cardinality,dimensions,bounded,max_size:128,bit_width:8,byte_width:1,alignment:1} time:{…} value:{interpret_as,domain}` shape; `_registries/{dim_tensor_type,fact_field,sql_tensor_field_star}` project its `bit_width/byte_width` coordinates. The unary-law `1..128` bound appears literally (`max_size:128`, `bit_width:8`).
- **FORM-3 relations / entity·dewey·ancestry planes** (§A.1) — `_registries/aob_family.j2::relation_witness` (relation_urn/predicate/source/target/evidence/gap slots) mirrors the curried `s@p@o` relation grammar; the `dim_node`/`fact_*` grains project `entity:{urn, display_name, grounding, kind_urn}`; `_ancestry/render.j2` renders the `[{axis, via}]` ancestry list; `_canon/dewey_template_contract.j2` is the base_templates-side realization of the `dewey_path` plane + golden path rule `golden/specs/<dewey_path>.aob.dir`.
- **Projection / emitter family** (§F) — the whole corpus IS the render side of the ledger's `*.sh · *.ex · *.scala · *.hs · *.atlas.csv · *.linkml.yaml · *.shacl.ttl (· *.osi.yaml)` fan-out with cross-leg functional consensus (the Set-0 gate).
- **Yoneda "node IS its arrows"** (§H) — `AtlasContract/_body/md.j2` Yoneda paragraph, `_registries/yoneda_*` fibre (`HOM_MATRIX`, `validate_hom_arrow`), `colimit/_body/yoneda/*`.
- **Dunbar layer / immediate alarm** (§E) — `_global_constants.j2::ALARM_PATH_DUNBAR_IMMEDIATE`, `atomic_mirror/atomic_evaluation/dunbar/gamma_propagation.yaml.j2` (`dunbar_layer: 0`, `alarm_severity: immediate`, `γ_propagate ⊣ dunbar`).
- **Telephone memory tiers L0/L1/L2/L3** (§G) — the memory-pyramid spine across `_registries/{shacl_shape,sql_tier_schema,linkml_family}` and `colimit/ring_l*`; the `.avro` OcfAppender/`{:telephone_record, record}` wire mechanism named in `sql_tier_schema.j2` matches the ledger's `logs/hooks/*.avro` wire bus. (The `L3.5` ducklake rung is a corpus extension not named in the ledger — recorded as-is.)
- **Joern citation URN** (§D.2) — `api_render/linkml_cli_project_class.j2` names a `joern_urn` source link matching the ledger's `urn:silmaril:joern:apache__jena:javasrc@<sha>` shape.
- **CCO anchoring** (§A.1) — the atlas/dim registries bind CCO curies (`cco:ont00000686/00000853/00000958/00000253/00002006/…`) via the same `cco_target`/`grounds_in_cco` mechanism the ledger records; the specific curies differ from the ledger's exemplar `cco:ont00000995` (mechanism shared, ids distinct — no equation asserted).
- **Synonym/antonym first-class families** (§C) — `_registries/ttl_predicates.j2` (`emit_has_synonym` → literal, `emit_has_antonym` → node) and the `colimit/_body/*/{synonym,antonym}` atoms project the ledger's paired Synonyms/Antonyms columns + `encyclopedia_{synonym,antonym,acronym}` atom families.

**Honest non-matches recorded (not force-fit).** The AOB-family names `witness_body / relation_witness / completion_receipt` (the `aob_*` registries) appear NOWHERE in `base_agents.md` (grep: zero hits) — no ledger block cites them, recorded as an honest non-match. The `r1_staging/atlas_models/**` entityDefs (`silmaril_l1f_*`, `silmaril_l3a_*`, `silmaril_l35en_*`, `0000-universal-aob-contract`) that the tier registries cite as their grammar ground are not named in the ledger. `grounds_in_cceo`, `cpo_process_iri`, `cheese_trap_immunity`, `circuit_imprint_tensor` have no matching ledger block. The broadcast-tier classification names disagree internally between legs (bash: `silmaril_l1f_durable_commit`/`silmaril_l3en_ring_tier`; haskell+scala: `silmaril_l1c_durability_acked`/`silmaril_l3a_ring_tier`) — held verbatim, unharmonized (see §7).

---

## 6. Honest-gap register (every PROVISIONAL carried verbatim from the fragments)

Fragments 001, 002, 003, 009, 010, 011, 013, 023, 024, 026, 028 declared **NO PROVISIONAL entries** (their cross-slice/cross-corpus references resolve to named files owned by sibling mappers, not unresolvable unknowns — PROVISIONAL is never used to dodge resolvable work). The genuine gaps, by fragment:

**Fragment 000 (`.git`/root + `_migration/divergent` + `_registries` head):**
1. `AtlasContract/definition.md.j2`: named consumers `bin/ba-atlas-render`, `specs/atlas/_tools.yaml`, `store/atlas/` do not exist inside `forge/base_templates`; host repo unresolvable from this corpus + AOB ledger (ledger does not name `ba-atlas-render`).
2. `_canon/silmaril_node_kind.j2`: named value source `config/constants/universal.exs` + "current canon seed" not in this corpus; ledger attests a `config/constants` tree in `base_agents` but not `universal.exs` itself.
3. `_global_constants.j2`: named mirror `atomic_mirror/schemas/fs_unreadable.avsc` and `SHACL DunbarPropagationShape` not in this corpus; host location unresolvable here (Dunbar family attested by ledger §E, the shape itself not).
4. `_migration/divergent/**` (family): the divergence baseline (the `agents-phx-real` tree the 16-hex-bucketed copies diverged from) is not in this corpus and not named by the AOB ledger; the digest-prefix bucket naming is measured (11/11), the intent is inference.
5. `_drv_donor_*` family: the expansion of "drv" is stated nowhere in the slice; lexical identity unresolved (function of the files is fully accounted regardless).

**Fragment 004 (`_universal_macros`/`_urn`/`_tensor`/atomic_mirror head):**
- **G1 (PROVISIONAL, cross-slice deferral):** `aob_node` tier node-type ↔ ledger `.aob.dir` AOB atom. Slice-004 sources name "AOB"/"aob_node"/"aob_ducklake_catalog"; ledger §A.1 defines the canonical `.aob.dir` dense-node atom. Name-level correspondence cited; field-level correspondence could not be resolved from slice-004 alone because the defining registries (`sql_tier_schema.j2`, `linkml_family.j2`, `shacl_shape.j2`) are outside that slice. **Synthesis resolution (this map):** those registries are now accounted (fragments 002/003) — the `aob_node` relational node-type projects the atom's identity/entity/dewey planes (`urn, spec_path, display_name, layer, kind_urn, spec_blob_sha, dewey_walk_ok`) as a flattened relational leg of the atom whose canonical dense-node form is the ledger's `.aob.dir` `entity:{urn, display_name, grounding, kind_urn}` + dewey plane. The correspondence is shape-level (inference from shared field names), not a byte-level identity; it does not upgrade to CONFIRMED because no atom instance is co-resident to diff. Carried as a documented, now-shape-resolved gap.

**Fragment 005 (`atomic_mirror/**` part 1):**
- Out-of-corpus citation targets (CITED-NOT-VERIFIED, genuinely unresolvable inside `forge/base_templates`): "Cook's 2026-04-17 ruling"; `specs/db/Column.yaml`; `memory:feedback_kernel_trace_visibility`; `$SILMARIL_PROJ_DIR/sandbox/REALMS/GLOBAL/.global/data/leahry/_leahry.yaml` + "colimit plan-roadmap.md §Atom-type-taxonomy"; `$SILMARIL_PROJ_DIR/.../atomic_mirror.context.jsonld` + `.../schemas/contracts/*` + `/proj/gitprojects/bls/schemas/contracts/*`; `$SIL_SYS_ALLURA_DIR/atomic/_colimit/plan-roadmap.md §Phase B.6`; `user00/memory/feedback_format_encoding_contract.md`, `user00/memory/feedback_no_or_true.md`, `bash.txt`, `$ENV_DIR_SIL_BA_IMPL` FinalAttack tree.

**Fragment 006 (`atomic_mirror` tail + `avro/` + `colimit/_body/atlas` head):**
1. `$SIL_SYS_ALLURA_DIR/atomic/_colimit/plan-roadmap.md` — env-var-rooted external path, not in the pinned working tree.
2. `ba/schemas/.specs/avro/Entity.v1.spec.yaml` — no `ba/` root in `forge/base_templates`; consuming-repo referent.
3. `ba::render::stamp_atom` — bash function of the consuming ba engine, not in this corpus.
4. `generators/atomic_mirror` — regeneration path, no such path in this corpus.
5. "Cook's 2026-04-17 indentation ruling" — ruling document not present in this corpus.

**Fragment 007 (`colimit/_body` rule-kind legs + linkml head):**
2. Cited feedback doctrine files absent — `feedback_silent_swallow.md`, `feedback_strict_unix_determinism`, `[[feedback_leverage_global_macros_constants]]` are cited as normative by files 12–31 and `ex.j2`, but no `*feedback*` file exists under `forge/base_templates`; their content is unverifiable here.
3. `P13.5.d` (files 13, 22) and `C1` discipline (files 13, 15) are used as if defined elsewhere; no slice file (or path named by one) defines them — recorded as opaque identifiers.
4. `count_floor.ex.j2` opens with `Project Unix doctrine: ALL 17 rules FAIL.` — the source names no rule list; which 17 rules is unresolvable from the slice.

**Fragment 008 (`colimit/_body` linkml/shacl bodies + projection macros):**
1. `regex_window.sh.j2`: the emitted awk window-branch sets `_ec=1` inside the awk program (awk-local), so the enclosing shell function's `_ec` return path is source-ambiguous; resolution needs the render harness/corroboration fixtures (outside slice).
2. `regex_window.sh.j2`: header names `$RW_FILES`, emitted code reads `${RW_FILES_FILE}` — recorded as header/code naming drift, resolved AGAINST the header by `sh.j2`'s `RW_FILES_FILE` export (entry 31); kept as a note.

**Fragment 012 (`dialect/` + `contracts` + `corpus_kg/` + `ducklake/`):**
- `bin/ba-spec-render` + named specs `specs/contracts/{atom_as_kernel_reality,finalattack_integration,mythology_index}.spec.yaml` absent from the entire working tree; external resolution unresolvable here (entries 2,3,4).
- `lib/ontology/render.sh` / `core/ontology/lib/render.sh` (+ `BA_RENDER_DIALECTS`) absent from the working tree (entries 23,24).
- `lib/telephone/storage/duck_runner/sql.ex` / `Telephone.Storage.DuckRunner.SQL` (the ground truth for the ducklake catalog `@catalog_path/@catalog_alias/@data_path` constants) absent everywhere in the working tree (entries 32,40).

**Fragment 014 (`heex/_anchors/**`):**
- `__refute1_before_flags_mythic.heex.j2` filename convention is defined by no file in the slice and by no comment in the file; inference (marked) it is a preserved pre-split witness of `_flags_mythic` "before" its constants/species split; the naming/refutation protocol is unresolvable from the slice.

**Fragment 015 (`heex/panel` tail + `integration/macros/_*` + bash/compose):**
- `bash/compose/kv/semicolon/join.sh.j2`: caller-side iteration discipline for the documented `pairs` input is unresolvable in-slice — the body renders exactly one `;k=v` pair with literal surrounding newlines while the doc specifies `k1=v1;k2=v2;...`. Both texts captured verbatim; not force-fit either way.

**Fragment 016 (`integration/macros/bash` compression/control/duckdb/frame/hash/posix):**
1. `primitives.ttl` absent — named `Reference: primitives.ttl §primitives.control.{conditional,loop}` by all 6 `control/` templates; no such file exists anywhere under `/home/user/silmaril`.
2. `_preamble` import seam unresolved — the flat path `integration/macros/bash/frame/errtrace_err_trap.sh.j2` is not in the inventory; the on-disk analogue `frame/errtrace/err/trap.sh.j2` defines no `{% macro %}` for the dotted call `et.errtrace_err_trap(...)`; renderer-side loader/aliasing is outside `base_templates`.
3. `Factory Charter §2.4` — no charter document in the working tree (string occurs only inside templates citing it).
4. `feedback_bash_strictness_trap_not_pipefail.md` (host path `$HOME/.claude/projects/-home-tristan-Music-final/memory/…`) and `feedback_cheese_text_emission_quirks.md` — the named memory directory does not exist on this host.
5. `cheese_text` defined nowhere in corpus or ledger — nearest referents are the `wire-cheese-call`/`wire-cheese-status` skills + "schema/cheese drift" (ledger §E).

**Fragment 017 (`integration/macros/bash` posix/proc/process/pyarrow/ssh/telephone/text):**
- **P1** — triple-brace render semantics: 13 files use `{{{ var }}}`/`${{{ var }}}` while `posix/stat/file/byte/size.sh.j2` uses the unambiguous `{{ '{' }}…{{ '}' }}` idiom; the renderer/config that fixes the triple-brace semantics is not in this slice (stock Jinja2 defaults make it ambiguous). Intended bash output stated by the files' own comments.
- **P2** — `primitives.ttl L218` (pyarrow template): `primitives.ttl` returns nothing over the full working tree; the "DuckDB-v1.5.2-has-no-ORC-writer" claim rests solely on the template comment; line L218 unverifiable.
- **P3** — `primitives.ssh.*` / `primitives.text.bash.*` / `SPECIES primitives.*` defining spec blocks appear only inside the ssh/text macro templates and nowhere in the ledger; the defining "SPECIES"/primitives catalog is not present in the mapped corpus or the ledger.

**Fragment 018 (`integration/macros/bash/text` tail + `time` + `elixir/_preamble` + `ex/**`):**
- `macros/elixir/` vs `macros/ex/` lane relation: `elixir/_preamble.ex.j2` is the sole `elixir/`-lane file, the sole slice file without a URN stamp, and diverges from `ex/_preamble.ex.j2` (`defmodule`+`@moduledoc` vs comment-only Phase R4 preamble); no owned file states whether `elixir/` is a predecessor, duplicate, or distinct render target; resolution requires out-of-slice registries/migration records.

**Fragment 019 (`integration/macros/{ex,haskell,heex}`):**
- `cheese_text` provider binding — the executable name appears nowhere in the ledger; nearest referents are the `wire-cheese-call`/`wire-cheese-status` skills and "schema/cheese drift" (§E); the binding from this macro's `cheese_text` CLI to a concrete provider is unresolvable from the slice + ledger.

**Fragment 020 (`integration/macros/{heex,liveview,python}`):**
- **020-1** — renderer/engine binding: no file names the engine that renders it; `.j2` suffix + `{{ }}`/`{# #}` grammar are observations, not definitions (unary law rule 13); the binding is resolvable only from other slices' registry/dispatch entries.
- **020-2** — `pg03-honeycomb FallbackTable` pattern referent: not in the ledger; ledger §I's honeycomb lattice is the closest named surface.
- **020-3** — `SilmarilWireWeb` (used via `use SilmarilWireWeb, :live_view`): its module definition is not in the slice; ledger names the `silmaril_wire` BEAM daemon (§G) but never the module `SilmarilWireWeb`.

**Fragment 021 (`integration/macros` tail + `logs/` + `papers-theorems-emit` + `papers/_appendix` head):**
- Files 32 & 33 — the two zero-byte Fuseki logs `templates/logs/fuseki-request.log` and `templates/logs/fuseki.log`: role/provenance unresolvable from empty content; role is inferred only from the path.

**Fragment 022 (`papers/{_appendix,_body,_diagrams}`):**
- External source citations unresolvable from the working tree: `$BA_ACTOR_HOME/sandbox/inventory/engine-spans.md`, `$BA_ACTOR_HOME/sandbox/specs/engine/Exec.*.yaml`, `$BA_ACTOR_HOME/example_avogadro.yml`, `$HOME/.claude/plans/dynamic-popping-grove.md`, `$BA_ACTOR_HOME/sandbox/dags/pipeline-vision-chain.yml`, `$HOME/Downloads/actual/17/texture.tex`, `$BA_ACTOR_HOME/sandbox/specs/linkml/silmaril-{roster,federation}.linkml.yaml`, `$ENV_DIR_DOCS_HUB/paper/compass_artifact_…md`, `$BA_ACTOR_HOME/slurm.md`, `$BA_ACTOR_HOME/sandbox/papers/…/fp-triple/`, plan "tender-brewing-oasis", `$ENV_DIR_SIL_SHARED_TEMPLATES/papers/section.tex.j2`. Whether `$BA_ACTOR_HOME` denotes `forge/base_agents` is an inference, not established by any in-slice text.

**Fragment 025 (`plugins/sql/{ontology,sink,state,vector}` + `projection/`):**
- The "LIVE Set-0.C universal-aob-contract Atlas model" fixture is named by reference but no URN literal appears in the file, the slice, or the ledger; the concrete fixture identity remains open (files 37 + shared).

**Fragment 027 (`sql/` + `unix/`):**
- **G1** — `SEAL.md` (`templates/templates/SEAL.md`) describes the `ba/templates/` sealed tree under `$BA_DIR`; this slice lives under `forge/base_templates/templates/`. Whether the `unix/{script,hook}.sh.j2` + `unix/citation-block.j2` present here are the SEALED copies, the FRONTIER, or a third `forge/`-rooted tree is not resolvable from any slice file — a genuine cross-tree unknown for the census/account tasks.
- **G2** — the star/tier SQL anchors (`sql/` files) import registry macros (`emit_star_ddl/dml`, `emit_tier_ddl/dml`, `emit_ducklake_catalog_ddl`, `emit_read_avro_view_ddl`, `read_csv/read_parquet/select/where_filter/snapshots_select/attach_database`) from `_registries/*` and `sql/_body/*` outside the slice. **Synthesis note:** these are now accounted in fragments 002/003 (the `sql_star_*`, `sql_tier_*`, `sql/_body/*` registries) — cross-slice pointers resolved, not gaps of the merged map.

---

## 7. Conflict resolutions (recorded per the brief)

1. **Working-tree HEAD (fragment 026 concern).** Fragment 026 observed `git rev-parse HEAD = a4e66a065659d2d355f065bbd8cded6aa2fc1430` during its run, differing from the pinned `eb3d916…`. **Resolved by re-verification at synthesis time:** both the `forge/base_templates` submodule and the `silmaril` superproject `git rev-parse HEAD` now equal `eb3d916b0db5c1429e0ce5abaac7b6b75aadea18` (the pin), and every other mapper that checked (000, 005, 006, 012, 016, 017, 022, 027) recorded `eb3d916…`. The a4e66a0 reading was a transient during that mapper's window. The binding authority is the manifest: all 1118 `sha256/bytes` pairs are byte-verified against the current on-disk tree (§below), so the mapped bytes are the `eb3d916…` bytes regardless of the transient HEAD.
2. **broadcast_record classification-name divergence (fragment 001).** The bash tier-classification leg names `silmaril_l1f_durable_commit` / `silmaril_l3en_ring_tier`; the haskell + scala legs name `silmaril_l1c_durability_acked` / `silmaril_l3a_ring_tier`. Both quoted verbatim from their files; both claim verification against `r1_staging/atlas_models/**` (outside this corpus). Not harmonized here — resolution belongs to Task 3 (census) / Task 4 (account), which can consult the atlas-model JSONs the files cite. Recorded as an intra-corpus divergence held verbatim, not a mapper error.
3. **Header/code drift notes (fragments 008, 018, 026, 003).** `regex_window.sh.j2` `$RW_FILES` vs `${RW_FILES_FILE}` resolved against the header by `sh.j2`'s export; `silmaril_env/_body/comment_block.j2` and several `_universal_macros.j2` in-comment line references are stale relative to current file state; `sql_star_dml.j2`/`sql_tier_dml.j2` header prose says `sql/_body/components.j2` while the `{% from %}` imports `sql/_body/clause.j2`. Each is recorded as a faithful capture of on-disk bytes (the import statement is authoritative for behavior); none is silently corrected.
4. **LICENSE vs doctrine footer** — BSD-3-Clause (this submodule) vs Apache 2.0 (doctrine footer); recorded as an observed difference, no reconciliation asserted (out of mapper scope).

---

## 8. Coverage statement

The manifest `ledger/W1/manifests/base_templates.manifest` is the union of the 29 fragment manifests, sorted by path, one tab-separated `sha256<TAB>bytes<TAB>path` line per inventory file. Verified: (a) 1118 lines, no duplicate paths, no malformed lines; (b) the path set is byte-identical to `t1-inventory.txt` AND to a live `find forge/base_templates -type f -not -path "*/.git/*"`; (c) every one of the 1118 `sha256` + `bytes` values recomputed against the working tree with **zero mismatches**. The shared acceptance check passes green:

```
COVERAGE EXACT: forge/base_templates == ledger/W1/manifests/base_templates.manifest (1118 files)
```

Every file in the inventory has a manifest line and a fragment map entry; `templates/erl_crash.dump` (2.8 MB BEAM crash dump, `=erl_crash_dump:0.5`, 89,188 lines, 1870 `=` markers, crashing process `<0.0.0>` `init` during boot) was given the full binary structural pass + digest per the binary protocol. No file was skipped, sampled, or truncated in the underlying fragment reads.
