# W1 Task 3 — Taxonomy Census (every distinct taxonomy, whole trees)

Author: W1 census (Task 3). Frame date: `2026-08-07`. Scope: read-only census over the
five committed W1 maps + the seven frozen whole trees in `ledger/W1/trees/`.

Doctrine read in full first, per Global Constraint 1:
`docs/praeriehund-demokratie-der-kategorien.md` (129 lines) +
`docs/unary-byte-frame-law.md` (765 lines). Maintainer law honoured: *"FILE TREES ARE OUR
TAXONOMY"* — every cardinality below is **computed over the whole committed tree file**
(`wc -l` for total cardinality; `sed`/`cut`/`grep` over the entire file for structure),
never a capped or sampled read. Präriehund discipline: quotes are verbatim (`>` or fenced);
inferences are marked **[inference]**; genuinely-unresolvable unknowns are carried into the
Honest-gap register as **PROVISIONAL** with a documented gap and a resolution path; nothing
force-fit, nothing fabricated. Global Constraint 9 (capture, don't conclude): every row
carries a source citation; no axis is asserted without quoted evidence.

**Tree cardinalities (computed `wc -l` over the whole tree files, this session):**

| tree file | lines (= files) | verified |
|---|---:|---|
| `trees/silmaril.tree` | **6,333** | `wc -l` |
| `trees/basicttl.tree` | **30,234** | `wc -l` |
| `trees/base_agents.tree` | **279,670** | `wc -l` |
| `trees/base_templates.tree` | **1,118** | `wc -l` |
| `trees/base_tower.tree` | **50** | `wc -l` |
| `trees/example_gippidy_01.tree` | **16** | `wc -l` |
| `trees/superpowers.tree` | **180** | `wc -l` |
| **total (7 trees)** | **317,601** | `cat trees/*.tree | wc -l` |

The seven trees are a **partition** of the physical universe (task brief Step 2: repo root
excludes `basicttl/`, `forge/`, `external/`, each of which owns its own tree — every file
appears in exactly one tree). The census below is therefore an enumeration of the *distinct
taxonomies* that live inside that partition, some of which co-reside within one tree
(e.g. `base_agents` hosts at least four distinct taxonomies: its corpus file-tree, the
`.aob.dir` atom taxonomy, the `corpus/*.shacl.ttl` CorpusAtom taxonomy, and the `_specspec`
W3C taxonomy).

---

## Census rows

Each row: **root** · **what-it-is** (one honest sentence) · **ordered axes as evidenced** ·
**exact cardinality** (from trees/manifests) · **source-map citation**. Numbers marked
`[tree]` were computed by this agent over the whole committed tree file this session;
numbers marked `[map]` are quoted from a committed W1 map; `[manifest]` from a committed
manifest.

### Row 1 — Silmaril repo file-tree

- **Root:** `.` (the `silmaril` superproject working tree, partitioned to exclude
  `basicttl/`, `forge/`, `external/` — each its own tree).
- **What it is:** the top-level Silmaril repository file-tree — the live Python `sparky`
  engine plus its docs, ledger, ontology, keys, hooks and CI, minus the three submodule /
  corpus subtrees that own their own census rows.
- **Ordered axes (evidenced):** (1) top-level region —
  `scripts` **6,274** · `docs` **17** · `ledger` **16** · `ontology` **7** · `keys` **5** ·
  `hooks` **4** · `.github` **2** · 8 root files `[tree]`; (2) under `scripts/`, the
  `python/pylib` engine dominates (6,208 of 6,274) `[tree]`; (3) the `ontology/` leaf is a
  small standalone RDF taxonomy — `manifest.ttl, shapes.ttl, silmaril-consolidated.ttl,
  ui-shapes.ttl, queries.sparql, geosparql.sparql, README.md` `[tree]`.
- **Cardinality:** **6,333 files** `[tree]` = `wc -l trees/silmaril.tree`.
- **Source:** `trees/silmaril.tree`; `ledger/W1/sparky_substrate.md` (the engine census).

### Row 2 — Sparky / pylib substrate taxonomy

- **Root:** `scripts/python/pylib/` (inside the silmaril tree).
- **What it is:** the live unary-morphism engine — a PEP-420 namespace tree mirrored across
  three physical roots (PROCESS+APPLY+SLOTS under `src/silmaril/sparky`, VALUE under
  `config/constants`, DEPENDENCY under `config/gate/external`) plus a 719-file orphaned
  legacy `reference/` copy.
- **Ordered axes (evidenced):** (1) live vs legacy — `pylib/src` **5,259** files vs
  `pylib/reference` **719** files `[tree]` (map: *"719 `.py` files, 100% `.py` (matches the
  brief's '719-file LEGACY copy')"* sparky_substrate.md §2.1); (2) three-root mirror —
  `silmaril/sparky/` **2,277** files `[tree]` (map §1.1: *"2,277 `.py` files"*),
  `config/constants` 1,858 `[map]`, `config/gate/external` 1,124 `[map]`; (3) operation-leaf
  role axis — the 5 carrier files `input/output/effect/frame/value.py` + `apply.py` per leaf
  (map §1.2).
- **Cardinality:** `pylib` subtree **6,208 files** `[tree]` (`src` 5,259 + `reference` 719 +
  tests/other 230); `sparky/` **2,277** `[tree]` / `[map §1.1]`.
- **Source:** `ledger/W1/sparky_substrate.md`; `trees/silmaril.tree`.

### Row 3 — basicttl internal ontology taxonomy

- **Root:** `basicttl/`.
- **What it is:** a Turtle-serialized OWL/RDF/SHACL ontology corpus organized as a
  chapter-partitioned atom library — the `_verb/<NN_topic>/` chapters plus per-atom-type
  top-level `.ttl` shapes and a `dag/` sub-ontology.
- **Ordered axes (evidenced):** (1) serialization axis — **30,232 `.ttl`** + 1 `.sparql`
  + 1 `.md` `[tree]`; (2) chapter axis `_verb/<NN_topic>/` — **30,146** files across ~20
  named chapters, largest `11_base_commutative_diagram` **8,909**, `01_orientation` 4,044,
  `07_the_canonical_question` 2,791, … `08_visual_discipline` 114 `[tree]`; (3) atom-type
  axis — 83 top-level `.ttl` named by atom kind (`synonym_atom.ttl`, `translation_atom.ttl`,
  `shape_atom.ttl`, `replacement_atom.ttl`, `preferred_term_atom.ttl`, `typed_hom_triple.ttl`,
  …) `[tree]`; (4) the `dag/` sub-ontology — `dag_ontology.ttl, dag_instances.ttl,
  dag_shapes.ttl, dag_queries.sparql, README.md` `[tree]`.
- **Cardinality:** **30,234 files** `[tree]` = `wc -l trees/basicttl.tree`. (Cross-ref:
  corpus_v17.md §5.1 FINAL_VALIDATION counts **30,224** basicttl source files inside the v17
  package — a different snapshot/pin; the +10 delta is recorded in the Honest-gap register.)
- **Source:** `trees/basicttl.tree`; cross-referenced as a source corpus in
  `ledger/W1/corpus_v17.md` §5.1 (`source-corpus/basicttl`).

### Row 4 — base_agents corpus taxonomy

- **Root:** `forge/base_agents/` (pinned `d2b1217f`).
- **What it is:** the deep SHACL/OWL/RDF/SPARQL AOB research forge — two fused things (the
  `silmaril_wire` BEAM daemon + a shard-based research catalog mirroring external repos into
  AOB atoms), the BEAM twin of the Scala `cpg-highway` repo.
- **Ordered axes (evidenced):** (1) region axis `[tree]` — `research` **155,250** ·
  `r1_site` **100,352** · `corpus` **7,899** · `lib` **3,258** · `vendor` **2,907** ·
  `golden` **2,094** · `specs` **1,974** · `r1_staging` **1,300** · `config` **1,000** ·
  `.claude` 870 · `.workflows` 729 · `test` 628 · `scripts` 378 · … ; (2) three co-existing
  AOB representations (map §A: *"There are THREE co-existing AOB representations"*) — the
  `.aob.dir` dense-node (Row 9), the `corpus/*.shacl.ttl` CorpusAtom (Row 11), the
  `_specspec` spec-of-specs (Row 10); (3) four sorts `type|instance|value|process`
  (map §A.1).
- **Cardinality:** **279,670 files** `[tree]` = `wc -l trees/base_agents.tree` (map header:
  *"279,670 files"*).
- **Source:** `ledger/W1/base_agents.md`; `trees/base_agents.tree`.

### Row 5 — base_templates corpus taxonomy

- **Root:** `forge/base_templates/` (git submodule, pinned `eb3d916b`).
- **What it is:** the Jinja2 render-template forge that emits the AOB projection/emitter legs
  — "the registry owns the grammar, the assembler owns the layout, the leaf emits one bare
  term".
- **Ordered axes (evidenced):** (1) template-family axis `templates/<family>/` `[tree]` —
  `integration` **244** · `colimit` **214** · `_registries` **111** · `papers` **85** ·
  `atomic_mirror` **79** · `plugins` **77** · `heex` **58** · `sql` **54** · `fp_triad` **39**
  · `_migration` 19 · `unix`/`ducklake` 16 · `corpus_kg` 14 · … (map §2 file-count table);
  (2) language-lane axis inside `integration/macros/` — `bash` 95 · `ex` 32 · `python` 30 ·
  `haskell` 30 · `scala` 27 · `heex` 14 · `liveview` 4 (map §2); (3) render-suffix axis —
  **1,087 `.j2`** templates `[tree]` + 1 binary (`erl_crash.dump`) + logs/iml/LICENSE.
- **Cardinality:** **1,118 files** `[tree]` = `wc -l trees/base_templates.tree` =
  `[manifest]` `ledger/W1/manifests/base_templates.manifest` (1,118 lines, `COVERAGE EXACT`)
  = `[map]` base_templates.md §1 (*"1118 files"*).
- **Source:** `ledger/W1/base_templates.md`; `trees/base_templates.tree`;
  `ledger/W1/manifests/base_templates.manifest`.

### Row 6 — base tower (forge/base) corpus taxonomy

- **Root:** `forge/base/` (git submodule, pinned `c4e828188a57d7a93c4f4972859dd0862ae6cce6`).
- **What it is:** a thin structural "turtle-tower" repo — a seven-child submodule tower plus
  one category-theory foundations corpus (`docs/mythology/silmaril/foundations/`: the papers
  I/II/IV/V, `AGENT.md`, and ten `skills/**/*.md`).
- **Ordered axes (evidenced):** (1) payload axis — (i) submodule tower (Row 13) vs
  (ii) foundations corpus (map §1: *"two payloads only"*); (2) foundations document axis —
  bundle numbered **I, II, IV, V** (map §4: *"there is no `III-*` document"*), each a
  `.pdf`+`.tex` pair; (3) skills axis — `skills/**/*.md` = ten skill files across
  `core`(3) `effects` `federate` `forge` `games` `observe` `optics` `provenance` (map §4.7).
- **Cardinality:** **50 files** `[tree]` = `wc -l trees/base_tower.tree` = `[manifest]`
  `ledger/W1/manifests/base_tower.manifest` (50 lines, `COVERAGE EXACT`) = `[map]`
  base_foundations.md §1.
- **Source:** `ledger/W1/base_foundations.md`; `trees/base_tower.tree`;
  `ledger/W1/manifests/base_tower.manifest`.

### Row 7 — example_gippidy_01 corpus taxonomy (v17 transport package)

- **Root:** `forge/example_gippidy_01/` (git-cloned; `.git` is a gitlink file).
- **What it is:** the transport package for the materialized GraphAtlas-epistemic0 v17 corpus
  — a README + `.git` + **14 split-ZIP slices** in two parallel build families (consolidated
  + semantic-formats), each 6 numbered parts + 1 control archive.
- **Ordered axes (evidenced):** (1) build-family axis — `consolidated-v17` (7 zips:
  control + part-001…006) vs `semantic-formats-v17` (7 zips) `[tree]`; (2) slice-ordinal axis
  — `part-00N-of-006` for N∈1..6 per family `[tree]` (map §1: *"12 split ZIP slices (two
  families × 6 numbered parts) plus two `-control.zip`"*).
- **Cardinality:** **16 files** `[tree]` = `wc -l trees/example_gippidy_01.tree` (README +
  `.git` + 14 zips). The *reassembled* corpus it carries is Row 12 (104,848 identities); this
  row is the on-disk transport artifact, not the projection plane.
- **Source:** `trees/example_gippidy_01.tree`; `ledger/W1/corpus_v17.md` §1–2.

### Row 8 — superpowers skill taxonomy

- **Root:** `external/skills/superpowers/`.
- **What it is:** the Obra "superpowers" skill/plugin corpus — a flat one-level skill library
  (`skills/<skill-name>/SKILL.md`) plus multi-harness plugin manifests, hooks, docs, and a
  test suite.
- **Ordered axes (evidenced):** (1) skill axis — **14** skills each with a `SKILL.md`
  `[tree]` (`grep -c 'skills/[^/]*/SKILL.md'`): `brainstorming, dispatching-parallel-agents,
  executing-plans, finishing-a-development-branch, receiving-code-review,
  requesting-code-review, subagent-driven-development, systematic-debugging,
  test-driven-development, using-git-worktrees, using-superpowers,
  verification-before-completion, writing-plans, writing-skills`; (2) harness-plugin axis —
  `.claude-plugin` `.codex-plugin` `.cursor-plugin` `.kimi-plugin` `.pi` `.opencode`
  `.agents/plugins` marketplace/plugin manifests `[tree]`; (3) region axis — `skills/`,
  `tests/`, `docs/`, `hooks/`, `scripts/`, `assets/` `[tree]`.
- **Cardinality:** **180 files** `[tree]` = `wc -l trees/superpowers.tree`; **14** skill
  directories `[tree]`.
- **Source:** `trees/superpowers.tree`.

### Row 9 — AOB `.aob.dir` dense-node taxonomy (inside base_agents golden)

- **Root:** `forge/base_agents/golden/specs/` (repo-wide `.aob.dir` also under
  `r1_site/`, `r1_staging/`, `_spark/`, `_specspec/`).
- **What it is:** the canonical AOB atom — every atom is a **directory** `<leaf>.aob.dir/`
  holding a base `<leaf>.spec.yaml` dense node + ≥2 `*.claim.spec.yaml` claim plugins (group
  law: identity=base, op=compose) + an `_aob/` sealed witness triad/sextet
  (identity/relation/inbound/outbound/lineage/dewey).
- **Ordered axes (evidenced):** (1) golden path axis — *"Golden path rule:
  `golden/specs/<dewey_path>.aob.dir`"* (map §A.1), exemplar
  `golden/specs/instance/artifact/ast/sha256/<sha256>.aob.dir/`; (2) sort axis — `kind:` one
  of `type|instance|value|process` (map §A.1); (3) the 21-column Atlas ring × N glossaries
  (see Axes); (4) FORM-3 curried relation axis `subject@predicate@object` with the is:a spine
  to `urn:silmaril:type:type` (see Axes).
- **Cardinality:** **golden `.aob.dir` atom-directories = 217** `[tree]`
  (`grep -oE 'golden/.*\.aob\.dir' | sort -u | wc -l`), spanning **2,094 golden files**
  `[tree]`/`[map §0]`; **repo-wide distinct `.aob.dir` = 458** `[tree]` (+ `.aob.dir.staged`
  staged atoms). **[inference]** the map's prose "2,094 sealed atoms" (§0 table) counts the
  golden *file* total, not the atom-*directory* count; the computed atom-directory count is
  217. Golden audits are RED: `_audit_sparql.yml` VERDICT **FAIL** (`isa_reaching_type_type
  201/208`, 7 broken spines); `_audit_contract.yml` 168/171 pass (map §D.7).
- **Source:** `ledger/W1/base_agents.md` §A.1, §D.7; `trees/base_agents.tree`.

### Row 10 — `_specspec` W3C spec-of-specs taxonomy

- **Root:** `forge/base_agents/r1_staging/forge/_specspec/`.
- **What it is:** an olog-of-ologs — the W3C standards (SPARQL 1.1, OWL 2, RDF 1.1
  Semantics, Turtle) themselves catalogued as AOB tickets, one per chapter / section /
  grammar-production / example / algebra-rule, `PATH IS THE HIERARCHY` rooted at
  `urn:silmaril:type:type`.
- **Ordered axes (evidenced):** (1) spec-family axis with per-family ticket cardinality
  `[tree]` (`grep -cE '_specspec/<fam>/tickets/.*\.yaml$'`): **sparql 267 · rdf 126 ·
  turtle 110 · owl 18** — byte-for-byte the map's `coverage_report.json` (map §A.3:
  *"sparql 267 nodes, rdf 126, turtle 110, owl 18"*); (2) ticket-kind axis — `kind:` ∈
  `{grammar_production, section, chapter, artifact, algebra}` (map §A.3); (3) containment
  chain axis rooted at `urn:silmaril:type:type` (map §A.3).
- **Cardinality:** **521 catalog tickets** (267+126+110+18) `[tree]`; **526** total
  `_specspec/` files `[tree]` (tickets + staging + coverage_report). Coverage state
  (map §A.3): *"stamped 16, gate_passed 11, dense_complete 11, … gaps_count 84"* — RED/WIP.
- **Source:** `ledger/W1/base_agents.md` §A.3, §H; `trees/base_agents.tree`.

### Row 11 — corpus SHACL CorpusAtom taxonomy

- **Root:** `forge/base_agents/corpus/`.
- **What it is:** the machine-emitted RDF/Turtle projection — each external source repo (or
  encyclopedia/tier/pin slice) is one `corpus:CorpusAtom` auto-rendered by
  `ResearchRender.Render.ShaclRenderer`, declaring a `signatureInput` typed-value set, a
  21+ `atlasColumn` ring, an emitter fan-out, and `ValueNode`s that `corpus:memberOf` the
  atom.
- **Ordered axes (evidenced):** (1) atom axis — **1,477 `*.shacl.ttl`** CorpusAtoms `[tree]`
  (`grep -cE 'corpus/[^/]*\.shacl\.ttl$'`; map §A: *"1,477 SHACL files"*), 1,478 total `.ttl`
  `[tree]`; (2) emitter-leg axis (the projection family) — each atom fans to a fixed leg set:
  **`.shacl.ttl` 1,477 · `.sh` 1,477 · `.linkml.yaml` 1,477 · `.ex` 1,477 · `.atlas.csv`
  1,477**, plus partial FP-triad completion **`.scala` 5 · `.hs` 5** `[tree]` (map §A.2/§F:
  *"emitter set = the projection family: `.sh .ex .scala .hs .atlas.csv .linkml.yaml
  .shacl.ttl`"*); (3) `corpus:ValueNode` membership axis (each `valueName`+`specPath` back to
  an `r1_site` AOB) (map §A.2).
- **Cardinality:** **1,477 CorpusAtoms** `[tree]`; corpus region **7,899 files** `[tree]`.
- **Source:** `ledger/W1/base_agents.md` §A.2, §F; `trees/base_agents.tree`.

### Row 12 — v17 gippidy projection-family taxonomy (the materialized epistemic0 corpus)

- **Root:** the reassembled corpus carried by `forge/example_gippidy_01/` — root dir
  `graphatlas-epistemic0-consolidated-v17-2026-08-06/`.
- **What it is:** the materialized GraphAtlas-epistemic0 v17 projection plane — one canonical
  carrier per identity fanned out across a fixed lens family (ttl, geosparql, shacl, linkml,
  ossie, xml, sparql, metadata, exports, native-runners) over a 16-axis Atlas glossary ring.
- **Ordered axes (evidenced):** (1) canonical-identity axis — **104,848** identities `[map]`
  (corpus_v17.md §5.1: sqlite `count(*)=104848`, cross-agreeing across AXIS_COVERAGE /
  PACKAGE_SUMMARY / epistemic0.yaml / terms/index.yaml); (2) 16 named Atlas Glossary axes
  (see Axes) with per-axis primary counts summing to 104,848 (§5.1); (3) 3-coordinate CRS
  (lexical-depth / operator-degree / digest-ordinal — see Axes); (4) projection-lens axis
  (12-family `nativeProjectionFamily` — see Projection families); (5) rebinding axis —
  **1,677,568** all-axis CRS rebindings = 104,848 × 16 `[map]` §5.1.
- **Cardinality:** **104,848 canonical identities**; **16 axes**; **1,677,568 rebindings**;
  **29,365,945** all-turtle statements; **4,279,572** validated ttl triples; materialized
  tree = **509 members** (consolidated) / 476 (semantic-formats) `[map]` (corpus_v17.md
  §3, §5.1, §8).
- **Source:** `ledger/W1/corpus_v17.md` §3–8.

### Row 13 — base tower submodule-graph taxonomy

- **Root:** `forge/base/` `.gitmodules` + index gitlinks (the tower's DAG, not its files).
- **What it is:** the physical submodule dependency graph of the `forge/base` turtle-tower —
  a seven-child L2 tower under `groenewt/*`, two of whose children (`agents`, and the
  crossed `sbin`) carry their own L3 sub-submodules, with two upstream repos mounted twice.
- **Ordered axes (evidenced):** (1) nesting-level axis — L1 `forge/base` → 7×L2
  (`external, forge/agents, forge/bin, forge/core, forge/docs, forge/specs, forge/templates`)
  → 3×L3 under agents (`core, docs, sbin`) `[map]` (base_foundations.md §2.1–2.3); (2)
  gitlink-pointer axis — **10 `.git` gitlink files** `[tree]`
  (`grep -c '/\.git$' base_tower.tree`) physically encoding tower depth; (3) URL-cycle axis —
  `groenewt/core` mounted at `forge/core` **and** `forge/agents/core` (both @`3f90564c`);
  `groenewt/base_bin` mounted at `forge/bin` **and** `forge/agents/sbin` (both @`6525c556`)
  (map §2.6).
- **Cardinality:** **10 index gitlinks** = 7 L2 + 3 L3 (incl. sbin) `[map §2.3]`, distinct
  from the **10 on-disk `.git` pointers** = base L1 + 7 L2 + 2 initialized L3 (sbin
  uninitialized) `[tree]` — two decompositions that coincidentally both total 10; **2**
  `.gitmodules` declaration files (7-entry + 3-entry) `[map §2.2]`; the whole tower = 50
  files (Row 6).
- **Source:** `ledger/W1/base_foundations.md` §2; `trees/base_tower.tree`.

---

## Axes

The axis *systems* found across the maps and trees, with verbatim evidence per axis claim.
No axis is asserted without a quoted source.

### A1 — v17 three-coordinate CRS (lexical-depth / operator-degree / digest-ordinal)

Verbatim (corpus_v17.md §5.1, identical in `metadata/crs-bindings.yaml`,
`atlas-glossaries.yaml`, `linkml/instance-index.yaml`; all 16 CRSs share these 3 axes):
> - axis 0 **lexical-depth** — "count of lexical/path segments in exact URN" (unit segment-count)
> - axis 1 **operator-degree** — "maximum N-grade among `:`, `#`, `@`, `;`, `!`" (unit maximum-glyph-run)
> - axis 2 **digest-ordinal** — "first two source-digest octets interpreted as an integer" (unit unsigned-16-bit)

Confirmed by brute-force over all 104,848 sqlite rows, **0 mismatches** (§5.2); x collapses
consecutive delimiters, z is the source/identity digest not a fresh digest of the URN.

### A2 — v17 sixteen named Atlas Glossary axes

Verbatim per-axis primary counts (corpus_v17.md §5.1, epistemic0.yaml `primaryAxisCount:15`,
general-ontology = universal cover only):
> urn-calculus **62,160**, document-corpus 24,281, software-languages 7,296,
> graphatlas-runtime 5,779, schema-validation 2,470, biological-taxonomy 1,256,
> storage-formats 616, hardware-compute 431, predictive-world-model 275, icarus-ide 96,
> identity-security 75, execution-effects 42, distributed-network 37, geospatial-topology 23,
> economics-game-theory 11, general-ontology 0.

`namedAxisCount: 16`, `glossaryCount:16`, `primaryAxisCount:15` (§5.1). Sum of primaries =
104,848.

### A3 — AOB 21-column Atlas glossary ring (the Yoneda sheaf)

Verbatim 21 columns (base_agents.md §C, `atlas_columns` enum tails):
> GlossaryName, TermName, ShortDescription, LongDescription, Examples, Abbreviation, Usage,
> AdditionalAttributes, TranslationTerms, ValidValuesFor, Synonyms, ReplacedBy, ValidValues,
> ReplacementTerms, SeeAlso, TranslatedTerms, IsA, **Antonyms**, Classifies,
> PreferredToTerms, PreferredTerms.

Projected across N DISTINCT GlossaryNames — the pyramid **dimensional** facet requires
*"≥4 DISTINCT GlossaryName dimensions … A collapsed single-glossary set = FAIL"* (§A.4). The
exemplar's 5 glossaries: `silmariltypeontology · silmarilidentity · silmarilheritage ·
silmarilsemantics · silmarilmeasure` (§C). base_templates.md §3.6 confirms this same 21-name
list byte-identical (names + order) as `atlas_glossary_columns` in
`_registries/semantic_render_target.j2`.

### A4 — AOB four sorts

Verbatim (base_agents.md §A.1): `kind:` is *"one of 4 sorts: type|instance|value|process"*,
spine progenitor `urn:silmaril:type:type`.

### A5 — AOB is:a progenitor spine (FORM-3 curried relations)

Verbatim (base_agents.md §A.1): *"The **is:a ladder** must reach the progenitor
`urn:silmaril:type:type` with **NO jumps**; the terminal rung carries a bang `!`
(`…@is:a@type:type!`)"*. Relations are curried `relation_urn: …:relation:<s>@<p>@<o>` with
clean flat `subject/predicate/object_urn` — *"A flat triple is a 'rank-0 reduction' of the
curried form"*. Same S·O·P towers as the unary law and the v17 `relation_urn` MAP
(corpus_v17.md §6.2) whose rank-zero REDUCE is `(identityUrn, denotes, lexeme(h))`.

### A6 — Dewey taxonomy plane (library/volume/book/chapter/section)

Verbatim (base_agents.md §A.1 `dewey:` block): *"dewey_path, file_locus, library, volume,
book, membership:[{axis: …:relation:member:of, via: <parent>}]"*. base_templates.md §3.5
realizes it: *"The on-disk path is the denormalized URN walk: dots and underscores become
path separators, and the final segment becomes the filename"* (`_canon/
dewey_template_contract.j2`), golden path rule `golden/specs/<dewey_path>.aob.dir`.

### A7 — five-facet pyramid enrichment axis

Verbatim (base_agents.md §A.4, `forge-speclangs-pyramid-enrich.js`): the five disjoint facet
micro-partitions **algebraic · cardinality · dimensional · projection · grounding**, each a
`<staged_dir>/_pyramid/<key>.facet.yml`.

### A8 — tensor three-axis byte-substrate (space / time / value)

Verbatim (base_agents.md §B.2, `r1_site` per-field `tensor` block; mirrored in
base_templates.md §3.7 `_tensor/{render,space,time,value}.j2`):
```yaml
tensor:
  space:  {cardinality: CardinalityOne, dimensions: 1, bounded: true, max_size: 128, bit_width: 8, byte_width: 1, alignment: 1}
  time:   {dynamics: DynamicsSnapshot, ordering: OrderingPositional, monotonic: true, lifetime: LifetimeImmutable, byte_order: ByteOrderNone, arithmetic: ArithmeticNone}
  value:  {interpret_as: InterpretAsAscii, domain: {kind: DomainKindEnum}}
```
The unary-law `1..128` bit-width bound appears literally (`max_size: 128`, `bit_width: 8`) —
the on-disk mirror of the law's Byte-Stream Carrier Closure.

### A9 — basicttl chapter axis (`_verb/<NN_topic>/`)

Computed `[tree]` over `trees/basicttl.tree` (`grep '^basicttl/_verb/' | cut -d/ -f3 | sort |
uniq -c`): the `_verb/` directory partitions **30,146** files across ~20 numbered chapters —
`11_base_commutative_diagram` 8,909 · `01_orientation` 4,044 · `07_the_canonical_question`
2,791 · `09_minimal_category_theory` 2,442 · `04_forge` 2,028 · `02_music` 1,921 · …
`08_visual_discipline` 114. (No W1 map narrates basicttl's internal structure; this axis is
computed from the frozen tree — see Honest-gap register.)

### A10 — semantic_render_target 25-column render contract

Verbatim (base_templates.md §3.6, `_registries/semantic_render_target.j2
::semantic_render_target_columns`, 25):
> schema_version, entity_urn, source_urn, render_target, graph_module, lambda_contract,
> topology_contract, effect_monad, semantic_subject, semantic_predicate, semantic_object,
> verb, adverb, adjective, relation_type, evidence_locus, input_path, input_sha256,
> input_bytes, output_path, output_sha256, output_bytes, artifact_hash, row_status,
> trust_scope

with `required_semantic_render_fields` (17) and `full_atlas_proof_columns` = 25+21 = 46. The
`semantic_subject/predicate/object` triple is the same S·P·O family as A5.

### A11 — superpowers skill axis (flat, 14)

Computed `[tree]` (`grep -c 'skills/[^/]*/SKILL.md' superpowers.tree` = 14): a single-level
skill library — 14 `skills/<name>/SKILL.md`, no nesting. (Observation from the tree; the
skill *contents* are not narrated by any W1 map.)

### A12 — base tower nesting-level + URL-cycle axes

Verbatim (base_foundations.md §2.1 gitlink pointers): L1 `forge/base` → L2 (7 children) →
L3 (`core/docs/sbin` under agents). URL-cycle (§2.6): *"`groenewt/core` is mounted as
`forge/base:forge/core` **and** as `forge/base/forge/agents:core`, both @ `3f90564c`"*;
*"`groenewt/base_bin` … `forge/bin` **and** … `forge/agents/sbin`, both @ `6525c556`"*.

---

## Projection families

Every materialization / emitter family found across the maps, each with its source citation.

### PF1 — v17 11-target `materialized:as` packet family (the URN slug)

Verbatim (corpus_v17.md §7.1, the `relation_urn` `materialized:as` slug embeds **11** legs):
> `self-shacl-linkml-ossie-geosparql-sparql-xml-uml-dot-graphml-native`

Honest discrepancy recorded by the map: *"the URN slug **omits `ttl`**"* — ttl is folded
under the RDF-carrying legs. Source: corpus_v17.md §7.1, §6.2.

### PF2 — v17 12-family `nativeProjectionFamily`

Verbatim (corpus_v17.md §7.1, `epistemic0/epistemic0.yaml`):
> **self, shacl, linkml, ossie, geosparql, sparql, ttl, xml, uml, dot, graphml, native**

Each is a catamorphism `π_L = cata(α_L): Self → L` with a partial retraction `ρ_L: L ⇀ Self`
(§6.4); every projection receipt assigns one of five loss classes
`exact / structural / approximated / externalized / dropped`. Source: corpus_v17.md §7.1, §6.4.

### PF3 — v17 10-lens strict-all-AOB paper contract

Verbatim (corpus_v17.md §6.1, `P : A → ∏_{L∈L} Artifact_L`, lenses):
> L = {self, SHACL, LinkML, Ossie, GeoSPARQL, SPARQL, UML, DOT, GraphML, native-acceptance}

The manifest gate *"rejects any atom for which P(a) is partial"* (total-function coverage
over all 104,848 identities). Source: corpus_v17.md §6.1. **[Recorded]** PF1 (11, no ttl),
PF2 (12, with ttl), PF3 (10) are three consistent-but-non-identical enumerations, held
verbatim, not reconciled by fiat (map §9).

### PF4 — base_agents CorpusAtom emitter fan-out (the OSI colimit of representations)

Verbatim (base_agents.md §F): one `CorpusAtom`/AOB → a fixed emitter fan-out —
> `*.sh` (bash) · `*.ex` (Elixir) · `*.scala` · `*.hs` (Haskell) — the FP-triad + Ba code
> twins; `*.atlas.csv` — 21-col Apache Atlas ring; `*.linkml.yaml` — LinkML; `*.shacl.ttl` —
> SHACL/RDF; `*.osi.yaml` — OSSIE semantic-model (YIN)

with cross-leg functional consensus (the Set-0 gate: *"input X → every leg → same Y hash"*).
**Computed leg cardinality `[tree]`** over `corpus/`: `.shacl.ttl` 1,477 · `.sh` 1,477 ·
`.linkml.yaml` 1,477 · `.ex` 1,477 · `.atlas.csv` 1,477 (5 full legs) + `.scala` 5 · `.hs` 5
(partial FP-triad completion). Source: base_agents.md §F; `trees/base_agents.tree`.

### PF5 — base_templates render-target family

Verbatim (base_templates.md §Orientation): the corpus emits the projection legs
> `.sh / .ex / .scala / .hs / .atlas.csv / .linkml.yaml / .shacl.ttl / .sparql / .ttl / .sql`

`base_templates` is the RENDER side of the machinery whose ATOM side is `base_agents`
(1,087 `.j2` templates `[tree]`). GROUND LAW VIII: *"a render is LIVE CODE — graded on
EXECUTION, not presence"*. Source: base_templates.md §Orientation, §4.

### PF6 — v17 two-build deterministic materialization (consolidated vs semantic-formats)

Verbatim (corpus_v17.md §3): two full parallel builds over the same 104,848 identities —
*"433 shared paths, of which 431 are byte-identical sha256; the only 2 differing shared files
are `TREE.txt` and `PACKAGE_SUMMARY.yaml`"* — strong evidence of deterministic, reproducible
materialization. Distribution-level split↔consolidated transport: 14 split-ZIP slices →
`.tar.zst` payload → directory tree, gated by a chain of content-addressed digests (§7.3).
Source: corpus_v17.md §3, §7.3.

### PF7 — AOB `.d/` atomic-mirror + eigenstate matrix (base_templates)

Verbatim (base_templates.md §4 `atomic_mirror/`): every source file gets a sibling `.d/`
tree — *"the 9-cell `{forge,unix,joy}×{bit,byte,word}` matrix, three eigenstates
`expected=matter / unexpected=anti-matter / unknown=γ|unknown⟩` each ≥3 entries"*; the
γ-unknown MUST propagate to Dunbar layer 0 (`alarm_path: Dunbar-immediate`). Source:
base_templates.md §4 (`atomic_mirror/`, 79 files `[tree]`).

---

## Version-skew register

Every same-repo-different-pin / crossed-record fact, with exact SHAs. All pins verified
read-only this session (`git -C <path> rev-parse HEAD`) where the working tree is present.

### VS1 — forge/base base pin (authoritative)

- **`forge/base` @ `c4e828188a57d7a93c4f4972859dd0862ae6cce6`** — verified live this session:
  `git -C forge/base rev-parse HEAD` = `c4e82818…`.
- The dispatch brief's asserted `9e60c103e3f6a41cc78e6dee40aeeded133e2eb9` **does not exist
  in the repo** (base_foundations.md §1/§2.4/§7: *"`git cat-file -t` fails … 'Not a valid
  commit name'"*). The live pin `c4e82818` governs. HEAD subject: `c4e8281 agents cleaner`.
- Source: base_foundations.md §1; live `git rev-parse`.

### VS2 — same taxonomy at two pins (tower child vs silmaril sibling clone)

The `silmaril` superproject mounts the same two taxonomies twice, at two co-existing commits
(base_foundations.md §2.5, all verified live):

| taxonomy | pin inside `forge/base` (tower) | pin as silmaril sibling clone |
|---|---|---|
| `base_agents` | `forge/base:forge/agents` @ **`672ba868`** (`672ba868d768c47f6d5cd616b54a06a080fb26cb`) | `silmaril:forge/base_agents` @ **`d2b1217f`** (`d2b1217ffb9b48303bb6743ef4a535e3e01a7a2d`) |
| `base_templates` | `forge/base:forge/templates` @ **`2d84826c`** (`2d84826c6db49771f64e6bbc39c32af3f6ae278c`) | `silmaril:forge/base_templates` @ **`eb3d916b`** (`eb3d916b0db5c1429e0ce5abaac7b6b75aadea18`) |

Verified this session: `git -C forge/base_agents rev-parse HEAD` = `d2b1217f…`;
`git -C forge/base_templates rev-parse HEAD` = `eb3d916b…`. The sibling pins are the targets
of `ledger/W1/base_agents.md` (`d2b1217f`) and Task 1 / base_templates.md (`eb3d916b`).
Source: base_foundations.md §2.5.

### VS3 — the `sbin`/`bin` crossed gitlink defect

Inside `forge/base/forge/agents` (base_foundations.md §2.4):
- `.gitmodules` maps a submodule pathed **`bin`** → `groenewt/base_bin`, but **the index
  carries no gitlink at path `bin`** (mapping-without-gitlink).
- The index carries a gitlink at path **`sbin` @ `6525c556`** (`6525c5569d70deb7ee1391ecd5b
  236ab3813336a`), but **`.gitmodules` has no mapping for `sbin`** (gitlink-without-mapping,
  no URL).
- `sbin`'s pin `6525c556` **equals** `base_bin`'s pin, so the *content* is capturable via
  `forge/base/forge/bin` at the identical SHA; the `sbin/` mount is empty (0 files). Head
  commit `d6bd3f7` documents the intent: *"forge/sbin-> forge/bin (super bin used in
  forge/**/sbin/**)"*.
- Source: base_foundations.md §2.4, §2.6.

### VS4 — L3 shared-mount pins (URL cycle)

Two upstream repos mounted twice at identical pins (base_foundations.md §2.3, §2.6):
- **`groenewt/core` @ `3f90564c`** (`3f90564c97c6b38f6c59616073957e15eedaae6e`) — mounted as
  `forge/base:forge/core` **and** `forge/base/forge/agents:core` (L3). READMEs byte-identical.
- **`groenewt/base_bin` @ `6525c556`** — mounted as `forge/bin` **and** `forge/agents/sbin`.
- L3 agents `docs` @ **`661af74e`** (`661af74ea3979c94a9c0b823ac318b9d8203c5f7`) →
  `groenewt/base_agents_docs`.
- Other L2 pins (all match brief, §2.3): `external` @ `90af0bad9bc150c67b996745f0e76865f9e1
  e4f8`; `forge/docs` @ `1cf127f6280edd8b59ab88643043c8b3c02ecc7d`; `forge/specs` @
  `469bb24fdc5e0ddcf621cf7ce497aa4c37d33c34`.
- Source: base_foundations.md §2.3, §2.6.

### VS5 — base_templates transient HEAD (resolved)

base_templates.md §7: fragment 026 transiently observed
`git rev-parse HEAD = a4e66a065659d2d355f065bbd8cded6aa2fc1430` during its run; re-verified
at synthesis time to `eb3d916b…` (the pin), and all 1,118 `sha256/bytes` manifest pairs are
byte-verified against the current tree. Recorded as a resolved transient, not a live skew.

### VS6 — license skew across the tower (recorded, not editorialized)

base_foundations.md §2.8: six LICENSE files, three distinct licenses — **GPLv2** (base, bin,
docs, specs; four byte-identical `8177f975…`), **Apache 2.0** (agents only; `c71d239d…`),
**BSD 3-Clause** (templates; `6de269db…`, filled `Copyright (c) 2026, Tristan Groenewold`) —
while the foundations prose and the Präriehund doctrine footer both commit to Apache 2.0
(base_templates.md §1 also flags BSD-3 vs the doctrine's `Apache 2.0`). Recorded as found.

---

## Honest-gap register

Every PROVISIONAL carried forward from the five maps, plus census-level unknowns. Each gap
carries its documented nature and what would resolve it (Präriehund: name the gap, do not
force-fit). PROVISIONAL is used only for genuinely-unresolvable unknowns, never to dodge
resolvable work.

### From `sparky_substrate.md` §5

1. **Continuation docs absent** — `docs/unary-byte-frame-law-enforcement-proof.md` and
   `…-receipts.md` are named in the index topology but do **not exist** on disk (§0, §5.1).
   All §4 census numbers rest on the single index doc. *Resolve:* locate the continuations
   in another checkout, or confirm they were planned-not-written.
2. **Pickle de-mux count 5 vs brief 3** — 5 two-load de-mux processes observed, brief said 3
   (§1.4). *Resolve:* reconcile whether the brief counts one family (equality vs mutation).
3. **`sparky/lambda/` keyword twin reachability** — 10-file Python-invalid `lambda/` vs the
   lawful 7-file `lambda_/`; live-reachable via importlib or orphaned dead weight unresolved
   (§1.4). *Resolve:* importlib reachability probe + byte-complete inverse before retire.
4. **sbt Scala engine not in tree** — `ci.sh` targets an sbt engine (`modules/`, `build.sbt`,
   `cli/`) with no such directory in this checkout (§3.4 note, §5.4). *Resolve:* confirm the
   engine lives in the `cpg-highway` twin / a sibling repo.
5. **reference `aob/layout` hyphenated projection constants** —
   `daedalus/icarus/ossie/yggdrasil-projection` meaning unresolved, no live analogue (§2.4,
   §5.5). *Resolve:* trace to a live `sparky` morphism or confirm orphaned legacy.
6. **"~100% unary-conformant" scope** — the figure is the pass state of the file-capture /
   Lambda-Blotto static gate over its captured set, **not** a whole-tree proof of all 2,277
   sparky files, and not the sealed-closure proof (§5.6). *Resolve:* run the sealed-closure
   receipts (still open).

### From `corpus_v17.md` §9

7. **`tools/seal_native_certificate.py` not shipped** — referenced by the native runners but
   absent from the package; the promotion sealer is external (§4.2, §9). *Resolve:* obtain the
   external promotion tooling.
8. **base_templates HEEx codegen wiring is intent, not demonstrated** — the atom.spec.yaml →
   base_templates macro → projection-artifact trace is specified in the repo plan but the
   corpus ships materialized outputs, not the invocation trace (§6.3, §9). PARTIAL. *Resolve:*
   run the base_templates render engine against the v17 reference target.
9. **In-package `split()`/`consolidate()` render engine + inverse certificates not shipped** —
   reversibility is evidenced by cross-build digest equality + the MAP/REDUCE pair, not an
   executable (§7.3, §9). *Resolve:* the enforcement implementation (law is "active red").
10. **Three non-identical projection enumerations** — `materialized:as` slug (11, no ttl) vs
    `nativeProjectionFamily` (12, with ttl) vs paper contract (10) (§7.1, §9). Recorded
    verbatim, not reconciled by fiat. *Resolve:* a normative reconciliation decision.
11. **`.aob.dir` normal form vs shipped shards** — the paper's per-atom `.aob.dir` normal form
    vs this distribution's corpus-wide per-axis shards are the same carrier at different
    granularities (§9). *Resolve:* materialize the per-atom directories if the atom-granular
    form is required downstream.

### From `base_agents.md` §HOW / §Provisional

12. **`agents/telephone` literal directory absent** — the telephone surface is
    `agents/codex/telephone-harness.md` + `lib/telephone/**` (§G, §Provisional). *Resolve:*
    n/a — the path was a mis-expectation; the real referents are named.
13. **Per-octet "one atom per byte 0..255" not materialized** — specified in law + present as
    tensor coordinates, but no physical one-atom-per-octet file (§B, §Provisional). PARTIAL.
    *Resolve:* materialize the per-octet atom family if required.
14. **RGB-256-per-channel standalone carrier PROVISIONAL** — present as law + tensor coordinate
    + traversal-color kernel + web-UI colors, not a standalone on-disk atom family (§I).
    *Resolve:* locate/mint the per-channel carrier atoms.
15. **Live GeoSPARQL (Sedona/SIS) engine — corpus evidence only** — Sedona/SIS present as
    corpus evidence repos + one Fuseki skill; no running geometry pipeline here (§F). *Resolve:*
    the engine likely lives in the `cpg-highway` twin.
16. **JEPA↔telephone bridge implied, not stated** — coupling visible only by cross-reading the
    `.twin` symlink + `cpg_highway_twin` dependency + `storage_lambda_frame` S:O:P doc (§G, §H).
    *Resolve:* an explicit stated bridge in `agents/`.
17. **golden AOB audits RED** — `_audit_sparql.yml` VERDICT **FAIL** (7 broken is:a spines,
    `isa_reaching_type_type 201/208`); `_audit_contract.yml` 168/171 (§D.7). Not a source gap
    but a live RED state. *Resolve:* repair the 7 spines + 3 contract fails (operator seal).

### From `base_templates.md` §6 (representative; 25+ fragment gaps, all cross-tree/out-of-corpus)

18. **AtlasContract consumers absent** — `bin/ba-atlas-render`, `specs/atlas/_tools.yaml`,
    `store/atlas/` named but not in `forge/base_templates`; host repo unresolvable (§6 frag-000).
    *Resolve:* locate the consuming `ba` engine repo.
19. **`_canon` value source `config/constants/universal.exs` not in corpus** — the enum/root
    map source is external (§6 frag-000). *Resolve:* the `base_agents` `config/constants` tree.
20. **`primitives.ttl` absent** — referenced by all 6 `control/` templates + the pyarrow
    template (`§primitives.control.*`, `L218`); returns nothing over the whole working tree
    (§6 frag-016, frag-017). *Resolve:* obtain the `primitives.ttl` SPECIES catalog.
21. **`SEAL.md` cross-tree unknown** — `templates/templates/SEAL.md` describes a `ba/templates/`
    sealed tree under `$BA_DIR`; whether the present `unix/` files are the SEALED copies, the
    FRONTIER, or a third `forge/`-rooted tree is unresolvable from any slice (§6 frag-027 G1).
    *Resolve:* diff against the `$BA_DIR` sealed tree.
22. **broadcast_record classification-name divergence** — bash leg names
    `silmaril_l1f_durable_commit`/`silmaril_l3en_ring_tier`; haskell+scala legs name
    `silmaril_l1c_durability_acked`/`silmaril_l3a_ring_tier`; both cite `r1_staging/
    atlas_models/**` (outside corpus) (§5, §7.2). *Resolve:* consult the atlas-model JSONs.
23. **Triple-brace `{{{ var }}}` render semantics** — 13 files use it for a second live
    substitution layer; the renderer/config that fixes the semantics is outside the corpus
    (§6 frag-017 P1, frag-016). *Resolve:* the render harness config.
24. **fp_triad `_body/hs.j2` & `scala.j2` `TemplateSyntaxError`** — endif-inside-for at
    hs.j2:30 / scala.j2:24; ex/sh parse OK (the "SILMARIL FORK 2026-05-18" fix present in ex/sh,
    absent in hs/scala) (§4 fp_triad). *Resolve:* port the fork-fix to hs/scala.
25. **`_drv_donor_*` "drv" expansion unresolved** — lexical identity stated nowhere (§6
    frag-000 item 5). *Resolve:* a naming key in the consuming engine.

### From `base_foundations.md` §6

26. **"AOB"/"AOBs" expansion unknown** — from `forge/specs` README `# base_aobs` / url
    `groenewt/base_aobs`; neither file nor brief expands the acronym; `base_agents.md` treats
    the corpus as "AOB atoms" but never spells it either (§6.1). *Resolve:* a source that spells
    the acronym (candidate: "Atom-of-Being" per corpus_v17.md §6 / "Atom-Oriented-Bundle" per
    base_templates.md §1 — **the two maps themselves disagree on the expansion**; see gap 30).
27. **"GA" expansion** — from `Base GA Repo/External/Templates/Bin/Agents`; **[inference]**
    plausibly "GraphAtlas" per the surrounding corpus title, not asserted by any README (§6.2).
    *Resolve:* a source that spells "GA".
28. **`sbin` path-record defect PROVISIONAL** — the `sbin` gitlink has no `.gitmodules` URL, so
    no declared origin for the `sbin` path exists in the source (content capturable via `bin`
    at the same SHA) (§6.3, §2.4). *Resolve:* n/a from the tree — the path-record's origin is
    genuinely unrecoverable; add a mapping upstream.
29. **No `III-` foundations document** — the bundle numbers I, II, IV, V; no `III-*` directory
    (§4, §2). *Resolve:* confirm whether III was planned/withdrawn.

### Census-level unknowns (this agent)

30. **"AOB" expansion disagreement across maps** — `corpus_v17.md` §6 titles it
    **"Atom-of-Being"**; `base_templates.md` §1 titles it **"Atom-Oriented-Bundle"**;
    `base_agents.md` never spells it; `base_foundations.md` §6.1 marks it genuinely unresolved.
    Held as an open discrepancy, not force-fit. *Resolve:* a canonical source spelling.
31. **basicttl has no dedicated W1 discovery map** — its internal ontology taxonomy (Row 3,
    Axis A9) is captured only via the frozen `basicttl.tree` + cross-references in
    `corpus_v17.md` as a source corpus. Structure (chapter axis, atom-type axis) is computed
    here from the tree, not narrated by any map. *Resolve:* a dedicated basicttl discovery map
    would narrate the `_verb/` chapter ontology and the atom-type shapes.
32. **basicttl count drift tree-vs-package** — `basicttl.tree` = **30,234** files (this pin);
    `corpus_v17.md` §5.1 FINAL_VALIDATION counts **30,224** basicttl source files inside the
    v17 package. +10 delta. *Resolve:* pin reconciliation between the live `basicttl/` and the
    snapshot frozen into the v17 corpus (`source-corpus/basicttl`).
33. **`.aob.dir` atom-count vs golden file-count** — `base_agents.md` §0 prose says "2,094
    sealed atoms"; the computed atom-directory count over the tree is **217** golden `.aob.dir`
    (458 repo-wide), while **2,094** is the golden *file* total. Recorded as a computed
    refinement of the map's loose prose. *Resolve:* n/a — both figures are correct at their
    granularity (217 atoms across 2,094 files); flagged so downstream does not equate them.
34. **superpowers skill contents un-narrated** — Row 8 / Axis A11 are computed from the tree
    only; no W1 map covers the superpowers corpus. The 14-skill flat axis is a tree observation,
    not a narrated taxonomy. *Resolve:* n/a for the census (structure is fully captured); a
    content map would be a separate task if downstream needs skill semantics.

---

*Silmaril · GraphAtlas — "Inspizierbar. Revidierbar. Föderiert." · Nihil occultum, tantum textum.*
