# Helios facet map — `helios/01_data_src_specs` (the executable SPECS / CONTRACTS layer)

> W1/W2 mapping agent, 2026-08-08. Praeriehund honesty: the tree IS the taxonomy; I read every
> top-level spec/contract IN FULL and characterized the ~191 `products/` atom files from a broad
> sample with coverage stated per subtree. What I sampled vs. read-in-full is marked. Nothing
> claimed read that was only sampled. No state-changing git was run; this is a git-ignored facet.

---

## 0. What this facet IS (one sentence)

This is the maintainer's **source-of-truth `data/` + `src/` spec layer**: the small set of top-level
`*.spec.yaml` / `*.contract.{yaml,json}` that (a) declare the **Layer-0 anchor algebra**, the
**7-leg / 3-fibre render fibration**, the **telephone twin**, and the **per-leg coverage** (SHACL /
SPARQL / TTL predicate) that drive the whole colimit render; plus (b) the **unary-byte-frame-law
CONTRACTS** that decompose each legacy shell/python script into typed request → ContractGate
boundaries → unary operations → Frame; plus (c) `products/` — the per-product **atom seed data**
(concrete_anchor nodes + yoneda_hom_leg arrows) these specs project. It is upstream of, and
re-derived by, SP1's Primitive Floor.

The **live filesystem home** (per `project_env.spec.yaml`) is
`$SIL_REPO_ROOT/src/silmaril_specs/data/…` = `/home/tristan/Music/final/working/src/silmaril_specs`;
the maintainer resolves this facet into that submodule. `predecessor_coordinates` inside the contracts
point at a *different* prior tree (`/home/tristan/Music/final/working/cannon`), the byte-equivalence
baseline.

---

## 1. Complete tree (the taxonomy)

### 1.1 Top level — 23 executable specs/contracts (all read IN FULL)

```
helios/01_data_src_specs/
├── universal_anchors.spec.yaml              LAYER-0 anchor law (11 anchors) — CCO/BFO upper anchor
├── universal_anchors_proposed.spec.yaml     Layer-0 staging (human_review_required, never_auto_merge)
├── triad_fibration.spec.yaml                7 render legs / 3 fibres (econ/lang/math) + coherence gates
├── triad_coherence_validation.spec.yaml     CONTRACT (active_red): validate fibration cardinality+fibre legs
├── triad_projection_validation.spec.yaml    CONTRACT (admitted_green): each leg's projection parses
├── telephone_events.spec.yaml               Directive-6 twin A: 4 agent-lifecycle emit arrows
├── telephone_supervision_tree.spec.yaml     Directive-6 twin B: 14-child parent supervision catalog
├── shacl_shape_coverage.spec.yaml           26 sh:NodeShapes, one per atom family (math fibre)
├── sparql_query_coverage.spec.yaml          7 canonical queries Q1..Q7 as typed Node/Arrow trees
├── ttl_predicate_coverage.spec.yaml         18 TTL predicates (Layer-1 arrows binding families→anchors)
├── sparql_render_context_merge.spec.yaml    CONTRACT (active_red): merge query+anchor+predicate ctx
├── turtle_subject_aggregation.contract.json CONTRACT (RED, 84 unary leaves): ttl-aggregate decomposition
├── turtle_subject_aggregation.equivalence_fixtures.json  13 predecessor byte-equality fixtures
├── wave_barrier_projection.spec.yaml        CONTRACT (admitted_green): roster→state precedence projection
├── wave_d_example_generation.spec.yaml      CONTRACT (active_red): worked-example atom generation
├── wave_f_music_grounding.spec.yaml         CONTRACT (active_red): 9-row type_urn→CCO grounding table
├── wave_f_orientation_grounding.spec.yaml   CONTRACT (active_red): 6-row family→CCO grounding table
├── yaml_document_parse_validation.spec.yaml CONTRACT (active_red): parse-only YAML gate
├── yaml_json_sequence_cardinality_projection.spec.yaml  CONTRACT (active_red): jq-length replacement
├── python_executable_identity_binding.spec.yaml         CONTRACT (active_red): python3 identity
├── rate_limit_probe.contract.yaml           CONTRACT (active_red, v2): api.anthropic.com HEAD probe
├── project_env.spec.yaml                    env source-of-truth (61 SIL_* vars) → .claude/settings.json
└── silmaril_conda_env.spec.yaml             conda/mamba env (python 3.12 + rdflib/pyshacl/linkml/duckdb)
```

### 1.2 `products/` — 191 files (per-product atom seeds + reference maps)

```
products/
├── _cco_class_label_map.tsv     CCO class IRI → label (cco:ontNNNNNNNN → "Deflecting Prism", …)
├── _cco_label_map.tsv           CCO relation IRI → label
├── _cpo_class_label_map.tsv     CPO/cceo class → label (cceo:ActOfAttending → "Act of Attending")
├── _demo.md                     "One CCO IRI, two disjoint domains" polysemy proof (cco:ont00001234)
├── bls/atoms.spec.yaml          (1275 ln) DuckLake/BLS survey analytics — concrete_anchors + yoneda_hom_legs
├── factory/atoms.spec.yaml      (2008 ln) 3-pillar orchestration (BashAttack/Cassander/PyBrain)
├── pyfun/atoms.spec.yaml        ( 845 ln) two presheaf examples (Burr+Hamilton / PyBrain→Jinja2)
├── storm/atoms.spec.yaml        (1178 ln) 8-Apache streaming pipeline (Storm/Kafka/Hudi/Ozone/Atlas/…)
├── users/atoms.spec.yaml        (1369 ln) identity-as-code (human/sous/robot; PGP/LDAP/Kerberos)
└── ldap/                        LDAPv3 modelled ONE-ATOM-PER-FILE (23 subdirs, ~180 files):
    ├── arrows_auth/ (8)          bind_simple, bind_sasl_{plain,scram_sha_256,gssapi,external,digest_md5}, …
    ├── arrows_avro_emit/ (8)     emit_*_witnessed — telephone-wire hook_ldap_* AVRO emission arrows
    ├── arrows_connection/ (5)    connect, disconnect, tls_at_connect, tls_upgrade_starttls, keepalive
    ├── arrows_extended/ (4)      who_am_i, start_tls, cancel, modify_password extended ops
    ├── arrows_filter/ (10)       and/or/not/equality/substring/approx/ge/le/presence/extensible match
    ├── arrows_mutation/ (11)     add/modify/delete/compare/modify_dn/abandon + samba-tool + ensure_*
    ├── arrows_result_handling/ (5)  classify_error, extract_dn/attribute_values/object_classes, count
    ├── arrows_schema/ (6)        get_root_dse / naming_contexts / supported_{controls,extensions,caps}
    ├── arrows_search/ (4)        search, search_paged, search_sorted, search_with_sync
    ├── capability_oids/ (4)      AD supportedCapabilities OID nodes
    ├── control_oids/ (4)         paged_results, persistent_search, server_sort, sync
    ├── enums/ (8)                scope, deref_alias_mode, auth_mech, tls_mode, change_type, server_family…
    ├── extended_op_oids/ (4)     who_am_i, start_tls, cancel, modify_password OIDs
    ├── identifiers/ (7)          ldap_dn, ldap_uri, ldap_oid, ldap_attr_name/value, filter_string, env_var
    ├── operations/ (12)          bind, unbind, search, add, modify, delete, compare, extended, abandon…
    ├── result_codes/ (53)        00_success … 94_no_results_returned (LDAPv3 RFC 4511 §A result codes)
    ├── sasl_mechanisms/ (9)      anonymous, plain, external, cram_md5, digest_md5, gssapi, scram*, oauth
    ├── seed_credential_profiles/ (1)  default_substrate_seed_profile (known-default password placeholder)
    ├── seed_identities/ (2)      substrate_svc, substrate_test
    ├── server_families/ (7)      openldap, active_directory, 389ds, apacheds, freeipa, oracle_oid, samba
    └── state_types/ (10)         ldap_session, authenticated_session, tcp_socket, tls_stream, result_set…
```

Coverage of `products/`: the 5 monolithic `atoms.spec.yaml` (bls/factory/pyfun/storm/users) — I read
bls in full (1275 ln) and sampled factory/pyfun/storm/users by key-structure + one-line summary. The
~180 LDAP files — I read `arrows_auth/bind_simple` + `state_types/ldap_session` in full and confirmed
the one-atom-per-file schema; the remaining files are the same schema at scale (enumerated above). A
census over every product file confirms the atom universe is exactly **two families**:
**634 `concrete_anchor` (node)** + **246 `yoneda_hom_leg` (arrow)** = 880 seed atoms. No other atom
family appears in `products/`.

---

## 2. The atom SCHEMA (the AOB seed shape, as this facet stores it)

Every atom in `products/` is ONE of two families. Both carry a `urn`, `bare_symbol`, `atom_family_urn`,
`top_kind`, and (in LDAP) `rfc_ref` + `description`.

**Node atom — `concrete_anchor` (`top_kind: node`):**
```yaml
- urn: urn:silmaril:product:bls:anchor:survey_cu_cpi_u
  bare_symbol: SurveySeries            # the abstract symbol (repeats across siblings)
  anchor_node: CuCpiU                  # the concrete instance node
  anchor_text: "The 'cu' Consumer Price Index …"   # ≥1-line prose grounding
  cco_grounding_iri: cco:ont00000958   # <<< CCO/BFO UPPER ANCHOR (load-bearing)
  cco_grounding_label: Information Content Entity
  atom_family_urn: urn:silmaril:atom-family:node:concrete_anchor
  top_kind: node
```

**Arrow atom — `yoneda_hom_leg` (`top_kind: arrow`):**
```yaml
- urn: urn:silmaril:product:bls:leg:scan_parquet_shard
  bare_symbol: ScanParquetShard
  source_node_urn: …:parquet_shard_file   # S (Subject tower)
  target_node_urn: …:ducklake_catalog_file # O (Object tower)
  cpo_process_iri: cceo:ProcessingAndExploitation   # P (Predicate — CPO/cceo process)
  cpo_process_label: Processing And Exploitation
  atom_family_urn: urn:silmaril:atom-family:arrow:yoneda_hom_leg
  top_kind: arrow
```

This is the concrete **S/O/P tower evidence** at the seed layer: `source_node`=Subject,
`target_node`=Object, `cpo_process_iri`=Predicate. The arrow family is *named* `yoneda_hom_leg` — an
atom is literally a leg of a Yoneda hom-profile (Hom(−, A)), which is exactly the "ologs of ologs /
turtles" Yoneda framing SP1 later materialises as `prim:RepresentablePresheaf` + `prim:YonedaArrow`.
**Where the octet/tensor-block/subatomic decomposition lives:** NOT here. This facet stores atoms at
the *grounded-anchor* granularity (one CCO IRI per node, one CPO process per arrow). The subatomic
byte/tensor decomposition (`Byte ≠ Octet`, width 1..128, stream→block→container→value, RGB/256) is the
**Physical olog of SP1** and the AOB meta-ontology (SP2) that consume this layer. The bls product only
*names* the byte/hexword/word layers and the `PAR1` magic bytes in `anchor_text` prose — evidence, not
a typed carrier. Praeriehund: the tensor block / sha256-identity / endianness carriers are **absent
from this facet**; they are downstream (SP1 physical.ttl + SP2/SP3).

**Each atom's rendered fan-out (the `triad_render` block on every product):** `rendered_legs: [sh, ex,
atlas.csv, ttl, shacl.ttl, sparql, linkml.yaml]` — i.e. every seed atom projects to all 7 fibration
legs. That is the projection family made concrete.

---

## 3. universal_anchors — the CCO/BFO upper-anchor law (LOAD-BEARING, verbatim)

`universal_anchors.spec.yaml` — `algebra_role: pure_seed`, `layer: 0`, `total_anchors: 11`
(`node_kind_count: 10` + `arrow_kind_count: 1`). Scheme:
`urn:silmaril:universal-anchor:<top_kind>:<sub_kind>:<slug>`. The 11 anchors are the **tensor spaces**
every downstream field binds to (see telephone `tensor_space_urn`). Primitives:
`StringNode / IntNode / BoolNode / EnumNode`.

The two load-bearing grounding anchors:

| anchor | primitive | pattern | resolves_in |
|--------|-----------|---------|-------------|
| `…node:identifier:cco_grounding_iri` | StringNode | `^cco:ont[0-9]{8}$` | `SIL_CCO_TTL_DIR` → `cco-merged/cco.ttl` |
| `…arrow:identifier:cpo_process_iri`  | StringNode | `^cceo:[A-Za-z0-9_]+$` | `SIL_CPO_TTL_FILE` |

The other 9: `paper_slug`, `urn_literal` (`^urn:silmaril:[a-z\-]+(:[a-z0-9_\-]+)+$`), `env_locked_path`
(`^/home/tristan(/…)+$`, `must_be_referenced_via_prefix: SIL_`), `counter:cardinality` (IntNode ≥0),
`flag:boolean` (BoolNode), `literal:prose_short` (≤2048), `literal:prose_long` (≤16384),
`enum:milestone` (chapter_skeleton/atom_pass/vision_pass/e2e_build_ok/render_all_legs_ok),
`enum:wave_role` (builder/polisher).

**The policy (what it mandates):** every **node** atom MUST carry exactly one `cco_grounding_iri`
matching `cco:ontNNNNNNNN` (enforced by `grounds_in_cco`, min 1 max 1 in ttl_predicate_coverage +
`ConcreteAnchorShape` in shacl_shape_coverage); every **arrow** atom MUST carry exactly one
`cpo_process_iri` matching `cceo:…` (`grounds_in_cceo`). CCO = **Common Core Ontologies** (mid-level,
sitting under **BFO** — Basic Formal Ontology); CPO/cceo = the Common Core **process/event** ontology.
So the "CCO/BFO upper-ontology anchor" the maintainer said "HAS TO BE" load-bearing is realised as:
*no atom exists without a CCO (node) or CPO (arrow) grounding IRI that resolves against the external
CommonCoreOntologies TTL.* Resolution paths (`project_env.spec.yaml`): `SIL_CCO_TTL_FILE =
…/CommonCoreOntologies/src/MergedAllCoreOntology.ttl`, `SIL_CPO_TTL_FILE = …/CommonCore/cpo.ttl`,
`SIL_CCO_VERSION = "2.x"`. The three `products/_c{c,p}o_*label_map.tsv` are the local IRI→label caches.

New anchors are **not auto-mergeable**: `universal_anchors_proposed.spec.yaml` has
`promotion_policy: human_review_required`, `never_auto_merge: true`. It currently stages 3 proposals
(`claude_hook_event` enum, `telephone_scope` enum of 10 values, `shell_command` literal), each
`awaits: human_review`. This is the anchor-law governance the maintainer wants.

---

## 4. The projection family + coherence/loss taxonomy

### 4.1 `triad_fibration.spec.yaml` — 7 legs over 3 fibres (the projection family)

| fibre | legs | coherence_check |
|-------|------|-----------------|
| **econ** | `sh` (bash), `ex` (elixir) | `byte_equal_stdout` — bash & elixir emit byte-identical stdout |
| **lang** | `atlas` (atlas_csv), `linkml` (linkml_yaml) | `schema_instance_match` |
| **math** | `ttl` (rdf_turtle), `shacl` (shacl_turtle), `sparql` (sparql_query) | `pyshacl_validation_passes` |

Gate: `check_triad_coherence` → `$SIL_SCRIPTS_DIR/check-triad-coherence.sh`. This is THE projection
family for W2: one atom → 7 surface renders, grouped into 3 epistemic fibres each with a defining
coherence law. The math-fibre coherence *is* "the ttl, its shacl shapes, and its sparql queries agree
under pyshacl" — the property `sparql_query_coverage` calls "the math fibre's defining property."

### 4.2 The nth-dim effect/loss projections

- **`triad_projection_validation.spec.yaml`** (state `admitted_green`, replacement 57-line python,
  84 declared operations, 16 ContractGate boundaries): validates every leg's projection *parses* —
  turtle/shacl via `rdflib.Graph.parse(format=turtle)`, sparql via `prepareQuery`, linkml via
  `yaml.safe_load` + id-or-name presence. Per-family counters `[success, failure]`; observed baseline
  totals `{success: 404, failure: 73}`. This is the **syntactic-acceptance projection** across the
  fibration — the first loss surface (a leg that fails to parse is a projection loss).
- **`wave_barrier_projection.spec.yaml`** (state `admitted_green`): the **precedence/state projection**
  — a roster of agent slugs projected through DuckDB-over-Avro into a 4-state lattice with explicit
  precedence `failed > done > started_but_not_complete > silent` (`predecessor_state_precedence`,
  `kind: precedence_projection`). `timestamp_semantics: truthiness_only`, `progress_event_semantics:
  ignored` — i.e. the projection deliberately *loses* timestamp magnitude and progress detail (nth-dim
  → lower-dim collapse). It has 5 explicit routes (missing_env / invocation_failure / empty_roster /
  nonempty_without_avro / nonempty_with_avro) and a `result_seal` + `result_readback` closure.

Praeriehund: the *named 5-class* nth-dimensional loss taxonomy the W2 lens asks about (SP1 README:
"the realization effects seed the 5 loss classes" for SP4 the projection packet) is **not enumerated in
this facet**. What this facet supplies is the *substrate* SP4 formalises: the 3-fibre coherence family +
two concrete lossy projections (syntactic-acceptance, state-precedence). The Frame's `output/effect`
loss lives in the unary-law contracts (§6), not as a 5-way enum here.

---

## 5. The telephone twin (Directive 6) — located and characterized

Directive 6 asked to make the "twin mention" link between the byte/color substrate and
`agents/telephone` explicit as a tighter Yoneda ologs-of-ologs. **This facet is where the telephone
lives as two paired specs (the twin):**

**`telephone_events.spec.yaml`** — `agent_lifecycle_taxonomy`, 4 emit **arrows**:
`agent_start / agent_progress / agent_complete / agent_failure`, each `top_kind: arrow`,
`scope_value: paper`. The Yoneda tightness Directive 6 wanted is **literally present**: every event
field carries a `tensor_space_urn` pointing at a Layer-0 universal anchor — e.g. `slug` →
`…node:identifier:paper_slug`, `milestone` → `…node:enum:milestone`, `atom_count_so_far` →
`…node:counter:cardinality`, `retry_recommended` → `…node:flag:boolean`. So a telephone event *is* a
tuple of points in universal-anchor tensor-spaces (the Frame = Yoneda point, applied to the wire). CLI
protocol: `$SIL_PARENT_REPO/bin/cheese_text --scope <v> --event <last-urn-segment>
--detail <semicolon-joined kv>`. Renders to `sh`+`ex` only (econ fibre).

**`telephone_supervision_tree.spec.yaml`** — `parent_repo_supervision_catalog`,
`read_only_reference: true`, 14 children under `Telephone.*` in the parent `research_render` app.
The **twin/gossip mechanism** Directive 6 tied to the federation theorems (GossipPreservesMittens,
ReplicationConvergence) is here concretely: `Telephone.GossipPropagator` (`role:
cross_origin_relay`) + `Telephone.Cross` (`event_router`) + `Telephone.Switchboard`
(`l0_hot_path_ring_buffer`, capacity 200) + `Telephone.Consumer.OcfAppender` (avro OCF writer) +
`Telephone.Dial` (rpc_reply_server) + `Telephone.Port` (UDS listener, ops
text/call/status/introspect/trace_start/trace_stop). Artifacts: `SIL_TELEPHONE_SOCK`,
`SIL_AVRO_OCF_DIR`, `SIL_DUCKDB_DB`, `logs/research_render_event.avsc`. The LDAP
`arrows_avro_emit/` product (8 `emit_*_witnessed` arrows) shows the same wire consumed at the product
level — an LDAP protocol step surfaces as a `hook_ldap_*` AVRO record on the telephone wire.

So Directive 6's concrete location = these two specs + `arrows_avro_emit`; the "twin" is the
events-taxonomy ⟷ supervision-catalog pair, joined at the Avro/`cheese_text` wire and Yoneda-tightened
by `tensor_space_urn` field-to-anchor pinning.

---

## 6. The unary-byte-frame-law CONTRACTS (how this facet relates to / corrects SP1..SP9)

Ten of the top-level artifacts are **`*.contract` decompositions** obeying the Universal Unary
Byte-Frame Law (`docs/unary-byte-frame-law.md`). Each takes a legacy shell/python `predecessor`
(hash-pinned) and re-expresses it as: a `request:` **carrier** (one typed input) → `external_boundaries`
(each an operation behind a **ContractGate**, `contract_gate_state: absent|admitted`) → a flat list of
**`operations`** (unary arrows `input → output`, `kind: …`) → a `frame_plan` (`composition_owner:
make`) → an **`admission:`** ledger tracking five gates:
`typed_input_carriers / physical_frame_results / rule_9_operation_proofs /
python_contract_gate_bindings / predecessor_equivalence_receipts`.

State of each contract (RED = law specified but enforcement not yet satisfied — matches the law doc's
"active red migration"):

| contract | state | scale |
|----------|-------|-------|
| `triad_projection_validation` | **admitted_green** | 84 operations, 16 gates, 19 caller-owned coords, predecessor byte-equal (stdout 1336 B, sha pinned) |
| `wave_barrier_projection` | **admitted_green** (Rule-9 composition still red) | 5 routes, result-seal + readback |
| `turtle_subject_aggregation` (.contract.json) | **RED** | 84 unary leaves + 9 coordinator gates, all Rule-9 RED (no authoritative python frontend) |
| `rate_limit_probe` (v2) | **active_red** | fixture-only network gate; production network gate absent; live probe RED |
| `triad_coherence_validation` | active_red | all admission gates `absent` |
| `wave_d_example_generation` | active_red | 306-line predecessor, all gates absent |
| `wave_f_music_grounding` | active_red | 9-row type_urn→CCO table |
| `wave_f_orientation_grounding` | active_red | 6-row family→CCO table |
| `sparql_render_context_merge` | active_red | RED evidence: hardcodes 5 query indices vs authority's 7 |
| `yaml_document_parse_validation` | active_red | parse-only gate |
| `yaml_json_sequence_cardinality_projection` | active_red | jq-length replacement |
| `python_executable_identity_binding` | active_red | python3 identity, 2 occurrences |

**Relation to SP1 (Primitive Floor) and corrections:**
- SP1 **re-derived the categorical spine** (Frame = Yoneda point; ρ as functor; presheaf/colimit;
  sheaf-style dual-grounding) that this facet only *names*. Here the Yoneda structure is nominal
  (`yoneda_hom_leg` atoms, `RepresentablePresheaf`-shaped hom-legs) and the Frame is the unary-law
  `Frame(output, error|effect)` that every contract's `operations`/`frame_plan` targets. SP1's
  `taiji.ttl` makes the Frame=Yoneda-point identification a teeth-proven graph fact; this facet is the
  *executable predecessor* that identification governs.
- **The correction SP1 applies to this facet:** here every atom bottoms out at a **flat CCO IRI**
  (`cco:ont00000958`, one grounding, no tower). SP1's dual-grounding invariant says *no formal type may
  bottom out at a bare leaf* — each must live in a subtyping tower (ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ …) **and** realize into a
  physical byte carrier via the monadic ρ. So this facet is the **pre-dual-grounding state** that SP1's
  Primitive Floor (#1) + AOB meta-ontology (#2) + depth remediation (#8) deepen: the anchors/atoms here
  become the *objects* SP1 puts into towers and realizes to bytes.
- **SP1's declared consumers ARE this facet's contents:** AOB(#2) "grounds each atom's tensor/byte
  field into the Physical olog" — the atom tensor/byte field is exactly the missing subatomic layer
  noted in §2. S/O/P-tower CRS(#3) "grounds `z` (uint16 of first two `source_sha256` octets)" —
  `source_sha256`/`z`/endianness are **absent here** and supplied by SP3 (Praeriehund). Projection
  packet(#4) "the realization effects seed the 5 loss classes" — this facet's 3-fibre coherence +
  wave_barrier/projection_validation are the substrate SP4 formalises. File+format(#5), depth-remed(#8),
  render seal(#9: "the colimit round-trip is per-primitive split↔consolidated reversibility") — the
  `result_seal`/`result_readback` and `consolidate(split(g))==g` machinery already prototyped in
  `turtle_subject_aggregation.contract.json` and `wave_barrier_projection`.
- **"We can't just jump to towers":** consistent with this facet — dimension/axes are per-geometer and
  built bottom-up. Here the axes present are the **anchor sub_kinds** (identifier/counter/flag/literal/
  enum) and the **S/O/P** of the arrow atom (source/target/cpo). The mathematical towers (ℕ⊂ℤ…) and the
  a,b / x,y / x,y,z,w,p geometer axes are NOT in this facet — they are SP1's formal olog. This facet
  supplies the flat geometer-agnostic seed the towers are grown from.

---

## 7. The coverage specs (per-leg emission law, keyed off Layer-0)

- **`ttl_predicate_coverage.spec.yaml`** — 18 predicates, each a **Layer-1 Arrow** binding
  (source family → target Layer-0 anchor). E.g. `grounds_in_cco` (node families → `cco_grounding_iri`,
  card 1..1), `grounds_in_cceo` (arrow families → `cpo_process_iri`), `source_node`/`target_node`
  (the S/O of every arrow family), `has_synonym`, `has_antonym`, `has_surface_syntax` (bash/elixir
  legs). **CURIEs and prefixes are NOT stored** — computed at render time from the anchor's `pattern`.
  This is the "no hardcoded predicate/prefix/IRI" law.
- **`shacl_shape_coverage.spec.yaml`** — 26 `sh:NodeShape`s (24 paper families + 2 primitives families
  from Wave-E). Each shape's property `path`s reference predicate URNs; `pattern` constraints reference
  Layer-0 anchor URNs (no inlined regex). Note **`SynonymShape` and `AntonymShape` both target the same
  atom style** with `source_node` + `has_synonym`/`has_antonym` — the polysemy substrate (one relation
  atom is synonym in one glossary, antonym in another).
- **`sparql_query_coverage.spec.yaml`** — 7 queries Q1..Q7 as **typed Node/Arrow trees** (no
  `query_body:` heredoc, no SPARQL keyword as data). `triple_patterns[]` are "structurally isomorphic to
  the typed_hom_triple Layer-1 Arrow family" — i.e. a SPARQL triple *is* an S/P/O arrow. Q1 anchors
  missing CCO, Q2 legs with unknown CPO, Q4/Q5 compute inverse-only atlas columns *at query time, never
  stored*. The render macro `α_star^{M_sparql}` walks the tree; the same tree projects to SHACL and TTL
  (`α_star^{M_shacl}`, `α_star^{M_ttl}`) — this is the math-fibre coherence made structural.

These three plus `atom_family_registry` and `universal_anchors` are the closed loop: **families →
predicates → shapes/queries**, all anchored to the 11 Layer-0 tensor spaces.

---

## 8. Glossary polysemy / geometer axes (Directive 1) — what this facet carries

- **Polysemy is literal and load-bearing:** `products/_demo.md` is the maintainer's "what can this do?"
  proof — **one CCO IRI `cco:ont00001234` (DataSet) grounds anchors in two disjoint domains**
  (encyclopedia's Mittens-cat ontology AND real-world BLS labor stats) "without code change." That is
  the "mole of glossaries" — the same upper-anchor speaks distinct epistemologies.
- **Synonym ⟺ antonym simultaneity:** carried by the `synonym`/`antonym` arrow families in
  `ttl_predicate_coverage` + `shacl_shape_coverage` (both present, same shape, opposite predicate) —
  the structural room for "one term as synonym AND antonym across glossaries."
- **Geometer axes:** the operative axes in THIS facet are the anchor `sub_kind`s and the arrow S/O/P —
  not the a,b / x,y / x,y,z,w,p / tower axes (those are SP1). Honest scope: this facet is the flat,
  per-geometer-agnostic seed layer.

---

## 9. Decisions answered from THIS facet (summary)

1. **z byte-order / endianness progenitor** — **NOT in this facet.** No `source_sha256`, no `z`, no
   endianness/BE-LE progenitor carrier. Only prose mentions of byte/hexword/word layers + `PAR1` magic
   bytes in `bls` anchor_text. This is a downstream (SP1 physical / SP3 CRS) concern; the anchor layer
   here is byte-agnostic. Stated honestly rather than force-fit.
2. **Full projection + nth-dim effect/loss family** — the **7-leg / 3-fibre fibration**
   (`triad_fibration`) IS the projection family; coherence laws are byte_equal_stdout / schema_match /
   pyshacl. Two concrete lossy projections: `triad_projection_validation` (syntactic acceptance) and
   `wave_barrier_projection` (4-state precedence collapse, timestamp/progress deliberately dropped). The
   named 5-loss-class enum is SP4's, seeded from — not defined in — this facet.
3. **geometer/glossary axes vs towers** — axes here = anchor sub_kinds + S/O/P; towers are absent (SP1).
   Glossary polysemy is real and load-bearing (`_demo.md` one-IRI-two-domains; synonym+antonym families).
4. **universal_anchors CCO/BFO policy** — **fully answered.** Every node atom MUST ground in exactly one
   `cco:ontNNNNNNNN` (Common Core Ontologies, under BFO); every arrow in one `cceo:…` CPO process.
   Resolves against external CommonCoreOntologies TTL (`SIL_CCO_TTL_FILE`, v2.x). New anchors are
   human-review-only, never auto-merged. This is the load-bearing upper-anchor law.
5. **telephone twin** — **fully located.** `telephone_events` (4 emit arrows, fields pinned to Layer-0
   anchors via `tensor_space_urn` = Yoneda-point tightness) + `telephone_supervision_tree` (14 children;
   twin = `GossipPropagator` cross_origin_relay + `Cross` router). Wire = Avro/`cheese_text`; product
   consumer = LDAP `arrows_avro_emit`.
6. **SP1..SP9 grounding/corrections** — this facet is the **executable predecessor SP1 re-derived and
   corrects**: flat CCO-IRI grounding here → SP1 dual-grounded towers+byte-carriers; `yoneda_hom_leg`
   nominal Yoneda → SP1 materialised presheaf/functor/naturality; unary-law contracts' Frame/seal/
   readback → SP1's Frame=Yoneda-point + render-seal reversibility. SP1's listed consumers (#2 AOB tensor,
   #3 CRS z, #4 projection, #5 file/format, #8 depth, #9 seal) map one-to-one onto this facet's gaps and
   contents.
```
