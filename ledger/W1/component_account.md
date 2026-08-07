# W1 Task 4 — Complete-Component-Account SEED

Author: W1 account (Task 4). Frame date: `2026-08-07`. Scope: read-only account over the
seven frozen whole trees in `ledger/W1/trees/`, the Task-3 census
(`ledger/W1/taxonomy_census.md`), the five committed W1 maps, and the three beacon rulings
(`JUNGLE_MAP.md`, `PLAN_FREEZE.md`, `STRICTNESS_RULES.md`).

Doctrine read in full first, per Global Constraint 1:
`docs/praeriehund-demokratie-der-kategorien.md` (129 lines) +
`docs/unary-byte-frame-law.md` (765 lines).

This document is the human-readable account. Its machine projection onto the frozen row
universe is `ledger/W1/account/GENERATOR.sh`, which emits `account/silmaril.csv` and
`account/forge.csv` (header + one row per tree path, columns
`path,component_family,disposition,successor_hint,inverse_evidence,provisional_gap`). The
acceptance gate is `ledger/W1/checks/account-check.sh`.

---

## 0. Governing law (verbatim anchors)

The disposition vocabulary is **closed** and is quoted from the doctrine's *Complete
Component Account* (`docs/unary-byte-frame-law.md`):

> - disposition: reuse, migrate, split, merge, retire, conflict, or provisional;
> - successor identity and inverse evidence.

and the deletion / provisional law that binds every `retire` and every `provisional` row:

> No label such as `duplicate`, `neglected`, or `unnecessary` authorizes deletion.
> A duplicate requires identity and denotation evidence; a retirement requires consumer
> closure plus a byte-complete inverse; an unresolved meaning remains provisional.

Präriehund honesty (`docs/praeriehund-…`): a new/unresolved thing is marked provisional with
its gap named, **not** force-fit into a known bin —
> Der Funktor zur bestehenden Linnéschen Taxonomie wäre als *partiell* deklariert worden … Das
> System hätte die Lücke dokumentiert, nicht kaschiert.

`split` and `consolidate` are **not** used as dispositions here: the doctrine reserves those
words for the reversible whole-graph render seal (*Split and Consolidated Render Seal*), not
for per-file lifecycle. Every row therefore carries one of
`reuse | migrate | retire | merge | provisional`. `conflict` is defined and available but
**no row needed it** — every path classified to a governed family (§2 confirms zero
`UNCLASSIFIED`/`conflict`).

---

## 1. Method

1. **Row universe = the seven frozen trees, whole.** Cardinalities computed this session by
   `wc -l` and cross-checked against the census: `silmaril` 6,333 · `basicttl` 30,234 ·
   `base_agents` 279,670 · `base_templates` 1,118 · `base_tower` 50 · `example_gippidy_01` 16
   · `superpowers` 180 = **317,601**. No path is read into context to be classified; the
   committed tree file **is** the complete transcription, and classification is a
   prefix-keyed projection computed over the entire file (`sed`/`cut`/`grep`/`awk`), never a
   capped or sampled read.

2. **CSV split matches the acceptance check.**
   `silmaril.csv` ← `silmaril.tree` (paths start `./`) + `basicttl.tree` (paths start
   `basicttl/`). `forge.csv` ← `base_agents.tree` + `base_templates.tree` + `base_tower.tree`
   + `example_gippidy_01.tree` + `superpowers.tree` (paths start `forge/` or `external/`).

3. **`component_family` per path is derived from the census taxonomy rows**, drilled to the
   granularity at which the disposition is uniform. Where the census/beacons rule a subtree
   differently from its parent region, the subtree gets its own family (first-match-wins,
   most-specific prefix first).

4. **Disposition is ruled at family granularity** with a governing citation (census row,
   beacon ruling, or doctrine clause). Family-uniform dispositions are ruled once for the
   whole family; genuinely non-uniform points are carved out as their own family or
   enumerated as exceptions (§8).

5. **Generation is programmatic.** One `awk` classifier keyed on the verbatim path prefix
   emits one row per tree line, so no path can be dropped and every path appears exactly
   once. CSV safety: tree paths contain **no commas** (verified, §2) and the generator emits
   no comma inside any field (uses `;` `/` `+`), so `cut -d, -f1` recovers the path verbatim
   and every row has exactly 6 fields (verified, §2). Because no path contains a comma, no
   switch to tab-delimited was needed.

6. **`retire` ⇒ inverse.** Per Präriehund "no delete without inverse", every `retire` family
   fills `inverse_evidence` with the byte-complete inverse that *exists or must exist* before
   deletion (§6).

7. **`provisional` ⇒ named gap.** Reserved for the genuinely undecidable-before-W2, never the
   tedious; each provisional row fills `provisional_gap` and each is **inherited from the
   frozen census Honest-gap register**, not minted here to dodge resolvable work (§7).

---

## 2. Row universe and CSV integrity (the acceptance basis)

Computed this session over the whole files:

| file | data rows | = tree lines |
|---|---:|---|
| `account/silmaril.csv` | **36,567** | 6,333 + 30,234 |
| `account/forge.csv` | **281,034** | 279,670 + 1,118 + 50 + 16 + 180 |
| **total** | **317,601** | `cat trees/*.tree \| wc -l` |

- Comma scan across all seven trees: **zero** lines contain a comma.
- Field-count scan: **zero** rows with `NF != 6` in either CSV.
- Disposition column (`cut -d, -f3 | sort -u`): exactly `{merge, migrate, provisional, retire,
  reuse}` — all inside the closed vocabulary; **no `UNCLASSIFIED`, no `conflict`**.
- `account-check.sh` diff of CSV column-1 (sorted) against the sorted tree paths: **empty**
  (every tree path has exactly one row; every row maps to a real tree path).

---

## 3. Statistics

### 3.1 Rows per disposition

| disposition | silmaril.csv | forge.csv | total |
|---|---:|---:|---:|
| reuse | 35,695 | 277,626 | **313,321** |
| migrate | 68 | 3,408 | **3,476** |
| retire | 710 | 0 | **710** |
| provisional | 93 | 0 | **93** |
| merge | 1 | 0 | **1** |
| conflict | 0 | 0 | **0** |
| **total** | **36,567** | **281,034** | **317,601** |

### 3.2 Rows per family (37 families: 29 silmaril + 8 forge)

**silmaril.csv (29):**

| family | disp | rows |
|---|---|---:|
| basicttl/ontology-source | reuse | 30,233 |
| silmaril/engine/sparky-live-src | reuse | 5,193 |
| silmaril/engine/build-and-verification | reuse | 223 |
| silmaril/ledger/audit-record | reuse | 16 |
| silmaril/engine/live-receipts-config | reuse | 7 |
| silmaril/root/governance-doc | reuse | 6 |
| silmaril/keys/pgp-trust-root | reuse | 4 |
| silmaril/docs/working-notes | reuse | 4 |
| silmaril/shell/lawful-launcher | reuse | 3 |
| silmaril/root/repo-config | reuse | 2 |
| silmaril/docs/doctrine | reuse | 2 |
| silmaril/ontology-dir/readme | reuse | 1 |
| silmaril/hooks/readme | reuse | 1 |
| silmaril/engine/legacy-reference-copy | retire | 692 |
| silmaril/site/generated-artifact | retire | 6 |
| silmaril/site/jekyll-scaffold | retire | 5 |
| silmaril/ontology-dir/generated-artifact | retire | 5 |
| silmaril/ontology-dir/orphaned-generated | retire | 1 |
| silmaril/keys/generated-manifest | retire | 1 |
| silmaril/engine/sparky-reserved-keyword-lambda-twin | provisional | 66 |
| silmaril/engine/legacy-reference-aob-layout | provisional | 27 |
| silmaril/engine/outside-pylib-python | migrate | 50 |
| silmaril/shell/top-level-violator | migrate | 9 |
| silmaril/hooks/git-hook | migrate | 3 |
| silmaril/shell/scala-cli-driver | migrate | 2 |
| silmaril/ci/workflow | migrate | 2 |
| silmaril/scripts/ui-constructor-violation | migrate | 1 |
| silmaril/scripts/depth-check | migrate | 1 |
| basicttl/fable-dissolve | merge | 1 |

**forge.csv (8):**

| family | disp | rows |
|---|---|---:|
| forge/base_agents/upstream-reference | reuse | 268,377 |
| forge/base_agents/corpus-projection | reuse | 7,899 |
| forge/base_templates/render-engine | reuse | 1,118 |
| external/superpowers/planning-methodology | reuse | 180 |
| forge/base/structural-tower-and-foundations | reuse | 50 |
| forge/example_gippidy_01/transport-wrapper | reuse | 2 |
| forge/base_agents/universal-base-generics | migrate | 3,394 |
| forge/example_gippidy_01/v17-corpus-transport | migrate | 14 |

Every family total reconciles against a census cardinality: e.g. `sparky-live-src` 5,193 =
`src` 5,259 − 66 keyword-`lambda` twins; `legacy-reference-copy` 692 = `reference` 719 − 27
`aob/layout`; `build-and-verification` 223 = `make` 69 + `tests` 154; `upstream-reference`
268,377 = `base_agents` 279,670 − `golden` 2,094 − `r1_staging` 1,300 − `corpus` 7,899;
`fable-dissolve` 1 + `ontology-source` 30,233 = `basicttl` 30,234.

---

## 4. Per-family disposition rulings — silmaril.csv

### 4.1 REUSE families

**`basicttl/ontology-source`** — covers `basicttl/**` except the one fable file.
Disposition **reuse**. Governing source: STRICTNESS Rule 4 *"Ontology IS the Project … All
content lives in basicttl TTL … If it is not in the ontology, it does not exist"*; JUNGLE_MAP
*"basicttl/ … THE ONTOLOGY SOURCE. Every class, individual, property lives here."* The
ontology source is the authored ground truth every projection is generated **from**; it is
kept and consumed as-is. (Census Row 3.) Depth-remediation of legacy empty labels
(PLAN_FREEZE Ruling 4) edits content in place — that is `reuse` under continued authorship,
not migrate/retire.

**`silmaril/engine/sparky-live-src`** — covers `./scripts/python/pylib/src/**` except the
reserved-keyword `lambda` twins (§7). Disposition **reuse**. Governing source: census Row 2
*"the live unary-morphism engine — a PEP-420 namespace tree mirrored across three physical
roots (PROCESS+APPLY+SLOTS under `src/silmaril/sparky`, VALUE under `config/constants`,
DEPENDENCY under `config/gate/external`)"*; JUNGLE_MAP *"This is the heart."* The live engine
is the substrate every future process must follow (STRICTNESS Rule 2/5) — reused, not rebuilt.
The lawful `lambda_/` sibling (7 files) is inside this reuse family; only the Python-invalid
`lambda/` spelling is carved out.

**`silmaril/engine/build-and-verification`** — covers `./scripts/python/pylib/make/**` and
`./scripts/python/pylib/tests/**`. Disposition **reuse**. Governing source: JUNGLE_MAP *"The
Make Envelope Pattern"* (the SILMARIL_PYTHON-guarded envelope recipes) and *"tests/ … Each
test invokes subprocess, checks exit+stdout+stderr"*. The build envelopes and pytest harness
are the live verification apparatus of the reused engine.

**`silmaril/engine/live-receipts-config`** — covers `./scripts/python/pylib/` root files
(`Makefile`, `FILE_CAPTURE.md`, `INTEGRATION_AUDIT.md`, `LIVE_PROMOTION_RECEIPT.md`, and the
three `*-routing.json` / `*-manifest.json` receipts). Disposition **reuse**. Governing source:
JUNGLE_MAP *"Makefile Master include file (26 .mk includes)"*; these are the engine's live
top-level receipts and master build entry.

**`silmaril/ledger/audit-record`** — covers `./ledger/**` (16 files). Disposition **reuse**.
This W1 ledger (census, maps, manifests, trees, checks, and **this account**) is the audit
record consumed by W3/W5/the panel; it is preserved (STRICTNESS Rule 15 *"Preserve Agent
Work"*).

**`silmaril/root/governance-doc`** — covers the six root handoff docs (`README.md`,
`JUNGLE_MAP.md`, `PLAN_FREEZE.md`, `STRICTNESS_RULES.md`, `SUBAGENT_FINDINGS.md`,
`TRANSCRIPT_VERBATIM.md`). Disposition **reuse**. Governing source: STRICTNESS Rule 14
*"Distinct Files for Distinct Concerns"* + Rule 1 *"Transcript Law"* — the requirements ledger
is retained verbatim.

**`silmaril/root/repo-config`** — covers `./.gitignore`, `./.gitmodules`. Disposition
**reuse**. Live VCS configuration (the submodule wiring under STRICTNESS Rule 8 forge
nomenclature).

**`silmaril/docs/doctrine`** — covers `./docs/praeriehund-demokratie-der-kategorien.md`,
`./docs/unary-byte-frame-law.md`. Disposition **reuse**. These two files ARE the binding law
of this campaign (Global Constraint 1); they are authored doctrine, never generated output —
Rule 10's "docs/*.html generated artifacts" ruling does not reach them (they are `.md`
doctrine, not rendered site pages).

**`silmaril/docs/working-notes`** — covers `./docs/README.md`, `./docs/pr2-review-addendum.md`,
`./docs/pr2-socratic-followup.md`, `./docs/superpowers/plans/2026-08-07-w1-completion.md`.
Disposition **reuse**. Hand-authored working/plan notes (Markdown), not site render output;
the W1-completion plan is the live plan this task executes under.

**`silmaril/keys/pgp-trust-root`** — covers `./keys/README.md`, `./keys/claude.asc`,
`./keys/github-web-flow.asc`, `./keys/herodotus.asc`. Disposition **reuse**. Governing source:
STRICTNESS Rule 11 *"Never modify committed keys/*.asc except via documented rotation"*;
JUNGLE_MAP Trust System (three identities). The public-key trust roots are immutable inputs —
explicitly **not** generated (contrast the derived manifest, §6). Only the derived
`trust-manifest.txt` retires.

**`silmaril/shell/lawful-launcher`** — covers `./scripts/source/discipline/**` (3 launchers).
Disposition **reuse**. Governing source: `docs/unary-byte-frame-law.md` *Normative boundary
law* — the `scripts/source/discipline/gate/shell/launcher/**` entrances are the
already-lawful Sparky-era shell launchers (one script definition, `$1`-only, one command);
census/law names them as the conformant surface. Reused as the launcher template the RED
shell violators (§4.4) must migrate toward.

**`silmaril/ontology-dir/readme`** — covers `./ontology/README.md`. Disposition **reuse**.
Hand-authored directory README, not a generated render target (contrast the five generated
`ontology/` artifacts, §6).

**`silmaril/hooks/readme`** — covers `./hooks/README.md`. Disposition **reuse**. Hand-authored
doc; the three hook scripts themselves migrate (§4.4).

### 4.2 RETIRE families — see §6 for full inverse evidence

**`silmaril/engine/legacy-reference-copy`** — covers `./scripts/python/pylib/reference/**`
except the `aob/layout` provisional carve (§7). Disposition **retire**. Governing source:
census Row 2 *"a 719-file orphaned legacy `reference/` copy"* / sparky_substrate.md §2.3–2.4
(RETIRE candidate, consumer closure evidenced empty, blocked until byte-complete inverse
recorded). Inverse in §6.

**`silmaril/site/generated-artifact`** — covers `./docs/architecture.html`,
`./docs/index.html`, `./docs/provenance.html`, `./docs/folklore.html`,
`./docs/_includes/build-status.html`, `./docs/assets/css/generated.css`. Disposition
**retire**. Governing source: STRICTNESS Rule 10 *"Everything rendered/generated (docs/\*.html
… generated.css …) is produced CI-only. Removed from branch."*; PLAN_FREEZE Ruling B *"zero
hand-authored HTML anywhere in the repo"* + Workflow 3.1 *"Remove ALL committed generated
artifacts from branch."* Rule 10 explicitly names `docs/*.html` as generated artifacts, so all
site HTML retires. Inverse in §6.

**`silmaril/site/jekyll-scaffold`** — covers the remaining `./docs/**`: `./docs/Gemfile`,
`./docs/_config.yml`, `./docs/_layouts/default.html`, `./docs/assets/css/main.css`,
`./docs/assets/js/main.js`. Disposition **retire**. Governing source: JUNGLE_MAP CI *"site …
Will be rebuilt as GeoSPARQL-driven generation"*; PLAN_FREEZE Ruling B (zero hand-authored
HTML) + Workflow 3. The whole Jekyll apparatus is superseded by the base_templates/GeoSPARQL
renderer. Inverse in §6 (this is the weakest inverse — a git-history recovery, honestly
flagged).

**`silmaril/ontology-dir/generated-artifact`** — covers `./ontology/silmaril-consolidated.ttl`,
`./ontology/manifest.ttl`, `./ontology/shapes.ttl`, `./ontology/queries.sparql`,
`./ontology/geosparql.sparql`. Disposition **retire**. Governing source: JUNGLE_MAP
*"ontology/ Generated artifacts (COMMITTED but should be CI-only per plan)"*; STRICTNESS
Rule 10 (*"ontology/ consolidated"* named explicitly); PLAN_FREEZE Workflow 3.1. Inverse in §6
(the strongest inverse — the CI ontology job literally regenerates-and-byte-compares).

**`silmaril/ontology-dir/orphaned-generated`** — covers `./ontology/ui-shapes.ttl` (1).
Disposition **retire**. Governing source: JUNGLE_MAP *"ui-shapes.ttl ORPHANED — nothing
consumes it (104 lines)"*, under the ontology/ generated block. Consumer closure trivially
empty. Inverse in §6 (the render step producing it must be built before deletion).

**`silmaril/keys/generated-manifest`** — covers `./keys/trust-manifest.txt` (1). Disposition
**retire**. Governing source: STRICTNESS Rule 10 (*"keys/trust-manifest.txt"* named
explicitly); JUNGLE_MAP *"Trust manifest (keys/trust-manifest.txt) derived from
basicttl/commit_signing_trust.ttl"*. Inverse in §6.

### 4.3 PROVISIONAL families — see §7

**`silmaril/engine/sparky-reserved-keyword-lambda-twin`** (66) and
**`silmaril/engine/legacy-reference-aob-layout`** (27) — both inherited from the census
Honest-gap register; gaps stated in §7.

### 4.4 MIGRATE families

**`silmaril/engine/outside-pylib-python`** — covers `./scripts/python/morphism_contracts/**`
(30) and `./scripts/python/sparky_lambda/**` (20). Disposition **migrate**. Governing source:
`docs/unary-byte-frame-law.md` clause 14 — *"Python campaign/runtime code is not executable
merely because it has a `.py` suffix or sits below `scripts/python`. Its physical
implementation … must first be integrated in the registered recursive physical tree rooted at
the exact directory `scripts/python/pylib`."* These sit under `scripts/python` but **outside**
`pylib`; they must migrate into the registered tree. Successor hint: integrate into
`scripts/python/pylib`.

**`silmaril/shell/top-level-violator`** — covers the nine top-level `./scripts/*.sh`
(`bootstrap-sdkman.sh`, `ci.sh`, `clone-reference-repos.sh`, `init-fake-remote.sh`,
`inspect-local-agents.sh`, `install-git-hook.sh`, `migrate-situational-awareness-to-codex.sh`,
`package-sparky.sh`, `validate-cicd.sh`). Disposition **migrate**. Governing source: STRICTNESS
Rule 2 (unary byte-frame law) + `docs/unary-byte-frame-law.md` Bash frontier (`ci.sh` is named
RED there: *"scripts/ci.sh is not exempt … All four bodies are multi-stage rather than
one-command arrows"*). Successor: the lawful `source/discipline/gate/shell/launcher` form
(§4.1).

**`silmaril/hooks/git-hook`** — covers `./hooks/pre-commit`, `./hooks/pre-push`,
`./hooks/remote-update` (3). Disposition **migrate**. Governing source: STRICTNESS Rule 2 +
the Bash frontier of the unary law (any `.sh`/shebang shell entrance is inventoried and must
carry the unary shell contract). Successor: unary-conformant launcher form.

**`silmaril/shell/scala-cli-driver`** — covers `./scripts/scala/**` (2:
`cli/workspace/execute.sh`, `cli/workspace/verify.sh`). Disposition **migrate**. Governing
source: sparky_substrate.md §3.4 (the Scala-CLI driver shells are RED, need unary refactor);
STRICTNESS Rule 2. Successor: unary `source/discipline/gate/shell` launcher form.

**`silmaril/ci/workflow`** — covers `./.github/workflows/ci.yml`, `./.github/workflows/cd.yml`.
Disposition **migrate**. Governing source: PLAN_FREEZE Workflow 4 (multi-engine CI/CD:
Jena/SIS/Sedona/rdflib, *"CI/CD is its OWN GOAL"*); JUNGLE_MAP CI table (*"Will be removed"* /
*"Will change"* jobs). The workflows are re-authored as Workflow 4, not kept as-is. (STRICTNESS
Rule 13 keeps CI its own workflow — migrate records the destination without doing that work
here.)

**`silmaril/scripts/ui-constructor-violation`** — covers `./scripts/ui-constructor.py` (1).
Disposition **migrate**. Governing source: JUNGLE_MAP *"scripts/ui-constructor.py — THE
VIOLATION. Hardcodes palette/typography in Python … Must be replaced with GeoSPARQL-driven
renderer using forge/base_templates."* Successor: `sparky/morphism/ontology` UI render ops +
`forge/base_templates` HEEx.

**`silmaril/scripts/depth-check`** — covers `./scripts/ontology-depth-check.py` (1).
Disposition **migrate**. Governing source: JUNGLE_MAP *"scripts/ontology-depth-check.py …
Currently advisory (|| true in CI). Plan makes it blocking for basicttl/*.ttl."*;
PLAN_FREEZE Ruling 4 (depth gate becomes executable law). Successor: the
`morphism/ontology/validation` depth family under unary law.

### 4.5 MERGE family

**`basicttl/fable-dissolve`** — covers `basicttl/folklore_provenance_fable.ttl` (1).
Disposition **merge**. Governing source: PLAN_FREEZE Ruling 3 verbatim — *"FABLE = DISSOLVE
AND ABSORB: File disappears; content retyped into existing classes (ConcreteAnchor/
DecompositionStep idioms); fable-as-query enters the query library."* The fable file ceases to
exist and its content is **absorbed into the pre-existing** ontology individuals + the query
library. Inverse (content preservation): retyped individuals + query-library entry (no byte is
lost; the file is dissolved, not deleted). Recorded judgment: see §9 (merge vs split).

---

## 5. Per-family disposition rulings — forge.csv

Frame: the `forge/**` trees are pinned git submodules — **immutable upstream provenance**
under `docs/unary-byte-frame-law.md` *Normative boundary law* (*"Isolation is permitted only
for immutable upstream provenance or typed host effects"*) and STRICTNESS Rule 8 (*"these are
not external, they are forged components"*). Default disposition for provenance consumed
as-is is **reuse**; only the subtrees a beacon ruling explicitly mobilizes are **migrate**.
Verified base pin: `forge/base` @ `c4e828188a57d7a93c4f4972859dd0862ae6cce6` (the SHA
`9e60c103` asserted by an earlier working note does not exist in the repo — census VS1).

### 5.1 REUSE families

**`forge/base_agents/upstream-reference`** — covers `forge/base_agents/**` except `golden/`,
`r1_staging/`, `corpus/` (268,377 rows). Disposition **reuse**. Governing source: census Row 4
(the deep AOB research forge, pinned `d2b1217f`); JUNGLE_MAP *"forge/base_agents … Reference
only."* Consumed as reference provenance; not rewritten. (Capture-don't-conclude: no beacon
ruling directs migrating `research/`, `r1_site/`, `lib/`, `vendor/`, `specs/`, etc. — so no
migrate is imported for them.)

**`forge/base_agents/corpus-projection`** — covers `forge/base_agents/corpus/**` (7,899).
Disposition **reuse**. Governing source: census Row 11 (the machine-emitted CorpusAtom SHACL
projection, 1,477 atoms × emitter legs). It is reference projection output inside the immutable
submodule; the corpus **consolidation** ruling (PLAN_FREEZE Ruling A) names
`example_gippidy_01`, not base_agents/corpus — so this stays reuse. Recorded judgment: §9.

**`forge/base_templates/render-engine`** — covers `forge/base_templates/**` (1,118).
Disposition **reuse**. Governing source: census Row 5 (the Jinja2 render-template forge,
pinned `eb3d916b`); STRICTNESS Rule 5 (*"the sparky/lambda-blotto substrate already implements
this substrate — use it, do not bypass it"*) and PLAN_FREEZE Ruling B/Workflow 3.3 (*"Wire
base_templates HEEx macros as the codegen engine"*). This is the render engine the retiring
site/ontology artifacts are regenerated **by** — reused wholesale.

**`external/superpowers/planning-methodology`** — covers `external/skills/superpowers/**`
(180). Disposition **reuse**. Governing source: census Row 8; PLAN_FREEZE Ruling C /
Workflow 1.1 (*"Use https://github.com/obra/superpowers for full e2e planning"*). The planning
methodology is adopted as-is. (Note: this tree lives under `external/skills/` — a superpowers
harness location — and is accounted in `forge.csv`; STRICTNESS Rule 8's "not external"
nomenclature governs the four `forge/*` submodules, and does not retro-rename the obra
`external/skills/superpowers` upstream, which is consumed as an external methodology.)

**`forge/base/structural-tower-and-foundations`** — covers `forge/base/**` (50). Disposition
**reuse**. Governing source: census Row 6 / Row 13 (the thin structural turtle-tower +
category-theory foundations corpus, pinned `c4e82818`). Consumed as the foundations reference.

**`forge/example_gippidy_01/transport-wrapper`** — covers `forge/example_gippidy_01/.git` and
`forge/example_gippidy_01/README.md` (2). Disposition **reuse**. The gitlink pointer and the
transport README are retained as the package wrapper; only the 14 ZIP slices migrate (§5.2).

### 5.2 MIGRATE families

**`forge/base_agents/universal-base-generics`** — covers `forge/base_agents/golden/**` (2,094)
and `forge/base_agents/r1_staging/**` (1,300) = 3,394. Disposition **migrate**. Governing
source: PLAN_FREEZE Ruling A (*"Discovery: base_agents `golden` and `r1_staging/*/**` contain
the generics"*) + Workflow 1.2 + Workflow 5.1 (*"Establish universal base with generics from
base_agents golden/r1_staging"*). These are mobilized (bound/morphed) into the owned universal
base ontology — a migrate, not a reuse-in-place. (Census Rows 9/10: golden `.aob.dir` atoms +
`_specspec` W3C spec-of-specs live here.)

**`forge/example_gippidy_01/v17-corpus-transport`** — covers the 14 `*.zip` split slices
(consolidated-v17 ×7, semantic-formats-v17 ×7). Disposition **migrate**. Governing source:
PLAN_FREEZE Ruling A (*"example_gippidy_01 IS the fullest wish — ALL projections"*) +
Workflow 5.2 (*"Import example_gippidy_01 algebra, projection family, native runners"*) +
5.3 (*"Establish v1 ontology AOB buildout"*). The v17 corpus transport is imported/consolidated
into the owned v1; migrate records that destination. (Census Row 7/12: the 104,848-identity
projection plane the slices carry.)

---

## 6. Retire families — inverse evidence (Präriehund: no delete without inverse)

The doctrine forbids deletion without *"consumer closure plus a byte-complete inverse."* Each
retire family below names the inverse that **exists or must exist**. Two grades are
distinguished honestly:

- **Regeneration inverse** (strong): the successor pipeline re-emits the exact bytes and CI
  byte-compares — deletion is safe the moment the pipeline is proven.
- **Recovery inverse** (weaker): the exact bytes are recoverable from git history while a
  *rebuild* (not byte-identical regeneration) stands up the successor — flagged as such.

| retire family | rows | consumer closure | byte-complete inverse | grade |
|---|---:|---|---|---|
| `silmaril/ontology-dir/generated-artifact` | 5 | consumed by CI `ontology` job (regenerate-and-compare) | **regenerated byte-identical** by `morphism/ontology/consolidation` from `basicttl/*.ttl`; the CI ontology job's regenerate-and-compare **is** the inverse check (JUNGLE_MAP; Rule 10; Workflow 3.1) | regeneration |
| `silmaril/site/generated-artifact` | 6 | site pages / `build-status` include / `generated.css` — consumed by the Jekyll `site` + `ui-constructor` CI jobs | regenerated by the GeoSPARQL/`base_templates` render from the basicttl ontology; CI `site`+`ui-constructor` jobs regenerate-and-compare (Rule 10; JUNGLE_MAP; Ruling B). `folklore.html`'s content is additionally dissolved-and-absorbed per Ruling 3 | regeneration |
| `silmaril/keys/generated-manifest` | 1 | `keys/trust-manifest.txt` derived from `commit_signing_trust.ttl`; checked by CI `provenance` | regenerated byte-identical from `basicttl/commit_signing_trust.ttl` by `morphism/provenance` trust pipeline; CI provenance job regenerates-and-checks (Rule 10; JUNGLE_MAP) | regeneration |
| `silmaril/ontology-dir/orphaned-generated` | 1 | **empty** — JUNGLE_MAP *"ORPHANED — nothing consumes it"* | the render step that emits `ui-shapes.ttl` is **not yet evidenced** and MUST exist before deletion (no-delete-without-inverse); until then git history holds the exact bytes | must-exist |
| `silmaril/site/jekyll-scaffold` | 5 | Jekyll build inputs (`Gemfile`/`_config.yml`/`_layouts`/`main.css`/`main.js`), superseded by the render engine | **recovery**: exact bytes recoverable from git history until the `base_templates`/GeoSPARQL successor renderer is proven; structure re-expressed as HEEx macros (Ruling B; Workflow 3) — not a byte-identical regeneration, flagged | recovery |
| `silmaril/engine/legacy-reference-copy` | 692 | **evidenced empty** — sparky_substrate.md §2.3: zero import hits repo-wide excluding `reference/` itself | successor superset = the live `src/silmaril/sparky` + `config` mirror; a **content-addressed predecessor/successor account MUST be recorded before deletion** (sparky_substrate.md §2.4: RETIRE candidate blocked until inverse recorded — *cannot delete on orphaned observation alone*); until recorded, git history is the byte-complete recovery | must-exist |

No retire family relies on a bare `duplicate`/`neglected`/`unnecessary` label; each names
consumer closure and a concrete inverse, per the doctrine.

---

## 7. Provisional rows — the gaps (genuinely undecidable-before-W2)

Both provisional families are **inherited verbatim from the frozen census Honest-gap
register** (Task 3), not minted here. Each names a gap whose resolution is a W2-design /
live-probe activity, not tedious bookkeeping.

**`silmaril/engine/sparky-reserved-keyword-lambda-twin`** — 66 rows across
`src/silmaril/sparky/lambda/` (10), `src/config/constants/lambda/` (55),
`src/config/gate/external/python/lambda/` (1). `provisional_gap`: *reserved-keyword `lambda`
module (Python-invalid spelling); live-reachability via importlib vs orphaned unresolved
(sparky_substrate.md §1.4/5.3); byte-complete inverse required before any retire.* Why
genuinely undecidable now: the disposition is a two-valued fork — **migrate→`lambda_`** if the
module is live-reachable via importlib, **retire** if it is orphaned dead weight — and the
deciding evidence is a live importlib reachability probe against the running engine, which is
out of scope for a read-only account over frozen trees and is a W2 activity. The lawful
`lambda_/` sibling (7 files) is **not** provisional — it is `reuse` inside
`sparky-live-src`; only the keyword-invalid spelling is held open. (Census gap 3.)

**`silmaril/engine/legacy-reference-aob-layout`** — 27 rows under
`reference/pylib/reference/config/constants/aob/layout/`. `provisional_gap`: *aob/layout
hyphenated projection constants (daedalus/icarus/ossie/yggdrasil): meaning unresolved; no live
analogue found (sparky_substrate.md §2.4/5.5); Präriehund name-the-gap.* Why genuinely
undecidable now: the doctrine says *"an unresolved meaning remains provisional"* — the
**denotation** of these `*-projection` constants is unresolved and has no live morphism
analogue, so they cannot be confidently swept into the surrounding `reference/` retire without
first tracing their meaning. This is the Präriehund case exactly: name the gap, do not
force-fit into the retire bin. (Census gap 5.)

---

## 8. Individually-enumerated exception rows

Every point where a single path (or a small explicit set) is ruled differently from its
enclosing region, enumerated individually per the brief:

1. `basicttl/folklore_provenance_fable.ttl` — **merge** (only non-reuse row in all of
   `basicttl/**`). Ruling 3.
2. `./docs/praeriehund-demokratie-der-kategorien.md` — **reuse** (doctrine, exempt from the
   docs retire).
3. `./docs/unary-byte-frame-law.md` — **reuse** (doctrine).
4. `./docs/README.md` — **reuse** (working note).
5. `./docs/pr2-review-addendum.md` — **reuse** (working note).
6. `./docs/pr2-socratic-followup.md` — **reuse** (working note).
7. `./docs/superpowers/plans/2026-08-07-w1-completion.md` — **reuse** (the live plan).
8. `./docs/architecture.html` — **retire** (site/generated-artifact).
9. `./docs/index.html` — **retire** (site/generated-artifact).
10. `./docs/provenance.html` — **retire** (site/generated-artifact).
11. `./docs/folklore.html` — **retire** (site/generated-artifact; content also dissolved per
    Ruling 3).
12. `./docs/_includes/build-status.html` — **retire** (site/generated-artifact; JUNGLE_MAP
    "generated").
13. `./docs/assets/css/generated.css` — **retire** (site/generated-artifact; JUNGLE_MAP
    "generated from ontology").
14. `./docs/Gemfile`, `./docs/_config.yml`, `./docs/_layouts/default.html`,
    `./docs/assets/css/main.css`, `./docs/assets/js/main.js` — **retire** (site/jekyll-scaffold,
    recovery inverse).
15. `./ontology/README.md` — **reuse** (only non-retire row under `./ontology/`).
16. `./ontology/ui-shapes.ttl` — **retire** (orphaned-generated; distinct must-exist inverse
    from the other four generated `ontology/` artifacts).
17. `./ontology/silmaril-consolidated.ttl`, `./ontology/manifest.ttl`, `./ontology/shapes.ttl`,
    `./ontology/queries.sparql`, `./ontology/geosparql.sparql` — **retire**
    (ontology-dir/generated-artifact, regeneration inverse).
18. `./keys/trust-manifest.txt` — **retire** (generated-manifest); the other four `./keys/*`
    are **reuse** (immutable PGP trust roots, Rule 11).
19. `./keys/README.md`, `./hooks/README.md`, `./ontology/README.md` — **reuse** READMEs carved
    out of their otherwise-migrate/retire regions.
20. `./scripts/ui-constructor.py` — **migrate** (named "THE VIOLATION").
21. `./scripts/ontology-depth-check.py` — **migrate** (named advisory→blocking).
22. `./hooks/pre-commit`, `./hooks/pre-push`, `./hooks/remote-update` — **migrate** (git-hook
    shells; README carved to reuse).
23. The reserved-keyword `lambda` twins (66) and `aob/layout` constants (27) — **provisional**
    carve-outs from their enclosing `reuse`/`retire` engine families (§7).
24. `forge/example_gippidy_01/.git`, `forge/example_gippidy_01/README.md` — **reuse** (wrapper)
    vs the 14 `*.zip` slices — **migrate**.

---

## 9. Judgment calls recorded honestly (Präriehund: mark the seam)

- **`basicttl/fable-dissolve` = merge vs split.** Ruling 3 is "dissolve and absorb". Read as
  *absorb into the pre-existing ontology corpus* → **merge** (chosen). Read as *one fable fans
  into several retyped anchors + one query* → split. `split` is additionally disfavoured
  because the doctrine reserves it for the whole-graph render seal, not per-file lifecycle. The
  disposition is a lossy projection onto the closed vocabulary; the **inverse is identical
  either way** (content preserved, file dissolved). Chosen: merge.

- **`forge/base_agents/corpus-projection` = reuse vs migrate.** The corpus is projection output
  and a corpus-consolidation goal exists (Ruling A) — but that ruling names
  `example_gippidy_01` as the consolidation source, and `golden`/`r1_staging` as the generics;
  it does **not** name `base_agents/corpus`. Per capture-don't-conclude (no interpretive
  gates), no migrate is imported for `corpus/` that the beacons do not direct; it stays
  **reuse** (reference projection inside immutable provenance). Flagged so W5 can revisit if a
  later ruling mobilizes it.

- **`./docs/*.html` "generated" grouping.** `generated.css`/`build-status.html` are literally
  machine-generated (JUNGLE_MAP); the four `.html` pages are hand-authored HTML that Ruling B
  *"zero hand-authored HTML"* replaces with generated output. Rule 10 itself names
  *"docs/\*.html"* as generated-artifacts-to-remove, so all six share disposition **retire**
  and family `site/generated-artifact`; the nuance (currently-generated vs
  authored-to-be-replaced) is recorded here rather than split into two families, since the
  disposition and the regeneration successor are the same.

---

## 10. What the seed hands downstream

- **W5 (reconciliation):** every one of 317,601 physical entries now has exactly one account
  row; the 37 family rulings and the two open provisional gaps are the reconciliation surface.
- **W3 (retire-with-inverse):** the six retire families in §6, with their consumer-closure and
  byte-complete-inverse grades (regeneration vs recovery vs must-exist), are W3's work list.
  The two **must-exist** inverses (`ui-shapes.ttl` render step; the `reference/`
  predecessor/successor content-addressed account) are the hard gates — no deletion until they
  exist.
- **The panel:** §9 records every seam where a disposition is a judgment rather than a
  beacon-forced value, so nothing is presented as more settled than it is.

---

*Silmaril · GraphAtlas — "Inspizierbar. Revidierbar. Föderiert." · Nihil occultum, tantum
textum.*
