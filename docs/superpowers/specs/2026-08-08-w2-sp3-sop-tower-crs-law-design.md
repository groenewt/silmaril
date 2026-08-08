# W2 · Sub-project 3 — the S/O/P-tower CRS law (design)

> **Batch design doc** (superpowers:brainstorming output, Directive 14 cadence: authored
> up front with SP2/SP4–SP9, presented for one maintainer review pass; no per-project
> Socratic gate). Design-only — NO `.ttl`/`.sparql`/implementation authored here.
> **THIS ITERATION's v1** — corpus-agnostic (zero live-corpus binding; that is the
> re-runnable W5), built to be re-run and relaunched, not to be permanent (Directive 13).
> **LIFTED, not invented (Directive 1):** the whole geometry is lifted from
> `helios/srcy/base/00_whitepaper/sections/00_helios_foundation/05_carrier_towers_triad.tex`
> (the S/O/P + Atlas/Graph carrier source) and
> `helios/srcy/shared/components/diagrams/patterns/projection/source_dimension_planes.tex`
> (the `z`/SHA-256 identity idiom + the `S:P:O`↔`S:O:P` order effect). Every asserted law
> below names the authored structure it materialises.

**Goal.** Author the N-dimensional Coordinate Reference System (CRS) law *realized as the
Subject/Object/Predicate URN towers* — where the Helios carrier triad is materialised as
teeth-bearing graph structure: (a) **three INDEPENDENT tower categories** `K_S, K_O, K_P`
(with the Atlas/Graph carrier categories `K_A, K_G` beside them), (b) the **disjoint**
Atlas/Graph byte carriers `Q_A ∩ Q_G = ∅`, (c) the **per-geometer quark grid** that sits
BELOW the towers (each geometer fixes its own dimension via its atlas glossary — "we cannot
jump to towers"), (d) **coordinates DERIVED, not stored** (worked example: `z` = a `uint16`
over the first two octets of `source_sha256`, where `source_sha256` is the SHA-256 of the
UTF-8 bytes of one canonical URN, endianness selected by the `byte_order` progenitor), and
(e) the binding SHACL law **coordinate-count == dimension PER-GEOMETER** (the W4 blocking
gate "chart coord-count==dimension").

**Binding sources** (gospel): `docs/unary-byte-frame-law.md` (S/O/P nth-dim tower amendment;
byte-stream carrier closure), `docs/praeriehund-demokratie-der-kategorien.md`,
`ledger/W2/design_constraints.md` (Directives 1–14), the committed **SP1 floor**
(`basicttl/primitives/*`) this sub-project grounds on (§5), and the two Helios source `.tex`
above.

---

## 1. The structure to build (three co-equal claims, each lifted)

1. **The role geometry IS three independent towers, never colour.** The whitepaper is
   explicit (`05_carrier_towers_triad.tex` §"Disjoint Carriers"): *"Subject, Object, and
   Predicate live in three other typed towers `𝒦_S, 𝒦_O, 𝒦_P`. There are no implicit
   positional maps `S→R`, `O→G`, `P→B`."* Each role tower is nth-dimensional; the terminal
   drill shows the live S/O/P files each *"descend from `Octet.Pair.Sequence.Value`, each own
   a separate `dimension` value."* SP3 materialises `K_S/K_O/K_P` as first-class carrier
   categories descending into the SP1 octet-vector floor, each carrying its OWN per-geometer
   dimension — and materialises the **positional-collapse obstruction** (the whitepaper's
   proposition + proof) as a biting tooth.
2. **Atlas and Graph are DISJOINT carriers.** `Q_A = {aTag}×RGB×Vec(Oct)`,
   `Q_G = {gTag}×RGB×Vec(Oct)`, `Q_A ∩ Q_G = ∅` even though the untagged payloads are
   isomorphic; erasing the outer tag is a *many-to-one forgetful* map, not equality
   (`05_carrier_towers_triad.tex`, Def. "Project-authored five-factor Helios carrier": no
   cross-tag hom-sets). SP3 carries `Q_A`/`Q_G` as nominally-tagged copies of the RGB
   byte-carrier and proves their disjointness with teeth.
3. **Dimension is PER-GEOMETER; the quark grid sits below the towers.** A geometer (fixed by
   its atlas glossary) declares its own axis system — `a,b` / `x,y` / `x,y,z,w,p` / `S-O-P` —
   and its own dimension; the per-geometer quark grid (`{cat,econ,lang} × {node_or_arrow,
   shape,color}`, lifted from `helios/00_src_specs` `_urn/identity.j2::quark`) is the
   low-order axis layer beneath the towers. "We cannot jump to towers": the five-factor
   product `K = K_A × K_G × K_S × K_O × K_P` is BUILT UP from per-geometer axes, not presumed.
4. **Coordinates are derived, never stored.** Every coordinate is the `frameOutput` of a
   derivation **Frame** (a Kleisli arrow extending SP1's ρ). The canonical case is the
   content-address descent `URN → UTF-8 bytes → SHA-256 → first two octets → uint16 = z`.

---

## 2. Architecture — five-factor carrier product over a per-geometer floor, coordinatised by the Frame monad

### 2.1 The five-factor Helios product `K` (lifted verbatim)

The apex is the whitepaper's declared synthesis (`05_carrier_towers_triad.tex`, Def.
"Project-authored five-factor Helios carrier"):
`K := K_A × K_G × K_S × K_O × K_P`, with product projections `π_j`, `j ∈ {A,G,S,O,P}`.
SP3 reifies each factor as an `owl:Class` and each `π_j` as a first-class projection arrow.
The whitepaper's **"Five projections are jointly faithful"** theorem (`u = v ⇔ π_j u = π_j v`
for every `j`; the five projections also jointly reflect isomorphisms) is materialised as the
**reversibility seal** of the carrier product — the round-trip tooth of §4 is exactly joint
faithfulness made a graph fact. `K_A` and `K_G` are nominally-tagged copies of one RGB
byte-carrier category `B_rgb` (`Ob(K_A) = {aTag}×Ob(B_rgb)`, likewise Graph); there are **no
cross-tag hom-sets** — a `Q_A` object is never a `Q_G` object merely because payloads are
isomorphic.

### 2.2 The disjoint byte carriers (`carriers.ttl`)

Lifted octet-for-octet:

```
Oct        = {0..255}                       -- SP1 prim:Octet (ordinal 0..255)
RGB        = {R,G,B}                         -- three NOMINAL channel constructors; NOT roles
Vec(Oct)   = ∐_{n≥0} Oct^n                   -- finite octet-vector coproduct (retains length coord)
Q_A        = {aTag} × RGB × Vec(Oct)         -- Atlas byte carrier
Q_G        = {gTag} × RGB × Vec(Oct)         -- Graph byte carrier
Q_A ∩ Q_G  = ∅                               -- distinct outer tags ⇒ disjoint carriers
```

`Oct`/`Vec(Oct)` are the SP1 `prim:Octet` and `prim:ByteVector` (byte-descend to `prim:Bit`);
`RGB` is the SP1 RGB code space (`q_rgb`: exactly Red/Green/Blue, each an Octet 0..255) — SP3
consumes it, does not redefine it. The inner colour tag is *"a constructor carried with a
vectorized byte stream; it is not a semantic role"* (verbatim). Tag-erasure `Q_A → Vec(Oct)`
and `Q_G → Vec(Oct)` are typed **forgetful Frames** carrying a typed loss effect (many-to-one)
— seeding SP4's loss classes.

### 2.3 The role towers `K_S/K_O/K_P` and the positional-collapse obstruction (`towers.ttl`)

Each role tower is a **URN tower**: a functor from an ordinal index (SP1 `prim:Ordinal`) into
`prim:URN` (SP1 Identifier tower), whose nth-dim composite is an SP1 `prim:Vector`/`prim:Tensor`
of URN components — never a `prim:Real` scalar (unary law: *"a scalar triple, raw tuple, or
three unrelated URN strings is not an admissible substitute for those towers"*). Each tower
descends from the octet-vector floor (mirroring the live `Octet.Pair.Sequence.Value` descent)
and **owns its own `dimension`** (per-geometer, §2.4).

The **TOWERS positional-collapse obstruction** (whitepaper Prop.
"TOWERS positional-collapse obstruction" + proof) is materialised as a law, not prose: the
three-colour projection `c : D_tower → R × G × B` that retains only colour payloads is
**non-injective** (two inputs differing only in a role-tower or Atlas/Graph coordinate collide
under `c`); therefore `S=R`, `O=G`, `P=B` are **underivable**. SP3 encodes the forbidden maps
as *asserted-absent* edges the SHACL law forbids (§4 `crs:NoPositionalMapShape`): any triple
identifying a role tower with a colour channel → `conforms=False`.

### 2.4 The per-geometer quark grid BELOW the towers (`geometers.ttl`)

"We cannot jump to towers" is the load-bearing discipline. A `crs:Geometer` is fixed by its
**atlas glossary** (the SP6 glossary that names its axes) and declares:

- its **quark grid** — the 3×3 low-order geometer plane `{cat,econ,lang} × {node_or_arrow,
  shape,color}` (lifted from `helios/00_src_specs` `_urn/identity.j2::quark` /
  `helios/01_src_specs` `quark_evidence/0`), the a,b/x,y-style axis layer;
- its **axis system** (nth): `a,b` (rank-1 pair) / `x,y` (planar, e.g. the Honeycomb
  `(x,y)` from `source_dimension_planes.tex`) / `x,y,z,w,p` (5-axis navigation) / `S-O-P`
  (the role-tower geometer);
- its own **`crs:hasDimension`** (`prim:Natural`) = the arity of its axis system, PER-GEOMETER.

The towers `K_S/K_O/K_P` sit ABOVE this grid: a role-tower geometer is the one whose axis
system is `S-O-P`, but a plane geometer (`x,y`) has dimension 2 without ever touching the
towers. The whitepaper's per-Frame perceptual tessellation `𝔗_f = (V_f, E_f, F_f, w_f, ℓ_f,
ε_f)` is the archetype: *dimension is per-Frame/per-geometer*, never a jump straight to S-O-P.

### 2.5 Coordinatization = a Kleisli arrow extending ρ; the `z` descent (`derivation.ttl`)

A `crs:CoordinateDerivation` is a **Frame** in the exact SP1 sense (`prim:frameOutput` +
`prim:frameEffect`), hence a Kleisli arrow of the SP1 realization monad — not a bare function.
Its domain is an SP2 atom identity (what gets coordinatised); its codomain is a tower position
or a derived ordinal. **"Derived, not stored"** is then precise: no atom/point may assert a
literal coordinate; every coordinate is some derivation's `frameOutput`. Per the unary law the
Frame is the Yoneda point, so coordinatization = Yoneda evaluation at the geometer's
representable — reusing SP1's `prim:Frame prim:isYonedaPoint true`, not re-deriving it.

**The `z` derivation, grounded end-to-end** (lifting `source_dimension_planes.tex`'s
*"SHA-256 content digest: 256-bit digest computed from the UTF-8 bytes of one canonical
uniform resource name"*):

```
urn : prim:URN                                   -- one canonical URN (SP1 Identifier tower)
  │  crs:encodeUtf8                              -- URN → UTF-8 octet stream (SP1 charset.utf8)
  ▼
utf8_bytes : prim:ByteVector                      -- the canonical byte string
  │  crs:sha256                                  -- SHA-256 over the UTF-8 bytes
  ▼
source_sha256 : prim:Hash (⊂ prim:Blob)           -- 32 octets, SP1 Binary/Hash tower
  │  crs:takesOctetPrefix 2                       -- first two octets (a prim:Block over the ByteVector)
  ▼
(octet[0], octet[1]) : two prim:Octet             -- ordinal 0..255 each, SP1 physical carrier
  │  interpret as prim:Uint16, byteOrder ∈ byte_order_{little,big,host,none}
  ▼
z : prim:Natural (ordinal 0..65535)               -- the layering coordinate
```

Every hop is an SP1 primitive (`prim:URN`, `prim:ByteVector`, `prim:Hash`→`prim:Blob`,
`prim:Octet`, `prim:Uint16` with `prim:bitWidth 16` / `prim:interpretAs prim:Natural`, the
`prim:byteDescendsTo+ prim:Bit` chain). The **endianness is the `byte_order` progenitor**
(agnostic parent + `little/big/host/none` children, lifted from the AOB prelude family
`types.prelude.byte_order_*` — the maintainer's worked endianness example): which octet is
most-significant is selected by a `byte_order` child, so the derived `z` is
byte-order-explicit, not silently big-endian. The derivation carries a **typed
`crs:HashPrefixTruncation` effect** (only 2 of 32 octets consumed — a genuine loss, minted
because a concrete consumer needs it, per SP1's extensible-Effect discipline).

### 2.6 The `S:P:O` ↔ `S:O:P` order effect (lifted; seeds SP4)

`source_dimension_planes.tex` fixes two distinct orders on one reified arrow-node: the
**rank-zero external order `S:P:O`** and the **internal role order `S:O:P`**. Re-ordering
between them is a *materialised effect/loss between projections* (a content-addressed reified
arrow-node carries "declared orders `S:P:O` / `S:O:P`"). SP3 models the reorder as a typed
`crs:OrderProjection` Frame with a `crs:RoleOrderEffect` — the projection packet (SP4)
consumes it as one loss class. The arrow-node identity itself is the content-address descent of
§2.5 (URN → UTF-8 → SHA-256 → bucket → atom directory), so `z` and the arrow identity share one
floor.

---

## 3. File layout (one file per concern — STRICTNESS Rule 14)

Namespace: `crs: <urn:silmaril:crs:#>` (full-lexical URN idiom, unary law). Long spellings for
new names; `prim:*` consumed as the floor fixed them.

| file | responsibility (the authored structure it materialises) |
|------|----------|
| `basicttl/crs/carriers.ttl` | the disjoint Atlas/Graph byte carriers: `Oct`, `RGB`, `Vec(Oct)`, `Q_A={aTag}×RGB×Vec(Oct)`, `Q_G={gTag}×…`, `Q_A∩Q_G=∅`, no cross-tag hom-sets, tag-erasure forgetful Frames — grounded in SP1 `prim:Octet`/`prim:ByteVector`/RGB |
| `basicttl/crs/towers.ttl` | the three INDEPENDENT tower categories `K_S/K_O/K_P` as nth-dim URN towers (functor `Ordinal→prim:URN`, composite `prim:Vector`/`prim:Tensor`), each descending from the octet-vector floor with its OWN dimension; the positional-collapse obstruction (`S=R/O=G/P=B` underivable) as asserted-absent forbidden maps |
| `basicttl/crs/geometers.ttl` | the per-geometer quark grid BELOW the towers: `crs:Geometer` fixed by its atlas glossary, its 3×3 quark grid, its nth axis system (`a,b`/`x,y`/`x,y,z,w,p`/`S-O-P`), its own `crs:hasDimension`; the five-factor product `K = K_A×K_G×K_S×K_O×K_P` + `π_j` projections + joint-faithfulness seal |
| `basicttl/crs/derivation.ttl` | coordinatization as Frame/Kleisli arrows extending ρ; the `z` descent (`URN→UTF-8→SHA-256→first two octets→uint16`); the `byte_order` progenitor `{little,big,host,none}`; the `S:P:O`↔`S:O:P` `crs:OrderProjection` + typed loss effects |
| `basicttl/crs/crs.shapes.ttl` | SHACL law: coord-count==dimension per-geometer, derived-not-stored, `z`-grounding, carrier-disjointness, no-positional-map (tower/colour independence), Frame-derivation, five-projection round-trip |
| `basicttl/crs/crs.queries.sparql` | the EXPECT-TRUE ASK suite (§4), each with an inline DATA CONTRACT |
| `basicttl/crs/checks/run-crs-checks.sh` + `README.md` | the runner (parse + pyshacl over the merged SP1+SP3 graph + depth gate + every ASK) and the floor doc |

The runner loads the **SP1 four data TTLs + the SP3 data TTLs into one graph** and validates
against `crs.shapes.ttl` **and** re-runs SP1's shapes/ASKs: SP3 adds `owl:Class`es that fall
under SP1's `prim:DualGroundingShape`/`q_universality`, so SP3 is not green unless it keeps the
SP1 floor green (every new carrier/tower/geometer class carries its own `prim:Realization` +
reflexive carrier + `prim:Primitive`).

---

## 4. Verification plan (evidence-first; every asserted law has a biting tooth)

Each shape is RED before authoring, GREEN after; each ASK is `EXPECT-TRUE`, non-vacuous, and
**proven to bite by a documented probe injection** (`True→False` / `conforms=True→False`), in
the SP1 idiom. Depth gate: every `owl:Class` ≥200-char `rdfs:comment` (and every individual a
real comment). Value-type checks use `sh:in`/`sh:sparql`, not range-inference-vacuous
`sh:class` (SP1 defang-proof discipline).

**SHACL shapes (`crs.shapes.ttl`):**
- `crs:DimensionCountShape` (`sh:sparql`) — **the headline law, PER-GEOMETER**: for every
  geometer, the arity of every point's coordinate tuple (and the `crs:hasAxis` count) **equals**
  that geometer's `crs:hasDimension`. *Probe:* an `x,y` geometer point with 3 coordinates, or a
  role-tower (`S-O-P`) geometer declaring dimension 2 → `conforms=False`.
- `crs:CarrierDisjointnessShape` (`sh:sparql`) — `Q_A` and `Q_G` share no object; no cross-tag
  hom-set. *Probe:* one object typed both `Q_A` and `Q_G` (payload-isomorphism sneaking in as
  equality) → `conforms=False`.
- `crs:NoPositionalMapShape` (`sh:sparql`) — no edge identifies a role tower with a colour
  channel (`S=R`/`O=G`/`P=B`), nor a colour with a role. *Probe:* inject `K_S owl:sameAs
  crs:RedChannel` → `conforms=False`. (The materialised positional-collapse obstruction.)
- `crs:DerivedNotStoredShape` — no atom/point carries a literal (xsd) coordinate; every
  coordinate is the `prim:frameOutput` of a `crs:CoordinateDerivation`. *Probe:* a stored
  `xsd:double` coordinate literal → `conforms=False`.
- `crs:ZGroundingShape` (`sh:sparql`) — the `z` derivation's chain is exactly `prim:URN →
  encodeUtf8 → prim:ByteVector → sha256 → prim:Hash → takesOctetPrefix 2 → prim:Uint16
  (bitWidth 16, interpretAs prim:Natural, byteOrder a byte_order child) → prim:Bit descent`.
  *Probe:* a `z` reading 4 octets, interpreting as non-Natural, or omitting the `byte_order`
  child → `conforms=False`.
- `crs:AxisUrnTowerShape` — every role-tower axis is a URN tower (component `prim:URN`,
  composite `prim:Vector`/`prim:Tensor`), never a scalar. *Probe:* an axis whose position is
  `prim:Real` → `conforms=False`.
- `crs:FrameDerivationShape` — every `crs:CoordinateDerivation`/`crs:OrderProjection` carries a
  `prim:frameOutput` AND a `prim:frameEffect` (SP1 Frame law). *Probe:* a derivation missing its
  effect → `conforms=False`.
- **Reused SP1 tooth:** each new carrier/tower/geometer `owl:Class` is under
  `prim:DualGroundingShape`; an ungrounded class flips SP1's `q_universality` false.

**EXPECT-TRUE ASKs (`crs.queries.sparql`):**
`q_dimension_equals_count` (per-geometer litmus), `q_towers_independent` (`K_S/K_O/K_P` each a
URN tower, nth-dim, not scalar, and no positional colour map exists), `q_carriers_disjoint`
(`Q_A∩Q_G=∅`; no cross-tag hom), `q_five_projections_faithful` (`π_j` jointly determine an
arrow of `K` — the round-trip/joint-faithfulness seal), `q_z_from_urn` (`z` descends
`URN→UTF-8→SHA-256→first two octets→Uint16→Natural→Bit` with an explicit `byte_order` child),
`q_coordinates_derived` (every coordinate is a derivation output, none stored),
`q_geometer_below_towers` (each geometer declares its own axis system+dimension; role towers are
a geometer, not a presumed jump), `q_order_effect` (the `S:P:O`↔`S:O:P` reorder is a typed
`crs:OrderProjection` with a loss effect), `q_chart_dual_grounded` (each class dual-grounds into
the SP1 floor over the merged graph).

---

## 5. Interfaces

### Consumes — from SP1 (committed floor), named precisely
- **Byte floor (carriers + `z`):** `prim:Octet` (0..255), `prim:ByteVector`, RGB code space
  (Red/Green/Blue Octets; `q_rgb`), `prim:Hash` (⊂ `prim:Blob`), `prim:Blob`, `prim:Block`,
  `prim:Uint16` (`prim:bitWidth 16`, `prim:interpretAs prim:Natural`), `prim:byteDescendsTo`,
  `prim:Bit`, `prim:Natural`.
- **Identifier tower (S/O/P are URN towers):** `prim:URN`, `prim:URI`, `prim:IRI`.
- **Aggregate/Enum (nth-dim geometry + axis order):** `prim:Vector`, `prim:Tensor`,
  `prim:Tuple`, `prim:Ordinal`.
- **Geospatial seeds (a plane geometer alternative):** `prim:CRS`, `prim:Coordinate`,
  `prim:Latitude`, `prim:Longitude`, `prim:Point`, `prim:Line`, `prim:Polygon`.
- **Realization monad (derivation extends it):** `prim:Realization`, `prim:realizesAs`,
  `prim:encoding`, `prim:frameOutput`, `prim:frameEffect`, `prim:Effect`,
  `prim:PhysicalEncoding`, `prim:interpretAs`, `prim:bitWidth`.
- **Colimit taiji + Yoneda:** `prim:Primitive`, `prim:formalFacet`, `prim:physicalFacet`,
  `prim:gluedBy`, `prim:rhoObject`, `prim:Frame` (`prim:isYonedaPoint true`).
- **SP1 law (kept green):** `prim:DualGroundingShape` / `q_universality`.

### Consumes — from SP2 (AOB meta-ontology, lower in the batch)
- The **AOB atom identity** (the colimit-taiji atom: its URN + `source_sha256` + S/O/P tower
  evidence — the `yoneda_hom_leg`/`typed_hom_triple` `{source_node, target_node, cpo_process}`
  seed) — the *domain of coordinatization*. The `byte_order` prelude progenitor family
  (`types.prelude.byte_order_{little,big,host,none}`) is authored/lifted in SP2's AOB tensor
  layer; SP3 consumes its children for the `z` endianness. Exact class/property spellings are a
  **forward reference, PROVISIONAL** until SP2's design lands in this same batch (Praeriehund;
  §6 Q0). Consistent with Directive 12's SP1→SP2→SP3 ordering.

### Produces — for higher sub-projects
- **SP4 (projection packet):** the tag-erasure forgetful Frames, the `S:P:O`↔`S:O:P`
  `crs:OrderProjection`, and the `crs:HashPrefixTruncation` effect seed the **5 loss classes**;
  the five `π_j` projections are the π_L family.
- **SP5 (file+format taxonomy):** files/formats are coordinatised in these geometers.
- **SP6 (glossary polysemy):** every `crs:Geometer` is *fixed by its atlas glossary* — SP6
  supplies the glossaries that name each geometer's axes; the Atlas ring ordinals ride
  `prim:Ordinal` axes.
- **SP7 (SHACL executable law):** `coord-count == dimension` (per-geometer) is a headline gate
  SP7 aggregates.
- **SP8 (depth remediation):** basicttl individuals get `z`-derived / coordinatised here.
- **SP9 (render seal):** the five-projection joint-faithfulness round-trip is a per-coordinate
  reversibility instance.

---

## 6. Non-goals (this iteration) and genuine open questions

**Non-goals / YAGNI deferrals:** corpus-agnostic — pure shape, **zero corpus instances** (live
coordinate binding is W5); no geodetic/EPSG projection math or datum transforms (the EPSG facet
on `prim:CRS` stays a facet); no perceptual-colour tessellation `𝔗_f` metric/lightness/error
machinery (the whitepaper's `(w_f, ℓ_f, ε_f)` perceptual layer is a *separate stratum* — SP3
models only that dimension is per-Frame, not the metric); `crs:Geometer` glossary *internals*
belong to SP6 (SP3 provides only the CRS mechanism); the `x,y,z,w,p` navigation `n` stays
symbolic until a corpus binds. Built to be relaunched (Directive 13).

**Open questions for the maintainer (flagged, not invented — Praeriehund):**
- **Q0 — SP2 atom-identity handle.** The exact spelling of "the atom that gets coordinatised"
  (and where `source_sha256` / the `byte_order` prelude family formally live) depends on SP2's
  design (same batch). Marked PROVISIONAL; the SP3 plan pins it once SP2 is reviewed.
- **Q1 — `z` byte-order default (load-bearing).** The descent now selects endianness via a
  `byte_order` child rather than assuming big-endian — but the *default* child for the canonical
  `z` (little/big/host/none) is unset. `none` (agnostic, defer to consumer) vs `big` (network
  order) is a real fork; the derived `z` differs. Named, not silently chosen.
- **Q2 — does `crs:hasDimension` count tower-axes or scalar coordinates?** For a role-tower
  (`S-O-P`) geometer, is dimension 3 because there are 3 *tower* axes, or because coordinatising
  yields 3 *scalar* ordinals? This fixes what `crs:DimensionCountShape` counts (`hasAxis`
  tower-arity vs coordinate scalar-arity). A real fork the per-geometer law must pin.
- **Q3 — plane geometer seeds.** Does the 2D plane geometer use `(Subject,Object)` URN-tower
  axes, the geographic `(Longitude,Latitude)` seed, the Honeycomb `(x,y)` render axes, or all
  three as co-existing geometers? The whitepaper seeds all; SP1 provides the geospatial pair.
- **Q4 — cross-tag comparison map.** The whitepaper leaves `χ: Ob(K) → W` (Atlas↔Graph vs an
  external world tuple) an *explicit comparison obligation*, "not forced by shared cardinality
  5." Does SP3 need to model any Atlas↔Graph transition at all this iteration, or is
  disjointness alone (no cross-tag hom) the whole v1 story?
