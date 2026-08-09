# Subagent Mapping Findings (Preserved from Session 1)

Five mapping agents ran to completion in Session 1. Their findings are
preserved here in full for successor sessions.

---

## Agent 1: forge/base_templates (Architecture Map)

### Structure
- **`_universal_macros.j2`**: Hub file — imports and re-exports all macro
  registries. Single entry point for template consumers.
- **`_registries/`**: Per-concern macro files. Each registry owns one
  semantic domain (layout, navigation, typography, color, etc.).
- **`_urn/identity.j2`**: URN identity stamping macro. Generates
  deterministic URN identifiers from template parameters.
- **`_urn/stamps.j2`**: Provenance stamps — timestamps, session IDs,
  generation metadata baked into every rendered output.
- **`_canon/dewey_template_contract.j2`**: Path law — the Dewey-decimal
  inspired template naming contract. Enforces hierarchical template
  organization.
- **`_dispatch/`**: Thin NON-macro dispatch seams. These are NOT macros —
  they are typed dispatch points that route to the correct macro based on
  component type. The distinction is semantic.

### HEEx Component Grammar
- **`heex/_anchors/_macros/_spine.heex.j2`**: THE typed component grammar.
  Defines the composition algebra for page rendering. Component types:
  - `header` — page hero / section header
  - `section` — content section with container
  - `table` — data table with scroll wrapper
  - `svg` — chart / diagram mount
  - `mount` — generic component mount point
  Each is a distinct macro with typed parameters. The spine defines their
  composition ORDER — header -> section -> table -> svg -> mount. This
  order IS the rendering algebra.
- **`semantic_render_target.j2`**: Provenance-row contract. Every rendered
  output carries a provenance row linking it back to the ontology source,
  the template that generated it, and the query that drove it.

### Configuration
- **StrictUndefined everywhere**: Jinja2 configured with StrictUndefined.
  Any reference to an undefined variable is a hard error, not a silent
  empty string. This is the type-safety guarantee.
- **No inheritance, composition only**: Templates compose via macro calls,
  never via Jinja2 template inheritance (extends/block). This keeps the
  dependency graph acyclic and auditable.

---

## Agent 2: forge/base (Hub Foundations)

### LaTeX Foundations
- **I-fundamenta**: Core mathematical foundations document.
- **II-en**: English-language formalization.
- **IV-turtles**: Turtle (TTL) formalization — the RDF serialization as a
  first-class mathematical object.
- **V-polysemy**: Polysemy formalization — the theoretical foundation for
  why glossary collision is not a bug but the core design.

### Category-Theory Skill Contracts
- **Sheaf**: Sheaf-theoretic data integration — how local data patches
  (basicttl files) glue into a global section (the consolidated graph).
- **Semiring**: Algebraic structure for combining provenance weights and
  trust scores.
- **Lens**: Bidirectional transformation — the theoretical basis for
  projection (ontology -> materialized format and back).

### What It Is NOT
- No actual binary/LinkML/GeoSPARQL tooling. This is the THEORETICAL
  foundation, not the implementation.
- User's own characterization: "perfect for compressed binary corpuses as
  well as turtles and geosparqls and shacls" — meaning this is where the
  THEORY lives that the implementation must satisfy.

---

## Agent 3: forge/base_agents (Reference Skills)

### GeoSPARQL Runner Status: NONE WORKING
- **Fuseki client**: BROKEN. Dead aliases break 10/11 subcommands.
  The client script references function names that don't exist in the
  current codebase. Reference only — do not attempt to use.
- **Hanse SPARQL CI**: A COMPARATOR, not an execution engine. It compares
  query results against expected outputs. It does not execute GeoSPARQL
  queries with spatial functions.
- **`fuseki-sparql`**: References an EXTERNAL Apache Jena installation.
  Not self-contained. The actual GeoSPARQL engine must come from the
  corpus's pinned Jena 6.2.0 native runners (in example_gippidy_01).

### DISCOVERY STILL NEEDED
- **`golden` branch/directory**: User identified this as containing
  universal base generics. Content NOT YET MAPPED.
- **`r1_staging/*/**`**: User identified this as containing additional
  universal base content. Content NOT YET MAPPED.
- These are CRITICAL discovery tasks for the next session.

---

## Agent 4: forge/example_gippidy_01 (Corpus — v16)

### Scale
- **16 axes** (semantic dimensions for charting)
- **104,848 identities** (chartable entities)
- **1.68M rebindings** (geometry triples linking identities to CRS positions)
- **Full projection family** (every materialization format)

### Projection System
Split binary ZIP slices -> zstd-compressed tarballs -> reassembly pipeline.

Full materialization directory structure:
- **`ttl/`**: Raw Turtle RDF
- **`geosparql/`**:
  - `dataset.yaml` — dataset descriptor
  - axis-rebindings — per-axis geometry triples
  - queries — GeoSPARQL query library
  - native runners — pinned to Apache Jena 6.2.0 with GeoSPARQL support
- **`shacl/`**: Shape constraint graphs
- **`linkml/`**: LinkML schema projections
- **`ossie/`**: OSSIE mime-ontology projections (polysemy enforcement)
- **`xml/`**: XML schema projections
- **`sparql/`**: SPARQL query libraries
- **`metadata/`**:
  - `yaml` — structured metadata
  - `sqlite` — queryable metadata database

### materialized:as Projection Family
The complete projection vocabulary:
`self` / `shacl` / `linkml` / `ossie` / `geosparql` / `sparql` / `ttl` /
`xml` / `uml` / `dot` / `graphml` / `native`

Each projection is a distinct materialization of the same ontology source.
The projection packet (basicttl/atlas_projection_packet.ttl) declares which
projections each identity family supports.

### Coordinate Algebra (CONFIRMED against corpus samples)
- **x** = lexical depth (tokens split on `: / # @ ; ,`)
- **y** = operator degree (longest run among `: # @ ; !`)
- **z** = uint16 of first two SHA-256 octets of the exact URN string

---

## Agent 5: Organization / Artifact Audit

### Violations Found (All Require Remediation)

1. **ui-constructor.py masquerade** (`ui-constructor.py:244-303`):
   Hardcodes palette/typography in Python dicts while
   `basicttl/ui_constructor.ttl` carries only labels. The drift gate
   "enforces" the Python output — meaning it enforces a lie. The ontology
   does not author the visual values; the Python script does, and the gate
   protects the Python output from changing. This is backwards.

2. **Generated banners credit deleted scripts**: The HTML output contains
   generation banners that reference scripts that no longer exist in the
   repository. Dead provenance.

3. **ontology/ui-shapes.ttl orphaned**: The file exists and contains SHACL
   shapes for UI elements (UIElementShape: exactly one hasRegion;
   UILayoutRegionShape: x/y/w/h) but NOTHING in the pipeline consumes it.
   The shapes are declared but unenforced. Dead letter.

4. **Depth/byte-frame gates advisory-only**: The ontology depth check and
   byte-frame validation gates run with `|| true` and
   `continue-on-error: true` in CI. They warn but never block. This means
   violations accumulate without consequence.

5. **`_verb` legacy files**: The basicttl/_verb/ directory contains files
   that predate the current depth standards and are not subject to the
   blocking depth gate. These stay advisory per user ruling but the scope
   boundary must be explicit.
