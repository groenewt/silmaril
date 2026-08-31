# W2 · SP3 — the S/O/P-tower CRS law (plan)

> **superpowers:writing-plans output.** Executes the SP3 design
> (`docs/superpowers/specs/2026-08-08-w2-sp3-sop-tower-crs-law-design.md`) with the five open
> questions **resolved and pinned** (ledger Directive 17). Bite-sized, independently-testable,
> test-first (RED→GREEN), zero placeholders. Corpus-agnostic v1 (Directive 13). Every asserted
> law has a **biting tooth proven by probe injection** (conforms/ASK True→False), never by
> absence. Every `owl:Class` ≥200-char `rdfs:comment`. LIFT from Helios + the committed SP1/SP2
> floors; never invent (Directive 1). Namespace `crs: <urn:silmaril:crs:#>`.

## Pinned resolutions (Directive 17 — gospel for every task)
- **Q0** domain of coordinatization = `aob:AOBAtom` (→`aob:ConcreteAnchor`/`aob:YonedaHomLeg`);
  value bridge `aob:aobValue → prim:Primitive`; content address = **class** `aob:HashDigest` via
  `aob:hasHashDigest` (32 `prim:Octet`, `aob:zSeed → prim:Uint16` already materialised); S/O/P
  triple = `aob:sourceNodeUrn`(S)/`aob:targetNodeUrn`(O)/`aob:cpoProcessIri`(P), all `xsd:string`
  — **SP3 bridges string→`prim:URN` itself**.
- **Q1 / z byte-order** = the **agnostic `aob:ByteOrderProgenitor`**, NO concrete leaf in v1;
  concrete endianness deferred to W5. `crs:ZGroundingShape` permits the ungrounded progenitor as
  the v1 default. `none`/`big` both rejected (category error / no floor basis).
- **Q2** `crs:hasDimension` counts **tower-axes** (`crs:hasAxis` arity), never scalars; S-O-P = 3.
- **Q3** agnostic `crs:PlaneGeometer` progenitor (dim 2) + `crs:HoneycombPlaneGeometer` (x,y) +
  `crs:GeographicPlaneGeometer` (lon,lat) + agnostic `crs:RolePairProjectionPlane` sub-progenitor
  with the **symmetric** family (S,O)/(S,P)/(O,P) — no role pair privileged; S-O-P stays a rank-3
  sibling. "Be more agnostic/progenitor on all."
- **Q4** SP3 does **NOT** model χ or any Atlas↔Graph transition; disjointness + the forgetful
  tag-erasure Frame is the whole v1 story; χ recorded only as an **honest-red deferral marker**.

## Interfaces

### Consumes — SP1 (committed floor, kept green over the merged graph)
`prim:Octet` (0..255), `prim:ByteVector`, RGB code space (Red/Green/Blue Octets; `q_rgb`),
`prim:Hash`⊂`prim:Blob`, `prim:Block`, `prim:Uint16` (`prim:bitWidth 16`,
`prim:interpretAs prim:Natural`, `prim:byteOrder prim:LE`), `prim:byteDescendsTo`+`prim:Bit`,
`prim:Natural`; `prim:URN`/`prim:URI`/`prim:IRI`; `prim:Vector`/`prim:Tensor`/`prim:Tuple`/
`prim:Ordinal`; `prim:CRS`/`prim:Coordinate`/`prim:Latitude`/`prim:Longitude`/`prim:Point`/
`prim:Line`/`prim:Polygon`; `prim:Realization`/`prim:realizesAs`/`prim:encoding`/
`prim:frameOutput`/`prim:frameEffect`/`prim:Effect`/`prim:PhysicalEncoding`/`prim:interpretAs`/
`prim:bitWidth`; `prim:Primitive`/`prim:formalFacet`/`prim:physicalFacet`/`prim:gluedBy`/
`prim:rhoObject`/`prim:Frame` (`prim:isYonedaPoint true`); the SP1 law
`prim:DualGroundingShape`/`q_universality`.

### Consumes — SP2 (committed floor)
`aob:AOBAtom`/`aob:ConcreteAnchor`/`aob:YonedaHomLeg`; `aob:aobValue`(→`prim:Primitive`);
`aob:hasHashDigest`→`aob:HashDigest`, `aob:digestOctet`/`aob:octetPosition`/`aob:octetValue`,
`aob:zSeed`(→`prim:Uint16`)/`aob:zSeedValue`; `aob:ByteOrderProgenitor` +
`aob:byteOrderLittle`/`aob:byteOrderBig`/`aob:byteOrderNone`/`aob:byteOrderHost`,
`aob:groundsInByteOrder`, `aob:ttByteOrder`; `aob:sourceNodeUrn`/`aob:targetNodeUrn`/
`aob:cpoProcessIri`; `aob:CircuitImprintTensor`/`aob:hasCircuitImprint`.

### Produces — for higher sub-projects
SP4: the tag-erasure forgetful Frames, the `crs:OrderProjection`+`crs:RoleOrderEffect`, the
`crs:HashPrefixTruncation` effect, and the five `π_j` (the π_L family). SP5: the geometers files
are coordinatised in. SP6: each `crs:Geometer` is fixed by its atlas glossary (SP6 supplies them).
SP7: `coord-count==dimension` per-geometer is a headline gate. SP8: individuals get z-derived.
SP9: five-projection joint-faithfulness = per-coordinate reversibility.

## File map (one file per concern — STRICTNESS Rule 14)
| file | responsibility |
|------|----------------|
| `basicttl/crs/carriers.ttl` | disjoint Atlas/Graph byte carriers `Q_A`/`Q_G` (`Q_A∩Q_G=∅`, no cross-tag hom), tag-erasure forgetful Frames — grounded in SP1 `prim:Octet`/`prim:ByteVector`/RGB |
| `basicttl/crs/towers.ttl` | `K_S/K_O/K_P` as nth-dim URN towers (functor `prim:Ordinal→prim:URN`, composite `prim:Vector`/`prim:Tensor`), bridging SP2's `xsd:string` S/O/P triple → `prim:URN`, each with its own dimension; the positional-collapse obstruction (`S=R`/`O=G`/`P=B` forbidden) |
| `basicttl/crs/geometers.ttl` | per-geometer quark grid; `crs:Geometer` (atlas-glossary-fixed, axis system, `crs:hasDimension`); the agnostic `crs:PlaneGeometer` progenitor family (Q3); the five-factor product `K`+`π_j`+joint-faithfulness seal |
| `basicttl/crs/derivation.ttl` | coordinatization as Frame/Kleisli (ρ ext.); the `z` descent + agnostic `aob:ByteOrderProgenitor` (Q1); the `S:P:O`↔`S:O:P` `crs:OrderProjection`+loss effects; χ honest-red deferral marker (Q4) |
| `basicttl/crs/crs.shapes.ttl` | the SHACL law (all shapes below) |
| `basicttl/crs/crs.queries.sparql` | the EXPECT-TRUE ASK suite, each with an inline DATA CONTRACT |
| `basicttl/crs/checks/run-crs-checks.sh` + `README.md` | runner (parse SP1+SP2+SP3 into one graph → pyshacl vs `crs.shapes.ttl` + re-run SP1/SP2 shapes+ASKs + depth gate + every crs ASK) and the floor doc |

The runner loads **SP1 four data TTLs + SP2 seven data TTLs + the SP3 data TTLs into one graph**;
SP3 is not green unless SP1 and SP2 stay green (every new class dual-grounds under SP1's
`prim:DualGroundingShape`/`q_universality`).

## Tasks (test-first; each = one biting tooth)

**T1 — scaffold + merged-graph runner.** Create `basicttl/crs/` + `checks/run-crs-checks.sh`
(parse SP1+SP2+SP3 → pyshacl over merged graph vs `crs.shapes.ttl` + re-run SP1 `run-floor-checks`
and SP2 `run-aob-checks` invariants + `scripts/ontology-depth-check.py basicttl/crs` + every crs
ASK) + empty `crs.shapes.ttl`/`crs.queries.sparql`/`README.md`. **RED→GREEN:** runner executes and
reports GREEN on the empty crs graph with SP1+SP2 still green. **Probe:** break the runner's SP1
load path → runner reports RED (proves it actually re-validates the floors).

**T2 — `carriers.ttl` disjoint Atlas/Graph.** `crs:AtlasByteCarrier` `Q_A={aTag}×RGB×Vec(Oct)`,
`crs:GraphByteCarrier` `Q_G={gTag}×RGB×Vec(Oct)` over SP1 `prim:Octet`/`prim:ByteVector`/RGB; no
cross-tag hom; tag-erasure `crs:forgetTag` forgetful Frames (`prim:frameOutput`+`prim:frameEffect`
many-to-one loss). **Tooth:** `crs:CarrierDisjointnessShape` + `q_carriers_disjoint`. **Probe:** one
object typed both `crs:AtlasByteCarrier` and `crs:GraphByteCarrier` → `conforms=False`.

**T3 — `towers.ttl` three independent URN towers.** `crs:SubjectTower`/`crs:ObjectTower`/
`crs:PredicateTower` as functors `prim:Ordinal→prim:URN`, composite `prim:Vector`/`prim:Tensor`,
descending from the octet-vector floor, each with its own `crs:hasTowerDimension`; a
`crs:bridgesLexToUrn` Frame lifting SP2's `xsd:string` `aob:sourceNodeUrn`/`aob:targetNodeUrn`/
`aob:cpoProcessIri` onto the `prim:URN` tower (the unary full-lexical idiom). **Tooth:**
`crs:AxisUrnTowerShape` + `q_towers_independent`. **Probe:** a tower axis position typed
`prim:Real` (scalar) → `conforms=False`.

**T4 — `towers.ttl` positional-collapse obstruction.** The forbidden identifications `S=R`/`O=G`/
`P=B` (and colour→role) as the law's negative space; the three-colour projection `crs:colourOnly`
declared non-injective. **Tooth:** `crs:NoPositionalMapShape`. **Probe:** inject
`crs:SubjectTower owl:sameAs crs:RedChannel` → `conforms=False`.

**T5 — `geometers.ttl` per-geometer floor + dimension law.** `crs:Geometer` fixed by an atlas
glossary (`crs:fixedByGlossary`, SP6 forward-ref PROVISIONAL), its 3×3 quark grid
`{cat,econ,lang}×{node_or_arrow,shape,color}` (lifted `_urn/identity.j2::quark`), its axis system
(`crs:hasAxis`), its own `crs:hasDimension` (`prim:Natural`). **Tooth:** `crs:DimensionCountShape`
(`sh:sparql`, per-geometer `count(crs:hasAxis)==crs:hasDimension`, counting **tower-axes not
scalars** per Q2) + `q_dimension_equals_count` + `q_geometer_below_towers`. **Probe:** an (x,y)
geometer with 3 axes, or a S-O-P geometer declaring dimension 2 → `conforms=False`.

**T6 — `geometers.ttl` agnostic plane-geometer progenitor family (Q3).** Agnostic
`crs:PlaneGeometer` (dim 2, **grounds nothing**) with children: `crs:HoneycombPlaneGeometer` (axes
(x,y), source-attested), `crs:GeographicPlaneGeometer` (axes `prim:Longitude`/`prim:Latitude` over
`prim:CRS`), and agnostic `crs:RolePairProjectionPlane` sub-progenitor (grounds nothing) with the
**symmetric** children `crs:SubjectObjectPlane` (π_S,π_O) / `crs:SubjectPredicatePlane` (π_S,π_P) /
`crs:ObjectPredicatePlane` (π_O,π_P), each a lawful projection off the rank-3 S-O-P role geometer
(each drops one role — a `crs:RoleDropEffect` seeding SP4). **Tooth:** `crs:PlaneProgenitorShape`
(the progenitor + each sub-progenitor grounds no concrete axis; every concrete plane child has
**exactly 2** `crs:hasAxis`; the role-pair family is symmetric — no pair privileged/missing) +
`q_plane_progenitor_symmetric`. **Probe:** a plane child with 3 axes, OR the progenitor carrying a
concrete axis, OR a role-pair family missing one of the three symmetric planes → `conforms=False`.

**T7 — `geometers.ttl` five-factor product + joint faithfulness.** `crs:CarrierProduct`
`K=K_A×K_G×K_S×K_O×K_P` with five `crs:projectsBy` arrows `π_j` (j∈{A,G,S,O,P}), each landing in
its factor category and **never in a colour component**; the joint-faithfulness seal (an arrow of
`K` is exactly its five-tuple of component arrows — the reversibility round-trip). **Tooth:**
`crs:FiveProjectionShape` + `q_five_projections_faithful`. **Probe:** two distinct `K` arrows
sharing an identical five-tuple of `π_j` images (faithfulness break), OR a `π_S` landing in
`crs:RedChannel` → `conforms=False`.

**T8 — `derivation.ttl` coordinatization = Frame/Kleisli; derived-not-stored.**
`crs:CoordinateDerivation` is a `prim:Frame` (carries `prim:frameOutput`+`prim:frameEffect`, reuses
`prim:isYonedaPoint true`), domain an `aob:AOBAtom` identity, codomain a tower position/ordinal.
**Tooth:** `crs:FrameDerivationShape` + `crs:DerivedNotStoredShape` + `q_coordinates_derived`.
**Probe:** a point carrying a stored `xsd:double` coordinate literal → `conforms=False`; a
derivation missing `prim:frameEffect` → `conforms=False`.

**T9 — `derivation.ttl` the z descent + agnostic byte-order (Q1).** `crs:ZDerivation`:
`aob:AOBAtom → aob:hasHashDigest → aob:HashDigest` (32 `prim:Octet`) → first two octets
(`crs:takesOctetPrefix 2`, a `prim:Block`) → `prim:Uint16` (`prim:bitWidth 16`,
`prim:interpretAs prim:Natural`) with its byte-order coordinate typed at **`aob:ByteOrderProgenitor`
(no concrete leaf)** → `prim:Natural` (0..65535) via the `prim:byteDescendsTo+ prim:Bit` chain;
carries a `crs:HashPrefixTruncation` effect (2 of 32 octets). SP2's LE `aob:zSeed` noted as the
`byteOrderLittle` realisation composing under the progenitor. **Tooth:** `crs:ZGroundingShape`
(the exact chain; **permits the ungrounded agnostic progenitor** as the v1 default; forbids a
concrete leaf being asserted as the canonical v1 default, a `none`/`big` default, a 4-octet read,
or a non-`prim:Natural` interpretation) + `q_z_from_urn`. **Probe:** a z reading 4 octets → RED; a
z omitting the byte-order progenitor coordinate entirely → RED; a z defaulting to `aob:byteOrderBig`
→ RED.

**T10 — `derivation.ttl` the S:P:O↔S:O:P order effect.** `crs:OrderProjection` Frame reordering
the external `S:P:O` and internal `S:O:P` orders on one content-addressed reified arrow-node, with
a typed `crs:RoleOrderEffect` loss (seeds SP4). **Tooth:** `q_order_effect`. **Probe:** an
`crs:OrderProjection` missing its `crs:RoleOrderEffect` → `conforms=False`.

**T11 — dual-grounding over the merged graph.** Every new `crs:` carrier/tower/geometer/plane/
product `owl:Class` carries its own `prim:Realization` (`aob:groundingClaim`-style) + reflexive
carrier + `prim:Primitive` so SP1's `prim:DualGroundingShape`/`q_universality` stays green on the
merged graph. **Tooth:** `q_chart_dual_grounded` (reuses SP1). **Probe:** strip one crs class's
realization → SP1 `q_universality` flips false.

**T12 — χ honest-red deferral marker (Q4).** In `derivation.ttl`, an `rdfs:comment`/annotation
individual `crs:chiComparisonObligation` naming χ:`Ob(K)→W` a **deferred** cross-framework
obligation to SP4/W5 — carrying **no** component map and **no** tooth, `silm:isProvisional true`.
**Guard tooth:** `crs:NoCrossTagTransitionShape` — no edge asserts an Atlas↔Graph hom/transition
(reinforcing T2 disjointness). **Probe:** inject an Atlas→Graph transition edge → `conforms=False`.

**T13 — integration, depth, DAG flip.** README (the floor doc + probe register); depth gate green
(every `owl:Class` ≥200-char comment, every individual a real comment); full `run-crs-checks.sh`
GREEN with SP1+SP2 untouched+green; flip `silm:phase_w2_sp3 silm:hasStatus "completed"` in
`basicttl/dag/dag_instances.ttl` with **honest inline evidence** (real triple/shape/ASK/probe
counts that reproduce on disk); confirm the DAG parses+conforms and `phase_w2_sp3` deps satisfied.

## Verification (evidence-first; §4 of the design)
SHACL shapes (all RED-before/GREEN-after, each proven to bite by a documented probe):
`crs:CarrierDisjointnessShape`, `crs:AxisUrnTowerShape`, `crs:NoPositionalMapShape`,
`crs:DimensionCountShape`, `crs:PlaneProgenitorShape`, `crs:FiveProjectionShape`,
`crs:FrameDerivationShape`, `crs:DerivedNotStoredShape`, `crs:ZGroundingShape`,
`crs:NoCrossTagTransitionShape`, + the reused SP1 `prim:DualGroundingShape`.
EXPECT-TRUE ASKs (non-vacuous, inline DATA CONTRACT, proven False on empty graph):
`q_carriers_disjoint`, `q_towers_independent`, `q_dimension_equals_count`,
`q_geometer_below_towers`, `q_plane_progenitor_symmetric`, `q_five_projections_faithful`,
`q_coordinates_derived`, `q_z_from_urn`, `q_order_effect`, `q_chart_dual_grounded`.
Value-type checks use `sh:in`/`sh:sparql`, never range-inference-vacuous `sh:class` (SP1 defang
discipline). Then the adversarial triple panel (completeness / honesty / doctrine).

## Non-goals (this iteration)
Corpus-agnostic — zero corpus instances (live binding = W5); no geodetic/EPSG projection math; no
perceptual-colour tessellation metric (`w_f,ℓ_f,ε_f`); geometer glossary internals belong to SP6;
`x,y,z,w,p` navigation stays symbolic; χ is deferred (T12 marker only). Built to be relaunched.
