# REFMAP shard R4 — docs / doctrine / gates

MAP-agent evidence (Praeriehund honesty: file:line + counts + quotes; opinions excluded).
Source of truth for this shard = the maintainer "FOR CLAUDIUS" consolidated drop, extracted at
`/tmp/claude-0/-home-user-silmaril/9319deb2-2eab-59fd-b601-de3e0fb18f37/scratchpad/refcomp/zip/silmaril/`
(hereafter `REF/`). Cross-checked against `ontology/consolidated.ttl` (78,692 lines) +
`ontology/consolidated.shacl.ttl` (1,434 lines). Governing law re-read: `design_constraints.md`
Directives 24 (Seed-Carrier) + 25 (fold into `basicttl/primordial/type/**`, spine-first).

Coverage attested: all shard-named files read IN FULL —
`docs/{baseline,grounding,parity,mathematics,gates,sources,sourcecounts,changes}.md`,
`docs/continuation/{ontology,capture,plan}.md`, `docs/research/anchor/map/{README,proofs,topology,economics}.md`,
`governance/` (EMPTY — see §5), `reports/independent/` + `reports/{structure,remaining,release,current,ontology,sources}.md`,
`evidence/{README,external/provenance}.md`, plus targeted greps of the two ontology graphs.

---

## 0. HEADLINE — the gate discrepancy the fold MUST reconcile (read first)

**The V0–V8 lettered gate names in Directive 24 do NOT appear anywhere in this consolidated
reference.** Grep of `REF/` for `V0`..`V8` / "gate V" = 0 hits. Directive 24's V0–V8 lettering
is sourced from the *seed-carrier spec* `docs/specs/2026-08-19-seed-carrier-rewrite-design.md`,
which lives in the OTHER corpus (`docs_anchor_map_consolidated_20260819.zip`, D24 authority stack)
and is **not** in this "FOR CLAUDIUS" drop. What THIS reference realizes instead is three parallel,
concretely-authored gate systems that the fold must MATCH:

1. **Ontology-modeled gates** — `gate:specification` OWL classes inside `consolidated.ttl`
   (internal / non-vacuous / complete / external / homotopy-engagement gate specs), each a
   prescriptive record kept plane-distinct from its evaluation-process and its clause-result
   evidence (§1.A).
2. **The 34-criterion acceptance table** — `docs/gates.md` + `docs/baseline.md` (§1.B).
3. **The executable Jena-SHACL harness** — `reports/independent/validation.log`:
   1 positive (conforms=true, 0 results) + 28 negative controls (each conforms=false) (§1.C).

These three MAP cleanly onto Directive 24's V0–V8 (§1.D). **No conflict with D24/D25 —
the reference is a faithful, more-concrete instance of the same doctrine.** But the fold cannot
grep for "V0..V8" in the reference; it must recognise them under the reference's own vocabulary.

---

## 1. VALIDATION GATES

### 1.A Gates modeled AS ontology records (`consolidated.ttl`)

The reference does not merely *run* gates — it models each gate as an `owl:Class` under a
`gate:specification` root, with the Seed-Carrier four-plane split baked in. Named gate classes
found (grep `gate:specification`, consolidated.ttl):

| Gate class (dcterms:identifier / URN local) | line |
|---|---|
| `internal:gate:specification` | 34022 |
| `non:vacuous:gate:specification` | 34373 |
| `complete:gate:specification` | 63375 |
| `homotopy:engagement:gate:specification` | 63585 |
| `external:gate:specification` | 69415 |
| `gate:specification` (root) | 70846 |

The **external gate** carries the doctrine's plane-non-collapse verbatim (consolidated.ttl:69411-69423):
> `ns806:elucidation "The external gate is a prescriptive information entity. Its evaluation is a
> BFO process. Its clause results are evidence records. These categories are not collapsed."`

The **root gate** class (70846-70858):
> `rdfs:label "finding record"` … `ns807:status "Gate specifications prescribe acceptance conditions."`
and gate specs carry `dcterms:source "docs/plan/sections/section_0N.md; sdd/stage/secNN/section_0N.append.ttl"`
(the executor build-plan lane — the `sdd/stage/` + `docs/plan/sections/` layout is the realized
executor discipline; those section files are NOT in this drop).

**Gate uniqueness is a biting SHACL tooth**, not prose (consolidated.shacl.ttl, via consolidated.ttl:75335-75345):
> `sh:message "gateIdentifier must identify at most one GateSpecification in the validation graph."`
> — a `sh:select` that returns a row (violation) whenever two `gate:specification` subclasses share
> a `gate:identifier`. This is the "one gate = one identity" enforcement.

Supporting gate-clause machinery (grep, consolidated.ttl): `gate:clause:coverage:shape`,
`gate:clause:specification:clause:identifier:key:shape`, `gate:clause:control:canonical` (×2),
`gate:clause:query:canonical` (×2), `gate:clause:refutation:canonical` (×2), `gate:clause:shape:canonical` (×2),
`external:gate:evaluation:process` (×2), `external:gate:assessment`, `external:gate:frame`,
`external:gate:inference:process`. So each gate = {specification record, clause specs, canonical
control/query/refutation/shape, evaluation process, assessment/frame}. This is a much richer gate
model than the flat V0–V8 list — the fold's gate layer SHOULD lift this clause/control/refutation
decomposition.

### 1.B The 34-criterion acceptance table (`docs/gates.md`, `docs/baseline.md`)

`docs/gates.md` is a 34-row acceptance matrix (Criterion | Requirement | assessment). Its
governing honesty stance (gates.md:1-3):
> "This revision repairs and verifies the executable profile. It does not convert passing fixture
> checks into a universal 34-gate corpus seal. Each remaining limitation is stated below."

`docs/baseline.md` (the *prior* revision's assessment, explicitly superseded) states the release
decision verbatim (baseline.md:9-14):
> "**Executable profile: tested. Whole-corpus acceptance: not sealed.**" … "A passing finite-model
> check does not discharge all 34 corpus requirements." … Legend: **Local / Partial / Blocked /
> Delivery / Documented / Modeled** severity vocabulary.

Selected criteria load-bearing for the algebra fold (gates.md):
- C1 "Pair carrier for every law family" — "Local runtime implemented; every historical law family
  has not been converted." (gates.md:… row 1)
- C7 "Exact ontology grounding everywhere" — "Pinned snapshot/version/import and named-chain checks
  … Full upstream provenance and universal local-class grounding not established."
- C11 "Full evidence on every rank edge" — "Not globally satisfied. No claim that generated labels
  prove semantic narrowing."
- C26 "Hashes are evidence only" — digest kept distinct from semantic identity & physical path.
- C34 "No unapproved Git write" — "No Git or remote repository mutation performed."

`docs/baseline.md` also carries an **error registry gate** (baseline.md:54-67): 23 required leaf
coordinates, current registry = 48; families GROUNDING / RANK / RESOURCE / PATH / PROTOCOL /
PROJECTION; verbatim: *"Registration is not emission coverage. Naming an error cannot serve as
evidence that the corresponding failure is detected."*

### 1.C The executable Jena-SHACL harness (`reports/independent/validation.log`)

The concrete pass/fail seal (validation.log:1-5, 34-35):
> `Apache Jena 5.6.0 independent SHACL validation`
> `positive conforms=true results=0`
> 28 lines `negative …:case:N conforms=false results=1` (case:28 = results=2)
> `empty native SHACL conforms=true; release coverage admission=REJECT`
> `negative cases=28 combined test gate=true`

Files present: `reports/independent/` = `positive.ttl` + `empty.ttl` + `negative.01..28.ttl`
(28 negatives, each ~485 KB) + `validation.log`. **This is the "1 positive + failing negatives"
fixture discipline D24 mandates**, run under a *named external validator with pinned input SHA-256s*
(validation.log:2-4 embeds the three input hashes). Note `empty conforms=true ⇒ admission=REJECT`:
an empty graph vacuously conforming is explicitly NOT accepted — the **non-vacuity gate realized**.

### 1.D Mapping the reference gates → Directive 24 V0–V8 (the fold's crosswalk)

| D24 gate | D24 meaning | Reference realization (this drop) |
|---|---|---|
| **V0 syntax** | parses | Turtle profile parse; `changes.md` "Syntax, UTF-8 and reference failures restore the previous graph" |
| **V1 OWL-profile + hygiene (no punning, class≠prov-participant)** | | `reports/structure.md`: "Property-kind/assertion or explicit class/individual overlaps: **0**"; `release.md`: "no object-property/literal … conflicting logical property-kind declaration or explicit named-class/named-individual overlap." Profile string on every record: `"OWL 2 DL with SHACL validation"` |
| **V2 SHACL non-vacuous** | shapes bite | `non:vacuous:gate:specification` class (ttl:34373); `empty conforms=true ⇒ admission=REJECT` (validation.log:34); structure.md reports 0-focus shapes as **unexercised**, not passing |
| **V3 categorical probes** | | 65 `sh:sparql`/`sh:select` probe clauses in consolidated.shacl.ttl; `gate:clause:query/refutation/control:canonical` |
| **V4 Yoneda-density fixtures** | | `homotopy:engagement:gate:specification` (ttl:63585); `seed:algebra:foundation:theorem:yoneda`, `:yoneda:full:faithfulness`, `:density` records; `docs/mathematics.md §4-5` supplies the proofs; finite fixtures in `tests/` (referenced, not in drop) |
| **V5 algebraic-law probes (model names theory+carrier+ops+laws; law-witness mode)** | | `seed:algebra:foundation:{carrier,category,model,olog}:seed`, six `foundation:axiom:*` (§3.B), `algebra:theory:rewrite` = law-witness MODE (ttl:1484) |
| **V6 manifest coverage (N_manifest = N_materialized)** | | `complete:gate:specification` (ttl:63375); `mandate:completeness:shape`; `docs/sourcecounts.md` counts derived from the 3 archive manifests (§2) |
| **V7 provenance closure (executor ≥1 AND shadow ≥1)** | | PROV-O on records: `prov:wasAttributedTo` ×1352, `prov:wasGeneratedBy` ×990, `prov:wasDerivedFrom` ×428 (§5); `external:gate:evaluation:process`; but the executor/shadow *dual* review is NOT realized in THIS drop (§5 — governance/ is empty) |
| **V8 SHACL-2017 discipline** | | profile string `"OWL 2 DL with SHACL validation"`; Jena 5.6.0 standard validation report (validation.log:1) |

**Verdict:** every V0–V8 gate has a concrete counterpart here EXCEPT the V7 *dual executor+shadow*
provenance-closure gate, which is realized only as one-sided PROV attribution (attributed-to/
generated-by), not the reviews/{executor,shadow} lifecycle. Flag for the fold: §5.

---

## 2. SOURCE-COUNTING / MANIFEST DISCIPLINE

`docs/sourcecounts.md` (whole file) — counts are archive-manifest-derived with pinned SHA-256:
> `silmarilbashdag.zip: 14 files, 127 function occurrences, 43806 bytes. SHA-256 a360b59e…`
> `silmaril-type-dag-engine-final.zip: 4043 files, 148 function occurrences, 17929104 bytes. SHA-256 c245de99…`
> `silmaril-type-dag-engine-final-2026-08-16.zip: 19866 files, 86 function occurrences, 19877293 bytes. SHA-256 9cb4a0a7…`

`docs/parity.md:3` derives the aggregate FROM these manifests and refuses to over-claim:
> "The three immutable source archives and their **361 function occurrences** remain inventoried in
> `registry/reconciliation.yaml` and `docs/sourcecounts.md`. An occurrence inventory does not imply
> behavioral equivalence." (127+148+86 = 361 — the count is arithmetic over the manifests, not asserted.)

`docs/continuation/capture.md:38`: *"The source catalog suite checks equality with every sealed
source registration, **not only a hard-coded count**."* — this is D24's "counts DERIVED from
manifests, never hard-coded" realized as an executable equality test.

`reports/structure.md` = the graph census: *"Triples: 66264. Named OWL classes: 2688. Ontology
headers: 1. … Strict named-subclass DAG: True. Longest asserted named path: 46 edges."*
`reports/release.md:13` cross-checks: *"66264 triples, 2688 named classes, 157 equivalent-class
axioms, 2923 subclass axioms, 20 key axioms, 52 node shapes and one ontology header."* Every count
is re-measured and reported, not stated.

`docs/sources.md` = provenance ledger for external inputs (observation date 2026-09-04), verbatim:
> "URLs are evidence locators, not canonical Silmaril semantic identities." Pinned specs: OWL 2
> Direct Semantics, XSD 1.1 Pt1/Pt2, RFC 8141/3986/8089, GNU Bash, BFO 2020 (byte-pinned IRI),
> Spivak-Kent Ologs arXiv:1102.1889, Curry (via mathematics). Legacy seed
> `anchor_map_full_consolidated.ttl` = 10,044,752 bytes, "remains unchanged as external evidence."

**Manifest coverage as a gate**: `reports/structure.md` "SHACL target coverage" table lists all
**52 node shapes** with observed focus-node counts (e.g. `class:annotation:shape` 1105,
`specification:identifier:shape` 758, `engagement:cell:shape` 5, many `0`); 0-count shapes are
declared *unexercised*, not passing — the N_manifest vs N_materialized reconciliation is literally
this table. `release.md:15`: *"Forty-three shapes have production or explicitly labeled synthetic
focus nodes; nine source shapes remain unexercised on the production graph."*

---

## 3. DOCTRINE REFINEMENTS / NEW RULES beyond Directives 24/25

None of the following OVERRIDE D24/D25; they REFINE and, in one place (§3.D algebra tower shape),
give a concrete authored template that the fold should MATCH rather than reinvent.

### 3.A Grounding stays relation-plural (`docs/grounding.md`)
grounding.md:3 (verbatim): *"Ontology grounding, programming inheritance, taxonomy, realization,
denotation and location remain different relations. A successful C3 order is not an ontology-grounding
proof."* External projection is byte-pinned: `ontology/external/imports.ttl` = 14,690 triples from
`evidence/external/source.ttl` (27,507 triples), projection SHA `601d8e1f…`, source SHA `cea9f1c3…`
(`evidence/external/provenance.md:3-7`). Pinned version IRIs (grounding.md:11-13): BFO
`obo/bfo/2020/bfo-core.ttl`, CCO `2024-11-06/CommonCoreOntologiesMerged`, CPO
`2025-04-25/CognitiveProcessOntology`. Rule: *"The .owl and .ttl identifiers are not silently
equated."* (grounding.md:16) — a byte/version-pinning refinement of D24's `external/` module.

### 3.B The algebra tower treatment — Lawvere theory/model/reduct realized as `seed:` records
This is the single most fold-relevant find. The reference already carries the D24 A6
theory/model/reduct stratification, as a **`urn:silmaril:seed:algebra:foundation:*`** vocabulary
(grep, consolidated.ttl):
- **Theory/model/carrier split**: `seed:algebra:foundation:{carrier,category,model,olog}:seed`,
  `seed:algebra:foundation:construction:{category:path:quotient, category:elements, coend:presentation,
  embedding:yoneda}`, `seed:algebra:foundation:theorem:{yoneda, yoneda:full:faithfulness, density}`.
- **Six foundation axioms** (matches `mathematics.md §2` + `proofs.md`): `seed:algebra:foundation:axiom:
  {category:identity, category:associativity, functor:identity, functor:composition, naturality,
  sketch:equation:satisfaction}`.
- **Categorical predicates** (the D24 exemplar envelope): `seed:algebra:{interpreted:by, modeled:within,
  presented:by, has:certificate, depends:on, domain, codomain, constructed:from, formal:characterization}`.
- **`algebra:theory:rewrite`** (ttl:1484) = validation MODE "rewrite" realized;
  `algebra:structure:...:record:post:schema:validation` = the post-validation record plane.

`docs/mathematics.md` is the algebra-tower monograph. Load-bearing rulings the fold must honor:
- §1 (math.md:5-15): `Pair = Key × Value`; `B = S×(K×V)×C×P×E`; assertion projection
  `(s,(k,v),c,p,e) ↦ (s,k,v)` is a **projection, not equality** — D24's four-plane forget map.
  *"Keys denote typed relation positions. A general relation must be represented by a span S ← E → V;
  it cannot be silently used as a single-valued function S → V."* (math.md:15)
- §2-3: `C_seed = Path(G_seed)/≡` and `SeedCarrier = ∫ M_seed` (category of elements) —
  *"a category over C, not an untyped union of payload strings."* (math.md:41)
- §4 (math.md:43-58): **"Yoneda is a theorem"** — Φ/Ψ inverse bijection proven, *"No seventh axiom
  has been inserted."* Directly enforces D24 "Yoneda is a theorem record with a certificate, never
  an axiom." The `proofs.md` twin gives variance discipline: *"These two variance conventions must
  not be mixed."* (proofs.md:37).
- §6 (math.md:87-95): group = one-object category with two-sided inverses; *"Commutativity is a
  separate check; it is not inherited from being a group."* — the abelian rung is a distinct law.
- §7 (math.md:97-102): **M-style corrections** — Church left-fold vs right-fold step type
  `Accumulator→Element→Accumulator`; *"A finite cyclic set with its discrete topology is not a
  circle and does not acquire the circle's first cohomology."*; *"Read and write are not inverses
  merely because directories are paired."* (These are the "M1-M8 corrections" the shard task names:
  fold-order, discrete-cycle≠circle, antipodal-only-for-even-n, mod-n quotient≠universal-cover,
  polar-cost≠measured-cost, Bash-mutation≠pure-lambda.)
- §8 (math.md:104-110): **ring-as-reducts / homonym separation** — *"An octet in the machine carrier,
  an unsigned-byte datatype value and an element of the modular ring are separately typed accounts."*
  Realized as the two `owl:differentFrom` witnesses (consolidated.ttl:35968 `…differentFrom ns2300:six`;
  37810 `…differentFrom ns2293:byte`) — exactly D24's "unsignedByte ≠ machine byte ≠ Z/256Z" idiom.

**The tower is materialized as a 46-edge intensional descent** (`reports/structure.md:71-118`,
maximum-depth witness), NOT the flat progenitor ladder of the lost fnd: floor:
`algebraic:structure → carrier:bearing → nonempty:carrier:bearing → operation:bearing → finitary →
single:operation → binary:operation → closed:binary:operation → magma → associative:magma →
semigroup → unital:semigroup → monoid → cancellative:monoid → invertible:monoid → group →
commutative:group → abelian:group → topological:abelian:group → … → standard:real:line:additive:group`.
Each rung is a `…:specification` `owl:Class` (e.g. ttl:34373 "invertible monoid specification",
`skos:definition "A cancellative monoid specification in which each carrier element has a two-sided
inverse."`, `dcterms:source "docs/plan/sections/section_03.md; sdd/stage/sec03/…"`). This is the
**intensional definition-by-differentia** D23 demanded and D24 systematized. Grep: 2,977 `a owl:Class`;
158 `owl:equivalentClass` (with witnesses); 2 `owl:differentFrom`; 65 `sh:sparql`/`sh:select` teeth;
33 `sh:targetClass`/`sh:targetNode`.

### 3.C Proof-status + validation-mode vocabulary realized
D24's 8-value proof-status is realized as typed individuals under a `proof` class with `seed:`
legacy bridges (consolidated.ttl:64678-64680):
> `ns2810:backed a ns2815:proof ; rdfs:label "literature-backed theorem status" ;
>  ns3457:legacy "urn:silmaril:seed:gate:proof:status:literature:backed" .`
Also `seed:gate:proof:status:specified` (ttl:72168) and prefix roots
`…:gate:proof:status:literature:` (ttl:2016), `…:gate:proof:status:` (ttl:2017),
`…:data:proof:status:` (ttl:3385). Value-vocabulary token counts in the graph: `asserted` 341,
`conditional` 34, `literature` 21, `Conditional` 6, `counterexample` 3, `rejected` 2. Validation
MODE realized: `algebra:theory:rewrite` (rewrite), `finite:cell:complex:validation:protocol`,
`shacl:validation:protocol`, `coherence:validation:process`, `confluence:validation`,
`official:aggregate:validation`, `service:validation:process` — the per-structure MODE declaration.

### 3.D The `seed:` bridge namespace = the D24 "bridge, never duplicate" idiom realized
The `legacy` predicate (`ns3457:legacy`) maps every reshaped record to a
`urn:silmaril:seed:…` legacy IRI — this IS D24 TODO-11's compat-bridge, and `seed:` is the
Seed-Carrier prefix. `seed:activity:anchor:map:consolidation` marks the provenance activity.
The fold into `basicttl/primordial/type/**` should carry this `seed:*` legacy-bridge pattern so
inbound `groundsIn*`/`subClassOf fnd:*` references stay resolvable (D25 alias-map requirement).

### 3.E Naming law realized (spec §10b)
All local names are lowercase colon-descent, genus-first: `class:invertible:monoid:specification`,
`gate:clause:coverage:shape`, `seed:algebra:foundation:construction:embedding:yoneda`. `structure.md`
confirms 0 punning overlaps. This is D24's naming law materialized — the fold's target grammar.

---

## 4. `docs/continuation/plan.md` — the intended build sequence

`plan.md` (whole file) IS a maintainer-specified next-steps plan, but scoped to the *runtime
repair*, not the algebra fold. Verbatim structure:
- Goal (plan.md:3): *"retain the repaired executor and close reproducible occurrence-identity and
  validation-coverage defects."*
- Architecture (plan.md:4): *"one Bash execution kernel, immutable input witnesses, distinct
  host-side ontology verification."*
- Global constraints (plan.md:9): *"Bash builtins only inside execution; no Git commit or push; no
  original-source modification; no digest as semantic identity; strict archive bound less than
  50000000 bytes; unavailable evidence cannot become an accepted gate."*
- Four tasks, ALL boxes `[x]` (done): T1 stable native capture; T2 nominal artifact identity
  (digest-key → `artifact:identifier` + SHACL uniqueness); T3 shape coverage + logical boundary
  (Jena over all target populations, labeled synthetic fixtures for absent targets); T4 delivery
  evidence. Remaining obligations deferred to `remaining.md`.

`reports/remaining.md` = the open-obligation ledger (6 rows): historical source editions,
semantically-valid rank accounts (7961 predecessor AOB files, 5646 repeat-taxon), universal KV/AOB
closure, complete predecessor behavior, full OWL reasoning, external seven-protocol build — verbatim
*"The central whole-corpus admission decision is WITHHELD."* (remaining.md:14).

`docs/continuation/{ontology,capture}.md` detail the two shipped corrections:
- ontology.md: `InformationBearingArtifactEntity` re-keyed by `artifact:identifier` not
  `artifact:digest`; controlled-zero SPARQL now `FILTER(?count = 0)`; blank-node RDF-list sharing
  serializer repair; *"The independent shape exercise uses all 52 declared node shapes."* (ont.md:11).
- capture.md: `kv::capture SOURCE OBSERVATION PIN` with independent SHA-256 pin; *"Do not obtain the
  expected pin from an untrusted receipt under test. The pin is content evidence, not an artifact
  identity or a signature."* (capture.md:22) — the D21 no-self-cert boundary realized in the runtime.

**Fold-relevant caveat:** plan.md's *"no Git commit or push"* and *"Bash builtins only"* are the
RUNTIME successor's self-imposed constraints; they do **NOT** bind the reshape (D25 §CI-lockstep
explicitly requires the fold to extend `ci.yml` + sign commits under `commit_signing_trust.ttl`).
Do not import plan.md's no-Git rule into the fold — it is scoped to the delivered Bash package.

---

## 5. GOVERNANCE + INDEPENDENT-REPORTS: executor/shadow/review + provenance realized

**`REF/governance/` is EMPTY** (`ls governance/` → only `.`/`..`). The executor/shadow/resolved
review-lane directory tree D24 mandates (`reviews/{executor,shadow,resolved}/`, `receipts/`) is
**NOT present in this drop**. This is the single biggest doctrine element the reference does NOT
realize. Flag for the fold: the executor+shadow dual-review lifecycle (D24 gates V7 + lane lifecycle
Draft→ExecutorValidation→ShadowCritique→Resolution→ShadowRevalidation→Accepted) must be built by the
fold; it cannot be lifted from here.

**What IS realized (one-sided, PROV-O):**
- `reports/independent/` = the *independent-validator* leg: Jena 5.6.0 (external tool) run with
  pinned input hashes, 1 positive + 28 negatives (§1.C). This is the "independent revalidation"
  half — a shadow-style adversarial check — but authored as an external tool run, not a named
  shadow agent's review record.
- PROV-O attribution is dense on RECORDS (grep consolidated.ttl): `prov:wasAttributedTo` ×1352,
  `prov:wasGeneratedBy` ×990, `prov:wasDerivedFrom` ×428, plus `prov:Activity`, `prov:startedAtTime`,
  `prov:wasAssociatedWith` ×1 each. This satisfies D24 "provenance on every RECORD, never on
  mathematical denotata" — but it is attribution-only; there is no dual executor≥1 AND shadow≥1
  *count* enforced.
- `docs/parity.md:20-26` records the executor DECISION discipline: *"The absolute no-external
  execution rule conflicts with historical instructions to launch Java, curl or external filesystem
  utilities. This revision resolves the execution choice in favor of the user's active
  prohibition."* + *"No remote repository mutation was performed. This is a downloadable local
  successor, not a claimed commit."* — the honest-conflict-resolution stance, not a review lane.
- `reports/release.md` = the executor's delivery attestation: *"Thirty suites completed with 246
  passing named cases and zero failures. Seven new implementations bring the sealed source-view
  census to 267."* + *"No whole-corpus acceptance seal is issued, and no Git commit or push
  occurred."* (release.md:5, 27).

---

## 6. GATE + DOCTRINE LEDGER THE FOLD MUST HONOR (synthesis)

Ordered by fold-actionability. Nothing here overrides D24/D25; the two override-flags are called out.

1. **Recognise gates under the reference's vocabulary, not "V0–V8".** V-lettering is absent here;
   map via §1.D. Lift the richer gate model: `gate:specification` classes +
   `gate:clause:{coverage,control,query,refutation,shape}` + `external:gate:evaluation:process`,
   with the plane-non-collapse elucidation (ttl:69411) and the gate-identity uniqueness `sh:select`
   tooth (ttl:75335).
2. **The algebra tower already has a doctrine-conformant template — MATCH it.** The 46-edge
   intensional `…:specification` descent (structure.md:71-118) + `seed:algebra:foundation:*`
   theory/model/carrier/olog/construction/theorem/axiom records + the six foundation axioms +
   `interpreted:by`/`modeled:within`/`presented:by`/`has:certificate`/`depends:on` predicates ARE
   the D24-A6 Lawvere stratification realized. The spine-first Pass-1 (D25) should reproduce THIS,
   not the retired flat-progenitor fnd: ladder.
3. **Proof-status + validation-mode are realized vocabularies** (`seed:gate:proof:status:*`;
   `algebra:theory:rewrite` etc.). Reuse the token set (`asserted / literature:backed / specified /
   conditional / counterexample / rejected`) rather than minting new.
4. **Homonym separation via `owl:differentFrom`** (ttl:35968, 37810) is the realized idiom for
   D25's Ring/Field/Module/Vector + byte/octet/Z256 collisions. Only 2 witnesses exist — the fold
   must ADD the Ring/Field/Module/Vector ones D25 names.
5. **Counts DERIVED, never hard-coded** (sourcecounts.md + parity.md:3 "not only a hard-coded count"
   + structure.md 52-shape coverage table). Fold manifests must recompute; 0-focus shapes = REJECT,
   empty-graph conformance = REJECT (validation.log:34).
6. **Fixture discipline = 1 positive + failing negatives, run by a named external validator with
   pinned input hashes** (reports/independent/, Jena 5.6.0). Match this shape for every reshaped shape.
7. **PROV-O on every record** is realized (1352/990/428). Keep it; ADD the missing half.
8. **`seed:*` legacy-bridge namespace** is the realized D24-TODO-11 / D25 alias-map mechanism —
   carry it into `basicttl/primordial/type/**` so inbound refs resolve.

### FLAGS — items the fold must SUPPLY (reference does NOT realize) or must NOT import
- **[GAP] Executor/shadow dual review lane** (`governance/` empty; no `reviews/{executor,shadow,
  resolved}/`, no `receipts/`). D24 V7 dual-count + lane lifecycle must be BUILT by the fold; only a
  one-sided independent-validator leg + attribution PROV exists here. (§5)
- **[GAP] V0–V8 lettered gate names** absent — they live in the seed-carrier spec zip, not this
  drop. The fold's gate identifiers should adopt D24's V-lettering AND bridge to the reference's
  `internal/non-vacuous/complete/external/homotopy-engagement` gate classes. (§0, §1.A)
- **[SCOPE, do NOT import] plan.md "no Git commit / Bash-builtins-only"** binds the delivered
  runtime successor ONLY; D25 §CI-lockstep REQUIRES the fold to extend `ci.yml` + sign commits under
  `commit_signing_trust.ttl`. Do not carry plan.md's no-Git constraint into the reshape. (§4)
- **[NOTE] `docs/gates.md` = 34 acceptance CRITERIA, a different axis** from D24 V0–V8 (V-gates =
  validation-pipeline stages; 34 criteria = corpus-completeness requirements). Both are honored;
  they are orthogonal. Neither overrides D24/D25.
- **[NOTE] `dcterms:source` on records points to `docs/plan/sections/section_0N.md` +
  `sdd/stage/secNN/…`** — the executor build-plan lane that produced the reference. Those section
  files are NOT in this drop; if the fold needs the per-section build order, it is in the
  seed-carrier corpus, not here.
