# REFMAP SHARD R3 — Engine algebra substrate, skills taxonomy, carrier bridge points

MAP-agent evidence (Praeriehund honesty: file:line, counts, quotes). Governing law: Directives 24
(Seed-Carrier) + 25 (fold into `basicttl/primordial/type/**`, spine-first, TODO-11 "bridge, never
duplicate"). This shard extracts the ENGINE-side algebra definitions the folded spine must BRIDGE to.

Reference roots (scratchpad, read-only):
- `T = /tmp/claude-0/-home-user-silmaril/9319deb2-2eab-59fd-b601-de3e0fb18f37/scratchpad/refcomp/tar/bash`
  (the 4101-file bash engine, master drop commit 4b5c4e25).

Repo roots referenced (fold target / inbound):
- `basicttl/foundation/*.ttl` (the committed `fnd:` floor — the SOURCE of the spine being reshaped).
- `basicttl/primordial/type/**` (the Directive-25 FOLD TARGET).

===============================================================================
## 0. HEADLINE FINDINGS (the bridge the fold must build)
===============================================================================

**F1 — The engine has NO magma/semigroup/monoid/commutative-monoid/abelian/quasigroup/loop rungs.**
The entire engine algebra tower is a FLAT fan of six leaves under one `TYPE/ALGEBRA` root:
`SET, CLASS, GROUP, CATEGORY, TOPOLOGY, GEOMETRY` (`T/config/algebra/primordials.yaml` :394–573;
`T/lib/type-dag/algebra.sh` has functions only for those six). The engine `GROUP` atom CRAMS all four
group axioms (closure, associativity, identity, inverse) into a single leaf with no intermediate
weakenings. Therefore the `fnd:` spine rungs `Magma→Semigroup→Monoid→CommutativeMonoid→Group→
AbelianGroup` + `Quasigroup/Loop` (confirmed present in `basicttl/foundation/algebra_spine.ttl`:
`fnd:AlgebraicStructure, fnd:Magma, fnd:Semigroup, fnd:Monoid, fnd:CommutativeMonoid, fnd:Group,
fnd:AbelianGroup, fnd:Quasigroup, fnd:Loop`) have **no rung-for-rung engine counterpart**. Only
`fnd:Group` and `fnd:AlgebraicStructure` have direct engine anchors; the intermediate rungs bridge to
the engine's *axiom* atoms (each engine group axiom = one weakening the fnd: tower re-introduces as a
theory-law record). This is the central TODO-11 bridge obligation.

**F2 — The bridge is a NEW obligation; the committed floor has ZERO engine references.**
`grep` for any `urn:silmaril:type:graph:...:realm:algebra...` engine URN across `basicttl/foundation/`
returns nothing; `reanchor.ttl` carries no engine `Primordial::Algebra::*` bridge. So the seed-bridge
edges from each `fnd:` rung to the engine algebra IRIs do not yet exist and must be authored in the
fold (`skos:exactMatch` / `seed:conservativeBridge` / `seed:implementationBridge` per Directive 24).

**F3 — The fold-target idiom is `urn:silmaril:primordial:type:` + `schema:seeAlso primitive:*`.**
`basicttl/primordial/type/algebra/product/frame.ttl` :7 declares `family:Frame a ontology:Class,
model:ClassDeclaration, model:Product, model:Frame ; schema:seeAlso primitive:Frame` — i.e. the
primordial tree already bridges to the `prim:` layer via `schema:seeAlso`, but does so with CamelCase
locals AND class-punning (`a owl:Class, model:Product, model:Frame` on one subject). Per Directive 25
the reshaped algebra subtree ADOPTS the primordial IRI root + `schema:seeAlso primitive:` bridge idiom
but FIXES the punning/extensional flaws (splits theory/model/element/proof planes) rather than copying
them.

===============================================================================
## 1. `.skills` TAXONOMY + ORGANIZATION (law / engine / type / runtime)
===============================================================================

Top level `T/.skills/`: `HEAD.md`, `HEAD.yaml`, and four kingdom dirs `engine/ law/ runtime/ type/`
(`T/.skills` listing). The kingdom is the FIRST path segment under `.skills` AND a taxonomy coordinate.

`T/.skills/HEAD.yaml` is the machine pointer index. Structure (deep-KV YAML, see §3):
- `HEAD:IDENTITY:VALUE` :3 — the head's own URN (`...:kingdom:registry:phylum:head:class:skill:...`).
- `HEAD:PROJECTION:VALUE` :5 = `'KINGDOM DOMAIN PHYLUM SPECIES'` — the 4-coordinate projection used to
  name/select a skill from its full URN.
- `HEAD:SPECIMEN:CARDINALITY:VALUE` :8 = `'21'` — **21 indexed skill specimens**.
- Each `ENTRY <N>` carries `IDENTITY:VALUE` (full URN), `PATH:VALUE` (`.skills/...` dir), `SCOPE:VALUE`.
- `HEAD:ADMISSION:VALUE` :157 = `'engineering projection only; research corpus blocked'`.
- `HEAD:GAP:ROOT:VALUE` :159 — a blocking research-admission gap URN (the corpus is un-sealed).

`HEAD.md` :11 states it plainly: *"This is a provisional engineering index, not a sealed
research-admission head."*

The 21 specimens by kingdom (from `HEAD.yaml` PATH values):
- **type/ (13):** `type/mathematics/algebra/{set,class,group,category,topology,geometry}` (ENTRY 1–6),
  `type/computation/carrier/{byte,octet,file/stream}` (ENTRY 7–9), `type/knowledge/object/object`
  (ENTRY 10), `type/computation/product/frame` (ENTRY 11), `type/identifier/identifier/name`
  (ENTRY 12), `type/computation/graph/node` (ENTRY 13).
- **engine/ (2):** `engine/computation/graph/dag` (ENTRY 15, "Declarative typed polymorphic DAG
  executor").
- **runtime/ (1):** `runtime/software/interpreter/runtime` (ENTRY 14, "Bash builtin only runtime
  boundary").
- **law/ (5):** `law/software/purity/runtime` (ENTRY 16), `law/computation/carrier/parser` (17),
  `law/knowledge/inheritance/resolution` (18, "Monotonic C3 multiple inheritance linearization"),
  `law/computation/contract/contract` (19, "Unary domain codomain receiver and frame admission"),
  `law/knowledge/materialization/aob` (20, "Full lexical AOB path projection"),
  `law/information/algebra/primordial/pair` (21).

**Kingdom semantics** (from the URN `kingdom:` coordinate, cross-checked against skill scopes):
`type` = a type/atom definition; `law` = a binding contract/prohibition; `engine` = an executor;
`runtime` = a host-boundary. The kingdom is polysemous with the SPECIES taxonomy: e.g. the group
*type* skill has `kingdom:type` but its axiom atoms have `kingdom:axiom` (see §4).

===============================================================================
## 2. WHAT EACH ALGEBRA SKILL DEFINES (type, atoms, laws, validators)
===============================================================================

Each `.skills/type/mathematics/algebra/<S>/` holds a thin `SKILL.md` + `atom.spec.yaml` that only
POINT (IDENTITY URN, IMPLEMENTATION path, SCOPE, `STATE: sealed`) — the real DEFINITIONS live in
`T/config/algebra/primordials.yaml` (the type registry) and `T/lib/type-dag/algebra.sh` (the
validators). Every skill's `atom.spec.yaml:IMPLEMENTATION:PACKAGE RELATIVE PATH:VALUE` =
`'lib/type-dag/algebra.sh'` (e.g. `set/atom.spec.yaml` :17). Runtime for all: `'Bash builtins only'`.

**Common root.** `primordials.yaml` :394–404 — `TYPE/ALGEBRA` (`...:subdomain:primordial:...:class:
structure:...:species:root`): *"root of registered structures defined by carriers operations
identities composition and axioms"*, `ABSTRACT: true`, `PARENT: TYPE/PRIMORDIAL`. All six leaves have
`PARENT: TYPE/ALGEBRA`.

### 2.1 SET — `species:set`, scope "Finite membership and extensional equality witness"
- Type: `primordials.yaml` :405–425, `TYPE/ALGEBRA/SET`, `ABSTRACT: true`; def *"collection determined
  solely by typed membership"*. Refinement `TYPE/ALGEBRA/SET/FINITE` :426–438 (`ABSTRACT: false`,
  SECONDARY parent `TYPE/OBJECT/SET/BOUND`) — *"members exhaustively registered in a finite vector"*.
- **Law/axiom atom:** EXTENSIONALITY :416–421 — *"two sets are equal exactly when they have the same
  members"* (URN `...:subdomain:set:kingdom:axiom:phylum:membership:class:extensionality:...`).
- **Method:** MEASURE :422–425 → the cardinality operation URN (`...:kingdom:operation:...:class:
  cardinality:order:unary:...`).
- **Validators (`algebra.sh`):** `set::define` :42, `set::add` :67, `set::contains` :86,
  `set::cardinality` :97, `set::is_empty` :115, `set::subset` :125, `set::equal` :145 (subset both
  ways = extensionality tooth), `set::union_equals` :154, `set::intersection_equals` :189.

### 2.2 CLASS — `species:class`, scope "Typed predicate membership without set collapse"
- Type: `primordials.yaml` :439–455, `TYPE/ALGEBRA/CLASS`, `ABSTRACT: false`; def *"collection
  specified by a typed membership predicate and not assumed to be a set"* (proper-class discipline).
- **Axiom atom:** MEMBERSHIP :450–455 — *"class membership is decided by its registered type
  predicate"*.
- **Validators (`algebra.sh`):** `class::define` :224 (binds a `member_type` via `type::resolve`),
  `class::contains` :240 (decides membership by `type::inherits object_type member_type` :252 — NO
  enumeration; polymorphic classification, exactly the intensional idiom Directive 23 asks fnd: to
  reach).

### 2.3 GROUP — `species:group`, scope "Finite group axioms and witness validation"
- Type: `primordials.yaml` :456–487, `TYPE/ALGEBRA/GROUP`, `ABSTRACT: false`; def *"carrier set with a
  closed associative binary operation identity and inverse for every member"*.
- **FOUR crammed axiom atoms** (each a distinct `kingdom:axiom` URN):
  - CLOSURE :467–472 — *"every product of members is a member"*
    (`...:class:closure:...:genus:product:species:membership`).
  - ASSOCIATIVITY :473–477 — *"every admitted triple associates"*
    (`...:class:associativity:...:genus:composition:species:equality`).
  - IDENTITY :478–482 — *"one registered member is a two sided identity"*
    (`...:class:identity:...:genus:neutral:species:member`).
  - INVERSE :483–487 — *"every member has a two sided inverse"*
    (`...:class:inverse:...:genus:member:species:inverse`).
  Each axiom also materializes its own deep AOB atom under `T/aob/urn/.../subdomain/group/kingdom/
  axiom/...` (closure/identity/inverse/associativity, all present — 12 group/set/class AOB atoms
  counted under `subdomain/{group,set,class}`; 14 total under `realm/algebra`).
- **Validators (`algebra.sh`):** `group::define` :256 (carrier must exist + identity ∈ carrier),
  `group::product` :281 (Cayley cell; asserts closure — result ∈ carrier :295), `group::operate` :303,
  `group::validate` :321. `group::validate` is the biting tooth:
  - identity axiom :343–349 (`e·x==x && x·e==x`);
  - inverse axiom :351–363 (∃ y: `x·y==e && y·x==e`);
  - associativity :366–379 (triple loop `(x·y)·z == x·(y·z)`).
  Note: closure is enforced at CELL-DEFINITION time (`group::product` :295), not re-checked in
  `validate`. Directive 25's "master's strengthened magma-totality tooth" maps onto making this
  cell-time closure a first-class intensional law record + probe.

### 2.4 CATEGORY — `realm:category:subdomain:small`, scope "Finite categorical identities and
associative composition"
- Type: `primordials.yaml` :488–509, `TYPE/ALGEBRA/CATEGORY`, `ABSTRACT: false`; def *"objects
  morphisms typed composition identity morphisms and associative composition"*.
- **Axiom atoms:** IDENTITY :500–504 (*"every object has a left and right identity morphism"*),
  ASSOCIATIVITY :505–509 (*"every composable morphism triple associates"*).
- **Validators (`algebra.sh`):** `category::define` :383, `category::object` :399, `category::morphism`
  :417 (endpoints must be objects), `category::identity` :446 (identity must be an endomorphism :459),
  `category::composition` :467 (composability check `target(first)==source(second)` :483),
  `category::compose` :495, `category::validate` :510 (per-object identity :536, left/right identity
  law :544, associativity over composable triples :562).

### 2.5 TOPOLOGY — `realm:topology:subdomain:finite`, scope "Finite topology open set axioms"
- Type: `primordials.yaml` :510–541, `TYPE/ALGEBRA/TOPOLOGY`, `ABSTRACT: false`; def carrier + open
  family containing ∅ and X, closed under unions + finite intersections.
- **FOUR axiom atoms:** EMPTY :522–526, UNIVERSAL :527–531, UNION :532–536 (*"unions of open sets are
  open"*, `order:arbitrary`), INTERSECTION :537–541 (`order:finite`).
- **Validators (`algebra.sh`):** `topology::define` :587, `topology::open` :607, `topology::validate`
  :628 (∅+X present :648–659; union+intersection closure over open-set pairs :661–674 using
  `set::union_equals`/`set::intersection_equals`).

### 2.6 GEOMETRY — `realm:geometry:subdomain:metric`, scope "Finite metric space axioms"
- Type: `primordials.yaml` :542–573, `TYPE/ALGEBRA/GEOMETRY`, `ABSTRACT: false`; def *"point set
  equipped with a nonnegative symmetric separating distance satisfying the triangle inequality"*.
- **FOUR axiom atoms:** NONNEGATIVE :554–558, SEPARATION :559–563 (*"distance is zero exactly for an
  identical point pair"*), SYMMETRY :564–568, TRIANGLE :569–573.
- **Validators (`algebra.sh`):** `geometry::define` :678, `geometry::distance` :697 (distance must be
  nonneg-integer notation :715; points ∈ carrier), `geometry::_get_distance` :723, `geometry::validate`
  :741 (nonneg+symmetry+separation :761–782; triangle inequality :784–796).

### 2.7 The single validator dispatcher (the engine's "algebra::validate")
`algebra.sh` :800–819 `algebra::validate(type_reference, structure_identity)` dispatches by
`type::inherits type_reference 'TYPE/ALGEBRA/{GROUP,CATEGORY,TOPOLOGY,GEOMETRY,SET}'`. **CLASS has no
validate branch** (membership is decided pointwise by `class::contains`, not batch-validated). Line 817
fails closed: *"no axiom validator is registered for ${type_reference}"*. This dispatcher is the
engine's law-witness-mode selector; the fold's per-model "validation MODE" (finite-table / rewrite /
external-cert / bounded — Directive 24) bridges to this dispatch shape.

===============================================================================
## 3. THE atom.spec.yaml SCHEMA (deep-KV YAML — the manifest idiom to lift)
===============================================================================

Two atom.spec.yaml FLAVORS exist, both **deep-nested key-value YAML terminating in a scalar `VALUE:`**
(never inline maps/lists; every leaf is `KEY:\n  VALUE: '...'`). This is Directive 24's "deep-KV YAML"
manifest idiom, natively present in the engine.

**Flavor A — SKILL spec** (`.skills/<...>/atom.spec.yaml`), thin pointer. Top key `SKILL:` with:
`IDENTITY:VALUE` (URN), `AOB:PATH:VALUE` (the authoritative deep AOB path),
`TAXONOMY:{KINGDOM,DOMAIN,PHYLUM,SPECIES}:VALUE`, `IMPLEMENTATION:PACKAGE RELATIVE PATH:VALUE`,
`SCOPE:VALUE`, `RUNTIME:VALUE`, `STATE:VALUE` (`'sealed'`). Example: `group/atom.spec.yaml` :1–25.
Note the PAIR skill's `TAXONOMY:SPECIES:VALUE` = `'primordial:pair'` (`pair/atom.spec.yaml`) — SPECIES
itself carries a colon-descent, i.e. the naming grammar the fold adopts is already in the engine.

**Flavor B — deep AOB atom** (`T/aob/urn/silmaril/.../atom.spec.yaml`, one per full URN path), the
RICH envelope. Top-level keys (from the GROUP type atom `.../subdomain/group/.../species/group/.../
atom.spec.yaml` :1–115 and the CLOSURE axiom atom):
- `ATOM:{IDENTITY:VALUE, UNIVERSAL ROOT:VALUE (='urn:silmaril:type:graph:instance:instruction:code:
  property'), KIND:VALUE (='semantic specimen')}` :1–7.
- `GROUNDING:CARRIER:{LAMBDA,BYTE,OCTET}:VALUE` :8–17 — **the carrier grounding: every atom names its
  Lambda/Byte/Octet carrier URNs** + `NOTATION:VALUE`=`'lexical byte stream interpreted under locale
  C'`. This is the atom-level bridge to prim:Octet/ByteVector (§5).
- `GROUNDING:ONTOLOGY:PRIMARY:VALUE` :18–20 — a CCO/BFO-style *"basic formal"* upper-ontology bridge
  URN; `STATUS:VALUE`=`'internal bridge evidence and not an external import claim'` :21–22 (honest-red:
  the engine already declares upper-ontology anchoring as bridge-only, not import — matches the
  exemplar's `universal_anchors` pattern-by-anchor).
- `TAXONOMY:` :23–59 — all 11 Linnaean rungs, each `<RUNG>:LEXICAL DESCENT:VALUE`
  (DOMAIN/REALM/SUBDOMAIN/KINGDOM/PHYLUM/CLASS/ORDER/FAMILY/GENUS/SPECIES/COMPONENT/INSTANCE).
- `INHERITANCE:DISPOSITION:VALUE` :60–62, `DENOTATION:RESOURCE UNIFORM NAME:VALUE` :63–65,
  `POSITION:FILESYSTEM:{PACKAGE RELATIVE,ABSOLUTE}` :66–72, `PATH:TAXONOMIC PROJECTION:VALUE` :73–75,
  `PROTOCOL:{ACCESS,EXECUTION}` :76–80.
- `EVIDENCE:SOURCE:{PACKAGE RELATIVE PATH:VALUE (='config/algebra/primordials.yaml'), LINE:{TYPE:VALUE
  (a natural-number carrier URN), NOTATION:VALUE (='441' for group type, '452' for closure axiom)}}`
  :81–89 — **each AOB atom cites its config source file:line** (the group type points at
  primordials.yaml:441; closure axiom at :452). This IS the file:line evidence discipline, native.
- `EVIDENCE:DIGEST:DISPOSITION:VALUE` :90–92 (*"integrity evidence only and never semantic identity"*).
- `PROVENANCE:{AUTHORITY:VALUE, STATE:VALUE (='provisional')}` :93–97.
- `PROJECTION:{SELF,SKILL}` :98–103; `GAPS:{CARDINALITY:NOTATION:VALUE, ITEM:CORPUS:REFERENCE:VALUE}`
  :104–111 (the blocking research-gap URN); `RECEIPT:MATERIALIZATION:VALUE` :112–114 (*"present; not a
  constitutional acceptance seal"*).

**Fold consequence:** the reshape's `manifests/` (deep-KV YAML, Directive 24) SHOULD adopt Flavor-B's
envelope — especially `EVIDENCE:SOURCE:...:LINE`, `GROUNDING:CARRIER`, `PROVENANCE:STATE`,
`GAPS`/`RECEIPT` — as the manifest schema, since it already encodes provenance + source-locator +
carrier-grounding + honest-gap in the engine's own idiom.

===============================================================================
## 4. THE ENGINE TYPE-DAG (the full type tree the algebra sits in)
===============================================================================

`T/config/algebra/primordials.yaml` is the whole registry (`REGISTRY:IDENTITY` :1–3). Root
`TYPE/PRIMORDIAL` :4–21 — *"universal semantic root for every admitted type and object"*, `ABSTRACT`,
`PARENT:CARDINALITY:VALUE`=`'zero'`, and carries a reflexive-identity AXIOM :16–21 (*"every admitted
specimen is identical to itself"*). Direct children of `TYPE/PRIMORDIAL`:
- `TYPE/SCALAR` :22 → `TOKEN` :35 → `NATURAL` :48 (regex `^(0|[1-9][0-9]*)$`); `IDENTIFIER/RESOURCE/
  UNIFORM/NAME` :72 (regex `^urn:silmaril:.+$`); `NONE` :61 (typed absence — the Frame's non-value).
- `TYPE/PATH/ABSOLUTE` :88.
- `TYPE/OBJECT` :102 (sealed typed object w/ linearized fields) → `PATH/BOUND` :113, `SET/BOUND` :131.
- `TYPE/CARRIER` :149 (see §5).
- `TYPE/ALGEBRA` :394 (see §2).
- `TYPE/FRAME` :574 (see §5.4); `TYPE/DAG/NODE` :607; `TYPE/COMPOSITE/PRODUCT` :621.

**Type-DAG semantics:** parents are given as slash-paths (`PARENT:PRIMARY:VALUE`=`'TYPE/ALGEBRA'`),
resolved by `type::inherits` / `type::resolve` in `T/lib/type-dag/type.sh`; multiple inheritance via
`PARENT:SECONDARY` (e.g. `SET/FINITE` :437–438 also `TYPE/OBJECT/SET/BOUND`) linearized by the C3 law
skill (ENTRY 18). The algebra atoms are thus TYPED individuals in one DAG, not a bare subclass ladder —
but the tree is still EXTENSIONAL (a group is validated by enumerating its Cayley table via
`group::validate`), which is exactly the flaw Directive 23/24 has the fold repair with intensional
theory/model records + declared validation-mode.

Adjacent config (not algebra-core but bridge-relevant): `T/config/type-dag/` =
`{constitution,corpus,graph,graph-cycle,graph-contract-invalid,objects,operations,purity,runtime}.yaml`
(the DAG-executor contract + purity law fixtures); `T/config/closure/` =
`{acceptance,canonical-graph,errors,grounding,index,local-graph,local-read,rank-lexicon,sha}.yaml` +
`records/` (the grounding-closure + rank-lexicon the naming grammar uses).

===============================================================================
## 5. CARRIER DEFINITIONS — bridge to prim:Frame / prim:Octet / prim:ByteVector
===============================================================================

`TYPE/CARRIER` subtree, `primordials.yaml` :149–393. This is the byte/octet floor the fold's
`groundsIn*` / `schema:seeAlso primitive:*` edges bridge to.

### 5.1 Carrier lineage (Lambda → Bit → Byte → Octet)
- `TYPE/CARRIER` :149–159 — *"physical realization lineage rooted in Lambda ... without semantic
  collapse"*, `ABSTRACT`, `PARENT: TYPE/PRIMORDIAL`. `class:substrate:order:lambda`.
- `TYPE/CARRIER/LAMBDA` :160–170 — *"primordial physical carrier ancestor"*, ABSTRACT.
- `TYPE/CARRIER/BIT` :171–183 — *"binary coordinate carried beneath every registered byte width"*,
  `PATTERN: ^[01]$`, `PARENT: TYPE/CARRIER/LAMBDA`. **← bridge target for prim:Bit.**
- `TYPE/CARRIER/BYTE` :184–198 — *"registered ordered bit vector cell whose width bit order byte order
  and encoding remain independent coordinates"*, ABSTRACT, `PARENT: TYPE/CARRIER`,
  `REALIZATION:ELEMENT:TYPE: TYPE/CARRIER/BIT`. **← bridge target for prim:Byte (width-independent).**
  - `BYTE/WIDTH` progenitor :199–209 (ABSTRACT) + concrete children ONE/TWO/FOUR/EIGHT/SIXTEEN/
    THIRTY TWO/SIXTY FOUR/ONE HUNDRED TWENTY EIGHT :210–297 — the width lattice 1..128 (Directive 3's
    "width 1..128" is literally here). Each is a separate atom (agnostic-progenitor pattern, native).
  - `BYTE/VECTOR` :298–312 — *"finite ordered sequence of registered byte cells without a fixed
    universal width"*, `REALIZATION:ELEMENT:TYPE: TYPE/CARRIER/BYTE`. **← bridge target for
    prim:ByteVector.**
  - `BYTE/STREAM` :313–327 — *"ordered registered width byte carrier consumed incrementally"*.

### 5.2 Octet (the 8-bit projection) — bridge to prim:Octet
- `TYPE/CARRIER/OCTET` :328–346 — *"eight bit projection of the general byte carrier used by host file
  descriptors"*, `ABSTRACT: false`, `PATTERN: ^[[:digit:]]+$`, `PARENT: TYPE/CARRIER/BYTE`. Carries a
  WIDTH AXIOM :341–346 — *"an octet has exactly the registered eight bit width while Byte remains width
  independent"*. **This axiom IS the Byte≠Octet distinction (Directive 3 / Directive 24
  `owl:differentFrom`-witnessed "unsignedByte ≠ machine byte ≠ Z/256Z").** ← bridge target for
  prim:Octet.
- `OCTET/VECTOR` :347–361 (`PARENT: TYPE/CARRIER/BYTE/VECTOR`, element `TYPE/CARRIER/OCTET`).
- `OCTET/STREAM` :362–376 — *"the only admitted eight bit projection of the general byte stream"*.
  - `OCTET/STREAM/FILE` :377–393 — `ABSTRACT: false`, dual parent `TYPE/CARRIER/OCTET/STREAM` +
    `TYPE/OBJECT/PATH/BOUND`; `METHOD:MEASURE:OPERATION` = the octet-file cardinality op. This is the
    ENTRY-9 `file/stream` skill's atom ("NUL safe octet stream over an existing file descriptor").
- Implementation: `T/lib/type-dag/byte.sh` — `byte::assert` :24 (`^(0|[1-9][0-9]?[0-9]?)$` and
  `0..SIL_BYTE_MAXIMUM`), `byte::_walk_chunk` :37 (per-character ordinal via `printf '%d' "'c"`).

### 5.3 Group/atom carrier grounding (how algebra atoms reach the carriers)
Every deep AOB algebra atom names its carriers in `GROUNDING:CARRIER:{LAMBDA,BYTE,OCTET}` (§3; group
type atom :8–17, closure axiom atom :8–17). So the engine already grounds each algebra specimen into
Lambda/Byte/Octet — the fold's algebra rung `schema:seeAlso`/`groundsIn` to prim:Octet is the SAME edge
the engine expresses in YAML.

### 5.4 Frame — bridge to prim:Frame (Directive 3/19 Yoneda-point / Curry-F)
- `TYPE/FRAME` :574–584 — *"one operational result product with separate output effect error state and
  provenance coordinates"*, `ABSTRACT: false`, `PARENT: TYPE/PRIMORDIAL`. (ENTRY-11 skill
  `type/computation/product/frame`, scope "One typed result with separate operational coordinates".)
- `FRAME/EFFECT` :585–595 + `FRAME/ERROR` :596–606 — canonical effect/error disposition identities
  (parent `TYPE/IDENTIFIER/RESOURCE/UNIFORM/NAME`).
- Implementation `T/lib/type-dag/frame.sh` :8–17 — a Frame is the 10-slot record
  `{NODE, OUTPUT_TYPE, OUTPUT_VALUE, OUTPUT_PRESENT, EFFECT_TYPE, EFFECT_VALUE, ERROR_TYPE,
  ERROR_VALUE, STATE, PROVENANCE}`; `frame::success` :35 sets output+effect and clears error;
  `frame::failure` :57 sets output to NONE. **This is exactly the `Frame(output:X, effect|error:Y)`
  the Directive-19 Curry-F / Directive-21 RosarchQueryFrame pillar re-anchors onto** — and the
  fold-target `basicttl/primordial/type/algebra/product/frame.ttl` already declares
  `family:Frame ... schema:seeAlso primitive:Frame` with `OutputParameter`/`EffectParameter` (invariant)
  + `OutputField`/`EffectField`. So `prim:Frame` ↔ engine `TYPE/FRAME` ↔ `fnd:` Frame/ArrowType is a
  three-way bridge already half-built on the primordial side.

### 5.5 The primordial-pair law (KV-binding algebra) — the deep-KV engine itself
- ENTRY-21 skill `law/information/algebra/primordial/pair`, scope "Contextual key value binding algebra
  projection", `IMPLEMENTATION: lib/type-dag/yaml.sh`, `SPECIES: primordial:pair`. This is the algebra
  of the deep-KV YAML manifests (§3) — a recursive typed key→value binding
  (`...:class:product:order:binary:product:family:key:value:binding:genus:recursive:typed:binding:
  species:primordial:pair`). Directive 24's "manifests/ (deep-KV YAML)" bridges to THIS law atom.

### 5.6 DAG node / composite product (the graded/product bridge)
- `TYPE/DAG/NODE` :607–620 — *"declarative operation or object method occurrence with typed dependency
  edges and one frame"* (ENTRY-13). `TYPE/COMPOSITE/PRODUCT` :621–632 — *"finite product record with
  separately typed dependency components; not a concatenated scalar"*. These bridge the SP3 CRS
  product / role-tower "graded structure" claims (Directive 18) to the engine product record.

===============================================================================
## 6. THE EXACT BRIDGE TABLE (fnd: rung → engine anchor) — TODO-11 targets
===============================================================================

Bridge kind per Directive 24: `skos:exactMatch` (same denotatum), `seed:conservativeBridge`
(engine is a faithful sub-theory), `seed:implementationBridge` (engine is one realization). fnd: names
confirmed in `basicttl/foundation/algebra_spine.ttl`; engine URNs from `primordials.yaml`.

| fnd: rung | Engine anchor (URN species / atom) | primordials.yaml | Bridge kind | Note |
|---|---|---|---|---|
| `fnd:AlgebraicStructure` | `TYPE/ALGEBRA` (`...:subdomain:primordial:...:species:root`) | :394–404 | conservativeBridge | engine "algebra root" ≈ fnd: structure root |
| `fnd:Magma` | NO engine rung → engine GROUP **CLOSURE** axiom atom | :467–472 | conservativeBridge (to the closure law only) | magma = carrier+total binary op; engine has no magma type, only the closure axiom + `group::product` cell-closure :295 |
| `fnd:Semigroup` | NO engine rung → engine GROUP **ASSOCIATIVITY** axiom atom | :473–477 | conservativeBridge (associativity law) | |
| `fnd:Monoid` | NO engine rung → engine GROUP **IDENTITY** axiom atom | :478–482 | conservativeBridge (two-sided identity — 2 Equation records per D25) | |
| `fnd:CommutativeMonoid` | NO engine rung, NO engine commutativity axiom | — | BUILD (no anchor) | honest-red: engine never models commutativity |
| `fnd:Group` | `TYPE/ALGEBRA/GROUP` + 4 axiom atoms + `group::validate` | :456–487 / algebra.sh:321 | **exactMatch** (D24 "SealedGroup→Group teeth-proven") | the one direct type-level anchor; engine crams all 4 axioms here |
| `fnd:AbelianGroup` | NO engine rung, NO commutativity axiom | — | BUILD (no anchor) | Blotto `A_{m-1}` witness (D22) is the intended model; still no engine type |
| `fnd:Quasigroup` / `fnd:Loop` | NO engine rung | — | BUILD (no anchor) | |
| `fnd:Set` (set_theory.ttl) | `TYPE/ALGEBRA/SET` + EXTENSIONALITY + FINITE | :405–438 | conservativeBridge / closeMatch | engine set is finite/extensional; fnd: set = structural/ETCS (closeMatch only per MAP §3) |
| `fnd:` category (functionality/cat) | `TYPE/ALGEBRA/CATEGORY` + identity/assoc axioms | :488–509 | conservativeBridge | engine = finite small category |
| `fnd:TopologicalSpace` (spaces.ttl) | `TYPE/ALGEBRA/TOPOLOGY` + 4 axiom atoms | :510–541 | conservativeBridge | engine = FINITE topology only |
| `fnd:MetricSpace` (spaces.ttl) | `TYPE/ALGEBRA/GEOMETRY` + 4 axiom atoms | :542–573 | conservativeBridge | engine metric = nonneg-INTEGER distance only |
| `fnd:` Frame / ArrowType / RosarchQueryFrame | `TYPE/FRAME` (frame.sh 10-slot) + `prim:Frame` | :574–606 | implementationBridge | HOLD DISTINCT from primordial runtime `family:Frame` per MAP §3 |
| `fnd:` Octet / ByteVector carriers | `TYPE/CARRIER/OCTET` / `.../BYTE/VECTOR` | :328–361 / :298–312 | implementationBridge | Byte≠Octet width axiom :341–346 = the `owl:differentFrom` witness |
| `fnd:` Bit | `TYPE/CARRIER/BIT` (`^[01]$`) | :171–183 | implementationBridge | |
| Ring/Field/Module/Vector (algebra_rings.ttl) | NO engine algebra rung | — | BUILD + HOMONYM guard | engine has no ring line; homonym hazard is vs `TYPE/COMPOSITE/PRODUCT`/carrier `VECTOR`, guard with `owl:differentFrom` (MAP §3) |
| GroupAction/GSet, Blotto (D22) | NO engine anchor (both trees) | — | BUILD | fan-out, not spine |
| CommutativeMonoid/Ring measure ops | `set::cardinality` measure-op URN idiom | :422–425 | implementationBridge | engine's `METHOD:MEASURE:OPERATION` idiom |

**Net:** of the spine rungs, only **Group** (type) and **AlgebraicStructure** (root) have a
type-level engine anchor; **Magma/Semigroup/Monoid** bridge to the engine's crammed group *axiom*
atoms (closure/associativity/identity); **CommutativeMonoid, AbelianGroup, Quasigroup, Loop** have NO
engine anchor and are pure BUILD (honest-red, cited-math per Directive 20's SYN discipline). The
carriers (Bit/Byte/Octet/ByteVector/Frame) have full, direct engine anchors and are implementationBridges.

===============================================================================
## 7. WHERE THE ENGINE ALREADY MATCHES / VIOLATES THE SEED-CARRIER DOCTRINE
===============================================================================

MATCHES (lift these, don't reinvent):
- deep-KV YAML manifest with per-atom `EVIDENCE:SOURCE:...:LINE` file:line provenance (§3).
- carrier grounding on every atom (`GROUNDING:CARRIER`) = native `groundsIn` (§5.3).
- upper-ontology bridge declared as *"internal bridge evidence and not an external import claim"* (§3)
  = the exemplar's pattern-by-anchor CCO/BFO discipline.
- agnostic-progenitor width lattice (§5.1) + Byte≠Octet distinction axiom (§5.2).
- honest gaps: `PROVENANCE:STATE: provisional`, `GAPS`, `RECEIPT: "not a constitutional acceptance
  seal"`, HEAD `ADMISSION: research corpus blocked` — native Praeriehund honesty.
- intensional CLASS membership by `type::inherits` (§2.2) — the polymorphism Directive 23 wants.

VIOLATES (the fold must FIX in the algebra subtree, not import):
- **Extensional group validation** (`group::validate` enumerates the Cayley table) — the fold re-homes
  this as intensional theory-law records + `fixtures/` Cayley tables + probes (Directive 24 A6/planes).
- **Axiom-cramming**: engine GROUP holds all 4 axioms in one leaf; the fold's spine re-introduces the
  weakenings (magma/semigroup/monoid) as separate theories, each ADDING one Equation record — bridging
  down to the engine's *individual* axiom atoms (which DO exist separately in the AOB tree) rather than
  the crammed type.
- **CamelCase + class-punning in the FOLD TARGET** (`basicttl/primordial/type/algebra/product/
  frame.ttl` :7 `a owl:Class, model:Product, model:Frame`) — Directive 25 requires the reshaped algebra
  subtree fix this to lowercase colon-descent + plane-split, never copy it.

===============================================================================
## 8. COVERAGE ATTESTATION
===============================================================================

Files READ IN FULL: design_constraints.md (D1–25), RECOVERY.md, map/00_MAP_SYNTHESIS_reconstructed.md;
engine `T/.skills/HEAD.yaml` + HEAD.md; all 6 algebra `SKILL.md` + `atom.spec.yaml`
(set/class/group/category/topology/geometry); the pair, frame, byte, octet, file/stream, node
`SKILL.md`; `T/lib/type-dag/algebra.sh` (820 lines, full); `T/config/algebra/primordials.yaml` (633
lines, full); the GROUP type deep AOB + CLOSURE axiom deep AOB (`T/aob/urn/...`); `frame.sh`+`byte.sh`
heads. Repo: `basicttl/foundation/` listing + `algebra_spine.ttl` fnd: rung names;
`basicttl/primordial/type/algebra/` tree + `product/frame.ttl` head; `primordial/type/byte/` listing.

Counts verified by grep/find: 21 skill specimens (HEAD.yaml:8); 6 algebra type leaves + 1 root;
engine group axioms = 4 (closure/associativity/identity/inverse); 14 AOB atoms under `realm/algebra`,
12 under `subdomain/{group,set,class}`; carrier width lattice = 8 concrete widths (1..128);
0 engine-algebra URN references in `basicttl/foundation/` (bridge is un-built).

GAPS / not fully read (out of shard scope, flagged for other shards or follow-up):
- The 3 non-algebra math AOB atoms beyond group/set/class (category/topology/geometry deep AOBs read
  only via primordials.yaml, not their `aob/urn/.../atom.spec.yaml` bytes) — schema is identical
  (Flavor B), so low risk.
- `T/lib/type-dag/type.sh` (`type::inherits`/`type::resolve` internals) read only by reference — the
  DAG resolution mechanics are R-other (type-dag) scope.
- `T/config/type-dag/*.yaml` + `T/config/closure/*.yaml` enumerated but not opened (executor/closure
  contract, not algebra substrate).
- The `.skills/engine/`, `.skills/law/` (beyond pair), `.skills/runtime/` SKILL bodies read only via
  HEAD.yaml SCOPE lines — kingdom taxonomy captured; full law texts (C3, contract, purity) are
  R-other scope.
- `basicttl/foundation/algebra_rings.ttl` / `spaces.ttl` / `functionality.ttl` fnd: rung bodies read
  only for rung NAMES (bridge endpoints) — their internal shape is R-other (fnd:-floor) scope.
