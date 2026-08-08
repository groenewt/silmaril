# W2 · Sub-project 9 — the Split↔Consolidated render seal (design)

> **Batch design doc** (superpowers:brainstorming output, Directive 14 cadence: authored up
> front with SP2–SP8, presented for one maintainer review pass; no per-project Socratic gate).
> Design-only — NO `.ttl`/`.sparql`/implementation authored here. **THIS ITERATION's v1** —
> corpus-agnostic (zero live-corpus binding; that is the re-runnable W5), built to be re-run and
> relaunched, not permanent (Directive 13). Terminal step for the batch → superpowers:writing-plans.
>
> **This is a LIFT, not an invention (Directive 1).** Every structure below is lifted from the
> authored Helios source-of-truth: srcy **Vol 30 disintegration↔reassimilation** (the two governed
> functors + the reconstruction receipt + readback-before-promotion), the **node_arrow monograph**
> HONEST COCONE (`W = ObservedProjection(ColimCandidate(D))`, *not* literally `colim`),
> `projections/local_encyclopedia.tex` (the aggregate volume build = the consolidate projection), and
> the two executable seal contracts `helios/01_data_src_specs/turtle_subject_aggregation.{contract.json,
> equivalence_fixtures.json}` + `wave_barrier_projection.spec.yaml` (`result_seal` +
> `result_readback`). Maps: `ledger/W2/helios/{srcy,data_specs_contracts}_map.md`.

**Goal.** Author the **Split↔Consolidated reversible render-seal ontology**: `split`
(one-precise-semantic-thing-per-file, the *Graph* normal form) and `consolidate` (the single
aggregate render, the *Atlas* view) as the **disintegration/reassimilation functor pair** of Vol 30,
whose round-trip is certified **not by a universal-property claim but by residual/digest equality**
(Vol 30: "its certificate is equality of measures rather than a universal factorization"). This is the
**whole-federated-graph generalization of the SP1 per-primitive colimit round-trip**: where SP1's
`q_colimit_reflexive` proves `physicalFacet → interpretAs → formalFacet = identity` for **one** taiji
atom, SP9 proves `consolidate(split(G)) == G` and `split(consolidate(G)) == split(G)` for the entire
graph `G`, the Atlas and Graph views being the two sides that reconstruct each other.

Namespace: `seal: <urn:silmaril:seal:#>` (full-lexical URN idiom, unary law), grounding onto
`prim: <urn:silmaril:prim:#>` (SP1, committed), `prj: <urn:silmaril:prj:#>` (SP4), `law:
<urn:silmaril:law:#>` (SP7).

---

## 1. Goal (precisely) — three claims, each becoming graph structure with teeth

1. **`split` is disintegration; `consolidate` is reassimilation (Vol 30 lift).** `seal:split :
   Graph ⤳ SplitTree` is the disintegration functor **F₃₀** — it "separates a donor particle into
   inspectable surfaces **without pretending that the surfaces are independent**" — and
   `seal:consolidate : SplitTree ⤳ Consolidated` is the reassimilation functor **G₃₀**, which
   "materializes only the artifact diagram that passed the contract gate." Each is a Kleisli arrow of
   the *same* Frame monad SP1 defines and SP4 lifted (`seal:frameOutput` = a `prim:Container` byte
   carrier; `seal:frameEffect` = a `prj:LossClass`, `prj:Lossless` for a true seal). Neither is a
   bare function; both are **`prj:Projection`s** (SP4) — SP9 reuses SP4's reversibility atom, it does
   not mint a new one.
2. **The pair round-trips, certified by digest equality — NOT by a colimit claim (the honest
   correction).** Per the node_arrow monograph, the render `W` is **`ObservedProjection(ColimCandidate(D))`,
   not `colim(D)`**, "because this document is still a rendered artifact and not the substrate
   itself." So `seal:RenderSeal` is NOT asserted to *be* a colimit; it is the **observed projection of
   a colimit candidate**, and the *checkable* certificate is Vol 30's reconstruction receipt:
   `consolidate ∘ split = id_Graph` holds **iff the maximum cell residual is zero** (Vol 30 seal:
   `p = p̂ ⟺ ε_∞ = 0`), which SP9 realizes as a `seal:DigestCertificate` whose byte identities of the
   inputs and the round-trip output **match on the nose**. Digest equality is the whole-graph analogue
   of SP1's per-atom `q_colimit_reflexive` identity — an *equality of measures*, not a universal
   property. **Polysemy scope (Directive 16, "Polysemy!").** This `ObservedProjection(ColimCandidate(D))`
   framing **IS the CORPUS / artifact glossary sense of the polysemous lexeme "colimit"** — not a denial
   that the word ever means a literal colimit. The same word carries a second, **LOCAL / per-primitive**
   sense (the genuine two-object colimit whose universal property SP1 earns via a `q_colimit_universal`
   tooth, reused by SP2's sealed-group apex); **SP6 holds the ONE lexeme with BOTH glossary-scoped senses
   simultaneously**, with a biting polysemy tooth (SP6's reflexive own-vocabulary worked example). So
   **SP9 and SP2 are the two glossary poles of the same word** — SP9 the corpus/cocone pole, SP2 the
   local/genuine-colimit pole — both referencing "colimit" **through the SP6 glossary layer, never
   bare**. SP9's `q_not_a_colimit_claim` tooth (§4) guards exactly this *corpus* sense.
3. **The seal is the receipt + a second read — readback before promotion (Vol 30 lift).** Vol 30's
   controlling principle: *"A zero-exit reconstruction program is not the seal. The seal is the
   returned receipt together with a second read of its normalization and residual fields."* So
   `seal:RenderSeal` is a **two-tooth** object: (a) the `seal:DigestCertificate` (canonical digest of
   the round-trip) **and** (b) a `seal:Readback` that **physically re-reads** the sealed output and
   re-compares — the concrete shape lifted from the two contracts (§2). Neither projection may
   **invent, erase, or silently rename** a coordinate (the monograph's cocone anti-cheating law +
   Vol 30's natural-transformation anti-drift law); that prohibition is a biting tooth (§4).

Corpus-agnostic: pure shape, **zero corpus instances** (exactly SP1/SP4). One tiny witness graph may
be authored solely to keep the ASK suite non-vacuous, in the SP1 litmus discipline.

---

## 2. Architecture — the seal is Vol 30's reconstruction receipt, lifted to the whole graph

Nothing categorical is invented. SP1's exact machinery (colimit taiji, Frame/Kleisli monad ρ, mutual
back-pointer round-trip), SP4's projection algebra, and Vol 30's disintegration/reassimilation +
reconstruction-receipt are reused; the monograph's honest-cocone constraint keeps the claim from
over-reaching.

```
                    seal:split = disintegration functor F₃₀ (prj:Projection; retraction)
   Graph ─────────────────────────────────────────────────────────▶  SplitTree
   = the certified-well-formed federated W2 graph (SP7 law:*)          = one precise semantic thing
   = seal:atlasView (aggregate, the local_encyclopedia \input build)     per file (Complete Component
                                          ◀───────────────────────────   Account) = seal:graphView
                    seal:consolidate = reassimilation functor G₃₀ (the section of split)
        └─── seal:RenderSeal = ObservedProjection(ColimCandidate(Atlas ⟷ Graph)) ───┘
             certificate = digest equality (residual = 0) + physical readback  (NOT a colimit claim)
```

- **`split`/`consolidate` are SP4 projections, so reversibility is already typed.** `seal:split` is a
  `prj:Projection` with `prj:reversible true`, `prj:section = seal:consolidate`, and `prj:frameEffect
  prj:Lossless` — a **retraction whose section is a genuine two-sided inverse**, upgrading SP4's
  retraction to an isomorphism. This is the SP4 hand-off; SP9 does not re-derive reversibility, it
  **closes the pair and certifies it by digest**.
- **The consolidate direction IS the `local_encyclopedia.tex` aggregate build.** Vol 30's
  reassimilation is concretely the encyclopedia's `\SilBeginEncyclopediaVolume{NN} \input{src/…/paper}`
  aggregation: the split tree (one paper/section/atom per file) is glued into one ordered aggregate.
  Its `contractbox` carries the **bounded-projection law** SP9 lifts as a non-goal-of-explosion:
  *"No lookup, rewrite, citation, or render rule may require materializing every possible arrangement
  of the encyclopedia"* — the seal certifies the round-trip of **one** ordered arrangement, not the
  Avogadro-scale powerset (Directive-13-safe; anti-cheese-master, Vol 41).
- **The one-thing-per-file normal form is the Complete Component Account.** `SplitTree` is not a bag
  of files: `split` drills the graph into a normal form with **exactly one independently identified
  carrier / identity / relation-occurrence / Frame / state / operation per file** (unary law "Split
  and Consolidated Render Seal"). Each split entry carries a `seal:ComponentAccount` row — lexical
  locator, byte revision, semantic identity + exact semantic-family progenitor, disposition,
  **successor identity + inverse evidence** — so the inverse can recreate the exact split tree. A
  split that drops or fuses entries is red (§4).
- **The digest certificate is grounded on `prim:Hash` ONLY (the fix).** SP1's Binary tower has
  `prim:Hash` and `prim:Blob`; **there is no `prim:Digest`** in the committed floor. So
  `seal:DigestCertificate` is a `prim:Frame` whose output is a **`prim:Hash`** (the sha256 discipline
  — the same tower that grounds the atom z-coordinate = uint16 of the first two sha256 octets) over a
  `prim:Container`/`prim:Stream` byte carrier that `prim:byteDescendsTo+ prim:Bit`. Equality is
  asserted over the unary law's **five coordinate families** (topology, ordered content, byte
  revision, identities, relationship digests), each its own `prim:Hash` sub-carrier; the certificate's
  effect is `prj:Lossless` when they match and **names the drifting `prj:LossClass`** when they do not
  (honest reporting, not silent pass — Vol 30's visible residual, not a bare zero exit).
- **The concrete seal shape is lifted verbatim from the two contracts.** The
  `turtle_subject_aggregation.equivalence_fixtures.json` fixture *"every-fixture-seals-status-output-
  effect-digest-and-readback-equivalence"* enumerates exactly what a seal covers: **{process status,
  standard-output bytes, standard-error bytes, output-artifact existence, output-artifact sha256
  digest, output-artifact readback bytes}**. And it carries **two independent teeth**:
  *"serialized-receipt-seal-tamper-is-independently-rejected"* (a `seal:ReceiptSealHash` over the
  canonical receipt bytes) and *"sealed-output-physical-byte-tamper-is-independently-rejected"*
  (`seal:Readback` **physically re-reads the output** and re-digests). SP9 models both as distinct
  `prim:Frame`s so a tamper on either side is caught independently — this is the `consolidate(split(g))
  == g` result-digest **plus** physical readback the contract proves.
- **The digest excludes nondeterministic coordinates (wave_barrier lift).**
  `wave_barrier_projection.spec.yaml` pairs `result-seal-construction` (`kind:
  canonical_digest_construction`) with `result-readback-decision` (`kind: byte_equality_predicate`)
  under `frame_identity_excludes: [timestamp, process_id, random_value]`. SP9 lifts this as
  `seal:excludesFromDigest` (timestamp / process-id / random) so the canonical digest is a **stable
  function of the graph's content**, not of the wall clock — the seal is "drift-free recapture"-able
  because the digest is deterministic by construction.
- **Sealed self-hosting alignment.** The unary law's "Sealed Self-Hosting Closure" state 5
  (deterministic owned-to-readback mappings whose topology/content/relation digests equal the planned
  successor) is exactly this seal at source-tree scale; SP9 authors the **ontology of that gate**,
  which W4 (`phase_w4_6`) runs as a blocking check.

---

## 3. File layout (one file per concern — STRICTNESS Rule 14; honest ~7-file style)

Directory: `basicttl/seal/`. Categorical grounding lands in the data ttls; teeth in the
shapes/query files (exactly SP1/SP4's split). Every `owl:Class` carries a ≥200-char `rdfs:comment`;
external spellings (`sha256`, `URDNA2015`, `Scala`) survive only as immutable bridge evidence.

| file | responsibility |
|------|----------------|
| `basicttl/seal/seal.ttl` | the seal TBox: `seal:RenderSeal` (= `ObservedProjection(ColimCandidate)`, the honest observed projection — **not** asserted a colimit), `seal:SplitProjection` (disintegration F₃₀) / `seal:ConsolidatedProjection` (reassimilation G₃₀), both `⊂ prj:Projection`; `seal:atlasView`/`seal:graphView` (the two reconstructing views); `seal:frameOutput`/`seal:frameEffect`; each class dual-grounded into the SP1 colimit taiji |
| `basicttl/seal/inverse.ttl` | the **inverse-pair / anti-drift law**: `seal:inverseOf` (split ⟷ consolidate), the two round-trip composites `seal:consolidateAfterSplit = id_Graph` and `seal:splitAfterConsolidate = id_SplitTree`, grounded on SP4 `prj:reversible`/`prj:section`/`prj:isRetraction` upgraded to a two-sided iso; the Vol 30 **natural-transformation anti-drift** obligation (a source coordinate keeps its lawful meaning through the round-trip) |
| `basicttl/seal/digest.ttl` | the **reconstruction receipt**: `seal:DigestCertificate` (a `prim:Frame`, output a **`prim:Hash`** over a `prim:Container`), the **five equality coordinates** (`seal:topologyDigest`/`seal:contentDigest`/`seal:byteRevisionDigest`/`seal:identityDigest`/`seal:relationshipDigest`), each a `prim:Hash` byte-descending to `prim:Bit`; `seal:residual` (`= 0` ⟺ exact, Vol 30); `seal:excludesFromDigest` (timestamp/pid/random, wave_barrier lift); the drift-report edge into `prj:LossClass` |
| `basicttl/seal/readback.ttl` | the **readback-before-promotion** law (Vol 30): `seal:Readback` (a `prim:Frame` that **physically re-reads** the sealed output and re-digests), `seal:ReceiptSealHash` (the receipt's own `prim:Hash`); the two-independent-teeth structure lifted from the fixtures (receipt-seal tamper vs physical-output tamper); `seal:promotedIff` = certificate-holds ∧ readback-holds |
| `basicttl/seal/account.ttl` | the **Complete Component Account**: `seal:ComponentAccount` per split entry (lexical locator, byte revision, semantic identity + progenitor, disposition, `seal:successorIdentity` + `seal:inverseEvidence`); the one-thing-per-file normal-form rule; the bounded-projection contract (no powerset materialization) |
| `basicttl/seal/seal.shapes.ttl` | SHACL law (§4) — one `sh:NodeShape` per invariant, each `sh:sparql`/`sh:in` and proven to bite (defang-proof per SP1's lesson) |
| `basicttl/seal/seal.queries.sparql` | the EXPECT-TRUE ASK suite (§4), each with an inline DATA-CONTRACT comment |
| `basicttl/seal/checks/run-seal-checks.sh` + `README.md` | the runner (parse + pyshacl over the merged SP1(+SP4+SP7)+SP9 graph, re-running the SP1 shapes/ASKs + depth gate + every SP9 ASK + probe battery) and the floor doc + Consumes/Produces + how-to-re-run |

The runner loads the **SP1 four data TTLs + SP4 + SP7 data/shape graphs + SP9 data TTLs into one
graph** and validates against `seal.shapes.ttl` **and** re-runs the SP1 shapes/ASKs, because SP9 adds
`rdfs:subClassOf prim:FormalType` / `⊂ prj:Projection` classes that fall under SP1's
`prim:DualGroundingShape` / `q_universality` — SP9 is not green unless it keeps the SP1 floor (and,
transitively, the SP4/SP7 law) green.

---

## 4. Verification plan (evidence-first; every asserted law has a biting tooth)

Each shape is RED before authoring, GREEN after; each ASK is `EXPECT-TRUE`, non-vacuous (positive
ASKs FAIL on the empty graph; `FILTER NOT EXISTS` universals FAIL under injection), and **proven to
bite by a documented probe injection** (`True→False` / `conforms=True→False`), in the SP1 idiom.

**EXPECT-TRUE ASKs (`seal.queries.sparql`):**

| ASK | asserts | probe of record (must be CAUGHT) |
|---|---|---|
| `q_disintegration_reassimilation_pair` (litmus) | `seal:split seal:inverseOf seal:consolidate` and back; split is the F₃₀ disintegration Frame, consolidate the G₃₀ reassimilation Frame, each a `prj:Projection` | drop `seal:inverseOf` one direction → False |
| `q_consolidate_split_identity` | `consolidate ∘ split = id_Graph` — the composite exists AND its `seal:DigestCertificate` shows predecessor `prim:Hash` = successor `prim:Hash` AND `seal:residual = 0` | mismatched round-trip hash / nonzero residual → False |
| `q_split_consolidate_stable` | `split ∘ consolidate = id_SplitTree` (the other composite is stable) | a non-idempotent second composite → False |
| `q_digest_equality` | the certificate's five coordinate `prim:Hash`es (topology/content/byteRevision/identity/relationship) each match across the round-trip | corrupt one byte (byteRevisionDigest drifts) → False |
| `q_readback_before_promotion` | `seal:promotedIff` requires BOTH the `seal:DigestCertificate` AND the physical `seal:Readback` to hold — a zero-exit alone does **not** promote (Vol 30) | promote on certificate-only, readback absent → False |
| `q_two_independent_teeth` | receipt-seal tamper and physical-output tamper are caught by **distinct** hashes (`seal:ReceiptSealHash` vs `seal:Readback` re-digest) — neither masks the other | tamper output bytes while leaving the receipt hash intact → False (readback fires) |
| `q_no_silent_rename` | no coordinate in the consolidate output is absent from the split input, and none is dropped (monograph cocone anti-cheating + Vol 30 anti-drift) | rename/erase one URN across the pair → False |
| `q_split_normal_form` | every `SplitTree` entry is exactly ONE semantic thing (one `seal:ComponentAccount`, one semantic identity) — not a bag of adjacent definitions | fuse two things into one file → False |
| `q_component_account_total` | EVERY split entry has a `seal:successorIdentity` AND `seal:inverseEvidence` (the account is complete) | delete one entry's inverse evidence → False |
| `q_not_a_colimit_claim` | `seal:RenderSeal` is typed `seal:ObservedProjection` of a `seal:ColimCandidate` and is **NOT** asserted `owl:sameAs`/`rdf:type` a bare colimit object — the honesty guard (monograph `W ≠ colim(D)`) | assert `seal:RenderSeal a prim:Colimit` directly → False |
| `q_seal_lossless_generalizes_sp1` | both projections carry `prj:frameEffect prj:Lossless` + `prj:reversible true` + a `prj:section`; the certificate carrier `prim:byteDescendsTo+ prim:Bit` and grounds on `prim:Hash` — the whole-graph lift of SP1 `q_colimit_reflexive` | mark the seal lossy / drop the section / carrier not reaching `prim:Bit` → False |

**SHACL mirrors (`seal.shapes.ttl`):** `seal:InversePairShape` (both directions of `seal:inverseOf`,
each a `prim:Frame` + `prj:Projection`), `seal:DigestCertificateShape` (all five coordinate `prim:Hash`es
present, each byte-descending to `prim:Bit`; `seal:residual = 0` or a `prj:LossClass` drift is named),
`seal:ReadbackShape` (a physical re-read `prim:Frame` distinct from the receipt hash; promotion gated on
both), `seal:ComponentAccountShape` (every split entry carries locator + byte revision + semantic
identity + progenitor + disposition + successor + inverse evidence — the unary law's full row),
`seal:OneThingPerFileShape` (each entry is exactly one semantic thing), `seal:NoRenameShape`
(`sh:sparql` — no invented/erased/renamed coordinate across the pair), `seal:HonestProjectionShape`
(`seal:RenderSeal` is an observed projection of a colim candidate, never a bare colimit assertion),
`seal:SealRetractionShape` (reuses SP4 `prj:RetractionShape`: reversible ⟺ section ∧ Lossless,
strengthened to two-sided iso) — each a `sh:sparql`/`sh:in` constraint (never a bare `sh:class` where
an `rdfs:range` would make it vacuous, per SP1's defang lesson). **Reused SP1 tooth:** each new seal
`owl:Class` sits under `prim:DualGroundingShape`; an ungrounded class flips SP1's `q_universality`
false — SP9 satisfies it directly (each class carries its own `prim:Realization` + reflexive carrier +
`prim:Primitive`). Depth gate: every `owl:Class` ≥200-char `rdfs:comment`. **Depth gate for the
runner:** exit 0 iff every TTL parses, pyshacl conforms over the merged graph, the SP1 ASKs still
pass, and every SP9 ASK returns true with its probe proven to bite.

---

## 5. Interfaces

### Consumes — from SP1 (committed floor), named precisely
- **The per-primitive colimit round-trip SP9 generalizes:** `prim:Primitive`, `prim:formalFacet`,
  `prim:physicalFacet`, `prim:interpretAs` — the reflexive identity (`q_colimit_reflexive`) that SP9
  lifts to the whole graph; the `taiji.ttl` `prim:Primitive` comment naming this "the per-primitive
  instance of the split↔consolidated render reversibility".
- **The colimit taiji shape (Atlas/Graph = yin/yang one level up):** `prim:formalFacet`/`prim:physicalFacet`
  mutuality + `prim:gluedBy` — for the whole-graph render SP9 uses the **CORPUS / artifact glossary
  sense** of the polysemous "colimit" (Directive 16), `ObservedProjection(ColimCandidate(D))` per the
  monograph (§1 claim 2); the SP1 per-atom taiji uses the **LOCAL / per-primitive sense** (a genuine
  colimit, universal property earned). Both are entries of ONE lexeme SP6 carries — not a single global
  claim demoted — so neither over-claims.
- **Frame + Yoneda:** `prim:Frame` (`prim:isYonedaPoint true`) — split, consolidate, the certificate,
  and the readback are each a `prim:Frame`.
- **Realization monad + effects:** `prim:realizesAs`, `prim:frameOutput`, `prim:frameEffect`,
  `prim:NoEffect` (the `prj:Lossless` seed for a true seal).
- **Byte carrier ladder:** `prim:Container`, `prim:Stream`, `prim:ByteVector`, `prim:byteDescendsTo`,
  `prim:Bit` — the split file-tree and the consolidated render are byte carriers.
- **Binary tower for the digest — `prim:Hash` and `prim:Blob` ONLY (the fix; there is NO
  `prim:Digest` in SP1):** `seal:DigestCertificate`, the five coordinate digests, `seal:ReceiptSealHash`,
  and the readback re-digest are all `prim:Hash` (the sha256 discipline; the same tower the atom
  z-coordinate uses — the uint16 of the first two sha256 octets).
- **RDF-term + Aggregate towers (topology vs ordered content):** `prim:RDFGraph`, `prim:Triple`,
  `prim:Quad`, `prim:Set` (topology, unordered), `prim:List` (ordered content), `prim:BlankNode`
  (identity/relabelling — a rename the seal forbids unless a lawful canonicalization tolerates it, Q3).
- **SP1 law kept green:** `prim:DualGroundingShape` / `q_universality` (SP9 classes satisfy it); the
  teeth discipline (defang-proof `sh:sparql`, EXPECT-TRUE ASK mirror, probe-injection RED→GREEN)
  lifted verbatim from `primitives.shapes.ttl` / `primitives.queries.sparql`.

### Consumes — from SP4 (projection packet, lower in the batch)
- **The headline hand-off:** `prj:Projection`, `prj:reversible`, `prj:section`, `prj:isRetraction` —
  the per-projection reversibility declaration that IS the split↔consolidated inverse-pair atom SP9
  seals (SP4 §5). SP9 upgrades the SP4 retraction to a **two-sided iso** and certifies it by digest.
- **`prj:self` = `id_Graph`** — the identity leg the round-trip composites collapse to (SP4 Q1 flags
  whether `self` = the consolidated render; see §6 Q2).
- **The loss classes + zero:** `prj:LossClass`, `prj:Lossless`, `prj:PrecisionLoss`, `prj:RangeLoss`,
  `prj:LexicalEncodingLoss`, `prj:StructuralLoss`, `prj:SemanticLoss` — the vocabulary the seal
  **reports drift in** (a lossy round-trip names its exact `prj:LossClass`, per Vol 30's visible
  residual). `prj:frameOutput`/`prj:frameEffect` — split/consolidate are projections, reusing SP4's
  Frame coordinates. Exact `prj:*` spellings are PROVISIONAL until SP4 is reviewed in this batch (§6 Q0).

### Consumes — from SP7 (federation SHACL law, lower in the batch)
- **A certified-well-formed federated graph** — SP7 §5 produces exactly this. The `law:*` conformance
  (`conforms=True` over the federated SP1..SP8 graph) is SP9's **precondition**: `split` operates only
  over a graph SP7 has certified (Vol 30 "No contract, no crossing" — reassimilation only evaluates
  **contract-valid** rows). PROVISIONAL `law:*` spellings pending SP7 review (§6 Q0).

### Produces — for the higher workflows (named, consistent with the DAG)
SP9 is the **terminal W2 sub-project** (highest ordinal, no higher W2 sub-project consumes it); its
outputs feed W3/W4:
- **For W3 (`phase_w3_7` "Split↔Consolidated reversible render with digest certificates"):** the
  render-seal law + `seal:DigestCertificate` + `seal:Readback` structure is the **contract the W3
  render pipeline implements** — SP9 is the *ontology of the seal*, W3 is the executable renderer that
  must satisfy it (the `turtle_subject_aggregation` / `wave_barrier` contracts are its live predecessors).
- **For W4 (`phase_w4_6` "Sealed self-hosting closure gate (split/consolidate inverse digests)"):**
  the `seal:*` shapes + ASKs become the **blocking CI gate** run under the multi-engine ContractGate;
  the digest-certificate + readback teeth are the gate's pass/fail (readback-before-promotion, Vol 30).
- **For the whole federated graph (SP1–SP8):** SP9 is the reversibility **capstone** — the proof that
  the entire iteration's ontology round-trips split↔consolidate byte-identically, the DAG artifact
  `silm:artifact_render_pipelines` ("Split/Consolidated seal, artifact-free branch").

---

## 6. Non-goals (this iteration; YAGNI deferrals) & genuine open questions

**Non-goals / YAGNI.** Corpus-agnostic — pure shape, **zero corpus instances**; **no actual
split/consolidate executor, no real digest computation, no Scala one-file renderer** — those are the
W3 render pipeline (`phase_w3_5/6/7`) and the W4 gate (`phase_w4_6`). SP9 authors the *ontology of the
seal* (the disintegration/reassimilation pair, the reconstruction-receipt structure, the readback law,
the component account) with teeth at the type level, exactly as SP1 authors the floor and SP4 the
packet ontology. No materialization of the unary law's Scala **inner-class path-dependent**
consolidated projection (per-instance type distinction, cross-instance bridge) beyond *declaring* it
as a coordinate — its compilation and the compiler-observed nested type graph are the self-hosting
closure (W4/X). No per-value digest measurement (type-level certificate structure only; live
measurement is W5). No RDF dataset canonicalization algorithm choice implemented (declared as a
coordinate — Q3). No powerset/"every possible arrangement" materialization (explicitly forbidden by
the `local_encyclopedia` bounded-projection contract). Built to be challenged and relaunched, not
final (Directive 13).

**Open questions for the maintainer (Praeriehund — flagged, not invented):**
- **Q0 — SP4/SP7 handles (same batch), PROVISIONAL.** The `prj:reversible`/`prj:section`/`prj:LossClass`
  spellings (SP4) and the `law:*` federation-conformance handle (SP7) are forward references reviewed
  in this same batch; exact spellings PROVISIONAL, pinned once SP4/SP7 are reviewed. Also depends
  transitively on the SP2 AOB atom identity and SP3 CRS geometry (they enter the federated graph SP9
  seals) — PROVISIONAL until those land.
- **Q1 — which physical carrier does the v1 seal target?** The unary law + Helios describe **two**
  seals sharing one law: (a) the **TTL** seal — `split` = `basicttl/*.ttl` one-thing-per-file ↔
  `consolidate` = `ontology/silmaril-consolidated.ttl` (the JUNGLE's committed aggregate), which is
  precisely the `turtle_subject_aggregation` contract's `consolidate(split(g))==g` predecessor; and
  (b) the **Scala** seal — the source tree ↔ the one-file path-dependent inner-class projection. I
  model the law generically but the v1 witness graph must pick one. I lean **(a) the TTL seal**, since
  `basicttl` IS the ontology source, W2 is corpus-agnostic ontology, and Helios already ships (a) as a
  teeth-bearing contract; confirm.
- **Q2 — does `prj:self` (SP4 Q1) equal SP9's consolidated render?** If `self` = the consolidated
  single-file render, `prj:self` and `seal:consolidate` share one section witness and the two designs
  must name one node. Resolve with SP4-Q1.
- **Q3 — digest algorithm for topology/relationship equality.** Byte-revision equality is a straight
  **sha256** (SP1 tower `prim:Hash`). But *topology* and *relationship* equality over an RDF graph
  with blank nodes needs a **canonical labelling** (URDNA2015 / RDF Dataset Canonicalization) before
  hashing, else a lawful bnode relabel (SP4's `prj:StructuralLoss`) false-positives as drift. Is the
  v1 certificate's topology/relationship digest computed over a canonicalized graph (bnode relabel
  tolerated) or over raw bytes (bnode relabel = drift)? The unary law says "after a drift-free
  recapture," implying canonicalization; Vol 30's receipt is exact-arithmetic over declared inputs —
  genuine fork, confirm.
- **Q4 — Atlas↔consolidate / Graph↔split orientation.** I map **Graph view = split** (one-thing-per-
  file, drilled, the `basicttl/*.ttl` tree) and **Atlas view = consolidate** (the aggregate
  `local_encyclopedia`/`silmaril-consolidated.ttl`), matching the SP6 21-column Atlas ring as the
  aggregate surface. The unary law says only "the Atlas and Graph views may colimit each other through
  this pair" without fixing orientation; confirm the mapping (it sets which view is the
  `seal:frameOutput` of which projection).
- **Q5 — Q_A/Q_G carrier ownership (PIN-AT-WRITING-PLANS — do not resolve here).** Confirm with SP3
  that the disjoint `Q_A`/`Q_G` carriers live in SP3 (`crs/carriers.ttl`) and SP9/SP4 only project
  over them — a one-line confirm, not a fork.
