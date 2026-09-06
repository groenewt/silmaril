# 00 — REFMAP SYNTHESIS (the reference-conformant fold template for SP0 Pass-1)

MAP-synthesis shard. Consolidates the four refmap evidence shards (R1 naming-grammar, R2
consolidated-shape, R3 engine-algebra-skills, R4 docs-doctrine-gates — all read in full) into ONE
actionable template the planner/executor uses to reshape the algebra spine
(magma→semigroup→monoid→commutative-monoid→group→abelian + quasigroup/loop) into
`basicttl/primordial/type/**` per Directives 24 (Seed-Carrier) + 25 (fold, spine-first).

Praeriehund honesty preserved: every structural claim carries a file:line / grep-count provenance to
a shard or a primary file. Where the reference and the governing directives CONFLICT, this synthesis
states the conflict and defers to the planner/maintainer (§6, §7) — it does not silently pick.

Sources: `ledger/W2/sp0-reshape/refmap/{R1_naming_grammar,R2_consolidated_shape,R3_engine_algebra_skills,R4_docs_doctrine_gates}.md`;
`ledger/W2/design_constraints.md` D21–25; `ledger/W2/sp0-reshape/RECOVERY.md`;
`silmaril.final.consolidated.ttl` (root); `refcomp/{zip/silmaril,tar/bash}/**`;
on-disk fold target `basicttl/primordial/type/**` + inbound `basicttl/foundation/algebra_spine.ttl`.

---

## 1. THE DEFINITIVE NAMING LAW THE FOLD ADOPTS

### 1.1 Two grammars are in evidence — the fold lives in the primordial one

There are **three distinct URN grammars** in the corpus, and the reconciliation hinges on keeping
them straight:

| grammar | root | example | where | authority |
|---|---|---|---|---|
| **A. Full-taxonomy runtime descent** | `urn:silmaril:type:graph:instance:instruction:code:property:` + 12-marker Linnaean ladder | `…:property:domain:mathematics:realm:algebra:subdomain:group:kingdom:type:phylum:algebra:class:group:order:binary:family:operation:genus:axiomatic:species:group:component:type:instance:canonical` | verified bash engine `aob/urn/**` (293 atoms, all 12 markers 293/293 — R1 §1c), `ontology/primordial.yaml`, root consolidated instances | the VERIFIED RUNTIME |
| **B. Degenerate collapsed spine** | same head, but 8 Linnaean ranks pinned to constants + real concept in a free tail after `specimen:instance:` | `…:kingdom:knowledge:phylum:formal:class:typed:order:declarative:family:execution:genus:graph:species:runtime:specimen:instance:<TAIL>` | root `silmaril.final.consolidated.ttl` (3403 instances, R1 §2-note) | ANTI-PATTERN — do NOT copy (baseline.md:12 "no fused/padded ranks") |
| **C. Primordial fold-target root** | `urn:silmaril:primordial:type:` (+ `…:class:` for `family:`, `urn:silmaril:prim:#` for `primitive:`) | `family:Frame`, `model:ClassDeclaration`, `model:Product` | on-disk `basicttl/primordial/type/**` (frame.ttl:1-3, schema.ttl:1-2) | the D25 FOLD TARGET |

**Ruling (D25 is dispositive):** Directive 25 says the reshaped floor "lands INSIDE
`basicttl/primordial/type/**`, adopting its IRI root + directory/file layout + lowercase-colon-descent
grammar" (design_constraints.md:486-488). The on-disk fold target uses **grammar C**
(`@prefix model: <urn:silmaril:primordial:type:>`, frame.ttl:1). Therefore **the fold's typed IRIs are
minted under `urn:silmaril:primordial:type:` (grammar C root)**, rendered in **grammar A's
naming discipline** (lowercase, colon-descent, genus-first — D24 §10b), FIXING grammar C's current
CamelCase/punning flaw (frame.ttl:7 `family:Frame a ontology:Class, model:Product, model:Frame` is the
punning D25 forbids — R3 §7, F3).

So the definitive surface law = **grammar-A per-segment discipline applied under the grammar-C root**.
The full 12-marker runtime ladder (grammar A) is NOT reproduced verbatim in the fold's own IRIs; it is
reached by the **seed/engine bridge** (§3) via `schema:seeAlso` / `skos:*Match` / `seed:*Bridge`
edges, so the runtime lineage stays resolvable without importing the head. (This is the single largest
grammar reconciliation and is restated as OPEN QUESTION Q1 in §7 for maintainer confirmation, because
grammar C's short root is not itself the verified-runtime grammar.)

### 1.2 The per-segment surface law (adopted verbatim — D24 §10b, confirmed by every source)

1. **All lowercase**, every segment. Confirmed: 0 uppercase in any `urn:silmaril:*` across root + aob
   + primordial.yaml (R1 §4).
2. **Colon-descent**; compounds decompose into `:` segments; **no `-` / `_`** in any typed identifier
   (file names keep the repo underscore convention). Confirmed across all sources (R1 §4; R4 §3.E).
3. **Genus-first for differentia**: `monoid:commutative` (2 occ) / `commutative:monoid` (0);
   `group:abelian` (4) / `abelian:group` (0); `ring:division`, `field:finite`, `module:free` all
   genus-first (R1 §4). A qualifier is a LATER segment than what it qualifies.
4. A rank/qualifier VALUE **may span multiple segments** (`species:one:hundred:twenty:eight`,
   `subdomain:bit:width`) — the marker keywords are reserved delimiters, values are free (R1 §1c).

### 1.3 The rank ladder (grammar A — the reference lineage the bridge targets)

The verified-runtime rank ladder every bridged atom carries (R1 §1c, 293/293), for cases where the
fold emits a full-taxonomy lineage record (manifests, bridge targets, or if Q1 resolves toward
grammar A):

```
urn:silmaril : type:graph:instance:instruction:code:property        (fixed literal head)
  : domain:<D> : realm:<R> : subdomain:<SD>                          (context wrapper)
  : kingdom:<K> : phylum:<P> : class:<C> : order:<O>                 (Linnaean core, upper)
  : family:<F> : genus:<G> : species:<S>                            (Linnaean core, lower)
  : component:<CMP> : instance:<I>                                   (facet + occurrence)
```

Per-rank value vocabularies are enumerated in R1 §2 (kingdom: `type|axiom|law|theorem|certificate|
definition|construction|…`; phylum: `algebra|axiom|composition|operation|…`; etc.). NOTE the runtime
uses `component:instance` as the final marker pair; the root drop's `specimen:instance` is the
collapsed variant — **follow the runtime `component`/`instance`** (R1 §2-note).

### 1.4 Refinements / conflicts vs Directive 24 §10b

- **[AGREE]** lowercase, colon-descent, no `-`/`_`, genus-first differentia — reference and D24 concur.
- **[CONFLICT — Q2 in §7] multi-word proper names.** D24 §10b prescribes
  `NaturalTransformation → transformation:natural` and `CategoryOfElements → category:elements`
  (design_constraints.md:457). The reference (root drop AND bash engine) instead uses
  **adjective-first** `natural:transformation` (9 occ vs 0) and keeps the stop-word:
  `category:of:elements` (12 occ vs 0) (R1 §4, R4 §3.B `construction:embedding:yoneda`,
  `category:elements`). D24 is governing law; the reference is the implementation; they disagree.
  Planner/maintainer must rule: either D24's two examples are amended to match the reference, or the
  reference renderings are renormalized on the way in.
- **[NOTE] primary text absent.** `USER_REF_00.md` and `docs/specs/2026-08-19-seed-carrier-rewrite-
  design.md §10b` are NOT in repo/scratchpad (uncommitted zip); D24's quoted summary is the only
  in-repo authority (R1 §4 gap). `docs/continuation/capture.md:11` independently corroborates the
  "ranked observation URN" model.

---

## 2. THE ALGEBRA-SPINE RECORD + SHAPE TEMPLATES (reference form)

### 2.1 What the reference actually carries (and what it LACKS)

- The consolidated algebra tower is a **bare `subClassOf` ladder of 17 "primitive" class stubs**
  (magma…field + signature/term/equation/action), **ZERO instances, ZERO reducts** (`:reduct:` = 0
  across final.consolidated) (R2 §3). The engine tower is even flatter — six leaves
  `SET/CLASS/GROUP/CATEGORY/TOPOLOGY/GEOMETRY`, no magma/semigroup/monoid rungs, GROUP crams all four
  axioms into one leaf (R3 F1, §2.3).
- **Therefore the theory/model/reduct/(S,Ω,E) content MUST BE AUTHORED by the fold** — it cannot be
  copied from either the consolidated stubs or the crammed engine leaf (R2 §7.1, R3 §7).
- BUT the reference's **richer sibling corpus DOES carry the doctrine-conformant template** as a
  46-edge intensional `…:specification` descent + `seed:algebra:foundation:*` records
  (`carrier/category/model/olog/construction/theorem/axiom` + predicates `interpreted:by /
  modeled:within / presented:by / has:certificate / depends:on`) (R4 §3.B, structure.md:71-118). This
  is the Lawvere theory/model/reduct stratification realized — MATCH it, do not reinvent (R4 §6.2).

### 2.2 The stratification the fold instantiates (D24 A0/A6, confirmed against reference)

A spine concept is NEVER one node. It is a family of distinct-IRI records across the disjoint planes
(D24 A0 forbids `fnd:Group a owl:Class, fnd:PresentedAlgebra` — design_constraints.md:436):

| plane | record kind | reference evidence |
|---|---|---|
| **Theory** | `theory:<name>` = (S,Ω,E): a signature + operation-symbols + equation set | to be AUTHORED (absent in ref — R2 §3); template R2 T2 |
| **Model** | `model:<name>` class + a carrier + validation-MODE | `seed:algebra:foundation:model:seed` (R4 §3.B); finite-table model R2 §1g |
| **Axiom (foundation)** | `axiom:<theory>:<law>` — object of `relation:foundation`, NO certificate | exactly 6 in consolidated (R2 §1d); each law a distinct IRI |
| **Equation** | `equation:<…>` = reified `left = right` pair | `relation:left`(82)/`right`(81)/`pair`(81) (R2 §2) |
| **Element** | `element:<…>` carrier members | finite:element (3), finite:object (5) (R2 §1g) |
| **Theorem + Certificate** | `theorem:<…>` → `relation:certificate` → `certificate:<…>` (digest + proof-method); NEVER an axiom | Yoneda ×3 theorem+cert (R2 §1e); "No seventh axiom" (math.md:58, R4 §3.B) |
| **Reduct / theory-morphism** | `relation:reduct` edge (ring = additive-abelian-group reduct + mult-monoid reduct + distributivity) | ZERO in ref — AUTHOR NEW (R2 §3, T2) |

### 2.3 The record envelope (the 1:1:1 Declaration/Denotatum/Gate triad — R2 §1b)

Every declared spine concept materializes as THREE distinct IRIs (445:445:445 in ref):

```
<theory:magma>          a owl:NamedIndividual, <…:type:declaration> ;
    <…:relation:denotatum>           <theory:magma:denotatum> ;    # what it means (Denotatum plane)
    <…:relation:assignment>          <theory:magma:gate> ;         # how admission was checked (Gate)
    <…:relation:historical:identity> <urn:silmaril:kind:algebra:magma> ;   # compat bridge (D24)
    <…:relation:identifier> "…:theory:magma" ;
    <…:relation:notation>   "magma" ;
    <…:relation:primary:taxon> <…:taxon:theory> ;
    <…:relation:source:location> "…/algebra/…ttl" ;
    <…:relation:created> … ; <…:relation:modified> … ; <…:relation:version> … ; <…:relation:state> … ;
    <…:relation:authority> "SYN|DS|PD" ; <…:relation:ground> … .
<theory:magma:denotatum> a owl:NamedIndividual, <…:type:theory:denotatum> ; … .
<theory:magma:gate>      a owl:NamedIndividual, <…:type:gate> ;
    <…:relation:check:status>   "declaration reconciled; not a generic semantic proof" ;  # honest verdict
    <…:relation:interpreted:by> <…:interpretation:algebraic:theory:record> .
```

Provenance quartet `created/modified/version/state` is uniform on every record (828 each, R2 §2);
`identifier`+`notation` are near-universal (3516/3027); `historical:identity` is the bridge (1670).
Check-status strings are honest and NEVER a claimed proof:
`"declaration reconciled; not a generic semantic proof"` (gate, 445) /
`"preserved declaration; original axioms not admitted into corrected kernel"` (quarantine, 1223).

### 2.4 The 6-axiom pattern (verbatim, R2 §1d)

An axiom is minimal, is an OBJECT of `relation:foundation`, carries NO certificate, and diverges from
its theory-siblings only at the `class:<lawname>` segment (R1 §5b):

```
<axiom:magma:closure> a owl:NamedIndividual, <…:type:axiom> ;
    <…:relation:identifier>      "…:axiom:magma:closure" ;
    <…:relation:notation>        "magma closure" ;
    <…:relation:source:location> "docs/research/proofs.md"|"…/algebra/…ttl" ;
    <…:relation:equation>        <equation:magma:closure> .
<…:ontology:sp0:spine> <…:relation:foundation> <axiom:magma:closure> .    # foundation membership
```
closure.ttl intensional variant adds `rdfs:comment "<law statement>. Checked exhaustively; not
inferred from a label."` and types it `…:species:axiom:record` (R2 §5a). Laws of one theory share
`subdomain`+`family`, diverge at `class` → distinct IRIs per law (R1 §5b; satisfies D24 A0 no-collapse).

### 2.5 Intensional record classes (closure.ttl idiom — R2 §5a) — the OWL the flat graph lacks

The consolidated instance graph has ZERO `owl:Restriction` (D23 diagnostic, design_constraints.md:422).
closure.ttl supplies the intensional layer the fold MUST carry: a record class = `rdfs:subClassOf` a
bundle of cardinality-1 restrictions + a parent + `owl:disjointWith`:

```
<…:class:equation:record> a owl:Class ;
    rdfs:subClassOf [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:relation:left> ],
                    [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:relation:right> ],
                    <…:class:specimen:record> .
```

### 2.6 THE MONOID RUNG END-TO-END (reference IRI grammar, worked)

Shown in grammar-C root + grammar-A discipline (the fold's actual output), with the runtime
full-taxonomy bridge target given for each. `M:` abbreviates the prefix
`urn:silmaril:primordial:type:` (frame.ttl:1); bridge targets are the verified-runtime grammar-A IRIs.

**(a) Theory** — monoid = semigroup + a nullary identity operation + two identity equations:
```
M:theory:monoid                     a owl:NamedIndividual, M:type:declaration ;
    M:relation:signature            M:signature:monoid ;              # Ω = {∙ (binary), e (nullary)}
    M:relation:equation             M:equation:monoid:associativity ,
                                    M:equation:monoid:identity:left ,
                                    M:equation:monoid:identity:right ; # two-sided ⇒ TWO records (D25:497)
    M:relation:reduct               M:theory:semigroup ;              # monoid → semigroup theory-morphism
    M:relation:historical:identity  <urn:silmaril:kind:algebra:monoid> ;
    M:relation:validation:mode      M:mode:finite:table ;
    M:relation:proof:status         M:status:literature:backed ;
    M:relation:identifier "…:theory:monoid" ; M:relation:notation "monoid" ;
    M:relation:denotatum M:theory:monoid:denotatum ; M:relation:assignment M:theory:monoid:gate ;
    M:relation:authority "SYN" ; M:relation:created … ; M:relation:version … ; M:relation:state … .
# engine bridge → group IDENTITY axiom atom (primordials.yaml:478-482; R3 §6):
M:theory:monoid  seed:conservativeBridge
    <urn:silmaril:type:graph:instance:instruction:code:property:domain:mathematics:realm:algebra:subdomain:group:kingdom:axiom:phylum:operation:class:identity:order:binary:family:group:genus:neutral:species:member:component:statement:instance:canonical> .
```
**(b) Signature** (Ω):
```
M:signature:monoid a owl:NamedIndividual, M:type:signature:record ;
    M:relation:operation M:operation:monoid:product ,        # arity 2
                         M:operation:monoid:unit .           # arity 0
M:operation:monoid:product a M:type:operation ; M:relation:arity "2" ;
    M:relation:domain M:sort:monoid:carrier ; M:relation:codomain M:sort:monoid:carrier .
M:operation:monoid:unit    a M:type:operation ; M:relation:arity "0" ;
    M:relation:codomain M:sort:monoid:carrier .
```
**(c) Equations** (reified left=right; identity two-sided ⇒ two records):
```
M:equation:monoid:identity:left  a M:type:equation:record ;
    M:relation:left  "product(unit, x)" ; M:relation:right "x" ; M:relation:pair M:equation:monoid:identity:left:pair .
M:equation:monoid:identity:right a M:type:equation:record ;
    M:relation:left  "product(x, unit)" ; M:relation:right "x" .
M:equation:monoid:associativity  a M:type:equation:record ;
    M:relation:left  "product(product(x,y),z)" ; M:relation:right "product(x,product(y,z))" .
```
**(d) Foundation axioms** (one per law; monoid ADDS identity over semigroup's associativity):
```
M:axiom:monoid:identity a owl:NamedIndividual, M:type:axiom ;
    M:relation:notation "monoid identity" ; M:relation:equation M:equation:monoid:identity:left ,
                                                                M:equation:monoid:identity:right .
M:ontology:sp0:spine M:relation:foundation M:axiom:monoid:identity .
```
**(e) Model + finite-table witness** (moved to `fixtures/`, NOT the ontology module — D24 four planes):
```
M:model:monoid:boolean:and a owl:NamedIndividual, M:type:model ;
    M:relation:interpreted:by M:theory:monoid ; M:relation:carrier M:carrier:monoid:boolean ;
    M:relation:validation:mode M:mode:finite:table .
# fixtures/monoid/positive.ttl — reified composition cells (R2 T7); + fixtures/monoid/negative.ttl (REQUIRED)
```
**(f) Intensional class** (closure.ttl idiom): `M:class:theory:record` `rdfs:subClassOf`
cardinality-1 on `relation:signature` + `min 1 relation:equation`, `owl:disjointWith M:class:model:record`.

**(g) Quarantine bridge** for the prior monoid carrier (R2 T8):
```
M:quarantine:prior:kind:algebra:monoid a owl:NamedIndividual, M:type:quarantine ;
    M:relation:check:status "preserved declaration; original axioms not admitted into corrected kernel" ;
    M:relation:historical:identity <urn:silmaril:kind:algebra:monoid> .
```

### 2.7 SHACL gate pair per record class (R2 §4, T6)

Two idioms, both `sh:targetClass` (never `sh:targetNode` — gate classes, not singletons; 0
`sh:pattern`/`sh:in`, value typing by `sh:class`):
```
M:shape:theory a sh:NodeShape ; sh:targetClass M:type:theory:record ;
    sh:message "An algebraic theory must carry exactly one signature and at least one equation." ;
    sh:property [ sh:path M:relation:signature ; sh:minCount 1 ; sh:maxCount 1 ; sh:class M:type:signature:record ] ,
                [ sh:path M:relation:equation  ; sh:minCount 1 ;                 sh:class M:type:equation:record ] .
M:shape:theory:unique a sh:NodeShape ; sh:targetSubjectsOf M:relation:identifier ;
    sh:sparql [ a sh:SPARQLConstraint ;
        sh:message "theoryIdentifier must identify at most one theory in the validation graph." ;
        sh:select "SELECT $this WHERE { $this M:relation:identifier ?k . ?o M:relation:identifier ?k . FILTER(?o != $this) }" ] .
```
Coordinate-separation (min1/max1 per field) + non-vacuity/identity-collision SPARQL are the two teeth
every record class carries (R2 §4a). closure.ttl carries 52 NodeShapes, 33 targetClass, 31 SPARQL, 83
messages (R2 §4).

---

## 3. THE ENGINE / SEED BRIDGE MAP (fnd: rung → engine IRI → consolidated counterpart)

Bridge kinds (D24, design_constraints.md:453): `skos:exactMatch` (same denotatum),
`skos:closeMatch`, `seed:conservativeBridge` (engine is a faithful sub-theory),
`seed:implementationBridge` (engine is one realization). fnd: names confirmed in
`basicttl/foundation/algebra_spine.ttl` (see rung list). Engine URNs from `primordials.yaml`.
**The bridge does not yet exist — `basicttl/foundation/` has ZERO engine URN references (R3 F2); the
fold must AUTHOR every edge.**

| fnd: rung | Engine anchor (primordials.yaml) | Consolidated counterpart | Bridge kind | Note |
|---|---|---|---|---|
| `fnd:AlgebraicStructure` | `TYPE/ALGEBRA` root :394-404 | `@P:type:algebra:structure` (parent stub) | conservativeBridge | R3 §6 |
| `fnd:Magma` | GROUP **CLOSURE** axiom atom :467-472 (no magma type) | `structure:magma` stub | conservativeBridge (closure law only) | engine has no magma type; `group::product` cell-closure algebra.sh:295 |
| `fnd:Semigroup` | GROUP **ASSOCIATIVITY** axiom :473-477 | `structure:semigroup` stub | conservativeBridge | |
| `fnd:Monoid` | GROUP **IDENTITY** axiom :478-482 | `structure:monoid` stub | conservativeBridge (two-sided = 2 Equation records) | |
| `fnd:CommutativeMonoid` | **NONE** (no commutativity axiom) | `structure:monoid` (no comm variant) | **BUILD (no anchor)** | honest-red: engine never models commutativity (R3 §6) |
| `fnd:Group` | `TYPE/ALGEBRA/GROUP` +4 axioms + `group::validate` :456-487 / algebra.sh:321 | `structure:group` stub | **exactMatch** | the one direct type-level anchor; engine crams all 4 axioms |
| `fnd:AbelianGroup` | **NONE** (no commutativity axiom) | `structure:group` | **BUILD (no anchor)** | Blotto A_{m-1} witness (D22) is intended model |
| `fnd:Quasigroup` / `fnd:Loop` | **NONE** | — | **BUILD (no anchor)** | Latin-division law authored new |
| `fnd:Set` | `TYPE/ALGEBRA/SET` + EXTENSIONALITY + FINITE :405-438 | `structure` (n/a) | conservativeBridge / closeMatch | engine set finite/extensional; fnd: set structural/ETCS |
| `fnd:` category | `TYPE/ALGEBRA/CATEGORY` + id/assoc :488-509 | 6 foundation axioms + Yoneda (R2 §1d/e) | conservativeBridge | engine = finite small category |
| `fnd:` Frame / ArrowType | `TYPE/FRAME` frame.sh 10-slot :574-606 + `prim:Frame` | `@P:type:frame` (3) | implementationBridge | 3-way bridge half-built on primordial side (frame.ttl:7) — HOLD DISTINCT from runtime `family:Frame` |
| `fnd:` Octet / ByteVector | `TYPE/CARRIER/OCTET` :328-346 / `BYTE/VECTOR` :298-312 | `@P:type:bytes` (7) | implementationBridge | Byte≠Octet WIDTH AXIOM :341-346 = the `owl:differentFrom` witness |
| `fnd:` Bit | `TYPE/CARRIER/BIT` `^[01]$` :171-183 | — | implementationBridge | |
| Ring/Field/Module/Vector | **NONE** (no engine ring line) | `structure:{ring,field,module,vector:space}` stubs | **BUILD + HOMONYM guard** | `owl:differentFrom` vs carrier `VECTOR` / `Z256` (R4 §6.4) — fan-out |
| GroupAction/GSet, Blotto (D22) | **NONE** | — | **BUILD** | fan-out sub-lane, not spine |

**Net (R3 §6):** only **Group** (type, exactMatch) and **AlgebraicStructure** (root) have a
type-level engine anchor; **Magma/Semigroup/Monoid** bridge to the engine's SEPARATE group *axiom*
atoms (which DO exist individually in the AOB tree, not the crammed type); **CommutativeMonoid /
AbelianGroup / Quasigroup / Loop** are pure BUILD (honest-red, cited-math per D20 SYN). Carriers
(Bit/Byte/Octet/ByteVector/Frame) have full direct engine anchors = implementationBridges.

**Carrier grounding is native (R3 §3, §5.3):** every engine AOB atom already names its
`GROUNDING:CARRIER:{LAMBDA,BYTE,OCTET}` URNs + cites `EVIDENCE:SOURCE:…:LINE` (e.g. group type →
primordials.yaml:441; closure axiom → :452). The fold's `groundsIn*` / `schema:seeAlso primitive:*`
edges (frame.ttl:8 `schema:seeAlso primitive:Frame`) express the SAME edge the engine states in YAML.

---

## 4. THE GATE PIPELINE (reference gates.md → V0-V8) + DISCIPLINE

**V0-V8 lettering is ABSENT from the reference drop** (grep V0..V8 = 0 hits — R4 §0); it lives in the
uncommitted seed-carrier spec. The reference realizes gates THREE concrete ways the fold must recognize
under the reference vocabulary, not by grepping "V":

1. **Ontology-modeled gates** — `gate:specification` OWL classes:
   `internal` (ttl:34022), `non:vacuous` (34373), `complete` (63375), `homotopy:engagement` (63585),
   `external` (69415), root (70846). Each keeps the four-plane split verbatim: *"The external gate is a
   prescriptive information entity. Its evaluation is a BFO process. Its clause results are evidence
   records. These categories are not collapsed."* (ttl:69411). Gate identity is a biting SHACL tooth:
   *"gateIdentifier must identify at most one GateSpecification"* (ttl:75335). Richer clause machinery:
   `gate:clause:{coverage,control,query,refutation,shape}` + `external:gate:evaluation:process` — LIFT
   this decomposition (R4 §1.A, §6.1).
2. **34-criterion acceptance table** — `docs/gates.md` + `docs/baseline.md` (corpus-completeness axis).
3. **Executable Jena 5.6.0 harness** — `reports/independent/validation.log`: 1 positive
   (conforms=true, results=0) + 28 negatives (conforms=false) + `empty conforms=true ⇒ admission=REJECT`
   (validation.log:34 — non-vacuity realized).

### Crosswalk (R4 §1.D) — the fold's gate identifiers adopt D24 V-lettering AND bridge these classes:

| D24 gate | reference realization |
|---|---|
| **V0 syntax** | Turtle parse; changes.md syntax-restore |
| **V1 OWL-profile + hygiene (no punning, class≠prov-participant)** | structure.md "punning overlaps: 0"; profile `"OWL 2 DL with SHACL validation"` |
| **V2 SHACL non-vacuous** | `non:vacuous:gate:specification` (34373); `empty ⇒ REJECT` (validation.log:34) |
| **V3 categorical probes** | 65 `sh:sparql`/`sh:select` + `gate:clause:{query,refutation,control}:canonical` |
| **V4 Yoneda-density fixtures** | `homotopy:engagement:gate:specification` (63585); Yoneda theorem+cert; mathematics.md §4-5 |
| **V5 algebraic-law probes (theory+carrier+ops+laws; law-witness mode)** | `seed:algebra:foundation:{carrier,category,model,olog}:seed` + 6 axioms; `algebra:theory:rewrite` MODE (ttl:1484) |
| **V6 manifest coverage (N_manifest = N_materialized)** | `complete:gate:specification` (63375); `docs/sourcecounts.md` (manifest-derived, SHA-pinned); 52-shape coverage table |
| **V7 provenance closure (executor≥1 AND shadow≥1)** | PROV-O one-sided only: `wasAttributedTo`×1352, `wasGeneratedBy`×990, `wasDerivedFrom`×428 — **dual review lane NOT realized (governance/ empty) → GAP** |
| **V8 SHACL-2017 discipline** | `"OWL 2 DL with SHACL validation"`; Jena 5.6.0 report |

**Verdict:** every V0-V8 has a concrete counterpart EXCEPT V7's *dual executor+shadow* closure.

### Fixtures / manifests / provenance discipline (R4 §2, §6):
- **Fixtures** = 1 positive + a failing negative per shape, run by a NAMED external validator (Jena
  5.6.0) with PINNED input SHA-256s (`reports/independent/`). `sh:conforms true` alone is vacuous;
  empty-graph conformance = REJECT. Witnesses live in `fixtures/`, OUT of ontology modules (D24 four
  planes).
- **Manifests** (deep-KV YAML) adopt the engine's Flavor-B AOB envelope: `EVIDENCE:SOURCE:…:LINE`,
  `GROUNDING:CARRIER`, `PROVENANCE:STATE`, `GAPS`, `RECEIPT` (R3 §3). Counts DERIVED from manifests,
  never hard-coded (`parity.md:3` "not only a hard-coded count"); 0-focus shapes = REJECT.
- **Proof-status + validation-MODE are realized vocabularies** — REUSE the tokens, don't mint new:
  status `asserted (341) / literature:backed / specified / conditional (34) / counterexample (3) /
  rejected (2)` (`seed:gate:proof:status:*`, ttl:64678); modes `finite:table / rewrite
  (algebra:theory:rewrite ttl:1484) / external:certificate / bounded` (R4 §3.C).
- **PROV-O on every RECORD** (never on denotata): `prov:wasAttributedTo` + `prov:wasGeneratedBy`
  (D24, design_constraints.md:464). ADD the missing shadow half.
- **`seed:*` legacy-bridge namespace** (`ns3457:legacy → urn:silmaril:seed:*`, ttl:64680) IS the D24
  TODO-11 / D25 alias-map mechanism — carry it into `basicttl/primordial/type/**` so inbound
  `groundsIn*` / `subClassOf fnd:*` refs stay resolvable (R4 §3.D).

---

## 5. EXACT FOLD PLACEMENT UNDER `basicttl/primordial/type/**`

On-disk fold target (confirmed by `find`): the algebra subtree already exists with the
product/sum idiom —
```
basicttl/primordial/type/algebra/product/frame.ttl
basicttl/primordial/type/algebra/sum/admission{,/accepted,/rejected}.ttl
basicttl/primordial/type/algebra/sum/byte/vector{,/empty,/link}.ttl
basicttl/primordial/type/{classes,schema,shapes,imports,unresolved}.ttl
basicttl/primordial/type/{catalog,coverage,readiness,unresolved}.sparql
basicttl/primordial/type/{byte,stream,declarations,properties}/
```
IRI root = `urn:silmaril:primordial:type:` (`model:`), `…:class:` (`family:`), `urn:silmaril:prim:#`
(`primitive:`) (frame.ttl:1-3). Existing pattern: one `…Declaration` class per file, `model:Product`
/ `model:ClosedSum` split, `schema:seeAlso primitive:*` carrier bridge — but with the CamelCase +
class-punning flaw the fold must FIX in the algebra subtree it touches (frame.ttl:7; D25:487-488).

**Proposed target paths for the Pass-1 spine** (grammar-A discipline, grammar-C root; the theory tower
is a `model:Product`-family of theories, so it sits beside `product/`):

```
basicttl/primordial/type/algebra/theory/
    structure.ttl              # theory:algebraic:structure root + signature/equation/operation classes (schema plane)
    magma.ttl                  # theory:magma + closure axiom + signature (one binary op)
    semigroup.ttl              # theory:semigroup = magma + associativity equation
    monoid.ttl                 # theory:monoid = semigroup + unit op + 2 identity equations  ← §2.6 template
    monoid/commutative.ttl     # theory:monoid:commutative = monoid + commutativity equation
    group.ttl                  # theory:group = monoid + inverse op + inverse equation (engine exactMatch)
    group/abelian.ttl          # theory:group:abelian = group + commutativity
    quasigroup.ttl             # theory:quasigroup + Latin-division law (BUILD)
    loop.ttl                   # theory:loop = quasigroup + identity (BUILD)
basicttl/primordial/type/algebra/model/*.ttl          # model classes + carriers + validation-mode
basicttl/primordial/type/algebra/axiom/*.ttl          # foundation axiom records (relation:foundation)
basicttl/primordial/type/algebra/bridge/{engine,seed,fnd}.ttl   # §3 bridge edges + alias map
basicttl/primordial/type/algebra/shapes/*.ttl         # SHACL gate pairs per record class (§2.7)
basicttl/primordial/type/algebra/probes/*.rq          # categorical + algebraic-law probes (V3/V5)
basicttl/primordial/type/algebra/fixtures/<rung>/{positive,negative}.ttl   # 1 positive + failing negative
basicttl/primordial/type/algebra/manifests/*.yaml     # deep-KV, Flavor-B envelope, DERIVED counts
```
(Exact directory names are a planner decision; the load-bearing constraints are: theory/model/axiom/
equation/element live in the ONTOLOGY plane, witnesses live under `fixtures/`, shapes under `shapes/`,
bridges collected so the alias map is auditable — R2 §7.5, D24 Modular Option A+ :461-466.)

**CI LOCKSTEP (D25:504-508 — mandatory, not optional):** master's `ci.yml` `ontology-floors` job
auto-discovers `basicttl/foundation/*.ttl` + a depth gate. Folding INTO `basicttl/primordial/type/**`
and moving witnesses to `fixtures/` (outside that glob) goes VACUOUS unless the runner + CI discovery +
gates V0-V8 move IN LOCKSTEP. The reshape MUST extend the committed runner and `ci.yml`, and sign
reshape commits under `commit_signing_trust.ttl`. (R4 §4 [SCOPE] flag: do NOT import plan.md's
"no Git commit / Bash-builtins-only" — that binds the delivered runtime successor only.)

---

## 6. DOCTRINE REFINEMENTS — items that MAY OVERRIDE Directives 24/25 (flag for directive update)

None of the reference material contradicts the DIRECTION of D24/D25; it is a faithful more-concrete
instance. Two items rise to the level of a directive-update flag; the rest are refinements to honor.

### [OVERRIDE-CANDIDATE 1] Multi-word proper-name ordering (naming law §10b)
D24 §10b's two worked examples (`transformation:natural`, `category:elements`) are CONTRADICTED by the
verified runtime + consolidated reference, which use `natural:transformation` and
`category:of:elements` (R1 §4). This is a genuine conflict inside the governing law itself: either D24's
examples are wrong and should be amended to the reference convention (adjective-first, stop-words kept
for established mathematical proper names), or the reference is renormalized. **A directive amendment is
needed either way** — the law as written cannot be followed against the reference without a ruling.
(Restated as Q2 in §7.)

### [OVERRIDE-CANDIDATE 2] The fold-target IRI root is NOT the verified-runtime grammar
D25 says adopt the primordial tree's IRI root (`urn:silmaril:primordial:type:`, grammar C). But the
VERIFIED RUNTIME (bash `aob/urn/**`, 293/293) and the consolidated reference use the full-taxonomy
`urn:silmaril:type:graph:instance:instruction:code:property:…` descent (grammar A). These are different
grammars for the "same" typed thing. D25's fold instruction and the runtime's canonical grammar are in
tension. The fold as specified (§1.1) reconciles by minting under grammar C and BRIDGING to grammar A —
but if the maintainer intends the fold to carry the full runtime lineage natively, D25's "adopt the
primordial IRI root" needs a clarifying amendment. (Restated as Q1 in §7.)

### Refinements to HONOR (no override; do not re-derive):
- **Yoneda is a theorem, "No seventh axiom has been inserted"** (math.md:58) — theorem+certificate,
  never axiom; theorem/axiom collapse = SHACL violation (already D24, reinforced R4 §3.B).
- **Grounding stays relation-plural** — ontology-grounding, inheritance, taxonomy, realization,
  denotation, location are DIFFERENT relations; "a successful C3 order is not an ontology-grounding
  proof" (grounding.md:3, R4 §3.A). External projection byte/version-pinned (BFO 2020, CCO 2024-11-06,
  CPO 2025-04-25).
- **Homonym separation via `owl:differentFrom`** — "an octet in the machine carrier, an unsigned-byte
  datatype value and an element of the modular ring are separately typed accounts" (math.md:110); only
  2 witnesses exist in ref — the fold ADDS the Ring/Field/Module/Vector + byte/octet/Z256 ones D25:500
  names (R4 §6.4).
- **M-corrections** (math.md §7): left-fold vs right-fold step type; discrete-cycle ≠ circle cohomology;
  antipodal only for even n; mod-n quotient ≠ universal cover; read/write not inverses; Bash-mutation ≠
  pure-lambda (R4 §3.B).
- **Two-sided identity/inverse = TWO Equation records** + obligation-counting extension morphism
  (already D25:497; reference confirms `left`/`right` reification, R2 §2).
- **[GAP the fold must SUPPLY, not override]** the executor/shadow dual-review lane
  (`reviews/{executor,shadow,resolved}/` + `receipts/`, D24 V7 lifecycle) is ABSENT from the reference
  (governance/ empty, R4 §5) — BUILD it; only a one-sided PROV + independent-validator leg exist.

---

## 7. OPEN QUESTIONS FOR THE MAINTAINER (verbatim)

**Q1 — IRI root grammar.** The verified runtime (`aob/urn/**`, 293/293) and the consolidated reference
use the full-taxonomy descent `urn:silmaril:type:graph:instance:instruction:code:property:domain:…:
component:…:instance:…`, but the D25 fold target on disk (`basicttl/primordial/type/**`) uses the short
root `urn:silmaril:primordial:type:`. Does the fold mint its typed IRIs under the short primordial root
(and reach the runtime lineage only via `schema:seeAlso`/`seed:*Bridge` edges, as §1.1 assumes), or must
the fold carry the full 12-marker runtime ladder natively inside `basicttl/primordial/type/**`?

**Q2 — Multi-word proper-name ordering.** D24 §10b prescribes genus-first even for compound proper
names (`NaturalTransformation → transformation:natural`, `CategoryOfElements → category:elements`), but
the verified runtime and consolidated reference both use `natural:transformation` (9 vs 0) and
`category:of:elements` (12 vs 0, stop-word kept). Which wins — do we amend D24's examples to the
reference convention (adjective-first + stop-words for established mathematical names), or renormalize
the reference on the way in?

**Q3 — Group-rung bridge kind.** The engine gives `fnd:Group` its ONLY direct type-level anchor
(`TYPE/ALGEBRA/GROUP` + `group::validate`, exactMatch) but CRAMS all four axioms into that one leaf,
while the fold re-introduces magma/semigroup/monoid as separate weaker theories bridging DOWN to the
engine's individual axiom atoms. Is `skos:exactMatch` still correct for Group given the engine leaf is
strictly coarser (no intermediate weakenings), or should Group also be a `seed:conservativeBridge` with
exactMatch reserved for a theory-by-theory correspondence the engine does not provide?

---

## COVERAGE ATTESTATION (Praeriehund)

- SYNTHESIZED from all four refmap shards read IN FULL (R1 13 files/7 findings; R2 10/8; R3 24/17;
  R4 22/8), plus governing law `design_constraints.md` D21-25 (lines 420-509 read) + RECOVERY.md +
  primary confirmation greps against `silmaril.final.consolidated.ttl`, `basicttl/primordial/type/**`
  (frame.ttl, schema.ttl heads), `basicttl/foundation/algebra_spine.ttl` (fnd: rung enumeration).
- COMPLETE for the 7 requested deliverables: (1) definitive naming law + rank tables + D24/25
  reconciliation; (2) record/shape templates incl. the MONOID rung end-to-end (§2.6); (3) engine
  bridge map fnd:→engine→consolidated (§3); (4) gate pipeline V0-V8 crosswalk + fixture/manifest/
  provenance discipline (§4); (5) exact fold placement (§5); (6) override-candidate refinements (§6);
  (7) three maintainer open questions verbatim (§7).
- GAPS carried forward from the shards (not re-closable here): USER_REF_00.md + seed-carrier spec
  §10b PRIMARY TEXT absent (uncommitted zip); the executor/shadow review lane + V0-V8 lettering absent
  from the reference drop (belong to the other corpus); the two grammar conflicts (Q1, Q2) are
  genuine and require a maintainer ruling — this synthesis picks the D25-consistent reading (mint
  under primordial root, bridge to runtime) but flags both rather than deciding unilaterally.
