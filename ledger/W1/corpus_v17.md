# W1 Discovery — Corpus v17 (`forge/example_gippidy_01`)

Agent: W1 discovery (ontology taiji). Date: 2026-08-07.
Target: `/home/user/silmaril/forge/example_gippidy_01` (484M, git-cloned; `.git` is a gitlink file).
Scratchpad (all reassembly here, nothing written to project tree except this ledger):
`/tmp/claude-0/-home-user-silmaril/9319deb2-2eab-59fd-b601-de3e0fb18f37/scratchpad/gippidy/`

Praeriehund discipline applied: unknowns are marked **PROVISIONAL**; partial mappings are named partial; nothing force-fit or fabricated. Scale reported honestly — bulk data rows (~1.68M rebindings, 29.4M turtle statements) were **sampled**, never fully read; **no structure, descriptor, runner, or schema was truncated**.

---

## 0. Tooling note

- `unzip`, `tar`, `python3` present. **`zstd` binary and `sqlite3` CLI are NOT installed** in this environment. Installed Python `zstandard` via pip; used Python `sqlite3` builtin. Decompression/untar done in Python (equivalent to the `zstd -d | tar -x` recipe). This does not change the recipe below — it only substitutes the reader.

---

## 1. `README.md` (target root) — full content (186 bytes)

```
unzip graphatlas-epistemic0-consolidated-v17-2026-08-06-control.zip -d graphatlas-epistemic0-full-control
cd graphatlas-epistemic0-full-control/ && ./reassemble.sh    ..   ./reassembled
```

The target dir holds `README.md` + `.git` gitlink + **12 split ZIP slices** (two families × 6 numbered parts) plus **two `-control.zip`** archives (**14** zip files total — 12 numbered slices + 2 `-control.zip`; verified `find forge/example_gippidy_01 -name '*.zip' | wc -l` = 14, matching the tree/census Row 7):
- `graphatlas-epistemic0-consolidated-v17-2026-08-06-{control, part-001..006-of-006}.zip`
- `graphatlas-epistemic0-semantic-formats-v17-2026-08-06-{control, part-001..006-of-006}.zip`

Every numbered ZIP ≤ 44,000,244 bytes (< 50,000,000 limit).

---

## 2. Reassembly — exact recipe quoted from the manifests

Both control zips carry `reassemble.sh`, `reassemble.py`, `PARTS.yaml`, `CHECKSUMS.sha256`, `README.md`, `DOWNLOAD_INDEX.md`. Consolidated additionally carries `reassemble.ps1`, `DISTRIBUTION_INDEX.yaml`, `FORMAT_COVERAGE.yaml`, `PACKAGE_SUMMARY.yaml`, `metadata__AXIS_COVERAGE.yaml`, `serialization__serialization-profile.yaml`, `validation__FINAL_VALIDATION.yaml`.

**Consolidated README recipe (verbatim):**
```bash
unzip graphatlas-epistemic0-consolidated-v17-2026-08-06-control.zip -d graphatlas-epistemic0-consolidated-v17-2026-08-06-control
cd graphatlas-epistemic0-consolidated-v17-2026-08-06-control
./reassemble.sh /path/to/graphatlas-epistemic0-consolidated-v17-2026-08-06-serialized-parts ./reassembled
```
> "The script verifies ZIP hashes, binary-slice hashes, the reconstructed payload hash, Zstandard integrity, safe tar paths, extraction, and the internal `PACKAGE_MANIFEST.sha256`."

**`reassemble.sh` (verbatim, consolidated):**
```bash
#!/usr/bin/env bash
set -Eeuo pipefail
trap 'printf "ERROR line=%s status=%s\n" "$LINENO" "$?" >&2' ERR
CONTROL_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
PARTS_DIR="${1:?usage: $0 PARTS_DIR [OUTPUT_DIR]}"
OUTPUT_DIR="${2:-$CONTROL_DIR/reassembled}"
PAYLOAD="$(PYTHONDONTWRITEBYTECODE=1 python "$CONTROL_DIR/reassemble.py" "$PARTS_DIR" "$OUTPUT_DIR")"
zstd -t "$PAYLOAD"
while IFS= read -r member; do case "$member" in /*|../*|*/../*|*'/..') echo "unsafe tar path: $member" >&2; exit 1;; esac; done < <(tar --use-compress-program=unzstd -tf "$PAYLOAD")
tar --use-compress-program=unzstd -xf "$PAYLOAD" -C "$OUTPUT_DIR"
ROOT="$OUTPUT_DIR/graphatlas-epistemic0-consolidated-v17-2026-08-06"
PYTHONDONTWRITEBYTECODE=1 python "$ROOT/tools/validate_release.py" "$ROOT"
printf 'PASS %s\n' "$ROOT"
```

**`reassemble.py` logic (both families identical in shape):** for each of the 6 parts in ordinal order — verify `zipSha256`, open the ZIP (must contain exactly one member `…-part-00N-of-006.bin`, `testzip()` clean), read the `.bin`, verify `sliceBytes` + `sliceSha256`, append to the payload, update a running SHA-256. Finally assert payload size + payload SHA-256, print payload path. The `.bin` members are raw concatenation slices of one `.tar.zst`.

**Recipe in one line:** `verify+concat the 6 .bin slices (in order) → one .tar.zst payload → verify payload SHA-256 → zstd -d → verify safe tar paths → untar → tools/validate_release.py checks PACKAGE_MANIFEST.sha256`.

**Payload facts (from `PARTS.yaml`/`reassemble.py` SPEC):**

| family | payload name | payload bytes | payload sha256 |
|---|---|---|---|
| consolidated | `graphatlas-epistemic0-consolidated-v17-2026-08-06.tar.zst` | 259,721,079 | `2f4cdc6d0e859771d363ea84d931abf3d8512c831d3005aca1a543bb7878c1ce` |
| semantic-formats | `graphatlas-epistemic0-semantic-formats-v17-2026-08-06.tar.zst` | 247,538,052 | `24cdf9e55c26fcc3889ca4b8bbefe3e03971d97502cc9726f8783406f9782733` |

Both payloads reassembled **successfully** (Python `reassemble.py` raises on any hash mismatch; both printed the payload path → all slice + payload hashes verified). Zstd-decompress + untar produced **509 members (consolidated)** and **476 members (semantic-formats)**.

Compression is declared a **transport choice, not a virtual identity model** (paper §Final Release Layout): "Materialization recreates ordinary AOB directories; compression is a transport choice."

---

## 3. Full materialized tree (from `find … | sort`; authoritative `TREE.txt` = 505 lines)

Root: `graphatlas-epistemic0-consolidated-v17-2026-08-06/`. Top-level sizes:

| dir | size | files | role |
|---|---|---|---|
| `xml/` | 515M | 22 | canonical XML, RDF/XML, GraphML, XMI + per-axis RDF |
| `ttl/` | 405M | 38 | canonical turtle, per-axis primary + membership graphs, basicttl canonical/source-index |
| `shacl/` | 243M | 66 | shapes (ttl+rdf), complete data graph, v16 shapes, fixtures, upstream suite |
| `linkml/` | 214M | 18 | schema.yaml + 16 per-axis instance shards + instance-index |
| `metadata/` | 465M | 71 | sqlite ledger, glossaries, crs-bindings, terms (primary/memberships), source-corpus |
| `geosparql/` | 2.1G | 126 | all-axis rebindings, 16 per-axis rebinding graphs, dataset/suite, 93 queries + 12 updates |
| `exports/` | 181M | 6 | uml(.puml), dot(.dot,.svg), graphml, xmi |
| `sparql/` | 276K | 63 | 10 custom queries + upstream suite (queries+updates) |
| `ossie/` | 8K | 1 | `semantic-model.yaml` |
| `native-runners/` | 84K | 12 | Jena 6.2.0 harness, python shacl runner, run-*.sh, pinned upstream, Containerfile |
| `schemas/` | 16K | 3 | JSON-Schema for term / term-collection / axis-membership |
| `serialization/` | 8K | 1 | serialization-profile.yaml |
| `validation/` | 48K | 4 | FINAL_VALIDATION, streaming, release summary, yaml-contract |
| `source-packets/` | 31M | 3 | `basicttl(2).zip`, `scripts(2).zip`, `urn-algebra-nomenclature.md` (consolidated only) |
| `paper/` | 628K | 3 | PDF + LaTeX source zip + PDF render validation (consolidated only) |
| `lineage/` | 36K | 3 | v16 README/summary/manifest (consolidated only) |
| `epistemic0/` | 12K | 2 | `epistemic0.yaml`, `projection-algebra.yaml` |

Projection family dirs requested by the task **all present**: `ttl/ geosparql/ shacl/ linkml/ ossie/ xml/ sparql/ metadata/` plus `exports/{uml,dot,graphml,xmi}` and `native-runners/` (Jena native). Per-axis fan-out is uniform: every one of the **16 named axes** gets its own file under `ttl/primary-axes/`, `ttl/axis-memberships/`, `geosparql/axis-rebindings/`, `xml/axes/`, `linkml/instances/`, `metadata/terms/primary/`, `metadata/terms/memberships/`, `metadata/source-corpus/{basicttl,scripts}/`.

**Consolidated vs semantic-formats:** both are full parallel builds over the same 104,848 identities. Manifest diff: 456 vs 434 files; **433 shared paths, of which 431 are byte-identical sha256**; the only 2 differing shared files are `TREE.txt` and `PACKAGE_SUMMARY.yaml` (each describes its own package). Consolidated adds 23 provenance/native/paper/lineage/source-packet files; semantic-formats adds only `README_SEMANTIC_FORMATS.md`. → strong evidence of **deterministic, reproducible materialization** of the projection plane across two independent builds.

---

## 4. Full reads: dataset descriptors, native runners, sqlite schema, projection samples

### 4.1 `geosparql/dataset.yaml` (GeoSparqlDataset)
- `completeRebindingGraph: graphatlas-epistemic0-all-axis-rebindings.ttl`; `axisRebindingPattern: axis-rebindings/*.ttl`
- `namedAxisCount: 16`, `canonicalIdentityCountPerAxis: 104848`, `totalCRSRebindingCount: 1677568`
- `crsBindingLaw`: "selected Atlas Glossary binds its semantic CRS; selection changes chart, not canonical identity"; `geodeticClaim: false`
- `geosparql/suite.yaml`: normativeTarget **GeoSPARQL 1.1 project profile**, 93 query files + 12 update files, 0 placeholders, `nativeUpstreamAcceptance: fail-closed`.

### 4.2 Native Jena 6.2.0 runners (`native-runners/`)
- `README.md`: runners are the *only* mechanism to promote `BLOCKED_EXTERNAL_NATIVE_RUNTIME` → upstream-native certificate; fresh isolated envs, record resolved versions/commits, **exit nonzero on any missing tool, skipped test, zero-test run, or failed assertion**. Receipts under `validation/native/`, then `tools/seal_native_certificate.py` (refuses PASS unless all mandatory receipts present+successful). *(sealer script referenced but not shipped in this package — PROVISIONAL: promotion tooling is external.)*
- `run-all-native.sh`: sequentially runs linkml → shacl → jena-geosparql → ossie → `tools/seal_native_certificate.py`.
- `run-jena-geosparql-6.2.0.sh`: **`git clone --depth 1 --branch jena-6.2.0 https://github.com/apache/jena.git`** and `--branch geosparql-1.1 …/opengeospatial/ogc-geosparql.git`; records HEAD commits; `mvn -f jena/pom.xml -pl jena-shacl -am test`; then `mvn -f native-runners/jena-harness/pom.xml -Dgraphatlas.root=$ROOT clean test`. A Python post-step parses `surefire-reports/TEST-*.xml` and asserts `tests>0 and failures==0 and errors==0 and skipped==0`, writes `receipt.json` (planes: ARQ SPARQL, SHACL, GeoSPARQL, TDB2, Fuseki).
- `jena-harness/pom.xml`: `groupId silmaril / artifactId graphatlas-native-conformance / version 16`, `maven.compiler.release 21`, `jena.version 6.2.0`; deps jena-arq, jena-shacl, jena-geosparql, jena-tdb2, jena-fuseki-main + junit-jupiter 5.13.4; surefire `failIfNoTests=true`, passes `-Dgraphatlas.root`.
- `GraphAtlasNativeConformanceTest.java` (JUnit5) — **what it queries**: loads `conformance/data/atlas-suite.ttl`; 4 tests: (1) SHACL conforming+negative fixtures (`negative-*` must NOT conform); (2) ARQ SPARQL + GeoSPARQL: walks `conformance/{sparql,geosparql}/queries` `.rq/.ru`, `assertTrue(files.size() >= 80)`, executes each (select/ask/construct/describe); (3) TDB2 persistence + `SELECT (COUNT(*) …)`; (4) Fuseki endpoint round-trip `ASK { ?s ?p ?o }` on port 0.
- `PINNED_UPSTREAM.json`: LinkML **1.11.1**, pySHACL **0.40.1**, W3C data-shapes gh-pages, Apache Jena **6.2.0** (+ zip SHA-512s), OGC GeoSPARQL 1.1 branch `geosparql-1.1`, Apache Ossie `main` (`core-spec/osi-schema.json`, `validation/validate.py`).
- `run-linkml-1.11.1.sh`: venv → `pip install 'linkml==1.11.1'` → `linkml-lint`, `linkml-validate`, `gen-json-schema`, `gen-shacl`, `gen-owl`, `gen-jsonld-context`; asserts installed version==1.11.1.
- `run-shacl-processors.sh`: `pyshacl==0.40.1` + clones W3C data-shapes (gh-pages) and pySHACL v0.40.1 source, runs pytest, then project fixtures via both **pyshacl** and **Jena** (`$JENA_HOME/bin/shacl`); both receipts must be `PASS` with `test_count>0`.
- `run-ossie-main.sh`: clones `apache/ossie main`, records HEAD, validates `conformance/ossie/semantic-model.yaml` against `core-spec/osi-schema.json` via `validation/validate.py` + jsonschema Draft2020-12.
- `python/run_shacl_conformance.py`: project fixtures (`negative-*` ⇒ expect non-conformance) + parses every `.ttl` under W3C `data-shapes-test-suite/tests` and `shacl12-test-suite/tests`; note: W3C suite has no universal runner, so full execution deferred to each processor's own source suite (marker `PROCESSOR_SOURCE_SUITE_REQUIRED_BY_CONNECTED_RUNNER`).

### 4.3 `metadata/atlas-metadata.sqlite` — schema (`.schema`)
```sql
CREATE TABLE terms(source_sha256 TEXT PRIMARY KEY, identity_urn TEXT, exact_urn TEXT,
  surface TEXT, glossary_urn TEXT, crs_urn TEXT, x INTEGER, y INTEGER, z INTEGER,
  status TEXT, source_plane TEXT, source_planes TEXT, candidate_glossaries_json TEXT);
CREATE INDEX idx_terms_glossary ON terms(glossary_urn);
CREATE INDEX idx_terms_surface  ON terms(surface);
```
Single table `terms`, **104,848 rows** (one per canonical identity, in its *primary* axis projection). `tools/rebind_axis.py` reads x,y,z from this table and emits `<crs> POINT Z (x y z)`; `tools/query_epistemic0.py` gives `stats/axis/search/term`.

### 4.4 Projection format samples (one representative each)
- **ttl** (`ttl/graphatlas-epistemic0.ttl`, 249.6MB, 2.34M lines): each identity → `e0:Projection, ga:Epistemic0Term` with `e0:projectsFrom` (packet URN), `e0:projectsTerm`, `e0:exactUrn`, `e0:surface`, coordinates, relationUrn.
- **geosparql** (`geosparql/axis-rebindings/geospatial-topology.ttl`): `<term> geo:hasGeometry <geom>`; `<geom> a geo:Geometry, e0:SemanticAxisGeometry ; e0:axis <…glossary:geospatial-topology> ; e0:boundCRS <…crs…:v16> ; geo:asWKT "<…crs…:v16> POINT Z (5 1 0)"^^geo:wktLiteral`. The all-axis graph `graphatlas-epistemic0-all-axis-rebindings.ttl` = 1.06GB, ~10.06M lines (≈6 lines × 1.68M rebindings).
- **shacl** (`shacl/epistemic0-shapes.ttl`): `e0:Epistemic0TermShape sh:targetClass e0:Projection` with min/max cardinalities on projectsFrom, primaryAxis, candidateAxis, boundCRS, coordinateX/Y/Z (xsd:integer), and `e0:relationUrn` `sh:pattern "@.*;.*!$"`. `e0:GlossaryShape` requires `atlas:hasCRS`.
- **linkml** (`linkml/schema.yaml`): LinkML schema `graphatlas_epistemic0` v17.0.0, Apache-2.0. tree_root `Epistemic0Corpus{glossaries[],terms[]}`; classes `AtlasGlossary`, `AxisDefinition{ordinal,name,unit,meaning}`, `Epistemic0Term` (identifier `source_sha256` pattern `^[0-9a-f]{64}$`, x/y/z integer, relation_urn, candidate_glossaries[]). Instances sharded per axis under `linkml/instances/`.
- **ossie** (`ossie/semantic-model.yaml`): Apache Ossie `version 0.2.0.dev0`; datasets `epistemic0_terms` (from `metadata/terms/primary/*.yaml`), `atlas_glossaries`, `axis_memberships`; relationships many_to_one; metrics `term_count/axis_count/polyaxial_term_count`; `ai_context` = "Treat projections as epistemic0 views over one carrier … Preserve the full relation_urn MAP and derive S:P:O only as rank-zero REDUCE"; `custom_extensions.silmaril` points to urn-grammar, crs-bindings, projection-algebra.
- **xml** family: `.xml` (custom `e0:corpus/e0:term`), `.rdf` (RDF/XML `rdf:Description`), `.graphml` (keyed node/edge attrs kind/label/urn/axis/crs/role/x/y), `.xmi` (`xmi:XMI`/`ga:EpistemicModel` with `<glossary>` elements).
- **uml** (`exports/uml/epistemic0.puml`): `@startuml` classes `CanonicalAOB{identityUrn,exactUrn,relationUrn MAP,rankZeroReduce S:P:O}`, `Epistemic0Projection`, `AtlasGlossary`, `DynamicCRS`.
- **dot** (`exports/dot/epistemic0-axes.dot`): `digraph axes` with `epistemic0 -> <slug> [label="<n> primary"]` for all 16 axes (general-ontology `0 primary`). Also `exports/dot/epistemic0-full.dot` + rendered `.svg`.
- **sparql**: `sparql/queries/001-axis-count.rq` = `SELECT (COUNT(DISTINCT ?axis) …)`; `geosparql/queries/002-dynamic-crs-rebinding.rq` = `CONSTRUCT` that BINDs `STRDT(CONCAT('<',STR(?crs),'> POINT Z (',x,' ',y,' ',z,')'), geo:wktLiteral)` — i.e. runtime CRS rebinding straight from the x/y/z coordinates.

---

## 5. The algebra — v17 counts (with provenance) and the coordinate rule

### 5.1 Counts (each with source)

| quantity | value | source |
|---|---|---|
| **Canonical identities** (ontic0 self carriers) | **104,848** | AXIS_COVERAGE, PACKAGE_SUMMARY, epistemic0.yaml, sqlite `count(*)=104848`, terms/index.yaml |
| distinct identities | 104,848 | AXIS_COVERAGE (`distinctIdentityCount`) |
| **Named Atlas Glossary axes** | **16** | PACKAGE_SUMMARY `namedAxisCount`, glossaries registry `glossaryCount:16` |
| primary axes (axes actually chosen as primary) | **15** | epistemic0.yaml `primaryAxisCount:15` (general-ontology is universal cover only → 0 primary) |
| candidate axis memberships | 246,910 | AXIS_COVERAGE `candidateMembershipCount` |
| memberships incl. universal cover | 351,758 | = 246,910 + 104,848 (PACKAGE_SUMMARY) |
| **All-axis glossary/CRS rebindings** | **1,677,568** | PACKAGE_SUMMARY `allAxisCRSRebindingCount`, geosparql/dataset.yaml `totalCRSRebindingCount` = 104,848 × 16 (arithmetic checks) |
| all-turtle statements | 29,365,945 | FINAL_VALIDATION `allTurtleStreaming.statementCount` (117 files, 3.12GB) |
| ttl triples (validated subset) | 4,279,572 | FINAL_VALIDATION `ttl.tripleCount` |
| source files (basicttl+scripts) | 39,678 | FINAL_VALIDATION (`30,224` basicttl + `9,454` scripts) |
| union arithmetic | 68,445 + 36,404 − 1 = 104,848 | paper §Final Source-Packet Integration |
| source planes | baseline 68,444 / packet 36,404 | epistemic0.yaml `sourcePlaneCounts` |
| admission status | baseline-sealed 68,444 / admitted-candidate 36,392 / held-explicit 12 | epistemic0.yaml `admissionStatusCounts` |

Per-axis primary counts (epistemic0.yaml): urn-calculus **62,160**, document-corpus 24,281, software-languages 7,296, graphatlas-runtime 5,779, schema-validation 2,470, biological-taxonomy 1,256, storage-formats 616, hardware-compute 431, predictive-world-model 275, icarus-ide 96, identity-security 75, execution-effects 42, distributed-network 37, geospatial-topology 23, economics-game-theory 11, general-ontology 0.

### 5.2 Coordinate rule — CONFIRMED (brute-forced against all 104,848 sqlite rows, **zero mismatches**)

Source of the rule (identical in `metadata/crs-bindings.yaml`, `metadata/atlas-glossaries.yaml`, `linkml/instance-index.yaml`; every one of the 16 CRSs shares the same 3 axes):
- axis 0 **lexical-depth** — "count of lexical/path segments in exact URN" (unit segment-count)
- axis 1 **operator-degree** — "maximum N-grade among `:`, `#`, `@`, `;`, `!`" (unit maximum-glyph-run)
- axis 2 **digest-ordinal** — "first two source-digest octets interpreted as an integer" (unit unsigned-16-bit)

Empirical confirmation over the full `terms` table (recomputed x/y/z from `exact_urn`/`source_sha256`, compared to stored):

- **x (lexical depth)** = number of **non-empty** segments splitting `exact_urn` on the delimiter class **`[ : / # @ ; , ]`** (consecutive delimiters collapse). **0 mismatches / 104,848.** Refinement vs task's stated rule: the task listed `: / # @ ; ,` — confirmed exactly — with the note that runs collapse, so a `::` (double colon) counts as **one** boundary, not two (e.g. `urn:avogadro:func:duckdb::duckdb_data_chunk_to_arrow` → x=5, not 6).
- **y (operator degree)** = longest run of a single glyph among **`: # @ ; !`**. **0 mismatches / 104,848.** Exactly the task's set. Max y observed in the corpus = **2** (from `::` type-ascription URNs like `…:func:fixture::ldap_dn_new_user`). Note `/` and `,` count for depth (x) but **not** degree (y); `!` counts for degree but not depth.
- **z (digest ordinal)** = `int(source_sha256[:4], 16)` = big-endian uint16 of the **first two octets of the term's `source_sha256`**, range 0–65535. **0 mismatches / 104,848** (e.g. `00f6…`→246, `0129…`→297, `07cb…`→1995).
  - *Precision vs task wording:* the digest is the SHA-256 of the **source term content** (`source_sha256`), which the identity_urn embeds as `…:sha256:<that hash>`. It is **not** a fresh SHA-256 computed over the `exact_urn` string. Effect is the task's "first two SHA-256 octets of the identifying URN's digest"; the load-bearing detail is *which* digest (the source/identity digest).

**Verdict: coordinate rule CONFIRMED**, with the two precisions above (delimiter-run collapsing for x; source-digest for z).

---

## 6. The AOB — atom-yml schema, base_templates, projection derivation

> Note on the expansion. "AOB" is used throughout this corpus, but its expansion is **not stated anywhere in `forge/example_gippidy_01`**: `grep -rE 'Atom.of.Being' forge/example_gippidy_01` = 0 hits. [inference] plausibly *Atom-of-Being* (consistent with the paper's atom / ontic0-carrier framing), marked as inference — **not asserted as fact**. Census gap 30 holds the cross-map disagreement open: `ledger/W1/base_templates.md` §Orientation reads the same acronym as *Atom-Oriented-Bundle*, itself unsourced in its own corpus.

### 6.1 Physical AOB normal form (paper §"Complete AOB Normal Form and Projection Closure")
Every new exact identity gets a content-addressed directory keyed by SHA-256 nibbles:
```
aob-render/<h0h1>/<h2h3>/<sha256>.aob.dir/
  atom.spec.yaml                         # authoritative SELF carrier (byte-identical to .project/self copy)
  .project/manifest.yaml
  .project/self/atom.spec.yaml
  .project/shacl/{atom.spec.yaml,shapes.ttl,data.ttl}
  .project/linkml/{atom.spec.yaml,schema.yaml,instance.yaml,transform.yaml}
  .project/ossie/{atom.spec.yaml,semantic-model.yaml}
  .project/geosparql/{atom.spec.yaml,profile.ttl,data.ttl}
  .projections/index.yaml
```
**Strict all-AOB closure revision** (final, sealed by union digest `940f5ef8290ac81397cab6023c31e1600658544d7519440b7331ea9a147fcd47`) makes every one of the 104,848 identities materialize the *same* contract, adding sparql / exports / native legs:
```
atom.spec.yaml
PACKAGE_MANIFEST.sha256
.project/manifest.yaml
.project/self/atom.spec.yaml
.project/shacl/{atom.spec.yaml,shapes.ttl,data.ttl}
.project/linkml/{atom.spec.yaml,schema.yaml,instance.yaml,transform.yaml}
.project/ossie/{atom.spec.yaml,semantic-model.yaml,validation.json}
.project/geosparql/{atom.spec.yaml,profile.ttl,data.ttl,queries.rq}
.project/sparql/{atom.spec.yaml,queries.rq}
.project/exports/{model.puml,model.dot,model.graphml}
.project/native/acceptance.json
.projections/index.yaml
```
Coverage is a **total function** `P : A → ∏_{L∈L} Artifact_L` over lenses L = {self, SHACL, LinkML, Ossie, GeoSPARQL, SPARQL, UML, DOT, GraphML, native-acceptance}; the manifest gate **rejects any atom for which P(a) is partial**. The AOB file name constant is confirmed in the repo: `scripts/python/pylib/reference/…/config/constants/aob/layout/{root-spec,projection-document}/value.py` both = **`atom.spec.yaml`**.

### 6.2 The `atom.spec.yaml` reference schema (paper §"Reference Atom Schema", verbatim abridged)
```yaml
atom:
  identity:        {urn, revision, carrier_digest}
  symbolic_state:
    hypergraph:    {nodes, hyperedges, arrow_nodes}
    relation_map:  {full_relation_urn: <MAP>, rank_zero_reduce: {subject, predicate, object}}
  topology:
    site:          {charts, covers, overlaps}
    sheaf:         {section_schema, sections, restriction_maps, gluing_status, obstructions}
  dynamics:        {rewrite_rules, candidate_matches, selected_rewrite, composition_spine}
  latent:          {encoder_revision, predictor_revision, context/target/predicted/observed_section, residual}
  valuation:
    semiring:      {kind: pareto-antichain-product,
                    dimensions: [confidence, freshness, authority, reversibility, volatility, cost]}
    candidate_weights, nondominated_frontier
  execution:       {effect_plan, runtime_evidence, error_channel, retries}
  receipt:         {observation_digest, rewrite_digest, prediction_digest, result_digest, law_checks}
```
The **released** per-term projection of this carrier (what actually ships, as `metadata/terms/*/*.yaml`, sqlite, and the LinkML/JSON schemas) is the flattened `Epistemic0Term`: `sourceSha256, identityUrn, epistemic0Urn, termUrn, exactUrn, surface, primaryGlossary, boundCrs, coordinates{x,y,z}, admissionStatus, sourcePlane(s), relationUrn, rankZeroReduce{subject,predicate,object}, candidateGlossaries[]`. JSON-Schema `schemas/epistemic0-term.schema.yaml` enforces `relationUrn` pattern `@.*;.*!$`.

**The full relation_urn MAP** (observed verbatim in `xml/graphatlas-epistemic0.xml` and `metadata/terms/primary/*.yaml`) — one curried λ-tower per identity:
```
urn:silmaril:relation:<identityUrn>
  @urn:silmaril:relation:denotes@urn:silmaril:lexeme:sha256:<h>
  @@urn:silmaril:relation:classified:by@urn:silmaril:atlas:glossary:<axis>
  @@urn:silmaril:relation:bound:to@urn:silmaril:crs:atlas-glossary:<axis>:v16
  ;urn:silmaril:relation:projected:as@urn:silmaril:epistemic:0
  ;urn:silmaril:relation:materialized:as@urn:silmaril:projection:family:self-shacl-linkml-ossie-geosparql-sparql-xml-uml-dot-graphml-native
  ;urn:silmaril:relation:is:a@urn:silmaril:type:relation
  ;urn:silmaril:relation:is:a@urn:silmaril:type:type!
```
Its **rank-zero REDUCE** = `(identityUrn, urn:silmaril:relation:denotes, urn:silmaril:lexeme:sha256:<h>)` — exactly the paper's `(a_u, denotes, lexeme(h))`. This is the taiji: MAP (the long curried eigenvector tower) is authored/sealed; S:P:O REDUCE is `cata(projection-algebra)` read off on demand (per `source-packets/urn-algebra-nomenclature.md`, read in full — the operator table `: # :: @ @@ ; !` with precedence `; < @@ < @ < :: < # < :`).

### 6.3 `base_templates` macros — how they power the AOB *(PARTIAL / PROVISIONAL — not inside this corpus package)*
`base_templates` is **not a literal string in the corpus package**; it is a sibling submodule `forge/base_templates` (per repo `JUNGLE_MAP.md`, `PLAN_FREEZE.md`, `STRICTNESS_RULES.md`). It is a **Jinja2/HEEx typed component grammar** = the intended codegen engine that renders atoms/projections:
```
templates/_universal_macros.j2          # hub — imports all registries
templates/_registries/                  # per-concern macro files
templates/_urn/identity.j2              # URN identity stamping
templates/_urn/stamps.j2                # provenance stamps
templates/_canon/dewey_template_contract.j2   # path (Dewey :-depth) law
templates/heex/_anchors/_macros/_spine.heex.j2  # THE component grammar (macros: header/section/table/svg/mount)
templates/semantic_render_target.j2     # provenance-row contract
```
"StrictUndefined. Composition only (no inheritance)." Repo plan (PLAN_FREEZE goal 3): "Map component classes to base_templates HEEx macros (ontology-first) … Wire base_templates HEEx macros as the codegen engine" and "GeoSPARQL-driven renderer using forge/base_templates". **PROVISIONAL:** the exact wiring (atom.spec.yaml → base_templates macro → each projection artifact) is *specified as intent in the repo plan*, not demonstrated inside `example_gippidy_01`; the corpus ships the already-materialized projection outputs, not the template invocation trace. `example_gippidy_01` is the **reference target** the base_templates codegen must reproduce.

### 6.4 How each projection derives from an AOB — the projection algebra (`epistemic0/projection-algebra.yaml`, paper §"Parallel Projection Algebras")
Each lens is a **catamorphism over one carrier**: `π_L = cata(α_L) : Self → L`, with a **partial retraction** `ρ_L : L ⇀ Self` recovering only what the lens represents; pairwise translation factors through self: `η_{A→B} = π_B ∘ ρ_A`. Information order `Self ⪰ π_L(Self)`. Named algebras: ttl, shacl, sparql, geosparql, xml, linkml, ossie (each `fold: cata(<lens>_algebra)`). Every projection receipt assigns **one of five loss classes**: `exact / structural / approximated / externalized / dropped`. Lens authorities & principal losses (paper Table): Self = canonical identity + bytes + rewrite topology + evidence (no loss by definition); SHACL = RDF constraints (loses learned dynamics, rewrite algebra); LinkML = classes/slots/instances (loses advanced SHACL paths, predictors); Ossie = analytical semantic model (loses higher morphisms, sheaf restrictions); GeoSPARQL = spatial vocab + WKT POINT Z in an **explicitly abstract CRS** (loses non-spatial dynamics; must NOT be read as Earth geography).

---

## 7. The `materialized:as` projection vocabulary & split↔consolidated reversibility

### 7.1 Vocabulary
- `epistemic0/epistemic0.yaml` `nativeProjectionFamily` (12): **self, shacl, linkml, ossie, geosparql, sparql, ttl, xml, uml, dot, graphml, native** — matches the task's requested set exactly.
- The `relation_urn` `materialized:as` slug embeds **11** legs: `self-shacl-linkml-ossie-geosparql-sparql-xml-uml-dot-graphml-native`. **Discrepancy (honest):** the URN slug **omits `ttl`** and the strict-all-AOB paper contract lists `{self, shacl, linkml, ossie, geosparql, sparql, uml, dot, graphml, native}` (also no standalone `ttl`, since ttl is the RDF serialization shared by shacl/geosparql). So: `ttl` is a projection family dir + a named algebra, but it is folded under the RDF-carrying legs in the URN materialized-family slug. Not a fabrication either way — recorded as observed.

### 7.2 How each is produced
- **self** = the immutable `atom.spec.yaml` (ontic0 canonical carrier); all others are `cata` folds over it.
- **ttl / xml / rdf / graphml / xmi** = serialization folds (`cata(ttl_algebra)`, `cata(xml_algebra)`); one canonical whole-corpus file each plus per-axis shards.
- **shacl** = `cata(shacl_algebra)` → shapes graph + complete data graph (`shacl/graphatlas-epistemic0-data.ttl`, sha256 recorded in FINAL_VALIDATION, `matchesCanonicalTurtle: true`).
- **linkml** = `cata(linkml_algebra)` → portable schema + 16 instance shards; native gen-{json-schema,shacl,owl,jsonld-context} in the promotion runner.
- **ossie** = `cata(ossie_algebra)` → analytical semantic-model.yaml over primary-axis yaml.
- **geosparql** = `cata(geosparql_algebra)` → 16 per-axis rebinding graphs + 1 all-axis graph; WKT `POINT Z (x y z)` from the CRS-bound coordinates; runtime rebinding via SPARQL CONSTRUCT `002-dynamic-crs-rebinding.rq`.
- **sparql** = query/update surface (10 custom + upstream suite).
- **uml/dot/graphml** = `exports/` diagram folds.
- **native** = fail-closed acceptance certificate (Jena 6.2.0 / LinkML 1.11.1 / pySHACL 0.40.1 / Ossie main), only from real upstream execution; never inferred from runner presence (paper Prop. "No presence-to-conformance promotion": a runner artifact `r` without an execution receipt `e` binding executable-revision/input-digests/command/exit-status/output-digest cannot derive conformance).

### 7.3 Split ↔ Consolidated reversibility (how it holds here)
Two senses in play, both grounded:
1. **Distribution-level split↔consolidated (this package):** the corpus is transported as **split ZIP slices** and reassembled to a **consolidated** `.tar.zst` → directory tree, gated by a chain of content-addressed digests (zip → slice → payload → internal `PACKAGE_MANIFEST.sha256`). The Split↔Consolidated render seal (unary-byte-frame-law §"Split and Consolidated Render Seal") requires `consolidate(split(graph))==graph` and `split(consolidate(graph))==split(graph)` with equal topology/content/byte-revision/identity/relationship digests. **Empirical support:** the two independent full builds (consolidated vs semantic-formats) agree byte-for-byte on **431/433 shared projection+data files** (only their self-describing `TREE.txt`/`PACKAGE_SUMMARY.yaml` differ) → deterministic, reproducible materialization.
2. **Projection-level reversibility (the colimit):** MAP `relation_urn` ⇄ REDUCE `S:P:O` is a reversible pair — the flat triple is recoverable at any time by `cata(projection-algebra)`, and the released `rankZeroReduce` is exactly that recovery; `ρ_L` retracts each lens back toward self. **Atlas (the axis/CRS charts) and Graph (the relation topology) colimit each other through this pair** — neither the split projections nor the consolidated carrier may invent, erase, or silently rename a coordinate (canonical identity is never mutated by CRS selection: `crsBindingLaw`, and `canonicalIdentityMutated: False` in `rebind_axis.py` receipts).

**PROVISIONAL:** the byte-complete inverse renderers and drift-free recapture certificates named by the unary law are **not shipped as executable tools inside this package** (this package is the materialized *output* + validators, not the split/consolidate render engine). The reversibility is evidenced here by cross-build digest equality and the MAP/REDUCE structural pair, not by an in-package `split()`/`consolidate()` executable. Consistent with the law's own status: "active red migration; the law is specified, but the enforcement implementation does not yet satisfy the law."

---

## 8. Validation status (as shipped)

`validation/FINAL_VALIDATION.yaml` status **PASS** for: yaml (99 docs), ttl (36 files, 4,279,572 triples), geo (16 axes × 104,848), xml (21 files), sparql (143 queries + 22 updates), corpus cardinality (104,848 distinct), axisCoverage (0 missingPrimaryAxis / 0 missingCRS / 0 malformed), shaclDistribution (`matchesCanonicalTurtle: true`), allTurtleStreaming (117 files, 29,365,945 statements, 3.12GB). **Native/upstream acceptance is explicitly `BLOCKED_EXTERNAL_NATIVE_RUNTIME` / fail-closed** (`geosparql/upstream-project-suite/validation.json` → `exact_native_jena.status: BLOCKED_EXTERNAL_RUNTIME_UNAVAILABLE`, version 6.2.0). PACKAGE_SUMMARY status PASS; `nativeAcceptance: fail-closed external gate`. Serialization: YAML 1.2 block, UTF-8 no-BOM, LF, 2-space, tab-free, no JSONL (the retired `terms.jsonl` defect).

---

## 9. Praeriehund ledger — items held PROVISIONAL (not fabricated)

- `tools/seal_native_certificate.py` referenced by runners but **not shipped** in this package → promotion sealer is external. PROVISIONAL.
- `base_templates` HEEx codegen wiring → intent per repo plan; not demonstrated in-package (corpus is the reference target). PARTIAL.
- In-package `split()`/`consolidate()` render engine + inverse certificates → not shipped; reversibility inferred from cross-build digest equality + MAP/REDUCE pair. PROVISIONAL.
- `materialized:as` URN slug (11 legs, no `ttl`) vs `nativeProjectionFamily` (12, with `ttl`) vs paper contract (10) → three consistent but non-identical enumerations; recorded verbatim, not reconciled by fiat.
- `.aob.dir/` physical directories are the *paper's* normal form; this distribution ships the **corpus-wide projection plane** (per-axis shards + whole-corpus graphs), not one directory per atom. The two are the same carrier at different granularities. Noted, not conflated.

---

### Provenance of numbers (quick map)
104,848 / 16 / 246,910 / 351,758 / 1,677,568 → PACKAGE_SUMMARY + AXIS_COVERAGE + epistemic0.yaml + terms/index.yaml (cross-agree). 29,365,945 statements + 4,279,572 triples + 39,678 source files → FINAL_VALIDATION. Coordinate rule → crs-bindings.yaml/atlas-glossaries.yaml + brute-force over sqlite (0 mismatches). AOB schema + closure → paper.tex (source-packets paper zip). Reproducibility → PACKAGE_MANIFEST.sha256 diff across the two builds.
