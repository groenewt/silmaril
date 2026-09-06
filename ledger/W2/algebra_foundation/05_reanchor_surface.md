# 05 — The SP1/SP2/SP3 re-anchor surface (algebra / set-theory / space foundation)

> Brainstorming-gate RESEARCH note (Directive 18). Präriehund honesty throughout: this maps,
> with exact `file:line` evidence, every place a **committed** structure in the three green floors
> (SP1 `basicttl/primitives/`, SP2 `basicttl/aob/`, SP3 `basicttl/crs/`) ALREADY IS an
> algebraic / set-theoretic / space object that should re-anchor onto the new algebra/set-theory
> foundation. It **decides nothing**, authors no `.ttl`, runs no git. Where the source does not
> yet carry a structure the foundation will need, that is marked as a GAP, not force-fit.
>
> Pillar scope: the RE-ANCHOR SURFACE only. The foundation's own depth/sequencing and the Curry
> functionality pillar (Directive 19) are other agents' pillars; this note flags where they touch
> the surface but does not design them.

---

## 0. The one-line finding

The three committed floors are **already algebra-shaped**. SP1's panel-NO-GO remediation and SP3's
T-series both explicitly demanded "algebra-recognizable" carriers/towers/products/groups (design_constraints
Directive 18 last bullet: SP3's panel "now also checks that its carriers/towers/products/groups are
**algebra-SHAPED and ready to re-anchor**"). The consequence is that **re-anchoring is overwhelmingly
ADDITIVE** — it means minting the foundation's magma→abelian-group tower + set/space progenitors and
adding **new grounding edges** (`rdfs:subClassOf` / a new `algfound:groundsInAlgebra` predicate) from the
already-committed structures up into it. **No committed structure needs to be rebuilt.** The two places
that need more than an edge are (a) SP2's `SealedGroup`, which is *called* a "monoid/group OBJECT" but whose
group axioms are only partially materialised (associativity yes, a general binary operation + closure +
two-sided identity/inverse laws as an abelian-vs-nonabelian distinction: no), and (b) the set-theoretic
carriers (Octet, RGB, Vec(Oct)), which are modelled as physical carriers but never as **Sets** with
cardinality/element/function structure — the set-theory bedrock the whole stack is supposed to anchor on
does not exist yet as an object. Those are the two genuine lift-vs-synthesize decisions.

---

## 1. SP1 (`basicttl/primitives/`) — the re-anchor surface

### 1.1 The number type-tower → a SET-THEORETIC inclusion chain of carriers (and a candidate ring/field line)

`basicttl/primitives/formal.ttl`:
- `prim:FormalType` (L30) — the tower apex.
- `prim:Complex` (L36) ⊃ `prim:Real` (L40) ⊃ `prim:Rational` (L44) ⊃ `prim:Integer` (L48) ⊃
  `prim:Natural` (L52) ⊃ `prim:NaturalWithZero` (L56); `prim:Imaginary` ⊂ `prim:Complex` (L64);
  `prim:Bignum` ⊂ `prim:Integer` (L68). This is literally ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ (Directive 8's "what is a number"
  tower), reified as `rdfs:subClassOf` cover edges and proven by `q_number_tower` (README L129).

**Algebraic reading (what it re-anchors as):** each of these carriers is a **SET** (bedrock set-theory
layer) AND the chain ℤ/ℚ/ℝ/ℂ carries the semiring→ring→field→algebraically-closed-field line of Directive
18's "semiring/ring/module/field line where a corpus needs it". `prim:NaturalWithZero` under `+` is a
**commutative monoid**; ℤ is a **commutative ring**; ℚ, ℝ are **fields**; ℂ is an **algebraically closed
field**. NONE of this operational structure is currently authored — the tower is pure *subtyping/inclusion*
(a set-inclusion poset), with no `+`/`×` operation object, no identity element, no closure fact.

**Re-anchor verdict:** ADDITIVE for the *set* layer (add `algfound:Set` grounding edges — the inclusion
chain is already exactly a chain of set inclusions). SYNTHESIZE-NEW for the *ring/field* algebra layer
(the operations do not exist; whether v1 mints them is a foundation-depth decision, below).

### 1.2 The formal olog as a THIN CATEGORY (poset) — already a category object

`formal.ttl`: `prim:SubtypeArrow` (L322), `prim:IdentityArrow` (L326), `prim:CompositeArrow` (L330),
all `rdfs:subClassOf prim:FormalArrow`. README (L45-52): 59 subtype generators + 60 identities + 45
composites, "the induced category is **thin (a poset)** … composition is associative on the nose".

**Algebraic reading:** this is a **category** (objects = the tower classes, arrows = subtyping), and since
it is thin it is exactly a **poset** — a set-theory/order-theory object. It also already witnesses the
category-theory layer the foundation sits under. It re-anchors as "a `Category` / `Poset` in the foundation".

**Re-anchor verdict:** ADDITIVE. The category is materialised with identity + associative composition; the
foundation just needs to name it a Category and the poset a set-with-order.

### 1.3 The physical byte carriers → the SET-THEORY bedrock (finite sets, cardinality)

`basicttl/primitives/physical.ttl`:
- `prim:PhysicalCarrier` (L144); `prim:Bit` (L148); `prim:Octet` (L156, "the unit of the 256-cardinality
  byte and colour code space … ordinal values 0..255 (cardinality 256)"); `prim:Byte` (L160, `Byte ≠ Octet`);
  `prim:ByteVector` (L164).
- `prim:ColourSpace` (L449); `prim:RGB a prim:ColourSpace` (L453); `prim:Red`/`prim:Green`/`prim:Blue`
  each `a prim:Octet` (L457/461/465).

**Algebraic/set-theoretic reading — THIS is the bedrock the whole directive anchors on:**
- `prim:Octet` **is a finite SET of cardinality 256** (the note "cardinality 256 … ordinal 255 … bit width
  128 remain three distinct coordinates" is exactly a set-cardinality-vs-element-ordinal distinction). It
  re-anchors as `algfound:FiniteSet` with `cardinality 256`.
- `prim:RGB` **is a finite SET `{Red,Green,Blue}` of cardinality 3** (Directive 18: "RGB code space → a
  finite set"). Its three elements are already minted as named individuals.
- `prim:ByteVector` under **concatenation** is the **free monoid on `Octet`** (Vec(Oct) = ∐ₙ Octⁿ in the
  Helios source, srcy_map §3 whitepaper §05) — the paradigm Monoid of Directive 18's "byte-vector carrier
  is a monoid under concatenation".
- `prim:Bit` is a finite set of cardinality 2 (the initial bit algebra, unary-byte-frame-law "Byte-Stream
  Carrier Closure": `0↔Zero`, `1↔One`).

**Re-anchor verdict:** ADDITIVE-but-substantive. The carriers exist and are green; what is MISSING is the
**set-theory layer itself** — there is no `algfound:Set`, no `hasCardinality`, no element/membership relation,
no `Monoid`(ByteVector,concat) object. This is the single biggest genuine synthesis: the bedrock the pyramid
rests on is currently implicit in comments ("cardinality 256") rather than a first-class object. Anchoring is
additive (no carrier is rebuilt) but the foundation must MINT the set/monoid objects these carriers ground into.

### 1.4 Space constructs — `prim:CRS` / `prim:Coordinate` / `prim:Vector` / `prim:Tensor`

`formal.ttl`: `prim:Vector a owl:Class ; rdfs:subClassOf prim:List` (L176); `prim:Tensor ⊂ prim:FormalType`
(L180); `prim:Coordinate ⊂ prim:FormalType` (L242); `prim:CRS ⊂ prim:FormalType` (L258);
`prim:Latitude`/`prim:Longitude ⊂ prim:Coordinate` (L262/266); `prim:Ordinal ⊂ prim:Enumeration` (L276).

**Algebraic reading:** these seed Directive 18's **space constructs (topological / metric / vector / normed
spaces)**. `prim:Vector` is present but as a `prim:List` (a sequence), NOT as an element of a **vector space**
(no scalar-field action, no vector-add). `prim:CRS`/`prim:Coordinate` seed the *space* over which coordinates
live but carry no metric/topology. This is the space-construct GAP: the carriers to hang a vector/metric space
off exist, the space objects themselves do not.

**Re-anchor verdict:** ADDITIVE for grounding edges; SYNTHESIZE-NEW for the space-construct objects (vector
space, metric, topology) — a foundation-depth decision.

### 1.5 The realization monad + Yoneda — the arrow/functor layer already present

`realization.ttl` `prim:RealizationTransport` (ρ as a functor on arrows, README L53-65); `taiji.ttl`
`prim:RepresentablePresheaf`/`prim:YonedaArrow`/`prim:NaturalitySquare` + `prim:Frame prim:isYonedaPoint true`
(README L66-88). This is the **functor / natural-transformation / presheaf** layer and the Frame monad
(Kleisli, `prim:KleisliCompositionShape`, monad unit/assoc laws). It is the surface the **Curry functionality
pillar (Directive 19)** re-anchors onto (ρ-functor-on-subtyping-arrows = the §4 variance carrier). Flagged for
that pillar; not designed here. **Verdict: ADDITIVE** (already category-theoretic; the foundation names it).

---

## 2. SP2 (`basicttl/aob/`) — the re-anchor surface

### 2.1 `aob:SealedGroup` — self-described "monoid/group OBJECT" → a Group in the tower (PARTIAL)

`basicttl/aob/group_law.ttl`:
- `aob:SealedGroup a owl:Class` (L46) — comment (L48) **verbatim**: "a **monoid/group OBJECT** whose colimit
  apex is the atom … Its BASE atom IS the group **identity** (`aob:groupIdentity`): each companion **COMPOSES
  ONTO** the identity (`aob:composesOnto`, **associative** — the cocone legs), and **RETRACT is the INVERSE**
  (`aob:retracts`)."
- `aob:groupIdentity` (L53, → the neutral element); `aob:composesOnto` (L58, "associative composition of the
  sealed group"); `aob:retracts` (L63, "The INVERSE of the sealed group … the group inverse");
  `aob:colimitApex` (L73); `aob:Composition` reified table (L362) with `q_group_associativity` enforcing
  `(a·b)·c == a·(b·c)` (README L107).

**Algebraic reading:** this is the clearest re-anchor target in the whole surface — the source *names itself*
a group/monoid. It maps onto the foundation's `Group` (Directive 18's "SP2's `group_law` sealed group IS a
group in this hierarchy"). What IS materialised: an identity element, a composition relation, an inverse
relation (`aob:retracts`, enforced as a genuine inverse per README L20-22), and **associativity** over a
reified `aob:Composition` table.

**Präriehund gap (do NOT overclaim it is already a Group):** the group axioms are only *partially* present.
`aob:composesOnto` is a **companion→identity** cocone-leg relation, NOT a general **binary operation
`G×G→G`**; there is no **closure** fact, no **totality** of the operation, and the two-sided identity/inverse
laws are stated in prose but the SHACL only checks "companions compose onto the identity" + "retract is a real
atom" + associativity of the reified table. So it is a **monoid-with-inverses SHAPED object**, genuinely
associative, but the full group law (`∀a∃a⁻¹: a·a⁻¹ = e = a⁻¹·a` as a materialised universal) and the
**AbelianGroup vs Group** commutativity distinction (Directive 18's `Group → AbelianGroup` with "all in
between") are NOT there. The magma→semigroup→monoid→group ladder that the foundation must place this on does
not exist yet either — `SealedGroup` currently sits directly under `owl:Class`, not under a `Monoid`/`Group`
progenitor.

**Re-anchor verdict:** ADDITIVE for the edge (add `aob:SealedGroup rdfs:subClassOf algfound:Group` once the
tower exists), but SYNTHESIZE-NEW for the tower it hangs from AND for the missing axiom teeth if the foundation
wants `SealedGroup` to *prove* it is a group (binary-op object, closure, two-sided inverse universal,
commutativity flag). **Effort: medium** — the hardest single item, because the maintainer's directive singles
this out ("its `group_law` sealed group IS a group in this hierarchy") so the re-anchor is expected to be
load-bearing, not cosmetic.

### 2.2 `aob:HashDigest` — a fixed-length product / 32-fold power of the Octet set

`basicttl/aob/octet_descent.ttl`: `aob:HashDigest a owl:Class` (L35, "a `prim:ByteVector` of exactly 32
`prim:Octet`s … byte-descending to `prim:Bit`"); `aob:zSeed` (L62, the first two octets → `prim:Uint16`).

**Algebraic/set-theoretic reading:** a 32-octet digest is an element of **Octet³² = the 32-fold Cartesian
power** of the Octet finite set (a finite product in Set), i.e. a point of a finite product set of cardinality
256³². The `aob:zSeed` is a projection onto the first-two-octet factor (Octet²). Re-anchors as an element of a
finite **product set**. **Verdict: ADDITIVE** (grounding edge to `algfound:FiniteSet`/product once minted).

### 2.3 `aob:ByteOrderProgenitor` + `aob:TensorBlock` — an agnostic progenitor family and a graded/tensor carrier

`basicttl/aob/tensor_block.ttl`: `aob:TensorBlock` (L40, the three-axis space/time/value block);
`aob:ByteOrderProgenitor` (L149) with children `aob:byteOrderLittle` (L153) / `aob:byteOrderBig` (L159) /
`aob:byteOrderNone` (L165) / `aob:byteOrderHost` (L171, `silm:isProvisional`).

**Algebraic reading:** `aob:TensorBlock` (space×time×value) is a **product/graded carrier** that re-anchors on
the space-construct/`prim:Tensor` line. `aob:ByteOrderProgenitor` is the Directive-17 agnostic-progenitor
pattern (a coproduct/disjoint-union of its children in Set) — the very pattern the foundation's magma→group
tower must itself use (each algebra its own atom under an agnostic progenitor, "NEVER crammed"). **Verdict:
ADDITIVE**; also a *template* for how the foundation's own tower should be shaped.

### 2.4 `aob:aobValue : AOBAtom → prim:Primitive` — the bridge that carries SP2 into SP1's set/algebra

`basicttl/aob/value_colimit.ttl` (`aob:aobValue`, README L48-50): every atom's value is an SP1 colimit-taiji
`prim:Primitive`. This is the edge along which SP2 already grounds into SP1's tower; when SP1 re-anchors onto
the foundation, SP2 inherits the anchoring transitively **for free**. **Verdict: ADDITIVE, zero extra work.**

---

## 3. SP3 (`basicttl/crs/`) — the re-anchor surface

### 3.1 The byte-vector carriers → Set/Monoid; the tagged carriers → coproduct + quotient

`basicttl/crs/carriers.ttl`:
- `crs:TaggedByteCarrier` (L63, "agnostic byte-carrier progenitor B_rgb", `{outer-tag}×RGB×Vec(Oct)`);
  `crs:AtlasByteCarrier` = `Q_A = {aTag}×RGB×Vec(Oct)` (L67); `crs:GraphByteCarrier` = `Q_G` (L73);
  `owl:disjointWith` between them (L69/75); `crs:UntaggedBytePayload` (L79, the shared `RGB×Vec(Oct)`);
  `crs:ForgetfulTagFrame a owl:Class ; rdfs:subClassOf prim:Realization` (L83, the "many-to-one tag-erasure
  Kleisli/Frame arrow"); relations `crs:forgetsFrom` (L91) / `crs:forgetsTo` (L97).

**Algebraic/set-theoretic reading:**
- Each carrier is a **product SET** `{tag} × RGB × Vec(Oct)` (a Cartesian product of a singleton tag set, the
  RGB 3-set, and the free monoid Vec(Oct)). `Q_A ∩ Q_G = ∅` is a literal **disjointness of sets** (`owl:disjointWith`).
- `crs:TaggedByteCarrier` as the agnostic parent of two disjoint children is a **coproduct / disjoint union**
  `Q_A ⊔ Q_G` in Set (Directive 18's "products/coproducts/disjoint unions" bedrock).
- `crs:ForgetfulTagFrame` is a **many-to-one forgetful map** onto the shared quotient `crs:UntaggedBytePayload`
  — a set **function** (surjection), authored as a Kleisli arrow of the SP1 Frame monad.
- `Vec(Oct)` inside every carrier is the **free monoid** (§1.3).

**Re-anchor verdict:** ADDITIVE. The set-theory content (product, disjoint union, forgetful function, quotient
image) is fully materialised; the foundation adds edges naming these `algfound:ProductSet`/`Coproduct`/`SetFunction`.
The forgetful map is *already* a function object, not just an assertion.

### 3.2 The S/O/P URN role towers → functors `Ordinal → URN` (graded structures)

`basicttl/crs/towers.ttl`:
- `crs:UrnRoleTower` (L71, "agnostic role-tower progenitor K_*", "a **functor** from an ordinal index
  (SP1 `prim:Ordinal`) into `prim:URN`"); children `crs:SubjectTower` K_S (L75), `crs:ObjectTower` K_O (L80),
  `crs:PredicateTower` K_P (L85), each `descendsFromOctetVector → prim:ByteVector`.
- `crs:UrnTowerAxis` (L93, component `prim:URN`, composite `{prim:Vector, prim:Tensor}`).
- The positional-collapse obstruction: `crs:ColourChannel` (L323) + `crs:Red/Green/BlueChannel` (L327/333/339)
  + `crs:ColourOnlyProjection` (L348) — the non-injective map proving `S=R`/`O=G`/`P=B` is underivable.

**Algebraic reading:** each role tower is a **functor** (`prim:Ordinal → prim:URN`) whose composite is a
`prim:Vector`/`prim:Tensor` — a **graded structure** (Directive 18: "the role towers are graded structures").
Anchors as functor objects into the identifier tower. The colour channels are a separate finite set (`prim:RGB`
re-used), deliberately non-identified with the role towers — a set-theoretic non-isomorphism the floor proves.

**Re-anchor verdict:** ADDITIVE. Functors are already reified; the foundation names the graded/functor layer.

### 3.3 The five-factor product K → a CATEGORICAL PRODUCT (with joint-faithfulness = the universal property)

`basicttl/crs/geometers.ttl`:
- `crs:CarrierProduct` (L560, "the five-factor Helios product category **K = K_A × K_G × K_S × K_O × K_P**",
  "the **categorical product** of Atlas Graph Subject Object and Predicate carrier towers", "the APEX of the
  SP3 floor").
- `crs:ProductArrow` (L564, "an arrow in a product category is exactly its five-tuple of component arrows");
  `crs:FactorComponentArrow` (L568); the projections `crs:FactorProjection` πⱼ (L575) with children
  `crs:CarrierTagProjection` π_A/π_G (L579) and `crs:RoleTowerProjection` π_S/π_O/π_P (L584).
- Joint faithfulness = the universal property of the product, enforced by `crs:FiveProjectionShape`
  (README L121, "5 πⱼ jointly faithful").

**Algebraic/categorical reading:** this is a **categorical product** with its five projection morphisms and a
joint-faithfulness (the product's universal-property mediating-uniqueness) seal — Directive 18's "the
five-factor K is a product". Fully materialised: product object, five projections, componentwise-equality
proof. **Verdict: ADDITIVE** — arguably the cleanest re-anchor: it is *already* a product with projections.

### 3.4 The geometers, planes, and role-pair family → rank/dimension objects (space geometry)

`basicttl/crs/geometers.ttl`: `crs:Geometer` (L76, agnostic, `crs:hasDimension` = axis arity), `crs:RoleGeometer`
rank-3 (L80), `crs:QuarkGridGeometer` rank-2 3×3 (L85); `crs:PlaneGeometer` (L277) with `crs:HoneycombPlaneGeometer`
(L282, x,y) / `crs:GeographicPlaneGeometer` (L287, lon,lat → SP1 `prim:CRS`/`prim:Latitude`/`prim:Longitude`);
the symmetric `crs:RolePairProjectionPlane` (L292) family `SubjectObjectPlane`/`SubjectPredicatePlane`/
`ObjectPredicatePlane` (L297/302/307); `crs:RoleDropEffect` (L312).

**Algebraic reading:** geometers are **finite-dimensional coordinate spaces** (rank = `crs:hasDimension`
= axis arity); the geographic plane anchors on `prim:CRS` — the **space-construct** line. Re-anchors on the
foundation's space constructs (a coordinate/affine space over the carrier sets). **Verdict: ADDITIVE for the
edge; the metric/topology of these spaces is the same space-construct GAP as §1.4.**

### 3.5 Coordinatization as Frame + the z-descent → functions/Kleisli arrows (derived, not stored)

`basicttl/crs/derivation.ttl`: `crs:CoordinateDerivation a owl:Class ; rdfs:subClassOf prim:Realization`
(L65, "coordinatization = a Frame / Kleisli arrow extending ρ"); `crs:CoordinatePoint` (L70, derived-not-stored);
`crs:zByteOrderCoordinate` (L200, z from the sha256 prefix, grounded in `aob:ByteOrderProgenitor`);
`crs:OrderProjection` (L302) + `crs:RoleOrderEffect` (L307, the S:P:O↔S:O:P reorder loss);
`crs:chiComparisonObligation` (L391, the honest-red χ deferral, `silm:isProvisional`).

**Algebraic reading:** coordinate derivations are **set functions / Kleisli arrows** (already `prim:Realization`
subclasses, so already Frame-monad-anchored). The order projection is a **permutation action** (S:P:O↔S:O:P) on
the role index set carrying a typed loss. **Verdict: ADDITIVE** (already arrow objects); the χ obligation stays
an honest-red deferral, untouched.

---

## 4. Summary table — re-anchor surface, algebra class, additive vs rebuild, effort

| # | Committed structure (file:line) | Re-anchors as (foundation object) | Additive / Rebuild | Effort |
|---|---|---|---|---|
| S1 | `prim:Octet` (physical.ttl:156), `prim:RGB`+Red/Green/Blue (449/453/457-465), `prim:Bit` (148) | **finite Set** (card 256 / 3 / 2) — the set-theory bedrock | Additive edge; MINT the Set objects | med (bedrock must be authored) |
| S2 | `prim:ByteVector` (physical.ttl:164) under concat | **Monoid** (free monoid on Octet) = Vec(Oct) | Additive edge; MINT Monoid object | med |
| S3 | number tower `prim:Natural…prim:Complex` (formal.ttl:36-68) | Set-inclusion chain; commutative-monoid/ring/field line | Additive (set); synth (ring/field ops) | low→high by depth |
| S4 | formal thin category `prim:SubtypeArrow`… (formal.ttl:322-330) | **Category / Poset** | Additive | low |
| S5 | `prim:Vector`/`prim:Tensor`/`prim:CRS`/`prim:Coordinate` (formal.ttl:176-266) | seeds **vector / metric / topological space** | Additive edge; synth space objects | med→high |
| A1 | `aob:SealedGroup` +group_law props (group_law.ttl:46-76,362) | **Group** (Directive 18 names it) — PARTIAL axioms | Additive edge; SYNTH tower + missing axiom teeth | **med (load-bearing)** |
| A2 | `aob:HashDigest` 32×Octet (octet_descent.ttl:35) | element of finite **product/power set** Octet³² | Additive | low |
| A3 | `aob:ByteOrderProgenitor`+children (tensor_block.ttl:149-171); `aob:TensorBlock` (40) | **coproduct** / agnostic progenitor; graded/tensor carrier | Additive | low |
| A4 | `aob:aobValue → prim:Primitive` (value_colimit.ttl) | inherits SP1 anchoring transitively | Additive, zero work | none |
| C1 | `crs:TaggedByteCarrier`/`Q_A`/`Q_G`/disjoint (carriers.ttl:63-77) | **product set** + **coproduct/disjoint union** | Additive | low |
| C2 | `crs:ForgetfulTagFrame`+forgetsFrom/To (carriers.ttl:83-100) | **set function** (surjection) onto quotient | Additive | low |
| C3 | `crs:UrnRoleTower`/K_S/K_O/K_P (towers.ttl:71-88) | **functors** `Ordinal→URN` = graded structures | Additive | low |
| C4 | `crs:CarrierProduct` K + πⱼ + joint-faithfulness (geometers.ttl:560-587) | **categorical product** w/ universal property | Additive | low |
| C5 | geometers/planes/role-pairs (geometers.ttl:76-312) | finite-dim coordinate **spaces** | Additive edge; space metric = GAP | med |
| C6 | `crs:CoordinateDerivation`/z/OrderProjection (derivation.ttl:65-307) | Kleisli **functions** / permutation action | Additive | low |

**Net:** 15 of 16 rows are ADDITIVE (new grounding edges, nothing rebuilt). The one row needing real new
teeth is **A1 (`aob:SealedGroup`)**; the recurring synthesis obligations are the **Set/Monoid bedrock objects**
(S1/S2) and the **space-construct objects** (S5/C5) — none of which *rebuild* a committed structure; they
author the foundation the edges point at.

---

## 5. Lift-vs-synthesize gaps (Präriehund — honest, not force-fit)

1. **The set-theory bedrock is IMPLICIT, not an object (GAP, must synthesize).** Directive 18 makes *set
   theory* the deepest anchor (sets, elements, functions, relations, products/coproducts, power sets,
   ordinals/cardinals). The floors USE set structure everywhere (Octet cardinality 256, RGB as a 3-set,
   Q_A∩Q_G=∅, forgetful functions, 32-fold powers) but there is **no `algfound:Set`, no membership relation,
   no cardinality object, no product/coproduct object** authored. Can it be LIFTED from Helios? The srcy_map
   shows the Helios source defines `Oct={0..255}`, `RGB={R,G,B}`, `Vec(Oct)=∐ₙ Octⁿ` as sets in
   `00_helios_foundation/05_carrier_towers_triad.tex` (srcy_map §3) — so the *set-theoretic framing is
   liftable from source*, it simply was not re-derived as TTL objects yet. **Decision for the maintainer:
   how deep does the v1 set-theory layer go** (bare Set+cardinality+function, vs. full products/coproducts/
   power-sets/ordinals)?

2. **The magma→abelian-group tower does not exist (GAP, must synthesize; LIFT depth TBD).** Directive 18
   demands `Magma → Semigroup → Monoid → Group → AbelianGroup` with "all in between" (Quasigroup, Loop,
   CommutativeMonoid, +semiring/ring/module/field). NONE of these classes exist in any committed floor.
   `aob:SealedGroup` is the only group-shaped object and it sits under `owl:Class`, not under a `Group`
   progenitor. **This is pure synthesis** — but the *shape* to author it in is already lifted (the
   agnostic-progenitor pattern, §2.3, Directive 17). Präriehund: I did NOT find a magma/semigroup/monoid
   ladder anywhere in the Helios srcy_map either (the papers carry `path_monoids` Vol 31 and
   `free_monoid` in whitepaper §02 — a Monoid IS liftable — but the full magma→abelian ladder is not
   authored in the source I have mapped). So "all in between" is **partly liftable (Monoid via Vol 31 +
   whitepaper §02_ecosystem_free_monoid; Group via the sealed-group), partly genuine new construction**.

3. **`aob:SealedGroup` is a monoid-with-inverses, not yet a proven Group (GAP in axioms).** As detailed
   §2.1: associativity + identity + a genuine inverse are materialised, but there is no general binary
   operation object, no closure/totality tooth, and no abelian-vs-non-abelian commutativity distinction.
   If the foundation wants "SP2's group_law IS a Group" to be a *teeth-proven* re-anchor (not a bare
   `subClassOf` edge), the operation/closure/two-sided-universal teeth must be synthesized. **Lift source:
   the group axioms are standard math (liftable as fact, cf. Directive 19's Curry paper precedent for
   "mathematics is fact and liftable"); no Helios paper is required to author them.**

4. **Space constructs (topological/metric/vector/normed) are seeded but absent (GAP).** `prim:Vector`
   (as a List), `prim:CRS`, `prim:Coordinate`, `crs:PlaneGeometer`/`crs:GeographicPlaneGeometer` seed the
   space layer, but no vector-space (scalar action + vector add), metric, or topology object exists.
   Präriehund: the srcy_map does NOT surface a vector-space/metric/topology paper — Helios's "space" content
   is the carrier-tower geometry, not normed/metric spaces — so this layer is **largely genuine synthesis,
   weakly lift-supported**. Flag: how far does v1 go on spaces?

5. **The Curry functionality/typing pillar (Directive 19) touches SP1's ρ-functor + Frame but is a
   SEPARATE pillar.** The re-anchor surface for it is `realization.ttl`'s `RealizationTransport` (functor on
   arrows) + `taiji.ttl`'s Yoneda/Frame apparatus (§1.5). I flag the surface; the arrow/typing tower + §4
   variance + §5 implication-taiji + §6 quarantine are that pillar's design, not this note's.

---

## 6. Design decisions this pillar raises for the maintainer

- **D1 — Sequencing (the gate's central question, Directive 18).** Because 15/16 surface items re-anchor
  **additively** (new grounding edges, no rebuild), the evidence strongly favors **re-anchor-in-place after
  the foundation lands** over "rebuild the floors on it". The only item needing new teeth (`aob:SealedGroup`,
  A1) is additive too (add axioms + a `subClassOf algfound:Group` edge). Recommendation to put to the
  maintainer: **land the foundation as a new deepest floor `basicttl/algfound/`, then add grounding edges
  from SP1/SP2/SP3 — do not rebuild.** (Decision is the maintainer's; this is the surface evidence for it.)

- **D2 — v1 depth of the set-theory bedrock (Gap 1).** Minimal (Set + cardinality + function/relation +
  binary product/coproduct — exactly what the surface already USES) vs. full (power sets, ordinals/cardinals
  as objects, pullbacks). The surface only *requires* Set+cardinality+function+product+coproduct+disjointness
  to anchor everything mapped above; anything beyond that is speculative for this corpus-agnostic v1.

- **D3 — v1 depth of the algebra tower (Gap 2).** Does v1 author the whole `Magma→…→AbelianGroup` ladder
  "with all in between" as agnostic-progenitor atoms (Directive 17), or only the rungs the surface actually
  hangs on — **Monoid** (ByteVector/Vec(Oct), lift-supported by Vol 31 + whitepaper §02) and **Group**
  (`aob:SealedGroup`)? The surface only *demands* Monoid + Group + (for the number tower) the ring/field
  line; the intermediate rungs (Quasigroup/Loop/Semigroup) have no current consumer.

- **D4 — Whether `aob:SealedGroup` re-anchor is teeth-proven or edge-only (Gap 3).** If the maintainer wants
  "the group_law sealed group IS a group" enforced (not asserted), A1 needs the binary-operation/closure/
  two-sided-universal/commutativity teeth synthesized. This is the single largest build item on the surface.

- **D5 — v1 depth of space constructs (Gap 4).** Given weak lift support, does v1 mint vector/metric/topological
  spaces at all, or defer them (honest-red) to the re-runnable W5, keeping only the seeds (`prim:CRS`,
  `prim:Vector`, geometers) as-is? The surface functions today without them.

- **D6 — one predicate or `rdfs:subClassOf`?** Additive re-anchoring can be either a new
  `algfound:groundsInAlgebra` object property (keeps the algebra grounding inspectably separate from the
  subtyping tower, mirrors SP1's `interpretAs`/`realizesAs` discipline) or plain `rdfs:subClassOf` edges into
  the tower. Recommend the former for the carriers→Set/Monoid edges (a carrier is not a *subtype* of a Set,
  it IS one under a forgetful grounding — same shape as `ForgetfulTagFrame`), and `rdfs:subClassOf` only where
  a genuine is-a holds (e.g. `aob:SealedGroup rdfs:subClassOf algfound:Group`). Maintainer's call.

---

## 7. Coverage statement (Präriehund)

- **Read IN FULL:** the 4 mandatory governing-law files (design_constraints, JUNGLE_MAP, STRICTNESS_RULES,
  unary-byte-frame-law, praeriehund doctrine); the srcy_map; the three floor READMEs
  (primitives/aob/crs); `group_law.ttl` L40-169 (the sealed-group core + witnesses); `carriers.ttl` L62-101;
  `towers.ttl` L70-101; `geometers.ttl` L559-588 (the product) + class index L75-312;
  `derivation.ttl` L65-76 + class index.
- **Read by targeted grep + spot-read (class heads + line-anchored):** `formal.ttl` number tower + arrows +
  space classes; `physical.ttl` Bit/Octet/Byte/ByteVector/RGB; `octet_descent.ttl` HashDigest/zSeed;
  `tensor_block.ttl` ByteOrderProgenitor family; `crs` colour-channel obstruction + OrderProjection/χ.
- **NOT re-read in full (relied on README + srcy_map, flagged):** `realization.ttl`/`taiji.ttl` bodies
  (Yoneda/monad — the Curry pillar's surface, not this pillar's to design); `dual_grounding.ttl` (192 KB,
  the T11 punning that already re-grounds crs chart classes into SP1 — confirmed present via crs README
  L61-66, not re-walked); the SHACL shapes bodies (teeth are documented in the READMEs' probe registers).
- **Honest limits:** the magma→group ladder and space-construct absence (Gaps 2, 4) are stated from the
  committed floors + srcy_map; I did not exhaustively re-read all 34 Helios papers to rule out a
  magma/metric-space paper — the srcy_map (read in full) surfaces `path_monoids` (Vol 31) and free-monoid
  (whitepaper §02) but no magma-ladder or metric/vector-space paper, which is the basis for "partly
  liftable, partly synthesis". Flagged rather than asserted.
