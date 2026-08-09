# `basicttl/aob/` — the AOB meta-ontology floor (W2 · SP2)

The corpus-agnostic **meta-TBox** that fixes, with teeth, exactly what an **AOB atom is**, by
**LIFTING** the real WIP AOB authored in the Helios library (Directive 1: lift, do not invent). This
is **this iteration's v1** — corpus-agnostic (Directive 13), built to be re-run and relaunched, never
for permanence. It grounds onto the committed, green SP1 primitive floor (`basicttl/primitives/`).

**Status: COMPLETED 2026-08-08; HARDENED 2026-08-08.** `basicttl/aob/checks/run-aob-checks.sh` exits 0
(parse · pyshacl conforms · 13/13 EXPECT-TRUE ASKs · depth gate); the full probe battery re-runs 28/28
CAUGHT at integration (the 12 original teeth spot-checked plus the four hardened teeth of the
decorative-teeth remediation below); `silm:phase_w2_sp2 silm:hasStatus "completed"` is recorded in
`basicttl/dag/dag_instances.ttl` with the green evidence inline. The SP1 floor is untouched and green.

**Decorative-teeth hardening (enrich-not-strip, Directive 16).** Four teeth that asserted more than they
enforced were made to genuinely bite (no prose weakened — the teeth were enriched to honor the prose):
(1) **`q_colimit_universal` / `aob:ColimitUniversalShape`** now models a genuine finite-colimit universal
property — a competing `aob:TestCocone` with a compatible `aob:CoconeLeg` from each companion and a
`aob:MediatingMorphism` `u : apex → vertex` — enforced by EXISTENCE, UNIQUENESS (at most one mediating
map per test cocone) and FACTORING (the triangle `u . iota_c = f_c` commutes), rather than a bare
`aob:universalFactor` edge identical to `aob:composesOnto`. (2) The **group-law inverse** (`aob:retracts`)
is now a genuine inverse (a self-retract, or a retract of an atom that composed onto no base, fails) and
**associativity** is enforced by the new `q_group_associativity` / `aob:GroupAssociativityShape` over a
reified `aob:Composition` table. (3) **Seal honesty** now closes the gated lane: a `aob:gated` atom must
carry graduation evidence (`aob:graduationTarget` + `aob:contentShaAtGraduation`), not only the staged
lane. (4) **Cardinality guards** on `aob:aobValue` and `aob:ttByteOrder` (design-single-valued, plus
universal well-formedness) stop a malformed sibling hiding behind a conforming value.

Namespace: `aob: <urn:silmaril:aob:#>` (full-lexical URN idiom, unary law), grounding onto
`prim: <urn:silmaril:prim:#>` (the SP1 floor) and `silm: <urn:silmaril:entity#>` (for
`silm:isProvisional`). External spellings (`sha256`, `cco:`, `cceo:`, `SHACL`, `UTF-8`, `BFO`) survive
only as immutable bridge evidence on the external side of a registered bridge (STRICTNESS Rule 3).

## What an AOB atom IS (the seven teeth of the meta-TBox)

1. **A two-family `top_kind` progenitor split** — `aob:ConcreteAnchor` (node) / `aob:YonedaHomLeg`
   (arrow), disjoint subclasses of `aob:AOBAtom`, each with its own `aob:atomFamilyUrn`; nothing
   crammed. The arrow carries the **S/O/P** carrier (`aob:sourceNodeUrn`=S, `aob:targetNodeUrn`=O,
   `aob:cpoProcessIri`=P) — the seed SP3 lifts into the CRS.
2. **A sealed group = a colimit** — the base atom is the group **identity**; companions
   **compose onto it** (`aob:composesOnto`, with associativity enforced by `q_group_associativity` over
   a reified `aob:Composition` table); **retract is a genuine inverse** (`aob:retracts` — a self-retract
   or a retract that inverts no composition fails); the apex is ONE atom (`aob:colimitApex`). "colimit"
   here is the **LOCAL / per-primitive glossary sense** (Directive 16), earned by the
   `q_colimit_universal` tooth — a genuine universal property over a competing `aob:TestCocone` with a
   **unique** factoring `aob:MediatingMorphism` (existence + uniqueness + factoring), not a bare
   `aob:universalFactor` edge — and referenced through the SP6 glossary layer
   (`aob:colimitGlossaryScope`), **never bare**.
3. **Its VALUE is an SP1 colimit-taiji `prim:Primitive`** — `aob:aobValue : AOBAtom → prim:Primitive`,
   a node carrying `prim:formalFacet` + `prim:physicalFacet` + `prim:gluedBy`. SP2 **selects** an
   existing SP1 primitive and authors **no** new `prim:Realization` / `prim:Effect`.
4. **Subatomic to the octet** — identity is a `source_sha256` `aob:HashDigest`, a `prim:ByteVector` of
   **exactly 32** `prim:Octet`s (each ordinal 0..255) that `prim:byteDescendsTo+ prim:Bit`; the first
   two octets are the `aob:zSeed` (`prim:Uint16`) SP3 consumes.
5. **The three-axis tensor block** (`space`/`time`/`value`) grounds into SP1 physical carriers; the
   `time.byte_order` grounds into the lifted **`aob:ByteOrderProgenitor`** (little/big/host/none)
   bridged to `prim:ByteOrder`; `value.interpret_as` bridges to the SP1 `prim:PhysicalEncoding` whose
   `prim:interpretAs` covers the atom's formal facet (yang↔yin).
6. **A load-bearing CCO/BFO upper anchor** — every node carries **exactly one** `cco:ont########`,
   every arrow **exactly one** `cceo:` process, each via a **`aob:patternAnchorUrn` reference** into the
   lifted `universal_anchors` (pattern-by-anchor, **never** inline regex).
7. **The `avd_tree` observation contract**, `CircuitImprintTensor` (witness-not-inference), the
   **Synonym+Antonym simultaneity seam** (one term held as synonym under glossary A AND antonym under
   glossary B, no contradiction), and the **PROVISIONAL telephone seam** (Yoneda-pinned).

## What SP2 lifts (source-of-truth: the git-ignored `helios/`, mapped in `ledger/W2/helios/*.md`)

- The **two-family `top_kind` progenitor split** — `concrete_anchor.spec.yaml` (`top_kind: node`) /
  `yoneda_hom_leg.spec.yaml` (`top_kind: arrow`) under `helios/00_src_specs/types/silmaril_wave8/`.
- The **atom envelope** — `entity.{urn, display_name, layer, kind_urn, type_node, type_urn, grounding,
  version, ancestry:[{axis,via}], citations}` from the per-paper register
  (`helios/papers_00_data_src_specs/`) and the `_aob_*` register (`kind: u:AtomicObject`).
- The **2-family seed + three-axis tensor block + `source_sha256`**
  (`helios/01_data_src_specs/products/`, `helios/00_src_specs/types/silmaril_wave8/`).
- The **11-anchor CCO/BFO upper law** (`helios/01_data_src_specs/universal_anchors.spec.yaml`) and the
  **`byte_order` agnostic progenitor** (`types.prelude.byte_order_{little,big,host,none}`).
- The **`avd_tree`** observation matrix, `CircuitImprintTensor`, Synonym(col 10)/Antonym(col 17)
  simultaneity, `CheeseTrapImmunity`, and the **telephone twin**
  (`helios/01_data_src_specs/telephone_{events,supervision_tree}.spec.yaml`).

## Files (one file per concern; SP1's data/teeth split)

| file | responsibility | tasks |
|------|----------------|-------|
| `meta.ttl` | `aob:AOBAtom` + the progenitor split `aob:ConcreteAnchor`/`aob:YonedaHomLeg`; the envelope coordinates; the arrow's S/O/P carrier; the one lifted witness pair (`aob:witnessAnchor` + `aob:witnessLeg`) | T1, T2 |
| `upper_anchor.ttl` | the CCO/BFO law: `aob:ccoGroundingIri` (node, 1..1) / `aob:cpoProcessIri` (arrow, 1..1) as `aob:patternAnchorUrn` references; `aob:resolvesInEnv` / `aob:resolutionArtifact` bridge (MD2) | T3 |
| `octet_descent.ttl` | `aob:HashDigest` (`source_sha256`) = 32 `prim:Octet`s byte-descending to `prim:Bit`; the `aob:zSeed` (`prim:Uint16`) for SP3 | T4 |
| `tensor_block.ttl` | the three-axis tensor block into SP1 carriers; `aob:ByteOrderProgenitor` + children bridged to `prim:ByteOrder`; the `value.interpret_as` bridge (yang↔yin) | T5, T6 |
| `value_colimit.ttl` | `aob:aobValue : AOBAtom → prim:Primitive`; the grounding-claim Frame; the ologs-of-ologs meta-layer assertion | T7 |
| `group_law.ttl` | the sealed-group colimit (`aob:groupIdentity` / `aob:composesOnto` / `aob:retracts` / `aob:colimitApex`); the `q_colimit_universal` LOCAL-sense tooth with a genuine `aob:TestCocone` + unique factoring `aob:MediatingMorphism`; the reified `aob:Composition` associativity table; the `graduation_target` seal state + seal honesty (staged + gated lanes) | T8, T9 |
| `evidence_glossary.ttl` | the `avd_tree` `aob:ObservationContract` (compressed, MD4); `aob:CircuitImprintTensor` + `aob:CheeseTrapImmunity`; the Synonym+Antonym seam → SP6; the telephone seam PROVISIONAL (MD5) | T10, T11 |
| `aob.shapes.ttl` | the SHACL law — one `sh:NodeShape` per invariant, each `sh:sparql`/`sh:in`/`sh:hasValue` (defang-proof), each proven to bite | T1–T11 |
| `aob.queries.sparql` | the EXPECT-TRUE ASK suite, each with an inline DATA CONTRACT + PROBE OF RECORD comment, auto-discovered on `# EXPECT-TRUE <name>` markers | T1–T11 |
| `checks/run-aob-checks.sh` | the runner: parse the 7 data TTLs into one graph, pyshacl against `aob.shapes.ttl` (shapes-only, `inference="rdfs"`), every EXPECT-TRUE ASK, then the depth gate | T1 |

## The acceptance suite — 13 EXPECT-TRUE ASKs and their SHACL mirrors

| ASK | SHACL mirror | asserts | probe of record (CAUGHT) |
|-----|--------------|---------|--------------------------|
| `q_progenitor_split` | `aob:ProgenitorSplitShape` | every atom is exactly one of node/arrow with its own `aob:atomFamilyUrn` | an atom typed as both, or neither |
| `q_sop_carrier` | `aob:SopCarrierShape` | every arrow carries S/O/P | an arrow missing `aob:targetNodeUrn` |
| `q_cco_bfo_anchor` | `aob:UpperAnchorShape` | node 1× `cco:ont########`, arrow 1× `cceo:`, via referenced pattern | two CCO IRIs; an IRI failing the pattern; (review) an inline `sh:pattern` |
| `q_octet_descent` | `aob:OctetDescentShape` | 32 octets (0..255) byte-descending to `prim:Bit`; `aob:zSeed` a `prim:Uint16` | a 33-octet digest; an octet `ordinalMax 256` |
| `q_tensor_byte_order` | `aob:TensorByteOrderShape` | `byte_order` a **single** progenitor child bridged to `prim:ByteOrder` (maxCount 1 + universal well-formedness); `bit_width` → SP1 encoding | a `byte_order` off the progenitor; a `bit_width` with no encoding; **a second rogue `aob:ttByteOrder`** |
| `q_interpret_as_bridge` | `aob:InterpretAsBridgeShape` | `value.interpret_as` bridges to the encoding covering the atom's `formalFacet` | an `interpret_as` landing off the formal facet |
| `q_aob_value_is_taiji` | `aob:AtomValueShape` | every atom's **single** `aob:aobValue` (maxCount 1 + universal well-formedness) is a taiji `prim:Primitive` (formal+physical+glued) | a value lacking `prim:physicalFacet`; **a second malformed `aob:aobValue`** beside a good one |
| `q_group_law` | `aob:GroupLawShape` | base = identity; companions compose onto it; retract is a **genuine inverse** (no self-retract; must invert a real composition) | a companion composing onto a non-identity; **a self-retract**; **a retract that inverts no composition** |
| `q_group_associativity` | `aob:GroupAssociativityShape` | the reified `aob:Composition` table is **associative**: `(a·b)·c == a·(b·c)` for every triple | a triple whose two bracketings disagree |
| `q_colimit_universal` | `aob:ColimitUniversalShape` | one apex; glossary-scoped; a competing `aob:TestCocone` has a **unique** factoring `aob:MediatingMorphism` (existence + uniqueness + factoring) | two apexes; a bare "colimit"; **no mediating morphism**; **a second mediating morphism**; **a non-factoring mediating target** |
| `q_seal_honesty` | `aob:SealHonestyShape` | every staged atom carries `silm:isProvisional true`; every **gated** atom carries graduation evidence (`aob:graduationTarget` + `aob:contentShaAtGraduation`) | a staged atom asserted green; **a gated atom with no graduation evidence** |
| `q_synonym_antonym_dual` | `aob:GlossarySeamShape` | one term synonym under A AND antonym under B, simultaneously | collapsing both senses into one scope |
| `q_telephone_seam` | `aob:TelephoneSeamShape` | the twin is a PROVISIONAL seam: twin URN + Yoneda pin + provisional flag | a seam missing its pin; a seam not provisional |

All shapes are **defang-proof** (`sh:sparql`/`sh:in`/`sh:hasValue`, never a bare `sh:class` an
`rdfs:range` would make vacuous under `inference="rdfs"`). `aob:UpperAnchorShape` reads the anchor
pattern from the referenced anchor node with SPARQL `REGEX` — the regex is **never** an `sh:pattern`
literal in the shape (grep for cco/cceo `sh:pattern` returns zero).

## MAINTAINER DECISIONS taken (recommended defaults, plan §MD1–MD6)

- **MD1** — keep the ordinal DAG. SP2⟸SP1 is carried by `silm:hasOrdinal 2` + the SP1 README consumer
  list; **no** phase-level `silm:dependsOn` edge minted (the completion flip is the only DAG edit).
- **MD2** — `MergedAllCoreOntology.ttl` via `SIL_CCO_TTL_FILE` (CCO 2.x, under BFO), carried as the
  string constants `aob:resolvesInEnv` / `aob:resolutionArtifact`. The `cco-merged/cco.ttl` spelling is
  recorded as an **honest divergence** on the anchor node's comment (to reconcile when the two Helios
  specs merge into submodules).
- **MD3** — open-enum `aob:typeNode`: the 22/25 `type_node` families are corpus **instances**, not 22/25
  hardwired `owl:Class`es (corpus-agnostic, relaunch-safe).
- **MD4** — compressed `aob:ObservationContract` (the `avd_tree` sub-facets as properties); the full
  30-slot matrix is an SP8/W5 instance concern.
- **MD5** — the telephone seam is **declared** at Yoneda tightness (field→Layer-0-anchor pins) and marked
  `silm:isProvisional true`; the gossip/supervision render mechanism is a later sub-project.
- **MD6** — the v1 tooth is card-1..1 + pattern-by-anchor; **live external TTL resolution** of
  `cco:ont########` against `MergedAllCoreOntology.ttl` is a **deferred, re-runnable W5 gate**.

## `silm:isProvisional` nodes (Präriehund honesty — genuinely-undecidable gaps, never a dodge)

Exactly **four** (verified on disk: `SELECT ?s WHERE { ?s silm:isProvisional true }` = 4) — the **three
genuinely-undecidable gaps** plus the **staged-atom honesty witness** that `aob:SealHonestyShape`'s
staged branch mandates carry the flag. Each is an honest Präriehund declaration, never a dodge:
- `aob:byteOrderHost` — host-endianness is runtime-resolved; it has no SP1 `prim:ByteOrder` sibling.
- `aob:witnessTelephone` — the telephone twin's render mechanism is a later sub-project (MD5).
- `aob:contentShaAtGraduation` — `content_sha256`-at-graduation is declared, **not** computed (design
  §6 non-goal: no sealing/graduation runtime this iteration).
- `aob:witnessStaged` — the staged (ungraduated) atom that inhabits the seal-honesty law non-vacuously;
  `aob:SealHonestyShape`'s staged branch **requires** any `aob:sealState aob:staged` atom to carry
  `silm:isProvisional true` (a staged atom is not conformant-green), so its flag is mandated evidence,
  not a dodge.

## Consumers (named, for the higher sub-projects)

- **SP3** — the `aob:YonedaHomLeg` S/O/P carrier + the `aob:zSeed` z-coordinate seed.
- **SP4** — the `aob:AOBAtom` + `aob:TensorBlock` + the 7-leg emitter seam; the grounding-Frame effects.
- **SP5** — the sealed group as a container carrier + the per-format emitter coordinates.
- **SP6** — the Synonym+Antonym simultaneity seam + the glossary-scoped `aob:colimitGlossaryScope`
  predicate + the `aob:ossieMimeAnchor` hook (the mole-of-glossaries **mechanism** is SP6's).
- **SP7** — the AOB group-law + upper-anchor shapes + the pattern-by-anchor (no-inline) discipline.
- **SP8** — every basicttl `*_atom.ttl` / untyped stub becomes an `aob:AOBAtom` grounded here.
- **SP9** — the sealed-group colimit + the group-law inverse (`aob:retracts`).

## Verification discipline (RED → GREEN, test-first; SP1's exact litmus)

- Every `owl:Class` carries a **≥200-char `rdfs:comment`** of real content (depth gate runs first:
  `scripts/ontology-depth-check.py basicttl/aob`).
- Every EXPECT-TRUE ASK is **non-vacuous** (returns false on an empty graph — 13/13 confirmed) and is
  proven to **flip `True→False`** under its probe of record; the SHACL mirror catches the same probe
  (`conforms=True→False`). Teeth are proven by **probe injection**, never by absence of violations.
- SP2 authored **no** new SP1 `prim:Realization` / `prim:Effect` and **no** inline anchor regex; the
  committed SP1 floor is untouched and green (`basicttl/primitives/checks/run-floor-checks.sh`, 21/21).

### Green run, captured verbatim from `basicttl/aob/checks/run-aob-checks.sh`

```
parse OK: 7 data ttl, 1071 triples
SHACL conforms: True
  PASS  q_progenitor_split
  PASS  q_sop_carrier
  PASS  q_cco_bfo_anchor
  PASS  q_octet_descent
  PASS  q_tensor_byte_order
  PASS  q_interpret_as_bridge
  PASS  q_aob_value_is_taiji
  PASS  q_group_law
  PASS  q_group_associativity
  PASS  q_colimit_universal
  PASS  q_seal_honesty
  PASS  q_synonym_antonym_dual
  PASS  q_telephone_seam
ASKs: 13 run, 0 failed
ONTOLOGY DEPTH CHECK PASSED
Files checked: 8
AOB CHECKS GREEN
```

### Integration teeth-proof (full probe battery, re-run at hardening)

28/28 probe injections CAUGHT — each flips **both** the SHACL mirror (`conforms=True→False`) **and** its
EXPECT-TRUE ASK (`True→False`).

Original 12 teeth (spot-checked): T1 crammed-both + neither-family; T2 arrow-missing-O; T3 two-CCO-IRIs +
`cco:BOGUS`; T4 33rd-octet + octet-`ordinalMax 256`; T5 `byte_order` off-progenitor + `bit_width 7`; T6
`interpretBridge`→`Int32`; T7 value lacking `physicalFacet`; T8 companion→non-identity; T10 syn+ant
collapsed into one scope; T11 seam-not-provisional + seam-missing-pin. Review probe T3c: inline
`sh:pattern` cco/cceo literals in `aob.shapes.ttl` = **0**.

Four hardened teeth (decorative-teeth remediation):
- **Defect 1 — `q_colimit_universal`:** two-apexes; bare-colimit (no glossary scope); **no** mediating
  morphism (existence); **second** mediating morphism (uniqueness); non-factoring `medTarget` (factoring).
- **Defect 2 — `q_group_law` / `q_group_associativity`:** self-retract; retract that inverts no
  composition; non-associative triple `(a·b)·c ≠ a·(b·c)`.
- **Defect 3 — `q_seal_honesty`:** staged atom asserted green; **gated** atom with no graduation evidence
  (both missing, and content-sha-only missing).
- **Defect 4 — `q_aob_value_is_taiji` / `q_tensor_byte_order`:** a second malformed `aob:aobValue` beside
  a good one; a second rogue `aob:ttByteOrder` beside `aob:byteOrderNone`.

## How to re-run

```bash
bash basicttl/aob/checks/run-aob-checks.sh    # parse + pyshacl + every EXPECT-TRUE ASK + depth gate; exit 0 iff green
```

Never run state-changing git from this floor. Author only under `basicttl/aob/` (plus, in Task 12
only, the `phase_w2_sp2` completion flip in `basicttl/dag/dag_instances.ttl`).
