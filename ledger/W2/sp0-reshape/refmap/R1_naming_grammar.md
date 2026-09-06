# REFMAP SHARD R1 — Naming Grammar (the URN descent law the fold must follow)

MAP-agent evidence. Quotes = file:line / grep counts. No opinions. Sources:
- `silmaril.final.consolidated.ttl` (repo root, 43,383 lines) — the "FOR CLAUDIUS" consolidated drop
- `silmaril.consolidated.repaired.ttl` (repo root, 82,953 lines)
- `refcomp/zip/silmaril/ontology/{primordial.yaml,consolidated.ttl,runtime.yaml,physical.yaml}` (verified-runtime project)
- `refcomp/tar/bash/aob/urn/**/atom.spec.yaml` (4101-file bash engine, the VERIFIED RUNTIME) + `bash/config/type-dag/*.yaml`
- `refcomp/zip/silmaril/docs/{baseline,grounding,continuation/capture}.md`
- Governing law: `ledger/W2/design_constraints.md` D24 (spec §10b naming law) + D25 (fold target).

scratchpad temp files used: `/tmp/claude-0/…/scratchpad/allurns_type.txt`, `/tmp/pyaml_urns.txt`, `/tmp/zipcons_urns.txt`, `/tmp/aob_paths.txt`.

---

## HEADLINE (the naming law in one sentence)

Every typed IRI is a **`urn:` NID = `silmaril`** URN whose descent is an **all-lowercase, colon-separated, genus-first** path with a **FIXED 6-segment literal prefix** (`type:graph:instance:instruction:code:property`) followed by a **fixed-MARKER / variable-VALUE Linnaean rank ladder** of twelve reserved marker keywords —
`domain : realm : subdomain : kingdom : phylum : class : order : family : genus : species : component : instance` —
where each marker is followed by a **one-or-more-segment differentia value**. This is the law realized by the VERIFIED-RUNTIME bash engine (`aob/urn/**`, 293 canonical atoms, ALL 12 markers present) and by `ontology/primordial.yaml`. **D24's "lowercase genus-first colon-descent" is the SUBSET/surface rule of this fuller taxonomy law** (§4). The root `silmaril.final.consolidated.ttl` shows a DEGENERATE fixed-spine variant (§1) that the fold must NOT copy.

---

## (0) THREE URN families in the root consolidated file — counts

`grep -oE "urn:silmaril:[a-z]+"` on `silmaril.final.consolidated.ttl` (occurrences):
```
  62234  urn:silmaril:type      (typed instances + predicates)
   1223  urn:silmaril:ontology  (primordial short vocabulary)
    445  urn:silmaril:seed      (seed-carrier manifest/anchor records)
```
Unique `urn:silmaril:type:` IRIs in root = **3,823**; total unique `urn:silmaril:*` = **5,491**.
The reference zip `ontology/consolidated.ttl` (78,692 lines) adds MORE prefix families — `core:entity` (2,637), `seed:manifest/external/map/algebra/decision/witness/gate/…`, `axiom:axiom` (51), `plan:ontology`, `engagement:cell` — i.e. the drop and the zip are NOT byte-identical grammars (see §6 discrepancy).

---

## (1) THE FULL URN DESCENT GRAMMAR

### 1a. Fixed literal leading prefix (invariant across ALL type: IRIs)
`allurns_type.txt`: **0 of 3,823** type: IRIs fail to start with
`urn:silmaril:type:graph:instance:instruction:code:property:`.
So the leading path is the fixed 6-segment literal `type : graph : instance : instruction : code : property` (after `urn:silmaril:`). No short forms of this head exist.

### 1b. Segment IMMEDIATELY after `…:code:property:` (root drop) — anchored counts
```
   3403 domain      → the entity/instance spine
    189 type        → type/predicate IRIs (type:algebra:structure:monoid, type:axiom …)
    108 example     → example/fixture data (no Linnaean spine)
     90 relation    → object/data-property predicates (relation:identifier …)
     22 shape       → SHACL shape IRIs
      6 law   2 ontology   2 operation   1 policy
```
So after `property:` the root branches into **`domain:` (entities)** vs **`type:`/`relation:`/`shape:` (predicates & types)** vs **`example:` (fixtures)**.

### 1c. **THE CANONICAL RANK LADDER (bash engine `aob/urn/**`, the verified runtime)**
Every one of the 293 `aob/urn/**/atom.spec.yaml` leaf paths carries the SAME 12 markers (grep count = 293 each for `realm subdomain kingdom phylum class order family genus species component instance`). One materialized path, segment-numbered (`bash/aob/urn/…/atom.spec.yaml`):
```
 1 silmaril      (NID authority)
 2 type   3 graph   4 instance   5 instruction   6 code   7 property   ← fixed literal head
 8 domain      / 9  mathematics   ← marker : value
10 realm       / 11 category
12 subdomain   / 13 small
14 kingdom     / 15 type
16 phylum      / 17 algebra
18 class       / 19 category
20 order       / 21 composition
22 family      / 23 morphism
24 genus       / 25 finite
26 species     / 27 category
28 component   / 29 type
30 instance    / 31 canonical
```
i.e. `…:property : domain:<D> : realm:<R> : subdomain:<SD> : kingdom:<K> : phylum:<P> : class:<C> : order:<O> : family:<F> : genus:<G> : species:<S> : component:<CMP> : instance:<I>`.
A rank VALUE may span multiple segments (e.g. `species:one:hundred:twenty:eight`, `subdomain:bit:width`, `species:byte:stream`); the twelve **marker keywords are reserved delimiters** that bound each rank. The eight classical Linnaean ranks (kingdom…species) sit at the CORE, wrapped by `domain/realm/subdomain` above and `component/instance` below.

### 1d. Are all IRIs full-taxonomy, or are there short forms? — BOTH exist, by ROLE
- **Instances/atoms** → FULL 12-rank path (bash `aob/urn/**`; primordial.yaml; root `…:domain:…:specimen:instance:<tail>`).
- **Primordial vocabulary** → SHORT genus-first descent `urn:silmaril:ontology:primordial:<subject>:<genus>:<differentia>` (e.g. `…:algebra:structure:monoid:commutative`). 1,223 occ in root.
- **Predicates** → `urn:silmaril:type:…:property:relation:<name>` / `…:property:type:<name>` (§3).
- **Seed records** → `urn:silmaril:seed:<subject>:<genus>:<differentia>` (445 occ).
So the full-taxonomy path is the law for **materialized instances**; primordial/predicate/seed vocab uses the same lowercase-genus-first colon grammar in a **shorter, un-ranked descent**.

---

## (2) RANK VOCABULARY — values seen at each rank + what governs them

**The ranks are VARIABLE-valued differentia, NOT a fixed spine.** Authoritative enumeration = bash `aob/urn/**` (293 atoms) and `ontology/primordial.yaml` (345 URNs). Selected value sets:

| rank marker | governing question | representative values (bash aob + primordial.yaml) |
|---|---|---|
| **domain** | top realm of discourse | `mathematics, computation, knowledge, logic, formal, physical, research, validation, information, semantic, process, system, software, runtime, resource…` (46 distinct in aob) |
| **realm** | sub-field of the domain | `algebra, category, geometry, topology, number, quantity, ontology, operation, representation, execution, identity, provenance, governance, semantic, test, formal…` (18 in aob) |
| **subdomain** | narrowed context | `group, morphism, small, categorical, bit, byte, callable, primordial, physical, set, natural, metric, object, type, pure, research, validation…` (37 in aob) |
| **kingdom** | ONTIC kind of the record | `type, axiom, law, theorem, certificate, definition, class, construction, assumption, bridge, evidence, specimen, operation, protocol, registry, shape, state, ontology, property, descriptor, error, gap, mapping, engine, constitution` (28 in aob) |
| **phylum** | formal category of that kind | `algebra, axiom, category, composition, operation, carrier, graph, ontology, specification, contract, type, value, relation, product, primordial, membership, identifier, grammar, closure, distance, measurement, purity, protocol, receipt, reference, registry, validation…` |
| **class** | structural class | `category, group, associativity, identity, inverse, closure, structure, monoid, magma, node, statement, value, typed, product, carrier, byte, octet, lambda, set, path, topology, triangle, symmetry, cardinality…` |
| **order** | ordering/arity/mode | `composition, binary, categorical, canonical, declarative, unary, ordered, primordial, effect, error, deterministic, metric, membership, eight, registered, sealed, reflexive, linearization…` |
| **family** | theory / lineage family | `morphism, group, monoid, semigroup, magma, algebra, category, operation, closure, byte, octet, stream, vector, width, type, set, space, topology, geometry, key, pair, node, resource, physical, primordial…` |
| **genus** | genus (immediate parent) | `finite, mathematical, formal, axiomatic, triple, neutral, composition, product, member, governed, natural, quantity, carrier, effect, unbounded, general, typed, specimen, primordial, pure, self…` |
| **species** | species (the leaf concept) | `category, group, monoid, associativity, identity, inverse, equality, member, arrow, functor, natural, byte, octet, one, two, four, eight, sixteen, thirty, sixty, node, pair, yoneda, presented, category/of/elements…` (127 distinct in aob) |
| **component** | facet of the atom | `type, statement, definition, category, group, morphism, member, element, object, set, node, operation, provenance, receipt, registry, runtime, value, grounding, manifest, contract, admission, catalog, class, engine, frame, geometry, graph, input, ontology, test, topology` (31 in aob) |
| **instance** | occurrence marker | `canonical, actor, alpha, beta, gamma, current, root, version, request, role, endpoint, graph, instruction, manifest, measure, missing, path, read, authority, corpus` (20 in aob) |

**What governs them:** `docs/baseline.md:9` — *"Meaningful complete ranked lineage … Independent domain/kingdom/phylum differentia and admissibility proofs for every taxon"*; `:11` — *"Every rank edge has differentia, authority, provenance, state, receipt"*; `:12` — *"No skipped/fused/padded/misplaced ranks"*; `:22` — *"Taxonomic path reverses to exact lineage."* → Each rank value is a **differentia** governed by an admissibility/authority record; the path must round-trip to the lineage. Baseline marks these as *Partial / not-implemented* — i.e. the SEMANTIC-rank requirement is the doctrine, the collapse is the debt.

### 2-note: the root drop's ranks are COLLAPSED to constants (the anti-pattern)
For all **3,403** full-spine research-infrastructure instances in `silmaril.final.consolidated.ttl`, the eight Linnaean ranks are FIXED literals (grep counts, each = 3403):
```
kingdom:knowledge   phylum:formal   class:typed   order:declarative
family:execution    genus:graph     species:runtime   specimen:instance
```
i.e. the root drop uses `…:domain:computational:economics:research:infrastructure:kingdom:knowledge:phylum:formal:class:typed:order:declarative:family:execution:genus:graph:species:runtime:specimen:instance:<TAIL>` and pushes the REAL concept into a free `<TAIL>` after `specimen:instance:` (tail heads by count: `construct` 10783, `fixture` 8650, `historical` 8561, `axiom` 42, `theorem` 18, `certificate` 24 …). **This is a padded/fused-rank degeneracy (baseline `:12`).** The fold must adopt the VARIABLE-rank law of §1c, not this fixed spine. (Note also: root uses `specimen:instance` as a NINTH marker pair; the verified bash engine uses `component:instance` — the fold should follow the runtime `component`/`instance` pair.)

---

## (3) PREDICATE NAMING

Predicates live under `urn:silmaril:type:graph:instance:instruction:code:property:` then `relation:` (object/data props), `type:` (rdf:type targets/classes), or `shape:` (SHACL). All lowercase genus-first colon-descent; deeper qualifier = later segment.

**`relation:*` predicates** (90 unique in root; full IRI e.g. `urn:silmaril:type:graph:instance:instruction:code:property:relation:identifier`):
```
relation:identifier          relation:notation            relation:source:location
relation:source:url          relation:source:kind         relation:source:section
relation:provenance          relation:provenance:document relation:provenance:occurrence
relation:proof:method        relation:proof:text          relation:check:status
relation:definition:status   relation:classified:rank     relation:primary:taxon
relation:taxon:parent        relation:path:parent         relation:historical:identity
relation:member  relation:member:ordinal  relation:member:value  relation:member:vector
relation:domain  relation:codomain        relation:left    relation:right   relation:pair
relation:category:composition relation:category:identity relation:category:source
relation:category:target      relation:category:object   relation:category:arrow
relation:execution:node/operation/output/effect/errors/receipt/digest
relation:position:{line,offset,path,ordinal,depth}   relation:created  relation:modified …
```
Confirms the prompt's exemplars: **`relation:identifier`, `relation:notation`, `relation:source:location`** all present verbatim.

**`type:*` predicate/class IRIs** (189 unique) — the type namespace names structures:
```
type:axiom                    (verbatim; prompt exemplar ✓)
type:algebra:structure        type:algebra:structure:{monoid,group,ring,field,module,magma,
                              semigroup,lattice,signature,term,equation,representation,
                              boolean:algebra,relation:algebra,vector:space,action}
type:category                 type:category:structure:{functor,limit,colimit,product,coproduct,
                              pullback,pushout,adjunction,presheaf,representable,coend,
                              natural:transformation,category:of:elements,presented:category,
                              small:category,yoneda:embedding}
type:group   type:cardinality  type:carrier  type:binding  type:boolean  type:bytes …
```
Rule: **predicate/type IRI = `property:<facet>:<genus>[:…:<differentia>]`, lowercase, genus-first.**

---

## (4) RECONCILIATION with Directive 24 (§10b) + USER_REF_00

D24 naming law verbatim (`design_constraints.md:456-460`):
> "**Naming law (spec §10b):** ALL LOWERCASE, every segment; compounds decompose into `:` descents, GENUS-FIRST (`NaturalTransformation`→`transformation:natural`; `CategoryOfElements`→`category:elements`); no `-`/`_` in any typed identifier (file names keep the repo underscore convention). Consequence: every CamelCase/underscore `fnd:` local name is renormalized with an alias/bridge map so nothing is silently lost."

**D24 is the SURFACE (per-segment) rule; the full-taxonomy rank ladder (§1c) is the STRUCTURAL law it lives inside.** They agree on:
- ALL lowercase, every segment — confirmed: 0 uppercase in any `urn:silmaril:*`.
- `:` descents, no `-`/`_` in typed IRIs — confirmed across root + aob + primordial.
- genus-first for DIFFERENTIA — confirmed: `monoid:commutative` (2 occ) with `commutative:monoid` = **0**; `group:abelian` (4) vs `abelian:group` = **0**; `ring:division`, `field:finite`, `module:free` all genus-first.

**DISCREPANCY the fold must resolve (honest-red):** D24 prescribes `NaturalTransformation → transformation:natural` and `CategoryOfElements → category:elements`. The ROOT reference drop instead uses:
```
natural:transformation   9 occ   |  transformation:natural   0 occ
category:of:elements    12 occ   |  category:elements         0 occ
```
So the root drop is **NOT genus-first for these compound proper-names** (it keeps adjective-first `natural:transformation` and even preserves the stop-word `of`). The bash engine agrees with the drop's spirit (`species:category:of:elements`). → **D24 §10b and the reference materials CONFLICT on multi-word proper names.** D24 is the governing law (design_constraints); the reference is the implementation. This must be flagged to the planner: either D24's `transformation:natural`/`category:elements` renderings win (and the reference is renormalized), or D24's two illustrative examples are amended. Record as a naming-law open question, not a silent choice.

USER_REF_00 is cited as the D24 authority source (`design_constraints.md:432`) but is NOT present in repo or scratchpad (`find -iname "*USER_REF*"` = 0 hits; the seed-carrier spec zip is "NOT committed" per `:435`). `docs/continuation/capture.md:11` independently confirms the model — *"a ranked observation URN"* — corroborating the ranked-URN law without the primary text.

---

## (5) HOW AN ALGEBRA CONCEPT IS NAMED — exact URN forms + derivation rule

Same concept appears in THREE roles, each with its own descent. Worked from the VERIFIED bash engine `aob/urn/**` (canonical) + root primordial vocab + root instance tails.

### 5a. The STRUCTURE / type (kingdom:type, component:type)
Bash aob, group as a type (`…/property/…/atom.spec.yaml`):
```
…:domain:mathematics:realm:algebra:subdomain:group:kingdom:type:phylum:algebra:
  class:group:order:binary:family:operation:genus:axiomatic:species:group:
  component:type:instance:canonical
```
category as a type:
```
…:domain:mathematics:realm:category:subdomain:small:kingdom:type:phylum:algebra:
  class:category:order:composition:family:morphism:genus:finite:species:category:
  component:type:instance:canonical
```
primordial.yaml monoid as a type:
```
urn:silmaril:type:graph:instance:instruction:code:property:grounding:ontology:basic:formal:
  domain:mathematics:kingdom:formal:phylum:algebra:class:structure:order:identity:
  family:monoid:genus:mathematical:species:monoid
```

### 5b. The AXIOM / law (kingdom:axiom, component:statement)
Bash aob — the FOUR group axioms share `subdomain:group` + `family:group`; each is a distinct record differing at `class:` (the law):
```
associativity : kingdom:axiom:phylum:operation:class:associativity:order:binary:family:group:genus:composition:species:equality:component:statement:instance:canonical
identity      : kingdom:axiom:phylum:operation:class:identity:order:binary:family:group:genus:neutral:species:member:component:statement:instance:canonical
inverse       : kingdom:axiom:phylum:operation:class:inverse:order:binary:family:group:genus:member:species:inverse:component:statement:instance:canonical
closure       : kingdom:axiom:phylum:operation:class:closure:order:binary:family:group:genus:product:species:membership:component:statement:instance:canonical
```
Category associativity axiom (different realm/family = category/morphism, same law class):
```
…:domain:mathematics:realm:category:subdomain:morphism:kingdom:axiom:phylum:composition:
  class:associativity:order:categorical:family:morphism:genus:triple:species:equality:
  component:statement:instance:canonical
```
primordial.yaml monoid/semigroup associativity + identity element:
```
…domain:mathematics:kingdom:law:phylum:axiom:class:statement:order:canonical:family:category:genus:formal:species:associativity
…domain:mathematics:kingdom:law:phylum:axiom:class:statement:order:canonical:family:semigroup:genus:formal:species:associativity
…domain:mathematics:kingdom:law:phylum:axiom:class:statement:order:canonical:family:monoid:genus:formal:species:identity:element
```

### 5c. The PRIMORDIAL short vocabulary (root `ontology:primordial:*`)
```
urn:silmaril:ontology:primordial:algebra:structure:monoid            (+ :monoid:{commutative,cancellative,finite,free,ordered,topological})
urn:silmaril:ontology:primordial:algebra:structure:group            (+ :group:{abelian,cyclic,finite,free,lie,matrix,nilpotent,permutation,simple,solvable,topological,algebraic})
urn:silmaril:ontology:primordial:algebra:structure:{magma,semigroup,ring,field,module,semiring,algebra}
urn:silmaril:ontology:primordial:algebra:law:associativity
urn:silmaril:ontology:primordial:algebra:law:commutativity
urn:silmaril:ontology:primordial:algebra:law:identity:two:sided     ← D24 §497 "two Equation records"
urn:silmaril:ontology:primordial:algebra:law:inverse:two:sided
urn:silmaril:ontology:primordial:algebra:law:<name>:specification   (52 laws: absorption, cancellation, closure, distributivity, idempotence, monad, naturality, jacobi, …)
urn:silmaril:ontology:primordial:category:monoidal
urn:silmaril:ontology:primordial:feature:algebra:structure:monoid   ← parallel feature/ mirror
```
Root instance tail (fixed-spine form, §2-note) for axioms/theorems:
```
…specimen:instance:axiom:category:associativity   …axiom:category:identity
…specimen:instance:axiom:functor:composition       …axiom:functor:identity   …axiom:naturality
…specimen:instance:theorem:yoneda   …theorem:yoneda:full:faithfulness   …theorem:covariant:co:yoneda
…specimen:instance:certificate:yoneda   (Yoneda = theorem+certificate, NEVER axiom → matches D24:450)
```

### 5d. DERIVATION RULE (the law the fold applies to name a new algebra concept)
1. Pick `domain:mathematics`, `realm:algebra` (or `realm:category` for categorical), `subdomain:<theory>` (e.g. `group`, `monoid`, `morphism`).
2. **A type/structure** → `kingdom:type`, `phylum:algebra`, `class:<structure>`, `order:<arity>` (e.g. `binary`), `family:operation|<theory>`, `genus:axiomatic|<parent>`, `species:<leaf>`, `component:type`, `instance:canonical`.
3. **An axiom/law** → `kingdom:axiom`, `phylum:operation|composition`, `class:<lawname>` (associativity/identity/inverse/closure/…), `order:<arity>`, `family:<theory>`, `genus:<role>` (composition/neutral/member/product/triple…), `species:equality|member|membership|inverse`, `component:statement`, `instance:canonical`.
4. **A theorem** → `kingdom:theorem` + a paired `kingdom:certificate` record (never an axiom).
5. Laws of ONE theory share `subdomain`+`family` and diverge only at `class` (+ genus/species) → distinct IRIs per law (satisfies D24 A0 no-collapse: theory / model / operation / equation / element / proof are separate records, distinct IRIs — `design_constraints.md:436-443`).
6. Multi-word leaf: lowercase colon-descent; **D24 says genus-first** (`transformation:natural`), **reference says adjective-first** (`natural:transformation`) — OPEN (§4).

---

## COVERAGE ATTESTATION (Praeriehund)
- Read/grepped: root `silmaril.final.consolidated.ttl` (all 3 URN families, 3,823 unique type: IRIs, rank counts, algebra vocab, axiom/theorem tails); `refcomp/zip/silmaril/ontology/primordial.yaml` (345 URNs, all 8 ranks enumerated) + `consolidated.ttl` (8,986 URNs, prefix families); bash `aob/urn/**` (293 canonical atoms, 12-marker skeleton verified 293/293) + `config/type-dag/objects.yaml`; `docs/{baseline,grounding,continuation/capture}.md`; `design_constraints.md` D24/D25.
- COMPLETE for: leading-path prefix, 12-marker rank ladder + per-rank value tables, predicate naming, primordial+axiom+theorem algebra forms, D24 reconciliation, derivation rule.
- GAPS: (a) USER_REF_00.md + `docs/specs/2026-08-19-seed-carrier-rewrite-design.md` §10b PRIMARY TEXT are NOT in repo/scratchpad (uncommitted zip) — D24's quoted summary used instead. (b) The **genus-first vs adjective-first conflict** for multi-word proper names (`transformation:natural` vs `natural:transformation`; `category:elements` vs `category:of:elements`) is UNRESOLVED between D24 and the reference — planner must decide. (c) Root drop uses a COLLAPSED fixed-spine (`kingdom:knowledge…specimen:instance`) that DIVERGES from the verified bash-engine variable-rank law + `component:instance` markers — the fold must follow the RUNTIME (aob/urn) law, not the drop's degeneracy. (d) Did not exhaustively diff all 5,491 root IRIs against all 4,101 bash files — sampled the algebra/category/axiom cores which the fold spine (D25 pass 1) needs.
