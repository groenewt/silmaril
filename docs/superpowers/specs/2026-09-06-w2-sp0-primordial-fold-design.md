# W2 · SP0 — the primordial spine-fold (algebra tower → `basicttl/primordial/type/algebra/**`) — design

> **superpowers:brainstorming output** (design-first HARD GATE). PLAN ONLY — no `.ttl`/`.sparql`/
> `.sh`/`.yml` authored here, no ontology edited, no git run. This is the planner/validator
> deliverable of the operator loop; the executor materialises it under parallel shadow review.
> Governing law: `ledger/W2/design_constraints.md` Directives **24** (Seed-Carrier doctrine), **25**
> (whole-floor reshape folded into primordial, spine-first, CI lockstep), **26** (LOCKED naming: full
> verified-runtime Linnaean-ladder IRIs verbatim, natural-language segment order). Maps:
> `ledger/W2/sp0-reshape/refmap/{00_REFMAP_SYNTHESIS,R1_naming_grammar,R2_consolidated_shape,R3_engine_algebra_skills,R4_docs_doctrine_gates}.md`.
> Reference to MATCH: `silmaril.final.consolidated.ttl` + the verified runtime
> (`…/scratchpad/refcomp/zip/silmaril/**`) + the engine
> (`…/scratchpad/refcomp/tar/bash/**`, the `aob/urn/**` full-ladder IRI corpus). Praeriehund honesty:
> every VERBATIM IRI below is grep-confirmed off disk (`file:line` cited); every DERIVED/SYN token is
> flagged and routed to the §7 maintainer sign-off.

---

## 0. Decisions recap — the three governing gates

**D24 (Seed-Carrier gospel).** The A0 stratification `Syntax ⊥ Theory ⊥ Model ⊥ Element ⊥
ProofArtifact` is law. `fnd:Group a owl:Class, fnd:PresentedAlgebra` (the current
`algebra_spine.ttl` shape) is the **forbidden collapse** — it must split into a *theory* individual
`(S,Ω,E)`, a *model* class, *operation-symbol* individuals, *equation* individuals, *carrier
elements*, and *proof records*, each a distinct IRI. A6: every structure is a model of a declared
Lawvere theory `T=(S,Ω,E)`; the tower is theories + model-classes + reducts/theory-morphisms, **not**
a subclass ladder of witness-defined classes. Four disjoint planes:
Denotatum / DeclarationRecord / EvidenceArtifact / ProvenanceArtifact — named witnesses are
EVIDENCE and move OUT into `fixtures/` (positive + a **failing** negative per shape; `sh:conforms
true` alone is vacuous). Each structure declares a validation MODE (finite:table / rewrite /
external:certificate / bounded:diagnostic) and an 8-value proof-status. Yoneda is a *theorem* record
with a certificate, never an axiom. Bridge, never duplicate (TODO-11).

**D25 (fold into primordial, spine first).** The reshaped algebra floor lands **inside**
`basicttl/primordial/type/**`, adopting its directory/file layout — but bringing the D24
stratification primordial lacks, and *fixing* (never importing) primordial's punning/extensional
flaws in the algebra subtree it touches. `fnd:` as a separate root is retired into the primordial
idiom via an exhaustive alias/bridge map. **Cadence = spine first, then fan out**: Pass 1 reshapes
ONLY the one-operation algebra tower
(magma→semigroup→monoid→commutative-monoid→group→abelian + quasigroup/loop) as the
exemplar-conformant TEMPLATE; the maintainer signs off on the *realized* pattern; then it fans across
rings/fields/modules/vector-spaces, set, spaces, functionality, combinators, logic, group-action,
Blotto, and the D21 epistemology stratum. Technical resolutions: two-sided identity/inverse = **TWO
Equation records + an obligation-counting extension morphism**; CI + runner + gates move IN LOCKSTEP
or the teeth go vacuous; commits signed under `commit_signing_trust.ttl`.

**D26 (naming LOCK — the runtime full Linnaean ladder is canonical).** Every minted typed IRI carries
the complete 12-marker descent `domain:realm:subdomain:kingdom:phylum:class:order:family:genus:
species:component:instance` under the leading path
`urn:silmaril:type:graph:instance:instruction:code:property:…`, VERBATIM as the verified runtime
realizes it (`bash aob/urn/**`, 293/293 markers). Use the runtime's **`component:instance`**, NOT the
drop's collapsed `specimen:instance`. Segment order = the reference's **natural-language order**
(`natural:transformation`, `category:of:elements`, `monoid:commutative`, `group:abelian` — stop-words
kept), NOT D24 §10b's genus-first forms (0 occurrences in the reference; **D24 §10b is amended, the
reference governs**). The short primordial root `urn:silmaril:primordial:type:` is **bridged to, never
the IRI grammar**. Directory PLACEMENT (`basicttl/primordial/type/algebra/**`) still stands —
placement ≠ IRI root.

**The one-line reconciliation of the two tensions.** D26 governs the *IRI grammar*; D24/A0-A6 governs
*which atoms exist*. The verified runtime carries the algebra tower ONLY as a FLAT `subdomain:group`
(1 model type + 4 collapsed two-sided axioms) plus the abstract `subdomain:primordial` root — i.e. the
runtime IS the A0 collapse D24 fixes. Therefore **the build mints MORE atoms than the runtime shows
for algebra, each in full-ladder grammar**: the group model + its 4 axioms + the progenitor are quoted
VERBATIM as anchors; every other rung and every stratified plane (theory / signature / operation-symbol
/ equation-set / reduct) is DERIVED by extending the grep-confirmed group skeleton with tower-specific
rank vocabulary. This "mint more, same grammar" ruling is the pivotal maintainer checkpoint (§7).

---

## 1. Fold placement + the full-ladder IRI table for the spine

### 1.1 Target paths (D25 placement; D26 grammar)

```
basicttl/primordial/type/algebra/
  spine/
    progenitor.ttl                 # fnd:AlgebraicStructure → progenitor theory-root
    magma.ttl  semigroup.ttl  monoid.ttl  commutative_monoid.ttl
    group.ttl  abelian_group.ttl  quasigroup.ttl  loop.ttl
  signatures.ttl                   # sigOneBinary / sigMonoid / sigGroup / sigQuasigroup / sigLoop
  operations.ttl                   # product · , unit e , inverse inv , \ , /
  equations.ttl                    # equation-set objects + equation records (= the axiom atoms)
  reducts.ttl                      # theory-morphism / forgetful reduct edges
  records.ttl                      # intensional record CLASSES (owl:Restriction bundles)
  bridges.ttl                      # alias/bridge map: fnd:* + engine aob + primordial short root + seed
  shapes/algebra.shapes.ttl        # SHACL pair per record class (min1/max1 + sh:sparql)
  fixtures/                        # 1 positive + 1 FAILING negative per shape + empty.ttl control
    monoid_z2.ttl  monoid_z2_negative.ttl  group_z3.ttl  group_z3_negative.ttl  … empty.ttl
  probes/*.rq                      # non-vacuity / identity-collision / law probes
  manifests/*.yaml                 # deep-KV; counts DERIVED, never hard-coded
  checks/run-algebra-checks.sh     # NEW runner (wired into ci.yml in lockstep, §4)
```

File names keep the repo underscore convention (D26 surface law: no `-`/`_` inside a *typed IRI*, but
file names may). Directory placement is under the primordial tree; IRIs mint the full runtime ladder
and carry bridge edges to the primordial short root.

### 1.2 Notation

Let **HEAD** = `urn:silmaril:type:graph:instance:instruction:code:property:domain:mathematics:realm:algebra:subdomain:`.
Every IRI below = **HEAD** + the shown tail. `[V]` = quoted byte-for-byte off disk (grep-confirmed);
`[D]` = derived by extending the group skeleton with primordial.yaml tower vocab; `[S]` = a token with
no runtime precedent, flagged for §7 sign-off.

### 1.3 Progenitor (theory-root, ABSTRACT, grounds nothing) — `[V]`

```
primordial:kingdom:type:phylum:algebra:class:structure:order:axiomatic:family:primordial:genus:algebra:species:root:component:type:instance:canonical
```
Grep-confirmed at `refcomp/tar/bash/aob/urn/.../subdomain/primordial/...` + `config/algebra/
primordials.yaml:395-402` (ABSTRACT VALUE `true`). This is exactly `fnd:AlgebraicStructure`
("grounds nothing", `basicttl/foundation/algebra_spine.ttl:408-411`).

### 1.4 Model classes — descent `kingdom:type:phylum:algebra:…:family:operation:genus:axiomatic:…:component:type:instance:canonical`

| rung | subdomain | tail (after HEAD) | tag |
|---|---|---|---|
| group `[V]` | `group` | `group:kingdom:type:phylum:algebra:class:group:order:binary:family:operation:genus:axiomatic:species:group:component:type:instance:canonical` | grep-confirmed `primordials.yaml:441` / `aob/.../subdomain/group/kingdom/type/...` |
| magma | `magma` | `magma:kingdom:type:phylum:algebra:class:magma:order:binary:family:operation:genus:axiomatic:species:magma:component:type:instance:canonical` | `[D]` |
| semigroup | `semigroup` | `semigroup:kingdom:type:phylum:algebra:class:semigroup:order:binary:family:operation:genus:axiomatic:species:semigroup:component:type:instance:canonical` | `[D]` |
| monoid | `monoid` | `monoid:kingdom:type:phylum:algebra:class:monoid:order:binary:family:operation:genus:axiomatic:species:monoid:component:type:instance:canonical` | `[D]` |
| commutative-monoid | `monoid:commutative` | `monoid:commutative:kingdom:type:phylum:algebra:class:monoid:commutative:order:binary:family:operation:genus:axiomatic:species:monoid:commutative:component:type:instance:canonical` | `[D]` (compound `[S]`, see risks) |
| abelian-group | `group:abelian` | `group:abelian:kingdom:type:phylum:algebra:class:group:abelian:order:binary:family:operation:genus:axiomatic:species:group:abelian:component:type:instance:canonical` | `[D]` |
| quasigroup | `quasigroup` | `quasigroup:kingdom:type:phylum:algebra:class:quasigroup:order:binary:family:operation:genus:axiomatic:species:quasigroup:component:type:instance:canonical` | `[D]` |
| loop | `loop` | `loop:kingdom:type:phylum:algebra:class:loop:order:binary:family:operation:genus:axiomatic:species:loop:component:type:instance:canonical` | `[D]` |

Compound order `monoid:commutative` / `group:abelian` follows the reference (`monoid:commutative`
2 occ, `commutative:monoid` 0; `group:abelian` 4 occ, `abelian:group` 0 — `R1_naming_grammar.md §4`,
`design_constraints.md:524-530`). The multi-segment subdomain value is consistent with the runtime's
own `subdomain:bit:width` / `subdomain:open:set` idiom but has no algebra precedent to copy — §7.

### 1.5 Added-law axiom atoms — descent `kingdom:axiom:phylum:operation:class:<law>:order:binary:family:<theory>:genus:<role>:species:<leaf>:component:statement:instance:canonical`

VERBATIM role vocabulary comes from the 4 grep-confirmed group axioms
(`aob/.../subdomain/group/kingdom/axiom/...`, `primordials.yaml:452-467`):
closure→`genus:product:species:membership`; associativity→`genus:composition:species:equality`;
identity→`genus:neutral:species:member`; inverse→`genus:member:species:inverse`.

| added law (rung) | tail (after HEAD) | tag |
|---|---|---|
| closure (magma) | `magma:kingdom:axiom:phylum:operation:class:closure:order:binary:family:magma:genus:product:species:membership:component:statement:instance:canonical` | `[D]` |
| associativity (semigroup) | `semigroup:kingdom:axiom:phylum:operation:class:associativity:order:binary:family:semigroup:genus:composition:species:equality:component:statement:instance:canonical` | `[D]` |
| commutativity (comm-monoid) | `monoid:commutative:kingdom:axiom:phylum:operation:class:commutativity:order:binary:family:monoid:commutative:genus:composition:species:equality:component:statement:instance:canonical` | `[D]` |
| commutativity (abelian) | `group:abelian:kingdom:axiom:phylum:operation:class:commutativity:order:binary:family:group:abelian:genus:composition:species:equality:component:statement:instance:canonical` | `[D]` (own atom, off group — no-cram) |
| latin-division (quasigroup) | `quasigroup:kingdom:axiom:phylum:operation:class:division:order:binary:family:quasigroup:genus:latin:species:unique:component:statement:instance:canonical` | `[S]` (`genus:latin`/`species:unique` unattested) |

The reference group anchors, quoted for the executor to copy verbatim:
```
HEAD+group:kingdom:axiom:phylum:operation:class:closure:order:binary:family:group:genus:product:species:membership:component:statement:instance:canonical          [V]
HEAD+group:kingdom:axiom:phylum:operation:class:associativity:order:binary:family:group:genus:composition:species:equality:component:statement:instance:canonical  [V]
HEAD+group:kingdom:axiom:phylum:operation:class:identity:order:binary:family:group:genus:neutral:species:member:component:statement:instance:canonical             [V]
HEAD+group:kingdom:axiom:phylum:operation:class:inverse:order:binary:family:group:genus:member:species:inverse:component:statement:instance:canonical             [V]
```

### 1.6 Two-sided split (D25 technical resolution) — TWO equation/axiom records + one obligation-counting morphism

The runtime carries a single two-sided identity and a single two-sided inverse. D24/D25 require each
as **two** Equation records (left case + right case) plus an obligation-counting extension morphism
(count = 2). The side is carried as an extra `species` segment (`member:left`/`member:right`,
`inverse:left`/`inverse:right`); the **exact placement of the side segment is OPEN** (§7).

| record | tail (after HEAD) | tag |
|---|---|---|
| monoid-identity-left | `monoid:kingdom:axiom:phylum:operation:class:identity:order:binary:family:monoid:genus:neutral:species:member:left:component:statement:instance:canonical` | `[S]` (side seg) |
| monoid-identity-right | `monoid:…:species:member:right:component:statement:instance:canonical` | `[S]` |
| group-inverse-left | `group:kingdom:axiom:phylum:operation:class:inverse:order:binary:family:group:genus:member:species:inverse:left:component:statement:instance:canonical` | `[S]` |
| group-inverse-right | `group:…:species:inverse:right:…` | `[S]` |
| loop-identity-left/right | `loop:…:family:loop:genus:neutral:species:member:left\|right:…` | `[S]` |
| monoid-identity extension | `monoid:kingdom:mapping:phylum:composition:class:extension:order:declarative:family:monoid:genus:obligation:species:count:two:component:definition:instance:canonical` | `[S]` (`genus:obligation`/`count:two`) |
| group-inverse extension | `group:…:class:extension:…:family:group:genus:obligation:species:count:two:…` | `[S]` |

### 1.7 Signature atoms (shared per Σ) — `kingdom:definition:phylum:specification:class:signature:order:<profile>:family:operation:genus:algebraic:species:signature:component:definition:instance:canonical`

`kingdom:definition`, `phylum:specification`, `component:definition` are all attested; `genus:algebraic`
is `[S]`. sigOneBinary (magma+semigroup, Σ={·}) under `subdomain:magma`; sigMonoid (monoid+comm-monoid,
Σ={·,e}) under `monoid`; sigGroup (group+abelian, Σ={·,e,inv}) under `group`; sigQuasigroup (Σ={·,\,/})
under `quasigroup`; sigLoop (Σ={·,\,/,e}) under `loop`.

### 1.8 Operation-symbol atoms — `kingdom:operation:phylum:primitive:class:<op>:order:<arity>:family:operation:genus:<role>:species:<op>:component:operation:instance:canonical`

`kingdom:operation`/`phylum:primitive`/`component:operation` attested (aob set-cardinality +
file-read atoms). product `·` (binary) `genus:composition:species:product`; unit `e` (**order:nullary
`[S]`** — runtime has unary/binary/eight, no nullary; fallback `order:constant`) `genus:neutral:
species:identity`; inverse `inv` (unary) `genus:member:species:inverse`; `\` `genus:left:species:
division` (binary); `/` `genus:right:species:division`.

### 1.9 Equation-set objects + reduct edges

Equation-**set** (per rung): `kingdom:construction:phylum:algebra:class:equation:set:order:declarative:
family:operation:genus:presentation:species:<theory>:equations:component:definition:instance:canonical`
`[D]` (`kingdom:construction`+`component:definition` attested). The individual equation records ARE the
added-law axiom atoms of §1.5–1.6 (the runtime models each law as ONE `kingdom:axiom…component:
statement` atom that is simultaneously the equation; `component:equation` is unattested — reuse the
axiom atom; §7 alternative: mint kingdom:law equation records).

Reduct / theory-morphism (child→parent, A6): `kingdom:mapping:phylum:composition:class:reduct:order:
forgetful:family:morphism:genus:theory:species:<child>:to:<parent>:component:definition:instance:
canonical` `[S]` (`order:forgetful`/`genus:theory` unattested). Edges: semigroup→magma,
monoid→semigroup, commutative-monoid→monoid, group→monoid, abelian-group→group, quasigroup→magma,
loop→quasigroup. magma→AlgebraicStructure is an `rdfs:subClassOf` to the progenitor (NOT a reduct — the
progenitor grounds nothing).

### 1.10 Per-rung composition map (from `algebra_spine.ttl:426-522`, verbatim)

| rung | parent | adds law | signature | equation-set |
|---|---|---|---|---|
| magma | AlgebraicStructure | closure | sigOneBinary | eqsMagma {closure} |
| semigroup | magma | associativity | sigOneBinary | +associativity |
| monoid | semigroup | identity (→left+right) | sigMonoid | +identity |
| commutative-monoid | monoid | commutativity | sigMonoid | +commutativity |
| group | monoid | inverse (→left+right) | sigGroup | +inverse |
| abelian-group | group | commutativity (own atom) | sigGroup | +commutativity |
| quasigroup | magma | latin-division | sigQuasigroup | {closure, latin-division} |
| loop | quasigroup | identity (→left+right, own atom) | sigLoop | +identity |

---

## 2. Record templates — the MONOID rung END-TO-END in the locked grammar

Predicate abbreviations (consolidated namespace, `R2_consolidated_shape.md §2`):
`@P` = `urn:silmaril:type:graph:instance:instruction:code:property`; `@rel` = `@P:relation`;
`@typ` = `@P:type`; `@Am` = HEAD+`monoid`. Record CLASSES are the closure.ttl seed-carrier record
classes (`axiom:record`/`theorem:record`/`construction:record`/`specimen:record`) REUSED as
`rdf:type` targets (bridge-never-duplicate), extended with parallel algebra record classes
(theory/model/signature/equation) built in the same seed-registry descent with the same
`owl:Restriction` idiom.

**(a) Theory record `(S,Ω,E)`.**
```
<@Am:kingdom:definition:phylum:algebra:class:theory:order:declarative:family:monoid:genus:presented:species:monoid:component:definition:instance:canonical>   [S: class:theory/genus:presented]
  a owl:NamedIndividual, <@typ:declaration> ;
  <@rel:signature>  <…sigMonoid> ;
  <@rel:equation>   <…closure-axiom>, <…associativity-axiom>,
                    <…identity-left>, <…identity-right> ;
  <@rel:reduct>     <…theory:semigroup> ;               # NEW predicate, :reduct:=0 in reference
  <@rel:denotes>    <…monoid model class> ;
  <@rel:validation:mode>  "rewrite" ;                    # NEW (D24 4-value)
  <@rel:proof:status>     "literature:backed" ;          # NEW (D24 8-value); monoid = the lifted rung
  <@rel:denotatum>  <…:denotatum> ; <@rel:assignment> <…:gate> ;
  <@rel:identifier> "<full URN>" ; <@rel:notation> "monoid" ;
  <@rel:primary:taxon> <…taxon node> ;
  <@rel:created>/<@rel:modified>/<@rel:version>/<@rel:state> … ;   # provenance quartet
  <@rel:authority> "DS" ;                                # monoid is the one lifted rung (algebra_spine.ttl:36)
  <@rel:historical:identity> fnd:Monoid,
     <urn:silmaril:ontology:primordial:algebra:structure:monoid> . # bridges (§5)
```

**(b) Model class + intensional bundle.**
```
<@Am:kingdom:class:phylum:algebra:class:model:order:declarative:family:monoid:genus:governed:species:monoid:component:class:instance:canonical>   [S: class:model/genus:governed]
  a owl:Class ;
  rdfs:subClassOf
    [ a owl:Restriction; owl:cardinality "1"^^xsd:nonNegativeInteger; owl:onProperty <@rel:carrier> ],
    [ a owl:Restriction; owl:cardinality "1"; owl:onProperty <@rel:identity:element> ],
    [ a owl:Restriction; owl:cardinality "1"; owl:onProperty <@rel:operation> ],
    <@typ:algebra:structure:monoid> ;
  owl:disjointWith <…group model class> .                # D25 homonym/distinction tooth
```
This is the closure.ttl `datatype:record` idiom (cardinality-1 restrictions + specimen parent) applied
to a tower class the reference leaves an empty stub. It is the fix for the D23 extensional flaw
(`basicttl/foundation/*.ttl` has **0** `owl:Restriction`; closure.ttl has 13).

**(c) Foundation axiom records (minimal, no denotatum/gate/provenance).** VERBATIM the group-axiom rank
values with `family:group`→`family:monoid`; carry NO `@rel:certificate` (axiom≠theorem is structural).
```
<@Am:kingdom:axiom:phylum:operation:class:closure:order:binary:family:monoid:genus:product:species:membership:component:statement:instance:canonical>
  a owl:NamedIndividual, <@typ:axiom> ;
  <@rel:notation> "monoid closure" ;
  <@rel:equation> <…closure equation> ;
  rdfs:comment "S is closed under · . Checked exhaustively; not inferred from a label." .
# assoc: class:associativity:…:genus:composition:species:equality
# identity: split into identity-left + identity-right (§1.6)
```

**(d) Equation records (reified left=right; two-sided → TWO equations).** This is EXACTLY closure.ttl
`category:identity` (case:zero + case:one, two members, `closure.ttl:185-192`).
```
<@Am:kingdom:law:phylum:operation:class:identity:order:binary:family:monoid:genus:neutral:species:member:component:equation:instance:canonical>   [S: kingdom:law + component:equation — §7 vs reuse axiom atom]
  a owl:NamedIndividual, <@typ:equation> ;
  <@rel:member> <…:case:zero>, <…:case:one> .
<…:case:zero> <@rel:left> <…term e·x> ; <@rel:right> <…term x> .   # LEFT unit e·x = x
<…:case:one>  <@rel:left> <…term x·e> ; <@rel:right> <…term x> .   # RIGHT unit x·e = x
```
Associativity = ONE equation (single member, `closure.ttl:180-183`). Terms are reified application
records (`@rel:operand:one`/`@rel:operand:zero`/`@rel:constructor`, mapping closure.ttl `ns2:one`/
`ns2:zero`/`ns3:constructor`).

**(e) Element + finite-table witnesses → DEMOTED to `fixtures/`** (D24 four-planes; witnesses are
EVIDENCE, outside the ontology module AND the CI data glob). `fixtures/monoid_z2.ttl` = Z/2 under +,
positive; `fixtures/monoid_z2_negative.ttl` = a broken identity row so the tooth bites. Element records
`a <@typ:finite:element>`; reified composition cells `a <@typ:finite:composition>` with
`@rel:category:first`/`@rel:category:second`/`@rel:category:result` (the executable table the (c)
axioms bite on). REQUIRED: a positive AND a materialized failing negative per shape.

**(f) Theorem + Certificate (digest + proof-method, NEVER an axiom).** VERBATIM the reference Yoneda
theorem/certificate pattern (`closure.ttl:129-142`).
```
<@Am:kingdom:theorem:phylum:algebra:class:identity:order:declarative:family:monoid:genus:uniqueness:species:member:component:statement:instance:canonical>
  a owl:NamedIndividual, <@typ:theorem> ;
  <@rel:certificate> <…certificate:monoid:identity:uniqueness> ;
  <@rel:notation> "monoid identity uniqueness" ;
  rdfs:comment "Theorem, not an additional foundational axiom." .
<…certificate…> a owl:NamedIndividual, <@typ:certificate> ;
  <@rel:digest:value> "<sha256>" ;
  <@rel:proof:method> "Explicit general mathematical derivation; not proof-assistant checked" ;
  <@rel:source:location> "docs/…" .
```

**(g) Triad envelope (per first-class denotatum: theory, model) + provenance quartet.** Plane-1
DeclarationRecord (`@typ:declaration`) → `@rel:denotatum` Plane-2 Denotatum (the denoted mathematical
object; carries identifier/notation/source:url, **no provenance**) → `@rel:assignment` Plane-3 Gate
(`@typ:gate`; `@rel:check:status` "declaration reconciled; not a generic semantic proof";
`@rel:interpreted:by` <…interpretation…>). Provenance quartet
(`created`/`modified`/`version`/`state`) + `@rel:authority` + `@rel:ground` on every RECORD, never on
the denotatum ("Group was not authored by an executor; the GroupTermRecord was").

**Intensional record CLASSES (the OWL the consolidated stubs lack).** Mint `<…seed:species:theory:
record> a owl:Class ; rdfs:subClassOf [owl:Restriction; owl:cardinality 1; owl:onProperty
<@rel:signature>], [owl:Restriction; owl:minCardinality 1; owl:onProperty <@rel:equation>],
<…specimen:record>`. Equation record class = cardinality-1 on `<@rel:left>` AND `<@rel:right>`
(`closure.ttl:153-169`). `axiom:record owl:disjointWith theorem:record` (`closure.ttl:431-433`).

**MONOID rung assembly (the complete atom set).** 1 theory record + 1 signature record (sigMonoid,
`@rel:operation:symbol "· : S,S→S"`, `"e : →S"`, mirrors `algebra_spine.ttl:187-193`) + 3 axiom
records (closure/assoc/identity, identity → 2 cases) + 3 equation records (identity = 2) + 1 model
class (carrier + identity:element cardinality-1, `owl:disjointWith` group model) + 1 reduct edge
(monoid→semigroup, obligation-count 3: adds `e` + 2-case identity) + 1 theorem + 1 certificate
(identity uniqueness) + `fixtures/monoid_z2.ttl` (positive) + `fixtures/monoid_z2_negative.ttl`
(broken identity row) + declaration triad envelope + provenance quartet + 3 bridges (§5) + 2 SHACL
shapes + the intensional record classes. **Same skeleton for the other 5 rungs by swapping
subdomain/family + the single added law** (`algebra_spine.ttl:103`, one-law-per-child).

---

## 3. Agnostic-progenitor-as-theory-root · one-law=one-obligation · two-sided=2-equations

**Agnostic progenitor = theory root.** `fnd:AlgebraicStructure` folds to the §1.3 VERBATIM
`subdomain:primordial` root (ABSTRACT `true`, grounds nothing: no operation, no signature, no carrier,
no added law, and NOT a `PresentedAlgebra`). In the stratified idiom it becomes the **theory root** the
tower descends from: magma `rdfs:subClassOf` the progenitor model class; every other rung reaches the
progenitor transitively via reduct edges. The `AlgebraProgenitorShape` "grounds nothing" tooth
(`algebra_spine.ttl:411`, constraint A) re-homes as a SHACL clause: the progenitor carrying any
`@rel:signature`/`@rel:addsLaw`/`@rel:carrier` → RED.

**One law = one obligation.** Each concrete rung adds EXACTLY ONE law over its parent
(`algebra_spine.ttl:99-103`, constraints B no-cram + C at-least-one). Made a graph fact via the reduct
edge's obligation count: semigroup→magma adds 1 (associativity), monoid→semigroup adds 1 (identity, but
that identity **discharges 2 equation obligations**), group→monoid adds 1 (inverse → 2 obligations).
The ProgenitorShape's <=1 upper bound and >=1 lower bound both survive as intensional theory-law probes
+ fixtures (no regression, D25 "re-homed BOTH as intensional records AND probes+fixtures").

**Two-sided = 2 equations + obligation-counting morphism.** Identity (`e·x=x` AND `x·e=x`) and inverse
(`x·inv(x)=e` AND `inv(x)·x=e`) each mint TWO equation records (§1.6, §2d) — the reference's own
realized precedent (`closure.ttl:185-192`, `category:identity` case:zero + case:one). The reduct edge
carries an obligation-counting extension morphism (`count:two`) so a rung that declares only ONE side
is RED. Associativity, closure, commutativity, latin-division stay ONE equation each.

---

## 4. Fixtures · gates V0–V8 · CI lockstep · commit-signing

**Fixtures (non-vacuity, D24 four-planes).** Per shape: exactly 1 positive graph
(`conforms=true, results=0`) + 1 **failing** negative graph (`conforms=false, results≥1`) injecting a
single violation of that shape's tooth onto an otherwise-conformant graph — mirroring
`refcomp/zip/silmaril/reports/independent/` (positive.ttl + negative.01..28.ttl; `validation.log`).
Plus ONE `empty.ttl` vacuity control asserting `empty ⇒ admission=REJECT` (`validation.log:34`). The
reified engine Cayley tables become `finite:checked` certificate fixtures (Z/2, Z/3 tables carrying
proof-status `finite:checked` + validation-mode `finite:table`); the matching negative is a
non-total/associativity-violating table.

**Gates V0–V8** (mapped onto the reference's realized gate model; no literal "V0..V8" string exists in
the reference — recognise under its vocabulary, `R4_docs_doctrine_gates.md`):
- **V0** syntax = Turtle parse.
- **V1** OWL-profile + hygiene = no punning (FIX `algebra/product/frame.ttl:7` `a ontology:Class,
  model:Product, model:Frame` class-punning), no class as a provenance participant.
- **V2** SHACL non-vacuous = `empty ⇒ REJECT` + a 0-focus shape is **unexercised (REJECT)**, not
  passing.
- **V3** categorical probes = `sh:sparql`/`sh:select` clauses.
- **V4** Yoneda-density fixtures (fan-out).
- **V5** algebraic-law probes = every model names theory + carrier + operations + laws + a declared
  law-witness MODE.
- **V6** manifest coverage `N_manifest = N_materialized` (recomputed from disk, never hard-coded).
- **V7** provenance closure `executor ≥1 AND shadow ≥1` — **GAP: must be BUILT** (reference
  `governance/` is empty; only one-sided PROV exists).
- **V8** SHACL-2017 discipline.

Gates are modelled AS `owl:Class` under the reference gate ladder
`urn:silmaril:type:graph:instance:instruction:code:property:core:entity:structure:class:gate:
specification` (VERBATIM `consolidated.shacl.ttl:1324`), with the gate-identity uniqueness `sh:select`
tooth (`:1317-1327`) + clause-identity twin (`:1301-1311`). **Two-ladder ruling:** algebra rungs mint
the *mathematics* 12-marker ladder; gate/clause specs mint the *core:entity* gate ladder — both
verbatim from the reference (§7).

**SHACL pair per class (the tooth shape).** Every rung/theory/model gets a NodeShape with
`sh:targetClass` (**NEVER `sh:targetNode`** — reference: 33 targetClass / 0 targetNode; the existing
primordial `ByteWidthShape`/`OctetOrdinalShape` at `shapes.ttl:169-177` use targetNode and are the
anti-pattern the algebra subtree must NOT copy) carrying (i) property shapes min1/max1 coordinate
separation (like `ClassDeclarationShape`, `shapes.ttl:11-17`) and (ii) a `sh:sparql` non-vacuity +
identity-collision probe (`IdentitySeparationShape` idiom, `shapes.ttl:276-282`). Required spine
shapes each with a fixture pair: TheoryShape (names S/Ω/E), ModelShape, ReductShape, EquationRecordShape
(two-sided = 2 records), CarrierGroundingShape, ProofStatusShape (8-value), ValidationModeShape
(4-value), ProvenanceShape, BridgeShape, DifferentFromWitnessShape. Theorem/axiom collapse = a SHACL
violation.

**CI lockstep (the vacuity trap — highest risk).** The committed
`basicttl/foundation/checks/run-foundation-checks.sh` globs ONLY `basicttl/foundation/*.ttl` (line 76);
`ci.yml:13-27` drives it; `basicttl/primordial/type/**` is in NO runner. PLAN:
1. Author `basicttl/primordial/type/algebra/checks/run-algebra-checks.sh` that (a) auto-discovers
   `basicttl/primordial/type/algebra/**/*.ttl` (except `*.shapes.ttl`) as the data graph and validates
   it against the algebra shapes graph with pyshacl; (b) **explicitly iterates `fixtures/`** — asserts
   every positive conforms, every negative does NOT conform (else RED), and the empty control REJECTs —
   so witnesses outside the data glob cannot go silent; (c) **FAILs any declared shape with zero focus
   nodes** (invert `run-foundation-checks.sh:90-102`'s skip-when-no-shapes logic: 0-focus =
   unexercised, not passing); (d) recomputes every algebra count from disk and asserts
   `== manifest N_manifest` (V6).
2. Extend `ci.yml`: add the runner as a step in `ontology-floors` (or a sibling job gated identically),
   keep the ≥200-char `rdfs:comment` depth gate (`run-foundation-checks.sh:148-149`) over the folded
   algebra classes.
3. Adopt the reference's derived-count self-checks (`run-foundation-checks.sh:163-367`,
   disk==register==DAG==README) so figures are recomputed, never pinned.

**Commit-signing.** The provenance job (`ci.yml:109-119`, `fetch-depth:0`) walks full history and
classifies every commit against `commit_signing_trust.ttl`; an unsigned reshape commit goes RED.
Reshape commits sign under `silm:signing_key_claude_2026`
(fp `27044DC503CD3A5EE470CE4E15B79D364040C858`, `trust_policy_agent`) or Aster.
`keys/trust-manifest.txt` is GENERATED from the `.ttl` — the executor regenerates it; the planner
touches neither.

---

## 5. Engine/seed bridge map + the alias map (old `fnd:` → full-ladder IRIs)

### 5.1 Engine bridge map (`R3_engine_algebra_skills.md`, TODO-11 bridge-never-duplicate)

| fnd: class | engine anchor | relation |
|---|---|---|
| AlgebraicStructure | engine TYPE/ALGEBRA root (`primordials.yaml:394-404`) | `seed:conservativeBridge` |
| Group | engine GROUP type atom (§1.4 `[V]` IRI) | `skos:exactMatch` (SealedGroup→Group teeth-proven) |
| Magma | engine GROUP **closure** axiom atom | `seed:conservativeBridge` |
| Semigroup | engine GROUP **associativity** axiom atom | `seed:conservativeBridge` |
| Monoid | engine GROUP **identity** axiom atom (→ TWO equation records) | `seed:conservativeBridge` |
| CommutativeMonoid / AbelianGroup / Quasigroup / Loop | **NO engine anchor** | honest-red BUILD; proof-status `asserted`/`literature:backed`, NOT `finite:checked`-from-engine |
| carriers (Bit/Octet/ByteVector) | engine TYPE/CARRIER/{BIT,OCTET} | `seed:implementationBridge` |

`Byte ≠ Octet` = `owl:differentFrom` witness (engine OCTET WIDTH AXIOM `primordials.yaml:341-346`
"octet has exactly eight bit width while Byte remains width independent"; reference witnesses
`consolidated.ttl:35968,37810`) + a forbidding tooth + a negative fixture. Ring/Field/Module/Vector
homonym-vs-carrier collisions = BUILD + `owl:differentFrom` guard (fan-out, must ADD).

### 5.2 Alias map (retire `fnd:` local names → full-ladder IRIs; keep SP1/SP2/SP3 refs resolvable)

Each `fnd:` name gets a bridge triple `<full-ladder-IRI> skos:exactMatch fnd:X` (rungs, model classes)
or `rdfs:subClassOf`/`owl:equivalentProperty` as appropriate, plus a legacy `urn:silmaril:seed:…` edge
per the reference legacy-bridge idiom. The complete inventory (from
`basicttl/foundation/algebra_spine.ttl`):

- **Rungs / model classes:** `fnd:AlgebraicStructure`→§1.3 progenitor; `fnd:Magma`/`Semigroup`/`Monoid`/
  `CommutativeMonoid`/`Group`/`AbelianGroup`/`Quasigroup`/`Loop`→§1.4 model classes.
- **Signatures:** `fnd:sigOneBinary`/`sigMonoid`/`sigGroup`/`sigQuasigroup`/`sigLoop`→§1.7.
- **Equation-sets:** `fnd:eqsMagma`/`eqsSemigroup`/`eqsMonoid`/`eqsCommMonoid`/`eqsGroup`/`eqsAbelian`/
  `eqsQuasigroup`/`eqsLoop`→§1.9 equation-set objects.
- **Laws (equation records):** `fnd:lawClosure`/`lawAssociativity`/`lawIdentity`/`lawCommutativity`/
  `lawInverse`/`lawLatinDivision`→§1.5–1.6 axiom/equation atoms (identity & inverse → 2 records each).
- **Carriers:** `fnd:carrierMagma`…`carrierLoop`→carrier grounding atoms (`implementationBridge` to
  engine carriers + `groundsInSet` to the set-theory floor's `setMagma…setLoop`).
- **Reified-table vocabulary (SYN support):** `fnd:AlgebraElement`, `fnd:BinaryOperationApplication`,
  `fnd:opStructure`/`opLeft`/`opRight`/`opResult`, `fnd:InversePairing`/`pairingModel`/…,
  `fnd:hasIdentityElement`, `fnd:addsLaw`/`hasSignature`/`hasEquationSet`/`hasCarrier`/`satisfiesLaw`,
  `fnd:CategoryObject`/`Endomorphism`/`OneObjectCategory` → these are EVIDENCE-plane machinery: their
  witness instances DEMOTE to `fixtures/`; the predicates re-express as `@rel:*` with
  `owl:equivalentProperty`/`rdfs:subPropertyOf` bridges to closure.ttl `ns3:*` so the merged graph does
  not silently fork (§7 predicate-unification risk).

The short primordial root `urn:silmaril:primordial:type:` (used by `classes.ttl:1`, `shapes.ttl:1`) is
BRIDGED to via `schema:seeAlso`, never adopted as the IRI grammar (D26). The exhaustive per-name alias
table is a build deliverable; SP2 `aob:SealedGroup rdfs:subClassOf fnd:Group` and all inbound
`groundsIn*`/`subClassOf fnd:*` edges stay green because the merged SP0+SP1+SP2+SP3 graph re-validates
against `run-foundation-checks.sh:80-84`.

---

## 6. Spine coverage vs fan-out vs deferred

**SPINE (Pass 1, this design — the maintainer-sign-off template).** The one-operation tower:
magma → semigroup → monoid → commutative-monoid → group → abelian-group, plus the division sub-family
quasigroup → loop, plus the agnostic progenitor theory-root. All eight rungs materialised end-to-end
in the D24 stratified idiom (theory / model / signature / operation-symbols / equations / reducts /
proof-status / validation-mode / provenance / bridges / fixtures / shapes / manifests), CI runner +
`ci.yml` extended in lockstep. Monoid is the fully-worked exemplar (§2).

**FAN-OUT (Pass 2+, after sign-off — same template, NOT this design).** rings / fields / modules /
vector-spaces (two-operation line, homonym collisions renormalised with `owl:differentFrom` +
forbidding tooth + negative fixture each), set, spaces, functionality/typing, combinators, logic,
group-action, Blotto (SUB-lane under group-action: shared `theory:action:group`, own fixtures +
simplex≠group `owl:differentFrom` tooth), and the **D21 epistemology stratum (IN-SCOPE**, reshaped in
the fan-out, not deferred).

**DEFERRED (out of scope entirely).** The stale 29MB `ontology/silmaril-consolidated.ttl` render-seal
pipeline → W4/render-seal (D25). W4 render/seal packaging generally.

---

## 7. Non-goals + maintainer sign-off checkpoint

### 7.1 Non-goals

- No `.ttl`/`.sparql`/`.sh`/`.yml` authored, no ontology edited, no git run (planner mandate).
- No fan-out atoms minted (spine first; fan-out is Pass 2).
- No render-seal / consolidated-pipeline work.
- The IRI grammar, engine, primordial short root, seed, and SP2 `aob:SealedGroup` are **bridged to,
  never re-minted** (bridge-never-duplicate).

### 7.2 Sign-off checkpoint — LOCK these 8 token/scope decisions BEFORE the executor mints

The build is *re-mint-expensive* if any of these change after materialisation. Each must be ratified in
the design sign-off (the "realized spine" is reviewed after Pass 1; but these token choices should be
locked up front):

1. **Mint-more-than-runtime ruling** — confirm the build mints stratified theory/signature/operation/
   equation-set/reduct atoms that have NO algebra precedent in the runtime (per D24; the runtime shows
   only the flat `subdomain:group` collapse). *Pivotal.*
2. **Left/right side-segment placement** — `species:member:left` vs `class:identity:left` vs an
   order/component qualifier. Affects identity-left/right, inverse-left/right, loop-identity-left/right
   (6 atoms) + 2 obligation-extension morphisms.
3. **`order:nullary`** (unit symbol) — unattested; accept, or fall back to `order:constant`/`order:zero`.
4. **Reduct tokens** `order:forgetful` + `genus:theory` — unattested; accept, or use the attested
   `typed:record` declaration idiom.
5. **Quasigroup latin-division** `genus:latin` + `species:unique` — unattested; accept or reshape.
6. **Signature `genus:algebraic`** + **extension `genus:obligation`/`species:count:two`** — unattested;
   accept or reshape.
7. **Equation identity** — reuse the added-law axiom atom as the equation individual (`component:
   statement`, unattested `component:equation` avoided), OR mint separate `kingdom:law…component:
   equation` records.
8. **Two-ladder split** — algebra rungs on the *mathematics* 12-marker ladder, gate/clause specs on the
   *core:entity* gate ladder (both verbatim from the reference) — confirm per layer.

Plus two build obligations the plan flags but cannot discharge: **V7 provenance closure**
(executor≥1 AND shadow≥1) must be BUILT from scratch (reference `governance/` empty), and **the
predicate-unification bridge** (`@rel:*` ↔ closure.ttl `ns3:*`) must emit `owl:equivalentProperty`/
`rdfs:subPropertyOf` edges to avoid a silent fork.

### 7.3 Realized-spine acceptance (what "signed off" means)

Sign-off is on the *materialized* monoid rung + the seven sibling rungs passing V0–V8 non-vacuously:
every shape has ≥1 focus node; every negative fixture flips RED under injection; `empty ⇒ REJECT`;
`N_manifest == N_materialized` recomputed from disk; `aob:SealedGroup rdfs:subClassOf fnd:Group` still
resolves through the alias map; the provenance job green under a signed reshape commit. Only then does
the template fan out.
