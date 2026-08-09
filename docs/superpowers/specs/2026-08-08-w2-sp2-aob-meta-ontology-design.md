# W2 · Sub-project 2 — the AOB meta-ontology (design)

> **Batched design doc** (superpowers:brainstorming output; design-only — no `.ttl`/`.sparql`/
> implementation authored here). Directive 14 cadence: SP2–SP9 designed up front, one maintainer
> review pass, each still a real design. **THIS ITERATION's v1** — corpus-agnostic (Directive 13),
> built to be re-run and relaunched, never for permanence. Zero live-corpus binding (that is W5).

**Goal.** Author the corpus-agnostic **meta-TBox** that says, with teeth, exactly what an **AOB atom
is** — by **LIFTING the real WIP AOB already authored in the Helios library** (Directive 1: lift, do
not invent). The AOB atom's **VALUE is an SP1 colimit-taiji `prim:Primitive` instance**; its identity
is a **sha256 over octets**; its byte/tensor field grounds into SP1's physical carriers + the
`byte_order` progenitor; every node atom carries exactly one CCO IRI and every arrow atom exactly one
CPO process IRI (load-bearing upper anchor). The sealed group of an atom + its companions forms a
**group** (identity = base atom, compose = associative colimit, retract = inverse).

**Binding sources** (gospel): `docs/unary-byte-frame-law.md`,
`docs/praeriehund-demokratie-der-kategorien.md`, `ledger/W2/design_constraints.md` (Directives 1, 2,
3+refinement, 6, 12–14). **SP1 floor consumed:** `basicttl/primitives/{formal,physical,realization,
taiji}.ttl` + `primitives.{shapes.ttl,queries.sparql}` (committed, green).

**Helios structures LIFTED** (git-ignored source-of-truth; do NOT commit `helios/`):

1. **The `_aob_*` atom envelope** — `helios/srcy/appendices/39_appendix_e_research_source_mirror/
   sections/specs/atoms/` (271 `_aob_*.yaml.tex`; read `core/entity/_aob_entity_register.yaml.tex` in
   full). Fields lifted: `urn` + `urn_spec.{atom_urn,function_urn,fut_urn,consumes,emits}`,
   `identity.{name,layer,domain,type,description}`, `kind: u:AtomicObject`, `version` (semver),
   `signature.{inputs[{name,type,type_urn,doc}],outputs,emits,errors}`, the **`avd_tree`** observation
   matrix (`SPACE`/`A_RANGE{min,max,step,distribution}`/`DEPTH.integer_value`/`E2E`/`SOURCE`/`SINK.points_at`/
   `SMOOTHNESS`/`INSTRUCTION-AWARENESS`/`UNIT-TEST-GENERATION.test_cases[]`),
   `swe_as_dag_accounting.{cites,feeds,graduation_target}`, `glue_binding`, `incorporates_from`,
   `produces`, `consumes_avro_records`, `test_generation.{samples,failure_cases,fut_path_relative}`.
2. **The universal per-paper atom envelope + the ~17,071 materialized atoms** —
   `helios/papers_00_data_src_specs/` (11 papers). Lifted: `entity.{urn, display_name, layer,
   kind_urn, type_node, type_urn, grounding, fields, ancestry:[{axis,via}], citations}` +
   `triad_render.{elixir_module, out_paths}`; the **22 `type_node` families**; the **PaperSection
   cocone apex** carrying `companion_atoms[]` (one section = a colimit of ~6–15 companions); the
   **4 lock-step `addl_*` metadata projections**; `CircuitImprintTensor` (witness-not-inferred);
   Synonym (col 10) / Antonym (col 17) simultaneity; `CheeseTrapImmunity`.
3. **The 2-family seed schema + `triad_render` tensor block** —
   `helios/01_data_src_specs/products/` + `helios/00_src_specs/types/silmaril_wave8/*.spec.yaml`.
   Lifted: `concrete_anchor` (node: `bare_symbol`, `anchor_node`, `anchor_text`, `cco_grounding_iri`,
   `atom_family_urn`, `top_kind: node`) + `yoneda_hom_leg` (arrow: `source_node_urn`=**S**,
   `target_node_urn`=**O**, `cpo_process_iri`=**P**, `atom_family_urn`, `top_kind: arrow`); the
   **three-axis tensor block** (`space{cardinality,dimensions,bounded,max_size,bit_width,byte_width,
   alignment}` / `time{dynamics,ordering,monotonic,lifetime,byte_order,arithmetic}` / `value{interpret_as,
   domain,read_via,write_via}`); `triad_render.{bash_namespace,elixir_module,out_paths.{bash,elixir}}`
   + `rendered_legs: [sh, ex, atlas.csv, ttl, shacl.ttl, sparql, linkml.yaml]`; `source_sha256` (the
   AtomCommon Avro identity).
4. **The Layer-0 upper-anchor law** — `helios/01_data_src_specs/universal_anchors.spec.yaml` (11
   anchors, `algebra_role: pure_seed`, `layer: 0`). Lifted verbatim: node atom → exactly one
   `cco_grounding_iri` matching `^cco:ont[0-9]{8}$` (`resolves_in_env: SIL_CCO_TTL_DIR`); arrow atom →
   exactly one `cpo_process_iri` matching `^cceo:[A-Za-z0-9_]+$` (`SIL_CPO_TTL_FILE`), resolved against
   `MergedAllCoreOntology.ttl` (CCO 2.x, under BFO). Patterns are **anchor URNs referenced, never
   inlined regex**.

Namespace: `aob: <urn:silmaril:aob:#>` (full-lexical URN idiom, unary law), grounding onto
`prim: <urn:silmaril:prim:#>`. External spellings (`sha256`, `cco:`, `cceo:`, `SHACL`, `UTF-8`)
survive only as immutable bridge evidence.

---

## 1. Goal (precisely)

Produce the meta-TBox that fixes, with teeth, what an AOB atom **is**:

1. an atom is a **two-family progenitor split** (`top_kind: node | arrow`) — `concrete_anchor` nodes
   and `yoneda_hom_leg` arrows — each modelled as its own addressable `atom_family_urn` (nothing
   crammed); the arrow carries the **S/O/P** carrier `(source_node_urn, target_node_urn,
   cpo_process_iri)` — the seed SP3 lifts into the CRS;
2. an atom + its companions is a **sealed group = a colimit** (the **LOCAL / per-primitive glossary
   sense** of the polysemous "colimit", Directive 16 — universal property earned by a tooth, referenced
   through SP6, never bare; see §2): the base atom is the group **identity**, companion/claim atoms
   **compose onto it** (associative; the `PaperSection.companion_atoms[]` cocone), **retract = inverse**
   (`Replacement`/`superseded` witnesses); the apex is ONE atom;
3. its **VALUE is a colimit-taiji `prim:Primitive`** over SP1 — `aob:aobValue : AOBAtom →
   prim:Primitive`; the atom's **formal facet** (its `type_urn` tower position) is glued to its
   **physical facet** (the tensor block) by SP1's realization ρ, with the **grounding = the Frame**
   carrying the byte/hash provenance effect;
4. it is **subatomic to the octet** (Directive 1): identity is a **sha256** (`source_sha256`) whose 32
   hexadecimal octets are each AOBed as a `prim:Octet` (ordinal 0..255) that `prim:byteDescendsTo+
   prim:Bit`; the tensor `time.byte_order` field grounds into the **`byte_order` agnostic progenitor**
   (`byte_order_none` here — UTF-8 prose atoms — with `{little,big,host}` its siblings in the floor);
5. every node atom carries **exactly one** `cco:ont########` IRI, every arrow **exactly one** `cceo:`
   process IRI, each a **`pattern_anchor_urn` reference** into `universal_anchors` (never inline regex),
   resolved against `MergedAllCoreOntology.ttl` — the load-bearing CCO/BFO upper anchor;
6. it carries the **`avd_tree` observation/evidence contract** (SPACE / A_RANGE / DEPTH / E2E /
   SOURCE→SINK / UNIT-TEST) — the atom-behaviour witness lifted from the `_aob_*` envelope;
7. it holds structured AND unstructured types as **synonyms AND antonyms simultaneously** (Synonym col
   10 `SemanticComparing`, Antonym col 17 `IsomorphicComparing`) — the **mole-of-glossaries seam** is
   declared here; the reconciliation **mechanism is SP6**.

Corpus-agnostic: pure shape, **zero corpus instances** (exactly as SP1). One tiny lifted witness atom
(one `concrete_anchor` + one `yoneda_hom_leg`) is authored purely to keep the ASK suite non-vacuous,
mirroring SP1's litmus discipline.

---

## 2. Architecture — two stacked colimits and a lifted monad (turtles all the way)

The AOB meta-ontology is the **second colimit layer** stacked on SP1. Nothing new is invented
categorically; SP1's exact machinery is re-used one level up.

```
                    aob:aobValue  (meta-functor)
   AOBAtom  ───────────────────────────────────▶  prim:Primitive   (SP1 taiji)
      │  = colimit over its companion diagram         = colimit(FormalType ─ρ→ PhysicalEncoding)
      │    (base atom = group identity;               formalFacet ⊕ physicalFacet, gluedBy ρ;
      │     companions compose; retract = inverse)     Frame IS the Yoneda point (SP1 closed it)
      ▼
   the atom's VALUE is itself an SP1 colimit-taiji atom
     ⇒ an OLOG whose objects are OLOGS  (Directive 2/6: "ologs of ologs, turtles all the way")
```

- **The progenitor split (lifted, not invented).** `top_kind: node | arrow` is the primordial
  bifurcation observed in every Helios facet. `aob:ConcreteAnchor` (node) and `aob:YonedaHomLeg`
  (arrow) are the two seed families; each declares its own `aob:atomFamilyUrn`. A node grounds via
  exactly one `cco_grounding_iri`; an arrow via exactly one `cpo_process_iri`. The arrow's
  `(source_node_urn, target_node_urn, cpo_process_iri)` is the **S/O/P** triple — literally a leg of a
  Yoneda hom-profile `Hom(−, A)` (hence the family name), which SP1 already materialised as
  `prim:RepresentablePresheaf` + `prim:YonedaArrow`.
- **The atom is a colimit (the sealed group).** Lifted from the `PaperSection` apex carrying
  `companion_atoms[]` (the cocone legs) and the `_aob_*` `graduation_target` seal. The base atom **is
  the group identity**; each companion (`Description`, `Example`, the 4 `addl_*`, `OlogBox`,
  `CircuitImprintTensor`, `CheeseTrapImmunity`, `DecompositionStep`, …) **composes onto it**
  (associative); **retract/supersede is the inverse** (`Replacement`/`superseded` witnesses). This
  makes the sealed group a **monoid/group object** whose colimit apex is the atom — the same colimit
  shape as SP1's taiji and the unary law's Atlas↔Graph colimit, reused not re-derived.
  **Polysemy scope (Directive 16):** "colimit" here is the **LOCAL / per-primitive glossary sense** of
  the polysemous lexeme — the finite companion-cocone whose **universal property is provable**, so the
  word is **earned by a tooth** (the `q_colimit_universal`-style universal-property ASK SP1 adds for
  its per-primitive taiji, mirrored here for the sealed-group apex), **not a bare assertion**. SP2
  references "colimit" **through the SP6 glossary layer, never bare**; the CORPUS / artifact sense of
  the same word (`ObservedProjection(ColimCandidate(D))`) is SP9's, and SP6 holds **both** glossary-scoped
  senses of the one lexeme simultaneously with a biting polysemy tooth (SP2 and SP9 are the two glossary
  poles of the same word).
- **The atom's VALUE is an SP1 taiji instance.** `aob:aobValue : AOBAtom → prim:Primitive` is a
  meta-functor into the floor. The atom's `formalFacet` is *what type it IS* (its `type_urn` tower
  position); its `physicalFacet` is the **three-axis tensor block** resolved to a
  `prim:PhysicalEncoding`; the gluing is SP1's ρ. The observed **grounding** prose ("what it asserts +
  the CPO/CCO process that licenses it") is precisely the **realization Frame**: output = the
  tensor-block encoding, **effect = the byte/hash provenance** (a lifted member of SP1's `prim:Effect`
  family).
- **Subatomic to the octet (Directive 1).** `aob:HashDigest` is the `source_sha256` identity carried
  as a `prim:ByteVector` of exactly **32 `prim:Octet`s** (each ordinal 0..255) that byte-descends to
  `prim:Bit` via SP1's `prim:byteDescendsTo` ladder — the hash is not opaque. The tensor
  `time.byte_order` field grounds into the **`byte_order` agnostic progenitor** in the floor; the
  first two octets of `source_sha256` are the **z-coordinate seed** SP3 consumes.
- **Monadic realization, consumed not re-built.** SP2 does **not** re-author ρ; it consumes SP1's
  Kleisli/Frame realization monad and asserts each atom's value selects one `gluedBy` realization.
  Byte-descent of the identity hash is Kleisli composition down to `prim:Bit`.
- **CCO/BFO load-bearing (lifted verbatim).** Every node names one `cco:ont########`; every arrow one
  `cceo:` process. The regex is **not inlined** — the shape references the `universal_anchors` anchor
  URN (`aob:patternAnchorUrn`), whose `pattern` + `resolves_in_env` resolve against
  `MergedAllCoreOntology.ttl` (CCO 2.x, under BFO). New anchors are `human_review_required,
  never_auto_merge` — carried as an honest governance note, not a runtime.
- **CircuitImprintTensor = witness, not inference.** Lifted discipline (verbatim grounding): *binary
  axes, cube/Hamming adjacency, and inferred relations are rejected; support and every directed
  relation require native-Frame witnesses and readback.* SP2 realizes it by binding
  `active_circuit_urns` support into SP1's `Frame(output, effect)` rather than re-inventing a tensor —
  exactly the unary law's "a scalar triple is not an admissible substitute for S/O/P towers."
- **Yoneda / ologs-of-ologs (Directive 2/6).** Because each AOB olog object *is itself* an SP1
  colimit-taiji atom (whose gluing SP1 already closed as literal Yoneda, Frame = the Yoneda point),
  the `aob:aobValue` edge realizes the maintainer's "tighter Yoneda realization of ologs-of-ologs,
  turtles all the way." SP2 records this as a real edge into SP1's already-Yoneda-closed primitives;
  it does **not** re-materialise a second presheaf category (YAGNI — §6). The **telephone twin**
  (`telephone_events` ⟷ `telephone_supervision_tree`, each field pinned to a Layer-0 anchor via
  `tensor_space_urn` = literal Yoneda-point tightness) is carried as a declared seam, PROVISIONAL
  (Directive 6, Q5).
- **Praeriehund seal honesty.** The `graduation_target` staged→gated discipline is the honesty spine:
  a staged (ungraduated) atom is `silm:isProvisional`, never counted conformant-green.
  `CheeseTrapImmunity` (failure-mode + immunity-mechanism) is the "don't collapse the category"
  discipline made a first-class atom — lifted, not paraphrased. `isProvisional` is reserved for
  genuinely undecidable gaps, never a dodge.

---

## 3. File layout (one-file-per-concern; STRICTNESS Rule 14; SP1's split)

Directory: `basicttl/aob/`. Categorical grounding lands in the data TTLs; teeth in the shapes/query
files (exactly SP1's split).

| file | responsibility |
|------|----------------|
| `aob/meta.ttl` | the meta-TBox: `aob:AOBAtom` + the `top_kind` progenitor split `aob:ConcreteAnchor`(node)/`aob:YonedaHomLeg`(arrow); the envelope coordinates (`urn`, `display_name`, `layer`, `kind_urn`, `type_node`, `type_urn`, `grounding`, `version` semver, `ancestry:[{axis,via}]`, `citations`); `aob:atomFamilyUrn` |
| `aob/group_law.ttl` | the sealed-group colimit: `aob:groupIdentity` (base atom), `aob:composesOnto` (associative companion cocone, `PaperSection.companion_atoms[]`), `aob:retracts` (inverse); the `graduation_target` staged↔gated seal state |
| `aob/octet_descent.ttl` | subatomic-to-octet: `aob:HashDigest` (`source_sha256`) as a `prim:ByteVector` of 32 `prim:Octet`s; the bridge `prim:byteDescendsTo` to `prim:Bit`; grounds atom identity; exposes the **z-seed** (first two octets) for SP3 |
| `aob/tensor_block.ttl` | the three-axis tensor block (`space`/`time`/`value`) grounded into SP1 physical carriers; `time.byte_order` → the `byte_order` agnostic progenitor; the `physicalFacet` for `aobValue` |
| `aob/upper_anchor.ttl` | the CCO/BFO law: `aob:ccoGroundingIri` (node, card 1..1) / `aob:cpoProcessIri` (arrow, card 1..1) as `aob:patternAnchorUrn` references into `universal_anchors` (no inline regex); `aob:resolvesInEnv` bridge to `MergedAllCoreOntology.ttl` |
| `aob/value_colimit.ttl` | the gluing: `aob:aobValue : AOBAtom → prim:Primitive`, the grounding-claim Frame, and the ologs-of-ologs meta-layer assertion (AOB olog objects ARE SP1 taiji atoms) |
| `aob/evidence_glossary.ttl` | the `avd_tree` observation contract (`SPACE`/`A_RANGE`/`DEPTH`/`E2E`/`SOURCE→SINK`/`UNIT-TEST`); `CircuitImprintTensor` witness-not-inferred bound to the Frame; the Synonym+Antonym simultaneity **seam** (glossary-scoped; OSSIE-mime hook) → SP6 |
| `aob/aob.shapes.ttl` | SHACL law (§4) — one `sh:NodeShape` per invariant, each proven to bite |
| `aob/aob.queries.sparql` | the EXPECT-TRUE ASK suite (§4), each with an inline DATA CONTRACT comment |
| `aob/checks/run-aob-checks.sh` + `aob/README.md` | the runner (parse + pyshacl + depth gate + every ASK) and the doc + consumer list + how-to-re-run |

Every `owl:Class` carries a ≥200-char `rdfs:comment` (depth gate). No internal abbreviations.

---

## 4. Verification plan (evidence-first; SHACL + EXPECT-TRUE ASKs; each proven by probe injection)

SP1's discipline: every ASK RED before authoring, GREEN after; each shape and each ASK proven to
**bite** by a targeted injection (`conforms=True → False`, `ASK True → False`); no ASK vacuous
(positive ASKs return false on an empty graph). The runner loads the seven data TTLs into one graph,
validates against `aob.shapes.ttl` (shapes graph only, never mixed into data), runs the depth gate,
and requires every ASK true. **Depth gate first** (SP1 gate discipline): no ASK is counted until every
`owl:Class` clears ≥200 chars.

| ASK (EXPECT-TRUE) | asserts | probe of record (must be CAUGHT) |
|---|---|---|
| `q_progenitor_split` | every `aob:AOBAtom` is exactly one of `aob:ConcreteAnchor`(node)/`aob:YonedaHomLeg`(arrow) with its own `aob:atomFamilyUrn`; nothing crammed | an atom with both/neither `top_kind` |
| `q_aob_value_is_taiji` | every atom has an `aob:aobValue` that is a `prim:Primitive` with `formalFacet`+`physicalFacet`+`gluedBy` (grounds into SP1) | a value lacking `physicalFacet` |
| `q_octet_descent` | the `source_sha256` identity is a `prim:ByteVector` of exactly 32 `prim:Octet`s (each ordinal 0..255) that `prim:byteDescendsTo+ prim:Bit` | a 33-octet digest, or an octet with `ordinalMax 256` |
| `q_sop_carrier` | every `aob:YonedaHomLeg` carries `source_node_urn`(S)/`target_node_urn`(O)/`cpo_process_iri`(P), each a URN-tower term | an arrow missing `target_node_urn` |
| `q_cco_bfo_anchor` | every node has **exactly one** `cco:ont########` and every arrow **exactly one** `cceo:` process, via an `aob:patternAnchorUrn` reference (no inline regex) resolving in `MergedAllCoreOntology.ttl` | a node with two CCO IRIs; an IRI failing the anchor pattern; an inlined `sh:pattern` literal |
| `q_group_law` | the base atom is `aob:groupIdentity`; every companion `aob:composesOnto` it (associative); a retract is the inverse of its companion (colimit closure — the **LOCAL / per-primitive glossary sense** of the polysemous "colimit", Directive 16, whose universal property is the **earned tooth**, referenced through SP6, never a bare assertion) | a companion composing onto a non-identity; a retract with no target |
| `q_tensor_byte_order` | every tensor block's `bit_width`/`byte_width` resolve to an SP1 `prim:PhysicalEncoding` whose `interpretAs` = the atom's `formalFacet`, and `time.byte_order` grounds in the `byte_order` progenitor | a `byte_order` not descended from the progenitor; a `bit_width` with no SP1 encoding |
| `q_synonym_antonym_dual` | one term is held as `Synonym` under glossary A **and** `Antonym` under glossary B **simultaneously**, no contradiction (distinct glossary epistemologies) | collapsing both into one glossary (forces a contradiction) |
| `q_seal_honesty` | every staged (ungraduated) atom carries `silm:isProvisional true`; no ungraduated atom counted conformant-green | an ungraduated atom asserted green with no provisional flag |

SHACL mirrors: `aob:ProgenitorSplitShape`, `aob:AtomValueShape`, `aob:OctetDescentShape`,
`aob:SopCarrierShape`, `aob:UpperAnchorShape`, `aob:GroupLawShape`, `aob:TensorByteOrderShape`,
`aob:GlossarySeamShape`, `aob:SealHonestyShape` — each a `sh:sparql`/`sh:in` constraint
(**defang-proof** against range-inference, per SP1's lesson: never a bare `sh:class` where an
`rdfs:range` would make it vacuous). `aob:UpperAnchorShape` checks cardinality 1..1 AND that the IRI
matches the **referenced** anchor pattern (the pattern lives in `universal_anchors`, not the shape).

---

## 5. Interfaces

### Consumes

**From SP1 (committed floor):**
- the **colimit-taiji `prim:Primitive`** (`formalFacet`/`physicalFacet`/`gluedBy`) — the atom's VALUE
  IS one of these;
- the **realization monad ρ** (`realizesAs`/`encoding`/`frameOutput`/`frameEffect`/`interpretAs`) — the
  grounding = a Frame; `prim:Effect` extended with the byte/hash-provenance effect;
- the **physical carrier ladder + `prim:byteDescendsTo`** (`prim:Bit`/`prim:Octet`/`prim:ByteVector`,
  `prim:ordinalMin/Max`, cardinality 256) + the **`byte_order` agnostic progenitor** — the
  subatomic-to-octet descent and the tensor `byte_order` grounding;
- the **Identifier URN tower** (`prim:URN ⊃ URI ⊃ IRI`, `prim:QName`) — every `*_urn` coordinate and
  the CCO/CPO CURIE bridge;
- the **RDF-term tower** (`prim:Triple`) — the S/O/P `yoneda_hom_leg` carrier;
- the **Aggregate/Tensor tower** (`prim:Tensor`/`prim:Vector`) — the three-axis tensor block;
- the **Binary/Hash tower** (`prim:Blob`/`prim:Hash`) — the `source_sha256` identity + z-seed.

**From the Helios WIP AOB (lifted, not invented — Directive 1):** the `_aob_*` envelope + `avd_tree`
observation contract (`helios/srcy/.../specs/atoms/`); the per-paper `entity.{…}` + `triad_render`
envelope, 22 `type_node` families, `PaperSection` cocone, `CircuitImprintTensor`, Synonym/Antonym
simultaneity, `CheeseTrapImmunity` (`helios/papers_00_data_src_specs/`); the 2-family
`concrete_anchor`/`yoneda_hom_leg` seed + three-axis tensor block + `source_sha256`
(`helios/01_data_src_specs/products/`, `helios/00_src_specs/types/`); the 11-anchor CCO/BFO upper law
(`helios/01_data_src_specs/universal_anchors.spec.yaml`).

**From lower sub-projects:** only SP1 (`phase_w2_sp2` ordinal 2; SP1 `completed`; SP1 README lists
AOB #2 as its first consumer). The DAG carries no explicit *phase-level* `dependsOn` edges — see Q1.

### Produces (named, for higher sub-projects)

- **SP3 (S/O/P CRS):** the `aob:YonedaHomLeg` S/O/P carrier + the **z-coordinate seed** (`prim:Uint16`
  of the first two `prim:Octet`s of `source_sha256`, via `octet_descent.ttl`) — exactly the seed SP1's
  README names for #3.
- **SP4 (projection packet):** the `aob:AOBAtom` + tensor block + the `rendered_legs:[sh,ex,atlas.csv,
  ttl,shacl.ttl,sparql,linkml.yaml]` emitter seam (the 7-leg / 3-fibre fibration); the grounding-Frame
  **effects** seed the 5 loss classes.
- **SP5 (file+format taxonomy):** the sealed group as a `prim:Container` carrier + the per-format
  emitter coordinates as the format axis; `fs_*`/`text_*` leaf datatypes.
- **SP6 (glossary polysemy):** the Synonym+Antonym simultaneity seam + the glossary-scoped predicate +
  the OSSIE-mime anchor hook — the mole-of-glossaries *mechanism* is SP6's to build.
- **SP7 (SHACL law):** the AOB group-law + upper-anchor shapes + the `pattern_anchor_urn` (no-inline)
  discipline.
- **SP8 (basicttl depth remediation):** every basicttl `*_atom.ttl` (`synonym_atom`, `antonym_atom`,
  `preferred_term_atom`, `shape_atom`, …) and untyped stub becomes an `aob:AOBAtom` grounded here.
- **SP9 (render seal):** the sealed-group colimit + the group-law **inverse (retract)** = the per-atom
  instance of the split↔consolidated reversibility.

---

## 6. Non-goals (this iteration; YAGNI deferrals)

- **No live-corpus binding** (W5). No new corpuses (2 more gippidy / sparky / agent / BLS incoming).
  Pure shape + one lifted witness atom for non-vacuity.
- **The mole-of-glossaries MECHANISM is SP6** — SP2 declares the synonym-AND-antonym seam and the
  OSSIE-mime hook only; it does not resolve collisions or encapsulate epistemologies.
- **The full projection algebra is SP4** — SP2 declares the 7-leg emitter seam, not the projections,
  fibre-coherence laws, or the 5 loss classes.
- **The CRS geometry is SP3** — SP2 emits the S/O/P carrier + the z-seed, not the CRS towers.
- **No second presheaf category re-materialised** at the AOB level — the ologs-of-ologs turtle is the
  `aob:aobValue` edge into SP1's already-Yoneda-closed primitives.
- **No sealing/graduation runtime** — SP2 models the seal *state* + honest-gap discipline; the gate
  pipeline that graduates a staged atom is a later render/CI concern. `content_sha256`-at-graduation is
  an honest-gap coordinate, not computed.
- **The telephone twin** is a declared seam only, PROVISIONAL per Directive 6 (Q5).
- Built to be **challenged and relaunched**, not final (Directive 13).

---

## Open questions for the maintainer (Praeriehund — flagged, not invented)

1. **Phase-level dependency edges.** The DAG has no `silm:dependsOn` between W2 *phases* (only between
   *workflows*). SP2⟸SP1 is currently carried by ordinal + the SP1 README consumer list. Add explicit
   `phase_w2_sp2 silm:dependsOn phase_w2_sp1` edges (and the rest of the SP chain), or keep ordinal +
   consumer-list as the intended contract?
2. **CCO/BFO anchor resolution scope.** `universal_anchors` resolves node/arrow IRIs against
   `MergedAllCoreOntology.ttl` under `SIL_CCO_TTL_DIR`/`SIL_CPO_TTL_FILE` (a corpus-locked host path).
   For the corpus-agnostic v1 I model `aob:ccoGroundingIri`/`aob:cpoProcessIri` as **load-bearing
   card-1..1 + pattern-via-anchor** but leave the *external TTL resolution* (does `cco:ont00000958`
   actually resolve?) as a deferred W5 gate. Confirm the pattern+cardinality tooth (not live external
   resolution) is the right v1 scope.
3. **`type_node` family taxonomy depth.** The papers facet has **22** `type_node` families; the wave8
   type system has **25**. SP2's meta-TBox models the *envelope* + the 2-family progenitor split, and
   treats the 22/25 families as instances of `type_node` (an open enum), not as 22 hardwired
   `owl:Class`es. Is the open-enum lift correct, or should each family be its own first-class subclass
   this iteration?
4. **`avd_tree` observation contract fidelity.** The `_aob_*` `avd_tree` (SPACE/A_RANGE/DEPTH/E2E/
   SOURCE→SINK/SMOOTHNESS/UNIT-TEST) is rich (the rule-of-three evidence matrix). I lift it as a single
   `aob:ObservationContract` coordinate with the sub-facets as properties, not the full 30-slot matrix.
   Is the compressed lift acceptable for v1, or must the full matrix be modelled?
5. **Telephone twin.** Directive 6's `telephone_events`⟷`telephone_supervision_tree` twin (fields
   pinned to Layer-0 anchors via `tensor_space_urn`) is located in `01_data_src_specs`. Carry the
   telephone-twin seam here as a named provisional coordinate, or leave it entirely to a later
   sub-project?
6. **CCO resolution-artifact name (PIN-AT-WRITING-PLANS — do not resolve here).** `universal_anchors`
   resolves `cco_grounding` to `cco-merged/cco.ttl` (`SIL_CCO_TTL_DIR`) while these designs cite
   `MergedAllCoreOntology.ttl` (`SIL_CCO_TTL_FILE`) — pin the canonical artifact at plan time.
