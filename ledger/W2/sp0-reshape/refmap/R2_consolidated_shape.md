# REFMAP shard R2 — the CONSOLIDATED record model (silmaril.final.consolidated.ttl + zip ontology/)

MAP agent evidence. Praeriehund honesty: file:line, counts, verbatim quotes. No opinions; the
"spine fold must instantiate" templates at the end are transcriptions of the reference's own forms.

## 0. Sources read + coverage attestation

| file | size | format | role |
|---|---|---|---|
| `silmaril.final.consolidated.ttl` (repo root) | 43,383 lines | **N-Triples** (fully-expanded URIs, no `@prefix`) | the consolidated instance graph |
| `silmaril.consolidated.repaired.ttl` (repo root) | 82,953 lines | N-Triples | final + a `…:repair:september:five:two:thousand:twenty:six:*` patch overlay (36 hits; adds betti:degree / class:binding / source:ontology / evidence / allocation repair records) |
| `refcomp/zip/silmaril/ontology/consolidated.ttl` | 4.31 MB / 43k+ triples | **Turtle** (auto-numbered `ns1…ns1067+` prefixes, each a full URN) | Turtle serialization of the same instance graph |
| `refcomp/zip/silmaril/ontology/consolidated.shacl.ttl` | 1,434 lines | Turtle | the SHACL gate file |
| `refcomp/zip/silmaril/ontology/closure.ttl` | ~70 KB | Turtle | the **Seed-Carrier grounding closure** (∫M; 6 axioms + 3 theorems + intensional owl:Restriction record classes) |
| `refcomp/zip/silmaril/ontology/primordial.yaml` | 318 KB | YAML | primordial **type registry source** (IDENTITY/ANCHORS/DEFINITIONS/AXIOMS/TYPES) |
| `refcomp/zip/silmaril/ontology/physical.yaml` | 23 KB | YAML | the **physical facet** carrier schema (bit/byte vectors) |
| `refcomp/zip/silmaril/ontology/runtime.yaml` | 23 KB | YAML | the **runtime** field/execution-graph schema |

`final.consolidated`: 9,700 `rdf:type` triples; **2,994 owl:NamedIndividual**, **1,928 owl:Class**.
Coverage: all record-class families enumerated by census (below); every record-class idiom quoted from
a materialized instance; SHACL every `sh:message` enumerated; closure.ttl axiom/theorem/construction/
restriction blocks read verbatim; three YAMLs' top structure read. NOT exhaustively read: the 4.3 MB
Turtle body line-by-line (used only for prefix/idiom confirmation — it is the same graph as the
N-Triples final), and the repaired overlay's 40k extra lines beyond confirming the repair namespace.

**Naming abbreviation used below** (to keep quotes legible), applied to the verbatim N-Triples:
- `@P` = `urn:silmaril:type:graph:instance:instruction:code:property`
- `@I` = `@P:domain:computational:economics:research:infrastructure:kingdom:knowledge:phylum:formal:class:typed:order:declarative:family:execution:genus:graph:species:runtime:specimen:instance` (the **instance-plane** descent — the Linnaean kingdom→…→specimen:instance spine every consolidated record lives under)
- `@S` = `urn:silmaril:type:graph:instance:instruction:code:property:grounding:ontology:basic:formal:domain:knowledge:representation:kingdom:specification:phylum:formal:contract:class` … `:order:declared:family:seed:genus:registry:species` (the **seed-registry** descent used by closure.ttl and the YAMLs)
The full unabbreviated URNs are in the cited files at the cited lines.

---

## 1. STRATIFICATION — how records are distinguished

### 1a. The record layer lives in ONE property namespace, `@P:type:*`, typed on individuals

Every record is an `owl:NamedIndividual` that ALSO carries a second `rdf:type` naming its **record
class** in the `@P:type:*` namespace. Census of `@P:type:*` rdf:type targets by instance count
(`grep "#type>" … | count`, final.consolidated):

```
1223  @P:type:quarantine       445  @P:type:gate           445  @P:type:external
 445  @P:type:declaration      292  @P:type:cardinality     72  @P:type:position
  72  @P:type:pair              72  @P:type:key             72  @P:type:binding
  59  @P:type:notation          52  @P:type:path            34  @P:type:definition
  32  @P:type:descriptor        27  @P:type:record          23  @P:type:error
  13  @P:type:interpretation    11  @P:type:finite:composition
  10  @P:type:digest             8  @P:type:taxon            8  @P:type:rank
   8  @P:type:finite:arrow       7  @P:type:provenance       7  @P:type:carrier
   7  @P:type:bytes              6  @P:type:source           6  @P:type:axiom
   5  @P:type:integer            5  @P:type:finite:object    5  @P:type:finite:application
   5  @P:type:construction       3  @P:type:vector           3  @P:type:theorem
   3  @P:type:node               3  @P:type:frame            3  @P:type:finite:generator
   3  @P:type:finite:element     3  @P:type:certificate      2  @P:type:operation
   2  @P:type:category           1  @P:type:version
```

The Directive-24 planes map onto this census as a **1:1:1 DeclarationRecord / Denotatum / Gate triad**
(445 : 445 : 445) plus a large **quarantine** plane (1223) and reified coordinate planes
(cardinality/position/pair/key/binding/…).

### 1b. The three-plane DeclarationRecord idiom (the core envelope) — VERBATIM

A declared thing is THREE distinct IRIs: the record, its denotatum, its gate. From
`final.consolidated.ttl` (the `…:construct:extensible:markup:language:schema:alternative:type` record;
`@X` = that node's `@I:construct:…:schema:alternative:type` stem):

**Plane 1 — DeclarationRecord** (`a @P:type:declaration`):
```
<@X> a owl:NamedIndividual .
<@X> a <@P:type:declaration> .
<@X> <@P:relation:assignment>          <@X:gate> .
<@X> <@P:relation:denotatum>           <@X:denotatum> .
<@X> <@P:relation:historical:identity> <urn:silmaril:seed:external:anchor:xsd:alternative:type> .
<@X> <@P:relation:identifier>          "…:schema:alternative:type" .
<@X> <@P:relation:notation>            "Type Alternative (conditional type assignment; {type table})" .
<@X> <@P:relation:primary:taxon>       <@I:taxon:species> .
<@X> <@P:relation:source:url>          "https://www.w3.org/TR/xmlschema11-1/" .
```

**Plane 2 — Denotatum** (`a @P:type:external` — the *denoted thing's* plane; other denotata get other
classes) pointed to by `relation:denotatum`:
```
<@X:denotatum> a owl:NamedIndividual .
<@X:denotatum> a <@P:type:external> .
<@X:denotatum> <@P:relation:identifier> "…:alternative:type:denotatum" .
<@X:denotatum> <@P:relation:notation>   "Description of external construct Type Alternative …" .
<@X:denotatum> <@P:relation:source:url> "https://www.w3.org/TR/xmlschema11-1/" .
```

**Plane 3 — GateAssignment** (`a @P:type:gate`) pointed to by `relation:assignment`:
```
<@X:gate> a owl:NamedIndividual .
<@X:gate> a <@P:type:gate> .
<@X:gate> <@P:relation:check:status>   "declaration reconciled; not a generic semantic proof" .
<@X:gate> <@P:relation:identifier>     "…:alternative:type:gate" .
<@X:gate> <@P:relation:interpreted:by> <@I:interpretation:general:record> .
```

So: **the record separates DENOTATUM (what it means) from the GATE (how its admission was checked)
from PROVENANCE (`historical:identity` bridge + `source:url`).** This is the exemplar's
DeclarationRecord envelope realized. `check:status` on the 445 gates is uniformly
`"declaration reconciled; not a generic semantic proof"` — an honest verdict, not a claimed proof.

### 1c. The QUARANTINE plane (1223 records) — honest non-admission

Every prior-corpus term preserved-but-not-admitted is `a @P:type:quarantine` with a bridge and a
verdict. Verbatim (the `@I:historical:class:eight:eight:eight` record):
```
<@I:historical:class:eight:eight:eight> a owl:NamedIndividual .
<@I:historical:class:eight:eight:eight> a <@P:type:quarantine> .
<@I:historical:class:eight:eight:eight> <@P:relation:check:status>
      "preserved declaration; original axioms not admitted into corrected kernel" .
<@I:historical:class:eight:eight:eight> <@P:relation:historical:identity>
      <urn:silmaril:ontology:primordial:homotopy:category:infinity:one> .
<@I:historical:class:eight:eight:eight> <@P:relation:notation>
      "Primordial::Homotopy::CategoryInfinityOne — (infinity,1)-category" .
```
All 1223 carry the identical `check:status` string `"preserved declaration; original axioms not
admitted into corrected kernel"`. This is the Curry §6 / Praeriehund quarantine plane made literal:
the prior `Primordial::…` names survive as bridged declarations, kept OUT of the corrected kernel.

### 1d. The `type:axiom` pattern — exactly SIX foundation axioms

`grep '<@P:type:axiom> .' | #type` → exactly 6 individuals (the task's hypothesis confirmed):
```
@I:axiom:category:associativity
@I:axiom:category:identity
@I:axiom:functor:composition
@I:axiom:functor:identity
@I:axiom:naturality
@I:axiom:sketch:equation:satisfaction
```
An axiom record is minimal, and is declared FOUNDATIONAL by the ontology node itself:
```
<@I:axiom:category:identity> a owl:NamedIndividual .
<@I:axiom:category:identity> a <@P:type:axiom> .
<@I:axiom:category:identity> <@P:relation:identifier>      "@I:axiom:category:identity" .
<@I:axiom:category:identity> <@P:relation:notation>        "category identity" .
<@I:axiom:category:identity> <@P:relation:source:location> "docs/research/proofs.md" .
<@P:ontology:consolidated> <@P:relation:foundation> <@I:axiom:category:identity> .
```
`relation:foundation` fires exactly 6 times, once per axiom (grep count = 6 axiom objects). The six
are the category laws (identity, associativity), functor laws (identity, composition), naturality, and
sketch equation-satisfaction — i.e. **the foundation is the theory of small categories + functors +
natural transformations + sketches, NOT a magma/group axiom set.**

### 1e. Yoneda IS a theorem record (never an axiom), each with a matching certificate

`grep '<@P:type:theorem> .'` → 3: `@I:theorem:yoneda`, `@I:theorem:yoneda:full:faithfulness`,
`@I:theorem:covariant:co:yoneda`. `grep '<@P:type:certificate> .'` → 3 parallel:
`@I:certificate:yoneda`, `…:yoneda:full:faithfulness`, `…:covariant:co:yoneda`. Verbatim:
```
<@I:theorem:yoneda> a owl:NamedIndividual .
<@I:theorem:yoneda> a <@P:type:theorem> .
<@I:theorem:yoneda> <@P:relation:certificate> <@I:certificate:yoneda> .
<@I:theorem:yoneda> <@P:relation:identifier>  "@I:theorem:yoneda" .
<@I:theorem:yoneda> <@P:relation:notation>    "yoneda" .

<@I:certificate:yoneda> a owl:NamedIndividual .
<@I:certificate:yoneda> a <@P:type:certificate> .
<@I:certificate:yoneda> <@P:relation:digest:value>
      "e9ad6ac29e6d367fe48b27b0b9e77ee6ffd77e2e0cba829be919037cbabaa653" .
<@I:certificate:yoneda> <@P:relation:identifier>     "@I:certificate:yoneda" .
<@I:certificate:yoneda> <@P:relation:proof:method>
      "Explicit general mathematical derivation; not proof-assistant checked" .
<@I:certificate:yoneda> <@P:relation:source:location> "docs/research/proofs.md" .
```
**The axiom≠theorem distinction is structural:** axioms are objects of `relation:foundation` and carry
NO certificate; theorems carry `relation:certificate → certificate` and NO `relation:foundation`; the
certificate carries a `digest:value` (sha256) + a `proof:method` string. `proof:method` values across
the graph: `"Explicit general mathematical derivation; not proof-assistant checked"` (×3) — the
honest 8-value-status idiom collapsed to a prose proof-method here.

### 1f. proof/definition status vocabularies (the reference's realized values)
- `relation:definition:status`: `"primitive"` (157), `"defined"` (32).
- `relation:check:status`: `"preserved declaration; original axioms not admitted into corrected kernel"`
  (1223, quarantine), `"declaration reconciled; not a generic semantic proof"` (445, gate).
- `relation:proof:method`: `"Explicit general mathematical derivation; not proof-assistant checked"` (3).

### 1g. The FINITE-MODEL plane (validation-mode = finite table) — the executable category
The actual categorical computation lives in `@P:type:finite:*` records (NOT in the algebra classes):
5 `finite:object`, 8 `finite:arrow`, 3 `finite:element`, 3 `finite:generator`, 11 `finite:composition`,
5 `finite:application`. A composition-table cell is reified (verbatim, `finite:base:composition:four`):
```
<@I:finite:base:composition:four> a <@P:type:finite:composition> .
<@I:finite:base:composition:four> <@P:relation:category:first>  <@I:finite:ib> .
<@I:finite:base:composition:four> <@P:relation:category:second> <@I:finite:ib> .
<@I:finite:base:composition:four> <@P:relation:category:result> <@I:finite:ib> .
<@I:finite:base> <@P:relation:category:composition> <@I:finite:base:composition:four> .
```
i.e. `g∘f = result` as a reified table cell (`category:first`=f, `category:second`=g, `category:result`
=g∘f), linked from the base category by `relation:category:composition`. This is the **finite table the
6 axioms are checked against** ("Checked exhaustively; not inferred from a label", closure.ttl:14).

---

## 2. Reified relation predicates + provenance

All predicates live in `@P:relation:*`. Census by triple count (final.consolidated), the record model's
field vocabulary:

```
3516 relation:identifier      3027 relation:notation        1672 relation:check:status
1670 relation:historical:identity  894 relation:source:url   828 relation:version
 828 relation:state           828 relation:modified          828 relation:created
 826 relation:ground          826 relation:authority         593 relation:primary:taxon
 450 relation:interpreted:by  450 relation:denotatum         450 relation:assignment
 231 relation:source:location 191 relation:definition:status 105 relation:semantic:condition
  82 relation:left             81 relation:right              81 relation:pair
  79 relation:subject          79 relation:provenance         79 relation:position
  79 relation:carrier          77 relation:position:path      77 relation:position:ordinal
  77 relation:position:offset  77 relation:position:line      77 relation:position:depth
  77 relation:domain           77 relation:codomain           56 relation:segment
  56 relation:kind             56 relation:depth              49 relation:path:parent
  36 relation:denotes          35 relation:requires           33 relation:differentia
  15 relation:category:{first,second,result,composition}  14 relation:digest:value
  13 relation:category:{base,target,source,map,argument}   12 relation:classified:rank
```

**Identity / notation:** `relation:identifier` (the record's own full URN as a string literal, on
essentially every record), `relation:notation` (human-readable label string).

**Provenance quartet** (Directive-24 "provenance on every RECORD"): `relation:created` /
`relation:modified` / `relation:version` / `relation:state` (828 each — a uniform provenance stamp),
plus `relation:authority` (826), `relation:ground` (826), `relation:provenance` (79),
`relation:historical:identity` (1670 — the **bridge to prior carriers / seed anchors**, e.g.
`urn:silmaril:seed:external:anchor:xsd:*`, `urn:silmaril:ontology:primordial:*`),
`relation:source:url` (894, external cite) and `relation:source:location` (231, in-repo file cite,
e.g. `"docs/research/proofs.md"`).

**Source-position (evidence file:line) block:** `relation:source:location` +
`relation:position:{path,ordinal,offset,line,depth}` (77 each) — the exemplar's 14-field source anchor.

**Denotatum/gate/interpretation triad predicates:** `relation:denotatum` (450), `relation:assignment`
(450, → gate), `relation:interpreted:by` (450, → interpretation record), `relation:denotes` (36).

**Equation/algebra predicates:** `relation:left` (82) / `relation:right` (81) / `relation:pair` (81)
(an equation is a reified `left = right` pair), `relation:domain`/`relation:codomain` (77 each, arrow
signature), `relation:category:*` (finite composition cells), `relation:carrier` (79),
`relation:semantic:condition` (105).

**Taxonomy:** `relation:primary:taxon` (593, → an `@P:type:taxon`/`@P:type:rank` node),
`relation:classified:rank` (12), `relation:differentia` (33) — genus+differentia classification.

**Certificate/digest:** `relation:certificate` (theorem→cert), `relation:digest:value` (14, sha256),
`relation:proof:method`.

---

## 3. The algebra TOWER — HOW it appears: a FLAT SUBCLASS LADDER OF BARE STUBS

**Finding: the tower is present as an OWL subclass ladder of "primitive" class stubs — NOT
theory+model+reduct, and NOT populated.** `:reduct:` count across final.consolidated = **0**.

The 17 tower classes, all `rdfs:subClassOf @P:type:algebra:structure` (which is
`rdfs:subClassOf @P:type:mathematical:structure`), verbatim IRIs:
```
@P:type:algebra:structure                     (parent, subClassOf @P:type:mathematical:structure)
@P:type:algebra:structure:magma
@P:type:algebra:structure:semigroup
@P:type:algebra:structure:monoid
@P:type:algebra:structure:group
@P:type:algebra:structure:ring
@P:type:algebra:structure:field
@P:type:algebra:structure:module
@P:type:algebra:structure:vector:space
@P:type:algebra:structure:lattice
@P:type:algebra:structure:boolean:algebra
@P:type:algebra:structure:relation:algebra
@P:type:algebra:structure:action                 (← the group-action rung is present)
@P:type:algebra:structure:representation
@P:type:algebra:structure:signature              (Σ carrier)
@P:type:algebra:structure:term                   (T_Σ carrier)
@P:type:algebra:structure:equation               (E carrier)
```
Every rung is IDENTICALLY shaped (verbatim, group; all others differ only in the local name):
```
<@P:type:algebra:structure:group> a owl:Class .
<@P:type:algebra:structure:group> <rdfs:label> "algebra structure group"@en .
<@P:type:algebra:structure:group> <rdfs:subClassOf> <@P:type:algebra:structure> .
<@P:type:algebra:structure:group> <@P:relation:definition:status> "primitive" .
<@P:type:algebra:structure:group> <skos:definition>
      "A typed algebra structure … information record in the governed finite profile."  (per-rung)
```

**Crucial gaps (what makes these STUBS):**
- `grep -c 'rdf-syntax-ns#type> <@P:type:algebra:structure:group>'` = **0** — NO individual is ever a
  model of any tower class. The ladder is uninhabited.
- There is NO `theory` individual, NO `model` individual, NO `reduct`/theory-morphism edge attached to
  any rung. `magma→…→field` is a bare `subClassOf` chain, each rung `definition:status "primitive"`.
- The signature/equation/term classes EXIST as siblings but carry no `(Σ,Ω,E)` presentation
  individuals linking group→its-operations→its-laws. `@P:type:operation` has only 2 individuals
  (`@P:operation:increment`, `@P:operation:sum`) and neither is wired to a tower rung.
- The `structure:action` rung is present (the group-action home) but likewise uninhabited.

The bridge to the prior carriers is the ONLY thing attached to a rung name — via
`relation:historical:identity` into `urn:silmaril:ontology:primordial:algebra:structure:{magma,…}` and
`urn:silmaril:ontology:primordial:feature:algebra:structure:magma:{commutative,medial,quasigroup,loop,
idempotent}` (final.consolidated:31127–33389). Those primordial targets appear ONLY as objects of
`historical:identity` (bridge anchors), never as defined records here.

**Where the REAL algebra content lives instead:** the executable mathematics is carried entirely in the
**category-theory layer** — the 6 foundation axioms (§1d), the 3 Yoneda theorem+certificate records
(§1e), the finite-table model (§1g), and the Seed-Carrier constructions in `closure.ttl` (§5). The
consolidated does the Lawvere/(S,Ω,E) job through **category-of-a-single-object-style finite tables +
Yoneda**, not through a populated group/ring/field tower. **This is precisely the gap the SP0 spine
fold must fill: give magma→…→abelian genuine theory + model + reduct individuals, since the reference
leaves the tower as bare `subClassOf` stubs.** (Matches MAP synthesis §2: "GO BEYOND it… carry real
(S,Ω,E) individuals.")

---

## 4. The `consolidated.shacl.ttl` gate idiom

Counts (whole file, 1,434 lines): **52 `sh:NodeShape`; 0 standalone `sh:PropertyShape`; 33
`sh:targetClass`; 0 `sh:targetNode`; 31 `sh:sparql`; 34 `sh:select`; 29 `sh:property`; 107
`sh:minCount`; 91 `sh:maxCount`; 30 `sh:datatype`; 75 `sh:class`; 83 `sh:message`; 119 `sh:path`;
0 `sh:pattern`; 0 `sh:in`; 0 `sh:node`.** Also present: `sh:targetSubjectsOf` (uniqueness shapes) and
a non-`sh:` custom key predicate `ns7:class` (annotation-key class constraint).

### 4a. Two shape idioms

**(i) Property-shape NodeShape** — `sh:targetClass <record-class>` + N × `sh:property [ … ]`, each a
blank carrying `sh:path` + `sh:minCount`/`sh:maxCount` + (`sh:datatype xsd:string` | `sh:class
<value-class>`) + a `sh:message`. Verbatim (the Frame shape, ns172:shape, lines 277–283 + bodies
1254–1275):
```
ns172:shape a sh:NodeShape ;
    sh:message "A Frame must keep status, outcome, and control disposition as separate required coordinates." ;
    sh:property _:source71, _:source72, _:source74, _:source75 ;
    sh:targetClass ns104:record .        # ns104 = …:structure:class:frame:
_:source71 sh:datatype xsd:string ; sh:minCount 1 ; sh:maxCount 1 ; sh:path ns22:identifier .
_:source72 sh:class ns152:specification ; sh:minCount 1 ; sh:maxCount 1 ; sh:path ns46:status .
_:source74 sh:class ns128:specification ; sh:minCount 1 ; sh:maxCount 1 ; sh:path ns46:outcome .
_:source75 sh:class ns87:specification  ; sh:minCount 1 ; sh:maxCount 1 ; sh:path ns52:disposition .
```
The `min 1 / max 1` per field is the **coordinate-separation tooth**: a record must carry exactly one
of each typed field, held as distinct coordinates (never collapsed).

**(ii) SPARQL-constraint NodeShape** — `sh:targetClass` (or `sh:targetSubjectsOf`) + `sh:sparql
[ a sh:SPARQLConstraint ; sh:message … ; sh:select "SELECT $this WHERE { …violation pattern… }" ]`.
The SELECT returns the *violating* `$this`. Verbatim (FINAL-type tooth, ns171 + _:source70, 1245–1252):
```
_:source70 a sh:SPARQLConstraint ;
    sh:message "A FINAL type may not be named as a parent type." ;
    sh:select """… SELECT $this WHERE {
        $this <…:property:object:has:parent:type> ?parent .
        ?parent <…:property:object:has:type:kind> <…:individual:final:type:kind> . }""" .
```
Uniqueness/non-vacuity teeth use `sh:targetSubjectsOf <…:identifier>` + a SELECT counting >1 subject
per key (e.g. _:source76: "frameIdentifier must identify at most one FrameRecord in the validation
graph").

### 4b. What the 83 messages enforce (the tooth taxonomy — all quoted verbatim, grouped)
- **Coordinate separation / exactly-one:** "A Frame must keep status, outcome, and control disposition
  as separate required coordinates."; "Every specification entity must carry exactly one canonical
  identifier."; "A homotopy engagement interface carries exactly one {admitted dimension class /
  coefficient domain / declared premise / … / validation profile}." (≈14 such).
- **Identity non-collision / non-vacuity (SPARQL):** "canonicalIdentifier must identify at most one
  SpecificationEntity in the validation graph."; "frameIdentifier must identify at most one
  FrameRecord…"; "cellIdentifier must be unique among EngagementCellSpecification subjects." (≈16
  such); "An artifact identifier names at most one artifact… Equal content digests alone do not
  identify artifacts."
- **Declaration ≠ computed / witness obligation:** "A homotopy receipt without grounds is a
  declaration, not a computed receipt."; "A higher cell without a coherence witness is an open
  obligation, not an admitted cell."; "A two-cell must cite a coherence witness rather than treating
  coherence as prose."; "A derived finding must cite at least one grounding evidence record."
- **Dimension discipline (n-cells):** "A {zero/one/two}-cell must carry dimensionValue {0/1/2}."; "A
  higher cell must carry dimensionValue three or greater."; "A zero-cell has no {source/target} cell."
- **Absence-evidence (the D≤1 / censoring tooth):** "A zero count without a known-present control is
  unmeasured and cannot be accepted as absence evidence."
- **Quarantine / ABSTRACT / FINAL:** "A FINAL type may not be named as a parent type."; "An object
  instance may not name an ABSTRACT runtime type."
- **Acyclicity / sealing:** "A stage may not be its own predecessor."; "A sealed verdict may not carry
  a blocking pending record."
- **Gate structure (Q/S/R/C):** "A homotopy gate carries exactly four Q/S/R/C clauses."; "An external
  gate must carry exactly one Q, S, R, and C clause and exactly one external context and protocol."

Targets are ALWAYS record/specification CLASSES (`sh:targetClass … :record`/`… :specification`), never
`sh:targetNode` singletons — the reference gates classes, not instances. No `sh:pattern`/`sh:in`;
value typing is by `sh:class` (75) into other record classes, i.e. structural not lexical.

---

## 5. closure.ttl + primordial.yaml + physical.yaml + runtime.yaml — roles

### 5a. `closure.ttl` — the Seed-Carrier grounding closure (the INTENSIONAL + ∫M layer)
Its own ontology node states the role (line 62–63):
> `…:species:closure a owl:Ontology ; rdfs:comment "Bounded closure projection. BFO named-edge
> extract, record/class separation, six axiom families and three theorem records. No full external
> import closure is asserted."`

Type census: 45 owl:NamedIndividual, **13 owl:Restriction, 13 owl:ObjectProperty, 12 owl:Class,
4 sh:NodeShape, 1 owl:Ontology.** It carries what the flat consolidated lacks — **intensional OWL**:
- The **6 axiom records** in the seed-registry namespace `@S:…:axiom:…:species:{category:associativity,
  category:identity,functor:composition,functor:identity,naturality,sketch:equation}`, each
  `a owl:NamedIndividual, <@S:…:species:axiom:record>` with `rdfs:comment` = the LAW STATEMENT + a
  checked-not-labelled clause, plus `ns3:equation → <equation record>`. Verbatim (line 12–15):
  > `…:axiom:…:category:associativity a owl:NamedIndividual, <…:species:axiom:record> ;
  >   rdfs:comment "For each composable triple f,g,h, (h∘g)∘f=h∘(g∘f). Checked exhaustively; not
  >   inferred from a label." ; ns3:equation <…:equation:…:category:associativity> .`
  (identity: "…f∘id(a)=f=id(b)∘f. Checked for every arrow of an admitted finite table."; naturality:
  "…N(f)(η(a)(x))=η(b)(M(f)(x)). Naturality applies to a declared transformation, not every untyped
  family."; sketch:equation: "Each declared parallel path equation has equal source, target, and
  normal-form arrow in the admitted finite model. Arbitrary presentation completeness is not asserted.")
- The **3 theorem records** with the honest verdict + certificate target (lines 131/136/141):
  > `rdfs:comment "Theorem, not an additional foundational axiom. General derivation is in
  > docs/mathematics.md. The executable target checks bounded finite instances; it is not a
  > proof-assistant certificate for all small categories." ; ns1:target <…:certificate:…:yoneda> .`
- The **5 construction records** (`…:species:construction:record`), which ARE the Seed Carrier itself:
  - `category:of:elements` — > "SeedCarrier=∫Mseed. Objects are (a,x) with x∈M(a). Arrows are f:a→b
    with M(f)(x)=y. Lifted units and composition are constructed and checked."
  - `coend:presentation` — > "For covariant M, M(c)≅∫^d M(d)×Hom(d,c)… computed, not just named."
  - `presented:category` — > "Cseed=Path(Gseed)/≡Eseed. …uses every admitted arrow as a generator,
    all identity laws and all table-composition equations. Normalization … confluent by the checked
    associativity and unit laws."
  - `set:valued:functor` — > "Mseed:Cseed→Set is represented by finite object carriers and total arrow
    action tables. All four category and functor axiom families are checked."
  - `yoneda:embedding` — > "Standard Yoneda has variance C→[C^op,Set], a↦Hom(-,a). The executable
    full-faithfulness checker uses the opposite category…"
- **Intensional record CLASSES via owl:Restriction** (the idiom the flat consolidated lacks): a record
  class = `rdfs:subClassOf` a bundle of `[ a owl:Restriction ; owl:cardinality "1"^^xsd:nonNegative
  Integer ; owl:onProperty <field> ]` + a parent class. Verbatim (datatype:record, 153–169):
  ```
  <@S:…:class:datatype:record> a owl:Class ;
    rdfs:subClassOf [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:canonical:mapping> ],
                    [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty ns3:facets ],
                    [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:lexical:space> ],
                    [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:value:space> ],
                    [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:lexical:mapping> ],
                    <@S:…:class:specimen:record> .
  ```
  and `primordial:pair` = cardinality-1 on `ns3:key` + `ns3:value`, `owl:disjointWith
  …:binding:occurrence` (171–178). Plus 4 `sh:NodeShape` (e.g. `…:binding:occurrence` with property
  shapes `min1/max1 nodeKind sh:IRI` on `ns3:{position,subject,pair,provenance,carrier}`).

  So closure.ttl carries the **OWL-intensional definition** (cardinality restrictions, disjointness)
  that the consolidated instance graph only enforces via external SHACL — it is the "corrected kernel"
  the 1223 quarantine records were excluded from.

### 5b. `primordial.yaml` — the primordial TYPE-REGISTRY source
Top-level keys: `IDENTITY`, `ANCHORS`, `DEFINITIONS`, `AXIOMS`, `TYPES` (lines 1/2/30/457/1111).
IDENTITY = `…:order:primordial:family:type:genus:bourne:again:shell:species:ontology:component:
registry:instance:one` — the **bash-engine (bourne-again-shell) primordial type registry**. ANCHORS
enumerates the upper ontologies grounded onto: `urn:silmaril:…:grounding:ontology:basic:formal` ("Basic
Formal Ontology grounding anchor"), `…:common:core` (CCO), `…:process:cognitive` (CPO). Holds algebra
vocabulary (60 `magma|semigroup|monoid|group|abelian|ring|field` hits) as REGISTRY entries. This is the
generator of the `basicttl/primordial/type/**` fold target — i.e. the doctrine's Directive-25 target's
source of record. (Note: same shape family as the master primordial tree the spine folds INTO.)

### 5c. `physical.yaml` — the PHYSICAL facet carrier schema (Directive 8/9 floor)
IDENTITY = `…:domain:computation:kingdom:specification:phylum:ontology:class:registry:order:physical:
family:carrier:genus:schema:species:extension`. Structure `IDENTITY / ANCHORS / DEFINITIONS / AXIOMS`
with a `VECTOR / COUNT / MEMBER` triple (a vector of MEMBER definitions). Its MEMBER definitions are
the **bit/byte carrier floor**: bit vector ("Finite ordered vector over the two bit alternatives.
Vector extent is independent of host integer width."), byte schema ("…registered width from one
through one hundred twenty eight bits, independent bit traversal, octet permutation, and encoding
coordinates."), byte vector ("…Eight bit octet projection is partial and never pads implicitly."). This
is the unary-law carrier closure (Bit→Octet→ByteVector; width 1..128) as a physical-facet YAML,
anchored via `ANCHORS.VECTOR/COUNT/MEMBER` into the seed-registry `constructor:…:species:vector`.

### 5d. `runtime.yaml` — the RUNTIME field/execution-graph schema
IDENTITY = `…:domain:computation:kingdom:execution:phylum:ontology:class:registry:order:runtime:
family:schema:genus:bourne:again:shell:species:registry`. Structure: `CARDINALITY` (ONE/OPTIONAL/MANY
→ set-cardinality anchors) + `FIELDS`. Each FIELD (VALUE, SOURCE, TARGET, OUTPUT, …) is a typed record
with `IDENTITY / OWNER / VALUE / CARDINALITY` — e.g. `OUTPUT.OWNER =
…:phylum:algebra:class:product:order:unary:family:frame:genus:result:species:frame` (the **unary
Frame** as the output field's owner). This is the runtime projection of the Frame/execution-graph
(task nodes, dependency edges) with each field pinned to a typed carrier + a cardinality anchor — the
Directive-21 packed-Frame / typed-field discipline made concrete as the bash-engine's field schema.

---

## 6. Concrete TEMPLATES the spine fold must instantiate (in the reference's exact form)

These are transcriptions of the idioms above, retargeted to the SP0 algebra spine. Grammar per
Directive 25 = lowercase colon-descent inside `basicttl/primordial/type/**`; here shown against the
reference's `@P`/`@S` stems so the fold can pattern-match.

**T1 — DeclarationRecord + Denotatum + Gate triad** (per §1b) for each spine concept:
```
<…:theory:magma>            a owl:NamedIndividual, <…:type:declaration> ;
    <…:relation:denotatum>           <…:theory:magma:denotatum> ;
    <…:relation:assignment>          <…:theory:magma:gate> ;
    <…:relation:historical:identity> <urn:silmaril:kind:algebra:magma> ;   # compat bridge, D24
    <…:relation:identifier> "…:theory:magma" ; <…:relation:notation> "magma" ;
    <…:relation:primary:taxon> <…:taxon:theory> ; <…:relation:source:location> "…/algebra/spine.ttl" ;
    <…:relation:created> "…" ; <…:relation:modified> "…" ; <…:relation:version> "…" ;
    <…:relation:authority> "SYN|DS|PD" .
<…:theory:magma:denotatum> a owl:NamedIndividual, <…:type:external|…:type:theory:denotatum> ; … .
<…:theory:magma:gate>      a owl:NamedIndividual, <…:type:gate> ;
    <…:relation:check:status> "declaration reconciled; not a generic semantic proof" ;
    <…:relation:interpreted:by> <…:interpretation:algebraic:theory:record> .
```

**T2 — the (S,Ω,E) presentation the reference LEFT ABSENT** (fill the §3 gap): a `theory:magma`
individual bearing a `signature` (Ω = one binary `operation` with `relation:domain`/`codomain`), an
`equation` set (each `a …:algebra:structure:equation` with `relation:left`/`relation:right`), and a
`model`/carrier link; `theory:semigroup` = `theory:magma` + one added associativity `equation`;
`theory:monoid` = `theory:semigroup` + identity `operation` (nullary) + two identity `equation`s
(two-sided → TWO Equation records per D25); `theory:group` = `+ inverse operation + inverse equation`;
reducts as explicit `relation:reduct`/theory-morphism edges (reference has ZERO — must be authored new).

**T3 — foundation axiom record** (per §1d), one per declared law:
```
<…:axiom:magma:closure> a owl:NamedIndividual, <…:type:axiom> ;
    <…:relation:identifier> "…:axiom:magma:closure" ; <…:relation:notation> "magma closure" ;
    <…:relation:source:location> "…/algebra/spine.ttl" ;
    <…:relation:equation> <…:equation:magma:closure> .
<…:ontology:sp0:spine> <…:relation:foundation> <…:axiom:magma:closure> .
```
(closure.ttl variant: add `rdfs:comment "<law statement>. Checked exhaustively; not inferred from a
label."` and type it `…:species:axiom:record`.)

**T4 — theorem + certificate** (per §1e), for any spine result that is proved-not-postulated:
```
<…:theorem:group:inverse:uniqueness> a owl:NamedIndividual, <…:type:theorem> ;
    <…:relation:certificate> <…:certificate:group:inverse:uniqueness> ;
    <…:relation:notation> "group inverse uniqueness" .
<…:certificate:group:inverse:uniqueness> a owl:NamedIndividual, <…:type:certificate> ;
    <…:relation:digest:value> "<sha256>" ;
    <…:relation:proof:method> "Explicit general mathematical derivation; not proof-assistant checked" ;
    <…:relation:source:location> "…" .
```

**T5 — intensional record class (closure.ttl idiom, per §5a)** — give each record class real OWL:
```
<…:class:equation:record> a owl:Class ;
    rdfs:subClassOf [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:relation:left> ],
                    [ a owl:Restriction ; owl:cardinality "1" ; owl:onProperty <…:relation:right> ],
                    <…:class:specimen:record> .
```

**T6 — SHACL gate pair (per §4)** — one property-shape (coordinate separation) + one SPARQL
(non-vacuity/collision), per record class, each with `sh:message`:
```
<…:shape:theory> a sh:NodeShape ; sh:targetClass <…:type:theory:record> ;
    sh:message "An algebraic theory must carry exactly one signature, and at least one equation." ;
    sh:property [ sh:path <…:relation:signature> ; sh:minCount 1 ; sh:maxCount 1 ; sh:class <…:type:signature:record> ] ,
                [ sh:path <…:relation:equation>  ; sh:minCount 1 ;                 sh:class <…:type:equation:record> ] .
<…:shape:theory:unique> a sh:NodeShape ; sh:targetSubjectsOf <…:relation:identifier> ;
    sh:sparql [ a sh:SPARQLConstraint ;
        sh:message "theoryIdentifier must identify at most one theory in the validation graph." ;
        sh:select "SELECT $this WHERE { $this <…:relation:identifier> ?k . ?o <…:relation:identifier> ?k . FILTER(?o != $this) }" ] .
```

**T7 — finite-table validation-mode witness (per §1g)** — reified composition cells
(`category:first`=f, `category:second`=g, `category:result`=g∘f) as the executable model the T3 axioms
bite on, kept in `fixtures/` (positive) with a materialized failing `:negative` fixture per shape
(30 `:negative` subjects exist in the reference; a negative fixture is REQUIRED — `sh:conforms true`
alone is vacuous, D24).

**T8 — quarantine + bridge (per §1c, §2)** — any prior term not admitted:
```
<…:quarantine:prior:kind:algebra:magma> a owl:NamedIndividual, <…:type:quarantine> ;
    <…:relation:check:status> "preserved declaration; original axioms not admitted into corrected kernel" ;
    <…:relation:historical:identity> <urn:silmaril:kind:algebra:magma> ;
    <…:relation:notation> "silmaril:kind:algebra:magma — prior magma carrier" .
```

---

## 7. Load-bearing conclusions for the fold

1. **The reference's algebra tower is a bare `subClassOf` ladder of 17 "primitive" class stubs
   (magma…field + signature/term/equation/action), ZERO instances, ZERO reducts.** The spine fold must
   ADD the theory/model/reduct/(S,Ω,E) content the reference omits (T2); it cannot copy a populated
   tower because none exists.
2. **The reference's real mathematical kernel is the CATEGORY layer:** exactly 6 foundation axioms
   (category id/assoc, functor id/comp, naturality, sketch), 3 Yoneda theorem records each with a
   digest+proof-method certificate, a finite composition-table model, and the Seed-Carrier ∫M / coend
   / Yoneda-embedding constructions in closure.ttl. **Yoneda is a theorem record, never an axiom.**
3. **The record model is a 1:1:1 Declaration/Denotatum/Gate triad** (445 each) with a uniform
   provenance quartet (created/modified/version/state ×828) + `historical:identity` bridges (1670) +
   `identifier`/`notation` on nearly every record; check-status verdicts are honest
   ("declaration reconciled; not a generic semantic proof" / "preserved declaration; … not admitted
   into corrected kernel"), never a claimed proof.
4. **Intensionality lives in closure.ttl** (owl:Restriction cardinality-1 record classes + disjoint
   ness), enforcement lives in consolidated.shacl.ttl (52 NodeShapes, targetClass-only, property-shape
   exactly-one + 31 SPARQL non-vacuity/collision teeth, 83 messages). The fold must carry BOTH the OWL
   intensional class defs (T5) AND the SHACL teeth (T6), plus positive+negative fixtures (T7).
5. **Grammar + placement:** seed-registry descent `…:grounding:…:family:seed:genus:registry:species:*`
   is the closure/YAML idiom; instance descent `…:specimen:instance:*` is the consolidated idiom;
   `primordial.yaml`/`physical.yaml`/`runtime.yaml` are the bash-engine registry / bit-byte physical
   floor / Frame-runtime schema respectively — all three anchor on BFO+CCO+CPO and pin fields to typed
   carriers + cardinality anchors, the shape the Directive-25 `basicttl/primordial/type/**` fold adopts.
