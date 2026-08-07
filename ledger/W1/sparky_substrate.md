# W1 Discovery — Sparky Substrate & RED Enforcement Surface

Agent: W1 discovery (phase-7). Frame date: `2026-08-07`.
Scope: read-only census. Nothing modified outside `ledger/W1/`.

---

## 0. Mandatory-read status (honest, no fabrication)

| Required file | Status |
|---|---|
| `docs/praeriehund-demokratie-der-kategorien.md` | **READ IN FULL** (130 lines) |
| `docs/unary-byte-frame-law.md` | **READ IN FULL** (766 lines) |
| `docs/unary-byte-frame-law-enforcement-proof.md` | **MISSING — DOES NOT EXIST.** `find` over the whole repo returns nothing. The index doc names it as a continuation, but the file was never created (or not yet). |
| `docs/unary-byte-frame-law-receipts.md` | **MISSING — DOES NOT EXIST.** Same: named in the index topology, absent on disk. |

Also referenced-but-absent (flagged so downstream does not chase them):
`docs/reference/Resource/Uniform/Name/Dictionary.md` (no `docs/reference/` dir),
`docs/campaigns/build-bootstrap-unary-law-red-receipt-2026-07-16.md` (no
`docs/campaigns/` dir). The **only** unary-law artifact physically present is
the single index/law file `docs/unary-byte-frame-law.md`. All census numbers in
§4 below therefore come from that one file. **PROVISIONAL:** the two
continuations either live outside this checkout or were planned and never
written; treat the index doc as the sole authority until they surface.

---

## 1. Live engine — `scripts/python/pylib/src/silmaril/sparky/`

### 1.1 Physical census

- **2,277 `.py` files, 100% `.py`.** Basename frequency is the tell:
  `process.py` ×989, `value.py` ×821, `apply.py` ×459, `project.py` ×7,
  `check.py` ×1.
- Top-level children and file counts:
  | child | files | role |
  |---|---|---|
  | `morphism/` | 2,039 | the bulk engine (codebase 1,714 · contract 201 · ontology 75 · provenance 24 · resource 15 · specification 10) |
  | `lambda_blotto/` | 220 | Colonel-Blotto allocation morphisms |
  | `lambda/` | 10 | **reserved-keyword duplicate (see 1.4)** |
  | `lambda_/` | 7 | the lawful spelling of the same substrate |
  | `contract/` | 1 | `file_capture_static/check.py` — the static enforcement gate |
- **Zero `__init__.py`** anywhere under `src/` — the live tree is a PEP-420
  namespace-package tree by construction.

### 1.2 The three-root mirror — CONFIRMED

The engine is one behaviour tree mirrored across three physical roots under
`scripts/python/pylib/src/`:

1. **`silmaril/sparky/` = PROCESS + APPLY + SLOTS** (behaviour). Two arrow shapes:
   - `apply.py` — the unary morphism: `def apply(value: Input) -> Frame: return PROJECT(value)`. One clause, one param, one body line, one typed delegation. Textbook §law-clauses 1/6/8/9.
   - `process.py` — the executable entrance: `def MAIN() -> int: ...` then `raise SystemExit(MAIN())` (the `.py`-launcher shape; no `__main__` guard, no argparse).
   - carrier files (`input/value.py`, `output/value.py`, `effect/value.py`, `frame/value.py`) are the **SLOTS**: each is a single `@DATACLASSES.dataclass(frozen=True, slots=True)` `class Value`.
2. **`config/constants/` = VALUE** (1,858 files: lambda 55 · lambda_ 55 · lambda_blotto 281 · morphism 1,437 · source 4 · substrate 26). Every constant is `VALUE = ...`, imported as `from config.constants.… import VALUE as X`.
3. **`config/gate/` = DEPENDENCY** (1,124 files, all under `gate/external/`). Every external binding is `DEPENDENCY = ...`, imported as `from config.gate.external.… import DEPENDENCY as X`; project-internal delegations import `PROJECT`.

So each operation is a physically-drilled directory whose leaf files split
cleanly into the VALUE side (constants pulled from `config/constants`), the
DEPENDENCY side (host/stdlib pulled from `config/gate/external`), and the
PROCESS/APPLY/SLOTS side (the sparky behaviour + frozen-slots carriers). The
mirror the task describes is real and physically enforced.

### 1.3 Conformance (the "~100% unary-conformant" claim)

Conformance is **actively machine-checked**, not asserted. The gate is
`sparky/contract/file_capture_static/check.py` → `check(root) -> tuple[str,…]`;
the test `pylib/tests/test_file_capture_contract.py` asserts `check(ROOT) == ()`.
`check.py` enforces, per operation leaf: presence of the 5 operation files
(`input/output/effect/frame/value.py` + `apply.py`); `frozen=True, slots=True`
on every role carrier; `schema_identity`/`lineage_identity` presence;
`effect` must carry `evidence_class: ByteVector` and must **not** default to
`ByteVector(OBSERVED)`; `apply.py` must be exactly
`def apply(value: Input) -> Frame … PROJECT(value)` (rejects non-unary apply);
a **FORBIDDEN_CAPTURE_TEXT** blacklist (`import os`, `import hashlib`, `print(`,
`logging.`, `uuid`, `time.time`, …) forcing every host call through an exact
gate leaf; scheduler libraries must contain **no `while`/`for`** ("scheduler
contains a loop instead of one transition"); and a final pass that
`compile()`-checks every `*.py` and rejects any surviving `.lambda.` /
`.evidence.class.` / `.issue.from.` reserved-keyword import. The "~100%"
figure is the pass state of *this* gate over the captured operation set — it is
a conformance of the **file-capture / Lambda-Blotto slice**, promoted live per
`pylib/LIVE_PROMOTION_RECEIPT.md` (21/21 isolated, 19/21 live with 2 intended
skips).

### 1.4 Exact edge cases (the non-uniform residue)

- **Fixed-arity pickle de-mux processes — task said 3; I count 5.** Process
  entrances that read **two** `_PICKLE.load(_SYS.stdin.buffer)` values off one
  stdin stream (binary de-mux, violating one-input purity in spirit while
  staying one-stream physically):
  1. `morphism/contract/validation/schema/equality/output/process.py` (`left==right → ACCEPTED|REJECTED`)
  2. `morphism/contract/validation/entry/self/test/output/process.py` (same compare)
  3. `morphism/contract/validation/entry/twin/readback/output/process.py` (same compare)
  4. `morphism/contract/validation/mutation/append/copy/output/process.py` (`target + copy`)
  5. `morphism/contract/validation/mutation/remove/matching/output/process.py` (`target.translate(TABLE, matching)`)
  Items 1–3 are the equality/compare family; 4–5 are the binary-mutation family.
  **The "3" in the brief is stale or counts only one family — the physical
  count of 2-load de-mux processes is 5.** (9 processes do any `PICKLE.load`;
  4 of those load exactly once.) These are the genuine fixed-arity outliers to
  the one-input law.
- **Multi-argv de-mux processes:** 29 `process.py` read `SYS.argv[2]` (2-arg
  shape, e.g. `atomic_delivery/process.py` runs `SUBPROCESS.run((*COMMAND, argv[1], argv[2]))`); 1 reads `argv[3]`. These pass a fixed operand count via argv rather than one byte frame.
- **Constant-heavy preambles:** carrier files such as
  `lambda_/invocation/process/file/input/value.py` carry ~10 lines of
  `from config.constants.… import VALUE as X` before a single `class Value`.
  Many *import statements*, but still exactly one semantic thing (one frozen
  dataclass) per file — the law's "one precise semantic thing per file" holds;
  the preamble length is cosmetic, not a cardinality violation.
- **Reserved-keyword `lambda/` twin (migrate/duplicate):** `sparky/lambda/`
  (10 files) is the Python-**invalid** spelling of `sparky/lambda_/` (7 files);
  mirrored in `config/constants/lambda` vs `lambda_` and
  `config/gate/external/python/lambda`. `lambda` is a Python keyword, so those
  modules cannot be reached by a normal `import` — check.py's own final loop
  rejects surviving `.lambda.` imports. **PROVISIONAL:** whether `lambda/` is
  live-reachable (via importlib) or orphaned dead weight was not resolved;
  disposition candidate = **migrate→`lambda_` / retire the keyword twin**
  (byte-complete inverse required first).

---

## 2. Legacy copy — `scripts/python/pylib/reference/` (X retire/migrate target)

### 2.1 Full census (`find | sort`, no `-maxdepth`, no truncation)

- **719 `.py` files, 100% `.py`** (matches the brief's "719-file LEGACY copy").
- Structure is a **copy-of-a-copy double nest**:
  `reference/pylib/src/` (341 files) + `reference/pylib/reference/` (378 files).
- **398 `__init__.py`** (vs **0** in the live tree).
- **`bootstrap.py` present** at `reference/pylib/reference/bootstrap.py` (6 lines:
  `resolve(frame)` = `importlib.import_module(RUNTIME_MODULE)` then
  `getattr(…, ENTRY_SYMBOL)(frame)`). No such file in the live tree.
- **13 hyphenated dirs** (all under `reference/pylib/reference/config/constants/aob/layout/`):
  `aob-directory-suffix`, `aob-witness-directory`, `ci-projection`,
  `daedalus-projection`, `icarus-projection`, `ossie-projection`,
  `project-directory`, `projection-document`, `projection-gap`, `root-spec`,
  `self-projection`, `storage-projection`, `yggdrasil-projection`.
  0 hyphenated *files*. (Hyphens are not valid Python identifiers → old
  string-addressed convention.)
- Basenames: `__init__.py` 398 · `apply.py` 150 · `value.py` 114 ·
  `library.py` 14 · plus one-off verbs (`observe/write/verify/seal/replay/…`).

### 2.2 Convention violations vs the live tree

| Convention | Live `src/` | `reference/` |
|---|---|---|
| Package style | PEP-420 namespace, **0** `__init__.py` | **398** `__init__.py` |
| Launcher | `process.py` + `raise SystemExit(MAIN())` | `bootstrap.py` importlib indirection |
| Dir naming | segmented underscore/atomic (no hyphens) | 13 **hyphenated** dirs |
| Reserved word | `lambda_` (migrating) | `aob/layout` legacy + one-off verb files |
| Layout | single `src/silmaril/sparky` + `config/*` | **double-nested** `pylib/{src,reference}` copy-of-copy |

### 2.3 Is it referenced by the live tree or CI? — NO

- `grep -rE '(from|import)\s+reference'` across the repo (excluding the
  reference dir itself): **zero hits.** No live module imports the legacy tree.
- The `"reference"` hits inside `src/` are unrelated **coordinate names**
  (`…/format/uri/reference/library.py`, `…/required/reference/order/…`), not
  imports of the legacy tree.
- `.github/` and `scripts/ci.sh`: **no reference** to the legacy tree.
- Conclusion: `reference/` is **orphaned relative to the live tree and CI** —
  dead to the running system but physically resident (719 files).

### 2.4 Complete-Component-Account disposition candidates

Per §"Complete Component Account" of the law (no deletion without a
byte-complete inverse; `duplicate`/`neglected`/`unnecessary` labels do **not**
authorize deletion):

- **RETIRE (candidate):** the whole `reference/` tree — no live/CI consumer
  (consumer closure looks empty). **Blocked** until a byte-complete inverse
  (content-addressed predecessor/successor account) is recorded. Cannot delete
  on the "orphaned" observation alone.
- **MIGRATE (candidate):** any `apply.py`/`value.py` in `reference/pylib/src`
  whose semantics have no live successor — drill into the live
  `silmaril/sparky` + `config` mirror before retiring the legacy copy.
- **CONFLICT (candidate):** the double-nest `reference/pylib/{src,reference}`
  is a copy-of-a-copy; locator-equality vs content-equality vs semantic-equality
  must be separately observed before either inner copy is called a duplicate.
- **PROVISIONAL:** the `aob/layout` hyphenated projection constants
  (`daedalus`/`icarus`/`ossie`/`yggdrasil`) — unresolved meaning, no live
  analogue found; keep provisional (Präriehund: name the gap, do not force-fit).

---

## 3. Top-level violator scripts — 10-point Source Discipline

The relevant Source-Discipline points (from `unary-byte-frame-law.md` §"Source
Discipline audit" 1–14): (1) exactly one param clause / one param; (8) one
physical body line / one top-level expression, no local decl sequence, no
multi-statement block, no `return`; (9) one atomic op or one typed delegation;
(11) no wildcard import; (12) every host symbol crosses a typed ContractGate;
Shell family: `$1` only (no `$@`/`$*`/`$#`/`shift`/`argv[2+]`), one non-decl
command, no pipeline/subshell/chain, the four `readonly …__*_type` bindings.

### 3.1 `scripts/ui-constructor.py` (472 LOC) — Python morphism family

Why it violates (representative, not exhaustive):
- **Multi-arg / argparse (¬1):** `main()` builds an `ArgumentParser` with
  `--input --output --format` — three inputs, not one byte frame.
- **Loops + multi-statement bodies (¬8/¬9):** `parse_turtle` is a hand-rolled
  char scanner with `while i < n`, nested closures (`skip_ws`, `parse_token`),
  and branching; `generate_css/html/svg` accumulate `css_lines`/`svg_parts`
  with `for … in subjects.items()` loops and conditionals.
- **Hardcoded values (¬law "no magic"):** literal hex palette
  (`#faf8f5`/`#2a2520`/`#8b7355`), inline font strings, `var_map`/`font_map`
  dicts, viewBox `'0 0 24 24'` — VALUE constants that belong in
  `config/constants`, not the body.
- **Ungated host effects (¬12):** direct `Path.read_text`/`write_text`/`mkdir`,
  `print(..., file=sys.stderr)`, `sys.exit` — filesystem + stdio with no
  ContractGate; exactly the `print(`/`import os`-class text `check.py` forbids.
- **Unary decomposition →** a `sparky/morphism/ontology/ui/…` operation family:
  TTL bytes admitted through one `config/gate/external/python/…` read leaf → a
  `parse/turtle` process producing a frozen triple/`subjects` carrier → per
  render format (`css`/`html`/`svg`) a separate `apply.py` doing
  `PROJECT(value)` over that carrier → palette/fonts/viewBox demoted to
  `config/constants/…/value.py`. Its render/serialize step mirrors the existing
  `…/serialize/project.py` shape already in the live morphism tree.

### 3.2 `scripts/ontology-depth-check.py` (217 LOC) — Python morphism family

- **Multi-statement `main()` + `check_file()` (¬8):** `sys.argv` dispatch,
  `rglob('*.ttl')`, `for ttl_file in ttl_files` accumulation loop.
- **Same hand-rolled `parse_turtle` scanner (¬8/¬9):** duplicated verbatim from
  ui-constructor (a duplicate-component in its own right).
- **Hardcoded thresholds (¬magic):** `< 200` char comment rule, the
  `owl:Class`/`owl:NamedIndividual`/`owl:ObjectProperty` literal type strings.
- **Ungated stdio (¬12):** `print` to stdout/stderr, `sys.exit` untyped effect.
- **Unary decomposition →** a `sparky/morphism/ontology/validation/depth/…`
  family: one TTL byte frame per file (bounded traversal like the existing
  `directory/crawl` scheduler, no `rglob` loop) → frozen `subjects` carrier →
  one `apply.py` per rule (class-comment-length, individual-typed,
  objectproperty-domain, objectproperty-range) each emitting an
  `Accepted|Rejected` Frame with typed effect; the `200` becomes a
  `config/constants` VALUE. Note the existing live gate
  `make/morphism/ontology/validation.mk` is the natural home.

### 3.3 Bash `*.sh` shells (15 files / 702 lines — matches doc census)

Repo shell surface (`scripts/**/*.sh`, 15 files): `bootstrap-sdkman.sh`,
`ci.sh`, `clone-reference-repos.sh`, `init-fake-remote.sh`,
`inspect-local-agents.sh`, `install-git-hook.sh`,
`migrate-situational-awareness-to-codex.sh`, `package-sparky.sh`,
`validate-cicd.sh`, `scala/cli/workspace/{execute,verify}.sh`,
`source/discipline/gate/shell/launcher/{value,commit/signature/policy/default/value,trust/manifest/check/value}.sh`,
plus a test fixture `tests/fixtures/volume_inventory/scripts/sample.sh`.

- **`scripts/ci.sh` — 4 definitions** (top-level entrance + `ci_finish`,
  `wire`, `fail`) → emits `Shell.Definition.Cardinality.Value` (plural defs).
  `ci_finish` reads 0 positions; `wire` reads `$1 $2`; top-level reads `$1 $2` +
  `shift` + `"${SBT_CMDS[@]}"` array-wide expansion → `Shell.Expansion.Wildcard.Present.Value`.
  Bodies are multi-stage (`trap`, `case`, pipelines `sbt … | grep | tail`,
  `diff -q`), not one-command arrows. `fail` uses `exit` (untyped effect). None
  declare the four `readonly …__input_type/__frame_type/__operation_type/__binding_type`
  bindings → `Shell.Callable.Contract.Absent.Value`.
- **`package-sparky.sh`:** `set -euo pipefail`, `while read -r entry` loop,
  `[[ … ]]` tests, command substitution, heredoc-generated launcher — heavy
  multi-stage. **`validate-cicd.sh`:** `check`/`ref_sha`/`check_ref_unmoved`
  functions + `$((npass+1))` arithmetic + `RESULTS+=()` arrays → plural-def +
  wildcard expansion.
- **The one COMPLIANT shape** is
  `scripts/source/discipline/gate/shell/launcher/value.sh`: one script
  definition, no function, observes only `$1`, one `printf '%s\n' "$1"`, and
  the four `readonly script__{input,frame,operation,binding}_type` bindings.
  This is the target normal form (the doc's "Sparky-era shell entrance").
- **Unary decomposition →** each shell callable becomes one
  `scripts/source/discipline/gate/shell/…/value.sh` launcher: `$1`-only input,
  a declared byte-descendant Frame, one non-decl command, and the four typed
  bindings; multi-stage bodies (ci tiers, packaging loop) re-expressed as typed
  stage state + a unary scheduler step (`Continue(next)`/`Complete(result)`),
  mirroring the loop-free `scheduler/transition/library.py` the Python engine
  already enforces.

### 3.4 Scala shells

- **Scala-CLI driver shells** `scripts/scala/cli/workspace/execute.sh` &
  `verify.sh`: these are `.sh` (bash) that *drive* Scala-CLI. Both carry a
  named fail function + `trap … ERR` + `if [[ $# -lt 1 ]]` (positional-count
  test) + `case` dispatch + `shift`; `verify.sh` additionally defines
  `source_state`/`workspace_state` with `find … -print0 | xargs sha256sum`
  pipelines and `cmp`/`diff` chains → plural-def, wildcard/`$@`, multi-stage.
  Same Shell-family findings as §3.3.
- **Joern/Scala scripts** (`forge/base_agents/scripts/cpg/{probe/calls.sc,
  probe/perfile.sc, joern/perfile/ndjson.sc}`): `@main def main(cpgFile: String)`
  — a callable with a **multi-statement body** (`importCpg`, `println`,
  `.filterNot(...).take(8).foreach(...)` iteration), i.e. loops + multi-line
  expression + multiple top-level ops → violates law-clauses 1/8/9 for the
  Scala callable surface. No registered ContractGate frontend observes `.sc`.
- **`forge/base_agents/*.scala`** (`species.scala`, `corpus/*.scala`, 134 LOC):
  Scala source with no unary-frame observation; part of the RED Scala census.
- **Unary decomposition →** the Joern probes become
  `sparky/morphism/codebase/…` CPG-observation operations projected through a
  registered Scala/Joern ContractGate frontend (the law explicitly requires a
  "registered ContractGate observation" per language frontend); each `println`
  survey becomes a separate unary Frame arrow over one admitted CPG byte input.

> **Note:** `scripts/ci.sh` targets an sbt Scala engine (`cli/run …`,
> `modules/semantic`, `Test/compile`) that has **no `build.sbt`, `project/`, or
> `modules/` directory in this checkout**. The Scala engine the CI spine and the
> build-bootstrap receipt describe is **not physically present here** — only its
> shell driver and stray `.scala`/`.sc` corpus files are. **PROVISIONAL:** the
> Scala engine lives in a submodule / sibling repo not in this working tree.

---

## 4. RED receipts — concrete X target list (from `unary-byte-frame-law.md`)

The law's own status line: **"active red migration; the law is specified, but
the enforcement implementation does not yet satisfy the law it enforces."**
Every census below is a frozen RED receipt X must turn GREEN.

| Surface | Frozen census (per doc) | Why RED |
|---|---|---|
| **Scala build-bootstrap** | 691 scoped Scala files · 166 `def` · 10 declared Frame results · 124 explicit returns · 2 explicit throws · **0** canonical `Byte.Substrate.Value` descents · 140 direct FQ host-reference lines outside adapter leaves | All 166 callables uncertified; both `(config/Compile/admission)` and `(config/Compile/verifyUnmanaged)` reject: *"Opened descriptor cannot be associated with its source coordinate."* Fresh compiler saw 19,481 Scala + 4 Java (incl 72 generated), then **846 application errors**. `Bootstrap/Carrier/Unverified` records debt, not proof. |
| **Python** | 1,191 `.py` (1,141 ≤ pylib, 50 outside) · production frontier 59 files · 1,082 ≤ `pylib/reference` · 342 `def` incl **236 raw `Bytes→Bytes` arrows** · 382 external-gate import lines · 0 wildcard imports · **no `pyproject.toml`** · all 59 import a `config` pkg absent from `pylib/src` | Missing package + launcher + typed readback; import lines are "spelling evidence only"; per §law-clause 14 a `.py` under `scripts/python` is **not executable** until integrated in the registered `scripts/python/pylib` tree. |
| **Lambda-Blotto** | 68 files · 771 physical lines · 9 unary Frame arrows · 9 exact output+effect Frames | Parser + static checks pass but "the modes are relays"; role-vector input, current heat, independence, Narrow/Wide, allocation, Complete, proof, receipt, root input, and **tests absent**. Chain `Heat→S→O→P→Δ→Σ→Π→Hybrid→…→Barrier→Wingtip refusal→Continue` does not make it green. |
| **Bash** | 15 Bash files · 702 lines · 12 declared functions · 27 callable entrances · 4 shell contract-coordinate declarations · 3 source/dot bindings | 26 of 27 callables lack the four typed bindings → `Shell.Callable.Contract.Absent.Value`; 5 files have plural defs → `Shell.Definition.Cardinality.Value`; `ci.sh`'s 4 callables (`ci_finish`/`wire`/`fail`/top-level) all multi-stage; `fail`'s `exit` is an untyped effect. Only the new `…/launcher/value.sh` is lawful. |
| **Scala/Java scanner surface** | scanner covers Scala `def`, extension methods, callable `val`/lambdas + Java methods/constructors/SAM | "Language-neutral frontend evidence and positive typed external admission/readback remain absent." `Registration.Admission.Apply` still returns **Rejected**. Enforcement fails its own law. |
| **Finding families** (must exist & stay red until cured) | `Import.Binding.Wildcard.Present.Value`, `Import.Binding.Explicit.Absent.Value`, `External.Binding.Contract.Gate.Absent.Value`, `Definition.Authority.Inferred.Value`, `Shell.Definition.Cardinality.Value`, `Shell.Callable.Contract.Absent.Value`, `Shell.Expansion.Wildcard.Present.Value` | These have Type/URN identities now but positive typed admission/readback is still missing. |

Additional sealed-closure obligations still RED (targets, not yet met): the
5-state **Sealed Self-Hosting Closure** (pinned Spark/Joern bytes → owned CPG →
owned twin compiles repo → twin compiles itself → deterministic readback digest
equality); the **Split ⇄ Consolidated Render Seal**
(`consolidate(split(g))==g` and `split(consolidate(g))==split(g)`); the
**Complete Component Account** (content-addressed predecessor/successor row per
entry); and the **Byte-Stream Carrier Closure** (bit/byte initial algebra,
1..128 width, 256 count, 255 ordinal as three distinct coordinates).

### 4.1 Staleness reconciliation (IMPORTANT for X)

The doc's Python receipt is dated **2026-07-16** and is now **materially
stale**. Measured today (2026-08-07):

| Metric | Doc (2026-07-16) | Live now |
|---|---|---|
| `scripts/python` total `.py` | 1,191 | **6,140** |
| under `pylib` | 1,141 | **6,090** |
| `pylib/src` `.py` | 59 (production frontier) | **5,259** |
| `pylib/reference` `.py` | 1,082 | **719** |
| outside pylib | 50 | **50** (unchanged) |
| `config` package in `src/` | **absent** | **PRESENT** (constants 1,858 + gate 1,124) |
| `pyproject.toml` | absent | **still absent** |
| `def` count in `pylib/src` | 342 (whole pylib) | **2,589** (src only) |

So between the frozen receipt and now, X (or a precursor) **already built out
the sparky engine and the `config/{constants,gate}` package** — repairing the
"config absent" red item and shrinking `reference/` from 1,082 → 719. What
remains RED and unrepaired: **no `pyproject.toml`**, **no admitted interpreter
launcher / typed readback** (per `LIVE_PROMOTION_RECEIPT.md` and
`INTEGRATION_AUDIT.md` gaps: linearity, whole-payload bound, wire emission,
kernel snapshot), the reserved-keyword `lambda/` twins, and the entire
Scala/build/Lambda-Blotto-completion surface. Treat the §4 table as the *frozen
target list* but re-census before claiming any line green.

---

## 5. PROVISIONAL items (Präriehund — named gaps, not force-fit)

1. Continuation docs `…-enforcement-proof.md` / `…-receipts.md` — **absent**;
   may exist outside this checkout. All §4 numbers rest on the single index doc.
2. Exact pickle de-mux count: **5 observed, brief said 3** — either brief is
   stale or counts one family (equality vs mutation).
3. `sparky/lambda/` (keyword twin) live-reachability vs orphaned — unresolved;
   disposition = migrate/retire pending inverse.
4. The sbt Scala engine (`modules/`, `build.sbt`, `cli/`) referenced by `ci.sh`
   and the build-bootstrap receipt is **not in this working tree** — likely a
   submodule/sibling repo.
5. `reference/pylib/reference/config/constants/aob/layout/*` hyphenated
   projection constants (`daedalus`/`icarus`/`ossie`/`yggdrasil`) — meaning
   unresolved, no live analogue; keep provisional.
6. "~100% unary-conformant" = pass state of the **file-capture/Lambda-Blotto
   static gate** over its captured operation set; it is **not** a whole-tree
   proof of all 2,277 sparky files, and explicitly not the sealed-closure
   proof (§4 seals remain open).

---

*Silmaril · GraphAtlas · Apache 2.0 — "Inspizierbar. Revidierbar. Föderiert."*
