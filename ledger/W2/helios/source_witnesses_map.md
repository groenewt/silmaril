# Helios facet map — `helios/01_src` (SOURCE WITNESSES)

> W2 lens map of the maintainer's source-of-truth **source witnesses**: the
> pre-formal evidence/provenance layer that the committed SP1 floor and the AOB
> meta-ontology (SP2) were re-derived from. Präriehund honesty on coverage is
> stated per subtree at the end. Do NOT commit `helios/` (maintainer resolves it
> into submodules). Zip facet: `helios/01_src`. Map written to
> `ledger/W2/helios/source_witnesses_map.md`.

## 0. What this facet IS (and is NOT)

`helios/01_src/` contains exactly one subtree: `source_witnesses/`. It is the
**witness / evidence / provenance corpus** — the human- and GPT-authored source
documents (the "cannon", the taxonomy witness, the GPT ontology drafts, and the
adversarial rebuttal) from which the executable SP1 primitive floor
(`basicttl/primitives/`) and the numbered categorical papers were later distilled.

It is NOT executable ontology (no `.ttl` classes, no SHACL shapes with teeth). It
is the **ground truth the formal layer must remain faithful to** — the "source
leg into the cocone" (rebuttal), the "cannon" axioms (physics/observation/soul),
and the atom SCHEMA in its original YAML form (`cannon_bootstrap/`). Relative to
SP1: this is the informal progenitor; SP1 is the teeth-proven re-derivation.

## 1. Complete directory + file taxonomy (the tree IS the taxonomy)

47 files. Full tree, all files listed (nothing elided):

```
helios/01_src/
└── source_witnesses/
    ├── cannon_bootstrap/          # THE AOB SCHEMA, in original self-defining YAML
    │   ├── atomic_object.yaml     # u:AtomicObject — "the turtle that defines turtles" (338 L)
    │   ├── dimension.yaml         # u:Dimension — one axis of variation, itself an AOB
    │   ├── types.yaml             # primitive type AOBs: int/string/enum/bool/urn (5 docs)
    │   ├── value_space.yaml       # u:ValueSpace — "the wave function", V(A)=∏dᵢ
    │   ├── morphism.yaml          # u:Morphism — the arrow that is an AOB (2-morphisms)
    │   ├── example_matrix.yaml    # u:ExampleMatrix — the 30-slot 2×5×3 observation protocol
    │   └── testgen.yaml           # u:TestGen — the observation functor (AOB→TestSuite)
    ├── cannon_cheese/
    │   └── cheese.md              # Leary/Alpert essay: categories as weaponized control (the "why")
    ├── cannon_language/
    │   ├── free_category.md       # 5 target functors (F_fs/F_db/F_rdf/F_test/F_bash) contract
    │   ├── language_arts.md       # the 6 linguistic turtles ↔ category theory (492 L)
    │   └── reserved_words.md      # polysemy collision law + VAR_ prefix disambiguation
    ├── cannon_observation/
    │   ├── definition.md          # observation as reading; 6 turtles; DSL grammar
    │   ├── definition_category_theory.md  # 2nd axiom: Expected⊔Unexpected⊔Unknown⊔DarkMatter
    │   ├── observation_protocol.md # 3-state |ψ⟩; UNKNOWN 5-step alarm; why 3× minimum
    │   ├── yoneda.md              # Yoneda contract: obs IS Hom(-,Obs) sources + F(Obs) sinks
    │   └── queries.sparql         # Q1-Q5 over the observation graph (UNKNOWN/dark-matter/chain)
    ├── cannon_paradigm/           # the "Silmaril triple" contracts (F_math/F_lang/F_econ)
    │   ├── definition.md          # paradigm = phylum/alloy backbone; category 𝒫
    │   ├── associativity.md       # composing paradigm translations is associative
    │   ├── commutativity.md       # which paradigm translations commute
    │   ├── dependencies_and_dags.md # paradigm features as an acyclic DAG
    │   ├── identity.md            # every paradigm needs an identity translator
    │   └── yoneda.md              # a paradigm IS how all others map into it
    ├── cannon_physics/
    │   └── physics_axioms.md      # "The Space": 7 axioms, the interpretation chain (423 L)
    ├── cannon_runtime/
    │   ├── contract-envelope.sh   # PostToolUse envelope-conformance hook (self-compliant header)
    │   └── trust_policy.yml       # tier→capability map (3 ABSOLUTE / 2 DELEGATED / 1 UNKNOWN / 0 NIL)
    ├── cannon_soul/               # the "soul": neuron/Leary/Yggdrasil worldview docs
    │   ├── ACID-TRIP-NEURON.md    # neuron as AOB; seasons=lifecycle (spring→winter)
    │   ├── INTERPRETATION-CHAIN.md # bits→presheaf, 10 layers, every arrow reversible
    │   ├── MASTER-ologs-contracts-templates.md  # THE canonical ref: olog/6 contracts/templates (530 L)
    │   ├── SESSION-CLOSE-acid-trip-neuron.md    # biological↔Forge neuron mapping, neurotransmitters
    │   └── YGGDRASIL-peace-love-zen.md          # rule-of-threes; 9 worlds=9 turtle layers
    ├── cannon_tax/                # the ITIS taxonomy WITNESS (Mittens type leg ground truth)
    │   ├── ITIS.sqbpro            # SQLiteStudio project file (query workspace)
    │   ├── ITIS.sqlite.witness.md # local witness: 875 MiB, SHA-256 recorded, NOT copied into src
    │   ├── ReadmeSqlite.txt       # upstream ITIS install instructions (provenance)
    │   └── tax_raw_snapshot.tsv   # RAW taxonomy rows preserved verbatim (Felis catus TSN 183798 + collisions)
    ├── cannon_templates/          # Jinja2 render templates (Yoneda card + yml atoms)
    │   ├── manifest.yml.j2        # per-(engine,db) manifest atom
    │   ├── ontology.yml.j2        # root ontology declaration atom
    │   └── yoneda_card.md.j2      # "actor IS the sum of morphisms pointing at it" identity card
    ├── gpt_ontology/              # GPT-authored LaTeX ontology papers (Yoneda + Avogadro/SIL/BIOS)
    │   ├── generated_90_abstract.tex             # abstract: object = governed position in a diagram
    │   ├── generated_90_texstyle.tex             # shared preamble/palette
    │   ├── generated_90_manifest_hom_profile.tex # manifest-as-hom-profile; SIL rules R1-R12; BIOS (3257 L)
    │   ├── generated_69_node_arrow_avogadro.tex  # 69-node/arrow cat of cats/taxa/CCO/Gremlin/SIL (5386 L)
    │   ├── generated_100_yoneda_governed_ontology.tex # 100-node Yoneda-governed ontology (2144 L)
    │   └── yoneda_generalized_ontology_graph_architecture.tex # the master GPT draft (4892 L)
    └── rebuttal_round00/          # adversarial "guide the Codex" rebuttal on the Mittens cocone
        ├── gippidy00.md          # Mittens taxonomic hierarchy witness; anti-collapse law (490 L)
        ├── gippidy01.md          # same, as a formal regression fixture + PathFelisCatus:[15]→CTax
        └── test.html            # standalone dark-theme HTML render of the free-monad corpus
```

## 2. The witness / evidence / provenance structure (the core of this facet)

### 2.1 The rule-of-three (3× / "quantum number of observation sufficiency")

The load-bearing evidence primitive. Appears identically across
`observation_protocol.md`, `definition_category_theory.md`, and the
`example_matrix.yaml` schema:

- **30-slot matrix** = 2 categories (`expected`, `unexpected`) × 5 facets
  (`needs`, `dislikes`, `wants`, `has`, `location`) × **3 datums** each.
- **Why 3**: 1 point = no distribution; 2 = a line, no curvature; **3 = a
  triangle (minimum polygon), detects curvature, estimates mean+variance+skew**.
  Framed as "quantum state tomography of a qubit — 3 measurements per basis".
- This is the minimum COMPLETE measurement of an atom's behaviour, and it is the
  evidence contract every atom must satisfy. `testgen.yaml` sets `slots_per_terminal`
  bounds `{min: 30}`; `example_matrix.yaml` sets `slots_per_facet` bounds `{min: 3}`.
- **The `location` facet is provenance**: each of its 3 datums carries a `zone`
  URN + a `type` URN (e.g. `kernel:zones#sysfs` / `location_types#leaf`) — i.e.
  every observation is stamped with WHERE in the deployment space it occurred.

### 2.2 Four observation states — evidence typed by what the physics can cover

`Ob(O) = Expected ⊔ Unexpected ⊔ Unknown ⊔ DarkMatter` (a coproduct decomposition).
This is the evidence-classification lattice:

- **Expected** — eigenstate, within declared bounds, matches a declared example → PASS.
- **Unexpected** — a KNOWN failure mode (declared error pattern) → handled FAIL.
- **UNKNOWN** — NO eigenstate; the physics has no basis vector → **ALARM**. The
  most important state: it means the value_space/example-matrix is INCOMPLETE.
  5-step protocol: immediate propagation (bypasses gossip) → **raw-bit
  preservation** (capture bytes before interpretation — "the raw bits are ground
  truth") → morphism quarantine → operator notification → schema evolution
  ("Big Bang", the physics grows). This is the maintainer's Präriehund honesty
  mechanism made operational: an unknown is named as unknown, its raw bytes
  preserved, and never force-fit into a bucket.
- **DarkMatter** — charted-but-unobserved: a morphism/dimension DECLARED but with
  zero traffic. Shapes topology without emitting evidence. "90% of a new Forge."

### 2.3 Claims + probes = the provenance/verification unit

Every bootstrap AOB carries a `claims:` block and `metrics.kernel_claims`:
```
claims:
  - type:     urn:...:claim_types#FileExists
    resource: urn:...:schema#AtomicObject   # what is claimed
    probe:    urn:...:probes#resolve_urn     # HOW to verify (the executable check)
```
A claim is not trusted; it is **probed**. The `MASTER` doc formalises this as the
**Claim Contract** (6 contract types): lifecycle `DECLARED → ACQUIRED → VERIFIED →
VIOLATED → RELEASED`, each transition verifiable by a probe command with no trust
required. The three-context model applies to contracts too: VERIFIED / VIOLATED /
UNKNOWN(→ALARM). This is the direct informal ancestor of SP2's atom-evidence
requirement and SP8's grounding.

### 2.4 `source_node` cocone / Mittens colimit (the rebuttal — provenance apex)

The `rebuttal_round00/` + `gpt_ontology/` witnesses carry the **cocone/colimit**
provenance model that SP1's colimit taiji re-derived. An individual (`Mittens`) is
`Mittens ≅ colim D_Mittens` where `D_Mittens` is a diagram of **separately typed
source legs**, each of which is a witness:
```
D_Mittens(type)        = TaxonNode(TSN=183798, "Felis catus")   ← source leg into the cocone
D_Mittens(taxon_path)  = TaxonHierarchyWitness(183798)          ← hierarchy_string, parsed to edges
D_Mittens(record)      = VetRecord77
D_Mittens(identifier)  = MicrochipIdentifier9
D_Mittens(quality/measurement/value/unit/role/process/shape) = …
D_Mittens(witness)     = SourceWitness
```
The **anti-collapse law** (the evidence-integrity core): a leg may NOT be replaced
by a cheaper string/record. `valid(Mittens → Felis catus / TSN 183798)`;
`invalid(Mittens → "catus")`; `invalid("catus" → DomesticCat)`. The `catus` epithet
recurs across 7 unrelated taxa (Aelurillus/Ameiurus/Coprococcus/Corycaeus/Hebrus/
Imogine/Felis) — **proof that a string is not an identity**; only the governed
`hierarchy_string` path is. Direction discipline is explicit: **assembly** reads
`TaxonHierarchyWitness → Mittens` (source leg IN), while **object-level** reads
`Mittens → hasTaxon → TaxonNode` (arrow OUT); the two must stay distinct.

### 2.5 Raw-custody rule (evidence provenance)

`cannon_tax/` embodies the custody discipline the rebuttal demands:
- `tax_raw_snapshot.tsv` preserves the ORIGINAL pasted columns verbatim —
  including duplicate/malformed headers (`TSN`/`tsn`, `Parent_TSN`/`Parent_tsn`,
  `currency_ratingphylo_sort_seq` merge defect). "Do not silently normalize the
  raw table; keep raw as witness, build normalized projections beside it."
- `ITIS.sqlite.witness.md` records the 875 MiB source by **SHA-256**
  (`b7a157231feb…be42d`) WITHOUT copying it into the buildable tree — a
  content-addressed provenance stub, mirroring the unary law's "content-addressed
  predecessor/successor account". `ReadmeSqlite.txt` retains the upstream origin.

### 2.6 Yoneda as the identity/provenance principle

Every witness family restates: **an object IS the totality of the morphisms
pointing at it** (`Nat(Hom(-,A),F) ≅ F(A)`). `yoneda_card.md.j2` renders it
literally: "each provider (pgp/ldap/kerberos/allura/direnv) contributes exactly
one arrow; the set of arrows IS the identity; missing an arrow means the actor is
not that thing — there is no silent default." This is the informal seed of SP1's
literal-Yoneda layer (representables, naturality squares, Frame = Yoneda point).

## 3. The atom (AOB) SCHEMA — captured faithfully from `cannon_bootstrap/`

The 7 YAML files are the ORIGINAL, self-defining atom schema (`u:AtomicObject`
"defines what an AOB IS; it is itself an AOB; turtles all the way down"). The
9-dimensional atom shape:

| field | meaning (from `atomic_object.yaml`) |
|---|---|
| `kind` | one categorical kind (`u:AtomicObject`); "kind IS the wave function" |
| `urn` | identity/address; pattern `^urn:silmaril:[a-z]+:[a-z]+#[a-zA-Z_]+`; unaddressable ⇒ does not exist |
| `version` | semver; fork changes it, commit pins it (VCS = wave-function collapse) |
| `identity` | name/domain/type/description; description must be ONE atomic sentence |
| `value_space` | product of `Dimension` AOBs; `V(A)=∏dᵢ`; cardinality finite/countable/continuous/**superposition** |
| `morphisms` | `incoming` (transport/PULL) + `outgoing` (functor/PUSH); `representable: true` = Yoneda-embeddable |
| `examples` | the 30-slot ExampleMatrix (the evidence) |
| `claims` | resource + probe (the provenance/verification) |
| `kernel_bind` | sysfs/proc/hex/asm/exec_model — physical grounding to hardware; `exec_model: superposition` until a profile collapses it |

Group-law / composability evidence present in the schema:
- **Identity**: `morphisms.outgoing` self-arrow with `functor: identity` (endomorphism
  `source=target`); `morphism.yaml` explicitly models the identity/fixed-point.
- **Compose**: `Morphism` has `composes_with → Morphism` via `functors#composition`
  (2-morphisms, "arrows between arrows, turtles"); the task **monoid** (`(M,⊕,ε)`,
  `monoid_algebra.md`) supplies associativity/identity/homomorphisms and Free-monoid
  → DAG generation.
- **Retract / decompose**: the interpretation chain (`INTERPRETATION-CHAIN.md`,
  `physics_axioms.md`) makes every arrow **reversible** — drill any layer DOWN to
  bits (presheaf → triple → Turtle bytes → RESP → syscall → register → BITS). Every
  concept is subatomically decomposable to the bit substrate ("Layer 0: The Bit").
- **Tensor block**: `language_arts.md` Turtle 5 — the 48-byte `ObservationEvent` is a
  **tensor product** `SequenceID ⊗ Timestamp ⊗ CategoryMask ⊗ SourcePID ⊗ Payload`,
  NOT a tuple ("a fused entity with its own morphisms"). Portmanteau ↔ `A⊗B` with its
  own Hom-set (Credentials = Username ⊗ Password).
- **S/O/P tower evidence**: present but INFORMAL here — the RDF `(subject, predicate,
  object)` triple appears in `physics_axioms.md`/`INTERPRETATION-CHAIN.md` as Layer 8
  (Knowledge), and the rebuttal separates `has_taxonomic_type` (domain Individual /
  range TaxonNode) relations. The nth-dimensional independent S/O/P **towers** of the
  unary law are the FORMALIZATION of these informal triple relations.
- **sha256 identity**: `ITIS.sqlite.witness.md` uses SHA-256 as the content-addressed
  witness identity; the observation `PROTOCOL CHAIN` (`definition_category_theory.md`)
  is a SHA-256/512 hash chain (`O_SYNC`, tamper-evident) — the informal ancestor of
  the AOB `sha256` identity + SP3's `z = uint16 of first two source_sha256 octets`.

## 4. W2-lens findings (what this facet contributes to SP1..SP9)

- **AOB atom shape (SP2)** — grounded here in original YAML (`cannon_bootstrap/`).
  SP2 must lift THIS 9-field shape (kind/urn/version/identity/value_space/morphisms/
  examples/claims/kernel_bind), not invent one. The `examples` block (30-slot 3× rule)
  IS the atom-evidence contract.
- **Progenitor / composability (protogenitor pattern)** — `gpt_ontology/` Avogadro
  layer: **Progenitors are absolute root origins tracked as SEPARATE axes**
  (upstream / vendor / hardware / license / conceptual-donor). `sil-gpu` "demonstrates
  axis separation: vendor, platform, hardware, upstream tracked as separate progenitor
  axes" — the exact "model every distinct thing as its own atom, nothing crammed"
  doctrine (endianness-as-agnostic-progenitor is the same shape one level down).
- **Universal anchors (CCO/BFO)** — `gpt_ontology` binds the whole scheme to **BFO
  (Basic Formal Ontology) + CCO (Common Core Ontologies)** as the "governance" upper
  ontology ("a CCO-style ontology is not a bag of nouns"; §"BFO and CCO as
  Governance"; bib cites `BFO-2020`). This is the informal witness for the
  load-bearing `universal_anchors` CCO/BFO anchor. (Note: `basicttl/*.ttl` already
  uses `cco:`/`cceo:` prefixes per JUNGLE_MAP.)
- **Projection family + nth-dim effect/loss** — the FIVE target functors are the
  projection family (`free_category.md`: `F_fs / F_db / F_rdf / F_test / F_bash`;
  `language_arts.md` adds `F_python / F_scala / F_sql / F_molt`). "Same syntax, different
  functor, different reality." Loss/effect is carried by the **monad** (Turtle 4 =
  subtext = `Result[A, Error]`) and by the observation trichotomy (Expected/Unexpected/
  **UNKNOWN**=loss the grammar can't express). SP1's 5 loss classes descend from these
  realization effects; the full nth-dim loss taxonomy is NOT enumerated in this facet
  (it is the formal SP4 job) — stated honestly.
- **Geometer/glossary axes vs towers** — dimensions here are **per-atom and named**
  (a `Dimension` is "an independent axis of variation, itself an AOB"); value_space is
  a product of them with a declared `dimensionality` (e.g. AtomicObject=9, ValueSpace=3,
  Neuron=5). This is the "dimension is per-geometer, axes are nth" axiom in its informal
  form: axes are whatever the atom declares (name/state/season/…), NOT a fixed a,b/x,y/
  x,y,z,w tower. The **glossary/epistemology** axis is `cannon_*` itself: each cannon
  directory encapsulates a DISTINCT epistemology (physics vs observation vs language vs
  soul vs paradigm) — the "mole of glossaries". Polysemy is literal: `reserved_words.md`
  shows `key` = 8 simultaneous meanings, resolved only by the `VAR_`/`$()` category
  declaration (Directive 1's synonym-and-antonym-simultaneously, informal source).
- **Telephone twin (Directive 6)** — NOT located in this facet. `01_src` has no
  `agents/telephone` file and no "twin mention". The nearest analogue is the **gossip /
  Dunbar propagation** layer (`definition_category_theory.md` §Gossip: individual →
  neighbourhood(inner-5) → state(inner-15) → federation(active-150)), and the "twin"
  taiji imagery in `YGGDRASIL` (🐢🐈‍⬛🐈). The telephone-twin's concrete site lives in the
  base_agents facet, not here — stated honestly.
- **Yoneda / functorial-transport / presheaf / colimit / sheaf-gluing (SP1 re-derived)**
  — ALL present as informal witnesses: Yoneda (`observation/yoneda.md`, `paradigm/
  yoneda.md`, `yoneda_card.md.j2`, every MASTER diagram); functorial transport (the 5
  functors + monoid homomorphisms φ_BP/ψ_PC across monoliths); **presheaf** (`O: U^op →
  Set`, "the 30-slot matrix IS the restriction maps"); **colimit** (Mittens ≅
  colim D_Mittens; `Cat ≅ colim(D)` mereology in `gpt_ontology`; TestSuite = "colimit of
  all TestGen outputs"); **sheaf-gluing** ("if two overlapping observations agree on
  their overlap they glue to a unique global observation; **CRDT merge IS this
  gluing**", `sheafGlues` morphism in MASTER). SP1 turned each of these into
  teeth-proven TTL — this facet is the prose they were proven from.

## 5. Relationship to the committed SP1 floor (correction/derivation map)

| SP1 floor (`basicttl/primitives/`, teeth-proven) | source-witness ancestor here (informal) |
|---|---|
| twin-olog colimit taiji (formal ⟷ physical) | Mittens cocone + `Cat ≅ colim(D)`; YIN/YANG taiji imagery |
| monadic realization ρ = the Frame | monad = "subtext" (`language_arts.md` T4); `Result[A,E]` |
| Frame = Yoneda point | `yoneda.md` "obs IS Hom(-,Obs) sources + F(Obs) sinks" |
| Bit→Octet→ByteVector descent, byte cap | `physics_axioms.md` §0 "The Bit"; INTERPRETATION-CHAIN drill-to-bits |
| RGB/256 code space | present only as a future note (not in this facet's evidence) |
| S/O/P nth-dim towers | informal RDF triples + rebuttal's separated relation legs |
| dual-grounding (no bare `xsd:` leaf) | claims+probe + kernel_bind grounding to hardware |
| 30-slot / class-form orphan teeth | 3× rule + UNKNOWN alarm (uncovered ⇒ ALARM, not force-fit) |

**Correction SP1 makes over the witnesses**: the witnesses ground atoms to a
Linux-kernel substrate (`sysfs`/`syscall`/`exec_model`) and to KVRocks/CRDT infra —
i.e. corpus-SPECIFIC. SP1 (per Directive 7) strips that to a **corpus-AGNOSTIC**
Bit/ByteVector floor and replaces "trust the probe ran" with SHACL `sh:sparql`
teeth (injection-proven to bite). The witnesses assert; SP1 proves.

## 6. Coverage (Präriehund honesty)

- **Read IN FULL** (every line): all 7 `cannon_bootstrap/*.yaml`; all 5
  `cannon_observation/*` (incl. `queries.sparql`); `cannon_physics/physics_axioms.md`;
  all 6 `cannon_paradigm/*`; `cannon_workflow/monoid_algebra.md`; all 3
  `cannon_language/*`; `cannon_cheese/cheese.md`; both `cannon_runtime/*`;
  `cannon_soul/MASTER-…md` + `INTERPRETATION-CHAIN.md`; all 3 `cannon_templates/*.j2`;
  `cannon_tax/ITIS.sqlite.witness.md` + `ReadmeSqlite.txt`; both `rebuttal_round00/
  gippidy0{0,1}.md`; `gpt_ontology/generated_90_abstract.tex`.
- **Sampled broadly (schema/thesis captured, not every line)**: `cannon_soul/
  ACID-TRIP-NEURON.md` (~120/444), `YGGDRASIL-…md` (~80/200), `SESSION-CLOSE-…md`
  (~60/281) — worldview prose, atom schema confirmed identical to bootstrap; the 4
  large `gpt_ontology/*.tex` (69-node 5386 L, master 4892 L, manifest-hom 3257 L,
  100-node 2144 L) — read the abstract in full + targeted reads of the SIL-namespace
  rules (R1-R12), progenitor/BIOS/CCO/BFO sections, and colimit sections via grep;
  the 100-node and 69-node bodies characterized from their shared preamble + section
  index, NOT line-by-line. `rebuttal_round00/test.html` (~40/581 — a Tailwind dark
  render, non-load-bearing). `cannon_tax/tax_raw_snapshot.tsv` (header + ~9/92 rows —
  enough to confirm the Felis-catus TSN 183798 row + `catus` collisions + raw-custody
  defects); `ITIS.sqbpro` (SQLiteStudio XML project — not read; a query workspace,
  no ontological content).
- **Honest gaps in THIS facet**: no telephone-twin site; no explicit endianness
  progenitor (it is a "later problem" per Directive 2, absent from these witnesses);
  the full nth-dim projection loss taxonomy is not enumerated (SP4's job); RGB/256
  color space appears only as a forward reference, not as witness evidence.
