# W2 · SP2 AOB meta-ontology — implementation plan (design → buildable, test-first)

> Turns the APPROVED, Helios-grounded design
> `docs/superpowers/specs/2026-08-08-w2-sp2-aob-meta-ontology-design.md` into a
> `superpowers:writing-plans` plan a subagent-driven build can execute straight through. Governing
> docs every agent reads IN FULL first: that design; `docs/unary-byte-frame-law.md`;
> `docs/praeriehund-demokratie-der-kategorien.md`; `ledger/W2/design_constraints.md` (Directives 1–16,
> esp. **15 Helios intake**, **16 polysemy**); `JUNGLE_MAP.md`; `STRICTNESS_RULES.md`; the committed SP1
> floor `basicttl/primitives/{formal,physical,realization,taiji}.ttl` +
> `primitives.{shapes.ttl,queries.sparql}` + `checks/run-floor-checks.sh` + `README.md`; and the
> Helios source-of-truth (git-ignored `helios/`, mapped in `ledger/W2/helios/*.md`). SP2 **LIFTS** the
> real WIP AOB (Directive 1: lift, do not invent). This is **THIS ITERATION's v1** — corpus-agnostic
> (Directive 13), built to be re-run and relaunched, never for permanence; zero live-corpus binding
> (that is W5). Subagents NEVER run state-changing git.

---

## MAINTAINER DECISIONS (surface at the top; each has a recommended default so the build proceeds unblocked)

These are SP2's genuine open decisions (design §6 open-questions, Directive 15/16). Each is flagged
Präriehund-honestly with a **recommended default**; the build uses the default unless the maintainer
overrides here at plan time. None is a dodge — each is a real fork with a defensible v1 answer.

| # | Decision | Options | **Recommended default (used unless overridden)** |
|---|----------|---------|--------------------------------------------------|
| **MD1** | **Phase-level DAG dependency edges.** The rebuild DAG carries `silm:dependsOn` only between *workflows*, never between *phases* (`basicttl/dag/dag_instances.ttl:141` lists `wf_w2 silm:hasPhase phase_w2_sp1..sp9`; `dag_ontology.ttl` scopes `dependsOn`/`hasOrdinal` to Workflows). SP2⟸SP1 is currently carried by `silm:hasOrdinal 2` + the SP1 README consumer list. | (a) add explicit `phase_w2_sp2 silm:dependsOn phase_w2_sp1` edges (and the rest of the SP chain); (b) keep ordinal + consumer-list as the intended contract. | **(b) keep ordinal + consumer-list.** `dependsOn` is defined and SHACL-shaped as a *workflow*-granular law; minting phase-level edges would widen the DAG ontology (an SP-outside change) for no new schedule information — the ordinal already totally orders the nine phases and the SP1 README already names AOB #2 as its first consumer. SP2 authors NO DAG edit except the completion flip in Task 12. If the maintainer wants phase-granular dependency provenance, that is a DAG-ontology change owned by a later pass, not smuggled into SP2. |
| **MD2** | **Canonical CCO resolution artifact (PIN-AT-WRITING-PLANS — design Q6).** `universal_anchors.spec.yaml` resolves `cco_grounding_iri` with `resolves_in_env: SIL_CCO_TTL_DIR`, `resolution_artifact: cco-merged/cco.ttl`; `project_env.spec.yaml` (the env source-of-truth) and these designs cite `SIL_CCO_TTL_FILE = …/CommonCoreOntologies/src/MergedAllCoreOntology.ttl`, `SIL_CCO_VERSION "2.x"`. Two spellings of "the merged CCO TTL". | (a) `cco-merged/cco.ttl` via `SIL_CCO_TTL_DIR`; (b) `MergedAllCoreOntology.ttl` via `SIL_CCO_TTL_FILE`. | **(b) `MergedAllCoreOntology.ttl` via `SIL_CCO_TTL_FILE` (CCO 2.x, under BFO).** `project_env.spec.yaml` is the declared env source-of-truth (61 `SIL_*` vars) and both cited designs use it; `cco-merged/cco.ttl` is recorded as an **honest divergence** in `upper_anchor.ttl`'s comment and the README, to be reconciled when the two Helios specs are merged into submodules. The pin is a *string constant* SP2 carries as `aob:resolvesInEnv "SIL_CCO_TTL_FILE"` + `aob:resolutionArtifact "MergedAllCoreOntology.ttl"` — **not** a live resolution (see MD6). |
| **MD3** | **`type_node` family taxonomy depth (design Q3).** The papers facet has **22** `type_node` families; the wave8 type system has **~25**. | (a) model the *envelope* + the 2-family `top_kind` progenitor split and treat the 22/25 families as instances of an OPEN enum `aob:typeNode`; (b) hardwire each family as its own first-class `owl:Class` this iteration. | **(a) open-enum lift.** The meta-TBox fixes what an atom **is** (envelope + node/arrow progenitor split); the 22/25 families are *instances* the corpus supplies (`aob:typeNode` a lifted string coordinate onto the Helios `type_urn` tower), not 22 hardwired classes. This is corpus-agnostic (Directive 13) and relaunch-safe: a family that appears/disappears at the W5 relaunch is a datum, not a schema change. Hardwiring 22 classes would bake this iteration's corpus into the shape — the exact permanence the maintainer forbids. |
| **MD4** | **`avd_tree` observation-contract fidelity (design Q4).** The `_aob_*` `avd_tree` is a rich rule-of-three evidence matrix (`0_SPACE`/`A_RANGE{min,max,step,distribution}`/`DEPTH.integer_value`/`E2E`/`SOURCE`/`SINK.points_at`/`SMOOTHNESS`/`INSTRUCTION-AWARENESS`/`UNIT-TEST-GENERATION.test_cases[]`). | (a) lift as a single `aob:ObservationContract` coordinate with the sub-facets as properties; (b) model the full ~30-slot matrix as first-class atoms this iteration. | **(a) compressed single `aob:ObservationContract`** with the eight sub-facets as properties (`aob:obsSpace`, `aob:obsARange`, `aob:obsDepth`, `aob:obsE2E`, `aob:obsSource`, `aob:obsSink`, `aob:obsSmoothness`, `aob:obsUnitTest`). The meta-TBox needs the *contract shape* (that every atom carries an observation/evidence witness), not the full instance matrix — the full 30-slot expansion is a corpus-instance concern (SP8/W5). The witness atom carries one populated contract so the tooth is non-vacuous. |
| **MD5** | **Telephone-twin ownership (design Q5, Directive 6).** The `telephone_events` ⟷ `telephone_supervision_tree` twin (each field pinned to a Layer-0 anchor via `tensor_space_urn` = Yoneda-point tightness) lives in `01_data_src_specs`. | (a) carry the telephone-twin seam here as a named PROVISIONAL coordinate; (b) leave it entirely to a later sub-project. | **(a) PROVISIONAL seam declared here.** Directive 6 asks the byte/substrate ⟷ telephone "twin mention" be realized at Yoneda tightness; SP2 declares the seam (`aob:TelephoneSeam`, `aob:tensorSpaceUrn` field→Layer-0-anchor pinning, `aob:telephoneTwinUrn`) and marks it `silm:isProvisional true` with the recommended default that the *mechanism* (gossip/supervision render) is a later sub-project. Declaring the seam now prevents the "bites us in the ass if we forgo it" risk (Directive 2) without over-building; leaving it out entirely would drop a maintainer-named coordinate. |
| **MD6** | **Live external CCO TTL resolution scope (design Q2).** Should v1 actually resolve `cco:ont00000958` against `MergedAllCoreOntology.ttl`? | (a) v1 tooth = cardinality-1..1 + pattern-via-anchor only; live external TTL resolution deferred to a re-runnable W5 gate; (b) resolve live now. | **(a) pattern + cardinality tooth is v1 scope; live resolution deferred to W5.** The corpus-agnostic floor cannot depend on a corpus-locked host path (`SIL_CCO_TTL_DIR`/`SIL_CCO_TTL_FILE` point at `/home/tristan/…`). SP2's `aob:UpperAnchorShape` enforces card-1..1 + the IRI matches the **referenced** `universal_anchors` pattern (never inline regex); `aob:resolvesInEnv`/`aob:resolutionArtifact` are carried as an honest governance note (a *deferred* gate), not a runtime. New anchors stay `human_review_required, never_auto_merge`. |

---

## Global Constraints (apply to every task)

- **Namespace.** `aob: <urn:silmaril:aob:#>` (full-lexical URN idiom, unary law), grounding onto
  `prim: <urn:silmaril:prim:#>` (the SP1 floor) and `silm: <urn:silmaril:entity#>` (for
  `silm:isProvisional`). External spellings (`sha256`, `cco:`, `cceo:`, `SHACL`, `UTF-8`, `BFO`) survive
  **only** as immutable bridge evidence on the external side of a registered bridge (STRICTNESS Rule 3 /
  unary-law full-lexical-identity amendment); they never become internal namespaces, field names, or
  dispatch shortcuts.
- **Depth gate (≥200-char `rdfs:comment`).** Every `owl:Class` and every non-trivial minted individual
  (`aob:AOBAtom` witnesses, `aob:SealedGroup`, `aob:HashDigest`, `aob:TensorBlock`,
  `aob:ObservationContract`, `aob:CircuitImprintTensor`, the byte-order progenitor + children) carries a
  ≥200-char `rdfs:comment` of **real** content (what it lifts from Helios + how it grounds into SP1 + the
  typed effect), never filler. **Depth gate runs FIRST** (SP1 gate discipline): no ASK is counted until
  every `owl:Class` clears the bar. Reuse `scripts/ontology-depth-check.py basicttl/aob`.
- **Teeth proven by probe injection**, not by absence of violations on the happy path. Every SHACL shape
  is proven to bite (`conforms=True → False`) and every EXPECT-TRUE ASK to flip (`True → False`) under a
  targeted injection; every positive ASK returns **false on an empty graph** (non-vacuous). This is SP1's
  exact RED→GREEN discipline (`basicttl/primitives/README.md` Verification block).
- **Corpus-agnostic v1 (Directive 13).** Pure shape + **exactly one lifted witness atom** (one
  `aob:ConcreteAnchor` node + one `aob:YonedaHomLeg` arrow) authored purely to keep the ASK suite
  non-vacuous, mirroring SP1's litmus discipline. Zero `gippidy`/`sparky`/BLS live-corpus data; no
  sha256-literal over real bytes (the witness digest is a fixed illustrative 32-octet vector).
- **One file per concern (STRICTNESS Rule 14; SP1's split).** Categorical grounding lands in the data
  TTLs; teeth in the shapes/query files. No concern collapsed into another file.
- **Praeriehund honesty.** Genuinely-undecidable items are `silm:isProvisional true` with the recommended
  default recorded in the comment — never a dodge, never a force-fit. A staged (ungraduated) atom is
  `silm:isProvisional`, never counted conformant-green. The `CheeseTrapImmunity` "don't collapse the
  category" discipline is a first-class atom, lifted not paraphrased.
- **LIFT Helios, do not invent (Directive 1 / 15).** Every `aob:*` term traces to a Helios structure:
  the `_aob_*` envelope (`helios/srcy/appendices/39_appendix_e_research_source_mirror/.../specs/atoms/`),
  the 2-family `concrete_anchor`/`yoneda_hom_leg` seed + three-axis tensor block
  (`helios/01_data_src_specs/products/`, `helios/00_src_specs/types/silmaril_wave8/`), the 11-anchor
  CCO/BFO law (`helios/01_data_src_specs/universal_anchors.spec.yaml`), the `byte_order` agnostic
  progenitor (`types.prelude.byte_order_{little,big,host,none}`), the Synonym(col 10)/Antonym(col 17)
  simultaneity, and the telephone twin. No AOB shape is invented where Helios authored one.
- **The word "colimit" is the LOCAL glossary sense (Directive 16 polysemy).** In SP2 "colimit" denotes
  the **local / per-primitive glossary** sense — the finite companion-cocone whose **universal property is
  provable** — so the word is **earned by a tooth** (`q_colimit_universal`, mirroring SP1's per-primitive
  taiji universality ASK), **never a bare assertion**. SP2 references "colimit" **through the SP6 glossary
  layer** (`aob:colimitGlossaryScope` → the LOCAL-sense seam), never bare. The CORPUS/artifact sense of
  the same lexeme (`ObservedProjection(ColimCandidate(D))`) is SP9's; SP6 holds both glossary-scoped senses
  of the one lexeme simultaneously. SP2 and SP9 are the two glossary poles of the same word.

---

## Interfaces

### Consumes

**From SP1 (committed, green floor — exact vocabulary):**
- the **colimit-taiji `prim:Primitive`** with `prim:formalFacet` / `prim:physicalFacet` / `prim:gluedBy` —
  the atom's VALUE **is** one of these (`aob:aobValue → prim:Primitive`);
- the **realization monad ρ** (`prim:Realization`, `prim:realizesAs` / `prim:realizesFrom` /
  `prim:encoding` / `prim:interpretAs` / `prim:frameOutput` / `prim:frameEffect`) and its typed
  `prim:Effect` family — the grounding-claim is a Frame; SP2 **selects an existing SP1 realization/effect**
  and authors **no** new `prim:Realization` or `prim:Effect` (keeping SP1's `RealizationShape` `sh:in`
  intact; a dedicated byte/hash-provenance effect, if ever needed, is an SP1-floor change, flagged);
- the **physical carrier ladder + `prim:byteDescendsTo`** (`prim:Bit`, `prim:Nibble`, `prim:Octet`,
  `prim:ByteVector`, `prim:CompositeCarrier`; `prim:ordinalMin`/`prim:ordinalMax`; octet ordinal 0..255,
  cardinality 256) — the subatomic-to-octet descent of the `source_sha256` identity;
- the **`prim:PhysicalEncoding`** family (`prim:bitWidth`, `prim:byteWidth`, `prim:byteOrder`,
  `prim:interpretAs`) + the **`prim:ByteOrder`** individuals (`prim:LE`, `prim:BE`, `prim:EndianNeutral`) —
  the three-axis tensor block's `space.bit_width`/`byte_width` and `time.byte_order` ground here;
- the **Identifier URN tower** (`prim:URN ⊃ prim:URI ⊃ prim:IRI`, `prim:QName`, `prim:BlankNode`) — every
  `*_urn` envelope coordinate and the `cco:`/`cceo:` CURIE bridge;
- the **RDF-term tower** (`prim:Triple`) — the S/O/P `yoneda_hom_leg` carrier;
- the **Aggregate/Tensor tower** (`prim:Tensor`, `prim:Vector`) — the three-axis tensor block;
- the **Binary/Hash tower** (`prim:Blob`, `prim:Hash`) + the **`prim:Uint16`** encoding — the
  `source_sha256` identity and the **z-coordinate seed** (uint16 of the first two digest octets) for SP3.

**From the Helios WIP AOB (lifted, not invented — Directive 1):** the `_aob_*` envelope + `avd_tree`
observation contract; the per-paper `entity.{urn,display_name,layer,kind_urn,type_node,type_urn,grounding,
version,ancestry[{axis,via}],citations}` + `triad_render`; the 22 `type_node` families (open enum, MD3);
the `PaperSection.companion_atoms[]` cocone; the 4 lock-step `addl_*` projections; `CircuitImprintTensor`
(witness-not-inferred); Synonym(col 10)/Antonym(col 17) simultaneity; `CheeseTrapImmunity`; the 2-family
`concrete_anchor`(node)/`yoneda_hom_leg`(arrow) seed + three-axis tensor block + `source_sha256`; the
11-anchor `universal_anchors` CCO/BFO law + `byte_order` progenitor; the telephone twin.

**From lower sub-projects:** only SP1 (`phase_w2_sp2` ordinal 2; SP1 `completed`; SP1 README lists AOB #2
as its first consumer). No explicit phase-level `dependsOn` edge — MD1.

### Produces (named, for the higher sub-projects that consume SP2)

- **SP3 (S/O/P CRS):** the `aob:YonedaHomLeg` **S/O/P carrier** (`aob:sourceNodeUrn`=S,
  `aob:targetNodeUrn`=O, `aob:cpoProcessIri`=P) + the **z-coordinate seed** (`aob:zSeed`, a `prim:Uint16`
  of the first two `prim:Octet`s of the `source_sha256`, via `octet_descent.ttl`) — exactly the seed SP1's
  README names for #3.
- **SP4 (projection packet):** the `aob:AOBAtom` + `aob:TensorBlock` + the `rendered_legs:[sh,ex,atlas.csv,
  ttl,shacl.ttl,sparql,linkml.yaml]` emitter seam (7-leg / 3-fibre fibration); the grounding-Frame effects
  seed the 5 loss classes.
- **SP5 (file+format taxonomy):** the sealed group as a container carrier + the per-format emitter
  coordinates as the format axis.
- **SP6 (glossary polysemy):** the **Synonym+Antonym simultaneity seam** (`aob:heldAsSynonym` +
  `aob:heldAsAntonym`, `aob:glossaryScope`) + the glossary-scoped `aob:colimitGlossaryScope` predicate +
  the OSSIE-mime anchor hook (`aob:ossieMimeAnchor`) — the mole-of-glossaries **mechanism** is SP6's.
- **SP7 (SHACL law):** the AOB group-law + upper-anchor shapes + the `aob:patternAnchorUrn` (no-inline)
  discipline.
- **SP8 (basicttl depth remediation):** every basicttl `*_atom.ttl` and untyped stub becomes an
  `aob:AOBAtom` grounded here.
- **SP9 (render seal):** the sealed-group colimit + the group-law **inverse (`aob:retracts`)** = the
  per-atom instance of the split↔consolidated reversibility.

---

## File map (one file per concern, under `basicttl/aob/`; SP1's data/teeth split)

| file | responsibility | task |
|------|----------------|------|
| `aob/meta.ttl` | the meta-TBox: `aob:AOBAtom` + the `top_kind` progenitor split `aob:ConcreteAnchor`(node) / `aob:YonedaHomLeg`(arrow); the `_aob_*` envelope coordinates (`aob:atomUrn`, `aob:displayName`, `aob:layer`, `aob:kindUrn`, `aob:typeNode`, `aob:typeUrn`, `aob:grounding`, `aob:version` semver, `aob:hasAncestry[{axis,via}]`, `aob:citation`); `aob:atomFamilyUrn`; the arrow's S/O/P carrier (`aob:sourceNodeUrn`/`aob:targetNodeUrn`/`aob:cpoProcessIri`); the ONE lifted witness atom | T1, T2 |
| `aob/upper_anchor.ttl` | the CCO/BFO law: `aob:ccoGroundingIri` (node, card 1..1) / `aob:cpoProcessIri` (arrow, card 1..1) as `aob:patternAnchorUrn` references into `universal_anchors` (no inline regex); `aob:resolvesInEnv` / `aob:resolutionArtifact` bridge (MD2) | T3 |
| `aob/octet_descent.ttl` | subatomic-to-octet: `aob:HashDigest` (`source_sha256`) as a `prim:ByteVector` of 32 `prim:Octet`s (each ordinal 0..255) that `prim:byteDescendsTo+ prim:Bit`; grounds atom identity; exposes the **z-seed** (`aob:zSeed`, `prim:Uint16` of the first two octets) for SP3 | T4 |
| `aob/tensor_block.ttl` | the three-axis tensor block (`space`/`time`/`value`) grounded into SP1 physical carriers; `aob:ByteOrderProgenitor` + children (`aob:byteOrderNone`/`Little`/`Big`/`Host`) lifted from Helios and bridged to `prim:ByteOrder`; the `physicalFacet` for `aobValue`; the `value.interpret_as` bridge | T5, T6 |
| `aob/value_colimit.ttl` | the gluing: `aob:aobValue : AOBAtom → prim:Primitive`; the grounding-claim Frame (`aob:groundingClaim`, effect = a lifted member of SP1's `prim:Effect`); the ologs-of-ologs meta-layer assertion (AOB olog objects ARE SP1 taiji atoms) | T7 |
| `aob/group_law.ttl` | the sealed-group colimit: `aob:groupIdentity` (base atom), `aob:composesOnto` (associative companion cocone), `aob:retracts` (inverse); `aob:colimitApex` + the `q_colimit_universal` LOCAL-sense universal-property witness (`aob:universalFactor`, `aob:colimitGlossaryScope`); the `aob:graduationTarget` staged↔gated seal state + `silm:isProvisional` honesty | T8, T9 |
| `aob/evidence_glossary.ttl` | the `avd_tree` `aob:ObservationContract` (compressed, MD4); `aob:CircuitImprintTensor` witness-not-inferred bound to SP1's Frame; the Synonym+Antonym simultaneity **seam** (glossary-scoped; OSSIE-mime hook) → SP6; the **telephone seam** PROVISIONAL (MD5) | T10, T11 |
| `aob/aob.shapes.ttl` | SHACL law — one `sh:NodeShape` per invariant, each `sh:sparql`/`sh:in`/`sh:hasValue` (defang-proof, never a bare `sh:class` an `rdfs:range` makes vacuous), each proven to bite | T1–T11 |
| `aob/aob.queries.sparql` | the EXPECT-TRUE ASK suite, each with an inline DATA CONTRACT comment naming the exact triples that turn it green (auto-discovered by the runner on `# EXPECT-TRUE <name>` markers) | T1–T11 |
| `aob/checks/run-aob-checks.sh` + `aob/README.md` | the runner (parse 7 data TTLs + pyshacl against `aob.shapes.ttl` shapes-only + depth gate + every EXPECT-TRUE ASK) and the doc + consumer list + how-to-re-run | T1, T12 |

The runner loads the **seven data TTLs** (`meta`, `upper_anchor`, `octet_descent`, `tensor_block`,
`value_colimit`, `group_law`, `evidence_glossary`) into one graph and validates against `aob.shapes.ttl`
loaded **only** as the shapes graph (never mixed into the data), exactly as SP1's runner does.

### The acceptance suite (`aob/aob.queries.sparql`) — EXPECT-TRUE ASKs and their SHACL mirrors

| ASK (EXPECT-TRUE) | SHACL mirror | asserts | probe of record (must be CAUGHT) |
|---|---|---|---|
| `q_progenitor_split` | `aob:ProgenitorSplitShape` | every `aob:AOBAtom` is **exactly one** of `aob:ConcreteAnchor`(node)/`aob:YonedaHomLeg`(arrow), each with its own `aob:atomFamilyUrn`; nothing crammed | an atom typed as **both**, or **neither** |
| `q_sop_carrier` | `aob:SopCarrierShape` | every `aob:YonedaHomLeg` carries `aob:sourceNodeUrn`(S)/`aob:targetNodeUrn`(O)/`aob:cpoProcessIri`(P), each a URN-tower term | an arrow missing `aob:targetNodeUrn` |
| `q_cco_bfo_anchor` | `aob:UpperAnchorShape` | every node has **exactly one** `cco:ont########` and every arrow **exactly one** `cceo:` process, each via an `aob:patternAnchorUrn` reference (no inline regex) resolving in the pinned artifact (MD2) | a node with **two** CCO IRIs; an IRI failing the referenced pattern; an **inlined `sh:pattern` literal** |
| `q_octet_descent` | `aob:OctetDescentShape` | the `source_sha256` identity is a `prim:ByteVector` of **exactly 32** `prim:Octet`s (each ordinal 0..255) that `prim:byteDescendsTo+ prim:Bit`; the z-seed is a `prim:Uint16` of the first two | a **33-octet** digest; an octet with `prim:ordinalMax 256` |
| `q_tensor_byte_order` | `aob:TensorByteOrderShape` | every tensor block's `bit_width`/`byte_width` resolve to a SP1 `prim:PhysicalEncoding`, and `time.byte_order` is a lifted `aob:ByteOrderProgenitor` child bridged to a `prim:ByteOrder` individual | a `byte_order` not descended from the progenitor; a `bit_width` with no SP1 encoding |
| `q_interpret_as_bridge` | `aob:InterpretAsBridgeShape` | every tensor block's `value.interpret_as` bridges to the SP1 `prim:PhysicalEncoding` whose `prim:interpretAs` **equals** the atom's `formalFacet` (the yang↔yin bridge) | an `interpret_as` landing on an encoding whose `interpretAs` ≠ the atom's `formalFacet` |
| `q_aob_value_is_taiji` | `aob:AtomValueShape` | every atom has an `aob:aobValue` that **is** a `prim:Primitive` carrying `formalFacet`+`physicalFacet`+`gluedBy` (grounds into SP1) | a value lacking `prim:physicalFacet` |
| `q_group_law` | `aob:GroupLawShape` | the base atom is the `aob:groupIdentity`; every companion `aob:composesOnto` it (associative); a retract is the inverse of its companion | a companion composing onto a **non-identity**; a retract with no target |
| `q_colimit_universal` | `aob:ColimitUniversalShape` | the sealed-group **apex** (the atom) satisfies the LOCAL/per-primitive glossary universal property — every companion cocone factors through a **unique** `aob:universalFactor`, and the sense is `aob:colimitGlossaryScope`-scoped (never bare) | a group with **two** apexes / a companion with **no** `aob:universalFactor`; a "colimit" with **no** glossary scope |
| `q_synonym_antonym_dual` | `aob:GlossarySeamShape` | one term is held as `aob:heldAsSynonym` under glossary A **and** `aob:heldAsAntonym` under glossary B **simultaneously**, no contradiction (distinct glossary epistemologies) | collapsing **both into one** `aob:glossaryScope` (forces a contradiction) |
| `q_seal_honesty` | `aob:SealHonestyShape` | every staged (ungraduated) atom carries `silm:isProvisional true`; no ungraduated atom counted conformant-green | an ungraduated atom asserted green with **no** provisional flag |
| `q_telephone_seam` | `aob:TelephoneSeamShape` | the telephone twin is declared as a PROVISIONAL seam: `aob:TelephoneSeam` carries `aob:telephoneTwinUrn` + at least one field pinned to a Layer-0 anchor via `aob:tensorSpaceUrn`, and `silm:isProvisional true` (MD5) | a `aob:TelephoneSeam` with a field lacking its `aob:tensorSpaceUrn` pin; a seam missing the provisional flag |

All shapes use `sh:sparql`/`sh:in`/`sh:hasValue` (**defang-proof**, per SP1's lesson: never a bare
`sh:class` where an `rdfs:range` would make it vacuous under `inference="rdfs"`). `aob:UpperAnchorShape`
checks cardinality 1..1 AND that the IRI matches the **referenced** anchor pattern (the pattern lives in
`universal_anchors`, mirrored as a literal on the anchor node, **never** as an `sh:pattern` in the shape).

---

## Tasks (bite-sized, independently testable, test-first, in dependency order)

Every task is RED→GREEN: **(RED)** write the failing ASK/SHACL first and capture the red (empty/absent →
false); **(Do)** the minimal authoring to make it green; **(GREEN)** the runner passes the new tooth;
**(Probe of record)** the injection that must be CAUGHT (`conforms=True→False`, `ASK True→False`);
**(Review)** spec+quality+depth. Depth gate runs first each task. Subagents never run state-changing git.

### Task 1 — Harness + `meta.ttl` envelope & the `top_kind` progenitor split
**Files:** `aob/checks/run-aob-checks.sh`, `aob/aob.queries.sparql`, `aob/aob.shapes.ttl`, `aob/meta.ttl`,
`aob/README.md`
**RED:** author `run-aob-checks.sh` (below) + the full `aob.queries.sparql` skeleton (every EXPECT-TRUE
ASK block from the table present as `# EXPECT-TRUE <name>` + inline DATA CONTRACT comment + `PREFIX`/`ASK`,
with the not-yet-satisfiable conjuncts real). Run it: it exits non-zero — every positive ASK is **false**
on the empty/near-empty graph (proves non-vacuity), and `pyshacl` reports the missing shapes. Capture the
red.
**Do:**
1. `meta.ttl` namespace prologue (`aob:`/`prim:`/`silm:`/`owl:`/`rdf:`/`rdfs:`/`xsd:`).
2. `aob:AOBAtom a owl:Class` (the meta-TBox root) with the ≥200-char comment: *an AOB atom is a
   colimit-taiji `prim:Primitive`-valued unit lifted from the Helios `_aob_*` envelope; it is exactly one
   `top_kind` (node|arrow); nothing crammed.* Disjoint subclasses `aob:ConcreteAnchor` (node) and
   `aob:YonedaHomLeg` (arrow), each `rdfs:subClassOf aob:AOBAtom`, marked `owl:disjointWith` each other.
3. Envelope datatype/object properties (lifted from `_aob_entity_register.yaml`): `aob:atomUrn`,
   `aob:displayName`, `aob:layer`, `aob:kindUrn` (= `u:AtomicObject`/`kind_node_instance` bridge),
   `aob:typeNode` (open enum, MD3), `aob:typeUrn` (onto the Helios Linnaean tower), `aob:grounding`
   (≥1-sentence prose: what it asserts + the CPO/CCO process that licenses it), `aob:version` (semver
   string, e.g. `"0.1.0"`), `aob:hasAncestry` → blank node with `aob:ancestryAxis` + `aob:ancestryVia`,
   `aob:citation`, `aob:atomFamilyUrn` (`urn:silmaril:atom-family:{node:concrete_anchor|arrow:yoneda_hom_leg}`).
4. The **one lifted witness atom** pair (kept minimal, grown across later tasks): `aob:witnessAnchor a
   aob:ConcreteAnchor` (node; `aob:atomFamilyUrn urn:silmaril:atom-family:node:concrete_anchor`) and
   `aob:witnessLeg a aob:YonedaHomLeg` (arrow; `aob:atomFamilyUrn
   urn:silmaril:atom-family:arrow:yoneda_hom_leg`), each with the full envelope filled.
5. `aob.shapes.ttl` `aob:ProgenitorSplitShape` (`sh:sparql` targeting `aob:AOBAtom`): flags any atom that
   is **not exactly one** of the two families (both, or neither), or lacks `aob:atomFamilyUrn`.
**EXPECT-TRUE `q_progenitor_split`** (DATA CONTRACT: every `?a a aob:AOBAtom` has exactly one of
`aob:ConcreteAnchor`/`aob:YonedaHomLeg` and an `aob:atomFamilyUrn`):
`ASK { FILTER NOT EXISTS { ?a a aob:AOBAtom . FILTER NOT EXISTS { { ?a a aob:ConcreteAnchor } UNION { ?a a aob:YonedaHomLeg } } } FILTER NOT EXISTS { ?a a aob:ConcreteAnchor, aob:YonedaHomLeg } FILTER NOT EXISTS { ?a a aob:AOBAtom . FILTER NOT EXISTS { ?a aob:atomFamilyUrn ?f } } }`
**GREEN:** `run-aob-checks.sh` runs; `q_progenitor_split` PASS; depth gate passes for `meta.ttl`.
**Probe of record:** inject `aob:bad a aob:ConcreteAnchor, aob:YonedaHomLeg` (crammed both) →
`aob:ProgenitorSplitShape` `conforms=True→False`, `q_progenitor_split` `True→False`; and inject
`aob:bad2 a aob:AOBAtom` with no family class → same flip.
**Review:** the split is disjoint + total; the witness carries the full envelope; comments ≥200 chars; no
`top_kind` crammed.

The runner (author verbatim, mirroring `basicttl/primitives/checks/run-floor-checks.sh`):
```bash
#!/usr/bin/env bash
# run-aob-checks.sh — the AOB meta-ontology verification runner (W2 · SP2).
# Parses the 7 DATA TTLs (meta/upper_anchor/octet_descent/tensor_block/value_colimit/group_law/
# evidence_glossary) into one graph, runs pyshacl against aob.shapes.ttl (loaded ONLY as the shapes
# graph, never mixed into the data), auto-discovers every "# EXPECT-TRUE <name>" ASK in
# aob.queries.sparql and requires each true, then runs the depth gate. Exits 0 iff all green.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python3 - <<'PY'
import os.path, re, sys
from rdflib import Graph
from pyshacl import validate
DATA=["meta.ttl","upper_anchor.ttl","octet_descent.ttl","tensor_block.ttl","value_colimit.ttl","group_law.ttl","evidence_glossary.ttl"]
data=Graph()
for f in DATA:
    p=f"basicttl/aob/{f}"
    if os.path.exists(p): data.parse(p)
print(f"parse OK: {len([f for f in DATA if os.path.exists('basicttl/aob/'+f)])} data ttl, {len(data)} triples")
sp="basicttl/aob/aob.shapes.ttl"
if os.path.exists(sp):
    s=Graph(); s.parse(sp)
    ok,_,rep=validate(data, shacl_graph=s, inference="rdfs")
    print("SHACL conforms:", ok)
    if not ok: print(rep[:2000]); sys.exit(1)
else: print("SHACL: shapes file not present yet (skipped)")
q=open("basicttl/aob/aob.queries.sparql").read()
fails=ran=0
for b in re.split(r'\n(?=#\s*EXPECT-TRUE\s)', q):
    m=re.search(r'EXPECT-TRUE\s+(\S+)', b)
    if not m: continue
    ask="\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
    if not ask.strip().upper().startswith(("PREFIX","ASK")): continue
    res=bool(data.query(ask)); ran+=1
    print(f"  {'PASS' if res else 'FAIL'}  {m.group(1)}"); fails+=(0 if res else 1)
print(f"ASKs: {ran} run, {fails} failed")
sys.exit(1 if fails else 0)
PY
python3 scripts/ontology-depth-check.py basicttl/aob
echo "AOB CHECKS GREEN"
```

### Task 2 — `meta.ttl` S/O/P carrier on the arrow family
**Files:** `aob/meta.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** with the arrow witness carrying no S/O/P, `q_sop_carrier` returns **false**. Capture.
**Do:** mint `aob:sourceNodeUrn` (S), `aob:targetNodeUrn` (O), `aob:cpoProcessIri` (P) — lifted verbatim
from the `yoneda_hom_leg` seed (`helios/01_data_src_specs/products/…`: `source_node_urn`/`target_node_urn`/
`cpo_process_iri`). Each value is a URN-tower term (grounds into `prim:URN`/`prim:QName`; the arrow triple
is a `prim:Triple` S/O/P carrier). Fill `aob:witnessLeg` with all three. `aob:SopCarrierShape` (`sh:sparql`
targeting `aob:YonedaHomLeg`): flags any arrow missing any of the three, or whose value is not a URN-tower
literal/term.
**EXPECT-TRUE `q_sop_carrier`** (DATA CONTRACT: every `?l a aob:YonedaHomLeg` has `aob:sourceNodeUrn`,
`aob:targetNodeUrn`, `aob:cpoProcessIri`):
`ASK { FILTER NOT EXISTS { ?l a aob:YonedaHomLeg . FILTER NOT EXISTS { ?l aob:sourceNodeUrn ?s ; aob:targetNodeUrn ?o ; aob:cpoProcessIri ?p } } }`
**GREEN:** `q_sop_carrier` PASS.
**Probe of record:** delete `aob:witnessLeg aob:targetNodeUrn` → `aob:SopCarrierShape`
`conforms=True→False`, `q_sop_carrier` `True→False`.
**Review:** S=source, O=target, P=cpo — the design's literal S/O/P triple; SP3's seed carrier is intact.

### Task 3 — `upper_anchor.ttl` the load-bearing CCO/BFO upper anchor (pattern-by-anchor, never inline)
**Files:** `aob/upper_anchor.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_cco_bfo_anchor` false (no anchor grounding yet). Capture.
**Do:**
1. Lift the two load-bearing `universal_anchors` as **anchor nodes** (not inlined regex):
   `aob:anchor_cco_grounding_iri` (`aob:anchorPattern "^cco:ont[0-9]{8}$"`, `aob:resolvesInEnv
   "SIL_CCO_TTL_FILE"`, `aob:resolutionArtifact "MergedAllCoreOntology.ttl"` per **MD2**, with a comment
   recording the `cco-merged/cco.ttl` divergence) and `aob:anchor_cpo_process_iri` (`aob:anchorPattern
   "^cceo:[A-Za-z0-9_]+$"`, `aob:resolvesInEnv "SIL_CPO_TTL_FILE"`).
2. `aob:ccoGroundingIri` (node → its CCO IRI) and `aob:cpoProcessIri` (arrow → its CPO IRI, reused from
   T2's P), each carrying `aob:patternAnchorUrn` pointing at the matching anchor node (the reference, not
   a regex).
3. Fill the witness: `aob:witnessAnchor aob:ccoGroundingIri "cco:ont00000958" ; aob:patternAnchorUrn
   aob:anchor_cco_grounding_iri`; the arrow's `aob:cpoProcessIri` already carries
   `aob:patternAnchorUrn aob:anchor_cpo_process_iri`.
4. `aob:UpperAnchorShape` (`sh:sparql`): node atoms have **exactly one** `aob:ccoGroundingIri` (card 1..1)
   whose value matches the **referenced** anchor's `aob:anchorPattern` (read the pattern from the anchor
   node with SPARQL `REGEX`, **never** an `sh:pattern` literal in the shape); arrow atoms have exactly one
   `aob:cpoProcessIri` matching `aob:anchor_cpo_process_iri`'s pattern; every grounding carries an
   `aob:patternAnchorUrn`. New anchors bear a `human_review_required, never_auto_merge` governance comment
   (MD6), not a runtime.
**EXPECT-TRUE `q_cco_bfo_anchor`** (DATA CONTRACT: each node exactly one `cco:ont########` matching its
referenced anchor pattern; each arrow exactly one `cceo:` matching; each via `aob:patternAnchorUrn`; no
`sh:pattern` literal appears in `aob.shapes.ttl` for these — checked by the review, not the ASK):
`ASK { FILTER NOT EXISTS { ?n a aob:ConcreteAnchor . FILTER NOT EXISTS { ?n aob:ccoGroundingIri ?i ; aob:patternAnchorUrn ?anc . ?anc aob:anchorPattern ?pat . FILTER(REGEX(?i,?pat)) } } FILTER NOT EXISTS { ?n a aob:ConcreteAnchor ; aob:ccoGroundingIri ?i1, ?i2 . FILTER(?i1 != ?i2) } FILTER NOT EXISTS { ?l a aob:YonedaHomLeg . FILTER NOT EXISTS { ?l aob:cpoProcessIri ?p ; aob:patternAnchorUrn ?anc2 . ?anc2 aob:anchorPattern ?pat2 . FILTER(REGEX(?p,?pat2)) } } }`
**GREEN:** `q_cco_bfo_anchor` PASS.
**Probe of record (three):** (a) add a second `aob:witnessAnchor aob:ccoGroundingIri "cco:ont00000001"`
→ card-1..1 clause flips (`conforms=True→False`, `q_cco_bfo_anchor True→False`); (b) set the value to
`"cco:BOGUS"` (fails the referenced pattern) → flips; (c) a review probe: grep `aob.shapes.ttl` for any
`sh:pattern "…cco…"` / `"…cceo…"` literal — **must be zero** (pattern lives only on the anchor node).
**Review:** card 1..1 both sides; pattern-by-anchor reference, never inline; MD2 pin recorded; MD6 live
resolution deferred honestly.

### Task 4 — `octet_descent.ttl` sha256 identity, subatomic to the octet + the z-seed
**Files:** `aob/octet_descent.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_octet_descent` false. Capture.
**Do:**
1. `aob:HashDigest a owl:Class` (the `source_sha256` identity, the AtomCommon Avro identity Helios names
   but the papers facet lacks — the delta SP2 ADDs on lift; comment ≥200 chars). `aob:hasHashDigest :
   AOBAtom → HashDigest`. The digest is a `prim:ByteVector` (grounds into SP1's `prim:Blob`/`prim:Hash`
   tower) of **exactly 32** `prim:Octet`s (`aob:digestOctet`, each `prim:ordinalMin 0`/`prim:ordinalMax
   255`, `aob:octetPosition` 0..31), byte-descending via SP1's `prim:byteDescendsTo+` to `prim:Bit`.
2. `aob:zSeed` : HashDigest → a `prim:Uint16` (the SP1 encoding) = the uint16 of the first two octets
   (`aob:octetPosition 0`,`1`) — the exact seed SP1's README names for SP3.
3. Fill `aob:witnessAnchor aob:hasHashDigest` a fixed illustrative 32-octet digest (corpus-agnostic: not
   a real sha256 over live bytes) + its `aob:zSeed`.
4. `aob:OctetDescentShape` (`sh:sparql` targeting `aob:HashDigest`): exactly 32 `aob:digestOctet` (count
   check), each ordinal in 0..255, and `prim:byteDescendsTo+ prim:Bit` reachable; a `aob:zSeed` present and
   typed `prim:Uint16`.
**EXPECT-TRUE `q_octet_descent`** (DATA CONTRACT: `?d a aob:HashDigest` has exactly 32 `aob:digestOctet`,
each a `prim:Octet` ordinal 0..255, and the ByteVector `prim:byteDescendsTo+ prim:Bit`; `?d aob:zSeed ?z`,
`?z a prim:Uint16`):
`ASK { ?d a aob:HashDigest . { SELECT ?d (COUNT(?o) AS ?n) WHERE { ?d aob:digestOctet ?o } GROUP BY ?d } FILTER(?n = 32) FILTER NOT EXISTS { ?d aob:digestOctet ?ox . FILTER NOT EXISTS { ?ox a prim:Octet ; prim:ordinalMin 0 ; prim:ordinalMax 255 } } ?d aob:zSeed ?z . ?z a prim:Uint16 . prim:ByteVector prim:byteDescendsTo+ prim:Bit . }`
**GREEN:** `q_octet_descent` PASS.
**Probe of record:** add a 33rd `aob:digestOctet` (count 32→33) → `aob:OctetDescentShape`
`conforms=True→False`, `q_octet_descent True→False`; and inject an octet with `prim:ordinalMax 256` →
flips.
**Review:** the hash is not opaque (32 octets, byte-descended); the z-seed is a real `prim:Uint16`; the
digest is illustrative, not live-corpus.

### Task 5 — `tensor_block.ttl` the three-axis tensor block + the `byte_order` agnostic progenitor
**Files:** `aob/tensor_block.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_tensor_byte_order` false. Capture.
**Do:**
1. `aob:TensorBlock a owl:Class` (lifted verbatim from the wave8 `tensor:` block —
   `helios/00_src_specs/types/silmaril_wave8/yoneda_hom_leg.spec.yaml`). `aob:hasTensorBlock : AOBAtom →
   TensorBlock`. Axes as sub-facets: **space** (`aob:tsCardinality`, `aob:tsDimensions`, `aob:tsBounded`,
   `aob:tsMaxSize`, `aob:tsBitWidth`, `aob:tsByteWidth`, `aob:tsAlignment`); **time** (`aob:ttDynamics`,
   `aob:ttOrdering`, `aob:ttMonotonic`, `aob:ttLifetime`, `aob:ttByteOrder`, `aob:ttArithmetic`);
   **value** (`aob:tvInterpretAs`, `aob:tvDomainKind`, `aob:tvReadVia`, `aob:tvWriteVia`).
2. The **`byte_order` agnostic progenitor** lifted from Helios (`types.prelude.byte_order_{little,big,
   host,none}`): `aob:ByteOrderProgenitor a owl:Class` (the agnostic parent) with the four children
   `aob:byteOrderLittle`/`aob:byteOrderBig`/`aob:byteOrderHost`/`aob:byteOrderNone`. Each child
   `aob:groundsInByteOrder` a SP1 `prim:ByteOrder` individual: little→`prim:LE`, big→`prim:BE`,
   none→`prim:EndianNeutral`. **`aob:byteOrderHost` has no SP1 sibling** (host-endianness is
   runtime-resolved) — mark it `silm:isProvisional true` with the honest gap note (Präriehund; not a dodge).
3. `aob:tsBitWidth`/`aob:tsByteWidth` `aob:groundsInEncoding` a SP1 `prim:PhysicalEncoding` (whose
   `prim:bitWidth`/`prim:byteWidth` match). Fill `aob:witnessAnchor aob:hasTensorBlock` a block whose
   `aob:ttByteOrder aob:byteOrderNone` (UTF-8 prose atom, endian-neutral), `aob:tsBitWidth 8`,
   `aob:groundsInEncoding prim:Utf8`.
4. `aob:TensorByteOrderShape` (`sh:sparql` targeting `aob:TensorBlock`): `aob:ttByteOrder` must be an
   `aob:ByteOrderProgenitor` child that `aob:groundsInByteOrder` a `prim:ByteOrder`; `aob:tsBitWidth` must
   resolve to a `prim:PhysicalEncoding` carrying that `prim:bitWidth`.
**EXPECT-TRUE `q_tensor_byte_order`** (DATA CONTRACT: every `?t a aob:TensorBlock` has `aob:ttByteOrder`
one of the four progenitor children each bridged to a `prim:ByteOrder`, and `aob:tsBitWidth`/`groundsInEncoding`
to a `prim:PhysicalEncoding`):
`ASK { FILTER NOT EXISTS { ?t a aob:TensorBlock . FILTER NOT EXISTS { ?t aob:ttByteOrder ?bo . ?bo rdfs:subClassOf* aob:ByteOrderProgenitor . ?bo aob:groundsInByteOrder ?pbo . ?pbo a prim:ByteOrder } } FILTER NOT EXISTS { ?t a aob:TensorBlock ; aob:tsBitWidth ?bw ; aob:groundsInEncoding ?e . FILTER NOT EXISTS { ?e a prim:PhysicalEncoding ; prim:bitWidth ?bw } } }`
**GREEN:** `q_tensor_byte_order` PASS.
**Probe of record:** point `aob:witnessAnchor`'s block `aob:ttByteOrder` at a fresh node not descended
from `aob:ByteOrderProgenitor` → `aob:TensorByteOrderShape` `conforms=True→False`, `q_tensor_byte_order
True→False`; and set `aob:tsBitWidth 7` with `aob:groundsInEncoding prim:Utf8` (no 7-bit encoding) → flips.
**Review:** byte_order progenitor lifted (not invented); host gap honest-flagged; bit/byte widths ground
into real SP1 encodings.

### Task 6 — `tensor_block.ttl` the `value.interpret_as` bridge (yang↔yin)
**Files:** `aob/tensor_block.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_interpret_as_bridge` false. Capture.
**Do:** mint `aob:tvInterpretAs` (lifted from the tensor `value.interpret_as`, e.g.
`types.prelude.interpret_as_utf8`) → `aob:interpretBridge` a SP1 `prim:PhysicalEncoding` whose
`prim:interpretAs` **equals** the atom's eventual `formalFacet` (Task 7 supplies the facet; here the bridge
pins the encoding). For the UTF-8 witness: `aob:tvInterpretAs` bridges to `prim:Utf8`, whose
`prim:interpretAs` is `prim:Codepoint` — and the atom's `formalFacet` (Task 7) is the text/String tower,
so the bridge closes. `aob:InterpretAsBridgeShape` (`sh:sparql` targeting `aob:TensorBlock`): the
`aob:interpretBridge` encoding's `prim:interpretAs` must equal the owning atom's `aob:aobValue`'s
`prim:formalFacet` (read transitively `rdfs:subClassOf*` so a subtype text facet still bridges).
**EXPECT-TRUE `q_interpret_as_bridge`** (DATA CONTRACT: for every atom's tensor block, the
`aob:interpretBridge` encoding `prim:interpretAs` a formal type on the atom's `formalFacet` line):
`ASK { FILTER NOT EXISTS { ?a aob:hasTensorBlock ?t ; aob:aobValue ?v . ?v prim:formalFacet ?f . ?t aob:interpretBridge ?e . FILTER NOT EXISTS { ?e prim:interpretAs ?g . ?f rdfs:subClassOf* ?g } } }`
**GREEN:** `q_interpret_as_bridge` PASS (after Task 7 supplies `aob:aobValue`; order the runner so both
land together — this task authors the bridge, Task 7 the value, and the joint tooth goes green at Task 7).
**Probe of record:** point `aob:interpretBridge` at `prim:Int32` (interprets as `prim:Integer`, not the
text facet) → `aob:InterpretAsBridgeShape` `conforms=True→False`, `q_interpret_as_bridge True→False`.
**Review:** the value axis genuinely bridges the physical encoding to the atom's formal facet — the
tensor's yang held by the atom's yin.

### Task 7 — `value_colimit.ttl` the atom's VALUE is an SP1 colimit-taiji `prim:Primitive`
**Files:** `aob/value_colimit.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_aob_value_is_taiji` false. Capture.
**Do:**
1. `aob:aobValue : AOBAtom → prim:Primitive` (the meta-functor into the floor). Its value **is** an
   **existing** SP1 `prim:Primitive` (grep `taiji.ttl` for the primitive whose `prim:formalFacet` is the
   text/String tower, since AOB prose atoms are UTF-8) — SP2 authors **no** new `prim:Realization` or
   `prim:Effect` (keeps SP1's `RealizationShape` `sh:in` intact; Consumes note).
2. `aob:groundingClaim` (the observed grounding prose = the realization Frame's output=tensor encoding,
   effect = a lifted member of SP1's `prim:Effect` family, selected not minted). `aob:ologObjectIsTaiji
   true` on each atom — the ologs-of-ologs meta-assertion (Directive 2/6): the AOB olog object IS itself an
   SP1 colimit-taiji atom (whose gluing SP1 already closed as literal Yoneda), so `aob:aobValue` realizes
   the "turtles all the way" edge into SP1's already-Yoneda-closed primitives; SP2 does **not**
   re-materialise a second presheaf category (YAGNI, design §6).
3. Fill `aob:witnessAnchor aob:aobValue` the selected SP1 text primitive.
4. `aob:AtomValueShape` (`sh:sparql` targeting `aob:AOBAtom`): every atom's `aob:aobValue` is a node
   carrying `prim:formalFacet` (on the FormalType tower), `prim:physicalFacet` (a `prim:PhysicalEncoding`
   with `prim:bitWidth`), and `prim:gluedBy` (a `prim:Realization` with `prim:frameOutput`) — the
   defang-proof structural signature (never `sh:class prim:Primitive`).
**EXPECT-TRUE `q_aob_value_is_taiji`** (DATA CONTRACT: every `?a a aob:AOBAtom` has `aob:aobValue ?v` with
`prim:formalFacet`, `prim:physicalFacet`, `prim:gluedBy`):
`ASK { FILTER NOT EXISTS { ?a a aob:AOBAtom . FILTER NOT EXISTS { ?a aob:aobValue ?v . ?v prim:formalFacet ?f ; prim:physicalFacet ?pe ; prim:gluedBy ?g } } }`
**GREEN:** `q_aob_value_is_taiji` PASS; and Task 6's `q_interpret_as_bridge` now GREEN (value present).
**Probe of record:** point `aob:witnessAnchor aob:aobValue` at a node lacking `prim:physicalFacet` →
`aob:AtomValueShape` `conforms=True→False`, `q_aob_value_is_taiji True→False`.
**Review:** the value IS an SP1 taiji atom (not a copy); no new realization/effect minted; ologs-of-ologs
edge is a real edge into SP1, not a re-derived presheaf category.

### Task 8 — `group_law.ttl` the sealed-group colimit + the `q_colimit_universal` LOCAL-sense tooth
**Files:** `aob/group_law.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_group_law` and `q_colimit_universal` false. Capture both.
**Do:**
1. `aob:SealedGroup a owl:Class` (lifted from the `PaperSection` apex + `companion_atoms[]` cocone + the
   `_aob_*` `graduation_target` seal). The **base atom is the group identity**: `aob:groupIdentity :
   SealedGroup → AOBAtom`. Companions **compose onto it** (associative): `aob:composesOnto : AOBAtom →
   AOBAtom` (companion → base). **Retract = inverse**: `aob:retracts : AOBAtom → AOBAtom`
   (`Replacement`/`superseded` witness). `aob:companionAtom : SealedGroup → AOBAtom` (the cocone legs).
   The apex is ONE atom: `aob:colimitApex : SealedGroup → AOBAtom` (= the `aob:groupIdentity`).
2. The **universal-property tooth (LOCAL/per-primitive glossary sense, Directive 16)**: `aob:universalFactor
   : AOBAtom → AOBAtom` — every companion cocone factors through the apex via a **unique** mediating
   morphism (mirroring SP1's `q_colimit_universal`-style taiji universality). `aob:colimitGlossaryScope :
   SealedGroup → <the LOCAL-sense glossary URN>` — the word "colimit" is referenced **through the SP6
   glossary layer**, never bare (the seam SP6 consumes).
3. Fill the witness: `aob:witnessGroup a aob:SealedGroup ; aob:groupIdentity aob:witnessAnchor ;
   aob:colimitApex aob:witnessAnchor ; aob:companionAtom aob:witnessDescription, aob:witnessExample ;
   aob:colimitGlossaryScope <urn:silmaril:glossary:local:colimit>`; author `aob:witnessDescription a
   aob:ConcreteAnchor` (a `Description` companion) + `aob:witnessExample` (an `Example` companion), each
   `aob:composesOnto aob:witnessAnchor` and `aob:universalFactor aob:witnessAnchor`; author a
   `aob:witnessReplacement aob:retracts aob:witnessDescription` (the inverse).
4. `aob:GroupLawShape` (`sh:sparql` targeting `aob:SealedGroup`): the `aob:groupIdentity` = the
   `aob:colimitApex`; every `aob:companionAtom` `aob:composesOnto` the identity (not another companion);
   every `aob:retracts` has a target. `aob:ColimitUniversalShape` (`sh:sparql`): the apex is **unique**
   (exactly one `aob:colimitApex`), every companion has a **unique** `aob:universalFactor` onto the apex,
   and the group carries an `aob:colimitGlossaryScope` (no bare "colimit").
**EXPECT-TRUE `q_group_law`** (DATA CONTRACT: `?g a aob:SealedGroup` has `aob:groupIdentity ?b`; every
`aob:companionAtom` `aob:composesOnto ?b`; every `aob:retracts` has a target):
`ASK { FILTER NOT EXISTS { ?g a aob:SealedGroup ; aob:companionAtom ?c ; aob:groupIdentity ?b . FILTER NOT EXISTS { ?c aob:composesOnto ?b } } FILTER NOT EXISTS { ?r aob:retracts ?x . FILTER NOT EXISTS { ?x a aob:AOBAtom } } }`
**EXPECT-TRUE `q_colimit_universal`** (DATA CONTRACT: exactly one `aob:colimitApex`; every companion a
unique `aob:universalFactor` onto it; `aob:colimitGlossaryScope` present — the LOCAL glossary sense):
`ASK { FILTER NOT EXISTS { ?g a aob:SealedGroup . FILTER NOT EXISTS { ?g aob:colimitApex ?apex ; aob:colimitGlossaryScope ?scope } } FILTER NOT EXISTS { ?g a aob:SealedGroup ; aob:colimitApex ?a1, ?a2 . FILTER(?a1 != ?a2) } FILTER NOT EXISTS { ?g aob:companionAtom ?c ; aob:colimitApex ?apex . FILTER NOT EXISTS { ?c aob:universalFactor ?apex } } }`
**GREEN:** both PASS.
**Probe of record:** (a) rewire `aob:witnessExample aob:composesOnto aob:witnessDescription` (composing
onto a non-identity companion) → `aob:GroupLawShape` `conforms=True→False`, `q_group_law True→False`;
(b) add a second `aob:witnessGroup aob:colimitApex aob:witnessExample` → `aob:ColimitUniversalShape`
`conforms=True→False`, `q_colimit_universal True→False`; (c) delete `aob:colimitGlossaryScope` (bare
"colimit") → `q_colimit_universal True→False`.
**Review:** identity=base atom, associative compose, retract=inverse; the universal property is **earned
by a tooth**, referenced through SP6, never bare (Directive 16).

### Task 9 — `group_law.ttl` the `graduation_target` seal state + Präriehund seal honesty
**Files:** `aob/group_law.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_seal_honesty` false. Capture.
**Do:** `aob:graduationTarget : AOBAtom → <urn>` (lifted from `swe_as_dag_accounting.graduation_target`);
`aob:sealState : AOBAtom → {aob:staged | aob:gated}` (the staged↔gated discipline). A **staged
(ungraduated)** atom MUST carry `silm:isProvisional true` — never counted conformant-green (the honesty
spine). `content_sha256`-at-graduation is an honest-gap coordinate (`aob:contentShaAtGraduation`
`silm:isProvisional true`), **not** computed (design §6 non-goal). Add a staged witness
`aob:witnessStaged a aob:ConcreteAnchor ; aob:sealState aob:staged ; silm:isProvisional true` (kept as the
non-vacuity case) and keep `aob:witnessAnchor aob:sealState aob:gated`. `aob:SealHonestyShape` (`sh:sparql`
targeting `aob:AOBAtom`): any atom with `aob:sealState aob:staged` and no `silm:isProvisional true` is
flagged.
**EXPECT-TRUE `q_seal_honesty`** (DATA CONTRACT: no `aob:sealState aob:staged` atom lacks
`silm:isProvisional true`):
`ASK { FILTER NOT EXISTS { ?a aob:sealState aob:staged . FILTER NOT EXISTS { ?a silm:isProvisional true } } }`
**GREEN:** `q_seal_honesty` PASS.
**Probe of record:** remove `aob:witnessStaged silm:isProvisional true` (a staged atom asserted green) →
`aob:SealHonestyShape` `conforms=True→False`, `q_seal_honesty True→False`.
**Review:** staged→provisional is enforced; the graduation runtime is NOT built (design non-goal); the
content-sha gap is honest, not computed.

### Task 10 — `evidence_glossary.ttl` the `avd_tree` observation contract + `CircuitImprintTensor` + the Synonym/Antonym simultaneity seam
**Files:** `aob/evidence_glossary.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_synonym_antonym_dual` false. Capture.
**Do:**
1. `aob:ObservationContract a owl:Class` (the `avd_tree`, compressed per **MD4**): `aob:hasObservationContract
   : AOBAtom → ObservationContract`, sub-facets `aob:obsSpace`, `aob:obsARange` (blank node
   `{min,max,step,distribution}`), `aob:obsDepth` (integer), `aob:obsE2E`, `aob:obsSource`, `aob:obsSink`
   (`points_at` urn), `aob:obsSmoothness`, `aob:obsUnitTest` (list of test-case slugs). Fill the witness
   with one populated contract (non-vacuity).
2. `aob:CircuitImprintTensor a owl:Class` — **witness, not inference** (lifted discipline verbatim): binds
   `aob:activeCircuitUrn` support into SP1's Frame (`aob:nativeFrameUrn` → the `prim:Frame` Yoneda point),
   with `aob:witnessReadback`; **inferred adjacency/relations are rejected** (a `aob:cheeseTrapGuard`
   comment). Also mint `aob:CheeseTrapImmunity` (`aob:failureMode` + `aob:immunityMechanism`) — the
   "don't collapse the category" discipline as a first-class atom (lifted, not paraphrased).
3. The **Synonym+Antonym simultaneity seam** (the mole-of-glossaries seam declared here; mechanism is SP6):
   `aob:heldAsSynonym` (CPO `SemanticComparing`, Atlas col 10) and `aob:heldAsAntonym` (CPO
   `IsomorphicComparing`, Atlas col 17), each carrying an `aob:glossaryScope` (glossary A vs glossary B),
   plus the `aob:ossieMimeAnchor` hook. Author a term held **simultaneously**:
   `aob:witnessTerm aob:heldAsSynonym [ aob:glossaryScope aob:glossaryA ] ; aob:heldAsAntonym [
   aob:glossaryScope aob:glossaryB ]` — synonym under A AND antonym under B, no contradiction (distinct
   glossary epistemologies).
4. `aob:GlossarySeamShape` (`sh:sparql`): a term is flagged only if it is held as **both** synonym and
   antonym **under the same** `aob:glossaryScope` (the collapse that forces a contradiction) — distinct
   scopes are lawful and required.
**EXPECT-TRUE `q_synonym_antonym_dual`** (DATA CONTRACT: some term has `aob:heldAsSynonym` under glossary A
AND `aob:heldAsAntonym` under glossary B, `A != B`; no term holds both under one scope):
`ASK { ?t aob:heldAsSynonym ?sa ; aob:heldAsAntonym ?an . ?sa aob:glossaryScope ?ga . ?an aob:glossaryScope ?gb . FILTER(?ga != ?gb) FILTER NOT EXISTS { ?x aob:heldAsSynonym ?s1 ; aob:heldAsAntonym ?a1 . ?s1 aob:glossaryScope ?g . ?a1 aob:glossaryScope ?g } }`
**GREEN:** `q_synonym_antonym_dual` PASS.
**Probe of record:** collapse the witness term's antonym scope to `aob:glossaryA` (both senses in one
glossary) → `aob:GlossarySeamShape` `conforms=True→False`, `q_synonym_antonym_dual True→False`.
**Review:** the seam is declared (not resolved — mechanism is SP6); synonym+antonym simultaneity is real
across distinct glossary epistemologies; CircuitImprintTensor binds to SP1's Frame, never infers adjacency.

### Task 11 — `evidence_glossary.ttl` the telephone twin seam (PROVISIONAL, MD5)
**Files:** `aob/evidence_glossary.ttl`, `aob/aob.shapes.ttl`, `aob/aob.queries.sparql`
**RED:** `q_telephone_seam` false. Capture.
**Do:** `aob:TelephoneSeam a owl:Class` (the `telephone_events` ⟷ `telephone_supervision_tree` twin,
lifted from `helios/01_data_src_specs/telephone_*`). `aob:telephoneTwinUrn` (the paired twin URN);
`aob:tensorSpaceUrn` (each seam field pinned to a Layer-0 `universal_anchors` anchor = the Yoneda-point
tightness Directive 6 asks for). The whole seam is `silm:isProvisional true` — SP2 declares the seam only;
the gossip/supervision **mechanism** is a later sub-project (MD5 recommended default). Author
`aob:witnessTelephone a aob:TelephoneSeam ; aob:telephoneTwinUrn <…supervision_tree> ; aob:tensorSpaceUrn
<urn:silmaril:universal-anchor:node:enum:milestone> ; silm:isProvisional true`. `aob:TelephoneSeamShape`
(`sh:sparql`): a `aob:TelephoneSeam` must carry `aob:telephoneTwinUrn`, at least one `aob:tensorSpaceUrn`
pin, and `silm:isProvisional true`.
**EXPECT-TRUE `q_telephone_seam`** (DATA CONTRACT: `?s a aob:TelephoneSeam` has `aob:telephoneTwinUrn`,
`aob:tensorSpaceUrn`, and `silm:isProvisional true`):
`ASK { FILTER NOT EXISTS { ?s a aob:TelephoneSeam . FILTER NOT EXISTS { ?s aob:telephoneTwinUrn ?tw ; aob:tensorSpaceUrn ?ts ; silm:isProvisional true } } ?any a aob:TelephoneSeam . }`
**GREEN:** `q_telephone_seam` PASS.
**Probe of record:** remove `aob:witnessTelephone silm:isProvisional true` (seam asserted non-provisional)
→ `aob:TelephoneSeamShape` `conforms=True→False`, `q_telephone_seam True→False`; and remove the
`aob:tensorSpaceUrn` pin (no Yoneda-point tightness) → flips.
**Review:** the seam is declared at Yoneda tightness (field→anchor pin) and honestly PROVISIONAL; the
mechanism is not over-built.

### Task 12 — Integration + teeth proof + README + DAG completion flip
**Files:** `aob/README.md`, `basicttl/dag/dag_instances.ttl`
**Do:** run `run-aob-checks.sh` fresh (parse 7 data TTLs · pyshacl conforms · depth gate · all 12
EXPECT-TRUE ASKs). Run the depth gate standalone (`scripts/ontology-depth-check.py basicttl/aob`). Re-run
**every** probe of record from Tasks 1–11 and show each is CAUGHT (`conforms=True→False`, `ASK
True→False`); confirm no ASK is vacuous (every positive ASK false on an empty graph; every `FILTER NOT
EXISTS` universal flips under its injection). Author `aob/README.md` (the meta-ontology, its Consumes/
Produces, the 12-ASK / 12-shape suite, the MAINTAINER DECISIONS defaults taken, the how-to-re-run, the
green run captured verbatim). Flip `silm:phase_w2_sp2 silm:hasStatus "completed"` in
`basicttl/dag/dag_instances.ttl` **only** with the green evidence inline in the report (mirroring the SP1
flip; MD1 = no phase-level `dependsOn` edge added). Confirm the DAG re-parses and re-conforms after the flip.
**Review (spec + quality + depth):** all 12 teeth bite, none vacuous; no overclaim; no PROVISIONAL-dodge
introduced by the expansion (host-endianness gap, telephone seam, content-sha-at-graduation are the only
`silm:isProvisional` nodes, each with a documented gap); every `owl:Class` ≥200-char comment; SP2 authored
no new SP1 realization/effect and no inline anchor regex.

## Re-audit — adversarial triple panel (must return CLEAN before commit)
Three adversaries (completeness / honesty / doctrine), each spawning two ontology-grounded
sub-subagents that re-verify on disk. They must specifically re-check: (a) the `top_kind` split is
disjoint+total and nothing crammed; (b) each node exactly one `cco:ont########` and each arrow exactly one
`cceo:` via a **referenced** anchor pattern with **zero** inline `sh:pattern` regex; (c) the sha256 is 32
octets byte-descending to `prim:Bit` and the z-seed is a real `prim:Uint16`; (d) the tensor block grounds
into real SP1 encodings + the lifted `byte_order` progenitor (host gap honest-flagged); (e) the
`interpret_as` bridge closes yang→yin; (f) `aob:aobValue` is a genuine SP1 taiji `prim:Primitive` and SP2
minted no new realization/effect; (g) the sealed-group law (identity/compose/retract) holds AND the
`q_colimit_universal` universal property is earned + glossary-scoped (never bare, Directive 16); (h) staged
atoms are `silm:isProvisional`; (i) the synonym+antonym simultaneity holds across distinct glossaries and
collapses under one; (j) the telephone seam is Yoneda-pinned + PROVISIONAL; (k) no new overclaim or
PROVISIONAL-dodge. Any surviving Critical/Important → another fix round before commit.
