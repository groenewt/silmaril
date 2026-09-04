# W2 design constraints — maintainer depth directives (beacons, verbatim)

Carried forward from live maintainer guidance during W1. Transcript law: quoted
verbatim, then interpreted. Inferences are marked as inferences (Praeriehund
honesty — not asserted as the maintainer's words).

---

## Directive 1 — the AOB "sauce" (deep WIP AOBs + glossary polysemy)

> "please use our deep shacl, owl, rdf, sparql wip aobs from agents golden+r1_staging
> bc this is the depth we need (literally each fucking hexadecimal/serialized binary)
> aobed to ensure we understand everything which requires being so fucking subatomic
> ... this is the sauce bc shit gets whacky rq as you can tell from agents where we
> need to handle unstructured/and structured types synonymously but also as antonyms
> (its a brain fuck but also properly handled through the thorough mole of glossaries
> wherein we encapsulate/emerge distinct epistemologies)"

Binding W2 constraints:
1. **Ground the AOB meta-ontology in the REAL WIP AOB** authored in SHACL/OWL/RDF/SPARQL
   in `base_agents` golden + r1_staging. Do not invent an AOB shape; lift the existing one.
2. **Subatomic to the octet**: every hexadecimal / serialized-binary octet is itself
   AOBed — modeled as its own carrier/atom. This is the unary law's **byte-stream carrier
   closure** (bit/byte/octet as first-class Lambda byte-vector carriers with schema;
   Byte != Octet; width 1..128; stream -> block -> container -> value).
3. **Structured AND unstructured types held as synonyms AND antonyms simultaneously**,
   reconciled only through the **"mole of glossaries"**: each glossary encapsulates a
   DISTINCT epistemology; collisions are intentional (polysemy is literal; OSSIE mime is
   the anchor). The AOB/glossary layer must express one term as both synonym and antonym
   across different glossaries.

## Directive 2 — unary grammar, bit/byte/color vectors, JEPA, and the telephone twin

> "dont forget the whole urnary grammar as well as bit vectors and byte vectors and
> color n shit bc that is a later problem but will bite us in the ass if we forgoe it.
> Its basically the computational optimizations for jepa (still not software engineering
> but rather data engineering from which we properly handled our epistemological
> emergences) <<< the link betwen this and agents/telephone is 'hidden' through a twin
> mention but needs to become that tighter yoneda realization of ologs of ologs
> (turtles all the way)"

Binding W2 constraints:
4. **Do not forgo the unary grammar + bit-vector + byte-vector + color substrate.** Even
   though its full implementation is a *later problem*, the ontology shape authored in W2
   must leave first-class room for it: the URN/full-lexical-identity grammar (unary law),
   bit-vector and byte-vector carriers, and the color-channel code space (RGB -> Red/Green/
   Blue; cardinality 256; ordinal 0..255 — per the unary law's byte-stream closure).
5. These are the **computational optimizations for JEPA** (cf. `basicttl/06_topology_jepa.ttl`)
   — framed by the maintainer as **data engineering**, the substrate from which the
   epistemological emergences are properly handled (NOT software engineering).
6. **The telephone twin (inference — verify in W1 base_agents map):** there is a link
   between the byte/color substrate and `agents/telephone` (inferred: an agent gossip /
   message-passing mechanism — cf. the federation's GossipPreservesMittens and
   ReplicationConvergence theorems in `basicttl/03_silmaril_federation.ttl`) that is
   currently only *implied via a "twin mention."* W2 must make it explicit as a **tighter
   Yoneda realization of ologs-of-ologs** — recursive ologs (an olog whose objects are
   themselves ologs), "turtles all the way down" (cf. `forge/base` IV-turtles; RDF Turtle;
   `basicttl/olog_box.ttl`). The Frame is already "the Yoneda point" in the unary law; this
   asks that the telephone/substrate twin be realized at that same Yoneda tightness.

Status: Directive 6's concrete `agents/telephone` + "twin mention" location is being
captured now by the W1 base_agents deep-AOB agent; PROVISIONAL until that map lands.

---

## Directive 3 — the depth floor: subatomic dual-grounding ("what's a number")

> "Corpus agnostic shape with basic ttl depth remediation especially bc we literally
> have to be as anal as 'whats a number' (understand real, natural, imaginary as well
> as properly through the ISA/UEFI perspective BC DONT FORGET OUR 'base unit' is still
> bit and byte vectors ...)"  — maintainer, 2026-08-07

Binding W2 constraints (in addition to Directives 1–2):

7. **W2 scope = corpus-AGNOSTIC ontology shape + basicttl depth remediation.** No new-corpus
   binding in W2 (2 more gippidy corpuses, sparky/agent/BLS-notebook updates are incoming and
   we "will probably relaunch all later"); all live-corpus binding stays in a **re-runnable W5**.
   The basicttl depth remediation IS in W2 because it is cleanup of already-present corpus, not
   new-corpus binding — hence relaunch-safe.

8. **Every primitive is DUAL-GROUNDED — formal facet AND physical facet, simultaneously.**
   The remediation may not stop at a flat `xsd:` type. Worked example, "what is a number":
   - **Formal facet** — the full type-tower: **ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ**, plus **imaginary**; the ISA
     *of the mathematics* (Boolean, Char, etc. get their own towers). Not `xsd:integer` and done.
   - **Physical facet (ISA/UEFI lens)** — the same value as its exact-width machine type
     (**UINT8/16/32/64, INT8..64, float32/64** → IEEE-754 for reals, two's-complement for ints),
     with **bit-width, byte-vector layout, endianness**. UEFI exact-width types (UINT16 …) are the
     naming precedent; ISA is the operational/representation precedent.

9. **The base unit remains bit- and byte-vectors.** The dual-grounding descent bottoms out at the
   unary law's carrier closure — **Bit → Octet → ByteVector** (Byte ≠ Octet; width 1..128;
   stream → block → container → value; the RGB/256 colour code space). This floor is the JEPA
   computational substrate (Directive 2), authored ONCE as the shared primitive floor that every
   other basicttl concept grounds into by reference — not re-derived per concept.

Status: captured verbatim + interpreted this session; the interpretation (formal-tower + ISA/UEFI
machine-type + bit/byte floor, established once and referenced) is being confirmed with the
maintainer in the W2 brainstorming gate before any authoring.

### Directive 3 refinement — the taiji is a colimit; realization is monadic (maintainer, 2026-08-07)

> "TAIJI BUT LITERALLY Algebraically a colimit and TWIN OLOGS WITH REALIZATION FUNCTORS
> (extremely monadic)"

10. **The AOB primitive = the taiji = literally, algebraically, a COLIMIT** of the twin-olog
    diagram (Formal olog ⟷ Physical olog + the realization morphisms). Mutual-colimit (each facet
    a colimit involving the other; yin contains yang) — same shape as the unary law's Atlas & Graph
    colimit and the OSSIE YIN/YANG taiji twin. The atom simultaneously *is* its formal type and its
    physical encoding, glued at the realization — not two linked things, one colimit object.
11. **Twin ologs with realization functors, EXTREMELY MONADIC.** ρ: Formal → Physical is a
    **Kleisli arrow of a monad**, not a bare functor. Realizing ℝ→bytes carries an effect (float32
    vs float64 choice, IEEE-754 rounding, endianness) — which is EXACTLY the unary law's
    `Frame(output:X, error|effect:Y)`. So the realization monad ≡ the Frame monad: the depth floor
    and the unary law's Yoneda-point Frame are one structure. Byte-descent = Kleisli composition
    down to the Bit/Octet/ByteVector floor; unit = trivial realization; join = compose descents.

### Q3 ruling — decomposition approved; iteration-not-final (maintainer, 2026-08-07)

> "Approve and agnostic ... we will fundamentally challenge it anyway later so stay
> committed/oriented on completion on this 'iteration' of workflows"

12. W2 = 9 sub-projects (Primitive Floor → AOB meta-ontology → S/O/P CRS → projection packet
    → file+format taxonomy → glossary polysemy → SHACL law → basicttl depth remediation →
    render seal); each its own spec→plan→build. **Primitive Floor designed FIRST** (bottom-up).
13. This is THIS ITERATION's v1: it WILL be fundamentally challenged/relaunched later. Design
    for completeness-of-this-iteration and clean re-runnability, NOT for permanence. Stay oriented
    on COMPLETING the workflow chain; do not seek an unchallengeable final form. Corpus-agnostic
    throughout (no live-corpus binding until the re-runnable W5).

### Cadence ruling — batch the SP2–SP9 designs, one review (maintainer, 2026-08-08)

> "Batch designs, one review" — maintainer's answer when asked how much to steer each of
> the remaining 8 W2 sub-projects before building.

14. **SP1 (Primitive Floor) keeps its own full design gate** (already run; it produced the
    colimit/monadic/expand-the-towers rulings). For **SP2 (AOB meta-ontology) through SP9
    (render seal)**: do NOT open a separate brainstorming gate per sub-project. Instead, once
    SP1 is committed and green, author **short design docs for all 8 up front** (each still a
    real design — twin-olog/colimit/monadic grounding, file map, verification plan, interfaces
    Consumes/Produces, non-goals — just written without a per-project Socratic exchange), and
    present the whole batch for **one maintainer review pass**. On approval, write the plans and
    build straight through SP2→SP9, with the between-sub-project adversarial triple panel still
    firing after each build. One design checkpoint for the eight, not eight. The maintainer's
    design input is preserved (they review every design before any of the eight is built); only
    the per-project ceremony/interruptions are removed.

### Helios intake + the polysemy resolution of our own vocabulary (maintainer, 2026-08-08)

> "Polysemy!" — maintainer's answer when asked to resolve the "colimit" divergence
> (SP1 says "colimit taiji"; Helios's node-arrow monograph authors the artifact as an
> honest cocone W = ObservedProjection(ColimCandidate(D)), "not literally colim").

15. **The Polysemy Helios Library is the authored SOURCE-OF-TRUTH** (34 categorical papers,
    ~17k AOB atom yamls, source witnesses, executable specs/contracts). Added to the base
    submodule main; git-ignored under `/helios/` (maintainer resolves it into submodules).
    W2 designs LIFT its structures, never invent (Directive 1). It answers the cross-cutting
    decisions from the source: the agnostic **byte_order progenitor** (little/big/host/none
    children) + ISA/UEFI layer tower; **three independent S/O/P tower categories** K_S/K_O/K_P
    with NO positional maps to R/G/B and **disjoint Atlas/Graph carriers** (Q_A ∩ Q_G = ∅, a
    forgetful map, not a colimit); **load-bearing CCO/BFO** via `universal_anchors` (every node
    atom one `cco:ont########`, every arrow one `cceo:` process, resolved against the merged CCO
    2.x TTL, pattern-by-anchor never inline); the **full projection family** `triad_fibration`
    (7 render legs × 3 fibres) + Vol 06's five carrier projections + an nth-dim loss progenitor
    tree; the **telephone twin** (`telephone_events` + `telephone_supervision_tree`, fields
    pinned to Layer-0 anchors = Yoneda-point tightness); and the `_aob_*` atom envelope to lift.

16. **Our own vocabulary is subject to our own polysemy law.** The "colimit" divergence is NOT
    resolved by earning-vs-renaming-vs-deferring — "colimit" is a **polysemous term** whose sense
    is **glossary-scoped**, and the mole-of-glossaries (SP6) carries it reflexively:
    - **local / per-primitive glossary:** the finite two-object twin-olog gluing IS a genuine
      colimit — its universal property is provable — so SP1 EARNS the word there via a
      `q_colimit_universal` tooth (teeth-not-trust; enrich-not-strip).
    - **corpus / artifact glossary:** the same lexeme denotes `ObservedProjection(ColimCandidate)`
      — the monograph's honest cocone — which is SP9's sense.
    - **SP6 holds "colimit" as one lexeme with both glossary-scoped senses simultaneously**, with
      a biting polysemy tooth, exactly as Directive 1 requires for every polysemous term. SP2/SP6
      reference "colimit" through the glossary layer, not bare; SP9 keeps the honest-cocone sense.
    The SP1 universality tooth (D1), the frame-sort fence (D2), and the corrected Atlas/Graph
    analogy (D3) are the SP1↔Helios reconciliation items; D4 (independent S/O/P towers) is already
    faithful. Whether D1–D3 land now or at the W2 relaunch (Directive 13) is a build-time call.

17. **Be MORE agnostic/progenitor in definitions — on ALL of them** (maintainer voice, SP3
    Q3 ruling, general going forward). Whenever a concept has variants, do NOT mint the bare
    concrete case and do NOT privilege one variant: mint an **agnostic progenitor parent that
    grounds nothing** + explicit **composable children**, symmetric across the variants — the
    `byte_order` progenitor pattern applied everywhere. "Do all" + "not crammed" + "no reductive
    either/or" simultaneously. This resolves the **SP3 open questions (Q0–Q4)**, recorded here as
    gospel for the build:
    - **Q0 (pinned from committed SP2):** SP3 coordinatises `aob:AOBAtom` (→`aob:ConcreteAnchor`/
      `aob:YonedaHomLeg`); value bridge `aob:aobValue → prim:Primitive`; content address is the
      **class** `aob:HashDigest` reached via `aob:hasHashDigest` (32 `prim:Octet`, with
      `aob:zSeed → prim:Uint16` already materialised); S/O/P triple = `aob:sourceNodeUrn` (S) /
      `aob:targetNodeUrn` (O) / `aob:cpoProcessIri` (P), all `xsd:string` full-lexical — **SP3
      bridges string→`prim:URN` itself** (does not expect SP2 to hand typed URN objects).
    - **Q1 + z byte-order (maintainer choice: agnostic progenitor, no leaf):** SP3's `z`
      derivation types its byte-order coordinate at `aob:ByteOrderProgenitor` with **no** concrete
      `little/big/host` child committed in this corpus-agnostic v1; concrete endianness is deferred
      to the consumer at the re-runnable W5. `z` is pure-shape (no numeric value yet); SP2's
      already-materialised LE `aob:zSeed` is the eventual `byteOrderLittle` realisation that
      composes **under** the progenitor. `none` is NOT the default (it means "ordering not
      applicable / single-octet", a category error for a 2-octet `z`); `big` is rejected (no floor
      basis — SP1 `prim:Uint16` is LE). SP3 must author a `z`-local grounding allowance so the
      deliberately-ungrounded progenitor is accepted (SP2's `TensorByteOrderShape` demands a
      grounded child; SP3's `crs:ZGroundingShape` permits the agnostic parent as the v1 default).
    - **Q2 (lifted from Helios):** `crs:hasDimension` counts **tower-axes** (`crs:hasAxis` arity),
      never scalar ordinals — the scalar reading is the forbidden positional-collapse. The S-O-P
      role geometer is dimension 3 (three tower projections). Each counted axis is a URN tower
      (`crs:AxisUrnTowerShape`); the per-geometer axis-arity dimension is kept DISTINCT from each
      tower's own internal nth.
    - **Q3 (maintainer choice: do all, be more agnostic — no privilege):** an agnostic
      `crs:PlaneGeometer` progenitor (dim 2, grounds nothing) with **all** planes minted as
      composable children — `crs:HoneycombPlaneGeometer` (x,y, source-attested) +
      `crs:GeographicPlaneGeometer` (lon,lat, SP1 `prim:CRS`/`prim:Latitude`/`prim:Longitude`) +
      an agnostic `crs:RolePairProjectionPlane` sub-progenitor carrying the **full symmetric**
      role-pair family (S,O)/(S,P)/(O,P), each a lawful `π`-projection off the rank-3 S-O-P role
      geometer (each drops one role — a documented SP4 loss). No role pair is privileged; the
      S-O-P role geometer stays a rank-3 sibling. This dissolves the D1 asymmetry worry by making
      the role-pair plane a symmetric composable family, not a special-cased (S,O).
    - **Q4 (lifted from Helios):** SP3 does **NOT** model χ (a cross-*framework* map `Ob(K)→W` to
      an external `.yur` proposal tuple, declared unsupplied in the source) and models **no**
      Atlas↔Graph transition/hom — carrier disjointness (`Q_A∩Q_G=∅`, no cross-tag hom) + the
      many-to-one forgetful tag-erasure Frame is the complete v1 Atlas/Graph story. χ is recorded
      only as an **honest-red deferral marker** (an `rdfs:comment`/annotation naming it a deferred
      obligation to SP4/W5, no component map, no tooth). SP3 keeps the **internal** product
      projections `π_j: K→K_j` (in scope, the joint-faithfulness seal) distinct from the
      **external** χ (deferred).

18. **Ontology-first means anchored on ALGEBRA, and algebra itself anchors on SET THEORY**
    (maintainer voice, verbatim: *"we need everything to be ontology first — or more precisely we
    anchor on algebra (the css and html artifacts are violations but this should be realized within
    your workflow as is!) `<<<<` Set theory (magma → abelian groups and all in between, as well as
    space constructs!)"*). This is the foundation the whole ontology stands on:
    - **The anchor stack (bedrock → surface):** **Set theory** (sets, elements, functions,
      relations, products/coproducts/disjoint unions, power sets, ordinals/cardinals) — *including
      the* **space constructs** *(topological / metric / vector / normed spaces)* — is the deepest
      anchor. **Algebra** sits ON set theory: the full **magma tower** `Magma → Semigroup → Monoid
      → Group → AbelianGroup` with **"all in between"** as first-class citizens (Quasigroup, Loop,
      CommutativeMonoid, and the semiring/ring/module/field line where a corpus needs it), each its
      own atom under an agnostic progenitor (Directive 17), NEVER crammed. **Everything else** —
      SP1 primitives, SP2's AOB (its `group_law` sealed group IS a group in this hierarchy), SP3's
      CRS carriers/towers/products (a byte-vector carrier is a monoid under concatenation; the
      five-factor `K` is a product; the role towers are graded structures), and onward — **grounds
      in this algebraic–set-theoretic foundation.**
    - **A foundational floor must exist and be anchored to.** The algebra/set-theory foundation is
      an explicit floor that sits **beneath** SP1 (or beside it as the deepest ground) and that
      SP1/SP2/SP3 **re-anchor onto**. It gets its OWN superpowers design gate (brainstorming HARD
      GATE) — its depth (how far the set-theory + algebra + space hierarchy goes for v1), and the
      **sequencing** (re-anchor the existing floors after it lands vs. rebuild on it) are that
      gate's central questions, resolved with the maintainer, LIFTED from the Helios categorical
      papers (34 `.tex`: sheaf/semiring/lens/category-theory foundations), never invented.
    - **CSS/HTML (and hand-authored render) artifacts are VIOLATIONS.** They violate the
      ontology-first / algebra-anchored law (hardcoded, not derived from the ground). The workflow
      must **REALIZE them as violations** — surface and model them AS violations in the ontology
      (the active-RED state), never legitimize or hardcode them. W3 (render seal, artifacts
      generated-not-committed) and W4 (blocking CI) are where the violation is driven RED→GREEN;
      until then it is named honestly, not hidden.
    - **Immediate application:** SP3 finishes on the SP1/SP2 grounding as planned (auto-resume after
      the Aug-10 usage reset); its panel now also checks that its carriers/towers/products/groups
      are **algebra-SHAPED and ready to re-anchor** (magma/monoid/group-recognizable) and that no
      render artifact is legitimized. The algebra/set-theory foundation is then the **next
      design-gate sub-project**, after which SP1–SP3 re-anchor onto it.

19. **The foundation's FOURTH pillar is FUNCTIONALITY / TYPING over COMBINATORY LOGIC — the
    Frame IS Curry's functionality** (maintainer-supplied source: H. B. Curry, *First Properties
    of Functionality in Combinatory Logic*, Tôhoku Mathematical Journal **41** (1936) 371–401;
    jstage `tmj1911/41/0/41_0_371`. CITE it, do NOT commit the PDF — the mathematics is fact and
    liftable; the journal scan is not ours to redistribute). Directive 18's stack (set theory →
    algebra tower → space constructs) is INCOMPLETE without the arrow/typing layer, and this paper
    supplies it:
    - **Functionality `F` = the Unary Frame.** Curry's `⊢ FXYZ` ("Z is a function from X to Y",
      X/Y categories) is exactly `F(x) → Frame(output:X, effect:Y)`. The foundation carries a
      **functionality/typing pillar** — the algebra of typed ARROWS — over the **combinatory-logic
      substrate** (the combinators B, C, W, K, I; `F_n` for n-ary functions; the `Γ_m·B…`
      compositor), which IS the closed-λ "Lambda"/Sparky engine the corpus already names
      (Lambda-Blotto). Point-free / variable-free = the unary law's "no free variables, closed
      terms". Set theory carries the CARRIERS, the algebra tower the OBJECTS/OPERATIONS, this
      pillar the ARROWS; "the Frame is the Yoneda point" = "the Frame is Curry's F applied".
    - **Subtyping variance (Curry §4).** `FXY` with `U⊆X` and `Y⊆V` ⟹ `FUV` — CONTRAVARIANT in
      the domain, COVARIANT in the codomain (axioms `(FP)₁`,`(FP)₂` via inclusion `P*`/`⊃`). The
      function-type algebra MUST carry this variance; it is the law SP1's ρ-functor-on-subtyping-
      arrows (`RealizationTransport`, functor identity/composition) re-anchors onto.
    - **Functionality ↔ implication = a taiji (Curry §5, Curry–Howard ancestor).** `F` is
      DEFINABLE as `F' ≡ [x,y,z](u)(xu ⊃ y(zu))` — a function type is a universally-quantified
      implication; Thm 5.8 shows every F-theorem holds for `F'` given the K/C/W implication laws.
      Types-as-propositions is ONE lexeme with two glossary senses (Directive 16 polysemy), not two
      layers: the arrow pillar and the logical-implication layer are the same object.
    - **Paradox quarantine by type discipline (Curry §6).** The Russell contradiction
      (`E≡WQ`; `χ≡[f]N(ff)`, `⊢χχ=N(χχ)`) rests on a tacit, "not even plausible" assumption about
      the functional character of negation — i.e. it arises ONLY from applying functionality
      OUTSIDE its proper category. Type/functionality discipline is the quarantine. This is our
      ContractGate branching-quarantine + Praeriehund provisional-naming + the "a category is a
      useful servant, dangerous master" warning (srcy paper 41 cheese/progenitor); the foundation
      must make self-application type-disciplined, never naively self-applicable.
    - **Design-gate consequence:** the algebra/set-theory foundation design gate (Directive 18) now
      has a functionality/combinatory-logic pillar as a co-equal fourth strand; its synthesis +
      maintainer decisions must cover how the arrow/typing layer is lifted (Curry's F + B/C/W/K/I,
      the §4 variance, the §5 implication taiji, the §6 quarantine) and how SP1's Frame/ρ/Yoneda
      apparatus re-anchors onto it.

20. **FOUNDATION DESIGN-GATE RESOLVED (SP0 — the deepest floor `basicttl/foundation/`).** After the
    four-pillar research (ledger/W2/algebra_foundation/00–06) the maintainer chose **MAXIMAL depth,
    all teeth-proved** across every pillar (overriding the synthesis's YAGNI lean — completeness is
    the mandate). Gospel for the build:
    - **Algebra tower (all teeth-proved):** the FULL spine `Magma → Semigroup → Monoid →
      CommutativeMonoid → Group → AbelianGroup` PLUS the two-operation line `Semiring → Ring →
      Field`, PLUS `Quasigroup / Loop`, PLUS `Module / VectorSpace` — every rung an agnostic-
      progenitor `(Σ,E)` presented-algebra atom minted through the LIFTED free⊣forgetful engine
      `F_E(X)=T_Σ(X)/≡_E`, each adding exactly one law, NEVER crammed (Directive 17), each with a
      genuine biting SHACL tooth (probe injection).
    - **Spaces (all teeth-proved):** `TopologicalSpace (X,τ)`, `MetricSpace (X,d)`, `VectorSpace`,
      `NormedSpace`/`InnerProductSpace` authored NOW as teeth-proved atoms, ALONGSIDE the LIFTED
      Site/sheaf + `𝔗_f` finite space + the non-Riemannian partition theorem.
    - **Functionality (all teeth-proved):** the full combinator family `B/C/W/K/I` + the n-ary
      `F_n` ladder (Def 2.1) + the `Γ` compositor as an agnostic-progenitor family, teeth-proved;
      the Frame RECOGNIZED as Curry's `F` (not rebuilt); the §4 variance carried via a separate
      `F(dom,cod)` bifunctor with CONTRAVARIANT-domain teeth (the covariant codomain reuses SP1's
      proved `RealizationTransport`; the unary-law input-coordinate collision becomes an SP6
      polysemy tooth).
    - **Logic (full sub-floor):** a proposition/negation/implication stratum `P_r / N / ⊃` + proof
      terms (the K/C/W implication laws), teeth-proved — complete Curry–Howard; the
      functionality↔implication taiji is one lexeme with two glossary senses (Directive 16).
    - **HONESTY (Praeriehund, load-bearing):** only **Monoid**, the **minting engine**, the
      **agnostic-progenitor pattern**, **Site/sheaf + 𝔗_f**, and structural **Set** are LIFTED from
      Helios. Every rung above Monoid, the two-operation line, quasigroup/loop, module/vector, ALL
      point-set spaces, the combinators/`F_n`, and the logic floor are **SYNTHESIZED as cited
      standard-mathematical fact** (the Directive-19 Curry precedent: math is fact and liftable, cite
      the source, do not pretend it is a Helios lift). The group **inverse law** is the one axiom
      with zero Helios basis — authored as cited math fact. Every atom carries a `DS`/`PD`/`SYN`
      authority tag; SYN atoms are honest-red where a v1 consumer is absent but STILL teeth-proved
      per the maximal choice. The corpus's *refusal* of point-set topology (`19/05/03`) is recorded
      as the reason those space atoms are SYN, not LIFTED.
    - **PINS adopted:** framing = taiji-via-engine; position = new deepest floor `basicttl/foundation/`
      BENEATH SP1; re-anchor = ADDITIVE (`foundation:groundsIn*` edges, rebuild nothing — 15/16
      points additive; the one real build is `aob:SealedGroup`→`foundation:Group` teeth-proven, with
      SP2 SealedGroup a CHILD of a fresh agnostic `Group` progenitor); set floor = structural/ETCS
      consolidating SP1 (material/ZFC set theory = honest-red deferral); external appendix-39
      `compass_artifact` space survey = reference-only (cite, never author-from). Functionality is a
      co-equal fourth pillar under the same floor.
