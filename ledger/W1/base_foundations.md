# W1 DISCOVERY LEDGER — `forge/base` (the turtle-tower foundation corpus)

Synthesis of W1 Task 2: full-capture map of the `forge/base` submodule tower and its
category-theory foundations corpus. Merged from the two mapper fragments
(`t2-frag-000-t2-slice-000.md`, 40 files; `t2-frag-001-t2-slice-001.md`, 10 files),
every file of which was read to EOF (every PDF paged through the Read tool's `pages`
parameter, every page; every `.tex` read in full; every `.git`/`.gitmodules`/LICENSE/
README read in full). Companion byte-anchor manifest:
`ledger/W1/manifests/base_tower.manifest` (50 lines == 50 inventory files;
`COVERAGE EXACT`).

Framing law read in full first, per Global Constraint 1:
`docs/praeriehund-demokratie-der-kategorien.md` + `docs/unary-byte-frame-law.md`.

Discipline applied: `>` blocks are verbatim source quotes; lines tagged **[inference]**
are marked interpretation; **[skew]** marks plainly-recorded version/naming/license facts
(recorded, not editorialized, per brief requirement (a)); **PROVISIONAL** appears only for
genuinely unresolvable unknowns, each carrying a documented gap (collected in §6). Nothing
in this map contradicts a fragment; the one brief-vs-live discrepancy (base's own pin) was
re-verified against live git and is recorded as found (§1, §2.4, §7).

All 50 file digests were independently recomputed by the synthesizer (`sha256sum` + byte
count over the live tree) and matched the fragment-manifest union **exactly** — the
fragment manifests are byte-accurate.

---

## 1. CORPUS IDENTITY

| coordinate | value (verified live) |
|---|---|
| repo | `forge/base` — GitHub `groenewt/base` **[inference]** (see §2.2; base's own `.gitmodules` names only its children, but the sibling `base_*` naming and the submodule urls establish the `groenewt/base` family) |
| pinned SHA (silmaril's index gitlink for `forge/base`) | `c4e828188a57d7a93c4f4972859dd0862ae6cce6` (verified: `git -C silmaril ls-files -s forge/base` **and** `git -C forge/base rev-parse HEAD` both return this) |
| **brief-asserted SHA (DISCREPANCY)** | brief said `9e60c103e3f6a41cc78e6dee40aeeded133e2eb9`; **that object does not exist in the `forge/base` repo** (`git cat-file -t` fails; `merge-base --is-ancestor` reports "Not a valid commit name"). Recorded as found: the live pin is `c4e82818`, not `9e60c103`. See §2.4 and §7. |
| HEAD commit subject | `c4e8281 agents cleaner` |
| file count (find, excluding `.git/` plumbing) | **50** |
| direct-tree size | tiny — every leaf file is a README/LICENSE/`.git`-pointer/`.gitmodules` or a foundations doc; the four PDFs (113 KB, 158 KB, 223 KB, 198 KB) and the four `.tex` sources dominate the byte weight |
| licenses present (as found) | **GPLv2** (base, bin, docs, specs — 4 byte-identical copies), **Apache 2.0** (agents), **BSD 3-Clause** (templates). See §2.6. |

`forge/base` is itself a submodule of the `silmaril` superproject (its `.git` is a
one-line gitlink pointer, not a directory). It is a **thin structural repo**: two payloads
only — (i) a seven-child submodule tower (the "turtles"), and (ii) a single foundations
corpus under `docs/mythology/silmaril/foundations/` (the category-theory papers, the
`AGENT.md` executable head, and the ten `skills/**/*.md` skill definitions). README top line:

> `# base`
> `Base GA Repo`

---

## 2. THE TOWER GRAPH AS FOUND (brief requirement (a); own top-level section)

### 2.1 Nesting levels (physical, from the `.git` gitlink pointer files)

Every checked-out submodule carries a `.git` **file** (not directory) of the form
`gitdir: <relative path into the superproject module store>`. The `modules/.../modules/...`
nesting in each pointer physically encodes the tower depth. Gitlink pointers as found
(verbatim final line of each):

| path | `gitdir:` target (verbatim) | level |
|---|---|---|
| `forge/base/.git` | `../../.git/modules/forge/base` | base is L1 (a submodule of silmaril) |
| `forge/base/external/.git` | `../../../.git/modules/forge/base/modules/external` | L2 |
| `forge/base/forge/agents/.git` | `../../../../.git/modules/forge/base/modules/forge/agents` | L2 |
| `forge/base/forge/bin/.git` | `../../../../.git/modules/forge/base/modules/forge/bin` | L2 |
| `forge/base/forge/core/.git` | `../../../../.git/modules/forge/base/modules/forge/core` | L2 |
| `forge/base/forge/docs/.git` | `../../../../.git/modules/forge/base/modules/forge/docs` | L2 |
| `forge/base/forge/specs/.git` | `../../../../.git/modules/forge/base/modules/forge/specs` | L2 |
| `forge/base/forge/templates/.git` | `../../../../.git/modules/forge/base/modules/forge/templates` | L2 |
| `forge/base/forge/agents/core/.git` | `../../../../../.git/modules/forge/base/modules/forge/agents/modules/core` | **L3** (under agents) |
| `forge/base/forge/agents/docs/.git` | `../../../../../.git/modules/forge/base/modules/forge/agents/modules/docs` | **L3** (under agents) |

**[inference]** the `../` depth of each pointer matches the physical directory depth of the
submodule; this is the standard git submodule layout, confirmed consistent across all nine
gitlink pointers.

Tree shape:

```
silmaril (superproject, L0)
└── forge/base                     @ c4e82818   (L1)
    ├── external                   @ 90af0bad   → groenewt/base_external      (L2)
    └── forge/
        ├── agents                 @ 672ba868   → groenewt/base_agents        (L2, embryonic: 4 tracked files)
        │   ├── core               @ 3f90564c   → groenewt/core               (L3)
        │   ├── docs               @ 661af74e   → groenewt/base_agents_docs   (L3)
        │   └── sbin               @ 6525c556   → (NO .gitmodules mapping)     (L3, index gitlink only; mount dir empty)
        ├── bin                    @ 6525c556   → groenewt/base_bin           (L2)
        ├── core                   @ 3f90564c   → groenewt/core               (L2)
        ├── docs                   @ 1cf127f6   → groenewt/base_docs          (L2)
        ├── specs                  @ 469bb24f   → groenewt/base_aobs          (L2)
        └── templates              @ 2d84826c   → groenewt/base_templates     (L2)
```

### 2.2 `.gitmodules` declarations — QUOTED IN FULL (brief requirement (a))

**`forge/base/.gitmodules`** (638 bytes, sha `6cff4f02…`) — declares 7 L2 submodules,
all under `https://github.com/groenewt/`:

> `[submodule "forge/core"]`
> `	path = forge/core`
> `	url = https://github.com/groenewt/core`
> `[submodule "forge/docs"]`
> `	path = forge/docs`
> `	url = https://github.com/groenewt/base_docs`
> `[submodule "forge/templates"]`
> `	path = forge/templates`
> `	url = https://github.com/groenewt/base_templates`
> `[submodule "external"]`
> `	path = external`
> `	url = https://github.com/groenewt/base_external`
> `[submodule "forge/agents"]`
> `	path = forge/agents`
> `	url = https://github.com/groenewt/base_agents`
> `[submodule "forge/bin"]`
> `	path = forge/bin`
> `	url = https://github.com/groenewt/base_bin`
> `[submodule "forge/specs"]`
> `	path = forge/specs`
> `	url = https://github.com/groenewt/base_aobs`

Note the declared name `forge/specs` maps to url `base_aobs` — the declared name is not the
upstream repo name.

**`forge/base/forge/agents/.gitmodules`** (230 bytes, sha `952d6884…`) — declares 3
submodules (verified verbatim against live tree):

> `[submodule "core"]`
> `	path = core`
> `	url = https://github.com/groenewt/core`
> `[submodule "bin"]`
> `	path = bin`
> `	url = https://github.com/groenewt/base_bin`
> `[submodule "docs"]`
> `	path = docs`
> `	url = https://github.com/groenewt/base_agents_docs`

### 2.3 Pins recorded (read-only `git ls-files -s` / `submodule status`; all verified live)

`forge/base` index gitlinks (mode 160000) — **all seven match the brief exactly**:

| path | pinned commit | maps to url |
|---|---|---|
| `external` | `90af0bad9bc150c67b996745f0e76865f9e1e4f8` | groenewt/base_external |
| `forge/agents` | `672ba868d768c47f6d5cd616b54a06a080fb26cb` | groenewt/base_agents |
| `forge/bin` | `6525c5569d70deb7ee1391ecd5b236ab3813336a` | groenewt/base_bin |
| `forge/core` | `3f90564c97c6b38f6c59616073957e15eedaae6e` | groenewt/core |
| `forge/docs` | `1cf127f6280edd8b59ab88643043c8b3c02ecc7d` | groenewt/base_docs |
| `forge/specs` | `469bb24fdc5e0ddcf621cf7ce497aa4c37d33c34` | groenewt/base_aobs |
| `forge/templates` | `2d84826c6db49771f64e6bbc39c32af3f6ae278c` | groenewt/base_templates |

`forge/base/forge/agents` index gitlinks (L3) — **all three match the brief exactly**:

| path | pinned commit | note |
|---|---|---|
| `core` | `3f90564c97c6b38f6c59616073957e15eedaae6e` | identical pin to `forge/base`'s `forge/core` (same repo `groenewt/core`) |
| `docs` | `661af74ea3979c94a9c0b823ac318b9d8203c5f7` | groenewt/base_agents_docs |
| `sbin` | `6525c5569d70deb7ee1391ecd5b236ab3813336a` | identical pin to `forge/base`'s `forge/bin` (same repo `groenewt/base_bin`) |

The full L3 agents index (verified) is exactly 6 entries: `.gitmodules`, `LICENSE`,
`README.md`, and the three gitlinks `core`/`docs`/`sbin`. This is the "embryonic, 4 files"
tree (3 tracked blobs + 3 gitlinks; the working tree materializes `.git`, `.gitmodules`,
`LICENSE`, `README.md`, and the two initialized L3 clones `core/` and `docs/`).

### 2.4 The `sbin`/`bin` broken-submodule-record defect (as found)

Inside `forge/base/forge/agents` there is a genuine mismatch between the `.gitmodules`
declaration and the index gitlinks:

- `.gitmodules` maps a submodule named/pathed **`bin`** → `groenewt/base_bin`, but the
  index carries **no gitlink at path `bin`**.
- The index carries a gitlink at path **`sbin`** @ `6525c556`, but **`.gitmodules` has no
  mapping for path `sbin`** — so `sbin` has no declared URL.

So the record is crossed: `bin` = mapping-without-gitlink; `sbin` = gitlink-without-mapping.
The head-commit message on `forge/base` documents the design intent behind this:

> `d6bd3f7 base agent repo submodule setup/// forge/sbin-> forge/bin (super bin used in forge/**/sbin/**)`

Consequence, as found:
- `sbin`'s pin (`6525c556`) **equals** `base_bin`'s pin, so the *content* at that commit is
  fully capturable via `forge/base/forge/bin` at the identical SHA (same repo, same commit).
- `forge/base/.gitignore` ignores `forge/agents/sbin/` (see §2.7), and the `sbin/` working
  directory is an **empty uninitialized mount point** (verified: `find … sbin -type f` → 0
  files) — it therefore contributes nothing to the 50-file census. It **cannot be
  initialized** in place: with no `.gitmodules` URL for path `sbin`, `git submodule init`
  has nothing to clone.
- **PROVISIONAL (§6):** the path defect *itself* — the absence of any URL for the `sbin`
  path record — is genuinely unresolvable from the source; no URL exists for it. (The
  *content* is not lost, only the path-record's own declared origin.)

### 2.5 Version-skew facts (recorded, not editorialized — brief requirement (a))

**Sibling-clone skew — CONFIRMED LIVE (frag-000 left this as synthesis-level; resolved
here).** The `silmaril` superproject mounts the same two taxonomies twice, at two different
commits that co-exist:

| taxonomy (repo) | pin inside `forge/base` (this tower) | pin as silmaril sibling clone | verified |
|---|---|---|---|
| `base_agents` | `forge/base:forge/agents` @ `672ba868` | `silmaril:forge/base_agents` @ `d2b1217f` | `git -C forge/base_agents rev-parse HEAD` = `d2b1217ffb9b48303bb6743ef4a535e3e01a7a2d`; silmaril index pins it @ `d2b1217f` |
| `base_templates` | `forge/base:forge/templates` @ `2d84826c` | `silmaril:forge/base_templates` @ `eb3d916b` | `git -C forge/base_templates rev-parse HEAD` = `eb3d916b0db5c1429e0ce5abaac7b6b75aadea18`; silmaril index pins it @ `eb3d916b` |

**[skew]** Two co-existing versions of the same taxonomies. Recorded as a census-bound
fact, not a problem. (These sibling clones are the W1 targets of Task 1 —
`base_templates` @ `eb3d916b` — and of `ledger/W1/base_agents.md` — `base_agents` @
`d2b1217f`.)

### 2.6 URL-cycle cross-references (shared mounts)

The tower mounts two upstream repos twice each, at identical pins — the "URL-cycle
cross-references" of the tower:

- **`groenewt/core`** is mounted as `forge/base:forge/core` **and** as
  `forge/base/forge/agents:core`, both @ `3f90564c` (same repo, same commit).
- **`groenewt/base_bin`** is mounted as `forge/base:forge/bin` **and** as
  `forge/base/forge/agents:sbin`, both @ `6525c556` (same repo, same commit).

**[skew]** These shared mounts mean the physical directory graph is not a tree of distinct
repos: two nodes are the same upstream at the same commit under two path spellings.

### 2.7 `.gitignore` (verbatim) and its role

`forge/base/.gitignore` (45 bytes, sha `dc623419…`), 3 lines:

> `*/.gitmodules`
> `forge/sbin/`
> `forge/agents/sbin/`

- `forge/agents/sbin/` is exactly the materialized-but-empty `sbin` mount from §2.4; this
  ignore rule keeps the crossed `sbin` mount out of ordinary status.
- `forge/sbin/` is a *preemptive* ignore — no such directory is materialized (verified:
  `forge/base/forge/` contains only `agents bin core docs specs templates`; no `sbin`).
- `*/.gitmodules` ignores nested `.gitmodules` one level down.

### 2.8 License skew across the tower (recorded, not editorialized — brief requirement (a))

Six LICENSE files, **three** distinct licenses:

| path | license | sha256 | bytes |
|---|---|---|---|
| `forge/base/LICENSE` | GNU GPL v2 | `8177f975…` | 18092 |
| `forge/base/forge/bin/LICENSE` | GNU GPL v2 (byte-identical) | `8177f975…` | 18092 |
| `forge/base/forge/docs/LICENSE` | GNU GPL v2 (byte-identical) | `8177f975…` | 18092 |
| `forge/base/forge/specs/LICENSE` | GNU GPL v2 (byte-identical) | `8177f975…` | 18092 |
| `forge/base/forge/agents/LICENSE` | Apache License 2.0 | `c71d239d…` | 11357 |
| `forge/base/forge/templates/LICENSE` | BSD 3-Clause | `6de269db…` | 1505 |

- The four GPLv2 copies are the verbatim FSF template with the placeholder appendix intact
  (`Copyright (C) <year>  <name of author>`) — **no** project-specific copyright holder
  filled in.
- The BSD 3-Clause (templates) **is** filled in: > `Copyright (c) 2026, Tristan Groenewold`.
- The Apache 2.0 (agents) is the full standard text.

**[skew]** The foundations corpus in this same tower repeatedly names an **Apache**
commitment (IV-turtles §14.5 "The Apache commitment — open license, federated governance";
the Präriehund doctrine's "Hansestadt-Modell (Apache 2.0)"). Recorded as a plain fact: the
base/bin/docs/specs repos ship **GPLv2**, templates ships **BSD 3-Clause**, and only agents
ships **Apache 2.0**, while the doctrine prose describes Apache 2.0 throughout. Not
reconciled; recorded as found.

---

## 3. TAXONOMY TREE AS FOUND (from the inventory, not from `ls`)

The 50 files, by region. `(gl)` = git gitlink pointer file; `(sub)` = submodule root.

```
forge/base/
├── .git            (gl → ../../.git/modules/forge/base)
├── .gitignore
├── .gitmodules     (7 L2 submodules)
├── LICENSE         (GPLv2)
├── README.md       ("# base / Base GA Repo")
├── docs/mythology/silmaril/foundations/          ← THE FOUNDATIONS CORPUS
│   ├── AGENT.md                                   (executable head: agent = bialgebra)
│   ├── README.md                                  (bundle index; numbering I,II,IV,V — III absent)
│   ├── I-fundamenta/
│   │   ├── graphatlas-fundamenta.pdf              (5 pp; Latin; Yoneda+Lambek)
│   │   └── graphatlas-fundamenta.tex
│   ├── II-en/
│   │   ├── graphatlas-foundations-en.pdf          (10 pp; English tragedy)
│   │   └── graphatlas-foundations-en.tex
│   ├── IV-turtles/
│   │   ├── silmaril-foundations-iv-turtles.pdf    (23 pp; eleven strata)
│   │   └── silmaril-foundations-iv-turtles.tex    (largest source, 70704 B)
│   ├── V-polysemy/
│   │   ├── silmaril-foundations-v-polysemy.pdf    (11 pp; algebra as polysemy)
│   │   └── silmaril-foundations-v-polysemy.tex
│   └── skills/
│       ├── README.md                              (skills = morphisms in premonoidal Sk)
│       ├── core/compose.md   core/lift.md   core/parallel.md
│       ├── effects/kleisli.md
│       ├── federate/sheaf.md
│       ├── forge/generate.md
│       ├── games/equilibrium.md
│       ├── observe/coalgebra.md
│       ├── optics/lens.md
│       └── provenance/semiring.md
├── external/       (sub: base_external @90af0bad)  → .git(gl), README.md
└── forge/
    ├── agents/     (sub: base_agents @672ba868)     → .git(gl), .gitmodules, LICENSE(Apache2), README.md
    │   ├── core/   (sub L3: core @3f90564c)          → .git(gl), README.md("# core")
    │   ├── docs/   (sub L3: base_agents_docs @661af74e) → .git(gl), README.md
    │   └── sbin/   (EMPTY mount; gitlink @6525c556; no .gitmodules mapping; 0 files)
    ├── bin/        (sub: base_bin @6525c556)         → .git(gl), LICENSE(GPLv2), README.md
    ├── core/       (sub: core @3f90564c)             → .git(gl), README.md("# core")
    ├── docs/       (sub: base_docs @1cf127f6)        → .git(gl), LICENSE(GPLv2), README.md
    ├── specs/      (sub: base_aobs @469bb24f)        → .git(gl), LICENSE(GPLv2), README.md
    └── templates/  (sub: base_templates @2d84826c)   → .git(gl), LICENSE(BSD3), README.md
```

The submodule leaf clones are **shallow identity stubs**: each L2/L3 clone that is
initialized carries only its `.git` pointer plus a README (and, for bin/docs/specs/
templates/agents, a LICENSE). None of the deep content of those upstream repos is present
in this tower at these pins — the tower is a *skeleton of pins*, not a fetched monorepo.
The one repo with real payload at this pin is `forge/base` itself, via the foundations
corpus under `docs/mythology/silmaril/foundations/`.

Submodule-root README identities (verbatim), consolidated:

| submodule | README top line(s) |
|---|---|
| `external` | `# base_external` / `Base GA External` |
| `forge/agents` | `# base_agents` / `Base GA Agents Implementation` … `# EXPORTS:` / `submodule:base_agents_docs --> docs` |
| `forge/agents/core` | `# core` (6 bytes, no trailing newline) |
| `forge/agents/docs` | `# base_agents_docs` / `Base GA Agents Implementation Documentation` |
| `forge/bin` | `# base_bin` / `Base GA Bin` |
| `forge/core` | `# core` (6 bytes, no trailing newline; byte-identical to agents/core README) |
| `forge/docs` | `# base_docs` / `Base GA Doc repo` |
| `forge/specs` | `# base_aobs` / `Base AOBs` |
| `forge/templates` | `# base_templates` / `Base GA Templates` |

`forge/agents/README.md` uniquely carries an export declaration:
> `submodule:base_agents_docs --> docs`
matching the `docs` submodule in `agents/.gitmodules` (groenewt/base_agents_docs, gitlink
@661af74e). `forge/agents/core/README.md` and `forge/core/README.md` are byte-identical
(both sha `e2662f1d…`, 6 bytes, `# core`) — consistent with both being the same upstream
`groenewt/core` @ `3f90564c` (§2.6).

---

## 4. THE FOUNDATIONS CORPUS — DEEP ACCOUNT (brief requirements (b), (c), (d))

The corpus motto (`foundations/README.md`, sha `2ce6bfca…`):
> `identity is the totality of morphisms (Yoneda); no self-totalization (Lawvere–Girard); the regress is the ontology; algebra is polysemy — one theory, many functorial projections.`
> `*Nihil occultum, tantum textum. — Nothing hidden, only woven.*`

Reading orders it prescribes:
> `Philosophy-first: II → IV → V. Math-first: I → V → IV. Engineering-first: AGENT.md → skills/ → V.`

**[skew]** The bundle numbers its documents **I, II, IV, V** — there is **no `III-*`
document** in the tree (the README table jumps I → II → IV → V; no `III-` directory exists
under `foundations/`). Recorded as found.

### 4.1 `AGENT.md` — "The Algebra of Agents" (executable head; read IN FULL, req. (d))

4623 bytes, sha `5d191950…`. Epigraph:
> `An agent is not a thing that has behaviors. An agent **is** a carrier glued between a syntax algebra and a behavior coalgebra by a distributive law. Identity is bisimilarity. Nothing else is postulated.`

- **§0 Signature** (verbatim): > `Agent := (X, α: Σ X → X, β: X → B X, λ: Σ(Id × B) ⇒ B Σ*)` — `X` carrier; `Σ` action grammar/signature endofunctor with free monad `Σ*`; `α` construction/Σ-algebra; `B` observation/behavior endofunctor; `β` dynamics/B-coalgebra; `λ` abstract GSOS distributive law.
- **Theorem (Turi–Plotkin 1997):** initial Σ-algebra carries a unique B-coalgebra (operational model); final B-coalgebra carries a unique Σ-algebra (denotational model); the unique bialgebra map is the interpretation; **bisimilarity is a congruence**. > `Compositionality is not engineered; it is purchased once, by λ.`
- **§1 Identity law:** two agents identical iff bisimilar. > `any agent attribute that changes behavior but is not observable through B is smuggled essence — reify it into B or delete it.`
- **§2 Effect discipline:** effectful capability = Kleisli morphism `A → T B` for strong monad `T` (Moggi). Fibers: `S ⇒ (− × S)` state; `P` nondeterminism; `D` probability; `− + E` failure; `(− → R) → R` control. Handlers = homomorphisms from the free model (Eilenberg–Moore); effects = Lawvere theory (Plotkin–Power).
- **§3 Composition laws:** Sequential `>>>` (Kleisli/arrow, assoc/unital); Parallel monoidal `⊗` (string diagrams, Joyal–Street); Bidirectional agent-as-optic play/coplay, open games (Ghani–Hedges) `G = (strategies, play, equilibrium)`; Interface as polynomial `p = Σᵢ y^{p[i]}` (Niu–Spivak, **Poly**), > `a polynomial comonoid is a category`; Protocol/session type = linear-logic proposition (Caires–Pfenning, Wadler), deadlock-freedom = cut elimination.
- **§4 Boundary law:** > `No agent contains its own totality.` A self-model is licensed (helix; Aczel-consistent hyperset); a *total* self-model is Girard's `Type : Type` and detonates; introspection stratifies, federation reflects (Feferman).
- **§5 Inference stance (optional):** Bayesian agent = Bayesian lens; active inference = statistical game over Poly (Smithe — flagged research frontier, not settled theorem).
- **§6 Conformance checklist (6 items):** declare Σ,B,λ in GSOS format; all state distinctions observable via B (no svabhāva); effects typed by T, handlers total; protocols session-typed; self-reference climbs a level; > `Every skill invoked is a morphism in the skill category (see skills/README.md) — the agent is the runtime of the skill algebra, not its owner.`
- FINAL LINE: > `*The agent is the jam, not the score: syntax proposes, observation disposes, the distributive law keeps them honest.*`

Cross-refs (source-named): `skills/README.md`, `skills/**/*.md`. The (Σ,B,λ) bialgebra here
is the same structure elaborated in V-polysemy Part A and I-fundamenta Scholium 9.

### 4.2 I-fundamenta — `graphatlas-fundamenta.tex` (11306 B, sha `2bf4c036…`) + PDF (5 pp, sha `c5ffa289…`)

Latin. Document class article 11pt, babel `[latin,english]`, custom theorem envs. Title
"Fundamenta Mathematica GraphAtlas", author GraphAtlas/Silmaril, date MMXXVI. Abstract:
two theorems making the GraphAtlas architecture *necessary* — (Primum) Yoneda ⇒ an object's
identity is contained in the totality of its morphisms; (Secundum) Lambek ⇒ `X ≅ F(X)` is a
categorical necessity, not the architect's choice.

- **§1 Praeliminaria:** **Def 1** locally small category; **Def 2** representable functor `h_A := Hom_C(-,A): C^op → Set`; **Def 3** natural transformation, `Nat(F,G)`.
- **§2 Lemma Yonedae — Lemma 4 (Yoneda):** `Φ: Nat(h_A,F) → F(A), Φ(η) := η_A(id_A)` a bijection natural in both A and F. Full proof: inverse `Ψ(x)_B(f)=F(f)(x)`; `Φ∘Ψ=id`; `Ψ∘Φ=id` by identity-chase; > `unum punctum totum determinat`. **Cor 5 (Immersio Yonedae plene fidelis):** Yoneda embedding fully faithful, `A ≅ B ⟺ h_A ≅ h_B`. **Consectarium Ontologicum:** > `identitas obiecti nihil aliud est quam totalitas morphismorum eius`; (a) Nodus = neighbourhood of morphisms; (b) Inspectabilitas = completudo — an opaque system asserting essence beyond inspectable relations `vel errat vel mentitur` (either errs or lies); (c) Reproducibilitas ⇒ Hanseatic federation without central authority.
- **§3 Theorema Lambekii — Def 6** F-algebra `(X, α: F(X)→X)`, initial algebra; **Theorema 7 (Lambek 1968):** initial F-algebra ⇒ `α` iso, `X ≅ F(X)` (full 3-step proof `i=α⁻¹`). **Cor 8** necessitas puncti fixi. **Scholium 9 (De classe fundamentali Silmaril):** > `Classis fundamentalis Silmaril, quae structuram X ≅ F(X) realizat, per Theorema Lambekii non electio architecti sed necessitas categorica est.` Adds the Turi–Plotkin bialgebra (initial Σ-algebra + terminal B-coalgebra coupled by `λ: Σ(B × id) ⇒ BΣ*`). Closing: > `Quod inspici potest, omne est.`
- PDF-only (page reads) confirms: title block "Fundamenta Mathematica GraphAtlas / De Lemmate Yonedae et Theoremate Lambekii / Silmaril Foundations Series / … / MMXXVI"; resolved Contents; typeset tikz-cd commuting squares; small-caps `Q.E.D. — ET QUOD ERAT CONSTRUENDUM` on p5, preceded by `Quod inspici potest, omne est.`
- `.tex` FINAL LINE: `\end{document}`.

### 4.3 II-en — `graphatlas-foundations-en.tex` (29605 B, sha `73c93269…`) + PDF (10 pp, sha `0a95ace1…`)

English retelling of I-fundamenta staged as a classical tragedy. Abstract's dramatic
mapping: substance metaphysics = protagonist; hamartia = belief in hidden essence;
anagnorisis = Yoneda; peripeteia = Lambek's fixed point; exodos = federated inspectable
knowledge graph. Full proofs for Yoneda, density, Lambek, Lawvere; Adámek and Turi–Plotkin
sketched.

- **Prologos: The Question** — Heraclitus vs Parmenides; Aristotle *Categories*, ousia/hypokeimenon vs pros ti. Hamartia: > `the thing is prior to its relations; the relations are decoration on an essence that could stand alone.` > `The answer is no, and the refutation is a bijection.`
- **Act I: The Long Siege** — Ockham nominalism; Leibniz identity of indiscernibles `A = B ⟺ ∀P(P(A)↔P(B))`; Kant *Ding an sich*.
- **Act II: Algebra Learns to Forget** — Galois (1832) forgot the roots; Noether (1920s) forgot the elements; Eilenberg–Mac Lane (1945) forgot the structures. **Def** category; **Def** presheaf/representable `h_A`, `h_•: C → [C^op,Set]`.
- **Act III: Anagnorisis — Yoneda (1954)** — bijection natural in A,F, full proof; > `one point determines the totality.` **Cor** fully faithful. > `substance, examined with full rigor, decomposes without remainder into relation.` **Theorem (Density)** `F ≅ colim_{(A,x)∈∫F} h_A`, full proof. **Scholium (chorus):** density = license for federation, no central node.
- **Act IV: Peripeteia — Lambek (1968)** — `X ≅ F(X)`, full proof; > `The architect's freedom, examined with full rigor, decomposes into necessity.` **Theorem (Adámek)** initial-chain colimit (sketch).
- **Act V: The Fate Mechanism — Lawvere's Diagonal** — **Theorem (Lawvere fixed-point)** full diagonal proof; **Cor (Cantor)** no surjection `A → 2^A`; **Scholium:** construction = induction into initial algebra, observation = coinduction out of terminal coalgebra.
- **Act VI: Synthesis — the Bialgebra** — abstract GSOS `λ: Σ(Id × B) ⇒ BΣ*`; **Theorem (Turi–Plotkin 1997)** bisimilarity a congruence. Apollo (initial algebra/score) married to Dionysus (terminal coalgebra/jam) by λ.
- **Exodos: GraphAtlas** — verdicts as spec: opacity is a metaphysical error not security (Yoneda); Hanseatic federation sufficient (density); `X ≅ F(X)` forced (Lambek/Adámek); self-reference governed by law, stratify (Lawvere); audit is compositional (Turi–Plotkin). > `deliver the field, expose the morphisms, and let the observer collapse where they will.`
- PDF-only confirms: title "Identity Is the Totality of Arrows / The Mathematical Foundations of GraphAtlas, Told as the History of Philosophy and Algebra"; resolved Contents w/ act subtitles + page numbers; the `∫ F` category-of-elements colimit typeset; p10 Ozymandias-allusion paragraph (> `Round the decay of that colossal wreck of hidden essences … the open, inspectable, federated arrows stretch far away.`) then `QUOD ERAT DEMONSTRANDUM — ET QUOD ERAT CONSTRUENDUM`.
- `.tex` FINAL LINE: `\end{document}`.

### 4.4 IV-turtles — `silmaril-foundations-iv-turtles.tex` (70704 B, sha `fe0b7547…`; largest source) + PDF (23 pp, sha `037a6042…`)

"Turtles All the Way Down / The Regress as Ontology: Eleven Strata of the Yoneda Principle,
and the Law That Forbids a Bottom." Thesis (abstract): > `there is no bottom turtle, and
that is a feature, not a bug`; > `The regress is the ontology.` Two recurring masks: the
**Yoneda principle** (identity exhausted by morphisms of that level) and the **boundary
law** (Lawvere/Girard diagonal forbidding self-containment).

- **Prologue: The Anecdote's Own Regress** — the "turtles all the way down" story has no bottom source (Hawking 1988 → Russell 1927 → NY Mirror 1838 "rocks" → Berg 1854 → James 1882 → Ross 1967; world-turtle Kūrma).
- **Stratum 0: Sets, Three Cosmologies** — (2.1) well-founded ZFC Foundation, `V` = initial algebra of powerset; (2.2) structural ETCS (Lawvere 1964), `is 2 ∈ 3?` ungrammatical; (2.3) anti-founded **Axiom 2.1 (AFA; Aczel 1988)**, `Ω = {Ω}` unique; **Theorem 2.2** under AFA the universe is the *final* coalgebra of powerset, under Foundation the *initial* algebra — exact categorical duals. Refrain: > `Self-membership is negotiable. Self-totalization is not.`
- **Stratum 1: Yoneda base case** — **Theorem 3.1**; "relative to which category?" launches the tower (`C` in `Cat` in `CAT`).
- **Stratum 2: Enriched Yoneda** — **Def 4.1** V-category; **Theorem 4.2 (Kelly 1982)**; **Prop 4.3 (Self-enrichment)** every closed monoidal V is a V-category. > `The turtle is enriched over itself.`
- **Stratum 3: n-Ladder** — bicategorical Yoneda; **Theorem 5.1 (∞-Yoneda; Lurie HTT 2009, 5.1.3.1)**; machine-checked by Kudasov–Riehl–Weinberger (CPP 2024) in Rzk. > `The machine has checked the anagnorisis.`
- **Stratum 4: Univalence** — `Id_A(x,y)` as path space; **Axiom 6.1 (Univalence; Voevodsky)** `Id_U(A,B) ≃ (A ≃ B)`; universes stratified `U0:U1:U2:…`; `U:U` forbidden.
- **Stratum 5: The Boundary Law** — **Theorem 7.1 (Lawvere 1969)**, five costumes (Cantor, Russell, Tarski, Gödel, Turing); **Theorem 7.2 (Girard 1972 / Hurkens 1995)** `Type:Type` ⇒ inconsistent. > `The infinite regress of universes is not a failure of imagination … It is theorem-enforced.` > `He who would stand on his own shell falls through it.`
- **Stratum 6: Universes, Size, Federation by Reflection** — **Def 8.1** Grothendieck universe; Grothendieck (inaccessibles) vs Feferman reflection `(s,∈) ≺ (V,∈)`. > `A universe tower founded on reflection is a tower of mirrors, not of masses` (Indra).
- **Stratum 7: The Topos** — **Def 9.1** elementary topos, `⊤: 1 ↣ Ω`; internal Heyting logic; > `a topos is a formal system that hosts its own semantics`; engineering translation: a knowledge graph carrying its own schema/access-logic/lineage is the topos pattern (self-hosting metadata).
- **Stratum 8: Iterated Yoneda** — **Theorem 10.1 (Free cocompletion)**; **Theorem 10.2 (Isbell duality)** presheaves ⊣ copresheaves; Lawvere space↔quantity.
- **Stratum 9: The Microcosm Principle** — **Scholium 11.1 (Baez–Dolan 1998)**; helix vs forbidden circle. > `The microcosm principle is the positive face of Girard's paradox.`
- **Stratum 10: The Proof-Theoretic Tower** — Gödel's 2nd incompleteness; Gödel hierarchy of consistency strengths, empirically linear; > `coherentism with theorems.` > `No bottom turtle. Turtles all the way down. And the house stands.`
- **Second Movement (13.1–13.7): The Excavation** — Nāgārjuna emptiness / svabhāva (MMK 24.18; Posina–Roy Brill 2024; Priest 2009; Friend 2024 OSR); Indra's Net (Huayan/Fazang) = presheaf category, jewel = `h_A`; Leibniz *Monadology* perceptions = `h_A`, pre-established harmony = naturality; Whitehead *Process and Reality* occasion = colimit; Structuralism (Benacerraf 1965, Awodey); Ontic structural realism (Ladyman/Ross 2007, French 2014, "relations without relata"); regress debates (Agrippan/Münchhausen trilemma, Klein infinitism, Schaffer vs Tahko, Hofstadter). > `The self is its arrows too.`
- **Exodos (14.1–14.6): GraphAtlas — The Tower as Specification** — node identity = its typed morphism-profile; > `if any node acquires meaning that cannot be reconstructed from its edges … the design has smuggled in svabhāva`; self-hosting metadata as controlled hyperset; federation by reflection not authorities: > `Palantir's architecture is refuted by a type theory.`; univalence as merge policy; **§14.5** > `The Apache commitment — open license, federated governance, no unauditable stratum — is the tower's final translation.`; Curtain: > `Being is the deferral … woven all the way down, and all the way up, forever.`
- Appendix A "Sources and Further Descent" (physically the final PDF page, p23), terminating: `Whitehead, Process and Reality, 1929. Auxier–Herstein, The Quantum of Explanation, 2017.`
- `.tex` FINAL LINE (read across two windows to line 444): `\end{document}`.

### 4.5 V-polysemy — `silmaril-foundations-v-polysemy.tex` (34872 B, sha `3a79d06e…`) + PDF (11 pp, sha `f76272de…`)

"Algebra as Polysemy / AGENT.md, skills/**/*.md, and the One Structure Wearing Many Faces."
Thesis: turns Yoneda "sideways" — one Lawvere theory known by the totality of its models;
> `Polysemy is functorial.` Three fused movements: Part A (AGENT.md algebra), Part B (skills
algebra), Part C (extended Rosetta Stone). > `Build below the boundary; project, do not
totalize.`

- **Stratum 0** — the boundary restated (work below `U:U`; polysemy is the escape).
- **Stratum I: Functorial Semantics — The Spine** — **Def 2.1** Lawvere theory / model (finite-product-preserving `M: T → Set`); Lawvere 1963; > `Yoneda for theories`; Birkhoff HSP; operads/PROPs; Segal–Atiyah TQFT. Refrain: > `theory = category, meaning = structure-preserving functor, polysemy = the model class.`
- **Part A (AGENT.md):**
  - **II Process Calculi** — CCS/CSP/π/ACP; bisimulation (Park/Milner); SOS (Plotkin); GSOS ⇒ congruence. > `Congruence is the whole game`.
  - **III Bialgebraic account (Turi–Plotkin)** — abstract GSOS `λ: Σ(Id×B) ⇒ BΣ*`; **Theorem 4.1 (Klin TCS 2011)** bisimilarity a congruence. > `An agent is initial-algebra syntax + final-coalgebra behavior, glued by a distributive law.`
  - **IV Agents as Coalgebras** — Rutten 2000; species table (`X^A` streams, `2×X^A` Moore, `(PX)^A` LTS, `D(X)` Markov, `D(X)^A` probabilistic LTS); coalgebraic modal logic (Moss ∇).
  - **V Effects as Monads (Moggi)** — Kleisli; T-table (state, nondet `PX`, probability `DX` Giry, continuation, exception); algebraic effects (Plotkin–Power); Kleisli = free algebras, Eilenberg–Moore = handlers.
  - **VI Compositional Structure** — Baez–Stay Rosetta Stone (Set "the odd man out: cartesian"); decorated cospans; lenses/optics (Riley, Clarke, Boisseau–Gibbons — representation theorem "literally Yoneda"); open games (Ghani–Hedges–Winschel–Zahn); polynomial functors (Niu–Spivak, Poly), > `a polynomial comonoid is exactly a category`; Myers categorical systems theory.
  - **VII Resources, Sessions, Protocols** — linear logic (Girard 1987); no-cloning as no-diagonal; session types = propositions (Caires–Pfenning, Wadler).
  - **VIII Bayesian Agents / Active Inference** — Smithe; Bayesian lenses / statistical games over Poly; > `a frame, not yet a theorem, and flagged as such.`
- **Part B (skills/):**
  - **IX Skills as Morphisms** — arrows (Hughes 2000: `arr`, `⋙`, `first`); **Theorem 10.1 (Atkey ENTCS 2011)** arrows = enriched Freyd categories, arrows ⊋ Freyd ⊋ strong monads; Jacobs–Heunen–Hasuo (arrow = monoid in profunctors).
  - **X Skills as Operad and Forge** — operad of wiring diagrams; skills as initial-algebra unfolding `μF ≅ F(μF)` (Lambek), free monad `F*`; > `a skill library is a bialgebra`; > `AGENT.md and skills/**/*.md are one bialgebra seen from two sides: what acts, and what it can do.`
- **Part C:**
  - **XI The Five Samples** — Topology (frame/locale, TQFT); Music (T/I group `D_24`, PLR, GIS = G-torsor, Tonnetz, Mazzola); Color (trichromacy = 3-dim vector space, metamerism = kernel, hue = SO(2)); Quantum superposition (free-vector-space functor; FdHilb dagger compact; ZX; no-cloning = no natural diagonal); Combinators (cartesian-closed `−×A ⊣ (−)^A`, Curry–Howard–Lambek, SKI/BCI).
  - **XII Wide — Recurring Structures** — groups; monoids/semigroups (Krohn–Rhodes); **semirings/rigs** (`(∨,∧)`, tropical `(min,+)`, probability `(+,×)`, `ℕ[X]` provenance, `ℂ` amplitudes; Green–Karvounarakis–Tannen PODS 2007, > `federated query lineage is semiring-annotated`); lattices (Knaster–Tarski); adjunctions; vector spaces; convolution/group algebras (geometric deep learning, Erlangen); operads; Hopf/bialgebras (Connes–Kreimer; Turi–Plotkin); **sheaves** (Abramsky–Brandenburger contextuality; Spivak `Σ_F ⊣ Δ_F ⊣ Π_F`, > `Federation is sheaf gluing.`); dualities (Stone/Gelfand/Pontryagin/Isbell/Zariski).
  - **XIII The Extended Rosetta Stone** — longtable structure × {topology, logic, computation, music, quantum, data/Atlas}. > `Read horizontally: one abstract structure wearing many domain-clothes. Read vertically: one domain is a model of the whole theory.`
- **Exodos: The GraphAtlas Program** — four directives: (1) bialgebra discipline for AGENT.md; (2) arrow/(enriched) Freyd structure for skills, DSL as free monad `μF ≅ F(μF)`; (3) federation as presheaf/sheaf with `ℕ[X]` provenance, migrate via `Σ_F ⊣ Δ_F ⊣ Π_F`; (4) extended Rosetta table as design invariant. > `Build below the boundary. Project, do not totalize.` > `una structura, vultus innumeri` / `one structure, countless faces`.
- PDF-only confirms: the typeset **Extended Rosetta Stone** longtable (p10); Appendix A "Primary Sources" is the physically final page (p11), terminating: `Atiyah, "TQFT," IHES 1988; Segal.`
- `.tex` FINAL LINE: `\end{document}`.

### 4.6 `skills/README.md` — "Skills as Composable Algebra" (1809 B, sha `6538d287…`)

A skill = morphism in a symmetric **premonoidal** category **Sk**; objects = typed
capabilities (precondition ⊢ postcondition); `∘` = sequencing, `⊗` = parallel resource use.
**Sk** is an (enriched) **Freyd category** (Atkey; Jacobs–Heunen–Hasuo). Generation (Forge):
initial algebra `μF ≅ F(μF)` (Lambek), free monad `F*`, GSOS ⇒ every skill library a
**bialgebra**. Laws (verbatim):
> `associativity of ∘; functoriality of lift; first coherence (sliding, exchange); ⊗ interchange up to the premonoidal centre. A skill that violates its laws is not a skill; it is a side effect wearing a name.`
FINAL LINE: > `- forge/       — generation of skills from atomic contracts`

### 4.7 The ten skills (`skills/**/*.md`) — full account (req. (c))

Each entry: signature · semantics · verbatim law · binding · verbatim final line.

**`core/compose.md`** (444 B, sha `446ffd18…`) — **Sig** `(>>>) : Sk a b → Sk b c → Sk a c`;
Kleisli `f >=> g = μ ∘ T g ∘ f`. **Law** > `Associativity; arr id unital. Postcondition of f
must equal precondition of g — type mismatch is refusal, not coercion.` Binding: pipeline =
composite morphism; provenance = ℕ[X] product of stage annotations. FINAL LINE:
`is the ℕ[X] product of stage annotations (see provenance/semiring.md).`

**`core/lift.md`** (412 B, sha `8f1799ff…`) — **Sig** `arr : (a → b) → Sk a b`; identity-on-
objects functor `J: C → K` of the Freyd category. **Law** > `arr id = id; arr (g ∘ f) = arr
f >>> arr g (functoriality).` Binding: pure graph transforms enter pipelines only through
`lift`, provenance-invisible. FINAL LINE:
`pipelines only through ``lift`` — provenance-invisible by construction.`

**`core/parallel.md`** (547 B, sha `8f8b99cb…`) — **Sig** `first : Sk a b → Sk (a ⊗ c) (b ⊗
c)`; derived `(***)`, `(&&&)`; premonoidal tensor, full interchange only in the centre.
**Law** > `first (arr f) = arr (f × id); sliding, association coherence.` Binding: federated
fan-out across cluster nodes `trixie/graph/silmaril`; non-central skills serialize. FINAL
LINE: `non-central skills serialize — the algebra records the causal order.`

**`effects/kleisli.md`** (677 B, sha `a9aa4b83…`) — **Sig** `Sk_T a b := a → T b`, T strong
monad; `>=>`. Fibers: state `S⇒(−×S)`, nondet `P`, probability `D`, failure `−+E`, control
`(−→R)→R`. Handler = homomorphism from free model (Eilenberg–Moore). **Law** > `Handlers are
total on the theory's operations; unhandled operation = type error, not runtime surprise.`
FINAL LINE: `speculative traversal (P) — one schema, semiring/monad swapped per fiber.`

**`federate/sheaf.md`** (746 B, sha `9577205c…`) — **Sig** site = schema category with
covers; matching family `{sᵢ ∈ F(Uᵢ)}` ↦ glued global section; failure = **obstruction**
(cohomology class; Abramsky–Brandenburger). **Law** > `Uniqueness: compatible locals glue to
at most one global (no central authority needed — the Hanseatic theorem).` Binding: peer
schema morphism induces `Σ_F ⊣ Δ_F ⊣ Π_F` (Spivak). FINAL LINE: `migration, pullback, join —
federation's entire query algebra is one adjoint triple.`

**`forge/generate.md`** (821 B, sha `cd7dade4…`) — **Sig** `forge : Signature F → (μF, F*,
λ) — language, library, law.` Atomic contracts generate initial algebra `μF ≅ F(μF)`
(Lambek), composites = free-monad `F*` terms, GSOS λ ⇒ library is a **bialgebra**;
bisimilarity of skills is a congruence. **Law** > `COOK_LEMMA_00/01 discharged formally:
every atom unique but documented (generators), e2e reproduction via Yoneda from the atomic
schema base (density: every skill is a colimit of representable atomic probes).` Binding:
Forge DSL triad `F_math/F_lang/F_econ` = three Lawvere-theory presentations of one
signature. FINAL LINE: `skills/**/*.md above are its first unfolding.`

**`games/equilibrium.md`** (668 B, sha `e2cdfb0b…`) — **Sig** `G : (A,A') → (B,B') =
(Strat_G, play_G: Strat_G → Optic, eq_G: context → P(Strat_G))`; open games
(Ghani–Hedges–Winschel–Zahn); composition of games = composition of optics under Para. **Law**
> `eq of a composite factors through eqs of parts (the whole game never needs recomputation
from scratch).` Binding: multi-agent GraphAtlas negotiation; Bayesian variant = Bayesian
lenses. FINAL LINE: `Bayesian variant = Bayesian lenses (research frontier, flagged).`

**`observe/coalgebra.md`** (637 B, sha `17441e97…`) — **Sig** `obs : X → B X`; skill =
coalgebra hom into the final B-coalgebra; equality = bisimilarity coinductively; modal
interface (Moss ∇). **Law** > `No skill may distinguish bisimilar states (observational
univalence).` Binding: monitoring/lineage-watch skills observe, never read hidden state.
FINAL LINE: `read hidden state, because the conformance rule (AGENT.md §1) deleted it.`

**`optics/lens.md`** (689 B, sha `6e5d8074…`) — **Sig** `Lens (s,t) (a,b) = (get: s→a, put:
s×b→t)`; general optic `∃m. (s → m⊗a) × (m⊗b → t)`; profunctor representation, ends over
Tambara modules; representation theorem = double-Yoneda (Boisseau–Gibbons). **Laws** >
`GetPut, PutGet, PutPut (lawful lens); optic composition = ordinary composition of the
profunctor representation (modularity for free).` Binding: schema↔instance focusing; every
GraphAtlas updater is an optic. FINAL LINE: `GraphAtlas updater is an optic so that reads and
writes stay coherent.`

**`provenance/semiring.md`** (734 B, sha `9817abf5…`) — **Sig** `annotate : Sk a b → Sk (a,
K) (b, K)` for commutative semiring K; join = `·`, union = `+`; Green–Karvounarakis–Tannen;
positive relational algebra factors through **ℕ[X]**. Fibers: Boolean (reachability),
tropical `min,+` (cheapest), Viterbi `max,×` (best explanation), ℕ[X] (full lineage). **Law**
> `Annotation is a semiring homomorphism; evaluate once in ℕ[X], specialize everywhere.`
Binding: every GraphAtlas answer carries its polynomial. FINAL LINE: `substitution, trust is
evaluation.`

---

## 5. CROSS-CORPUS REFERENCES (the tower's own weave)

- **Executable-head ↔ skills:** `AGENT.md` §6 and `foundations/README.md` name `skills/README.md` and `skills/**/*.md`; V-polysemy Part B is the theory of exactly those skill files; `observe/coalgebra.md` cites `AGENT.md §1` by name; `core/compose.md` cites `provenance/semiring.md` by name; `forge/generate.md` cites `COOK_LEMMA_00/01` and `skills/**/*.md`.
- **Paper ↔ paper:** I-fundamenta (Latin proofs) and II-en (English tragedy) prove the *same* Yoneda + Lambek theorems; IV-turtles iterates the Yoneda/boundary pair through eleven strata; V-polysemy turns Yoneda "sideways" (functorial semantics) and unifies AGENT.md + skills as one bialgebra. Scholium 9 of I-fundamenta = Act VI of II-en = Stratum III of V-polysemy = §0 of AGENT.md (the Turi–Plotkin (Σ,B,λ) bialgebra).
- **Skill theory ↔ tower federation:** `federate/sheaf.md`'s "Hanseatic theorem" and `Σ_F ⊣ Δ_F ⊣ Π_F` are the engineering face of II-en's density-scholium ("no central node") and IV-turtles §14.3 ("Palantir's architecture is refuted by a type theory"). This closes the loop back to the framing doctrine `docs/praeriehund-demokratie-der-kategorien.md` (the "Hansestadt-Modell", federation as the Lewis-&-Clark alternative to the Palantir endpoint).
- **URL-cycle cross-references (physical):** `groenewt/core` mounted at `forge/core` and `forge/agents/core` (both @3f90564c); `groenewt/base_bin` mounted at `forge/bin` and `forge/agents/sbin` (both @6525c556). See §2.6.
- **Taxonomy skew cross-reference:** the same `base_agents` / `base_templates` taxonomies exist at two pins each — `672ba868`/`2d84826c` inside this tower vs `d2b1217f`/`eb3d916b` as silmaril siblings (§2.5); the sibling pins are the targets of `ledger/W1/base_agents.md` and W1 Task 1 respectively.
- **License-vs-doctrine cross-reference:** the corpus prose commits to Apache 2.0 (IV-turtles §14.5; Präriehund doctrine); the tower's LICENSE files are GPLv2 (base/bin/docs/specs), BSD 3-Clause (templates), Apache 2.0 (agents only) — recorded in §2.8, not reconciled.

---

## 6. HONEST-GAP REGISTER (every PROVISIONAL, carried verbatim)

Collected from both fragments plus the one synthesizer-level gap the brief flags. These are
genuinely unresolvable from the in-scope evidence; none is force-fit.

1. **"AOB"/"AOBs" expansion** (from `forge/specs` README `# base_aobs` / `Base AOBs`, url
   `groenewt/base_aobs`). frag-001 File 7, verbatim: *"The expansion/meaning of 'AOB'/'AOBs'
   is genuinely unresolvable from this file. The brief labels `forge/specs` as `base_aobs`
   and calls the directory `specs`, but neither the file nor the brief expands the acronym.
   Per praeriehund honesty I do NOT force-fit an expansion. GAP: 'AOB' expansion unknown from
   in-slice evidence."* (Note: `ledger/W1/base_agents.md` treats `base_aobs`'s corpus as
   "AOB atoms" but does not spell the acronym either; the expansion remains unresolved here.)

2. **"GA" expansion** (from `Base GA Repo`, `Base GA External`, `Base GA Doc repo`, `Base GA
   Templates`, `Base GA Bin`, `Base GA Agents Implementation`). frag-001 File 4, verbatim:
   *"expansion of 'GA' is not resolvable from this file alone; the inference to 'GraphAtlas'
   is documented above but not carried by the source."* **[inference]** the surrounding
   corpus is titled "GraphAtlas" throughout, so "GA" plausibly = "GraphAtlas" — marked as
   inference, not asserted by any of the README files themselves. frag-001 File 10 repeats
   the gap for `base_templates`.

3. **The `sbin` path-record defect** (§2.4). Genuinely PROVISIONAL: the `sbin` gitlink at
   `forge/base/forge/agents` has **no `.gitmodules` mapping**, so **no URL exists in the
   source for the `sbin` path itself**. The *content* at that pin (`6525c556`) is capturable
   via `forge/base/forge/bin` at the identical SHA (same repo `groenewt/base_bin`), and the
   commit message documents the `forge/sbin -> forge/bin` intent — but the path record's own
   declared origin is unrecoverable from the tree. Recorded as found, not editorialized.

No other PROVISIONAL gaps were raised by either fragment. Every other file entry in both
fragments explicitly records "PROVISIONAL gaps: none."

**Non-gap discrepancy also recorded (not a source gap, a brief-vs-live fact — see §1, §2.4,
§7):** the dispatch brief asserted `forge/base` is pinned @ `9e60c103…`; the live pin is
`c4e828188a57d7a93c4f4972859dd0862ae6cce6` and object `9e60c103…` does not exist in the
repo. This is resolvable (and resolved: the found value governs), so it is a recorded
discrepancy rather than a PROVISIONAL gap.

---

## 7. COVERAGE STATEMENT

- Manifest: `ledger/W1/manifests/base_tower.manifest` — the union of the two fragment
  manifests (40 + 10 = 50 lines), sorted by path, tab-separated `sha256<TAB>bytes<TAB>path`,
  one line per inventory file. No duplicate paths.
- All 50 digests independently recomputed by the synthesizer over the live tree and matched
  the fragment-manifest union exactly (fragment manifests are byte-accurate).
- Live tree verified identical to `t2-inventory.txt` (`diff` of `find forge/base -type f
  -not -path "*/.git/*" | sort` against the inventory: empty).
- Acceptance check, verbatim:

```
COVERAGE EXACT: forge/base == ledger/W1/manifests/base_tower.manifest (50 files)
```

- Git facts verified read-only before assertion: `forge/base` HEAD/pin `c4e82818` (NOT the
  brief's `9e60c103`, which does not exist); the seven L2 pins and the three L3 agents pins
  (`core@3f90564c`, `docs@661af74e`, `sbin@6525c556`) all match the brief; the `sbin`/`bin`
  crossed record and empty `sbin` mount confirmed; the `d2b1217f`/`eb3d916b` sibling skew
  confirmed live.

*Nihil occultum, tantum textum.*
