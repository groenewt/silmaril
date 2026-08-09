# Plan Freeze: Silmaril Ontology-First Rebuild

Session terminated due to context exhaustion. This is one of four handoff
files — each concern in its own file:

- **PLAN_FREEZE.md** (this file) — plan state and what's next
- **TRANSCRIPT_VERBATIM.md** — complete verbatim user transcript with all QA
- **STRICTNESS_RULES.md** — binding precision rules (15 rules)
- **SUBAGENT_FINDINGS.md** — full mapping agent findings (5 agents)

---

## Plan State (Frozen As-Is)

### Approved Plan (from Session 1, user-ruled)

The approved plan file is at `.claude/plans/tighten-build-out-and-ensure-velvet-feather.md`.

Four user rulings (final, binding):

1. **FILE AXIS = VIRTUAL TAXONOMY WITH BFO/CCO GROUNDING**: Not bare path
   URNs. The file tree is a taxonomy: silm classes for repository, file
   tree, directory, module, file, plus kernel layer (file descriptor, inode),
   each descending through cco:/BFO parent classes. File identity URNs use
   the corpus path idiom. MANDATORY: a FULL PREDEFINED PROJECTION PACKET.

2. **COORDINATES = N-DIMENSIONAL CRS LAW**: Geometry/axes are Nth-dimensional,
   never hard-fixed at 3. A CRS DECLARES its ordered axis list. The web page
   is MULTIPLE CO-EXISTING CRSs (plane 2D, layering 3D, navigation ND, five
   glossary chart CRSs 3D). Coordinates DERIVED, never hand-written.
   SHACL enforces coordinate-count == CRS dimension.

3. **FABLE = DISSOLVE AND ABSORB**: File disappears; content retyped into
   existing classes (ConcreteAnchor/DecompositionStep idioms); fable-as-query
   enters the query library.

4. **DEPTH GATE = AGGRESSIVE ENFORCEMENT WITH ABSOLUTE REMEDIATION**: Blocking
   for all of basicttl/ now. Every legacy file remediated with real
   content-derived depth. Strict-unary CPython overhead accepted.

### Original Six Phases

- **Phase 1**: Glossary registry + virtual file taxonomy + projection packet
- **Phase 2**: Derivation pipeline (typed pylib family morphism/ontology/chart/)
- **Phase 3**: Shapes and depth become the executable law
- **Phase 4**: Query law: all runs GeoSPARQL
- **Phase 5**: Renderer consumes geometry (UI configured from glossaries)
- **Phase 6**: CI assembly, docs, ship

### Session 2 Expansions (New Rulings from Goal Answers)

These expand the plan based on the four Goal answers in Message 16:

**A. Corpus consolidation scope (Goal 1):**
- example_gippidy_01 IS the fullest wish — ALL projections:
  - AOB (Atom YML — templates submodule powers this exact format)
  - LinkML (critical for broader renders with ALL output formats expected)
  - Atlas (dictionary/thesaurus/axes/"semantic topology")
  - OSSIE (essential mime-ontology for strict polysemy enforcement as literal anchor)
- Multiple corpuses consolidated onto universal base with generics
- Discovery: base_agents `golden` and `r1_staging/*/**` contain the generics
- All of chat gippidy content, no exceptions except on collisions
- Establishing the true definitive v1 ontology AOB buildout

**B. Render scope (Goal 2):**
- EVERYTHING including docs/ — zero hand-authored HTML anywhere in the repo
- Subatomic file-format decomposition for EVERY format touched
- Sparky substrate (lambda blotto engine) requires files understood as their own languages
- Glossaries are numerous, collide by design (polysemy is literal, not metaphor)
- File format breakdown: file -> markdown -> {structure: headers n1..n+, tables, diagrams, snippets, etc.}

**C. Planning mandate (Goal 3):**
- Use https://github.com/obra/superpowers for full e2e planning with proper sequencing/order
- Strict enforcement of unary style across ALL scripts in the library
- All existing scripts that violate unary law require refactoring — no exceptions
- Ontology-first, full completion — macros are projection targets of the owl:Class taxonomy

**D. CI engine architecture (Goal 4):**
- Engine-agnostic, preferably ALL of:
  - Apache Jena (Java/Scala, GeoSPARQL native runners, pinned 6.2.0 from corpus)
  - Apache SIS (in tandem with Jena for Scala/Java geospatial implementations)
  - Apache Sedona (embedded geospatial database)
  - rdflib (Python, consolidation and non-spatial queries)
- All external dependencies explicitly declared under unary law
- Nomenclature precise and subatomic
- CI/CD is its OWN GOAL — distinct from render/projection/ontology

---

## What's Next (Based on Most Recent Answers)

The next session picks up HERE. The sequence, with CI/CD as its own
distinct workflow:

### Workflow 1: Discovery and Mapping
1. Clone and map https://github.com/obra/superpowers — user mandated its
   use for e2e planning.
2. Map base_agents `golden` branch and `r1_staging/*/**` — user identified
   these as containing universal base generics. Content not yet mapped.
3. Map the sparky/lambda-blotto substrate in full — understand the existing
   lambda invocation and byte-schema families in
   `scripts/python/pylib/src/silmaril/sparky/`.
4. Full corpus structure deep-dive (example_gippidy_01 materialization
   pipeline, especially the native Jena 6.2.0 runners).

### Workflow 2: Ontology Design (Subatomic File-Format Taxonomy)
1. Define owl:Classes for every file format: TTL, HTML, CSS, SVG, Markdown,
   SPARQL, YAML, Python — each as its own language/glossary.
2. Each format decomposes into structural components (distinct typed classes).
3. Map component classes to base_templates HEEx macros (ontology-first;
   macros are projection targets).
4. Wire SHACL shapes for composition constraints.

### Workflow 3: Render Pipeline (GeoSPARQL Codegen)
1. Remove ALL committed generated artifacts from branch.
2. Build the GeoSPARQL query library for rendering.
3. Wire base_templates HEEx macros as the codegen engine.
4. Every page/component generated from query results ONLY.

### Workflow 4: CI/CD Pipeline (Its Own Goal)
1. Multi-engine dependency declaration (Jena, SIS, Sedona, rdflib).
2. Consolidation, validation, depth gate, chart gate, query-law gate.
3. Render pipeline execution in CI.
4. Trust/provenance gates.
5. CI failures investigated and fixed AS THEIR OWN WORKFLOW — never mixed
   into other tasks.

### Workflow 5: Corpus Consolidation (Bound/Morph)
1. Establish universal base with generics from base_agents golden/r1_staging.
2. Import example_gippidy_01 algebra, projection family, native runners.
3. Establish v1 ontology AOB buildout.
4. Collision resolution (all of gippidy, no exceptions except collisions).

### Present the Full DAG
Express the above as a typed dependency graph (not a flat list) with
workflows as base units, phases/sequences as children, in SHACL + GeoSPARQL
terms. The DAG itself is ontology. Budget: 1000 agents.

---

## Branch State at Freeze

- Branch: `claude/custom-pgp-sign-git-ozh8th`
- HEAD: `9079d817` on top of `8a563e34`
- Content: clean rebase + four forge/ submodules + PLAN_FREEZE.md
- Prior phase-3 work: deliberately dropped in user-mandated rebase. Start fresh.
- CI status: two checks failing (Ontology Validation, Script Gates) — these
  are a pre-existing condition on the rebased branch. CI fix is Workflow 4.
- Submodules:
  - `forge/base_agents` (d2b1217)
  - `forge/base_templates` (eb3d916)
  - `forge/example_gippidy_01` (f9be255)
  - `forge/base` (c4e8281)

---

## Explicitly Deferred (Named, Not Silent)

- Jena/GeoSPARQL-native execution acceptance (corpus native-runners equivalent)
- Charting full basicttl corpus (30k fragment files)
- The 40+ volume Helios scaffold intake (maintainer holding back)
- Apache SIS and Sedona integration (declared; implementation follows Jena)
