# W2 · SP6 — Glossary polysemy: the mole of glossaries (design)

> **Batched design doc** (superpowers:brainstorming; design-only — no `.ttl`/`.sparql` authored here).
> Directive 14 cadence: SP2–SP9 designed up front, one maintainer review; each a real design (lifted
> Helios structures, file map, verification plan, Consumes/Produces, non-goals). **THIS ITERATION's v1**
> — corpus-agnostic (Directive 13), built to be re-run and relaunched, never permanent. Zero live-corpus
> binding (that is the re-runnable W5, phase `w5_5` "Collision resolution — OSSIE mime = polysemy arbiter").
> **LIFT, do not invent (Directive 1).** Every structure below is traced to an authored Helios file.

**Goal.** Author the meta-TBox for the **mole of glossaries** (STRICTNESS Rule 6; Directive 1): a layer
where **each glossary is a distinct epistemology**, and one lexeme is held as **SYNONYM in one glossary
AND ANTONYM in another, simultaneously and without contradiction** — because synonymy/antonymy are
**glossary-scoped sense relations, not global facts**. Collisions are **intentional and literal**; the
**OSSIE mime is the arbiter** that confirms a registered collision versus flags an unreconciled gap. The
layer grounds term identity in the SP1 Text/Identifier towers, makes each glossary entry an SP2 AOB atom,
and supplies the **teeth** (reified sense arrows + SHACL + EXPECT-TRUE ASKs) that make a synonym/antonym
pair inspectable and checkable.

**Authored Helios sources lifted (gospel):**
- `helios/srcy/shared/term_authority.yaml` — **the glossary = a citation authority**; the SAME lexeme
  carries a distinct `authority_type` (epistemology) per authority: `Mittens = local_colimit_anchor`
  vs `Felis catus = local_taxonomy_label` ("only when paired with TSN 183798 … **not as Mittens
  identity**") vs `catus collision = local_negative_regression_label`; `Node or Arrow` / `Node-or-Arrow`
  same `citation_key` (alias); `source_status ∈ {local, third_party}`.
- `helios/srcy/base/00_whitepaper/sections/00_helios_foundation/06_frame_sort_separation.tex` — **the
  progenitor law of polysemy**: the word "frame" = **6 disjoint sorts** (`F_cap`, `F_auth`, `F_lin`,
  `P_I`, `Frame(O,E)=O×E`, `T_vid`); *"No map, metric, or equivalence between these sorts is implicit …
  they do not transfer … by lexical reuse."*
- `helios/papers_00_data_src_specs/**/{*_synonym_*,*_antonym_*,…}.spec.yaml` — the **reified sense-relation
  atom families** keyed on `source_atom_urn`: `Synonym` (Atlas col 10, `cceo:SemanticComparing`),
  `Antonym` (col 17, `cceo:IsomorphicComparing`), `PreferredTerm` (col 19 PreferredToTerms,
  `cceo:ActOfJudging`), `Replacement` (col 11 ReplacedBy), `Translation` (`…/ActOfInterpretation`),
  `EnumMembership` (col 9 ValidValuesFor, `cceo:Classification`). Worked witness: `"node"` is the
  `source_atom_urn` of a **Synonym arrow** (`object↔node`) AND an **Antonym arrow** (`node↔arrow`)
  simultaneously.
- `helios/01_data_src_specs/products/_demo.md` — **the literal mole at the grounding altitude**: one CCO
  IRI `cco:ont00001234` (DataSet) grounds anchors in **two disjoint domains** (encyclopedia Mittens
  cheese-plate AND BLS CPI) — "one IRI, two disjoint domains, no code change."
- **Maps consulted:** `papers_atoms_map.md` (§4 relational families + Atlas cols), `srcy_map.md`
  (§6 SP6 = term_authority + frame-sort + cheese-trap negative-regression), `data_specs_contracts_map.md`
  (§8 `_demo.md`; `shacl_shape_coverage` SynonymShape/AntonymShape same style; `universal_anchors`).

**SP1 floor consumed:** `basicttl/primitives/{formal,physical,realization,taiji}.ttl` +
`primitives.{shapes.ttl,queries.sparql}`. Namespace: `gloss: <urn:silmaril:gloss:#>` (full-lexical URN
idiom, unary law), grounding onto `prim: <urn:silmaril:prim:#>` (SP1) and `aob: <urn:silmaril:aob:#>` (SP2).

---

## 1. Goal (precisely) — polysemy is authored at FOUR altitudes, each lifted

The maintainer's polysemy is not one mechanism; the Helios source realizes it at four independently-typed
altitudes. SP6 lifts all four and glues them with one progenitor discipline.

1. **Lexeme altitude — the progenitor law (`06_frame_sort_separation`).** One word → N **disjoint typed
   sorts**, with **no implicit map** between sorts. This is *the* polysemy progenitor: `gloss:Sort` is the
   agnostic parent; a shared lexeme carrying two sorts is legal iff the two sorts are declared disjoint and
   any transition is an **explicitly typed map**, never lexical reuse. Frame's 6 sorts are lifted verbatim
   as the reference instance.
2. **Authority altitude — the glossary (`term_authority.yaml`).** A **`gloss:Glossary` IS a citation
   authority**; its `gloss:authorityType` (progenitor + children lifted from the file's `authority_type`
   values) IS its epistemology. One lexeme bound under ≥2 distinct authorities/`authorityType`s is
   polysemy; the **`Mittens`(local_colimit_anchor) vs `Felis catus`(local_taxonomy_label) vs
   `catus`(negative_regression)** triad is the worked litmus, and the anti-collapse rule
   (*Felis catus is a taxonomy leg, **not** Mittens identity*) is the frame-sort law applied: identity-sort
   ≠ classification-sort, no implicit map.
3. **Sense-arrow altitude — the reified relations (papers_00 `*_synonym_*`/`*_antonym_*`).** Synonymy and
   antonymy are **reified arrows keyed on `source_atom_urn`**, each grounded in a **distinct CPO process**
   (Synonym→`cceo:SemanticComparing`, Antonym→`cceo:IsomorphicComparing`) and populating a **distinct Atlas
   column**. Because the two families are separate arrows on the SAME `source_atom_urn`, one term is a
   synonym-source AND an antonym-source at once — the literal simultaneity.
4. **Grounding altitude — the cross-domain anchor (`_demo.md`).** One `cco:ont########` IRI grounds ≥2
   **disjoint domains**; the upper-anchor speaks distinct epistemologies. This is the dual of altitude 1
   (there: one word / many disjoint sorts; here: one IRI / many disjoint domains).

**Corpus-agnostic:** pure shape + a small **synthetic witness mole** lifting only the *shapes* of the
worked witnesses (Mittens/Felis-catus/catus; node synonym+antonym; `cco:ont00001234` two-domain; and
the **reflexive own-vocabulary** witness — the lexeme `"colimit"` held as a genuine per-primitive
colimit under the local glossary AND an `ObservedProjection(ColimCandidate(D))` cocone under the corpus
glossary, plus `"frame"` across its disjoint sorts, Directive 16) as epistemology tags emptied of live
corpus, to keep the ASK suite non-vacuous — mirroring SP1's "what's a number" litmus and SP2's
one-witness-atom discipline.

---

## 2. Architecture — one referent manifold, many authority-charts; polysemy = chart-dependence

Nothing categorical is invented; SP1's exact machinery is re-used, and the four Helios altitudes are glued
by the **progenitor + composability** ethos (every distinct thing its own atom with an agnostic parent and
explicit children via `ancestry.via`).

```
                     one shared REFERENT MANIFOLD   (term identities: SP1 Text + URN, sha256 → Bit)
                    ╱            │             ╲
      gloss:Glossary_A     gloss:Glossary_B     gloss:Glossary_C …   (each = one AUTHORITY = one epistemology)
      authorityType:α       authorityType:β       authorityType:γ      ← lifted term_authority.yaml values
            │                     │                     │
     Synonym@SemanticComparing  Antonym@IsomorphicComparing  Translation@ActOfInterpretation
        (Atlas col 10)             (Atlas col 17)               ← reified sense arrows on source_atom_urn
            └─────── OSSIE mime arbiter (YIN/YANG mutual-colimit) ───────┘
                       registers the intended collision  ⇒  LITERAL POLYSEMY
```

- **Progenitor families (the composability spine).** Three agnostic progenitors, each with children whose
  `ancestry.via` points at the parent (the endianness→{little,big,host,none} pattern one level up):
  - `gloss:Sort` → {`sort_cap`, `sort_auth`, `sort_lin`, `sort_image_region`, `sort_output_effect`,
    `sort_video_time`} — the 6 frame sorts, plus room for domain sorts; disjointness is a declared law,
    not an accident.
  - `gloss:AuthorityType` → {`local_colimit_anchor`, `local_taxonomy_label`, `local_negative_regression_label`,
    `local_component_family_label`, `local_class_label`, `local_source_witness_label`, `official_spec`,
    `standard`, `project_documentation`, `research_paper`, …} — **lifted verbatim** from the file's
    `authority_type` values. Each is one epistemology.
  - `gloss:SenseRelation` → {`SynonymArrow`, `AntonymArrow`, `PreferredToArrow`, `ReplacedByArrow`,
    `TranslationArrow`, `ValidValuesForArrow`, `SeeAlsoArrow`} — the Atlas ring columns, each child pinning
    its `gloss:atlasColumn` ordinal and its `gloss:cpoProcess` (the distinct `cceo:` process). Nothing
    crammed: synonym and antonym are **separate atoms**, never an either/or flag.
- **The glossary = an authority; the entry = an AOB atom.** `gloss:Glossary` is one `term_authority`
  authority carrying exactly one `gloss:authorityType`. A `gloss:GlossaryEntry` is the `(lexeme, glossary,
  authorityType, allowedUse, sourceStatus)` binding — it **IS an `aob:AOBAtom`** (SP2) whose `aob:aobValue`
  is an SP1 colimit-taiji `prim:Primitive`. The lexeme's **referent identity** (URN + `source_sha256`,
  byte-descending to `prim:Bit` via SP2 octet descent) is **coherent across glossaries**; only its **sense
  coordinates diverge** (identity-coherent / sense-divergent — see Q2).
- **Sense relations are reified ARROWS (the teeth).** Following SP1's `prim:SubtypeArrow` discipline, every
  relation is a first-class reified arrow carrying `gloss:sourceAtomUrn` (S), `gloss:targetAtomUrn` (O),
  `gloss:cpoProcess` (P — the distinct `cceo:` process = the Predicate), `gloss:inGlossary`, `gloss:leftTerm`,
  `gloss:rightTerm`, `gloss:directionality`, `gloss:atlasColumn` — the exact field set of the papers_00
  Synonym/Antonym atoms. This (S=source, O=target, P=cceo-process) is the seed-schema `yoneda_hom_leg`
  shape SP1/SP3 already ground. A bare triple is NOT admissible; the arbiter and SHACL both walk these arrows.
- **The arbiter = CPO-process discrimination + OSSIE mime.** The synonym-vs-antonym distinction is not
  free-floating: it is grounded in a **distinct load-bearing `cceo:` process** (SemanticComparing vs
  IsomorphicComparing), resolved against `MergedAllCoreOntology.ttl` (CCO 2.x under BFO). The **OSSIE mime**
  is the literal arbiter (Rule 6): each intended collision is an SP1-shape **YIN/YANG mutual-colimit**
  (YANG = the AOB is_a-spine ontology reading, YIN = the OSSIE semantic-model reading of the SAME referent,
  glued by `gloss:gluedByMime`), carrying a `gloss:MimeArbitration` that marks it **registered**. An
  un-arbitrated collision is `silm:isProvisional true` with a documented gap (Präriehund) — never silently
  green. Same colimit as SP1 (formal⊕physical) and SP2 (base⊕claims), third level: YANG-ontology⊕YIN-model
  (turtles all the way, Directive 6).
- **Yoneda / ologs-of-ologs, consumed not re-built.** Each glossary is a presheaf over the referent
  category (the "sense sheaf of the lexeme over its arrows"). Because each entry's value is an SP1
  `prim:Primitive` whose gluing SP1 already closed as **literal Yoneda (Frame = the Yoneda point)**, SP6
  *inherits* that closure; it records the presheaf reading as one edge (`gloss:senseSheafOf` into SP1's
  representables) and does **not** re-materialise a second presheaf category this iteration (YAGNI, §6;
  mirrors SP2).

- **Worked example — the project's OWN design vocabulary obeys this law (Directive 16, the reflexive
  polysemy).** The maintainer's ruling on the "colimit" divergence is "Polysemy!": **"colimit" is ONE
  lexeme carrying TWO glossary-scoped senses simultaneously, without contradiction** — the same
  mole-of-glossaries mechanism SP6 builds for the corpus, now turned reflexively on our own vocabulary.
  - **`gloss:Glossary_local` (per-primitive epistemology; SP1/SP2's sense).** Here "colimit" denotes the
    finite two-object twin-olog gluing whose **universal property is provable**; SP1 **earns** the word
    with a `q_colimit_universal` tooth, and SP2's sealed-group apex reuses it. `authorityType:
    local_colimit_anchor` — the same `term_authority` authority that anchors Mittens.
  - **`gloss:Glossary_corpus` (artifact epistemology; SP9's sense).** Here the same lexeme denotes
    `ObservedProjection(ColimCandidate(D))` — the node_arrow monograph's **honest cocone**, "still a
    rendered artifact and not the substrate itself," certified by digest equality, **not** a literal
    colimit.
  These are a `gloss:PolysemyCollision` on the lexeme `"colimit"`: a genuine-colimit sense under the
  local authority and an honest-cocone sense under the corpus authority, **held at once and not
  contradictory** because they are **distinct glossary-scoped entries** (the scoping law above). The
  OSSIE-mime arbiter registers it as intended; SP2 references the local sense, SP9 the corpus sense,
  **both through this glossary layer, never bare** — so SP2 and SP9 are the two glossary poles of the
  one word. **`"frame"` is the sibling reflexive example**: one lexeme, the six disjoint
  `06_frame_sort_separation` sorts, `Frame(O,E)=O×E` being the sense SP1's `prim:Frame` uses — already
  lifted as SP6's `gloss:Sort` reference instance (altitude 1). Both cases are the design **obeying its
  own polysemy law** — turtles all the way, reflexively.

**Why this is not decorative:** every asserted law in §2 has a biting tooth in §4. The scoping law is
load-bearing and proven both ways — the cross-glossary collision ASK returns *false* on a collapsed mole
(non-vacuous), and the same-authority contradiction shape flips `conforms=True → False` under an injected
in-glossary syn+ant pair on one `(source_atom_urn, target)`.

---

## 3. File layout (one-file-per-concern; STRICTNESS Rule 14; `urn:` namespace)

Directory: `basicttl/glossary/`. Categorical grounding in the data ttls; teeth in shapes/queries (SP1/SP2 split).

| file | responsibility |
|------|----------------|
| `glossary/sort.ttl` | **the polysemy progenitor law** (lifts `06_frame_sort_separation`): `gloss:Sort` agnostic progenitor + the 6 disjoint frame-sort children (each `ancestry.via` → `gloss:Sort`); `gloss:disjointFromSort` (no implicit map); `gloss:sortTransition` = the only admissible cross-sort map, an explicitly typed arrow |
| `glossary/authority.ttl` | **the glossary = authority** (lifts `term_authority.yaml`): `gloss:Glossary`, `gloss:AuthorityType` progenitor + children (verbatim values), `gloss:GlossaryEntry` = `(lexeme, glossary, authorityType, allowedUse, sourceStatus, citationKey)` AOB atom; `gloss:Lexeme` (identity = string + `source_sha256`, grounded SP1 `prim:String`+`prim:URN`); the Mittens/Felis-catus/catus worked triad + `gloss:antiCollapse` (identity-sort ≠ taxonomy-leg-sort) |
| `glossary/sense_relations.ttl` | **the reified Atlas-ring sense arrows** (lifts papers_00 relational families): `gloss:SenseRelation` progenitor → the 7 children, each pinning `gloss:atlasColumn` (10/17/19/11/9/… ) + `gloss:cpoProcess` (`cceo:*`); every arrow carries `sourceAtomUrn`/`targetAtomUrn`/`inGlossary`/`leftTerm`/`rightTerm`/`directionality` |
| `glossary/polysemy.ttl` | **the collision law + `_demo` cross-domain grounding**: `gloss:PolysemyCollision` binding a `SynonymArrow@A` and an `AntonymArrow@B` on the SAME `sourceAtomUrn` (`A ≠ B`); `gloss:CrossDomainGrounding` = one `cco_grounding_iri` grounding ≥2 disjoint `gloss:Domain`s (the `cco:ont00001234` witness); same-authority contradiction is the rejected shape; the **reflexive own-vocabulary witness** (Directive 16) — the lexeme `"colimit"` as a `gloss:PolysemyCollision` across `gloss:Glossary_local` (genuine per-primitive colimit, universal property earned) vs `gloss:Glossary_corpus` (`ObservedProjection(ColimCandidate(D))` cocone), and `"frame"` across its disjoint sorts |
| `glossary/ossie_arbiter.ttl` | **OSSIE mime = arbiter**: `gloss:OssieMime` (YIN semantic-model twin), `gloss:MimeArbitration` (`gloss:arbitrates` a collision, marks registered/intended), per-collision YANG/YIN mutual-colimit (`gloss:yangFacet`/`gloss:yinFacet`/`gloss:gluedByMime`) on the SP1 taiji shape; `gloss:ossieSemanticModelRef` inert locator (no live validation this iteration) |
| `glossary/glossary.shapes.ttl` | SHACL law (§4) — one `sh:NodeShape` per invariant; `sh:sparql`/`sh:in` (defang-proof); CCO/CPO patterns **reference the `universal_anchors` `pattern_anchor` URNs, never inline regex** (`node:identifier:cco_grounding_iri`, `arrow:identifier:cpo_process_iri`) |
| `glossary/glossary.queries.sparql` | EXPECT-TRUE ASK suite (§4), each with an inline DATA CONTRACT comment |
| `glossary/checks/run-glossary-checks.sh` + `glossary/README.md` | runner (parse + pyshacl + depth gate + every ASK) and the layer doc + consumer list + how-to-re-run |

Every `owl:Class` carries a ≥200-char `rdfs:comment` (depth gate). Full-lexical identity internally;
external spellings (`OSSIE`, `sha256`, `cceo`, `TSN`, `GlossaryName.TermName`) survive only as immutable
bridge evidence. Five data ttls + shapes + queries + runner/readme.

---

## 4. Verification plan (evidence-first; SHACL + EXPECT-TRUE ASKs; each proven by probe injection)

SP1 discipline: every ASK RED before authoring, GREEN after; each SHACL shape and each ASK proven to
**bite** by targeted injection (`conforms=True → False`, `ASK True → False`); no ASK vacuous (positive ASKs
return false on the empty graph). Runner loads the five data ttls into one graph, validates against
`glossary.shapes.ttl` (shapes graph only, never mixed into data), runs the depth gate, requires every ASK true.

| ASK (EXPECT-TRUE) | asserts (traced to the lifted source) | probe of record (must be CAUGHT) |
|---|---|---|
| `q_lexeme_grounds` | every `gloss:Lexeme` grounds into SP1 `prim:String` + a `prim:URN` identity whose `source_sha256` byte-descends (SP2 octet) to `prim:Bit` | a lexeme with no SP1 String/URN grounding |
| `q_entry_is_aob_atom` | every `gloss:GlossaryEntry` is an `aob:AOBAtom` scoped to exactly one `gloss:Glossary`, with an `aob:aobValue` `prim:Primitive` and exactly one `gloss:authorityType` | an entry with no glossary / two authorityTypes / not an AOB atom |
| `q_glossary_epistemology_distinct` | the mole holds **≥4** `gloss:Glossary` individuals with pairwise-distinct `gloss:authorityType` (each a distinct epistemology, `term_authority` values) | collapsing two glossaries onto one authorityType (count < 4) |
| `q_authority_polysemy` *(litmus 2)* | the SAME referent is addressed by ≥2 lexemes under **distinct authorityType** (`Mittens`=colimit_anchor vs `Felis catus`=taxonomy_label), and the cross-lexeme link is a **typed classification arrow**, not an identity equation | (positive) false on a single-authority mole → non-vacuity |
| `q_anti_collapse` | NO arrow equates an identity-sort lexeme with a taxonomy-leg-sort lexeme across the disjoint sorts (`Mittens ≠ "catus"`; frame-sort "no implicit map") | an injected `Mittens owl:sameAs "catus"` / a taxonomy-leg promoted to identity |
| `q_sense_collision` *(litmus 3, load-bearing)* | there EXISTS a `sourceAtomUrn` bearing a `SynonymArrow@SemanticComparing` (col 10) **and** an `AntonymArrow@IsomorphicComparing` (col 17) in distinct glossaries — the `"node"` witness | (positive) false on an empty/single-glossary mole |
| `q_scoped_no_contradiction` | NO glossary holds both a `SynonymArrow` and an `AntonymArrow` on the same `(sourceAtomUrn,target)` **within itself** (the scoping law that makes cross-glossary collision non-contradictory) | an injected in-glossary syn+ant pair on one `(S,O)` |
| `q_cross_domain_grounding` *(litmus 4)* | one `cco_grounding_iri` (matching the `pattern_anchor`, resolvable in CCO) grounds ≥2 disjoint `gloss:Domain`s — the `cco:ont00001234` two-domain witness | collapsing the two domains to one / a fabricated IRI failing the anchor pattern |
| `q_arbiter_registered` | every `gloss:PolysemyCollision` carries a `gloss:MimeArbitration` (registered/intended) OR is `silm:isProvisional true`; no collision silently green | a collision with neither arbitration nor provisional flag |
| `q_pair_inspectable` | every sense arrow carries `sourceAtomUrn`+`targetAtomUrn`+`cpoProcess`+`inGlossary` (fully inspectable & checkable) | a pair missing `inGlossary` or `cpoProcess` (dangling/unprovenanced) |
| `q_taiji_twin` | every `gloss:PolysemyCollision` carries a `gloss:yangFacet` (AOB ontology) AND `gloss:yinFacet` (OSSIE model) glued by `gloss:gluedByMime`; the mutual-colimit round-trip closes | a collision with YANG but no YIN twin (half-taiji) |
| `q_reflexive_own_vocabulary` *(reflexive polysemy, Directive 16 — our design vocabulary obeys our own law)* | the lexeme `"colimit"` has **two distinct glossary-scoped `gloss:GlossaryEntry`s** — a genuine-colimit sense under `gloss:Glossary_local` (`authorityType local_colimit_anchor`, universal property earned) AND an `ObservedProjection(ColimCandidate(D))` cocone sense under `gloss:Glossary_corpus` — bound as ONE `gloss:PolysemyCollision`, arbitration-registered, **no contradiction** (SP2 references the local sense, SP9 the corpus sense); likewise `"frame"` across its disjoint sorts | collapsing the two "colimit" senses into one glossary entry (forces a contradiction) / asserting `owl:sameAs` between the local-colimit and corpus-cocone senses |

SHACL mirrors (one per invariant, each `sh:sparql`/`sh:in`, defang-proof; CCO/CPO patterns via
`pattern_anchor` URN reference, never inline regex): `gloss:LexemeGroundingShape`, `gloss:EntryIsAtomShape`,
`gloss:GlossaryDistinctnessShape`, `gloss:AntiCollapseShape`, `gloss:ScopedRelationShape` (same-glossary
contradiction guard), `gloss:CrossDomainGroundingShape`, `gloss:ArbitrationHonestyShape`,
`gloss:PairInspectableShape`, `gloss:TaijiTwinShape`, `gloss:ReflexivePolysemyShape` (the
own-vocabulary "colimit"/"frame" tooth — the two senses are distinct glossary-scoped entries of one
lexeme, never `owl:sameAs`, Directive 16). Depth gate: every `owl:Class` ≥200-char.

**Litmus (the maintainer's SP6 test):** `q_sense_collision` + `q_scoped_no_contradiction` together are the
"one term, synonym here, antonym there, on purpose, and it does not break" proof — SP6's "what's a number".

---

## 5. Interfaces

### Consumes

**SP1 (committed floor):** the **Text tower** (`prim:String`, `prim:Codepoint`, `prim:Grapheme`) — lexeme
identity; the **Identifier URN tower** (`prim:URN ⊃ URI ⊃ IRI`, `prim:QName`) — every URN; **`prim:Kleene3`**
— the structured↔unstructured indeterminacy; the **colimit-taiji `prim:Primitive`**
(`formalFacet`/`physicalFacet`/`gluedBy`) + the OSSIE YIN/YANG taiji shape SP1 names — the per-collision
YANG/YIN mutual-colimit is this shape lifted one level; the **literal-Yoneda layer**
(`prim:RepresentablePresheaf`, Frame = Yoneda point) — the glossary-as-presheaf reading is an edge into it,
not re-materialised; the **Ordinal tower** (`prim:Ordinal`) — the Atlas-column ordinals (10/17/19/11/9/…).

**SP2 (AOB meta-ontology):** **`aob:AOBAtom` + `aob:aobValue`** — every glossary entry IS an AOB atom;
the **Atlas ring + Synonyms/Antonyms simultaneity seam + the glossary-scoped predicate + the OSSIE-mime
anchor hook** (SP2 hands SP6 the declared seam; SP6 builds the mechanism); **`aob/octet_descent.ttl`** —
the lexeme `source_sha256` byte-descent to `prim:Bit`; the **CCO/CPO `pattern_anchor`** (`universal_anchors`
`node:identifier:cco_grounding_iri`, `arrow:identifier:cpo_process_iri`, resolved against
`MergedAllCoreOntology.ttl`) — SHACL patterns reference these, never inline regex.

**SP3 (N-dim CRS = S/O/P towers):** the **`crs:GlossaryChart` CRS mechanism** — one chart per authority
epistemology over the shared referent manifold; a sense arrow's (source, target, cpoProcess) IS the
(S, O, P) seed; partial transition maps between charts are the intentional non-agreements.

**SP4 (projection packet):** the **`ossie` projection surface** — where SP6's collisions get mime-confirmed;
SP4's `SemanticLoss` class is the loss carried on a partial transition.

**SP5 (file + format taxonomy):** the **`fmt:hasGlossary` seam** — every format carries its own glossary
(SP5 holds the binding PROVISIONAL); SP6 supplies the glossary type that fills it *(edge-direction — Q1)*.

**Authored WIP substrate (lifted, not invented — Directive 1):** `term_authority.yaml` (glossary=authority,
`authority_type` epistemologies, Mittens/Felis-catus/catus triad, anti-collapse); `06_frame_sort_separation`
(6 disjoint sorts, no implicit map); the papers_00 `Synonym`/`Antonym`/… relational atoms (reified arrows on
`source_atom_urn`, distinct `cceo:` process, Atlas columns); `products/_demo.md` (`cco:ont00001234` two
disjoint domains).

### Produces (named, for higher sub-projects; consistent with the DAG)

- **SP7 (SHACL executable law):** the nine `gloss:*Shape`s — especially `gloss:ScopedRelationShape` and
  `gloss:ArbitrationHonestyShape` — as the polysemy half of the W2 executable law.
- **SP8 (basicttl depth remediation):** the grounding target for the corpus `Synonym`/`Antonym`/
  `PreferredTerm`/`Replacement`/`Translation`/`EnumMembership` atoms and `term_authority` records — each
  becomes a `gloss:GlossaryEntry` / reified sense arrow grounded here.
- **SP9 (render seal):** the per-collision YANG/YIN **mutual-colimit** (mime arbiter = gluing morphism) =
  the per-glossary-atom instance of split↔consolidated reversibility; partial transitions carry the honest
  loss the seal must preserve. **And (Directive 16) the CORPUS / artifact sense of the polysemous lexeme
  "colimit"** — `ObservedProjection(ColimCandidate(D))`, which SP9 keeps — which SP6 holds as ONE lexeme
  together with the LOCAL / per-primitive genuine-colimit sense that SP2's sealed-group apex references,
  so **SP2 and SP9 are the two glossary poles of the same word**, both referencing it through this layer,
  never bare (the reflexive worked example, §2).
- **W5 (re-runnable corpus binding, phase `w5_5`):** the OSSIE-mime arbiter **mechanism** live-corpus
  collision resolution invokes — SP6 builds the arbiter; W5 feeds it real collisions.

---

## 6. Non-goals (this iteration; YAGNI deferrals)

- **No live-corpus glossary content** (W5, `w5_5`). Pure shape + a synthetic witness mole (≥4 glossaries,
  the node synonym+antonym triad, the `cco:ont00001234` two-domain triad, the Mittens/Felis-catus/catus
  triad) for non-vacuity only.
- **No live Apache OSSIE engine** — the mime arbiter is an ontology coordinate (YIN/YANG taiji +
  `MimeArbitration` + inert `ossieSemanticModelRef`); running a real OSSIE validator is corpus/CI *(Q3)*.
- **No second presheaf category re-materialised** — the glossary-as-presheaf turtle is an edge into SP1's
  already-Yoneda-closed representables (mirrors SP2).
- **No CRS geometry internals** — SP6 instantiates SP3's `GlossaryChart`; the chart algebra is SP3's.
- **No projection algebra** — the `ossie` arbiter surface is consumed from SP4.
- **No automatic collision resolution** — SP6 *registers and inspects* intended collisions and flags
  un-arbitrated ones as provisional; it does not auto-resolve which reading "wins" (W5's `PreferredToTerms`/
  `ReplacedBy` over live data).
- Built to be **challenged and relaunched**, not final (Directive 13).

---

## Open questions for the maintainer (Präriehund — flagged, not invented)

1. **SP5↔SP6 edge direction (and phase-level edges generally).** The DAG has no `silm:dependsOn` between W2
   *phases* (only *workflows*) — every sibling SP flags this. SP5 declares `fmt:hasGlossary` and marks the
   glossary-class binding PROVISIONAL "so it works either way"; the ordinal reads "SP5 produces the seam,
   SP6 fills it", while the brief lists SP6 under SP5's *Consumes*. Add explicit
   `phase_w2_sp6 silm:dependsOn phase_w2_sp{1..5}` edges and pin SP5↔SP6, or is ordinal + seam-PROVISIONAL
   the intended contract?

2. **Identity-coherent vs sense-divergent (the load-bearing tension).** `term_authority.yaml` gives one
   referent multiple names each with a distinct `authority_type`, and the anti-collapse rule (Felis catus
   ≠ Mittens identity) says the classification leg must not become identity. My resolution: a lexeme's
   **referent identity** (URN, `source_sha256`) is coherent across glossaries; its **sense relations**
   (synonym/antonym roles, authority_type) are glossary-scoped and intentionally collide — same point,
   different coordinate (the CRS picture + the frame-sort disjointness). Is this identity-coherent /
   sense-divergent split the intended reading? (I assert it as the design's spine; confirm before build.)

3. **OSSIE-mime arbiter depth this iteration.** Is the arbiter a **lifted OSSIE semantic-model YIN twin per
   collision** (full mutual-colimit taiji, modeled as ontology), or a **declared-but-inert mime-anchor
   coordinate** deferred to W5 (like SP2's inert CCO anchor)? I have it as the modeled-taiji shape with an
   inert `gloss:ossieSemanticModelRef` locator (no live validation).

4. **Witness-mole names.** Should the corpus-agnostic witness mole lift the **real `authority_type` values**
   from `term_authority.yaml` (as empty-of-corpus epistemology tags) plus the `"node"` synonym/antonym and
   `cco:ont00001234` two-domain witnesses, or author fully synthetic neutral authorities? (I lean: lift the
   real `authority_type` names + the two worked witnesses — they are shape, not corpus — but confirm this
   stays corpus-agnostic.)

5. **Frame-sort scope in SP6.** `06_frame_sort_separation` names 6 sorts including image/video/effect sorts
   that are largely SP1/SP4 concerns. Should SP6's `gloss:Sort` lift **all 6** as the reference disjointness
   instance (my choice, for the anti-collapse law), or only the lexeme/authority-relevant sorts, leaving the
   physical sorts to SP1/SP4 and referencing them by URN?

6. **Canonical depth predicate (PIN-AT-WRITING-PLANS — do not resolve here).** The ≥200-char depth predicate
   is enforced at three sites (SP7 `FederationDepthShape`, SP8 `NoStubClassShape`,
   `scripts/ontology-depth-check.py`) — the plans must name ONE canonical depth predicate the others
   reference.
