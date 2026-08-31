# `basicttl/crs/` — the S/O/P-tower CRS law floor (W2 · SP3)

The corpus-agnostic **N-dimensional Coordinate Reference System (CRS) law**, *realized as the
Subject/Object/Predicate URN towers*, **LIFTED** from the Helios carrier-towers triad (Directive 1:
lift, do not invent). This is **this iteration's v1** — corpus-agnostic (Directive 13), built to be
re-run and relaunched, never for permanence. It grounds ONTO the two committed, green floors below
it: **SP1** (`basicttl/primitives/`) and **SP2** (`basicttl/aob/`).

**Status: COMPLETE — T1 … T13 all landed (this floor is done, v1).** The runner
`basicttl/crs/checks/run-crs-checks.sh` exits 0, GREEN in ~23s wall clock: SP1 primitive floor green
standalone (21 ASKs) + SP2 AOB floor green standalone (13 ASKs) + the single merged SP1+SP2+SP3 graph
(11 632 triples) conforms to `crs.shapes.ttl` (the SP3 law) AND to SP1 `primitives.shapes.ttl` re-run
over the merge (`prim:DualGroundingShape` — the T11 dual-grounding tooth) AND to SP2 `aob.shapes.ttl`,
with all **10 crs + 21 SP1 + 13 SP2** EXPECT-TRUE ASKs true over the merge and the depth gate green
(every crs `owl:Class` ≥ 200-char `rdfs:comment`, 6 files). On disk: **43 crs `owl:Class`, 265 minted
crs individuals** (each a real comment), **11 biting SHACL `sh:NodeShape`s over 17 `sh:sparql` (+ 10
`sh:property` `sh:minCount`) constraints, 10 EXPECT-TRUE ASKs**, across the 5 data TTLs (2233 triples).
Grounds-nothing is enforced **symmetrically across every progenitor level** (G1, Directive 17
no-privilege): a node typed at the bare TOP progenitor `crs:Geometer` carrying a concrete `crs:hasAxis`
is RED via the generalised `crs:PlaneProgenitorShape` constraint A (guarded on `crs:Geometer` with the
seven-concrete-leaf enumeration), and one carrying a concrete `crs:hasDimension` is RED via
`crs:DimensionCountShape`'s top-progenitor grounds-nothing clause — while the two plane progenitors
`crs:PlaneGeometer` / `crs:RolePairProjectionPlane` stay exempt (they may declare their rank-2 family
arity `crs:hasDimension 2`).

`carriers.ttl` (T2) adds the agnostic `crs:TaggedByteCarrier` progenitor (= B_rgb) with its two
symmetric children `crs:AtlasByteCarrier` / `crs:GraphByteCarrier` (`Q_A ∩ Q_G = ∅`, `owl:disjointWith`)
over SP1 `prim:Octet`/`prim:ByteVector`/RGB, plus the many-to-one tag-erasure `crs:ForgetfulTagFrame`
Kleisli arrows. `towers.ttl` (T3/T4) adds the agnostic `crs:UrnRoleTower` progenitor with its three
symmetric children `crs:SubjectTower`/`crs:ObjectTower`/`crs:PredicateTower` (each a URN tower functor
`prim:Ordinal→prim:URN`, own `crs:hasTowerDimension`) + the `crs:LexToUrnBridge` lift of SP2's S/O/P
strings, then the positional-collapse obstruction (`crs:ColourChannel` + `crs:Red/Green/BlueChannel`,
the non-injective `crs:colourOnly` — the WHY `S=R`/`O=G`/`P=B` are underivable). `geometers.ttl`
(T5/T6/T7) adds the agnostic `crs:Geometer` (`crs:RoleGeometer` rank-3 S-O-P, `crs:QuarkGridGeometer`
rank-2 3×3 quark grid) enforcing `count(crs:hasAxis)==crs:hasDimension` (Q2), the agnostic
`crs:PlaneGeometer` progenitor family (Q3: `crs:Honeycomb`/`crs:Geographic` planes + the symmetric
`crs:RolePairProjectionPlane` family (S,O)/(S,P)/(O,P)), and the five-factor product `crs:CarrierProduct`
`K=K_A×K_G×K_S×K_O×K_P` with its `π_j` joint-faithfulness seal. `derivation.ttl` (T8/T9/T10/T12) adds
coordinatization-as-Frame (`crs:CoordinateDerivation`, derived-not-stored), the `z` descent grounded in
the agnostic `aob:ByteOrderProgenitor` (Q1, no v1 leaf), the `S:P:O`↔`S:O:P` `crs:OrderProjection`, and
the χ honest-red deferral marker `crs:chiComparisonObligation` (Q4). `dual_grounding.ttl` (T11) brings
each coordinate-chart `owl:Class` under SP1's `prim:DualGroundingShape`/`prim:YonedaShape` over the merge.

**Runner performance (T13 — the floor is not green until the runner completes GREEN in reasonable
wall-clock).** Two whole-graph hot spots each cost ~165–177 s on the partial floor (the runner timed
out > 2 min). Both were fixed *without weakening any tooth or trimming honest content*:
1. **`aob.shapes` over the merged graph (~177 s).** `aob.shapes` targets EXCLUSIVELY by `sh:targetClass`
   and its 13 `sh:sparql` constraints are all `$this`-anchored, so its focus set = the class-typed aob
   nodes. SP3 is corpus-agnostic v1: it mints zero aob-typed individuals, no crs class subclasses an aob
   class, and it mutates no aob individual — so the merged-graph focus set is identical to the aob-only
   graph the SP2 standalone runner already validates green. Re-running the 38 constraints over the 10×
   larger merged graph is gratuitous. The runner now **machine-checks that invariant over the full
   non-aob (SP1+SP3) delta each run** and transfers the SP2-standalone green, falling back to the full
   re-validation if a future corpus-bound version ever contributes an aob focus node. (The full merged
   `aob.shapes` run was separately measured `conforms=True`, so this is a proven equivalence, not a skip.)
2. **`q_chart_dual_grounded` ASK (~165 s).** The witness clause was joined into the main pattern,
   binding ~46 rows that each redundantly re-evaluated the costly bidirectional-`subClassOf*`
   `NOT EXISTS`. Wrapping the witness in `FILTER EXISTS { … }` evaluates it once — **semantically
   identical** (`(∃ grounded witness) ∧ (∀ chart class grounded)`), verified True on the clean graph and
   still False under both probes of record — and drops the ASK to < 1 s.

`dual_grounding.ttl` (~192 KB) was audited and is **not** padding: 23 genuinely distinct grounded chart
classes (= the plan T11 scope), no duplicate subjects, per-class distinct comments, each cluster the
`prim:FormalType` pun + `prim:Realization` + reflexive carrier + `prim:Primitive` + Yoneda apparatus
that SP1's `prim:DualGroundingShape` *and* `prim:YonedaShape` require over the merge — load-bearing, so
it is kept intact (trimming it would regress the T11 tooth).

Namespace: `crs: <urn:silmaril:crs:#>` (full-lexical URN idiom, unary law), grounding onto
`prim: <urn:silmaril:prim:#>` (SP1), `aob: <urn:silmaril:aob:#>` (SP2), and
`silm: <urn:silmaril:entity#>` (for `silm:isProvisional`). External spellings survive only as
immutable bridge evidence on the external side of a registered bridge (STRICTNESS Rule 3).

## The merged-graph discipline (why the runner loads three floors)

SP3 adds `owl:Class`es that must **dual-ground** under SP1's `prim:DualGroundingShape` /
`q_universality` — so SP3 is not green unless the SP1 (and SP2) laws still hold **over the single
merged graph** into which SP3's classes descend. The runner therefore:

1. re-runs the committed **SP1** floor on its OWN graph (`run-floor-checks.sh`, 21 ASKs) — untouched + green;
2. re-runs the committed **SP2** floor on its OWN graph (`run-aob-checks.sh`, 13 ASKs) — untouched + green;
3. parses **SP1 (4) + SP2 (7) + SP3 (auto-discovered `basicttl/crs/*.ttl`, minus `crs.shapes.ttl`)**
   into ONE merged graph and validates it against `crs.shapes.ttl` (the SP3 law), `primitives.shapes.ttl`
   (the SP1 law re-run over the merged graph — the tooth T11 injects against) and `aob.shapes.ttl`,
   then requires every EXPECT-TRUE ASK of all three suites true over the merged graph;
4. runs the depth gate (`scripts/ontology-depth-check.py basicttl/crs`) — every `owl:Class` ≥ 200-char comment.

`crs.shapes.ttl` is loaded **only** as the shapes graph, never mixed into the data graph. The SP3 data
TTLs are **auto-discovered** so each later task's new data file wires itself in with no runner edit.

## File map (one file per concern — STRICTNESS Rule 14)

| file | responsibility | task(s) |
|------|----------------|---------|
| `carriers.ttl` | disjoint Atlas/Graph byte carriers `Q_A`/`Q_G` (`Q_A∩Q_G=∅`, no cross-tag hom), tag-erasure forgetful Frames — over SP1 `prim:Octet`/`prim:ByteVector`/RGB | T2 |
| `towers.ttl` | `K_S/K_O/K_P` as nth-dim URN towers (functor `prim:Ordinal→prim:URN`), bridging SP2's `xsd:string` S/O/P triple → `prim:URN`; the positional-collapse obstruction (`S=R`/`O=G`/`P=B` forbidden) | T3, T4 |
| `geometers.ttl` | per-geometer quark grid; `crs:Geometer` (atlas-glossary-fixed, axis system, `crs:hasDimension`); the agnostic `crs:PlaneGeometer` progenitor family (Q3); the five-factor product `K` + `π_j` + joint-faithfulness seal | T5, T6, T7 |
| `derivation.ttl` | coordinatization as Frame/Kleisli; the `z` descent + agnostic `aob:ByteOrderProgenitor` (Q1); the `S:P:O`↔`S:O:P` order effect; χ honest-red deferral marker (Q4) | T8, T9, T10, T12 |
| `crs.shapes.ttl` | the SHACL law — one biting `sh:NodeShape` per invariant (`sh:sparql`/`sh:in`, defang-proof) | T2–T12 |
| `crs.queries.sparql` | the EXPECT-TRUE ASK suite, each with an inline DATA CONTRACT + probe-of-record comment | T2–T11 |
| `checks/run-crs-checks.sh` | the runner (SP1 + SP2 standalone, then merged-graph pyshacl + every ASK + depth gate) | T1 |

## How to re-run

```bash
bash basicttl/crs/checks/run-crs-checks.sh   # SP1 + SP2 floors + merged pyshacl + every ASK + depth gate; exit 0 iff green
```

Never run state-changing git from this floor. Author only under `basicttl/crs/` (plus, in Task T13
only, the `phase_w2_sp3` completion flip in `basicttl/dag/dag_instances.ttl`).

## Probe register (teeth proven by injection, filled in as tasks land)

| task | tooth | probe of record (CAUGHT: conforms/ASK True→False) |
|------|-------|---------------------------------------------------|
| T1 | the merged-graph runner genuinely re-validates the floors | break the runner's SP1 load path → runner exits non-zero (RED) |
| T2 | `crs:CarrierDisjointnessShape` + `q_carriers_disjoint` (Q_A ∩ Q_G = ∅) | inject one object typed both `crs:AtlasByteCarrier` and `crs:GraphByteCarrier` → `conforms=True→False` and `q_carriers_disjoint True→False` |
| T3 | `crs:AxisUrnTowerShape` + `q_towers_independent` (K_S/K_O/K_P each a URN tower, not scalar) | inject `crs:probeScalarAxis a crs:UrnTowerAxis ; crs:axisComponentType prim:Real` → `conforms=True→False` and `q_towers_independent True→False` |
| T4 | `crs:NoPositionalMapShape` + `q_towers_independent` no-colour-map clause (S=R/O=G/P=B forbidden) | inject `crs:SubjectTower owl:sameAs crs:RedChannel` → `conforms=True→False` and `q_towers_independent True→False` |
| T5 | `crs:DimensionCountShape` + `q_dimension_equals_count` + `q_geometer_below_towers` (per-geometer `count(crs:hasAxis)==crs:hasDimension`, Q2; **G1b** top-progenitor grounds-nothing DIMENSION clause) | inject `crs:probeXyGeometer a crs:QuarkGridGeometer ; crs:hasDimension 2 ; crs:hasAxis` (3 axes) — an (x,y) geometer with 3 axes, or a S-O-P geometer declaring dimension 2 → `conforms=True→False` and `q_dimension_equals_count True→False`; **G1b:** `crs:evilGeo4 a crs:Geometer ; crs:hasDimension 7` (a bare TOP progenitor carrying a concrete dimension — the top `crs:Geometer` declares none) → `conforms=True→False`, while a bare `crs:PlaneGeometer`/`crs:RolePairProjectionPlane` carrying `crs:hasDimension 2` (family arity) stays GREEN |
| T6 | `crs:PlaneProgenitorShape` + `q_plane_progenitor_symmetric` (progenitor grounds nothing; every concrete plane has exactly 2 axes; role-pair family symmetric; **G1a** grounds-nothing axis tooth generalised to the TOP `crs:Geometer`) | inject `crs:probePlaneProgenitorAxis a crs:PlaneGeometer ; crs:hasAxis crs:honeycombXAxis` (the progenitor carrying a concrete axis) — or a 3-axis plane child, or a family missing one symmetric plane → `conforms=True→False` and `q_plane_progenitor_symmetric True→False`; **G1a:** the SAME constraint A now bites the TOP progenitor — `crs:evilGeo a crs:Geometer ; crs:hasAxis crs:a` (bare `crs:Geometer` carrying a concrete axis, none of the 7 concrete leaves) → `conforms=True→False`, symmetrically with the bare `crs:PlaneGeometer` |
| T7 | `crs:FiveProjectionShape` + `q_five_projections_faithful` (5 `π_j` jointly faithful; never in a colour component) | inject `crs:probeColourProj a crs:FactorProjection ; crs:landsInFactor crs:RedChannel` (a `π_j` landing in colour) — or a second `crs:ProductArrow` duplicating a five-tuple (faithfulness break) → `conforms=True→False` and `q_five_projections_faithful True→False` |
| T8 | `crs:FrameDerivationShape` + `crs:DerivedNotStoredShape` + `q_coordinates_derived` (coordinatization = Frame; coordinates derived, never stored) | inject `crs:probeEffectlessDerivation a crs:CoordinateDerivation ; prim:frameOutput prim:Uint16` (Frame missing `prim:frameEffect`), or `crs:probeStoredPoint a crs:CoordinatePoint ; crs:atCoordinate "3.14"^^xsd:double` (stored literal coordinate) → `conforms=True→False` and `q_coordinates_derived True→False` |
| T9 | `crs:ZGroundingShape` + `q_z_from_urn` (z = uint16 over first 2 octets of the sha256, agnostic `aob:ByteOrderProgenitor`, `prim:Natural`; Q1) | inject `crs:probeZFourOctets … crs:takesOctetPrefix 4` (4-octet read), a z omitting `crs:zByteOrderCoordinate`, or `crs:zByteOrderCoordinate aob:byteOrderBig` (concrete-leaf default) → `conforms=True→False` and `q_z_from_urn True→False` |
| T10 | `crs:OrderProjectionShape` + `q_order_effect` (S:P:O↔S:O:P reorder carries a typed `crs:RoleOrderEffect`) | inject `crs:probeOrderNoEffect a crs:OrderProjection ; crs:reordersArrowNode … ; crs:externalOrder "S:P:O" ; crs:internalOrder "S:O:P" ; prim:frameOutput … ; prim:frameEffect …` (reorder missing its `crs:RoleOrderEffect`) → `conforms=True→False` and `q_order_effect True→False` |
| T11 | reused SP1 `prim:DualGroundingShape` + `q_chart_dual_grounded` (every crs chart class dual-grounds into SP1 over the merge) | inject `crs:probeOrphanChart a owl:Class ; rdfs:subClassOf prim:FormalType` (ungrounded chart class) — or strip `crs:realize_CarrierProduct` — → SP1 `prim:DualGroundingShape conforms True→False`, SP1 `q_universality True→False`, and `q_chart_dual_grounded True→False` |
| T12 | `crs:NoCrossTagTransitionShape` (Q4: no Atlas↔Graph hom/transition; disjointness' second face) | inject `crs:atlasCarrierWitness crs:crossTagTransition crs:graphCarrierWitness` (an Atlas→Graph transition edge) → `conforms=True→False` |
| T13 | the runner completes GREEN in reasonable wall-clock (the partial floor timed out > 2 min) | the pre-T13 runner did not complete in ≤ 2 min (merged `aob.shapes` ~177 s + `q_chart_dual_grounded` ~165 s); after the T13 fixes the full runner exits 0 in ~23 s with every earlier tooth still biting (all 11 shapes flip conforms True→False under probe injection; verified) |
