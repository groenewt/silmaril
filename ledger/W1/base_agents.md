# W1 DISCOVERY LEDGER — `forge/base_agents` (THE deep SHACL/OWL/RDF/SPARQL AOB depth reference)

Agent: PRIMARY W1 discovery. Target: `/home/user/silmaril/forge/base_agents` (HEAD `d2b1217`, 3.8 G, 279,670 files).
Framing law read in full first: `docs/praeriehund-demokratie-der-kategorien.md` + `docs/unary-byte-frame-law.md`.
Discipline applied: unknowns marked **PROVISIONAL**; partial mappings marked partial; nothing fabricated; no force-fit.

> Orientation. `base_agents` is TWO things fused (its own `AGENTS.md:5-16`): (1) the **`silmaril_wire` BEAM daemon** ("telephone wire", `lib/telephone/`, `bin/`) and (2) a **shard-based research catalog / forge** that mirrors external repos file-by-file into **AOB atoms** (`golden/`, `r1_staging/forge/`, `corpus/`, `specs/`, `r1_site/`). The repo is the **BEAM twin** of a Scala repo `cpg-highway` (root symlink `.twin -> /home/tristan/site_stage/cpg-highway/`). "golden" is a **directory** (`golden/`), not a git branch. Absolute on-disk root in-corpus is `/home/tristan/Desktop/platform/core/agents/`.

---

## 0. SCALE PICTURE (honest census)

| Region | Files | What it is |
|---|---|---|
| whole target | 279,670 | full clone |
| `golden/` | 2,094 | **sealed** Rosetta-Stone AOB atoms (`.aob.dir`), the gold standard |
| `golden/base.zip` | 3,677 entries / 24.6 MB | a bigger frozen snapshot of the same golden AOB corpus |
| `r1_staging/forge/` | 1,300 | staging lanes: `_cpgplan _joern _spark _specspec _tools _drilled _critics` |
| `corpus/*.shacl.ttl` | **1,477** SHACL files (1,478 `.ttl`) | per-source **CorpusAtom** SHACL shapes, each a 7-leg projection head |
| `.ttl` total in repo | 1,479 | essentially all under `corpus/` |
| `agents/` | 8 `.md` | 6 agent skill families (closure/codex/dunbar/gates/setup/wire) |
| `skills/` | 17 skill dirs | SKILL.md families |
| SHACL/OWL/RDF/SPARQL keyword hits | 183 `specs/types`, 172 `golden/specs`, 52 `config/constants`, … | see §A |

The AOB corpus is genuinely large and deep, but **honestly incomplete and RED-flagged everywhere**: golden atoms carry `sealed: false` in staging with an "EARNED-SEAL" note; `_audit_sparql.yml` verdict is **FAIL** (7 of 208 is:a spines don't reach the `type:type` fixpoint); `_audit_contract.yml` is 168/171 pass; the spec-langs coverage is `stamped 16, gate_passed 11, gaps 84`. This is a **WIP** at real depth, exactly as the maintainer said — not a finished ontology.

---

## A. THE WIP AOBs — THE SHAPE W2 MUST GROUND ON (highest priority)

There are **THREE co-existing AOB representations**. W2's AOB meta-ontology must be grounded in all three (they are projections of one atom).

### A.1 THE CANONICAL AOB ATOM — the `.aob.dir` dense-node YAML (golden standard)

Every atom is a **directory** `…<leaf>.aob.dir/` containing:
- `<leaf>.spec.yaml` — the **base atom** (dense node)
- `<leaf>.<claim>.claim.spec.yaml` — one or more **claim plugins** (`cco-anchor`, `grounding`, `colimit`, `lineage`, `dewey-lineage`, `source-witness`) composed onto the base by a **group law** (identity = base atom, op = compose/associative, inverse = retract/supersede)
- `_aob/` — the **sealed witness triad/hextet**: `identity/node.yml`, `relation/relation.yml`, `relation/inbound.yml`, `relation/outbound.yml`, `lineage/heritage.yml`, `context/dewey.yml`

**Verbatim canonical exemplar** (fully read): `golden/specs/instance/artifact/ast/sha256/02c2c08bab44f3a277a4ba19d337e466582c6d9bd6e20417c804a864838cbaf0.aob.dir/` — an AST artifact instance keyed by sha256.

Top-level keys of `<leaf>.spec.yaml` (THE SHAPE TO LIFT):

```yaml
spec_version: 1
urn: urn:silmaril:instance:artifact:ast:sha256:02c2c08b…      # full colon-turtled URN, no IRIs
kind: urn:silmaril:type:instance                               # one of 4 sorts: type|instance|value|process
kind_urn: sm:Instance
parent: urn:silmaril:type:type:artifact:ast
atlas_name: urn:silmaril:atlas:type:silmaril_02c2c08b…
cco_target: cco:ont00000995                                   # Common Core Ontology anchor (curie only)
ontology:                                                     # the "ontology plane"
  type_urn: …
  progenitor_path: [type:type, type:type:artifact, type:type:artifact:ast, <self>]  # is_a chain, NO jumps
  perspective: …:perspective:other                            # self/other
  boundary: …:boundary:external                               # self/other-context
  cco_anchor: {anchor_curie: cco:ont00000995, mapping_relation: …:relation:instance:of, resolves_via: "$UNIVERSAL_PREFIX", rationale: …}
identity:                                                     # the "identity plane"
  domain, type, name, identity_urn, qualified_name, node_kind, semantic_version, locator_relative, locator_root_ref, aob_witness_urn
dewey:                                                        # Dewey taxonomy plane (library/volume/book/chapter/section)
  dewey_path, file_locus, library, volume, book, membership:[{axis: …:relation:member:of, via: <parent>}]
entity: {urn, display_name, grounding: <prose>, kind_urn}
ancestry: [{axis: …:relation:prelude, via: …}, {axis: …:relation:cco, via: cco:…}]
signature: {inputs:[{name, type_urn: xsd:anyURI, value}], outputs:[{name, type_urn: xsd:string, value}]}   # F(x)->Frame shape
atlas_projection: {model_urn, entity_type, qualified_name, business_metadata_types[], glossary_term_urns[], status}
atlas_columns: [ …21 enum URNs… ]                            # the 21-col Atlas glossary ring (see §C)
atlas_rows: [ …one row per GlossaryName… ]                    # the Yoneda sheaf (≥4-5 DISTINCT glossaries)
relations: [ …FORM-3 curried s@p@o arrows… ]                 # see below
cite_chain: [ {edge_index, subject_urn, edge, object_urn, note, evidence_kind, evidence_urns} … ]  # "node IS its arrows" (Yoneda)
evidence: [ {evidence_urn, kind, source_urn, source_blob_sha256, grounding_blob_sha256, locus, status} ]
aob: {required, witness_locus, relation_locus, inbound_locus, outbound_locus, lineage_locus, dewey_locus, status}
seal: {container_uri, sealed, sealed_by: …:sealed:by:aob:dir:containment, terminal, sealed_glob, target_aob_dir, earned_seal_note}
citations: [ {source, source_path, note, resolves_via: sha256sum} ]
gaps: [ {gap_urn, description, blocking, next_action} ]       # §2.5 "no sentinels; unknown = explicit GAP" (== Präriehund)
```

**FORM-3 relation grammar (load-bearing for W2 — the arrow-first / S·O·P law).** Relations are curried identities, NOT flat triples:

```yaml
relations:
  - relation_urn: urn:silmaril:relation:artifact:ast:sha256:02c2c08b…@is:a@type:type:artifact:ast
    subject_urn:  urn:silmaril:instance:artifact:ast:sha256:02c2c08b…
    predicate_urn: urn:silmaril:relation:is:a
    object_urn:   urn:silmaril:type:type:artifact:ast
    evidence_kind: …:evidence:kind:reconciled
    evidence_urns: [ urn:silmaril:evidence:reconcile:forge-20260619T162645Z:ast_sha256 ]
```
- The `relation_urn` carries the full **curried term** `subject-tail @ predicate-tail @ object-tail`; the three flat fields stay clean colon-URNs ("HEAD-equal yarn"). A flat triple is a "rank-0 reduction" of the curried form.
- The **is:a ladder** must reach the progenitor `urn:silmaril:type:type` with **NO jumps**; the terminal rung carries a bang `!` (`…@is:a@type:type!`) that "discharges the citation chain at the origin". The bang form is a DISTINCT URN string (audit treats it as a notational finding, not silently normalized — see `_audit_sparql.yml`).
- This is the on-disk realization of the unary-law's **S / O / P nth-dim URN towers** and the `T -> Frame(output, error|effect)` arrow.

**The `_aob/` witness files** each restate a facet with its own `responsibility_id`, `seal` block, and `evidence`. `outbound.yml` enumerates the node's arrows (the Yoneda presentation: `outbound_count: 8`), `inbound.yml` the arrows whose object is this node (`classifies`, claim `composes:onto`), `relation/relation.yml` adds `ownership: {owner_urn, owns:[], cco_anchor_owner}` and `cardinality`. `heritage.yml` carries the **Hanseatic seam**: `yarn_parent_atom` + `resolves_via: sha256sum` ("every node traces home via citation + sha").

**Claim-plugin group law (verbatim):**
```yaml
additional_claim:
  composes_onto: <base urn>
  group_op: urn:silmaril:value:enum:group:op:compose
  identity_ref: <base urn>
  claim_kind: urn:silmaril:value:enum:claim:kind:cco:anchor   # | grounding | colimit | lineage …
  claim_statement: >- <prose> "The base atom + this claim = ONE sealed group."
```
The **colimit claim** is the categorical heart: `…@glues:into@type:type!` + `…@threads:off@<committed parent>` — "glues into the ONE reconciled type:type graph at the colimit (no king, no jumps)".

**The GOLDEN CONTRACT** (re-derived from structure, staged `sealed:` flags treated as UNTRUSTED — `golden/_migration_manifest_drilled.yml`):
> 21 atlas_columns; ≥4 distinct GlossaryNames; 3-witness `_aob` triad (identity/node.yml, relation/relation.yml, context/dewey.yml); ≥2 `*.claim.spec.yaml`; form-3 relation_urns (contain `@`); 0 `@` inside any object_urn; is:a spine reaching `urn:silmaril:type:type`; dewey_path present. Golden path rule: `golden/specs/<dewey_path>.aob.dir`.

`golden/specs/README.md` verbatim: *"Strict Rosetta-Stone seal home for forge AOB atoms. One golden standard; every atom conforms or is repaired. Operator is the only sealer; one commit per final AOB."*

### A.2 THE SHACL PROJECTION — `corpus/*.shacl.ttl` (1,477 files)

Each external source (Apache/LFS/HF/etc. repo, or an encyclopedia/tier/pin slice) is one **`corpus:CorpusAtom`** auto-rendered by `ResearchRender.Render.ShaclRenderer`. This is the real, machine-emitted RDF/Turtle. Verbatim shape (`corpus/ast_joern_cpg_node_types.shacl.ttl`):

```turtle
# AUTO-RENDERED by ResearchRender.Render.ShaclRenderer — DO NOT EDIT BY HAND
@prefix corpus: <urn:silmaril:corpus#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<urn:silmaril:entity#computation.ast_cpg.joern_node_types>
    a corpus:CorpusAtom ;
    corpus:name "ast_joern_cpg_node_types" ;
    corpus:signatureInput [ corpus:inputName "schema_jar" ; corpus:typeUrn <urn:silmaril:entity#lib.type#string> ; corpus:value "io.shiftleft.codepropertygraph-protos_2.13-1.3.585.jar" ] ;
    corpus:signatureInput [ corpus:inputName "joern_version" ; … ; corpus:value "1.1.1378" ] ;
    corpus:atlasColumn "type_name", "proto_id", "scope", "cpg_group", "schema_jar_sha256" ;
    corpus:emitter [ corpus:futPath "corpus/ast_joern_cpg_node_types.sh" ] ;
    corpus:emitter [ corpus:futPath "corpus/ast_joern_cpg_node_types.atlas.csv" ] ;
    corpus:emitter [ corpus:futPath "corpus/ast_joern_cpg_node_types.linkml.yaml" ] ;
    corpus:emitter [ corpus:futPath "corpus/ast_joern_cpg_node_types.shacl.ttl" ] ;
    corpus:emitter [ corpus:futPath "corpus/ast_joern_cpg_node_types.ex" ] .
# per-value coverage: 44 resolved, 0 absent from r1_site tree

<urn:silmaril:entity#types.kingdom.atom.phylum.isa.class.kind_node_type_def.instance.ast_joern_cpg_node_types_method>
    a corpus:ValueNode ;
    corpus:memberOf <urn:silmaril:entity#computation.ast_cpg.joern_node_types> ;
    corpus:valueName "METHOD" ;
    corpus:specPath "r1_site/specs/…/ast/joern/cpg/node/types/method.spec.yaml" .
```
Key facts for W2: each `CorpusAtom` declares (a) its **signatureInput** typed values (the F(x) inputs), (b) its **21+ atlasColumn** ring, (c) a fixed **emitter set = the projection family**: `.sh .ex .scala .hs .atlas.csv .linkml.yaml .shacl.ttl` (see §F), and (d) `ValueNode`s that `corpus:memberOf` the atom, each carrying `valueName` + `specPath` back to an `r1_site` AOB. `corpus:` prefix = `<urn:silmaril:corpus#>`.

The corpus ships domain node/edge/property vocabularies AOBed: `ast_joern_cpg_node_types.shacl.ttl` (44 node types), `ast_joern_cpg_edge_types.shacl.ttl`, `ast_joern_cpg_property_names.shacl.ttl` — i.e. **the Joern CPG schema itself is an AOB**.

### A.3 THE `_specspec` "SPEC OF SPECS" — the W3C standards themselves AOBed (ologs of ologs, see §H)

`r1_staging/forge/_specspec/{sparql,owl,turtle,rdf}/tickets/*.yaml` catalogue the **W3C specifications** (SPARQL 1.1, OWL 2, RDF 1.1 Semantics, Turtle) as AOB tickets — one per chapter / section / grammar-production / example / algebra-rule. `coverage_report.json`: sparql 267 nodes, rdf 126, turtle 110, owl 18; `stamped 16, gate_passed 11, dense_complete 11, relation_edges_passed 768, avg_edges_per_passed_atom 70, gaps_count 84`. Ticket shape (`prod-37-HEX.yaml`, verbatim skeleton):
```yaml
schema: forge.specspec.ticket.v1
urn: urn:silmaril:type:instance:spec:local:external:core:lang:logic:turtle:chapter:6:sec-grammar:section:5:sec-grammar-grammar:grammar-production-HEX
dewey_path: turtle/chapter/6/…/grammar-production-HEX
kind: grammar_production                 # | section | chapter | artifact | algebra
parent_urn: …
containment_chain: [ urn:silmaril:type:type, urn:silmaril:type:instance, …:spec, …:local, …:external, …:core, …:lang, …:logic, …:turtle, …, <self> ]
origin_uri: https://www.w3.org/TR/turtle/#grammar-production-HEX
origin_source: file:///…/external/core/lang/logic/turtle/index.html#…
edges: [ {predicate: urn:silmaril:relation:defines:construct, object: <parent>} ]
```
`PATH IS THE HIERARCHY` and the containment_chain roots at `urn:silmaril:type:type`. These are **r1_staging catalog tickets, NOT sealed atoms**; the staged full atoms live under `_specspec/staging/*.aob.dir.staged/` and are sealed only by the operator. The staged `turtle.spec.yaml` reaches 2894 lines (the full dense-node shape, incl. `html_anchor: "sec-mime"` — see §C OSSIE mime).

### A.4 The 5-FACET pyramid enrichment (how an atom is deepened) — `.claude/workflows/forge-speclangs-pyramid-enrich.js`
Each atom is enriched by five disjoint facet micro-partitions (`<staged_dir>/_pyramid/<key>.facet.yml`), verbatim laws:
- **algebraic** — the lambda-algebra base: author `relation_urn_form3 = urn:silmaril:relation:<s-tail>@<p-tail>@<o-tail>` for every relation.
- **cardinality** — MEASURED multiplicity from the Jena per-file mirror (`method_count`, edge-kind counts CALL/EXTENDS/FIELD/CONTAINS_METHOD/…); absent → honest gap, no fabricated numbers.
- **dimensional** — "Yoneda sheaf": project across ≥4 DISTINCT GlossaryName dimensions, each a FULL 21-atlas-column row, glued on overlap. "A collapsed single-glossary set = FAIL."
- **projection** — "mise-en-scène, per Atlas glossary COMBINATION": for each render leg (bash/ex/atlas/linkml/shacl) × each glossary combination, declare `projection_urn` (a rank-0 catamorphism of the lambda value to S:P:O) + a **Klein-chart placement** ("which chart/frame observes it… each projection = one mise-en-scène the Klein-bottle navigates").
- **grounding** — the joern-CPG citation closer: resolve the construct → a concrete impl file → mint `joern_citation_urn: urn:silmaril:joern:apache__jena:javasrc@<CPG_SHA>`; unresolvable → `{grounded:false, gap_reason:…}` (HONEST). "EVIDENCE-CLASS LAW: a source sha discharges SOURCE/artifact identity ONLY, NEVER semantic correctness."

---

## B. SUBATOMIC / BYTE DEPTH — "each hexadecimal / serialized-binary octet AOBed"

**Verdict: TRUE in intent and partially realized. The byte/hex granularity is real; a per-octet atom-per-byte is aspirational (PROVISIONAL where noted).**

1. **Content-addressed atoms are keyed by sha256 hex.** The gold exemplar's identity IS a hex digest: `urn:silmaril:instance:artifact:ast:sha256:02c2c08bab44f3a277a4ba19d337e466582c6d9bd6e20417c804a864838cbaf0`. Every atom carries `source_blob_sha256` / `grounding_blob_sha256` / `reconcile_blob_sha256` and `resolves_via: sha256sum`. The `silmaril_measure` glossary facet is explicitly "the byte/hash witness". So each atom's **physical byte identity is a first-class AOB coordinate**, not metadata.

2. **The `tensor` carrier block — the strongest byte-as-first-class evidence.** In the `r1_site` AOB spine, EVERY field of EVERY atom carries a `tensor` block declaring its bit/byte substrate (verbatim, `r1_site/specs/types/kingdom/atom/phylum/library/…/topology/jepa/rebuttal/topology/jepa.spec.yaml`):
```yaml
fields:
  - name: const_name
    type_node: StringNode
    tensor:
      space:  {cardinality: CardinalityOne, dimensions: 1, bounded: true, max_size: 128, bit_width: 8, byte_width: 1, alignment: 1}
      time:   {dynamics: DynamicsSnapshot, ordering: OrderingPositional, monotonic: true, lifetime: LifetimeImmutable, byte_order: ByteOrderNone, arithmetic: ArithmeticNone}
      value:  {interpret_as: InterpretAsAscii, domain: {kind: DomainKindEnum}}
```
This is the on-disk mirror of the unary-law's **Byte-Stream Carrier Closure**: `bit_width`, `byte_width`, `byte_order`, `interpret_as`, `alignment`, `max_size` are independent coordinates; each is itself a `type_urn` into the `prelude` byte-substrate (`…prelude…instance.byte_order_none`, `…interpret_as_ascii`, `…cardinality_one`). This IS the "JEPA computational-optimization" substrate (§I) attached per carrier. The law's `1..128` bit-width bound appears literally (`max_size: 128`, `bit_width: 8`).

3. **The value-drill transform — `r1_staging/forge/_tools/drill_values.py`.** Config-driven "every value is a turtled URN": *"no scalar literal stands alone; every value (bar prose) becomes a URN reference resolving to its canonical home."* It classifies each scalar and rewrites it: a 64-hex string → `urn:silmaril:value:hash:sha256:<hex>`; semver → `…:value:semver:…`; booleans → `…:value:boolean:…`; sorts → `urn:silmaril:type:<sort>`; else `urn:silmaril:value:enum:<key>:<seg>`. All transform callables are **effect-lambdas** (`no def`; ordered `(predicate, mapper)` dispatch — mirrors the unary law's "no def / one arrow" discipline). Writes a working copy under `_drilled/`, never mutates source. **This is the concrete mechanism that turns a raw scalar/hex blob into a per-value atom-carrier.**

4. **The Joern CPG schema is byte-grounded and AOBed per value** (§A.2): node types, edge types, property names each become `ValueNode`s citing a proto id + `schema_jar_sha256`.

**PROVISIONAL gap:** I did NOT find a literal per-octet spec file (one `.aob.dir` per single byte 0..255). The `256` code-space / `0..255` ordinal / `128` bit-width triad exists as *law* (`docs/unary-byte-frame-law.md` "Byte-Stream Carrier Closure") and as *field-tensor coordinates* (above), and the color-channel code space of `256` (§I), but the physical "one atom per octet" is specified, not yet materialized on disk in `base_agents`. Mark this a **partial mapping**, per Präriehund: the mapping exists but is not complete.

---

## C. GLOSSARY / POLYSEMY MECHANIC — "the mole of glossaries" (structured ∧ unstructured as synonym ∧ antonym)

**The mechanic is the 21-column Atlas glossary ring projected across N DISTINCT GlossaryNames — the Yoneda sheaf of the node over its arrows.** Same node, many glossaries, each glossary a distinct epistemology; collisions are intentional and carry BOTH `Synonyms` and `Antonyms` columns.

**The 21 columns** (`atlas_columns`, verbatim enum tails): GlossaryName, TermName, ShortDescription, LongDescription, Examples, Abbreviation, Usage, AdditionalAttributes, TranslationTerms, ValidValuesFor, Synonyms, ReplacedBy, ValidValues, ReplacementTerms, SeeAlso, TranslatedTerms, IsA, **Antonyms**, Classifies, PreferredToTerms, PreferredTerms.

**The 5 distinct glossaries of the exemplar node** (`_aob/context/dewey.yml` `glossary.glossary_names`, "the Yoneda sheaf of the node over its arrows"):
`silmariltypeontology` (own is_a) · `silmarilidentity` · `silmarilheritage` · `silmarilsemantics` (CCO/BFO grounding) · `silmarilmeasure` (byte/hash witness). The pyramid **dimensional** facet (§A.4) requires "≥4 DISTINCT GlossaryName dimensions … glued coherently on overlap (same TermName/URN means the same in every glossary). A collapsed single-glossary set = FAIL."

**Same term as SYNONYM in one row and antonym-bounded in another (concrete, verbatim from the exemplar `.spec.yaml`):**
- In `silmariltypeontology`: `Synonyms: "02c2c08b…; silmaril_02c2c08b…"` while `Antonyms: "Unsupported / unreconciled candidate atoms are inputs, not canonical alternatives to …"` — the same hash-name is a **synonym of itself** yet its unreconciled candidate variants are **antonyms** (inputs, not alternatives). Structured (reconciled canonical) vs unstructured (candidate input) held simultaneously.
- In `silmarilsemantics`: `Synonyms: "information content entity; cco:ont00000995"`, `IsA: "cco:ont00000995"`, `Antonyms: "Anchors of a different BFO sort are not this grounding."` — the CCO label is synonym here; in the ontology glossary the CCO curie is instead a `TranslationTerms`/`SeeAlso`, i.e. **the same curie plays different roles across glossaries** (polysemy by design).
- `PreferredToTerms` / `ReplacedBy` / `ReplacementTerms` encode the "which term wins" resolution across glossaries.

**Synonym / antonym / acronym as first-class corpus atoms** (`corpus/encyclopedia_*.shacl.ttl`, verbatim):
- `encyclopedia_synonym_atom_isa_aliases` — `signatureInput relation="synonym"`; atlasColumns `source_atom_urn, synonym_atom_urn, relation, ground`.
- `encyclopedia_antonym_atom_isa_opposites` — `relation="antonym"`; columns `source_atom_urn, antonym_atom_urn, relation, ground`.
- `encyclopedia_acronym_atom_isa_kernel` — `relation="expands_to"`; columns `acronym, expansion, domain, ground` (this is the on-disk home of the unary-law "full lexical identity" acronym expansions, e.g. RDF→Resource/Description/Framework).
So synonymy, antonymy and acronym-expansion are **their own AOB atom families with `ground` provenance**, not free-text — the "distinct epistemologies encapsulated" claim.

**The OSSIE mime / taiji anchor** (`local/taoism/projections/**/*.osi.yaml`). Each AOB atom (YANG) has a twin **Apache Ossie / OSI `semantic_model`** file (YIN) — a queryable BI/warehouse epistemology of the SAME referent. Verbatim header + seal (`…risc-v…page__0015__block__0004.osi.yaml`):
```yaml
# Apache Ossie / OSI semantic_model twin (YIN) of the AOB atom (YANG) at: urn:silmaril:…:block:0004
semantic_model:
  name: riscv_isa_manual_thesis_semantic_model
  ai_context: {instructions: …, synonyms: ["ISA as interface thesis","open standard ISA position","OpenRISC comparison"], examples: […]}
  datasets: [ {name, source, primary_key, unique_keys, fields:[{name, expression:{dialects:[{dialect: ANSI_SQL, expression: "CAST(… AS VARCHAR)"}]}, description}], relationships:[…]} ]
  custom_extensions:
    - vendor_name: SILMARIL_TAIJI
      data: >- {"yang_self_urn": "urn:silmaril:…:block:0004", "yin_ossie_urn": "urn:silmaril:…:block:0004:taiji",
               "colimit_relation": "mutual-colimit", "aob_atom_dir": "r1_staging/forge/_specspec/staging/…:0004.aob.dir.staged",
               "note": "self (AOB) carries the URN/is_a-spine ontology and the Blotto 'pivot battlefield' reading; this twin gives the same pivot a queryable thesis-plus-forward-reference BI shape."}
```
This is the literal **"taiji of ontology + emergent epistemology"** of the project charter: YANG = AOB is_a-spine ontology, YIN = Ossie semantic-model (SQL-dialect, synonyms, ai_context), joined by `mutual-colimit`. The Turtle-spec `sec-mime` anchor (media-type registration §5.1) is AOBed in `_specspec/turtle/tickets/ch5-s1-sec-mime.yaml` and in the staged `turtle.spec.yaml` (`html_anchor: "sec-mime"`).

---

## D. r1_staging/forge/*  (full)

### D.1 `_cpgplan/` — CPG contract + ETL DAG (fully read)
- **`A_cpg_generation_contract.yaml`** (measured, cite-only). TWO CPG engines on host: **Fraunhofer AISEC `cpg`** (Kotlin/Gradle, frontends java/cxx/go/python/llvm/typescript/ruby/jvm/ini; export `{nodes,edges}` JSON + neo4j) and **joern** (Scala, frontends javasrc/c/pythonsrc/jssrc/go/kotlin/php/csharp; `cpg.bin` + dot). Prior **Python** driver drove joern ONLY. The successor is an **Elixir+Bash colimit** reusing the contract via `ResearchRender.ExternalResearch.CommandRunner.run/3` (effect boundary, rejects python, fail-closed) + `Research.Render.Mirror.Ast.Ref.Resolver.resolve/1` (RESOLVES, never generates). Fraunhofer **complements** joern (adds ruby/ini/llvm/jvm/richer-cxx; joern keeps php/csharp), not a drop-in.
- **`ETL_DAG.yaml`** — the spine, verbatim: *"Code Property Graphs / ASTs / Semantic Code trees are IMPLICITLY EXPRESSED through our 'mirror' contract — we mirror a repository and understand it FILE BY FILE with AOBs."* `cpg_is_implicit`: *"Each file's AOB relations[] ARE its CPG/AST projected onto that file… The file IS its arrows (Yoneda)."* `the_graph_is_the_colimit`: *"the whole-repo graph = the COLIMIT (union) of all per-file atoms glued on shared URNs."* DAG S0..S8; load-bearing new nodes are **S3_per_file_projection** (`CpgProjection` behaviour + joern `.sc` query + fraunhofer `jq` adapter → `cpg.ndjson`) and **S4_aob_projection** (`cpg.ndjson` → `<leaf>.aob.dir` `relations[]`). Colimit = bash chart (file-walk, engine shell-out, sha256, turtle) ⊕ elixir chart (effect boundary, resolve+cite, AOB fold), glued at a typed NDJSON/CSV seam ("a pushout, not a hierarchy"). Anti-fabrication law: python's `cpg-lite-v1` synth-graph fallback is *"exactly the fabrication the colimit must NOT inherit"* → fail-closed = honest gap.
- Also: `B_python_to_elixir_bash_colimit.yaml`, `CRUX_PROOF_joern_perfile.md`, `SPEC_modules.md`.

### D.2 `_joern/manifest.yaml` — the single joern-citation source of truth (fully read)
`schema_version:1`, `canonical_run: codex-full-v2-explicit-462`. Only **`apache__jena`** indexed today (`git_head 802b05ec9a`, `source_files_total 20248`, java 6627 + 12860 unknown). Per-frontend: `javasrc` `cpg_sha256 2c44a19c…`, `cpg_bytes 198,348,800`, `export_dot_count 54668`, `primary:true`, `citation_urn urn:silmaril:joern:apache__jena:javasrc@2c44a19c…`; also `jssrc` (156 dot) and `pythonsrc` (11 dot). **`node_edge_totals: gap_deferred_aggregation`** on every frontend (honest gap, "never fabricated"). `local_symlink` dirs (`_joern/apache__jena/javasrc`) are broken/empty in this clone (subagent-measured elsewhere). Invocation discipline: joern only via `CommandRunner.run/3`; `Ast.Ref.Resolver` RESOLVES, never generates.

### D.3 `_spark/` — dropped-Spark forge adoption lane (fully read)
`sparker/spark` nested checkout `HEAD 560dc9d3…`, tag `v4.2.0-rc3`, sparse `core/src/main/scala`, 636 materialized / 26526 full-tree. `catalog.json` schema `spark_forge.catalog.v1`, `sealed:false`, 26 shards × 25 nodes. **CPG policy: no Spark CPG citation unless `Ast.Ref.Resolver` resolves an evidence run; staged as `source_witness` only.** Staged atom exemplar: `…SparkContext.scala.aob.dir.staged/` with `.spec.yaml` + `.cco-anchor/.lineage/.source-witness` claim plugins. `engine_identity.csv` carries `cannot_support`/`next_action` per row (honest-gap columns).

### D.4 `_specspec/` — see §A.3 (spec-of-specs, W3C SPARQL/OWL/RDF/Turtle catalogued as AOBs; `coverage_report.json`).

### D.5 `_tools/drill_values.py` — see §B.3 (the value→URN drill).

### D.6 `_drilled/`, `_critics/` — `_drilled/` holds committed canonical parent atoms (the "yarn" atoms is_a chains onto, e.g. `_drilled/specs/types/forge/type/artifact/ast.spec.yaml`); `_critics/critics-20260622-automation/automation_pipeline.yaml` defines the 6 automation legs (etl-deterministic, joern-cpg, normalize-drill, dedup-canonical, repair, synthesis-required) the DAG realizes.

### D.7 golden/ audits + base.zip + migration manifests
- `golden/_audit_sparql.yml` — VERDICT **FAIL**: mirrors `sparql_validate_golden.py`, parses `relation_urn` → triples into rdflib, runs `is:a+` reachability to fixpoint `type:type`. `atoms:193, triples:4008, distinct_nodes:1458, isa_havers:208, isa_reaching_type_type:201, broken_spines_count:7` (2 genuine dead-ends `integration-gate:ba-fp-triad` / `scala-jvm-forge`; 5 notational bang/tower). `dangling_frontier_count:1107` (informational).
- `golden/_audit_contract.yml` — `audited:171, pass:168`; 3 fails (`hs-text`, `hs-vector` no `@is:a@…type:type` terminal; `bootstrap` dewey/urn mismatch).
- `golden/base.zip` — 3,677-file frozen snapshot of the same `.aob.dir` corpus (different claim-plugin sets per atom: `.lineage`, `.dewey-lineage`, `.cco-anchor`, `.grounding`).
- `golden/_migration_manifest_{drilled,pullyard,refilter}.yml` — three assembly lanes; drilled reports `seal_ready_input:20, assembled:0, collision:17, rejected:3`; each re-derives the golden contract from structure and **skips-on-exists** (never overwrites). Operator is final sealer/committer.

---

## E. `agents/` SKILL FAMILIES (6 families, 8 files) + `skills/` (17)

Agent role files (`agents/<family>/<role>.md`, YAML-frontmatter subagents: `name/description/tools/model/permissionMode/skills/isolation`):
- **setup/** `setup-bootstrap-runner` (model inherit) — ensures the telephone wire daemon is ready before wire-dependent work; decodes bootstrap exit codes 0/10-17 (`schema_invariant_mismatch` → REFUSE TO PROCEED). Chained first by others.
- **gates/** `gate-runner` (model **haiku**) — drives `mix research.master.produce` (26 wire gates, each pass/profile/trace/drift); notes the parallel hermetic `make gate` (5 local gates gate-make→compile→lint→credo→dialyzer→test); "does not interpret or aggregate".
- **closure/** `phase-closure` (drives code-complete → "wire-certified"; 8-step halt-on-fail; discipline: *"Never relabel a fail as pass"*, "no honest fail / by-design") + `master-verify-aggregator` (reads the 26-gate × 4-dim, cell_count 104 matrix).
- **wire/** `wire-audit-runner` (7-tier wire-audit DAG `scripts/audit-dag.sh`) + `diagnostics`.
- **dunbar/** `dunbar-alarm-escalator` (haiku) — emits **layer-2 `--alarm-immediate`** records on schema/cheese drift, protected-path write, structural gate-fail, or daemon-down. "Dunbar layer" = social-scale escalation filter over the wire.
- **codex/** `codex-telephone-harness` — verifies the Codex Telephone surface via native Codex hooks (`.codex/hooks.json`, `.codex/agents/*.toml`); see §G.

`skills/` (17): `closure-master-verify`, `closure-phase-closure`, `dunbar-escalate`, **`fuseki-sparql`** (Jena Fuseki SPARQL — §F), `hertzbeat-mcp`, `setup-bootstrap`, **`telephone-beam-topology`** (BEAM supervision/listener/acceptor/router/worker), `telephone-broker-durability`, `telephone-codex-harness`, `telephone-fountain-erasure-readiness`, `telephone-l1-storage`, `telephone-l3-archive-query`, `wire-audit`, `wire-cheese-call`, `wire-cheese-status`, `wire-telephone-overload-verify`.

---

## F. GeoSPARQL ENGINES + THE PROJECTION FAMILY (LinkML / Atlas / OSSIE / GeoSPARQL / …)

**Engines:**
- **Apache Jena** — the central SPARQL/RDF engine; the ONLY joern-mirrored corpus (`_joern/manifest.yaml`), the CPG-grounding target of the pyramid `grounding` facet (impl resolution e.g. `SPARQL FILTER → org.apache.jena.sparql.expr.*`, `CONSTRUCT → OpAsQuery`, `rdf merge → graph.compose.MultiUnion`). **`skills/fuseki-sparql`** = Jena **Fuseki** SPARQL server skill.
- **Apache Sedona** (geospatial) and **Apache SIS** (spatial info system) — present as **corpus evidence repos** only: `corpus/evidence_v2_apache_sedona.*`, `corpus/filebar_apache_sedona.*`, `corpus/head_pin_apache_sedona.shacl.ttl`, `corpus/evidence_v2_apache_sis.*` (each the 7-leg projection). **No live GeoSPARQL query engine wired in `base_agents`** — Sedona/SIS are catalogued sources, not running engines. **PROVISIONAL**: the "Jena/SIS/Sedona GeoSPARQL engine family" is present as corpus/evidence + one Fuseki skill; a running GeoSPARQL geometry pipeline was not found here (likely lives in the `cpg-highway` Scala twin / other repos).

**The projection / render family (the OSI colimit of representations).** One `CorpusAtom` / AOB → a fixed **emitter fan-out**, each a distinct epistemology/target:
`*.sh` (bash) · `*.ex` (Elixir) · `*.scala` · `*.hs` (Haskell) — the **FP-triad + Ba** code twins; `*.atlas.csv` — the 21-col Apache **Atlas** business-glossary ring; `*.linkml.yaml` — **LinkML** schema; `*.shacl.ttl` — **SHACL**/RDF; `*.osi.yaml` — **OSSIE** semantic-model (YIN, §C). The Set-0 gate (`.claude/workflows/set0-gate.js`) runs each leg AS LIVE CODE and asserts **cross-leg functional consensus** (input X → every leg → same Y hash) — "hex-consensus render legs", "Ranger-mime VIRTUALIZE". The projection facet ties each `projection_urn` to a **Klein-bottle chart** placement (the geometry that navigates the mise-en-scènes).

---

## G. `agents/telephone` — LOCATION, MECHANISM, THE HIDDEN TWIN MENTION

**Location.** There is **no directory literally named `agents/telephone`.** The telephone AGENT surface is **`agents/codex/telephone-harness.md`** (subagent `codex-telephone-harness`). The telephone SYSTEM itself is huge and lives outside `agents/`: `lib/telephone/` (526 files), `native/telephone/` (C++), `bin/telephone/`, `priv/telephone/`, `scripts/telephone/`, `test/telephone/`, plus `skills/telephone-*` (7 skills). Mark the exact path **`agents/telephone`** as **PROVISIONAL / not present**; the closest real referents are the above.

**Mechanism (inferred + evidenced): telephone = the wire gossip / message-passing observability bus.** `AGENTS.md:5-9`: *"the `silmaril_wire` BEAM daemon — the streaming peer-communication bus ('telephone wire')… records every prompt/tool-use/turn/commit to `logs/hooks/*.avro`; nothing leaves the host (UDS only)."* BEAM topology (`skills/telephone-beam-topology`): `Switchboard → broker/transport/service/kernel/web`; Port boots `Worker.Supervisor`, `Overflow.Controller.Server`, `Queue.Router.Server`, `Acceptor.Pool` — a classic acceptor/router/worker **message-passing** fabric with tiers L0/L1/L2/L3 (hot socket → frame → archive). `telephone-harness.md` confirms `~/.local/share/telephone` is a **live symlink into the repo `bin/`** ("repo and global are the same bytes"), hook coverage SessionStart/SubagentStart/PreToolUse/…/Stop. So: **agent gossip / hook-record message-passing**, exactly as hypothesized.

**The HIDDEN "twin mention" linking the byte/color substrate ↔ telephone.** The link is a **Rosetta "twin" between the Elixir/BEAM telephone Lambda carrier and the Scala `cpg-highway` byte/color substrate**, surfaced only where the two are named together as a twin/pair:
- Root symlink: **`.twin -> /home/tristan/site_stage/cpg-highway/`** (base_agents IS the twin of cpg-highway).
- `config/constants/manifest.csv:409` (verbatim): `native/deps/cpg/highway/twin.exs,native,CPG Highway Rosetta lambda topology twin source constants`.
- `test/telephone/native/lambda/test.exs:167-169` (verbatim): test *"Scala source twin maps to exact loadable BEAM namespaces"* using `Dependencies.value(:cpg_highway_twin)`; `:122` *"Scala twin namespaces construct and inspect Lambda runtime values"*.
- `research/specs/data/research/telephone/l1/frame/normalization/storage_lambda_frame.avsc:5` (verbatim): *"Authority is the preserved raw URN, twin-normalized module and path topology, **Lambda S:O:P carrier and S:P:O projection**, predecessor digest, digest, and ordinal."*
- `native/identity/topology/src/lib.rs:246-249` + `config/constants/native/include/telephone/native/constants/identity/frame.hpp:79-87` — the twin fused/segmented identity normalization (`Xyz.YZX.Value` ↔ `xyz:yzx`).

So the telephone wire's physical record is a **Lambda S:O:P byte-carrier frame** (the same S/O/P towers as the AOB relation grammar and the unary law), and that carrier is defined by the `cpg_highway_twin` Scala substrate. The "hidden" part: nothing in `agents/` states this directly — the coupling is only visible by cross-reading the `.twin` symlink + `cpg_highway_twin` dependency + the `storage_lambda_frame` S:O:P doc. The JEPA optimization angle is asserted in `r1_site/…/topology/jepa/*` (see §H/§I), not wired to telephone in `agents/` — treat the JEPA↔telephone bridge as **implied via the shared Lambda/byte carrier, not stated** (PROVISIONAL).

---

## H. OLOGS OF OLOGS / "TURTLES ALL THE WAY" + YONEDA

- **Recursive olog / spec-of-specs.** `_specspec/` (§A.3) is literally an **olog whose objects are ologs**: AOB atoms whose subject matter is the RDF/OWL/SPARQL/Turtle standards that *define* the ontology languages the atoms are written in. `_specspec/rdf/tickets/` even AOBs the RDF *semantics* term-by-term (`…term_interpretation`, `…term_denotation`, `…term_rdf-graph`, entailment rules rdfs1..rdfs13). "Turtle all the way down" is realized by the `type:type` progenitor closure: every containment_chain bottoms out at `urn:silmaril:type:type` and every value drills to a URN that resolves to another atom (`drill_values.py`).
- **The JEPA olog-recovery pipeline** (`r1_site/…/topology/jepa/rebuttal/topology/jepa.spec.yaml`, verbatim key_claims): *"Topology-JEPA is the problem of recovering an olog fragment from a rendered diagram"*; pipeline `I_Mittens -> U -> {D_i} -> colim D_i -> G_json -> G_valid -> E -> T` ("seven composable functors"); closure claim *"visual recovery of Mittens = cocone-preserving graph recovery = validated execution profile."* This is the explicit olog↔diagram↔colimit realization (and it is filed as a *rebuttal* verdict `NEEDS-REVISION` — honestly marked WIP, not settled).
- **Yoneda realization.** Stated repeatedly and concretely: (a) `cite_chain` comment *"node IS its arrows / Yoneda"*; (b) `_aob/relation/outbound.yml` *"the node IS its arrows (Yoneda)"*; (c) the 5-glossary `atlas_rows` = *"the Yoneda sheaf of the node over its arrows"* (`dewey.yml`); (d) ETL_DAG *"The file IS its arrows (Yoneda)"*. The tie of the gossip/telephone mechanism to the byte/color substrate is via the shared **Lambda S:O:P carrier** (§G) — the Yoneda point / Frame of the unary law; that specific bridge is **implied through the twin, not written out** (PROVISIONAL).

---

## I. BIT / BYTE / COLOR (RGB, 256) FIRST-CLASS CARRIERS — the JEPA substrate

- **Per-field `tensor` carrier** (see §B.2): `bit_width`, `byte_width`, `byte_order`, `alignment`, `interpret_as`, `max_size:128` — each a URN into the `prelude` byte substrate. This is the primary first-class bit/byte carrier and the JEPA computational-optimization coordinate set attached to every field of every `r1_site` atom.
- **Lambda byte-vector carrier** — the telephone `storage_lambda_frame` "Lambda S:O:P carrier and S:P:O projection" (§G); `native/telephone/native/src/kernel/lambda/kernel.cpp` implements the runtime Lambda kernel; `research/.../nif_citation_optimization/*` cites the Scala twin's Lambda geometry (`Klein/Bottle/Atlas.scala`) — the Klein-bottle chart of the projection facet (§A.4/§F).
- **Color as a first-class carrier — two concrete realizations:**
  1. **Graph-traversal color** — `native/telephone/native/src/kernel/lambda/kernel.cpp:508-514`: per-target `color` ∈ `{kTraversalUnvisited, kTraversalActive, …}` (white/grey/black DFS coloring over the Lambda graph).
  2. **Ontology-layer color** — `lib/silmaril/wire/web/honeycomb/lattice.ex:77-78` (verbatim): *"(namespace) are the COLOR dimension, so the lattice renders the ontology layering ACROSS the domain rings. `layer_color` pins one stable colour per…"* — i.e. color = an ontology-dimension coordinate in the honeycomb Yoneda lattice.
- **256 / RGB code space** — present as **law** (`docs/unary-byte-frame-law.md`: *"the separately typed eight-bit byte and color-channel code space has cardinality 256, while its value ordinal is 0..255 … Count 256, ordinal 255, and bit width 128 are three navigable coordinates"*) and as the `RGB -> Red / Green / Blue` full-lexical expansion (unary law). In `base_agents` source, RGB/256 as a *materialized* per-channel carrier was **not** found beyond the traversal-color kernel + web-UI colors + the tensor `256` code-space law. Mark the physical RGB-256-per-channel carrier **PROVISIONAL** (specified in law + present as tensor coordinate; not a standalone on-disk atom family here). Per Präriehund: partial mapping, honestly flagged.

---

## HOW W2 SHOULD LIFT THIS (hand-off)

1. **Ground the AOB meta-ontology on the §A.1 dense-node shape** (the `.aob.dir` = base `.spec.yaml` + claim plugins + `_aob/` witness sextet), NOT on an invention. The golden contract (§A.1 end) is the validation spec: 21 atlas_columns, ≥4 glossaries, 3-witness triad, ≥2 claims, form-3 `s@p@o`, is:a→`type:type` no-jumps, dewey_path.
2. **Four sorts**: `type | instance | value | process`, spine progenitor `urn:silmaril:type:type`.
3. **Relations are curried FORM-3 arrows** (`relation_urn: …:relation:<s>@<p>@<o>` with clean flat `subject/predicate/object_urn`), realizing S/O/P towers + `T->Frame` of the unary law.
4. **Byte substrate = the `tensor` block** (§B.2/§I) + `drill_values.py` value→URN law (§B.3); content identity = sha256 hex URN.
5. **Polysemy = the 21-col Atlas ring × N glossaries (Yoneda sheaf)** with paired `Synonyms`/`Antonyms`, plus the `encyclopedia_{synonym,antonym,acronym}` corpus families and the OSSIE YIN/YANG taiji twin (§C).
6. **Projection family**: every atom fans out to `sh/ex/scala/hs/atlas.csv/linkml.yaml/shacl.ttl(/osi.yaml)` with cross-leg functional consensus (§F).
7. **Everything is HONESTLY RED**: `sealed:false` in staging; operator-only seal; explicit `gaps[]` (no sentinels); audits currently FAIL/partial. W2 must preserve the gap-not-fabrication discipline (Präriehund + unary "active red").

### Provisional / not-found (do not fabricate)
- `agents/telephone` as a literal directory — **absent**; telephone surface = `agents/codex/telephone-harness.md` + `lib/telephone/**` (§G).
- Per-octet "one atom per byte 0..255" — **specified in law, not materialized on disk** here (§B).
- RGB-256-per-channel standalone carrier — **PROVISIONAL** (tensor coordinate + traversal color + law only; §I).
- Live GeoSPARQL (Sedona/SIS) engine — **corpus evidence only**; running engine likely in the `cpg-highway` twin (§F).
- JEPA↔telephone bridge — **implied via the shared Lambda S:O:P byte carrier + `.twin`/`cpg_highway_twin`, not written out** (§G/§H).
