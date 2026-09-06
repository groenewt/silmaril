# W2 · Sub-project 5 — File + subatomic file-format taxonomy (design)

> **Brainstorming design doc** (superpowers:brainstorming) — one of the SP2–SP9 batch presented
> for a single maintainer review pass (Directive 14). Design-first HARD GATE: no
> `.ttl`/`.sparql`/implementation until the batch is approved; terminal step →
> superpowers:writing-plans. **THIS ITERATION's v1** — corpus-agnostic, built to be re-run and
> relaunched, not permanent (Directive 13). Zero live-corpus binding (that is W5). Genuinely
> undecidable gaps are marked `silm:isProvisional` with a documented gap, never force-fit
> (Präriehund honesty).
>
> **LIFT, do not invent (Directive 1).** Every class below is a re-expression of an authored
> Helios structure. The authored sources and their `helios/` paths are named inline and collected
> in §5. The design ethos is **PROGENITOR + COMPOSABILITY**: each distinct format/charset/
> byte-order/comment-style is its own atom under an **agnostic progenitor** parent, wired by an
> explicit `ancestry.via` edge — nothing crammed into one, no reductive either/or.

**Binding sources:** the committed SP1 floor (`basicttl/primitives/*`), `docs/unary-byte-frame-law.md`
(byte-stream carrier closure), `docs/praeriehund-demokratie-der-kategorien.md`,
`ledger/W2/design_constraints.md`, the six Helios maps under `ledger/W2/helios/`, and STRICTNESS
Rules 3 (full-lexical identity), 5 (subatomic decomposition — "a div is not a title"), 6 (polysemy
is literal), 14 (distinct files for distinct concerns).

---

## 1. Goal

Author the two linked, corpus-agnostic taxonomies that let every artefact be addressed both as a
*thing on disk* and as *typed subatomic content*, by **lifting** the authored Helios format/type
layer:

- **(a) Format-axis (the meaning olog)** — the authored `format` **discriminator progenitor** and
  its explicit children `format_{avro,json,ex,hs,md,py,scala,sh,shacl,ttl,yaml,jsonld}`
  (`helios/srcy/appendices/39_appendix_e_research_source_mirror/sections/specs/types/prelude/format*.spec.yaml.tex`),
  each a CCO Information Content Entity subtype, plus the three **sibling encoding-facet
  progenitors** that co-type a format's bytes: `charset` → `{ascii,latin1,utf8,utf16be,utf16le}`,
  `comment_prefix` → `{hash,double_dash,double_slash,percent,semicolon}`, `byte_order` →
  `{little,big,host,none}`. Every format decomposes into **its own** subatomic component species
  (Turtle → triples; Markdown → headings + fenced code; a `text_turtle` species is NOT a
  `text_markdown` species — Rule 5).
- **(b) File-axis (the carrier olog)** — the authored **14-type atom taxonomy** `T1..T14`
  materialised by the `.avsc` schemas
  (`helios/00_src_specs/templates/atomic_mirror/schemas/*.avsc`): the filesystem-bearer species
  `fs_{regular,dir,symlink,binary,device,unreadable}` and the text-format species
  `text_{turtle,markdown,json,yaml,script}`, all composing the shared `AtomCommon`
  (`atom_iri, source_path, source_sha256, qualified_name, parent_atom, provenance, …`). A file's
  bytes bottom out at the SP1 physical carrier ladder.

Every **render leg** declares its leaf format + `parser_selector` (lifted from
`helios/01_data_src_specs/triad_projection_validation.spec.yaml`: `rdflib.Graph.parse(format=turtle)`,
`rdflib.plugins.sparql.prepareQuery`, `yaml.safe_load`). File-axis is CCO/BFO-grounded. **Each format
carries its own glossary; SP5 PRODUCES the `fmt:hasGlossary` seam and SP6 CONSUMES it — one forward
edge** (this pins the prior open direction question; see §6).

The deliverable is pure shape (classes, progenitor edges, shapes, ASKs) with the authored formats
lifted and two exemplars fully decomposed — **zero file instances** — so SP8 and W5 bind real files
later.

## 2. Architecture — the progenitor discriminator lattice, glued as a file-level twin-olog colimit

SP5 reuses SP1's exact structure one level up. The two taxonomies are the **twin ologs**; a *file*
is the **colimit-taiji** that glues them; **parse/serialize** is the **monadic realization** whose
Frame carries the parse effect. Every arrow below has a biting tooth in §4.

### 2a. The lifted progenitor pattern (the core structure)

The authored specs realise the maintainer's endianness worked example exactly: an **agnostic
umbrella node-type-def** whose leaves each point back at it by an explicit `ancestry.via` edge. From
`format.spec.yaml` (verbatim): `urn:…types.prelude.format`, `display_name: Format`, note
*"discriminator umbrella for the format axis"*, `ancestry: [{axis: prelude, via: …prelude.node}]`.
From `format_ttl.spec.yaml`: `ancestry: [{axis: prelude, via: …prelude.node}, {axis: domain, via:
…prelude.format}]` — the leaf carries a **second ancestry edge up to the umbrella**. SP5 lifts this
literally:

```
fmt:format  (agnostic progenitor; CCO ICE subtype; ancestryVia → prelude node)
  ├─ fmt:format_avro   ├─ fmt:format_json   ├─ fmt:format_ex    ├─ fmt:format_hs
  ├─ fmt:format_md     ├─ fmt:format_py     ├─ fmt:format_scala ├─ fmt:format_sh
  ├─ fmt:format_shacl  ├─ fmt:format_ttl    ├─ fmt:format_yaml  └─ fmt:format_jsonld
        each: fmt:ancestryVia fmt:format   (lifts {axis: domain, via: …prelude.format})

fmt:charset  ──▶ {ascii, latin1, utf8*, utf16be, utf16le}   (*utf8 = canonical, GLOBAL_FILE_ENCODING)
fmt:comment_prefix ──▶ {hash, double_dash, double_slash, percent, semicolon}
fmt:byte_order ──▶ {little, big, host, none}   (none = the agnostic slot; the progenitor default)
fmt:impl ──▶ {bash, beam, ghc, jvm, fastavro}   (runtime facet; see §6 open Q)
```

These four (five) are **independent** discriminator progenitors — NOT one crammed enum. A file's
encoding is a *product of points* in these axes (a `.ttl` = format_ttl × charset_utf8 ×
comment_prefix_hash × byte_order_none), exactly the geometry the render engine's
`_global_constants.j2` fixes (`FORMAT_SH`, `COMMENT_HASH`, `IMPL_BASH`, `GLOBAL_FILE_ENCODING_URN =
charset_utf8`, `helios/00_src_specs/templates/_global_constants.j2`). `byte_order_none` sitting in
the `none` slot is the endianness-agnostic progenitor the design ethos names.

### 2b. The twin-olog colimit

```
   Format-axis olog             ── ρ (parse / serialize, ──▶   File-axis olog
   (fmt:format + component          Kleisli/Frame arrow)        (the 14-type atom taxonomy;
    species: what the bytes                                      fs_* filesystem bearers +
    MEAN)                        ◀── interpret_as back-pointer ─ text_* content, on-disk bytes)
        └───────────────────────────── colimit ─────────────────────────────┘
                              = the FILE (a file-level taiji)
```

- **Format-axis = formal/yin olog.** Each `fmt:Format` leaf is a CCO Information Content Entity
  subtype (the *meaning*). Its **subatomic component species** are lifted from the per-format
  `.avsc` fields: `text_turtle` (T10) → `{triple_count, parses}`; `text_markdown` (T12) →
  `{h2_count, fenced_code_blocks}`; `text_json` → `{has_context, parses}`; `text_yaml` →
  `{yaml_top_level_keys, parses}`; `text_script` → `{shebang, interpreter}`. These are the honest
  analogue of SP1's `prim:FormalType` tower: a format is a poset of distinct component-species
  objects, and **no format shares another's species** (Rule 5: a Turtle triple is not a Markdown
  heading).
- **File-axis = physical/yang olog.** `file:Repository … file:File` is a BFO
  independent-continuant mereology; the OS bearers are the authored `fs_*` species with their real
  fields: `fs_regular {size_bytes, mime_type, mode_octal, line_count}`, `fs_dir {direct_children,
  mode_octal, owner_uid, group_gid, fhs_top_level}`, `fs_symlink {readlink_target,
  target_within_chroot}`, `fs_binary {size_bytes, mime_type, magic}`, `fs_device {device_kind,
  mode_octal}`, `fs_unreadable {mode_octal, owner_uid, reason, alarm_path}`. A `file:File`'s byte
  content **is realized as a `prim:Container`** — SP1's top carrier rung — and descends
  `prim:Container → Stream → Block → ByteVector → Octet → Bit` via `prim:byteDescendsTo`.
- **AtomCommon = the SP2 atom, reused verbatim.** Every fs_*/text_* atom composes `AtomCommon`
  (`atom_iri, atom_type ∈ {T1..T14}, source_path, source_sha256, qualified_name, emit_triples,
  parent_atom, traceback_to, co_owners, provenance ∈ {hand_authored_specimen, hand_edited_source,
  ba_jinja2_rendered}, rendered_by, rendered_at_utc`,
  `helios/00_src_specs/templates/atomic_mirror/schemas/_atom_common.avsc`). `source_sha256` is the
  content-addressed identity SP2/SP3 ground; `parent_atom` is the composition pointer.
- **ρ = parse/serialize = the realization monad (SP1's Frame monad, reused in shape).** Parsing a
  byte `prim:Container` into a typed format decomposition is a Kleisli arrow into
  `prim:Realization = Frame(frameOutput: decomposition, frameEffect: parse-loss / encoding-choice /
  ambiguity)`. Each **render leg** carries the concrete ρ selectors (from
  `triad_projection_validation.spec.yaml`): `leafFormat`, `pathnamePattern` (`*.ttl`, `*.sparql`,
  `*.linkml.yaml`), `parserSelector` (`rdflib.Graph.parse(format=turtle)` for ttl+shacl,
  `rdflib.plugins.sparql.prepareQuery` for sparql, `yaml.safe_load` for linkml), `syntaxAcceptance`
  (`rdf_turtle_parse_success`, `sparql_prepare_query_success`), and `textDecoding` (a `fmt:charset`
  point). Serialize is ρ's inverse; the mutual `prim:interpretAs` back-pointer (container → format)
  closes the colimit. **This file-level parse↔serialize colimit is the per-file seed of SP9's
  split↔consolidate render seal.**
- **`file:conformsTo` = a functor `File-axis → Format-axis`.** Each file maps to its format leaf; a
  file's component atoms must carry only component species admitted by that format's decomposition.

**Precisely which SP1 structures SP5 consumes** (grounds on, does not re-derive): `prim:Container`
+ the `prim:byteDescendsTo` ladder to `prim:Bit`; the towers `prim:Natural`/`prim:Ordinal` (fd,
inode, `size_bytes`, `triple_count`, `h2_count`, `line_count`, `mode_octal`, heading levels),
`prim:Bool` (`parses`, `has_context`, `target_within_chroot`), `prim:String`/`prim:Codepoint`
(text), `prim:Blob`/`prim:Hash` (`fs_binary.magic`, `source_sha256`),
`prim:Enumeration`/`prim:Categorical` (`mime_type`, `atom_type ∈ {T1..T14}`, the discriminator
leaves); the colimit-taiji + `prim:Realization` Frame-monad (`prim:frameOutput`/`prim:frameEffect`);
and the `prim:interpretAs` mutual-back-pointer discipline. **Deliberately NOT re-materialised**
(anti-decorative): SP1's literal Yoneda layer, `prim:RealizationTransport`,
`prim:AncestralGroundingPath` — SP5 inherits ρ's *discipline* (functor-on-arrows via `conformsTo`)
without rebuilding 59-object representables that no consumer needs this iteration.

## 3. File layout (STRICTNESS Rule 14 — one concern per file; SP1's honest ~8-file idiom)

Namespace idiom: `fmt: <urn:silmaril:fmt:#>`, `file: <urn:silmaril:file:#>`, consuming
`prim: <urn:silmaril:prim:#>` (SP1) and `atom:` (SP2). Each lifted class records its authored source
URN `urn:silmaril:entity#types.prelude.<name>` in an `rdfs:isDefinedBy`/provenance note (the lift is
a re-expression of authored YAML type-defs as TTL `owl:Class`es). Directory `basicttl/fileformat/`.

| file | responsibility |
|------|----------------|
| `basicttl/fileformat/format_progenitors.ttl` | The four/five discriminator progenitors + their explicit children, lifted from `srcy` appendix E prelude: `fmt:format` + 12 `format_*`, `fmt:charset` + 5, `fmt:comment_prefix` + 5, `fmt:byte_order` + 4, `fmt:impl` + 5; each child's `fmt:ancestryVia` edge to its umbrella; each `fmt:Format` a CCO ICE subtype; `charset_utf8` flagged canonical |
| `basicttl/fileformat/format_components.ttl` | Subatomic component species per text format (lifted from the `.avsc` per-format fields): `text_turtle→{triple_count,parses}`, `text_markdown→{h2_count,fenced_code_blocks}`, `text_json`, `text_yaml`, `text_script`; the cross-format species-disjointness (Turtle-triple ≠ Markdown-heading); each component leaf datatype `rdfs:subClassOf* prim:FormalType` |
| `basicttl/fileformat/file_axis.ttl` | File-axis: `Repository/FileTree/Directory/Module/File` BFO mereology + the authored `fs_*` filesystem-bearer species with their real fields; each `File`'s physical facet → `prim:Container`; `FileDescriptor`/`IndexNode` → `prim:Natural`; BFO declared, CCO used |
| `basicttl/fileformat/atom_common.ttl` | The `AtomCommon` composition (the shared T1..T14 atom envelope) lifted from `_atom_common.avsc`, wired as `rdfs:subClassOf atom:Atom` (SP2); the 14-type `atom_type` enum grounded in `prim:Categorical` |
| `basicttl/fileformat/render_legs.ttl` | The render legs declaring `leafFormat` + `pathnamePattern` + `parserSelector` + `syntaxAcceptance` + `textDecoding`, lifted from `triad_projection_validation.spec.yaml` (7-leg fibration: sh, ex, atlas.csv, ttl, shacl.ttl, sparql, linkml.yaml); the ρ parse/serialize Frame-monad shape + file-level colimit gluing + mutual `interpret_as`; SP9 seed |
| `basicttl/fileformat/fileformat.shapes.ttl` | SHACL law: progenitor-edge well-formedness, format-is-ICE, component-species disjointness (Rule 5), leaf-datatype-grounds-in-SP1, `fs_* ≠ text_*` disjointness, `AtomCommon` field presence (`source_sha256`), render-leg parser-selector presence, **`fmt:hasGlossary` seam presence**, file-colimit closure |
| `basicttl/fileformat/fileformat.queries.sparql` | EXPECT-TRUE ASK suite (§4), each with an inline DATA CONTRACT comment naming the triples that turn it green |
| `basicttl/fileformat/README.md` + `checks/run-fileformat-checks.sh` | the two taxonomies, consumers, how to re-run; runner mirrors SP1's `run-floor-checks.sh` (parse + pyshacl + depth gate + every ASK) |

## 4. Verification plan (evidence-first; every asserted law has a biting tooth)

Same discipline as SP1: each ASK is RED before authoring and GREEN after; each SHACL shape and each
positive ASK is **proven to bite by probe injection** (`conforms=True → False` / `True → False`);
positive ASKs return false on an empty graph (non-vacuous); the depth gate requires every `owl:Class`
to carry `rdfs:comment ≥ 200` chars (`scripts/ontology-depth-check.py`). Stack: rdflib + pyshacl over
the merged data graph with `primitives/*` loaded so SP1 grounding resolves. Value-type checks use
`sh:sparql`/`sh:in` (defang-proof against `inference="rdfs"`, per the SP1 lesson).

Named EXPECT-TRUE ASKs (litmus first):

- **`q_format_progenitor`** *(litmus — the lifted progenitor pattern)* — `fmt:format` is the agnostic
  umbrella (`ancestryVia → prelude node`), and **every** `format_*` leaf carries `fmt:ancestryVia
  fmt:format` (the lifted `{axis: domain, via: …prelude.format}` edge). *Probe:* drop a leaf's
  `ancestryVia`, or reparent it off `fmt:format` → false.
- **`q_format_children_complete`** — the 12 authored children are present and exactly
  `{avro,json,ex,hs,md,py,scala,sh,shacl,ttl,yaml,jsonld}`. *Probe:* remove one / add an unauthored
  one → false.
- **`q_charset_byteorder_comment_progenitors`** — the three sibling progenitors each carry their
  authored children (`charset`→5, `comment_prefix`→5, `byte_order`→4), `byte_order_none` occupies the
  agnostic slot, and `charset_utf8` is flagged canonical (`GLOBAL_FILE_ENCODING`). *Probe:* a child
  missing its `ancestryVia`, or a second `charset` marked canonical → false.
- **`q_format_is_ice`** — every `fmt:Format` (umbrella + leaves) is `rdfs:subClassOf*` a CCO
  Information Content Entity, resolved against `MergedAllCoreOntology.ttl` (CCO *used*, not just
  prefixed). *Probe:* a Format with no CCO ancestor → false.
- **`q_component_species_distinct`** *(the Rule-5 tooth)* — each text format's component species are
  disjoint from every other format's (`text_turtle`'s `triple_count` species ≠ `text_markdown`'s
  `h2_count` species); no component individual belongs to two formats' decompositions. *Probe:* type
  one component node under both Turtle and Markdown decompositions → `conforms=False`.
- **`q_fs_text_disjoint`** — the filesystem-bearer species `fs_*` (BFO continuants) are
  `owl:disjointWith` the text-format species `text_*` (ICE content) — the file/format cut is real, a
  directory-node is not a markdown-content atom. *Probe:* a node typed both `fs_regular` and
  `text_markdown` → `conforms=False`.
- **`q_atom_common_sha`** — every `T1..T14` atom composes `AtomCommon` and carries `source_sha256`
  (grounding in `prim:Hash`) + `atom_type ∈ {T1..T14}` (grounding in `prim:Categorical`) + a
  `parent_atom` slot. *Probe:* an atom missing `source_sha256` → false.
- **`q_leaf_grounds_sp1`** — every format-component and fs-field leaf datatype declares
  `rdfs:subClassOf* prim:FormalType` — no bare `xsd:` leaf (`size_bytes`→`prim:Natural`,
  `triple_count`→`prim:Natural`, `parses`→`prim:Bool`, `mode_octal`→`prim:Natural`,
  `source_sha256`→`prim:Hash`). *Probe:* a leaf whose datatype is bare `xsd:integer` → false.
- **`q_render_leg_parser`** — every render leg declares all of `{leafFormat, pathnamePattern,
  parserSelector, syntaxAcceptance, textDecoding}`; the ttl leg's `parserSelector` is
  `rdflib.Graph.parse(format=turtle)` with `pathnamePattern *.ttl`, the sparql leg
  `rdflib.plugins.sparql.prepareQuery` / `*.sparql`, the linkml leg `yaml.safe_load` /
  `*.linkml.yaml`. *Probe:* a leg missing `parserSelector` → false.
- **`q_file_container`** — every `file:File`'s physical facet resolves to `prim:Container`, which
  `prim:byteDescendsTo+ prim:Bit`; `file:FileDescriptor`/`file:IndexNode` ground in
  `prim:Natural`/`prim:Ordinal`. *Probe:* point a File's facet off `prim:Container`, or reground fd to
  bare `xsd:string` → false.
- **`q_file_axis_bfo`** — the `Repository…File` chain is a real BFO parthood mereology reaching a BFO
  independent-continuant root. *Probe:* cut a parthood edge → false.
- **`q_hasGlossary_seam`** *(the SP5→SP6 forward edge)* — every `fmt:Format` carries a
  `fmt:hasGlossary` edge whose range is the SP6 glossary class. The seam presence is **enforced now**;
  the glossary *content* is SP6's and its range class binding is `silm:isProvisional` until SP6 lands.
  *Probe:* a Format with no `fmt:hasGlossary` → false.
- **`q_file_colimit_roundtrip`** — the file-level taiji: a `file:File`'s `formatFacet` +
  `containerFacet`, glued by the parse `prim:Realization`, and the container's `interpret_as` returns
  the file's own `formatFacet` (render-seal reversibility seed). *Probe:* a wrong-facet file → false.

SHACL shapes mirror the universals (`FormatProgenitorShape`, `FormatIceShape`,
`ComponentSpeciesDisjointShape` carrying the Rule-5 disjointness, `FsTextDisjointShape`,
`AtomCommonShape`, `LeafGroundingShape`, `RenderLegShape`, `GlossarySeamShape`, `FileMereologyShape`,
`FileColimitShape`).

## 5. Interfaces & the exact Helios structures lifted

**LIFTED (authored source-of-truth → SP5 class), with `helios/` paths:**

- **Format/charset/comment/byte_order/impl progenitors** ←
  `helios/srcy/appendices/39_appendix_e_research_source_mirror/sections/specs/types/prelude/`:
  `format.spec.yaml.tex` (+ `format_{avro,json,ex,hs,md,py,scala,sh,shacl,ttl,yaml,jsonld}`),
  `charset.spec.yaml.tex` (+ `charset_{ascii,latin1,utf8,utf16be,utf16le}`),
  `comment_prefix.spec.yaml.tex` (+ `_{hash,double_dash,double_slash,percent,semicolon}`),
  `byte_order.spec.yaml.tex` (+ `_{little,big,host,none}`), `impl_{bash,beam,ghc,jvm,fastavro}` — the
  `entity.{urn,ancestry[axis/via],grounding,kind_urn}` + `triad_render` envelope.
- **The 14-type file/format atom taxonomy + AtomCommon composition** ←
  `helios/00_src_specs/templates/atomic_mirror/schemas/{_atom_common,fs_regular,fs_dir,fs_symlink,fs_binary,fs_device,fs_unreadable,text_turtle,text_markdown,text_json,text_yaml,text_script}.avsc`.
- **Render legs + parser_selectors** ← `helios/01_data_src_specs/triad_projection_validation.spec.yaml`
  (`parser_selectors: turtle→rdflib.Graph.parse(format=turtle); sparql→…prepareQuery; linkml→yaml.safe_load`;
  `pathname_patterns`, `syntax_acceptance`) and the 7-leg fibration in `triad_fibration.spec.yaml`.
- **Format/comment/impl/charset URN-ref discriminators + canonical encoding** ←
  `helios/00_src_specs/templates/_global_constants.j2` (`FORMAT_*`, `COMMENT_*`, `IMPL_*`,
  `GLOBAL_FILE_ENCODING_URN = charset_utf8`).
- **The render grammar mount/header/section/table/svg macros** (the target the format species feed) ←
  `helios/00_src_specs/templates/colimit/verb.<leg>.j2` (10 projection legs) +
  `_urn/identity.j2::universal_base` (header), `papers/_body/section_*.j2` (section),
  `_markdown/tables.j2` (table), `papers/_diagrams/**` (svg), `colimit/verb.*` (mount) — per
  `ledger/W2/helios/render_types_map.md` §2d (the HEEx `_spine` header/section/table/svg/mount is
  NOT in this zip slice; its functional equivalents are named here — Präriehund).

**Consumes** (from SP1 and lower sub-projects — named precisely):

- **SP1 (Primitive Floor):** `prim:Container` + `prim:byteDescendsTo` ladder to `prim:Bit`; towers
  `prim:Natural`, `prim:Ordinal`, `prim:Bool`, `prim:Enumeration`, `prim:Categorical`, `prim:String`,
  `prim:Codepoint`, `prim:Blob`, `prim:Hash`; the colimit-taiji + `prim:Realization` Frame-monad
  (`prim:frameOutput`/`prim:frameEffect`); the `prim:interpretAs` mutual-back-pointer; the
  `rdfs:subClassOf* prim:FormalType` dual-grounding litmus (reused for leaves).
- **SP2 (AOB meta-ontology):** the `atom:Atom` class — `AtomCommon` **is** the SP2 atom envelope
  (`atom_iri`/`source_sha256`/`parent_atom`/`provenance`/`rendered_by`), so file/format atoms inherit
  URN addressing + the tensor block rather than re-declaring them.
- **universal_anchors CCO/BFO (Layer-0):** `cco_grounding_iri` (`^cco:ont[0-9]{8}$`) for each
  `fmt:Format` node-type-def, resolved against `MergedAllCoreOntology.ttl` (CCO 2.x under BFO); BFO
  reached transitively through CCO. Referenced by IRI (`helios/01_data_src_specs/universal_anchors.spec.yaml`).
- **SP3 (S/O/P CRS)** *(lower ordinal; optional this iteration)* — file/format entities are
  URN-addressed coordinates that MAY be placed in the CRS (z from `source_sha256`). Deferred to W5 if
  SP3 is not available at build time.

**Produces** (for higher sub-projects — named precisely):

- **SP6 (glossary polysemy) — the `fmt:hasGlossary` seam. ONE forward edge:** SP5 declares
  `fmt:hasGlossary` on every `fmt:Format` and enforces its presence; **SP6 consumes it** and supplies
  the glossary class + the mole-of-glossaries content. Direction is now pinned (was the prior open
  question).
- **SP7 (SHACL executable law):** the format-is-ICE + component-species-disjointness (Rule 5) +
  fs≠text disjointness + leaf-grounds-in-SP1 + render-leg shapes are the file/format half of SP7's
  global law (SP7 extends, does not re-author).
- **SP8 (basicttl depth remediation):** the vocabulary SP8 uses to type real repo files — every
  `basicttl/*.ttl` is a `file:File` × `fmt:format_ttl`, every `docs/*.md` × `fmt:format_md`, etc.
- **SP9 (split↔consolidated render seal):** the file-tree graph (file-axis mereology) + subatomic
  component decomposition + the parse/serialize ρ colimit — the "complete owned syntax tree and
  physical file-tree graph" the unary law's render seal splits and consolidates.
- **W3 render pipelines:** each render leg (`leafFormat` + `parserSelector`) and each format's
  component species map to the `colimit/verb.<leg>.j2` / template macros — the target of the
  subatomic per-format renderers.

## 6. Non-goals + open questions (Präriehund — flagged, not invented)

**Non-goals (this iteration; YAGNI deferrals):**

- **No live-corpus binding, zero file instances** — pure shape + the authored format leaves + two
  fully-decomposed exemplars (Turtle, Markdown); real files bound in SP8/W5 (relaunch-safe).
- **No glossary mechanism** — the mole of glossaries, distinct epistemologies, synonym/antonym
  pairing, OSSIE-MIME arbiter are SP6; SP5 provides only the `fmt:hasGlossary` attachment seam.
- **No parse/serialize implementation** — SP5 authors the ρ colimit *shape* + declares the render
  legs' selectors; the runnable renderers/parsers are W3.
- **No literal-Yoneda re-materialisation** — inherited from SP1 as discipline, not rebuilt.
- **No CCO/BFO re-authoring** — SP5 references upstream CCO/BFO IRIs; it does not fork or vendor them.

**Genuine open questions for the maintainer (not force-fit):**

1. **The full `T1..T14` mapping.** The `.avsc` set concretely fixes only `text_turtle=T10` and
   `text_markdown=T12`; the other symbols (T1..T9, T11, T13, T14) are declared in the `AtomCommon`
   enum but the 11 authored `.avsc` files do not enumerate every one. SP5 lifts the 11 present species
   and marks the unmapped T-symbols `silm:isProvisional`. Is there an authored T1..T14 legend
   elsewhere to bind, or does SP5 leave the gaps provisional this iteration?
2. **CCO import vs IRI-reference, and BFO declaration.** The authored tree references CCO by opaque
   IRI (`cco:ont…`) with **no `owl:imports`**, resolving against `MergedAllCoreOntology.ttl`; BFO
   appears only transitively. Should SP5 `owl:imports` a pinned CCO release (which version — the specs
   say `SIL_CCO_VERSION = "2.x"`), or keep the IRI-reference idiom and pin exact opaque IRIs by hand?
3. **Is `impl` a fifth encoding-facet progenitor or a runtime/file-axis concern?** `impl_{bash,beam,
   ghc,jvm,fastavro}` is a sibling prelude discriminator, but it names a *runtime*, not a byte-layout
   facet like format/charset/byte_order. Lift it as a co-equal `fmt:` progenitor (as drafted), or hang
   it off the render leg (`triad_render.impl`) instead?
4. **What is a `Module`?** Between `Directory` and `File`: a `forge/` git submodule, a `pylib` Python
   package, or a semantically-grouped directory (or a *role* a `Directory` plays)? Affects whether the
   file-axis mereology has 5 rungs or 4, and whether `Repository`≠`FileTree` (versioned whole incl.
   `.git` vs working-tree projection).
