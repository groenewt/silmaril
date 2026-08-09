# W2 · Sub-project 8 — basicttl depth remediation (design)

> **Batch design doc** (superpowers:brainstorming; batched SP2–SP9 for one maintainer review pass,
> Directive 14). Design-only: NO `.ttl`/`.sparql`/implementation authored here; terminal step on batch
> approval → superpowers:writing-plans. **THIS ITERATION's v1** — corpus-agnostic (Directive 13),
> relaunch-safe; it will be fundamentally challenged and relaunched later. basicttl remediation is in
> W2 (not W5) because it is cleanup of *already-present* corpus, not new-corpus binding (Directive 7).
> **This re-author LIFTS the authored Helios structures (Directive 1: lift, do not invent); it does
> not re-pick the six cross-cutting decisions.**
>
> **Grounding (gospel):** `docs/unary-byte-frame-law.md`, `docs/praeriehund-demokratie-der-kategorien.md`,
> `ledger/W2/design_constraints.md` Directives 1–14, `STRICTNESS_RULES.md` (esp. Rules 3, 4, 5, 7, 14),
> the DAG rulings `ruling_depth_gate` + `ruling_fable_dissolve` (both bind `wf_w2`), and — as the
> grounding substrate — the **committed, green SP1 Primitive Floor** at `basicttl/primitives/`.
>
> **The two authored structures this sub-project LIFTS (with `helios/` paths):**
> 1. The **`\SilTaggedMath{expr}{URN}{label}{description}` 4-arg described-occurrence receipt** —
>    `helios/srcy/shared/components/accessibility/semantic_footer.tex` (macro L135–142; the
>    occurrence-registration + publication-gate machinery L100–133). This is the **authored ancestor
>    of the ≥200-char `rdfs:comment` depth discipline** (srcy_map §1): every symbol/identifier
>    occurrence is a content-addressed atom carrying a stable id, a label, and a ≥1-sentence
>    description, and the **publication gate independently requires a nonblank label AND a nonblank
>    description in the readback, permits byte-identical repeats, and rejects any conflict for the same
>    kind/key** (L100–106). Depth is not "a long comment" — it is a 4-slot occurrence receipt with a
>    biting publish gate.
> 2. The **`wave_f_music` / `wave_f_orientation` grounding tables** (type_urn/family → a specific CCO
>    class) — `helios/01_data_src_specs/wave_f_music_grounding.spec.yaml` (9-row `family_grounding_table`
>    L55–64) and `…/wave_f_orientation_grounding.spec.yaml` (6-row table L60–66). e.g. `concrete_anchor`
>    → Designative Information Content Entity `cco:ont00000686`; `cheese_trap_immunity` → Prescriptive
>    ICE `cco:ont00000965`; `circuit_imprint_tensor` → Act of Measuring `cco:ont00000345`;
>    `decomposition_step`/`yoneda_hom_leg` → Act of Data Transformation `cco:ont00001158`;
>    `synonym`/`antonym`/`description` → Act of Communication `cco:ont00000402`.

---

## 1. Goal

Absolutely remediate the existing `basicttl/` corpus so it satisfies its own depth law with real teeth,
and so **every basicttl concept dual-grounds into the SP1 Primitive Floor** (subatomic dual-grounding,
Directives 3/8). Two authored structures drive it:

- **Depth = the described-occurrence receipt (lift #1).** Every remediated concept becomes a 4-slot
  receipt — `{expr/symbol, URN-key, label, ≥200-char description}` — modelled on `\SilTaggedMath`, not
  a bare comment-length rule. The depth gate becomes the **publication gate**: a concept whose label OR
  description readback is blank/short is REJECTED, and two occurrences of the same URN-key with
  conflicting label/description are REJECTED (byte-identical repeats permitted).
- **Grounding = the functor G that DEEPENS the flat CCO tables (lift #2 + the correction pattern).**
  The `wave_f` tables ground each family at exactly **one flat CCO IRI**. **The correction: every flat
  single-CCO-IRI anchor becomes an SP1 dual-grounded tower object** via a grounding functor `G` into
  the floor. The CCO IRI is *retained* (load-bearing universal-anchor, CCO/BFO decision) as the
  concept's formal upper-anchor; `G` *adds* the concept's value-carrier grounding into its SP1 formal
  tower + physical carrier + ρ. Flat anchor → dual-grounded taiji object.

Concretely, close the four debts the depth gate currently only *warns* about (it runs `|| true` in CI —
SUBAGENT_FINDINGS §5.4):

1. **Author the stub `owl:Class`es** as described-occurrence receipts (subtyping rationale + physical
   realization + typed effect in the ≥200-char description slot), not filler.
2. **Type the bare individuals** — every `owl:NamedIndividual` carrying *only* `owl:NamedIndividual`
   gets a specific domain class (depth-check rules 2/4).
3. **Define the undefined content-predicates** — each with `rdfs:domain`, `rdfs:range`, and a
   ≥200-char description receipt.
4. **Dual-ground every concept into SP1 via G** — each remediated class carries a `silm:groundsIn`
   edge into a floor `prim:` primitive AND retains its `wave_f`-table CCO upper-anchor, so the basicttl
   graph inherits the twin-olog colimit taiji rather than bottoming out at a bare `xsd:` leaf, a bare
   `owl:NamedIndividual`, or a flat CCO IRI.

Mark `silm:isProvisional` **only** where meaning is genuinely undecidable from context (Präriehund —
name the gap, document it; never a dodge; target as close to the floor's **0** as the corpus honestly
allows). Additionally **dissolve-and-absorb the folklore fable** (`ruling_fable_dissolve`) so it is a
*projection* of the typed trust graph, never standalone narrative.

### 1a. Build Task-0 — the census reality (Präriehund honesty: a gap to reconcile, not a dodge)

The DAG label for `phase_w2_sp8` cites **~156 stub classes, ~59,777 untyped individuals, 6 predicates**.
A fresh in-session `rdflib` census over the **81 of 83** top-level files that parse found a materially
different picture — this divergence is surfaced as the first build task, not silently adopted:

| target | DAG-cited | in-session recount (81/83 files) |
|--------|-----------|----------------------------------|
| `owl:Class` total | — | 65 |
| stub classes (`rdfs:comment` absent or <200) | ~156 | 21 |
| `owl:NamedIndividual` (bare, only-NamedIndividual) | ~59,777 | 23,096 (of 23,218 total) |
| undefined content-predicates | 6 | **6 confirmed** (+3 structural) |

The **6 content-predicates are confirmed exactly**: `silm:hasSynonym`, `silm:hasAntonym`,
`silm:hasAbbreviation`, `silm:hasExample`, `silm:hasLongDescription`, `silm:hasAdditionalAttribute` —
used across the 21 numbered narrative files + the folklore fable, declared nowhere. Three further
structural predicates are also undefined: `silm:groundsIn`, `silm:sourceNode`, `silm:targetNode`. The
class/individual divergence is because **two files fail to parse** — `basicttl/ui_constructor.ttl`
(line 146) and `basicttl/computational_agent.ttl` (line 95), both *"Prefix xsd: not bound"* — so their
classes/individuals are invisible to any rdflib census, and the DAG-cited figures evidently derive from
a broader W1 census (full corpus/consolidated/`_verb/`). **Build Task-0 is a fresh authoritative census
that reconciles the two and drives the fanout**; the numbers above are the design's honest current
evidence, and the parse failures are themselves an in-scope blocker (§3, §6). This divergence is Open
Question 1.

---

## 2. Architecture — remediation as the grounding functor G, carried by the described-occurrence receipt

The remediation is **not** hand-decoration file-by-file. It is a single categorical operation — the
grounding functor `G` — whose object map is `silm:groundsIn` and whose every asserted law has a biting
tooth. The *vehicle* of each grounded concept is the `\SilTaggedMath`-style 4-slot receipt.

```
   basicttl legacy graph  ──G (grounding functor)──▶  SP1 Primitive Floor (prim:)
        │  65+ classes, 23k+ individuals,                │  59 FormalType towers · Bit→Container
        │  6 content arrows, 21 chapter-glossaries        │  carrier ladder · ρ (Kleisli/Frame) ·
        │  each a described-occurrence receipt            │  literal Yoneda · colimit taiji
        └──── each concept: groundsIn (SP1 tower) + retains wave_f CCO upper-anchor ────┘
                 dual-grounding = the flat CCO IRI DEEPENED into a taiji object
```

### 2.1 Lift #1 — the described-occurrence receipt is the unit of depth

`\SilTaggedMath{#1 expr}{#2 URN}{#3 label}{#4 description}` (semantic_footer.tex L135–138) registers a
content-addressed semantic occurrence (`\silRegisterSemanticOccurrence`, L113–133) that the
**publication gate reads back and rejects unless the label and description are both nonblank**, while
permitting byte-identical repeats and rejecting same-key conflicts (L100–110 comment). SP8 lifts this
one-to-one onto RDF:

| SilTaggedMath slot | basicttl receipt slot | tooth |
|---|---|---|
| `#1` expr / symbol | the concept's `rdfs:label`-bearing symbol / atom `bare_symbol` | present |
| `#2` URN occurrence-id | the concept URN (`urn:silmaril:entity#…`, full-lexical, Rule 3) | resolvable, unique kind/key |
| `#3` label | `rdfs:label` (full-enough identity) | nonblank |
| `#4` description | `rdfs:comment` ≥200 chars (what it asserts + the CPO/CCO process that licenses it) | ≥200, nonblank |

So the depth gate is not "comment length ≥ 200" bolted on — it is the **authored publication gate**:
`NoStubClassShape`/`NoBareIndividualShape` enforce the nonblank label+description readback, and a new
`OccurrenceConsistencyShape` enforces the same-kind/key no-conflict rule (two receipts for one URN must
be byte-identical). This is a richer, authored tooth than a length check.

### 2.2 Lift #2 + the correction — G deepens the flat `wave_f` CCO tables into dual-grounded tower objects

The `wave_f` tables are the authored **flat** grounding: one family → one CCO IRI. They are the
`pre-dual-grounding state` (data_specs_contracts_map §6: *"here every atom bottoms out at a flat CCO
IRI … no tower"*). **G is exactly the correction SP1 mandates.** For each family/type_urn row, G assigns:

- **the formal upper-anchor (retained, load-bearing):** the row's CCO IRI — Designative ICE
  `cco:ont00000686`, Prescriptive ICE `cco:ont00000965`, Act of Measuring `cco:ont00000345`, Act of
  Data Transformation `cco:ont00001158`, Act of Communication `cco:ont00000402`, Act of Information
  Processing `cco:ont00000366` — resolved against `MergedAllCoreOntology.ttl` (CCO 2.x under BFO) via
  `SIL_CCO_TTL_FILE` (universal_anchors law; the six cross-cutting CCO/BFO decision is *used, not
  re-picked*). Node families ground via `cco:ont…`; the one arrow family (`yoneda_hom_leg`, `top_kind:
  arrow` in the orientation table) grounds its process via `cceo:…`.
- **the floor-tower grounding (added by G — the deepening):** a `silm:groundsIn` edge from the
  concept's **value carrier** into its SP1 formal tower, dual-grounded to a physical carrier via ρ. A
  `hasLongDescription` value is a `prim:String` realized via `prim:Utf8` (`frameEffect
  prim:EncodingLoss`) byte-descending to `prim:Bit`; a URN identifier grounds into the `prim:URN`
  tower; a `color_atom` channel grounds into `prim:RGB` (three `prim:Octet`, ordinal 0..255); a
  `citation`/`enum_membership` ordinal grounds into `prim:Ordinal`. Because SP1 closed ρ as a **functor
  on subtyping arrows** with `prim:AncestralGroundingPath` + literal Yoneda, a concept grounded at a
  subtype is dual-grounded *two ways* — directly and transported up its tower — both resolvable edges,
  not prose.

The result: `G(concrete_anchor)` is no longer the bare IRI `cco:ont00000686` — it is a taiji object
whose formal facet is Designative ICE / its SP1 Identifier-tower type and whose physical facet is the
byte carrier, glued by ρ. The flat table is **deepened, not discarded**.

**Which SP1 structures G consumes (named precisely):** the **59 dual-grounded `prim:FormalType`
towers** (`formal.ttl`) as grounding targets (Number ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ+Imaginary; Text
Codepoint/Grapheme/String; Identifier URN⊃URI⊃IRI/QName/BlankNode; RDF-term
Literal/Triple/Quad/RDFGraph; Enum Enumeration/Ordinal/Categorical; Boolean/Kleene3; Binary
Blob/Hash; …); the **physical carrier ladder + ISA/UEFI encodings + RGB** (`physical.ttl`,
`prim:byteDescendsTo`); the **monadic realization = Frame** (`realization.ttl`:
`realizesFrom`/`encoding`/`frameOutput`/`frameEffect`; ρ-as-functor `prim:RealizationTransport` +
`prim:AncestralGroundingPath`); the **colimit taiji atom** (`taiji.ttl`:
`formalFacet`/`physicalFacet`/`gluedBy`, `prim:Frame prim:isYonedaPoint true`); and the **SHACL
`prim:DualGroundingShape`** self/ancestor/descendant `rdfs:subClassOf*` walk, reused as SP8's
`ConceptGroundedShape` template.

### 2.3 The AOB atom envelope is the receipt's home (consumes SP2)

The 18 `*_atom.ttl` files already declare atom-classes (`silm:synonymatom`, `silm:coloratom`, …) — these
ARE AOBs. SP8 re-expresses each through **SP2's AOB meta-ontology** (the appendix-E envelope
`entity.{urn,kind_urn,layer,ancestry,citations,grounding}` + `triad_render`, lifted at
`helios/srcy/appendices/39_E_research_source_mirror/specs/atoms/`), where the `grounding` field is
exactly the receipt's description slot and `entity.urn` its URN-key. The six content-predicates are
defined as **AOB atom-column arrows** whose literal ranges ground into SP1's Text tower.

### 2.4 Polysemy is literal (consumes SP6); files are subatomic per format (consumes SP5)

The 21 numbered chapter files (`00_whitepaper`…`25_sheaf_gluing`) are **21 distinct epistemologies** —
each a glossary in SP6's "mole of glossaries". The same term recurs across chapters with intentionally
colliding meaning (one term held as `hasSynonym` in one glossary, `hasAntonym` in another). SP8 does not
flatten collisions; it types each occurrence against its chapter's glossary (SP6) so the collision is
preserved and OSSIE-mime-arbitrable (Directives 1/6, Rule 6). Each `basicttl/*.ttl` file is itself a
`File` individual in SP5's file+format taxonomy (format = Turtle; components = the classes/individuals
it declares), so the Complete Component Account has one navigable entry per file.

### 2.5 Fable dissolve-and-absorb (`ruling_fable_dissolve`)

`folklore_provenance_fable.ttl` narrates the trust model (`commit_signing_trust.ttl`). Each
`silm:fablefigure`'s `silm:hasExample` string must resolve to a **real triple** in the trust graph — the
fable asserts nothing the graph cannot back. SP8 dissolves the fable into typed edges to the trust
individuals (absorb), and `FableBackedShape` enforces that every `hasExample` claim has graph evidence.
The folklore becomes the memorable *projection* of the typed provenance graph ("the ontology is the
thing").

---

## 3. File layout — one authored concern-set + a per-file fanout (Rules 7, 14; `urn:` namespace)

SP8 edits the **existing** `basicttl/*.ttl` in place (basicttl IS the source — Rule 4) AND adds one
small remediation concern-set. Namespace idiom stays `urn:silmaril:…` (`silm:` for entity concepts,
`prim:` referenced for grounding targets; no internal abbreviations — Rule 3).

| file | responsibility |
|------|----------------|
| `basicttl/remediation/content_predicates.ttl` | the 6 content-predicates + `silm:groundsIn`/`sourceNode`/`targetNode` **defined** — domain/range + a ≥200-char **description-slot receipt** each; declared as SP2 AOB atom-column arrows whose literal range grounds into the SP1 Text tower |
| `basicttl/remediation/grounding.ttl` | the object map of **G**: `silm:groundsIn` edges from each basicttl domain class into its SP1 `prim:` tower **plus** the retained `wave_f`-table CCO upper-anchor per family (the flat table deepened), consuming `prim:DualGroundingShape`'s pattern |
| `basicttl/remediation/fable_dissolve.ttl` | the fable→trust-graph absorption edges (each `hasExample` bound to real `commit_signing_trust.ttl` triples) |
| `basicttl/remediation/remediation.shapes.ttl` | SHACL law: `NoStubClassShape`, `NoBareIndividualShape`, `OccurrenceConsistencyShape`, `ContentPredicateDefinedShape`, `ConceptGroundedShape`, `FableBackedShape`, `ParseCleanShape` (§4) |
| `basicttl/remediation/remediation.queries.sparql` | the EXPECT-TRUE ASK suite (§4), each with an inline DATA-CONTRACT comment |
| `basicttl/remediation/checks/run-remediation-checks.sh` | the runner: parse-all + pyshacl + depth gate + every EXPECT-TRUE ASK + the probe battery |
| `basicttl/remediation/README.md` | the remediation, its consumers, how to re-run, the true census |

That is a **7-entry honest concern-set** (same shape as SP1's floor). The **large fanout is the in-place
edit of the 83 `basicttl/*.ttl` files** — the per-file/per-class "distinct concern per file" work
(Rule 14) and the "appropriate fan-out, never one hammer" mandate (Rule 7). Staged fanout at build time:

- **Stage 0 — census + parse-fix (Task-0).** Reconcile DAG-cited vs. recount figures (§1a, Open Q1);
  fix the two `xsd:`-prefix parse failures so the whole corpus is machine-visible (Open Q2 boundary with
  W4). Freeze the authoritative worklists (stub-class list, bare-individual-per-file counts, predicate
  list) as the Complete Component Account seed.
- **Stage 1 — predicates.** Author `content_predicates.ttl` (unblocks everything citing the 6 arrows).
- **Stage 2 — stub classes.** One worker per file with stub classes; each authors the ≥200-char
  dual-grounded description receipt. Fanned by file.
- **Stage 3 — individual typing.** The biggest fanout: one worker per file, typing that file's bare
  individuals against specific domain classes (numbered chapters dominate — `11_base_commutative_diagram`
  ≈ 3,908; `19_mereology` ≈ 3,223; `02_music` ≈ 2,821). Micro-batch within a file if needed.
- **Stage 4 — grounding + fable dissolve.** Author `grounding.ttl` (the G object map, seeded by the
  `wave_f` tables and deepened) and `fable_dissolve.ttl`.
- **Stage 5 — verify.** Runner + probe battery + adversarial triple panel.

---

## 4. Verification plan — evidence-first, every tooth proven by probe injection

Same discipline as the floor (`verification-before-completion`): each check is RED before the
remediation, GREEN after, and **each SHACL shape / EXPECT-TRUE ASK is proven to bite by injecting a
violating probe** (`conforms=True → False`, or ASK `True → False`). Stack: rdflib 7.6.0 + pyshacl 0.40.1
(`inference="rdfs"`); wired into the multi-engine CI in W4 (where the depth gate stops being `|| true`).

**SHACL shapes (`remediation.shapes.ttl`) — defang-proof `sh:sparql`, per SP1 §6 idiom:**

- `NoStubClassShape` — every `owl:Class` carries the receipt's description slot ≥200 chars.
  *Probe:* `silm:ex_stub a owl:Class ; rdfs:comment "short"` → `conforms=False`.
- `NoBareIndividualShape` — every `owl:NamedIndividual` has ≥1 `rdf:type` other than
  `owl:NamedIndividual`/`owl:Thing`. *Probe:* `silm:ex_bare a owl:NamedIndividual` → `conforms=False`.
- `OccurrenceConsistencyShape` (**lift #1 publish-gate tooth**) — a URN-key's label+description are
  nonblank, and no two receipts for one key carry conflicting label/description (byte-identical repeats
  OK). *Probe:* two `rdfs:comment`s differing on one subject, or a subject with `rdfs:comment` but blank
  `rdfs:label` → `conforms=False`.
- `ContentPredicateDefinedShape` — each of the 6 content-predicates has `rdfs:domain`, `rdfs:range`, and
  a ≥200-char comment. *Probe:* delete `hasSynonym`'s range → `conforms=False`.
- `ConceptGroundedShape` (**lift #2 / functor-G tooth**) — reuses SP1's `prim:DualGroundingShape` walk:
  every basicttl domain class has a `silm:groundsIn` whose target `rdfs:subClassOf* prim:FormalType` (or
  is a `prim:Primitive`) **and** carries its `wave_f` CCO upper-anchor (`cco:ont[0-9]{8}` for node
  families, `cceo:` for the arrow family — pattern via the universal-anchor, never inlined). *Probe:*
  `silm:ex_concept a owl:Class` with a valid comment but no `groundsIn` → `conforms=False`.
- `FableBackedShape` — every `silm:fablefigure`'s `silm:hasExample` resolves to a real trust-graph
  individual/edge. *Probe:* a figure whose example names a non-existent identity → `conforms=False`.
- `ParseCleanShape` / runner gate — the whole `basicttl/` tree parses (0 failures). *Probe:* the two
  current `xsd:`-prefix failures are the standing RED; GREEN when both parse.

**EXPECT-TRUE ASKs (`remediation.queries.sparql`), none vacuous (each FAILs on an empty graph and flips
under a targeted violating injection), each with an inline DATA-CONTRACT comment:**

- `q_no_stub_class` — no `owl:Class` with a <200-char/absent description survives.
- `q_no_bare_individual` — no individual typed *only* `owl:NamedIndividual`.
- `q_occurrence_consistent` — no URN-key carries a conflicting label/description receipt (publish-gate).
- `q_content_predicates_defined` — all 6 arrows carry domain+range+comment.
- `q_every_concept_grounded` — every domain class has a `groundsIn` resolving into the SP1 tower AND its
  CCO upper-anchor (the class-level dual-grounding litmus, mirroring SP1 `q_universality`).
- `q_grounding_byte_descends` — a grounded String/URN/colour concept's realization byte-descends to
  `prim:Bit` (reuses SP1 `q_byte_descent` over the grounded targets).
- `q_fable_backed` — every fable `hasExample` claim has a matching trust-graph triple.
- `q_polysemy_preserved` — at least one term is held as `hasSynonym` in one chapter-glossary and
  `hasAntonym` in another (collisions preserved, not flattened — consumes SP6).
- `q_parse_clean` + `q_provisional_documented` — corpus parses; every `silm:isProvisional` carries a
  documented-gap comment.

**Depth gate:** `python3 scripts/ontology-depth-check.py basicttl/` exits 0 over the remediated tree
(classes ≥200, no bare individuals, object-properties have domain+range).

**Federation gate (consumes SP7).** SP8's local runner is the *inner* gate; the *outer* acceptance is
that **SP7's federation depth-SHACL + semantic-ancestry + coverage law conforms over the whole tree**
(§5). SP8 is done when SP7's `FederationDepthShape` + `SemanticAncestryShape` (which SP7 owns and stages
to bite whole-tree post-SP8) go GREEN on the remediated basicttl graph.

**Adversarial triple panel** (completeness / honesty / doctrine) after build, per the DAG Gate
discipline and Directive 14 — must return CLEAN before the `phase_w2_sp8` status flip.

---

## 5. Interfaces — Consumes / Produces

**Consumes (named precisely):**

- **From Helios (authored source-of-truth — the structures LIFTED):**
  `helios/srcy/shared/components/accessibility/semantic_footer.tex` — the `\SilTaggedMath` 4-arg
  described-occurrence receipt + its publication gate (lift #1, the depth-discipline ancestor);
  `helios/01_data_src_specs/wave_f_music_grounding.spec.yaml` +
  `…/wave_f_orientation_grounding.spec.yaml` — the flat type_urn/family→CCO grounding tables (lift #2,
  the seed G deepens); `helios/01_data_src_specs/universal_anchors.spec.yaml` — the CCO/BFO
  upper-anchor law (`cco:ont[0-9]{8}` / `cceo:` patterns, `MergedAllCoreOntology.ttl`, CCO 2.x);
  `helios/srcy/appendices/39_E_research_source_mirror/specs/atoms/` — the AOB envelope
  `entity.{urn,kind_urn,layer,ancestry,citations,grounding}` + `triad_render`.
- **From SP1 (committed floor `basicttl/primitives/`):** the 59 `prim:FormalType` towers; the
  `prim:Bit`→`prim:Container` carrier ladder + ISA/UEFI encodings + `prim:RGB`; the ρ Kleisli/Frame
  realization monad (`realizesFrom`/`encoding`/`frameOutput`/`frameEffect`) and ρ-as-functor
  (`prim:RealizationTransport`/`prim:AncestralGroundingPath`); the `prim:Primitive` colimit taiji
  (`formalFacet`/`physicalFacet`/`gluedBy`) + literal Yoneda; the `prim:DualGroundingShape` pattern and
  the teeth discipline (defang-proof `sh:sparql`, EXPECT-TRUE ASK mirror, probe RED→GREEN, non-vacuous).
- **From SP2 (AOB meta-ontology):** the colimit-taiji atom pattern; the 18 `*_atom.ttl` re-express as
  SP2 AOBs and the 6 content-predicates are defined as AOB atom-column arrows.
- **From SP5 (file+format taxonomy):** each `basicttl/*.ttl` typed as a `File` (format = Turtle);
  per-file components enumerated for the Complete Component Account.
- **From SP6 (glossary polysemy):** the 21 numbered chapters as distinct glossaries; synonym/antonym
  collisions typed and preserved (OSSIE-mime-arbitrable).
- **From SP7 (W2 SHACL coverage law) — SP8's acceptance target:** SP7 **owns** the federation
  depth-SHACL + semantic-ancestry + coverage law; **SP8 consumes it as the absolute remediation target**
  and is remediation-*local*. SP8 fixes the basicttl files until SP7's federation law conforms. (SP7 is
  the earlier sub-project; the prior draft's backward "produces-for-SP7" edge is DROPPED.)

**Produces (for higher sub-projects / W-phases):**

- The **fully-typed, fully-grounded, depth-clean, parse-clean basicttl graph**: 0 stub classes, 0 bare
  individuals, 6 (+3) predicates defined, every concept dual-grounded into the SP1 floor via G (SP1
  tower + retained CCO upper-anchor), fable dissolved, provisionals documented — the thing SP7's
  federation law conforms over.
- **For SP9 (Split↔Consolidated render seal):** the remediated graph is the reversibility input — every
  typed individual is a navigable split-file entry with an inverse; the per-concept colimit round-trip
  (inherited from SP1) is the per-primitive split↔consolidated reversibility unit.
- **For W4 (CI/CD engine):** `remediation/checks/run-remediation-checks.sh` + the depth gate become part
  of the `phase_w4_3`/`phase_w4_8` blocking gate (where the depth gate stops being `|| true`).
- **For W5 (corpus consolidation):** a clean, relaunch-safe basicttl baseline the re-runnable corpus
  binding builds on (Directive 7).

---

## 6. Non-goals (this iteration; YAGNI deferrals) & open questions

**Non-goals.**
- **No new-corpus binding** — zero gippidy/sparky/BLS/agent binding, no sha256-literal live data; that
  is the re-runnable W5 (Directives 7/13). SP8 cleans *already-present* corpus only.
- **No re-architecting basicttl's domain content** — SP8 types, comments, defines, and grounds what
  exists; it does not invent new domain concepts or restructure the chapters.
- **No bespoke class per individual at scale** — ~tens of thousands of individuals are typed against
  *existing* domain classes (provisional only where undecidable), not one new class each.
- **SP8 does not author the federation depth-SHACL** — that is SP7's; SP8 consumes it (§5).
- **`_verb/` legacy** stays advisory per the prior user ruling (SUBAGENT_FINDINGS §5.5); SP8's blocking
  scope is the current top-level `basicttl/*.ttl`, boundary stated explicitly.
- **CI wiring / making the depth gate blocking** is W4 (`phase_w4_3`); SP8 supplies the runner and proves
  green locally. **The render pipeline itself** is W3/SP9; SP8 only guarantees reversibility-readiness.
- Expected to be **challenged and relaunched** (Directive 13) — built to re-run, not to be final.

**Open questions for the maintainer (Präriehund — flagged, not invented):**

1. **Authoritative census.** DAG-cited ~156 stubs / ~59,777 individuals vs. in-session recount 21 stubs
   / 23,096 individuals over the 81 parseable files (§1a). Which census is canonical, and is build Task-0
   a recount-and-reconcile against the W1 full-corpus/consolidated figure?
2. **Parse-failure boundary.** `ui_constructor.ttl` + `computational_agent.ttl` fail to parse (missing
   `xsd:` prefix). Is fixing the prefix binding in SP8 scope, or does it belong to W4 `phase_w4_8`
   (which already names `ui_constructor.ttl`)?
3. **Edit-in-place vs. overlay.** SP8 assumes in-place edits to `basicttl/*.ttl` (basicttl IS the
   source, Rule 4). Confirm over a separate non-destructive remediation overlay (which would change how
   SP9's render seal sees the tree).
4. **Grounding granularity.** Is a `groundsIn` edge per *class* sufficient (values inherit grounding
   through the content-predicate ranges), or must every individual carry its own grounding edge? The
   design assumes per-class + per-content-predicate-range; per-individual grounding would multiply the
   fanout by ~59k.
5. **PROVISIONAL — `wave_f`-table coverage vs. basicttl families.** The lifted `wave_f` tables ground the
   **9 music + 6 orientation** paper atom-families; basicttl's 18 `*_atom.ttl` families and the 21
   chapter glossaries are a *superset*. For families with no `wave_f` row, G must assign a CCO
   upper-anchor from `universal_anchors`/the `_cco_class_label_map.tsv` — genuinely undecidable which
   CCO class per un-tabled family without the maintainer's authority; flagged PROVISIONAL, to bind in the
   plan (never force-fit a CCO IRI).
