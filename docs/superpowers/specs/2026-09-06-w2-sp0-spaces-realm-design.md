# W2 · SP0 — the SPACES REALM fold (non-algebraic structural-theory tower → `basicttl/primordial/type/spaces/**`) — design

**Status:** DESIGN pass only. NO ontology/foundation/git edits. Sole write target: this file.
**Governing gates:** D24 (four planes + validation-modes + 8-value proof-status + A6 theory/model/reduct **and its ALGEBRAIC limit**), D25 (fold into `basicttl/primordial/type/**`, CI lockstep), D26 (full runtime Linnaean ladder, adjective-first compounds).
**Maintainer directive:** fold the eight spaces MetricSpace / TopologicalSpace / UniformSpace / NormedSpace / InnerProductSpace / MeasureSpace / BanachSpace / HilbertSpace into the B4 tower. Four exist in `fnd:` today; four (Uniform / Measure / Banach / Hilbert) must be BUILT.

---

## MAINTAINER RULINGS (LOCKED — these OVERRIDE the open-question recommendations in §3/§7 below)

- **OQ1 → ALL 8 spaces under the single attested `realm:topology`** (NOT three realms). D26 lift-don't-invent: the reference attests `domain:mathematics:realm:topology` but not `realm:analysis`/`realm:measure`, so every space is `domain:mathematics:realm:topology:subdomain:<sub>` with the subdomain distinguishing it (`topological:space`, `uniform:space`, `metric:space`, `normed:space`, `banach:space`, `inner:product:space`, `hilbert:space`, `measure:space`). The §1.5 metric exemplar already uses `realm:topology` — correct; the analysis/measure spaces use it too (drop the §3 realm:analysis/realm:measure proposal). No new realm minted.
- **OQ2 → FOLD the sheaf/site core NOW** (Site/Cover/Sheaf/MatchingFamily/LocalSection/PerceptualTessellation) into the new tower AND demolish it from `fnd:` this pass. It is category/topos theory, so it folds under the ATTESTED `domain:mathematics:realm:category` (reference attests `realm:category`), in a sibling subtree `basicttl/primordial/type/category/**`, with the same structural-theory / B4 idiom (a Grothendieck site = a category + a coverage; a sheaf = a presheaf + a gluing condition). NOT preserved in `fnd:`.
- **OQ3 → SHIP ALL 8** with completeness / σ-additivity / homogeneity as `external:certificate` honest-reds (`proof:status open`/`conditional`, no finite witness, teeth only on the finitely-checkable base) — per §4.3.
- **R1–R5 review corrections ADOPTED** into the build (metric separation-half tooth added `finite:table`; homogeneity/linearity full form `external:certificate` with only enumerated-instance `bounded:diagnostic`; the normed/inner witnesses split into the GF(3) algebraic-reduct fixture + a real-valued norm/inner-value fixture over named vectors; all four structural record classes `rdfs:subClassOf rec:specimen:record` NOT the algebra namesakes; the metric⊥measure disjointness stays a record-type distinction, not a carrier claim).

Build order: **3b-spaces** (fold all 8 spaces under `realm:topology` + the sheaf/site core under `realm:category`, additive) → **3c-spaces** (demolish the `fnd:` spaces + sheaf core, re-home VectorSpace/enrichedOver/groundsInSpace, migrate teeth, lockstep). Fires after the in-flight algebra demolition (3c) lands.
**Praeriehund:** every structural claim cites `file:line`; every unattested token is `[S]`-flagged; every honest-red / certificate deferral is explicit.

---

## 0. The core design problem — spaces are NON-ALGEBRAIC, so A6's engine does not fit

The committed B4 algebra tower folds each rung as a **presented Lawvere theory** `T=(S,Ω,E)` (D24 A6): a signature naming finitary operation symbols (`signatures.ttl` `sigMonoid` Σ={·,e}) and an equation set `E` of `t_left = t_right` laws (`equations.ttl`), reified as a Cayley table (`shapes/algebra.shapes.ttl:110` walks `?cell @rel:structure <model>` with `@rel:category:first/second/result`). Every rung theory record MUST name **exactly one `@rel:signature` + ≥1 `@rel:equation`** (`TheoryShape`, `algebra.shapes.ttl:72-87`).

Spaces do not have this shape:

- a **topology** is a SET OF OPEN SETS `τ ⊆ P(X)` — a family-of-subsets predicate, not a finitary operation;
- a **metric** is a real-valued FUNCTION `d: X×X → [0,∞)` with order/inequality axioms (identity of indiscernibles, symmetry, triangle inequality) — not a `t_left = t_right` equation;
- a **uniformity** is a FILTER of entourages `Φ ⊆ P(X×X)` closed under a composition-refinement `∃V: V∘V ⊆ U`;
- a **measure** is a σ-additive FUNCTION `μ: Σ → [0,∞]` on a **σ-algebra** `Σ ⊆ P(X)`.

None is a Lawvere finitary-equational theory. D24 A6 is explicitly scoped to **algebraic/Lawvere theories** (`design_constraints.md:441-443` "every structure is a model of a declared theory T=(S,Ω,E) (Lawvere)"), so the algebra `TheoryShape` / `EquationRecordShape` / reified-Cayley engine does **not** directly fit. This design specifies the **STRUCTURAL-THEORY template** that does, reusing every reusable part of the B4 idiom.

The move is the same one the two-operation floor already made: where the one-operation `rec:reduct:record` was insufficient, a **parallel discriminated class** `rec:reduct:two:operation:record` was minted `subClassOf rec:specimen:record`, NOT `rec:reduct:record`, so the one-law `ReductShape` never focuses it (`reducts_twoop.ttl:54-58`). We mint the structural-theory analogues the same way, so the algebra teeth never falsely bite a space and the space teeth never falsely bite an algebra.

---

## 1. THE STRUCTURAL-THEORY TEMPLATE (the B4 four planes, adapted)

### 1.1 What is REUSED verbatim vs what is NEW

**Reused unchanged** (bridge-never-duplicate, TODO-11): the four D24 planes; the B4 **two model planes** (a Plane-2 DENOTATUM `rec:denotatum:record` with NO provenance + a Plane-1 DECLARATION-RECORD model class `rec:model:record`/`rec:declaration:record` linked by `@rel:denotes`, `records.ttl:95-109`); the intensional `owl:Restriction` bundle idiom (`monoid.ttl:109-112`); the provenance quartet on RECORDS only (`monoid.ttl:80-84`); the triad-envelope gate (`monoid.ttl:168-173`); `rec:axiom:record` / `rec:theorem:record` + `@typ:certificate` (`monoid.ttl:127-163`); `BridgeShape` / `ProvenanceShape` / `DifferentFromWitnessShape` (`algebra.shapes.ttl:226-273`); the runner's discovery + fixture-polarity + 0-focus + depth gates (`run-algebra-checks.sh`).

**New (minted parallel, each `[S]`, flagged for sign-off):**

| new record class | parallel to (`records.ttl`) | why the algebra class does not fit |
|---|---|---|
| `rec:structural:theory:record` | `rec:theory:record` (:46) | a structural theory has **no algebraic signature and no equation set**; it names a **structure-signature** + **structural axioms**. `TheoryShape`'s `min1 @rel:equation` would falsely redden it. |
| `rec:structure:signature:record` | `rec:signature:record` (:67) | a structure-signature names a **carrier sort + a structure component** (a family-of-subsets predicate / a real-valued function / a σ-algebra), NOT finitary operation symbols with arities. |
| `rec:structural:axiom:record` | `rec:axiom:record` (:REUSED, `closure.ttl`) | a structural axiom carries a **per-axiom `@rel:validation:mode`** (D24 4-value) and is an **order/membership/limit predicate**, never a `t_left=t_right` equation; targeting bare `rec:axiom:record` would demand a mode on every algebra closure axiom too. |
| `rec:reduct:structural:record` | `rec:reduct:two:operation:record` (`reducts_twoop.ttl:54`) | an **induced-structure** reduct (a metric INDUCES a uniformity which INDUCES a topology; a norm INDUCES a metric) forgets/derives a whole structure component, not one law; and the **algebra-space seam** reduct connects a space to a `spine/vector_space.ttl` / `spine/commutative_monoid.ttl` model-record across realms. |

### 1.2 The four planes for a structural theory

**Plane A0 stratification (unchanged):** Syntax(structure-signature) ⊥ Theory ⊥ Model ⊥ Element(carrier points / open sets / distance rows) ⊥ ProofArtifact.

- **DENOTATUM (Plane-2):** the mathematical object ("a metric space") carrying `@rel:identifier` + `@rel:notation` ONLY, NO provenance (`records.ttl:100`); `skos:exactMatch fnd:<Space>` retire-bridge.
- **DECLARATION-RECORD model class (Plane-1):** `owl:Class , rec:model:record , rec:declaration:record`; `@rel:denotes` the denotatum; an `owl:Restriction` bundle making the structure a graph fact — for a metric space: cardinality-1 `@rel:carrier` (the set X) + cardinality-1 `@rel:distance:function` (the structure component); provenance quartet + `@rel:authority`; `owl:disjointWith` genuine homonym siblings.
- **STRUCTURAL THEORY record (also the Plane-1 `@typ:declaration`):** `@rel:structure:signature` (the carrier+structure), `@rel:axiom` (the structural axioms, each a `rec:structural:axiom:record` with its own `@rel:validation:mode`), `@rel:reduct` (the induced-structure theory it refines to), `@rel:denotatum`, `@rel:assignment` (the reconciliation gate), theory-level `@rel:proof:status`, provenance.
- **GATE (Plane-3):** the reconciliation gate (`monoid.ttl:168` idiom) closing the Denotatum/DeclarationRecord/Gate triad.

### 1.3 How the STRUCTURE is reified (analogue of the reified Cayley table)

The algebra tower makes laws checkable by reifying the operation as `@rel:structure`-scoped `@rel:category:first/second/result` cells (`algebra.shapes.ttl:110`). Spaces reify their **structure component** the same way — as scoped, per-witness graph rows the SHACL teeth walk — so each axiom becomes a checkable graph fact with biting teeth + a failing negative. Each row-family gets its OWN scoped predicate (the `fnd:intersectionIn` vs `fnd:unionIn` discipline, `spaces.ttl:192-215`, so `inference=rdfs` never cross-types a row):

| structure | reified as (folded from / newly minted) | scoped predicates |
|---|---|---|
| topology `τ⊆P(X)` | **reified open-set membership** + **reified closure rows** `L∩R=result`, `L∪R=result` (FOLD `fnd:hasOpenSet` / `fnd:OpenIntersection` / `fnd:OpenUnion`, `spaces.ttl:177-230,447-490`) | `@rel:open:member`, `@rel:open:intersection` (`@rel:intersect:left/right/result`), `@rel:open:union` |
| uniformity `Φ⊆P(X×X)` | **reified entourage membership** + **diagonal-membership rows** + **composition-refinement rows** `V∘V⊆U` (NEW) | `@rel:entourage:member`, `@rel:entourage:composition` (`@rel:comp:half`, `@rel:comp:whole`) |
| metric `d:X×X→ℝ≥0` | **reified distance assertions** `d(x,y)=v` (FOLD `fnd:DistanceAssertion`, `spaces.ttl:237-315,543-587`) | `@rel:distance:assertion` (`@rel:dist:from/to/value`) |
| norm `‖·‖:V→ℝ≥0` | **reified norm-value assertions** `‖v‖=r` + **induced-metric rows** `d(u,v)=‖u−v‖` (NEW) | `@rel:norm:assertion` (`@rel:norm:vector/value`) |
| inner product `⟨·,·⟩:V×V→F` | **reified inner-product assertions** `⟨u,v⟩=c` + **induced-norm rows** `‖v‖²=⟨v,v⟩` (NEW) | `@rel:inner:assertion` (`@rel:inner:left/right/value`) |
| σ-algebra + measure `(Σ,μ)` | **reified σ-algebra membership** + **complement rows** `Aᶜ=result` + **countable(finite-witness)-union rows** + **measure-value assertions** `μ(A)=v` + **disjoint-additivity rows** `μ(A⊔B)=μ(A)+μ(B)` (NEW) | `@rel:sigma:member`, `@rel:sigma:complement`, `@rel:sigma:union`, `@rel:measure:assertion` (`@rel:meas:set/value`), `@rel:measure:additivity` |

The witness rows live in `fixtures/` (D24 four planes: witnesses are EVIDENCE, outside the ontology data glob — `run-algebra-checks.sh:68-71`).

### 1.4 Per-axiom VALIDATION MODES (D24 4-value: `finite:table` / `rewrite` / `external:certificate` / `bounded:diagnostic`)

The load-bearing difference from algebra: **the validation mode is per-AXIOM, not per-theory** (algebra puts one `@rel:validation:mode` on the theory record, `ValidationModeShape` `algebra.shapes.ttl:207`; spaces put a mode on each `rec:structural:axiom:record`, gated by the new `StructuralAxiomShape`). This is exactly the maintainer directive "each carrying a D24 VALIDATION MODE". Assignment rule:

- **`finite:table`** — a finite witness fully decides the axiom (topology closure under finite intersection / representative union on a finite τ; metric identity/symmetry; σ-algebra closure under complement + finite union; finite-additivity on disjoint sets).
- **`bounded:diagnostic`** — order/inequality axioms decided on a finite witness by a numeric FILTER (the triangle inequality `d(x,z) > d(x,y)+d(y,z)`; the norm triangle `‖u+v‖ > ‖u‖+‖v‖`; the inner-product parallelogram-law diagnostic).
- **`external:certificate`** — completeness / uncountable axioms that **cannot** be finitely checked (Banach/Hilbert completeness: *every* Cauchy sequence converges; absolute homogeneity `‖a·v‖=|a|·‖v‖` over an uncountable scalar field; countable additivity over an uncountable σ-algebra). These are the **honest-red / certificate deferrals**: the axiom record exists, declares `external:certificate`, and carries an `@rel:proof:status` of `open` or `conditional` with NO finite witness (§4.3).
- **`rewrite`** — not used by the space tower (it is algebra's term-rewriting mode).

### 1.5 THE WORKED EXEMPLAR — MetricSpace END-TO-END in the full-ladder grammar (D26)

Prefixes (mirroring `monoid.ttl:46-59`; the realm token is the subject of **Open Question #1** — `realm:topology` used here, `[S]`):

```turtle
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix fnd:  <urn:silmaril:fnd:#> .
# mathematics 12-marker ladder head (D26), realm:topology [S], ending at subdomain::
@prefix spc:  <urn:silmaril:type:graph:instance:instruction:code:property:domain:mathematics:realm:topology:subdomain:> .
@prefix rel:  <urn:silmaril:type:graph:instance:instruction:code:property:relation:> .
@prefix typ:  <urn:silmaril:type:graph:instance:instruction:code:property:type:> .
@prefix rec:  <urn:silmaril:type:graph:instance:instruction:code:property:grounding:ontology:basic:formal:domain:knowledge:representation:kingdom:specification:phylum:formal:contract:class:class:order:declared:family:seed:genus:registry:species:> .
```

**(a) STRUCTURAL THEORY record** (`@typ:declaration`; the metric structural theory) — [S] `class:structural:theory`/`genus:presented`:

```turtle
spc:metric:space:kingdom:definition:phylum:space:class:structural:theory:order:declarative:family:metric:space:genus:presented:species:metric:space:component:definition:instance:canonical
    a owl:NamedIndividual , rec:structural:theory:record , typ:declaration ;
    rdfs:label "metric space structural theory (X, d)" ;
    rel:notation   "metric space" ;
    rel:structure:signature
        spc:metric:space:kingdom:definition:phylum:specification:class:structure:signature:order:distance:family:function:genus:structural:species:signature:component:definition:instance:canonical ;
    rel:axiom
        spc:metric:space:kingdom:axiom:phylum:order:class:identity:order:binary:family:metric:space:genus:distance:species:indiscernible:component:statement:instance:canonical ,
        spc:metric:space:kingdom:axiom:phylum:order:class:symmetry:order:binary:family:metric:space:genus:distance:species:commutative:component:statement:instance:canonical ,
        spc:metric:space:kingdom:axiom:phylum:order:class:triangle:order:ternary:family:metric:space:genus:distance:species:subadditivity:component:statement:instance:canonical ;
    rel:reduct
        spc:uniform:space:kingdom:definition:phylum:space:class:structural:theory:order:declarative:family:uniform:space:genus:presented:species:uniform:space:component:definition:instance:canonical ;
    rel:enrichment
        <...:realm:algebra:subdomain:commutative:monoid:kingdom:class:...:model:...:component:class:instance:canonical> ;
    rel:denotatum
        spc:metric:space:kingdom:type:phylum:space:class:metric:space:order:distance:family:function:genus:axiomatic:species:metric:space:component:type:instance:canonical ;
    rel:assignment
        spc:metric:space:kingdom:assignment:phylum:reconciliation:class:gate:order:declarative:family:metric:space:genus:reconciled:species:declaration:component:assignment:instance:canonical ;
    rel:proof:status "literature:backed" ;
    rel:created "2026-09-06T00:00:00Z"^^xsd:dateTime ; rel:modified "2026-09-06T00:00:00Z"^^xsd:dateTime ;
    rel:version "1"^^xsd:nonNegativeInteger ; rel:state "accepted" ; rel:authority "SYN" ;
    rel:historical:identity fnd:MetricSpace ; skos:closeMatch fnd:MetricSpace ;
    rdfs:comment "[S] The presented metric-space STRUCTURAL theory (X,d) ... folds fnd:MetricSpace (basicttl/foundation/spaces.ttl:302-305). @rel:structure:signature names carrier X + distance function d:X×X->[0,inf); @rel:axiom the THREE structural axioms (identity-of-indiscernibles finite:table, symmetry finite:table, triangle bounded:diagnostic); @rel:reduct -> the uniform-space structural theory (a metric INDUCES a uniformity, E_eps={(x,y):d(x,y)<eps}); @rel:enrichment -> the commutative_monoid model-record ([0,inf],>=,+) (the algebra-space seam, folding fnd:enrichedOver fnd:nonnegRealsMonoid, spaces.ttl:242-245,504-508). proof:status literature:backed (cited standard metric geometry; only the finite 3-point WITNESS is finite:checked). SYN (Helios refuses point-set metrics on its objects, spaces.ttl:302-305). [S] class:structural:theory / genus:presented / @rel:structure:signature / @rel:enrichment UNATTESTED -> sign-off." .
```

**(b) STRUCTURE-SIGNATURE record** (carrier + structure component; analogue of `sigMonoid`) — [S]:

```turtle
spc:metric:space:kingdom:definition:phylum:specification:class:structure:signature:order:distance:family:function:genus:structural:species:signature:component:definition:instance:canonical
    a owl:NamedIndividual , rec:structure:signature:record ;
    rdfs:label "metric structure signature (X ; d: X x X -> [0,inf))" ;
    rel:carrier:sort   "X" ;
    rel:structure:component
        spc:metric:space:kingdom:operation:phylum:primitive:class:distance:order:binary:family:function:genus:realvalued:species:distance:component:operation:instance:canonical ;
    rdfs:comment "[S] The metric STRUCTURE signature: a carrier sort X and ONE structure component, the distance FUNCTION d:X x X -> [0,inf) (domain X x X, codomain the nonnegative reals) -- NOT a finitary operation symbol with an arity (that is the algebra rec:signature:record, records.ttl:67). This is the structural analogue: the component names a real-valued function, reified per witness as fnd:DistanceAssertion rows (spaces.ttl:237-240). [S] structure:signature / structure:component / genus:realvalued UNATTESTED -> sign-off." .
```

**(c) DENOTATUM (Plane-2, no provenance)** — retire-bridge `skos:exactMatch fnd:MetricSpace`:

```turtle
spc:metric:space:kingdom:type:phylum:space:class:metric:space:order:distance:family:function:genus:axiomatic:species:metric:space:component:type:instance:canonical
    a owl:NamedIndividual , rec:denotatum:record ;
    rdfs:label "metric space" ; rel:notation "metric space" ;
    rel:identifier "urn:silmaril:type:graph:instance:instruction:code:property:domain:mathematics:realm:topology:subdomain:metric:space:kingdom:type:phylum:space:class:metric:space:order:distance:family:function:genus:axiomatic:species:metric:space:component:type:instance:canonical" ;
    skos:exactMatch fnd:MetricSpace ;
    rdfs:comment "[S] The metric-space DENOTATUM (B4 Plane-2): the object 'a metric space' itself, @rel:identifier + @rel:notation ONLY, NO provenance (V1DenotatumHygieneShape). skos:exactMatch fnd:MetricSpace is the retire bridge keeping inbound SP3 fnd:MetricSpace refs (reanchor.ttl:82,268 fnd:groundsInSpace fnd:metricSpaceWitness) resolvable through the fold. BridgeShape focus. [S] phylum:space / class:metric:space UNATTESTED -> sign-off." .
```

**(d) MODEL-RECORD class (Plane-1)** — `owl:Restriction` bundle + provenance + disjointness:

```turtle
spc:metric:space:kingdom:class:phylum:space:class:model:order:declarative:family:metric:space:genus:governed:species:metric:space:component:class:instance:canonical
    a owl:Class , rec:model:record , rec:declaration:record ;
    rdfs:label "metric space model class" ; rel:notation "metric space model" ;
    rel:denotes spc:metric:space:kingdom:type:...:component:type:instance:canonical ;
    rdfs:subClassOf
        [ a owl:Restriction ; owl:cardinality "1"^^xsd:nonNegativeInteger ; owl:onProperty rel:carrier ] ,
        [ a owl:Restriction ; owl:cardinality "1"^^xsd:nonNegativeInteger ; owl:onProperty rel:distance:function ] ;
    owl:disjointWith spc:measure:space:kingdom:class:...:model:...:component:class:instance:canonical ;
    rel:created "2026-09-06T00:00:00Z"^^xsd:dateTime ; rel:modified "2026-09-06T00:00:00Z"^^xsd:dateTime ;
    rel:version "1"^^xsd:nonNegativeInteger ; rel:state "accepted" ; rel:authority "SYN" ;
    rdfs:comment "[S] The metric-space MODEL-RECORD (B4 Plane-1): 'a metric space has exactly one carrier X and exactly one distance function d' as a graph fact via two cardinality-1 owl:Restrictions (the D23 extensional fix -- fnd:*.ttl has ZERO owl:Restriction). owl:disjointWith the measure-space model-record (a metric space is NOT a measure space -- a genuine homonym/distinction tooth). It is NOT disjoint from topological/uniform space: a metric space IS a topological space via the induced-structure reduct (subsumption, not disjointness -- reducts_space_metric.ttl). Punned owl:Class + rec:model:record so a concrete space types against it AND it is a counted focus (ModelShape/ProvenanceShape). On this class the structure teeth are vacuous (no reified rows); the finite 3-point witness in fixtures/ is where they bite. [S] class:model / genus:governed / component:class UNATTESTED -> sign-off." .
```

**(e) STRUCTURAL AXIOM records — each with its own `@rel:validation:mode`** (the triangle shown; identity/symmetry analogous with `finite:table`):

```turtle
spc:metric:space:kingdom:axiom:phylum:order:class:triangle:order:ternary:family:metric:space:genus:distance:species:subadditivity:component:statement:instance:canonical
    a owl:NamedIndividual , rec:structural:axiom:record ;
    rdfs:label "metric triangle inequality" ;
    rel:notation "for all x,y,z in X: d(x,z) <= d(x,y) + d(y,z)" ;
    rel:validation:mode "bounded:diagnostic" ;
    rel:proof:status    "finite:checked" ;
    rdfs:comment "[S] The TRIANGLE inequality of the metric structural theory (rec:structural:axiom:record): an ORDER/inequality predicate d(x,z) <= d(x,y)+d(y,z), NOT a t_left=t_right equation -- so it is an axiom record, never a rec:equation:record, carrying NO @rel:left/@rel:right. @rel:validation:mode 'bounded:diagnostic' (D24 4-value): decided on the finite 3-point witness by a numeric FILTER(?vxz > ?vxy + ?vyz) (folding fnd:MetricTriangleShape, foundation.shapes.ttl:1248-1251; the probe raises d(A,C) 2->5, spaces.ttl:578-581). @rel:proof:status finite:checked over that witness. Minimal per the axiom plane: no denotatum/gate/provenance/certificate (an axiom is asserted, not proved). [S] phylum:order / class:triangle / genus:distance / species:subadditivity + @rel:validation:mode on an axiom UNATTESTED -> sign-off." .
```

**(f) THEOREM + certificate (ProofArtifact plane)** — a general finite derivation, `@typ:certificate`, `proof:method` honestly "not proof-assistant checked" (`monoid.ttl:157-163` idiom): *metric nonnegativity* — `0 = d(x,x) ≤ d(x,y)+d(y,x) = 2·d(x,y)`, so `d(x,y) ≥ 0` from identity+symmetry+triangle. A `rec:theorem:record` with `@rel:certificate` → a `@typ:certificate` atom carrying `@rel:digest:value` + `@rel:proof:method` + `@rel:source:location`; NEVER a `rec:axiom:record` (the axiom/theorem collapse is a `records.ttl:119` violation).

**(g) GATE (Plane-3)** — `@typ:gate`, `@rel:check:status "declaration reconciled; not a generic semantic proof"` (`monoid.ttl:168-173` verbatim idiom), scoped to the metric-space rung.

**(h) REDUCT + enrichment edges** (in `reducts_space_metric.ttl`, a per-rung file avoiding write races — the `reducts_twoop_vector_space.ttl:26-30` precedent): the metric→uniform **induced-structure reduct** (`rec:reduct:structural:record`) + the metric→commutative-monoid **enrichment seam** (§5). The witness (`fixtures/metric_space_pos.ttl` folding the 3-point space; `fixtures/metric_space_neg.ttl` the `d(A,C)=5` flip) is EVIDENCE.

---

## 2. THE 8-SPACE HIERARCHY — theories + model-classes + REDUCTS (the structural reduct lattice)

The lattice has three branches. **Point-set branch** `TopologicalSpace ← UniformSpace ← MetricSpace` (a uniformity refines to a topology; a metric induces a uniformity + topology). **Analysis branch** anchored on `spine/vector_space.ttl`: `NormedSpace` (norm induces a metric; algebraic reduct onto vector-space + analytic reduct onto metric) → `BanachSpace` (complete normed) and `NormedSpace ← InnerProductSpace` (inner product induces a norm) → `HilbertSpace` (complete inner-product). **Measure branch** `MeasureSpace` (σ-algebra + measure) standalone.

Reduct edges point **child → the structure it induces/refines-to** (a child forgets its added structure to land on the parent), mirroring the algebra forgetful reduct (`spine/vector_space.ttl:123` vector-space `@rel:reduct` module).

| Space | v1 status | added structure / axiom | reduct edge(s) | validation mode(s) | v1 witness OR honest-red deferral |
|---|---|---|---|---|---|
| **TopologicalSpace** | FOLD (`spaces.ttl:287`) | topology `τ⊆P(X)`: ∅,X∈τ; closed under finite ∩ + arbitrary ∪ | branch base (no structural reduct); cross-realm `skos:closeMatch fnd:Site` (point-free specialization, `spaces.ttl:290`) | `finite:table` (all three) | **witness**: discrete topology on {a,b} (FOLD `fnd:topSpaceWitness`, `spaces.ttl:435`); neg: ∩-result off τ |
| **UniformSpace** | BUILD | uniformity `Φ⊆P(X×X)`: filter of entourages ⊇ diagonal, closed under superset/∩/inverse; **composition** `∀U∃V: V∘V⊆U` | → TopologicalSpace (induced topology) | `finite:table` (filter/diagonal/composition on finite witness) | **witness**: discrete uniformity on {a,b} (finite set ⇒ unique uniformity); neg: entourage missing its `V∘V⊆U` half |
| **MetricSpace** | FOLD (`spaces.ttl:302`) | metric `d:X×X→ℝ≥0`: identity-of-indiscernibles, symmetry, triangle | → UniformSpace (E_ε entourages); **enrichment** → commutative-monoid | identity/symmetry `finite:table`; triangle `bounded:diagnostic` | **witness**: 3-point {A,B,C} (FOLD `fnd:metricSpaceWitness`, `spaces.ttl:525`); neg: `d(A,C)=5` |
| **VectorSpace** | already folded (`spine/vector_space.ttl`) | (algebraic — the analysis anchor) | (its own module reduct + scalar-field morphism, `reducts_twoop_vector_space.ttl`) | `finite:table` (GF(3) witness) | **witness**: 1-dim space over GF(3) (`fixtures/vector_space_pos.ttl`) |
| **NormedSpace** | FOLD (`spaces.ttl:317`) | norm `‖·‖:V→ℝ≥0`: positive-definiteness, absolute homogeneity, triangle | **algebraic** → vector-space model-record (algebra-space seam, §5); **analytic** → MetricSpace (d(u,v)=‖u−v‖) | triangle `bounded:diagnostic`; **homogeneity over uncountable field `external:certificate`** | **partial**: finite witness for the reducts + norm-triangle; full homogeneity/positive-definiteness **honest-red** (matches `fnd:` "carries NO normed witness", `spaces.ttl:321`) |
| **BanachSpace** | BUILD | **completeness** (every Cauchy sequence converges) | → NormedSpace (forget completeness) | **`external:certificate` (NOT finitely checkable)** | **NO finite witness** — completeness is an honest-red certificate deferral; only "is a normed space" is checked via the reduct tooth |
| **InnerProductSpace** | FOLD (`spaces.ttl:323`) | inner product `⟨·,·⟩:V×V→F`: conjugate-symmetry, linearity, positive-definiteness | → NormedSpace (‖v‖=√⟨v,v⟩); transitively → Metric + VectorSpace | conjugate-symmetry/linearity `bounded:diagnostic` (finite); **positive-definiteness over uncountable `external:certificate`** | **partial**: finite witness for the algebraic identities + parallelogram-law diagnostic; positive-definiteness **honest-red** (matches `fnd:`, `spaces.ttl:327`) |
| **HilbertSpace** | BUILD | **completeness** (inner-product-induced norm is complete) | → InnerProductSpace (forget completeness) + → BanachSpace (its norm is inner-product-induced) | **`external:certificate` (NOT finitely checkable)** | **NO finite witness** — completeness honest-red certificate deferral |
| **MeasureSpace** | BUILD | σ-algebra `Σ⊆P(X)` (X∈Σ; complement-closed; countable-∪-closed) + measure `μ:Σ→[0,∞]` (μ(∅)=0; σ-additive) | standalone branch; σ-algebra `owl:differentFrom` topology (complement+countable-∪, not arbitrary-∪, §3) | σ-algebra-closure + finite-additivity `finite:table`; **countable additivity / uncountable measure `external:certificate`** | **partial witness**: finite σ-algebra {∅,{a},{b},{a,b}} + counting measure; neg: missing complement / μ(A⊔B)≠μ(A)+μ(B). **Countable additivity honest-red** |

**Completeness is NOT finitely checkable — stated plainly.** Banach and Hilbert are defined by *every Cauchy sequence converging*, a quantifier over infinitely many sequences with a limit that need not lie in any finite witness. No finite graph decides it. Their completeness axiom records therefore declare `@rel:validation:mode "external:certificate"` and `@rel:proof:status "open"` (no v1 witness), and their teeth check only the **normed / inner-product base** through the reduct edge. This is the design's most important honest-red, and it is per the maximal-depth mandate (D20): the atoms are authored, the completeness axiom is honestly certificate-deferred, never faked as `finite:checked`.

---

## 3. THE FULL-LADDER IRI NAMING (D26)

**Surface law (D26):** all lowercase; colon-descent; no `-`/`_` in any typed IRI (file names keep the repo underscore convention); full runtime 12-marker ladder verbatim; segment order matches the reference's natural-language order; **adjective-first compounds** (`inner:product:space`, NOT `product:inner:space`; `metric:space`, `normed:space`, `banach:space`, `hilbert:space`, `uniform:space`, `measure:space`, `topological:space` — replicating the committed `vector:space` / `abelian:group` / `commutative:monoid`, `spine/vector_space.ttl:75-78`).

**Realm question (recommended; Open Question #1).** The algebra tower is `domain:mathematics:realm:algebra:subdomain:<rung>`. Two candidate shapes for spaces:

- **(recommended) three sibling realms** under `domain:mathematics`, matching the honest mathematical taxonomy and letting the analysis branch reduct cleanly across realms: `realm:topology` (Topological, Uniform, Metric), `realm:analysis` (Normed, Banach, Inner-Product, Hilbert — they sit on *both* topology and algebra), `realm:measure` (Measure). All three realm tokens are `[S]` (unattested — the reference corpus is the D26 authority on realm vocabulary).
- **(alternative) a single `realm:space`** with all eight as subdomains — simplest "fold into the tower," but collapses the topology/analysis/measure grouping and mis-suggests measure and topology are one realm.

The recommendation is three realms; the decision is the maintainer's (§7 OQ#1) because realm vocabulary must be lifted from the reference, not invented.

**Directory placement (D25; placement ≠ IRI root).** A **sibling subtree** `basicttl/primordial/type/spaces/**` (NOT under `algebra/`), mirroring the algebra layout, with per-branch subdirs:

```
basicttl/primordial/type/spaces/
  records.ttl                      # rec:structural:theory / structure:signature / structural:axiom / reduct:structural  [S]
  topology/  { topological_space.ttl, uniform_space.ttl, metric_space.ttl }
  analysis/  { normed_space.ttl, banach_space.ttl, inner_product_space.ttl, hilbert_space.ttl }
  measure/   { measure_space.ttl }
  reducts_space_topology.ttl reducts_space_metric.ttl reducts_space_analysis.ttl reducts_space_measure.ttl
  shapes/    { spaces.shapes.ttl + per-space *.shapes.ttl }
  probes/  fixtures/  manifests/  reviews/  receipts/  gates/  bridges.ttl
  checks/run-spaces-checks.sh
```

Spaces live under a sibling of `algebra/` (not inside it) because they are a different realm; but they REUSE the algebra tree's committed record-class parents (`rec:specimen:record`, `records.ttl:48`) and the `spine/vector_space.ttl` / `spine/commutative_monoid.ttl` model-records by IRI (bridge-never-duplicate, §5). Full-ladder IRIs + bridge edges to the primordial short-root / `fnd:` counterparts (D26).

**Per-space descent skeleton** (denotatum plane shown; theory/model/axiom planes follow the metric exemplar §1.5, `[S]` tokens flagged in-file):

| Space | subdomain | denotatum descent tail (after `realm:<r>:subdomain:<sub>`) |
|---|---|---|
| Topological | `topological:space` | `kingdom:type:phylum:space:class:topological:space:order:open:family:family:genus:axiomatic:species:topological:space:component:type:instance:canonical` |
| Uniform | `uniform:space` | `kingdom:type:phylum:space:class:uniform:space:order:entourage:family:filter:genus:axiomatic:species:uniform:space:component:type:instance:canonical` |
| Metric | `metric:space` | `kingdom:type:phylum:space:class:metric:space:order:distance:family:function:genus:axiomatic:species:metric:space:component:type:instance:canonical` |
| Normed | `normed:space` | `kingdom:type:phylum:space:class:normed:space:order:norm:family:function:genus:axiomatic:species:normed:space:component:type:instance:canonical` |
| Banach | `banach:space` | `kingdom:type:phylum:space:class:banach:space:order:complete:family:normed:genus:axiomatic:species:banach:space:component:type:instance:canonical` |
| Inner-product | `inner:product:space` | `kingdom:type:phylum:space:class:inner:product:space:order:inner:product:family:form:genus:axiomatic:species:inner:product:space:component:type:instance:canonical` |
| Hilbert | `hilbert:space` | `kingdom:type:phylum:space:class:hilbert:space:order:complete:family:inner:product:genus:axiomatic:species:hilbert:space:component:type:instance:canonical` |
| Measure | `measure:space` | `kingdom:type:phylum:space:class:measure:space:order:sigma:additive:family:measure:genus:axiomatic:species:measure:space:component:type:instance:canonical` |

All `phylum:space` / `class:<space>` / `order:*` / `family:*` differentia are `[S]` (no runtime precedent) — flagged in each file for the sign-off packet. `realm:topology`/`realm:analysis`/`realm:measure` are `[S]` and gated by OQ#1.

---

## 4. THE TEETH PLAN

All shapes: `constraint:targetClass` (NEVER `constraint:targetNode` — the `run-*-checks.sh` 0-focus anti-pattern gate, `run-algebra-checks.sh:104-108`); a `constraint:sparql` tooth over the reified structure; ≥1 focus node; a positive finite witness that conforms + a failing negative in `fixtures/`. The model-record classes are the vacuous foci (no reified rows); the finite witnesses are where teeth bite.

### 4.1 Finitely-checkable teeth (positive witness + failing negative)

| Space | shape(s) (targetClass) | sh:sparql tooth (reified structure) | positive witness | failing negative |
|---|---|---|---|---|
| Topological | `StructuralTopologyShape` (rec:model:record) — FOLD `fnd:TopologyAxiomsShape` (`foundation.shapes.ttl:1198`) | ∅/X not `@rel:open:member`; OR a `@rel:open:intersection`/`@rel:open:union` whose result is not an open (closure broken) | discrete τ on {a,b} (FOLD `fnd:topSpaceWitness`) | `@rel:intersect:result` repointed off τ (FOLD `fnd:setNonOpen`, `spaces.ttl:430`) |
| Uniform | `UniformityCompositionShape` | an `@rel:entourage:member` with NO `@rel:entourage:composition` half `V∘V⊆U`; OR an entourage not ⊇ diagonal | discrete uniformity on {a,b} | entourage stripped of its composition row |
| Metric | `StructuralMetricTriangleShape` — FOLD `fnd:MetricTriangleShape` (`foundation.shapes.ttl:1248`) | identity `distFrom=distTo ∧ value≠0`; symmetry `(x,y,v1)∧(y,x,v2)∧v1≠v2`; triangle `vxz>vxy+vyz` | 3-point {A,B,C} (FOLD `fnd:metricSpaceWitness`) | `d(A,C)` 2→5 (FOLD probe, `spaces.ttl:580`) |
| Normed | `NormInducesMetricShape` + the vector-space base via the reduct tooth | a `@rel:norm:assertion ‖v‖` whose induced-metric row `d(0,v)` ≠ `‖v‖` (finite consistency); norm-triangle `‖u+v‖>‖u‖+‖v‖` | finite 2-vector normed witness over GF(?)-shaped finite scalars for the reduct + triangle | one `‖u+v‖` raised above `‖u‖+‖v‖` |
| Inner-product | `InnerProductParallelogramShape` | the parallelogram diagnostic `‖u+v‖²+‖u−v‖² ≠ 2‖u‖²+2‖v‖²` over reified `@rel:inner:assertion`; induced-norm `‖v‖²≠⟨v,v⟩` | finite inner-product witness satisfying the parallelogram identity | one `⟨v,v⟩` perturbed so `‖v‖²≠⟨v,v⟩` |
| Measure | `SigmaAlgebraClosureShape` + `FiniteAdditivityShape` | X/∅ not `@rel:sigma:member`; a complement/finite-union result off Σ; a disjoint pair with `μ(A⊔B)≠μ(A)+μ(B)` | finite σ-algebra {∅,{a},{b},{a,b}} + counting measure | complement of {a} repointed off Σ; OR `μ({a,b})≠μ({a})+μ({b})` |
| VectorSpace base (all analysis rungs) | REUSE `VectorSpaceScalarFieldShape` (`shapes/vector_space.shapes.ttl`) via the algebraic reduct tooth (§5) | (unchanged — a "vector space" whose scalars are not a field → RED) | (unchanged) `fixtures/vector_space_neg.ttl` |
| Structural infra | `StructuralTheoryShape` (rec:structural:theory:record), `StructuralAxiomShape` (rec:structural:axiom:record), `StructuralReductShape` (rec:reduct:structural:record) | theory: min1/max1 `@rel:structure:signature` + min1 `@rel:axiom` + identity-collision; axiom: min1/max1 `@rel:validation:mode` ∈ 4-enum; reduct: min1/max1 `@rel:reduct` + collision | the 8 theory records / their axioms / the reduct edges | a theory with no structure-signature; an axiom with no/bogus validation-mode |

### 4.2 Reused hygiene/provenance teeth (unchanged)

`BridgeShape` (every space denotatum `skos:exactMatch/closeMatch` a `fnd:` name, `algebra.shapes.ttl:247`), `ProvenanceShape` (quartet + authority on theory + declaration records, `:226`), `DifferentFromWitnessShape` (σ-algebra ≠ topology and metric ≠ measure never collapse, `:263`), `V1DenotatumHygieneShape` (no provenance on a denotatum), depth gate (≥200-char `rdfs:comment`).

### 4.3 THE HONEST-RED LIST (validation-mode + why deferred)

| honest-red axiom | space(s) | validation-mode | proof-status | why deferred |
|---|---|---|---|---|
| absolute homogeneity `‖a·v‖=|a|·‖v‖` | Normed, Inner, Banach, Hilbert | `external:certificate` | `conditional` | quantifies over an **uncountable** scalar field; no finite witness decides it |
| positive-definiteness `⟨v,v⟩>0 (v≠0)` | Inner, Hilbert | `external:certificate` | `conditional` | positivity over an uncountable carrier; the finite witness checks only the algebraic identities |
| **completeness** (every Cauchy sequence converges) | **Banach, Hilbert** | `external:certificate` | `open` | quantifies over infinitely many sequences with limits outside any finite graph — **NOT finitely checkable** (§2); the atoms carry NO completeness witness |
| **countable (σ-)additivity** `μ(⊔ᵢAᵢ)=Σμ(Aᵢ)` | Measure | `external:certificate` | `open` | a countable sum over an uncountable σ-algebra; only the **finite-additivity** restriction is `finite:table` v1 |
| uncountable/continuum point sets | all (carriers) | `external:certificate` | `open` | v1 carries only finite worked witnesses (the `fnd:` honest-red, `spaces.ttl:310`); transfinite carriers deferred to W5 |

Each honest-red axiom is still AUTHORED (maximal-depth mandate, D20): the `rec:structural:axiom:record` exists and declares its mode + status; it simply carries no finite witness and its tooth does not claim `finite:checked`. `StructuralAxiomShape` still requires the mode to be present and in-enum, so an axiom cannot silently drop its honesty tag.

---

## 5. THE REDUCT SEAM TO THE ALGEBRA TOWER (the algebra-space seam)

Two seams, both realized as `rec:reduct:structural:record` edges in per-branch reduct files (the `reducts_twoop_vector_space.ttl` per-rung-file / bridge-never-duplicate precedent, `:26-40`), reusing the committed algebra model-records **by IRI**, never re-minting them.

**(1) The metric enrichment seam (folds `fnd:enrichedOver`, `spaces.ttl:242-245,504-508`).** A metric space is Lawvere-enriched over the commutative monoid `([0,∞],≥,+)` (triangle = arrow composition, `d(x,x)=0` = identity arrow). Fold as an `@rel:enrichment` edge from the metric-space theory/model-record → `spine/commutative_monoid.ttl`'s commutative-monoid model-record (the `[0,∞]` base = the folded `fnd:nonnegRealsMonoid`). This grounds the point-set branch DOWN onto the T4 algebra tower (Directive 18: spaces on algebra on set theory) as a graph edge, not a slogan.

**(2) The analysis algebraic seam (folds `fnd:NormedSpace rdfs:subClassOf fnd:VectorSpace`, `spaces.ttl:36,319`).** Normed / Inner-Product / Banach / Hilbert each carry, in `reducts_space_analysis.ttl`, TWO reduct edges + one connecting morphism — exactly the vector-space-as-reducts shape (`reducts_twoop_vector_space.ttl`):

- **algebraic reduct** (`rec:reduct:structural:record`): the space model-record → `spine/vector_space.ttl`'s **vector-space model-record** (REUSED by IRI). "A normed space IS a vector space" made a reduct edge (the `fnd:NormedSpace rdfs:subClassOf fnd:VectorSpace` subsumption). The vector-space base is teeth-proved by the EXISTING `VectorSpaceScalarFieldShape` over the shared vector-space witness — NOT re-authored (the shared-tooth discipline, `spaces.ttl:38`).
- **analytic reduct** (`rec:reduct:structural:record`): the space model-record → the **metric-space model-record** (a norm induces a metric `d(u,v)=‖u−v‖`; an inner product induces a norm which induces a metric). This is how the analytic structure lands on the point-set branch.
- **analytic-structure connecting morphism** (analogue of the scalar-field morphism, `reducts_twoop_vector_space.ttl:88-101`): `@rel:connects` BOTH the algebraic reduct AND the analytic reduct, `@rel:equation` → the norm (resp. inner-product) axiom record — the morphism that **adds the analytic structure on top** of the algebraic carrier and glues it to the induced metric. This is where `‖·‖` / `⟨·,·⟩` is added on top of the vector space.

So a NormedSpace decomposes as: *(the whole vector-space structure)* + *(a norm morphism)* → *(the induced metric)*; Banach = NormedSpace + the (certificate-deferred) completeness axiom; InnerProductSpace = NormedSpace + an inner-product morphism whose induced norm satisfies the parallelogram law; Hilbert = InnerProductSpace + completeness. The seam keeps the algebraic part in the algebra realm (reused, not copied) and the analytic part in the spaces realm (added on top).

---

## 6. FOLD + DEMOLISH PLAN

### 6.1 What folds (the 4 existing `fnd:` spaces)

`fnd:TopologicalSpace` (`spaces.ttl:287`), `fnd:MetricSpace` (:302), `fnd:NormedSpace` (:317), `fnd:InnerProductSpace` (:323) → new full-ladder structural-theory atoms with `skos:exactMatch` (denotatum) + `@rel:historical:identity` (theory) bridges back to `fnd:`. Their reified structure (`fnd:OpenIntersection`/`OpenUnion`/`hasOpenSet`, `fnd:DistanceAssertion`/`SpacePoint`) → refolded reified rows in `fixtures/`. Their witnesses (`fnd:topSpaceWitness`, `fnd:metricSpaceWitness` + the nine distance rows) → `fixtures/*_pos.ttl` + the `_neg.ttl` probes-of-record. `fnd:enrichedOver fnd:nonnegRealsMonoid` → the metric enrichment reduct edge (§5.1). `fnd:NormedSpace rdfs:subClassOf fnd:VectorSpace` / `fnd:InnerProductSpace rdfs:subClassOf fnd:NormedSpace` → the analysis reduct edges (§5.2).

### 6.2 What is built new (the 4)

`UniformSpace`, `MeasureSpace`, `BanachSpace`, `HilbertSpace` — no `fnd:` predecessor; authored as cited standard mathematics (SYN), `@rel:authority "SYN"`, `[S]` tokens flagged (the `spine/vector_space.ttl:56-63` SYN precedent). UniformSpace + MeasureSpace ship finite witnesses; Banach + Hilbert ship completeness as `external:certificate` honest-red with NO finite witness (§4.3).

### 6.3 The sheaf/site core disposition (RECOMMENDATION)

`fnd:Site` / `fnd:Cover` / `fnd:Sheaf` / `fnd:MatchingFamily` / `fnd:LocalSection` + `fnd:PerceptualTessellation` (`spaces.ttl:66-165,331-402`) are a **different category/topos realm**, not point-set spaces: a Grothendieck site is *point-free* topology living in the Presheaf/Sheaf apparatus (`fnd:Sheaf rdfs:subClassOf fnd:Presheaf`, `spaces.ttl:158`), tied to the Pillar-4 **category seam** the monoid fold explicitly deferred to the **category fan-out** (`monoid.ttl:22-25`, the `q_monoid_is_endo` "monoid = one-object category" re-homing). **Recommendation: PRESERVE the sheaf/site core in `fnd:` byte-intact for the spaces pass, and fold it later into a `realm:category` / `realm:topos` subtree in the category fan-out — do NOT fold it into `spaces/`.** Folding point-free category theory into `realm:space` would mis-file it. The `fnd:TopologicalSpace` "specialization leaf of the `fnd:Site` progenitor" relation (`spaces.ttl:290`) becomes a cross-realm `skos:closeMatch` / `seed:conservativeBridge` edge (topological:space → the point-free site specialization), not a fold. `SheafGluesShape` (`foundation.shapes.ttl:1156`) stays with the preserved core. This is an honest-red scoping decision surfaced as **OQ#2**.

### 6.4 Stage-3c-spaces demolition scope (CI lockstep)

Two-stage, matching the algebra `B3(a) additive → T-RETIRE stub` cadence (`monoid.ttl:36-37`):

- **Stage additive** (the fold): author `basicttl/primordial/type/spaces/**` + the bridges; NO `fnd:`/foundation edit; `fnd:` spaces stay byte-intact and resolvable through the bridges. Author `checks/run-spaces-checks.sh` (the `run-algebra-checks.sh` clone: discover `spaces/**/*.ttl` minus shapes/fixtures; merge `spaces/shapes/*.shapes.ttl`; fixture-polarity; 0-focus; count-coverage; gates V0–V8; depth) and **wire it into `ci.yml` IN LOCKSTEP** (D25: `ci.yml`'s `ontology-floors` job globs `basicttl/foundation/*.ttl`; the folded tree is in NO runner unless one is added — `run-algebra-checks.sh:5-11`).
- **Stage-3c-spaces T-RETIRE** (the demolition): STUB the four `fnd:` space classes (leave a bridge shell pointing at the folded atoms). **Re-home the `VectorSpace` reference**: `fnd:NormedSpace rdfs:subClassOf fnd:VectorSpace` → the normed-space algebraic reduct onto `spine/vector_space.ttl` (already the fold target, §5.2). **Re-home `fnd:enrichedOver`** → the metric enrichment reduct. **Migrate the space teeth** out of `foundation.shapes.ttl`: `TopologyAxiomsShape` → `StructuralTopologyShape`, `MetricTriangleShape` → `StructuralMetricTriangleShape`; the normed/inner slices of `VectorSpaceAxiomsShape` stay in the algebra realm (they are the vector-space base, reused via the reduct). `SheafGluesShape` stays (sheaf core preserved, §6.3). **Re-home `reanchor.ttl:82,268`** `fnd:groundsInSpace fnd:metricSpaceWitness` (SP3's geographic plane grounds into the metric witness) → the folded metric-space witness, keeping the SP3 bridge resolvable. **CI lockstep, again**: removing spaces content from `basicttl/foundation/*.ttl` makes the foundation runner's auto-discovered space ASKs (`run-foundation-checks.sh:71`) vacuous unless the runner + `foundation.queries.sparql` + `foundation.shapes.ttl` tooth-register move in the same commit (`run-foundation-checks.sh:176`). Honor `commit_signing_trust.ttl` (D25). No git in this DESIGN pass.

---

## 7. OPEN QUESTIONS (maintainer only)

**OQ1 — Realm naming.** Three sibling realms `realm:topology` (Topological/Uniform/Metric) + `realm:analysis` (Normed/Banach/Inner-Product/Hilbert) + `realm:measure` (Measure) under `domain:mathematics` — matching the mathematical taxonomy and letting the analysis branch reduct across realms onto both topology and algebra — OR a single `realm:space` with all eight as subdomains (simplest "fold into the tower")? All realm tokens are `[S]` (unattested); the reference corpus is the D26 authority on realm vocabulary, so this must be lifted, not invented. (Recommend three realms.)

**OQ2 — Sheaf-core disposition.** Preserve `fnd:Site`/`Cover`/`Sheaf`/`MatchingFamily`/`LocalSection`/`PerceptualTessellation` byte-intact in `fnd:` for the spaces pass and fold them later into a `realm:category`/`realm:topos` subtree in the category fan-out (they are point-free category theory, tied to the deferred Pillar-4 category seam), OR fold them now into `spaces/`? (Recommend preserve-then-category-fold.)

**OQ3 — How far to push completeness certificates in v1.** Banach/Hilbert completeness and countable (σ-)additivity are `external:certificate` honest-red — NOT finitely checkable. Ship all four "complete"/measure atoms now with the completeness / σ-additivity axioms authored as certificate-deferred (`proof:status open`, no finite witness, teeth only on the normed/inner/finite-additive base), OR defer BanachSpace + HilbertSpace + σ-additivity entirely to a later analysis pass and ship only the six finitely-witnessable spaces in this fold?

---

## Review addendum (adversarial pass, 2026-09-06)

Verdict: **GREEN with corrections applied below.** The hierarchy directions, the non-algebraic structural-theory template, the honesty of the validation modes, the D24/D26 conformance, the reduct seam onto `spine/vector_space.ttl`, and the teeth non-vacuity are all correct. Five items were found; four are minor and one (R3) is a modeling-soundness clarification. Each is resolved here rather than by rewriting the body.

**What was re-verified against source (all confirmed accurate):**
- Reduct directions are all the correct forgetful direction (child → the less-structured parent it forgets its added structure onto): Metric → Uniform → Topological (a metric induces a uniformity induces a topology; class containment `{metric} ⊆ {uniform} ⊆ {topological}`); Normed → Metric (`d(u,v)=‖u−v‖`) and Normed → VectorSpace; Banach → Normed (forget completeness); Inner → Normed (`‖v‖=√⟨v,v⟩`); Hilbert → Inner **and** Hilbert → Banach (the diamond — a Hilbert space is both a complete inner-product space and a Banach space whose norm is inner-product-induced); Measure standalone. No direction is inverted.
- The parallel-class idiom is faithful to the committed precedent: `rec:reduct:two:operation:record a owl:Class ; rdfs:subClassOf rec:specimen:record` (NOT `rec:reduct:record`), `reducts_twoop.ttl:54-56`; the vector-space "module reduct + scalar-FIELD strengthening morphism" with `@rel:connects`/`@rel:reduct`/`@rel:equation`, `reducts_twoop_vector_space.ttl:15-45` — the analysis connecting-morphism design (§5) mirrors it edge-for-edge.
- The B4 idiom citations check out: `spine/monoid.ttl:22-25` (category deferral), `:65-90` (theory record shape + `@rel:validation:mode`/`@rel:proof:status`/`@rel:historical:identity`/`skos:closeMatch`), `:157-163` (`@typ:certificate`, "not proof-assistant checked"), `:168-173` (`@typ:gate` `check:status` verbatim); `spine/commutative_monoid.ttl` and `spine/vector_space.ttl` exist as reduct-seam targets; `fnd:nonnegRealsMonoid a fnd:CommutativeMonoid` (`spaces.ttl:504`) is the enrichment base.
- **Completeness honesty is correct and is the design's strongest point:** Banach/Hilbert completeness and countable σ-additivity are stated `external:certificate` / `proof:status open`, no finite witness, explicitly "NOT finitely checkable" (§2, §4.3, OQ3) — never faked as `finite:table`. The `StructuralAxiomShape` still focuses these honest-red axiom records and checks the mode is present + in-enum, so there is no 0-focus vacuity and the honesty tag cannot be silently dropped.

**R1 (minor — metric axiom naming/tooth scope).** §1.5(e) / §2 / §4.1 label the finite metric identity axiom "identity-of-indiscernibles" but the folded tooth (inherited from `fnd:` via `spaces.ttl:315`) only checks the `d(x,x)=0` half (`distFrom=distTo ∧ value≠0 → RED`). The *separation* half — `d(x,y)=0 ∧ x≠y → RED`, the axiom that distinguishes a **metric** from a **pseudometric** — is not checked, yet it **is** finitely checkable on the 3-point witness. Resolution: either (a) strengthen the finite tooth with a second `finite:table` clause `∃(x,y): x≠y ∧ d(x,y)=0 → RED` (preferred — it is finitely decidable and makes the atom a genuine metric, not a pseudometric), or (b) rename the checked axiom honestly as "identity / self-distance-zero (`d(x,x)=0`)" and mark the separation half a separate `finite:table` axiom. Adopt (a) in the build.

**R2 (minor — validation-mode consistency).** §4.3 defers norm **absolute homogeneity** `‖a·v‖=|a|·‖v‖` as `external:certificate` because it quantifies over an uncountable scalar field, but §2 gives inner-product **linearity** as `bounded:diagnostic` (finite). Linearity carries the *same* "for all scalars `a`" quantifier over the same uncountable field. Resolution: treat them identically — the *full* laws (homogeneity and linearity) are both `external:certificate`; only a **bounded diagnostic over specific enumerated scalar instances** is finite. Reclassify inner-product linearity's full form to `external:certificate` and keep only its finite instance-diagnostic as `bounded:diagnostic` (and add homogeneity's finite instance-diagnostic symmetrically if a norm-value witness carries scalar-scaled rows).

**R3 (modeling soundness — the one real muddle, fix required).** §4.1's Normed row says "finite 2-vector normed witness **over GF(?)-shaped finite scalars** for the reduct + triangle." This conflates two *different* witnesses. A genuine real-valued norm satisfying homogeneity requires an **infinite (valued) scalar field** — you cannot put a nontrivial `[0,∞)`-valued norm on a `GF(p)` vector space (a finite field carries no archimedean absolute value, so the only such "norm" is trivial). The norm-triangle tooth must therefore be a **finite table of reified real norm-VALUE rows** `‖0‖=0, ‖u‖, ‖v‖, ‖u+v‖` over *named* vectors (`0,u,v,u+v`) checked by a numeric FILTER `‖u+v‖ > ‖u‖+‖v‖ → RED` — exactly the metric-triangle idiom, and **scalar-field-agnostic**. This is separate from the **algebraic-reduct base**, which *is* teeth-proved by the existing `GF(3)` `VectorSpaceScalarFieldShape` witness (§5). Resolution: split §4.1's Normed witness into (i) the algebraic-reduct witness (reuse the `GF(3)` vector-space fixture, unchanged) and (ii) a `bounded:diagnostic` norm-value fixture (real values on named vectors, no finite scalar field). Same correction applies to the Inner-product parallelogram/induced-norm rows (`⟨·,·⟩`/`‖·‖` values are reals on named vectors, not finite-field-valued).

**R4 (explicitness — prevents an executor foot-gun).** The body types the metric exemplar atoms `a … rec:structural:theory:record` etc. but never shows the class declarations. State explicitly in `spaces/records.ttl` that all four minted classes — `rec:structural:theory:record`, `rec:structure:signature:record`, `rec:structural:axiom:record`, `rec:reduct:structural:record` — are `rdfs:subClassOf rec:specimen:record` (the `reducts_twoop.ttl:54-56` precedent), **NOT** `subClassOf` their algebra namesakes (`rec:theory:record` / `rec:signature:record` / `rec:axiom:record` / `rec:reduct:record`). Under `inference=rdfs` a structural-theory record typed as a subclass of `rec:theory:record` would be materialized as an instance of `rec:theory:record` and then **falsely reddened** by the algebra `TheoryShape` (`min1 @rel:equation`, `algebra.shapes.ttl:72-87`) — the exact cross-tower bite the parallel-class discipline exists to prevent. (The `rec:model:record` / `rec:declaration:record` / `rec:denotatum:record` planes are correctly REUSED, not re-minted — those are structure-agnostic and the algebra `ModelShape`/per-law teeth stay vacuous on spaces because they are guarded by algebra-only predicates `@rel:identity:element` / `@rel:carrier:member` / `@rel:structure`+`@rel:category:result`, which the scoped-predicate discipline keeps distinct from the space row predicates.)

**R5 (note, no change).** The §2 disjointness `metric model-record owl:disjointWith measure model-record` is sound as a *record-type* homonym-distinction tooth and, as §1.5(d) already states, must NOT be read as "no carrier bears both a metric and a σ-algebra" (a Borel σ-algebra on a metric space bears both); the design already scopes it correctly to the declaration records, not the carriers. Flagged only so the build preserves that wording.

These corrections are surgical (tooth clauses + one witness split + one explicit `subClassOf` line) and do not disturb the template, the hierarchy, the reduct lattice, or the honest-red boundary. The three open questions above stand unchanged for the maintainer.
