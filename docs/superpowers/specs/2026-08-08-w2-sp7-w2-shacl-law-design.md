# W2 · Sub-project 7 — the W2 SHACL coverage law (math fibre + federation gluing) — design

> **Batch design doc** (superpowers:brainstorming; batched SP2–SP9 per Directive 14 — one
> maintainer review pass for the eight, no per-project Socratic gate). Design-only: NO
> `.ttl`/`.sparql`/implementation authored here. **THIS ITERATION's v1** — corpus-agnostic,
> to be fundamentally challenged and relaunched later (Directive 13). Terminal step on batch
> approval → superpowers:writing-plans. **This re-author LIFTS the authored coverage law from
> Helios (Directive 1: lift, do not invent); it does not re-pick the cross-cutting decisions.**

**Grounding (gospel):** `docs/unary-byte-frame-law.md`, `docs/praeriehund-demokratie-der-kategorien.md`,
`ledger/W2/design_constraints.md` Directives 1–14, the **committed SP1 floor** `basicttl/primitives/*`,
and the **authored Helios source-of-truth** — the three coverage specs + `universal_anchors` under
`helios/01_data_src_specs/`, the `is?/1` validators under `helios/01_src_specs/`, srcy **Vol 24**
(`helios/srcy/papers/24_shacl_validation_and_path_constraints/`) and appendix **E** `specs/shapes/`
(`helios/srcy/appendices/39_E_research_source_mirror/`). SP7 authors **NO** new value classes — it is
the **executable coverage law over the federated W2 graph**, sitting *above* each sub-project's own
local shapes. **Boundary fix:** SP7 OWNS the federation depth-SHACL; SP8 is remediation-*local* and
**consumes** SP7's law as its target.

---

## 1. Goal

Author the **math-fibre coverage law** — the closed loop *families → predicates → shapes/queries, all
anchored to the 11 Layer-0 tensor spaces* — as executable SHACL + EXPECT-TRUE SPARQL, plus the
**federation gluing** that makes the six W2 graphs cohere as one global section over the shared SP1
floor. This is a direct lift of the authored Helios coverage specs. Six biting laws, each with SP1
teeth discipline (defang-proof `sh:sparql`, EXPECT-TRUE ASK mirror, probe-injection RED→GREEN,
non-vacuous):

1. **shape-coverage completeness** — every AOB atom-family (SP2 `aob:atomFamilyUrn`) is targeted by
   **exactly one** `sh:NodeShape`; every shape targets a real family. The **26 NodeShapes** (24 paper
   + 2 Wave-E primitives) of `shacl_shape_coverage.spec.yaml`, materialized.
2. **universal-anchor grounding** — every **node** atom carries exactly one `grounds_in_cco`
   (`cco:ontNNNNNNNN`, card **1..1**); every **arrow** atom exactly one `grounds_in_cceo`
   (`cceo:…`, card **1..1**). The `ConcreteAnchorShape` + `YonedaHomLegShape` load-bearing exemplars.
3. **pattern-from-anchor (no inlined regex)** — every `sh:pattern` resolves from a Layer-0
   `universal_anchor`'s `pattern:` field via `pattern_anchor_urn`; **no regex literal** is stored in
   any shape. `dispatcher_contract.no_hardcoded_patterns`, made a graph fact.
4. **predicate-catalogue** — every shape `sh:property` path is one of the **18** catalogued Layer-1
   predicate arrows (`ttl_predicate_coverage.spec.yaml`); CURIE/prefix is **computed** from the
   anchor pattern, never stored. `no_hardcoded_predicates`, made a graph fact.
5. **query-tree / math-fibre coherence** — **Q1..Q7** are typed Node/Arrow trees whose
   `triple_patterns` are structurally isomorphic to the `typed_hom_triple` (S/P/O) Arrow family; **no
   query_body heredoc, no SPARQL keyword as data**; the same tree projects to SHACL, TTL and SPARQL
   (the math-fibre coherence `pyshacl_validation_passes`). Q4/Q5 compute inverse-only atlas columns
   **at query time, never stored**.
6. **SHACL ⟷ `is?/1` colimit coherence + federation gluing + federation depth** — the declarative
   SHACL NodeShape and the executable Elixir `is?/1` validator are the two legs of the math-fibre
   colimit over one family and must agree; the six W2 graphs pushout-colimit over the shared SP1 floor
   (**semantic-ancestry** = the gluing axiom); and every `owl:Class` in the federated graph carries a
   `rdfs:comment` ≥ 200 chars (**SP7-owned** depth gate, SP8's target).

## 2. Architecture — the coverage law is the math fibre; the federation is a pushout colimit / sheaf

### 2.1 The closed loop is the math fibre of the triad fibration (lifted, not invented)

`triad_fibration.spec.yaml` groups the 7 render legs into 3 fibres; the **math fibre** is
`{ttl, shacl, sparql}` with `coherence_check: pyshacl_validation_passes`. SP7 IS the executable form
of that coherence check. The authored coverage specs already close the loop — **families →
predicates → shapes/queries** — all anchored to the **11 Layer-0 tensor spaces** of
`universal_anchors.spec.yaml`. SP7 lifts each edge of that loop into a biting shape:

```
 atom_family_registry (SP2 families)          universal_anchors  (11 Layer-0 anchors, Layer 0)
        │  aob:atomFamilyUrn                         │  pattern:  (^cco:ont[0-9]{8}$, ^cceo:…$, …)
        ▼                                            ▼
 ttl_predicate_coverage (18 Layer-1 arrows) ──bind──▶ (source family → target Layer-0 anchor)
        │  path_predicate_urn                        │  pattern_anchor_urn
        ▼                                            ▼
 shacl_shape_coverage (26 NodeShapes) ◀──isomorphic──▶ sparql_query_coverage (Q1..Q7 typed trees)
        │  one shape per family                      │  triple_patterns ≅ typed_hom_triple (S/P/O)
        └──────────────── the math-fibre coherence (pyshacl passes) ───────────────┘
```

Every arrow of this loop is a **graph edge SP7 checks with teeth** — completeness (families↔shapes
bijection), grounding (card 1..1 into the two grounding anchors), pattern-from-anchor (no inlined
regex), predicate-catalogue (path ∈ 18), query-tree isomorphism, and the SHACL⟷`is?/1` colimit. The
theory ancestor is **srcy Vol 24** (SHACL shapes + *path constraints*: a `sh:NodeShape`'s `sh:path`
is a typed navigable arrow, not a string) and **appendix E `specs/shapes/`** (the rendered `.tex`
mirror of exactly this shape system).

### 2.2 The 26 NodeShapes + universal-anchor grounding (lifted from `shacl_shape_coverage.spec.yaml`)

The two load-bearing exemplars are lifted verbatim in structure:

- **`ConcreteAnchorShape`** (node family `concrete_anchor`): `rdfs_label` (1..1) + `grounds_in_cco`
  **min 1 max 1** with `pattern_anchor_urn = …node:identifier:cco_grounding_iri`. That anchor's own
  `pattern: '^cco:ont[0-9]{8}$'` (in `universal_anchors.spec.yaml`) is the **only** place the regex
  lives — the shape references the anchor, never the literal.
- **`YonedaHomLegShape`** (arrow family `yoneda_hom_leg`): `grounds_in_cceo` **min 1 max 1**
  (`pattern_anchor_urn = …arrow:identifier:cpo_process_iri`, pattern `'^cceo:[A-Za-z0-9_]+$'`) +
  `source_node` (S) + `target_node` (O). This is the S/O/P Arrow made a SHACL law.

The other 24 (Description/Example/Acronym/AdditionalAttributes/Synonym/Antonym/Lemma/OlogBox/… + the
2 Wave-E primitives `FactoryCharterPreambleShape`/`PrimitiveAtomShape`) follow the same envelope. The
`grounds_in_cco`/`grounds_in_cceo` **card 1..1** IS the "universal_anchors is LOAD-BEARING" policy the
maps flag: *no node atom exists without exactly one CCO grounding IRI; no arrow atom without exactly
one CPO process IRI*, both resolving against `MergedAllCoreOntology.ttl` (CCO 2.x under BFO) via
`SIL_CCO_TTL_FILE`/`SIL_CPO_TTL_FILE`. Per the Directive-1 progenitor ethos and CCO/BFO load-bearing
decision: SP7 references the `cco:ont########` IRI and the `pattern_anchor_urn`; it **never** inlines
a regex and **never** re-picks the anchor set (that is `universal_anchors_proposed`,
`human_review_required`).

### 2.3 Q1..Q7 as typed Node/Arrow trees (lifted from `sparql_query_coverage.spec.yaml`)

Each query is a tree of `selected_variables` / `triple_patterns` / `filter_arrows` /
`aggregation_arrows` — **no `query_body:` heredoc, no SPARQL keyword as data**. A `triple_pattern`
`(subject_var, predicate_urn, object_var)` is **structurally isomorphic to the `typed_hom_triple`
Layer-1 Arrow** (S=subject_var, P=predicate_urn, O=object_var) — the same S/O/P carrier SP2 authors
and SP3 towers. The render macro `α*^{M_sparql}` walks the tree to surface SPARQL; the **same tree**
projects to SHACL (`α*^{M_shacl}`) and TTL (`α*^{M_ttl}`) — this triple-projection agreement IS the
math-fibre coherence. Q1 (anchors missing CCO) and Q2 (legs with unknown CPO) are the negative
coverage probes; **Q4/Q5 derive inverse-only atlas columns (Classifies / ValidValues / Replacement /
Translated / Preferred) at query time, `never stored`** (`derives_atlas_column_urn`); Q6/Q7 are the
Wave-E primitive-family additions reusing Q3's tree shape.

### 2.4 SHACL ⟷ `is?/1`: the math-fibre colimit (lifted from `helios/01_src_specs`)

`helios/01_src_specs/lib/silmaril/wave8/*.ex` renders **one typed struct per atom family** with a
total structural validator **`is?/1`** (pattern-match the struct, then `StringNode.is?`/`IntNode.is?`/
`BoolNode.is?` per field, list fields `is_list` + `Enum.all?` + `length ≤ max_size`, fallthrough
`false`) plus `checks/runner.ex` (URN-convention dispatcher, `System.halt(0|1)`). This is the
**executable counterpart** of the declarative SHACL NodeShape: same family, two legs. The math-fibre
colimit law (mirroring the bash⟷beam colimit corroboration of `00_src_specs`) is *SHACL verdict ==
`is?/1` verdict* for every family — SHACL is the `shacl` leg, `is?/1` the executable witness; a spec
that conforms to `YonedaHomLegShape` but fails `YonedaHomLeg.is?/1` (or vice-versa) is an incoherence
SP7 rejects. (Design captures the law; the `is?/1` legs are rendered elsewhere — SP7 checks agreement.)

### 2.5 The federation is a pushout colimit; SP7 is the gluing axiom

The six W2 data graphs SP1..SP6 do **not** union disjointly: each includes the SP1 floor **by
reference** (its carriers ground into `prim:` towers). So the **federated graph is a pushout colimit**
of SP1..SP6 *over the shared SP1 floor subobject* — the same colimit shape as SP1's twin-olog taiji,
one dimension up; the theory is srcy **Vol 19** (mereology as pushout/coequalizer colimit,
`colimit ≠ disjoint union`) glued by **Vol 25** (sheaf: local records glue iff restrictions agree on
overlaps).

```
        SP2 ─┐
        SP3 ─┤
        SP4 ─┼──(pushout over the shared SP1 floor)──▶  federated W2 graph  ◀── SP7 coverage law
        SP5 ─┤                                                 (global section)
        SP6 ─┘
              └────────── all include the SP1 prim: floor by reference ──────────┘
```

- A SHACL shapes graph is a **predicate over the graph**; `conforms` is a **global section**. Local
  conformance ≠ global conformance — the coverage law and semantic-ancestry live on the **overlaps**.
- **Semantic-ancestry = the descent/connectivity gluing axiom** (ontology form of the unary law's
  semantic-ancestry amendment): every W2 semantic carrier reaches, by `rdfs:subClassOf+`, a class the
  SP1 `prim:DualGroundingShape` already certifies dual-grounded. A class dangling at `owl:Thing` or on
  a generic-capability base is the ontology analogue of a direct-`Sorted.Value` shortcut — **rejected**,
  not repaired by a directory prefix.
- **Federation depth (SP7-owned):** every `owl:Class` in the federated graph carries a `rdfs:comment`
  ≥ 200 chars — authored federation-wide, **staged** to bite on the W2 graph first, then the whole
  tree once SP8 remediation lands. SP8 *consumes* this as its remediation target (§5).
- **Every asserted law has a biting tooth.** Each shape is a **defang-proof `sh:sparql` NodeShape**
  (genuine edges / `STRLEN` / count aggregates / `rdfs:subClassOf*` walks that `inference="rdfs"`
  range-inference cannot forge — the SP1 `EncodingShape`/`DualGroundingShape` idiom), mirrored by an
  EXPECT-TRUE ASK, proven to bite by a probe (§4), non-vacuous.

## 3. File layout (one concern per file — STRICTNESS Rule 14; `urn:` namespace)

Namespace `law: <urn:silmaril:law:#>` (full-lexical URN idiom, unary law). Directory `basicttl/law/`.
No value classes are authored (SP7 is pure law). The coverage law is split by concern, not one monolith.

| file | responsibility |
|------|----------------|
| `basicttl/law/shape_coverage.shapes.ttl` | **completeness**: families↔NodeShapes bijection (the 26 shapes each target one `aob:atomFamilyUrn`; no orphan family, no shape without a family) + the per-family shape envelope lifted from `shacl_shape_coverage.spec.yaml` |
| `basicttl/law/anchor_grounding.shapes.ttl` | **universal-anchor grounding**: `grounds_in_cco` card **1..1** on node families + `grounds_in_cceo` card **1..1** on arrow families (`ConcreteAnchorShape`/`YonedaHomLegShape`), each pattern via `pattern_anchor_urn` into the two Layer-0 grounding anchors |
| `basicttl/law/pattern_predicate.shapes.ttl` | **pattern-from-anchor** (no `sh:pattern` literal — every pattern traces to a `universal_anchor.pattern`) + **predicate-catalogue** (every `sh:path` ∈ the 18 `ttl_predicate_coverage` arrows; CURIE computed, not stored) |
| `basicttl/law/query_tree.shapes.ttl` | **query-tree**: Q1..Q7 are typed Node/Arrow trees (no heredoc, no keyword-as-data); each `triple_pattern` isomorphic to `typed_hom_triple` (S/P/O); Q4/Q5 inverse columns query-time-only |
| `basicttl/law/coherence.shapes.ttl` | **SHACL ⟷ `is?/1` colimit** (per-family verdict agreement) + **semantic-ancestry** gluing (every carrier `rdfs:subClassOf+` a dual-grounded SP1 tower) + **federation depth** (`owl:Class` `rdfs:comment` ≥ 200) |
| `basicttl/law/w2_coverage.queries.sparql` | the EXPECT-TRUE ASK suite — one biting ASK mirroring each shape (`q_shape_coverage`, `q_anchor_grounding`, `q_pattern_from_anchor`, `q_predicate_catalogue`, `q_query_tree`, `q_shacl_is_coherence`, `q_semantic_ancestry`, `q_federation_depth`) + a per-boundary inline **DATA CONTRACT** comment naming the exact triples that turn it GREEN |
| `basicttl/law/checks/run-w2-law-checks.sh` | the runner: parse the federated graph (SP1..SP6 data TTLs + the coverage-registry TTLs) + pyshacl against the five shape files (`inference="rdfs"`, `conforms=True`) + depth gate + every ASK + the probe battery |
| `basicttl/law/README.md` | the coverage law, the federated graph it validates, Consumes/Produces, how to re-run, the probe log |

## 4. Verification plan (evidence-first; every constraint a proven tooth)

Runner `basicttl/law/checks/run-w2-law-checks.sh` loads SP1..SP6 **data** TTLs + the materialized
coverage registries (families / 18 predicates / 26 shapes / Q1..Q7 trees / 11 anchors) into one
federated graph, validates against the five SP7 shape files (loaded **only** as the shapes graph),
runs the ASK suite against the data graph, runs the depth gate — exits 0 iff parse OK,
`pyshacl conforms=True`, every EXPECT-TRUE ASK true, and depth gate passes. Each law's tooth
(probe of record, RED→GREEN, `conforms=True → False` and the mirror ASK `True → False`):

- **shape-coverage** — add an atom family with no NodeShape (or a NodeShape targeting no family) →
  `ShapeCoverageShape` fires; `q_shape_coverage` flips.
- **anchor-grounding** — inject a `concrete_anchor` with two `grounds_in_cco` (violates max 1) or none
  (violates min 1) → `ConcreteAnchorShape` fires; a `yoneda_hom_leg` missing `grounds_in_cceo` →
  `YonedaHomLegShape` fires; `q_anchor_grounding` flips.
- **pattern-from-anchor** — inject a shape carrying an inlined `sh:pattern "^cco:.*"` literal instead
  of a `pattern_anchor_urn` reference → `PatternFromAnchorShape` fires; `q_pattern_from_anchor` flips.
- **predicate-catalogue** — inject a shape `sh:path` referencing a predicate URN absent from the 18 →
  `PredicateCatalogueShape` fires; `q_predicate_catalogue` flips.
- **query-tree** — inject a query carrying a raw `query_body` string (a SPARQL keyword as data) or a
  `triple_pattern` missing its P (predicate_urn) → `QueryTreeShape` fires; `q_query_tree` flips.
- **SHACL⟷is?** — inject a spec that conforms to its NodeShape but whose recorded `is?/1` verdict is
  `false` (or vice-versa) → `ShaclIsCoherenceShape` fires; `q_shacl_is_coherence` flips.
- **semantic-ancestry** — inject `ex:Loose a owl:Class ; rdfs:subClassOf owl:Thing` (never reaches a
  floor tower) → `SemanticAncestryShape` fires; `q_semantic_ancestry` flips.
- **federation-depth** — inject `ex:Shallow a owl:Class ; rdfs:comment "too short"` →
  `FederationDepthShape` fires; `q_federation_depth` flips.

Defang note (consumed from SP1 §6): because targets carry `rdfs:range`, plain `sh:class` would be made
vacuous under `inference="rdfs"`; every value-type check is `sh:sparql` reading genuine edges
(`rdfs:subClassOf*` walks, `STRLEN`, `COUNT`, `NOT EXISTS`) that range-inference cannot synthesise.
Federation depth is enforced **twice** — the SHACL `FederationDepthShape` and the existing
`scripts/ontology-depth-check.py` — so a regression is caught by either. Each ASK carries an inline
DATA-CONTRACT comment naming the exact triples the downstream TTL must emit to go GREEN (defines "done").

## 5. Interfaces

### Consumes (named precisely)

- **From Helios (authored source-of-truth — the structures LIFTED):**
  `helios/01_data_src_specs/shacl_shape_coverage.spec.yaml` (26 NodeShapes; ConcreteAnchorShape +
  YonedaHomLegShape; `pattern_anchor_urn`; `no_hardcoded_patterns`),
  `…/sparql_query_coverage.spec.yaml` (Q1..Q7 typed trees; `no_hardcoded_queries`; Q4/Q5 query-time
  columns), `…/ttl_predicate_coverage.spec.yaml` (18 predicate arrows; `grounds_in_cco`/`grounds_in_cceo`
  card 1..1; `no_hardcoded_predicates`), `…/universal_anchors.spec.yaml` (11 Layer-0 anchors; the two
  grounding-anchor `pattern:` regexes), `…/triad_fibration.spec.yaml` (math fibre coherence check),
  `helios/01_src_specs/lib/silmaril/wave8/*.ex` + `checks/runner.ex` (the `is?/1` executable legs),
  srcy Vol 24 + appendix E `specs/shapes/` (theory ancestor).
- **From SP1 (committed floor):** the **twin-olog colimit taiji** + **59 dual-grounded towers**
  (`SemanticAncestryShape` requires every carrier to reach a `prim:DualGroundingShape`-certified class);
  the teeth discipline (defang-proof `sh:sparql`, EXPECT-TRUE ASK mirror, probe RED→GREEN, non-vacuous)
  lifted from `primitives.shapes.ttl`/`primitives.queries.sparql`.
- **From SP2 (AOB meta-ontology):** the family registry `aob:atomFamilyUrn` + the `top_kind: node|arrow`
  progenitor split + `aob:ConcreteAnchor`/`aob:YonedaHomLeg` — the `sh:targetClass`es and the
  families↔shapes bijection domain; the S/O/P columns (`source_node_urn`/`target_node_urn`/`cpo_process_iri`)
  the query trees walk.
- **From SP3/SP4/SP5/SP6:** their value classes enter the federated graph as `SemanticAncestryShape`
  targets (S/O/P-tower geometry SP3, projection classes SP4, format leaves SP5, glossary terms SP6) —
  each must reach the SP1 floor. SP7 does **not** re-author their *interior* laws (SP3 `crs:DimensionCountShape`,
  SP2 AOB composition, SP4 loss-class algebra, SP5 format decomposition, SP6 OSSIE polysemy stay local).

### Produces

- **For SP8 (basicttl depth remediation — CONSUMES SP7):** the **federation depth + semantic-ancestry +
  coverage law is the absolute remediation target**. SP8 is remediation-local — it fixes the basicttl
  files (stub classes, bare individuals, content predicates, fable dissolve) until SP7's federation law
  conforms. SP7 owns the depth-SHACL; SP8 consumes it. (Resolves the prior mutual-ownership ambiguity.)
- **For SP9 (Split↔Consolidated render seal):** a **certified-coverage-complete federated graph** — no
  orphan family, no ungrounded atom, no inlined regex, no off-catalogue predicate, no incoherent
  SHACL/`is?` verdict — the clean input the split/consolidate inverse pair seals.
- **For W4 (CI/CD engine):** the five shapes + ASK suite become the **`phase_w4_3` blocking coverage
  gate** run under the multi-engine ContractGate; the math-fibre coherence check made CI-executable.

## 6. Non-goals (this iteration) & open questions

**Non-goals.** Corpus-agnostic — zero live-corpus binding (that is W5). SP7 does **not** re-pick the
anchor set (`universal_anchors_proposed` is `human_review_required`, `never_auto_merge`), does **not**
render the surface SHACL/SPARQL (that is the `verb.shacl.ttl.j2`/`verb.sparql.j2` engine in W3/W4 — SP7
authors the *law over* the render, not the render), does **not** resolve OSSIE polysemy (SP6 authors
the layer; W5's mime arbiter resolves), and does **not** duplicate any sub-project's *local* interior
shapes. Built to be re-run and relaunched, not final (Directive 13).

**Open questions for the maintainer (Praeriehund — flagged, not invented):**

1. **PROVISIONAL — SHACL⟷`is?/1` verdict carrier.** The coherence law needs the *exact* form in which
   an `is?/1` verdict enters the graph (a materialized `law:isVerdict` boolean per spec, vs. running
   the Elixir leg in the runner and comparing exit codes out-of-band). The `is?/1` legs are rendered in
   `01_src_specs`, not the W2 graph; whether SP7 checks agreement *in-graph* or *in-runner* is
   genuinely undecidable now — marked PROVISIONAL, to bind in the plan once the render seam (SP9/W4) is
   fixed.
2. **Semantic-ancestry target scope.** Should `SemanticAncestryShape` target *every* `owl:Class` in
   SP2–SP6, or only classes marked `law:SemanticCarrier` / `rdfs:subClassOf+` an AOB value root? SP1
   deliberately excluded its arrow/presheaf meta-classes from dual-grounding; the federation law must
   likewise not false-positive on SP2–SP6 *meta* classes. Recommend marker-scoped; needs the
   maintainer's call on marker vs. exclusion list.
3. **Depth-gate federation staging.** Authored federation-wide, but does it bite on the *whole*
   `basicttl` tree immediately (RED by construction until SP8 lands) or stage to the W2 graph first,
   whole-tree post-SP8? Recommend staged; needs the maintainer's staging decision (this is the
   SP7-owns / SP8-consumes seam made concrete).
4. **`primitive_atom` family top_kind: mixed.** `shacl_shape_coverage` notes `primitive_atom` is
   `top_kind: mixed` (62 arrow + 11 node species) so its shape is top_kind-agnostic. Does the
   families↔shapes bijection count `primitive_atom` as one family (26 total) or split it by species
   top_kind? Lifting the spec's own `total_shapes: 26` says one — flagged to confirm it is not force-fit.
