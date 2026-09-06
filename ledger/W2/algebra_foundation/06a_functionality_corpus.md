# 06a — FUNCTIONALITY / TYPING / COMBINATORY-LOGIC corpus map (Directive 19, the fourth pillar)

> Präriehund honesty banner. This is a W2 brainstorming-gate RESEARCH note for the FOURTH
> foundation pillar (Directive 19, `ledger/W2/design_constraints.md:263-299`): the algebra of
> typed ARROWS / functionality `F` over a combinatory/λ substrate, the co-equal strand that
> completes Directive 18's set-theory → algebra-tower → space stack. It maps, with exact
> `file:line` evidence, what the authored Helios source-of-truth (`helios/srcy/`, git-ignored)
> and the committed floors (`basicttl/`) ALREADY carry toward Curry's functionality, and where
> the genuine GAPS and maintainer decisions are. It authors NOTHING in `basicttl/`, runs no
> git, and decides nothing. Every structural claim is tagged **LIFTED** (present in a named
> Helios/basicttl `file:line`), **SYNTHESIZED-FROM** (extended from a named source or the
> maintainer-supplied Curry 1936 extract — honest `SYN`), or **GAP** (pure invention → flagged
> hard, Präriehund). Consistent with `00_synthesis.md`'s framing (taiji-via-engine,
> agnostic-progenitor, DS/PD/SYN honesty machinery). The Curry source (H. B. Curry, *First
> Properties of Functionality in Combinatory Logic*, Tôhoku Math. J. **41** (1936) 371-401;
> jstage `tmj1911/41/0/41_0_371`) is **CITED, never committed** — the mathematics is fact and
> liftable, the journal scan is not ours to redistribute (Directive 19).

---

## 0. One-paragraph verdict (lift-vs-gap, brutally honest)

The corpus authors the **arrow/typing layer richly and provably** — but as **named-variable
typed λ-calculus with an explicit unary Frame codomain**, NOT as Curry's variable-free
combinatory logic. Curry's functionality `F` (`⊢FXYZ` = "Z is a function from X to Y") is
**already present three ways, all committed or authored**: (i) as the **unary Frame law itself**
(`T → Frame(output:X, effect:Y)` = `F(x)→Frame(output:X, effect:Y)`, the maintainer's Directive-19
identity, materialized as `prim:Frame prim:isYonedaPoint true`); (ii) as the categorical
**exponential object / internal-hom** `B^A` with the currying universal property (whitepaper
limit-colimit zoo); (iii) as the **adjoint transpose** `Hom(LG,A)≅Hom(G,RA)` (paper 26). The
**closed-λ "Lambda"/Sparky engine** the maintainer names is authored in full: paper 33's
**Lambda-Term Graph Ontology** types the one β-step as a unary Frame arrow, and the shared
`lambda_blotto_model.tex` fixes the closed lambda term (`FV=∅`), the Frame carrier, and Sparky's
**map-shuffle-reduce** motion. Curry §4 **subtyping variance** (contravariant domain / covariant
codomain) is authored as the hom-iso's "natural in G [contravariant] and A [covariant]" and
re-derived in the committed floor as `ρ` **a functor on subtyping arrows** (`RealizationTransport`,
`q_functor_identity`/`q_functor_composition`). Curry §6 **paradox quarantine by type discipline**
is authored as the corpus's **ill-typed-object refusal** (a bare string is a *typing failure*,
not an inference), the **Prairie-Dog provisional-naming** classifier (cited from the Präriehund
doctrine doc by sha256), the **institutional-category-machine** fixed-point countermodels ("the
risk that compartmentalization becomes rational mastery" = the category-as-dangerous-master), and
the **fuel-bounded** β-reducer (unbounded self-application/`Y` kept OUT). **The genuine GAPs are
narrow but real: (1) the combinators B/C/W/K/I / SKI / bracket-abstraction are ABSENT — the
corpus is a λ-calculus corpus, not a combinatory-logic corpus (`Y` appears ONLY in the external
appendix-39 mirror); (2) Curry §5's functionality↔implication taiji / types-as-propositions
(Curry-Howard) is NOT authored — the exponential is a categorical internal-hom, never identified
with logical implication; (3) `F_n` n-ary functionality and the `Γ_m·B…` compositor are absent
as such.** Net for the gate: this is **not** a "lift combinatory logic" project; it is a "**the
Frame IS Curry's F — recognize/consolidate the already-authored typed-arrow + λ-engine + variance
+ quarantine, and decide whether the B/C/W/K/I substrate + the §5 implication-taiji are minted or
declared honest-red**" project.

---

## 1. Functionality `F` = the typed arrow — where the corpus ALREADY carries it

Curry's `F`: `⊢FXYZ` means "Z is a function from X to Y", X/Y categories; `F` is a PRIMITIVE
typing/arrow operator. Directive 19: this IS `F(x)→Frame(output:X, effect:Y)`. Three authored/
committed realizations:

### 1.1 The unary Frame law IS Curry's `F` (LIFTED — committed floor + governing law)
- **Law text:** `T -> Frame(output: X, error|effect: Y)` — "the typed product required to construct
  a frame around a byte stream … The frame is the **Yoneda point** at which the callable's one
  observed input maps to its output and typed effect."
  `docs/unary-byte-frame-law.md:28-38` (LIFTED). The input/output/error are "separately navigable
  coordinates" — exactly Curry's X (domain category), the codomain, and the effect. This is the
  maintainer's Directive-19 identity **stated in the governing law**, predating the Curry cite.
- **Committed materialization:** `prim:Frame prim:isYonedaPoint true`, teeth-checked by
  `q_yoneda_point` ("the Frame **is** the Yoneda point … must carry `prim:isYonedaPoint true` and
  must NOT also carry `…false`") — `basicttl/primitives/primitives.queries.sparql:471-496`;
  `basicttl/primitives/README.md:166`. The Frame is the product `Frame(O,E):=O×E` (frame-sort §06,
  per `srcy_map.md:153`). LIFTED (committed, teeth-green).
- **Curry map (SYNTHESIZED-FROM the extract):** `⊢FXYZ` with Z the callable, X the input carrier,
  Y the codomain — the corpus's `T` is the domain X, the `Frame(output,effect)` is the (codomain ×
  effect) Curry folds into "function from X to Y". The **effect coordinate** is a genuine Helios
  *enrichment* of Curry's bare F (Curry has no effect slot); it is the ρ-monad's Kleisli effect
  (§1.4, `00_synthesis.md` D3 monadic-realization). SYN — faithful extension, flag as enrichment.

### 1.2 The exponential object `B^A` = internal-hom / function type / currying (LIFTED — thin)
`helios/srcy/base/00_whitepaper/sections/13_limit_colimit_zoo/20_exponential_object.tex`:
- title `B^A` = "internal hom from A to B"; `\silSetActiveContext{exponential object;
  cartesian-closed; currying}` (`:1-3`).
- **Universal property (currying) authored verbatim:** "maps `X×A→B` correspond to maps `X→B^A`"
  (`:6-7`), with the `eval` arrow and the unique transpose `f̄` in a commuting triangle (`:11-19`).
  This is EXACTLY Curry's F as a categorical object: `B^A` is the object of functions A→B, and
  currying `X×A→B ↔ X→B^A` is the adjunction Curry's `F_n` compositor generalizes.
- **Honesty tooth:** "Forbidden collapse: exponential = function-space." (`:23`) — an SP6 polysemy
  tooth: `B^A` is the *internal* hom, not naively "the set of functions".
- **Coverage is THIN (Präriehund):** grep shows the exponential/internal-hom/cartesian-closed
  material is concentrated in this **single zoo entry** (14 hits) + its spec-atom siblings + the
  node-arrow monograph (7) + `lambda_blotto_node_arrow_engine` (6) + one `functor_categories`
  mention. There is **no developed cartesian-closed-category theory**, no `eval`/`curry` as
  reified arrows in `basicttl/`, no exponential atom committed. So `B^A` is **LIFTED as a
  definition** but must be **SYNTHESIZED as a first-class typed-function atom** if the pillar wants
  it teeth-bearing.

### 1.3 The adjoint transpose = currying's categorical engine (LIFTED — richly proved)
`helios/srcy/papers/26_adjunctions_free_graphs_governed_algebras/chapters/01_hom_set_adjunction/`:
- **Hom-iso** `φ_{G,A}: Hom_GovAlg(LG,A) ≅ Hom_Graph(G,RA)`, "natural in G [**contravariant**]
  and A [**covariant**]" — `sections/01_hom_iso_definition.tex:20-27` (`thm:26-c01-hom-iso`,
  proved via triangle identities `:104-171`). This is the **curry/uncurry** correspondence at the
  free⊣forgetful level: `f ↔ f̄`.
- **Transpose correspondence** `f↔f̄`, mutually-inverse bijections
  (`sections/02_transpose_correspondence.tex:59-71`, `thm:26-c01-transpose`); "the bar is not a
  rename … two artifacts in two different categories" (`:113-117`); forbidden collapse "Bar ≠
  rename" (`:150`). This is the honest-typed currying: `f̄` (curried) is a genuinely different
  typed object from `f` (uncurried), the same discipline Curry's `F` enforces.
- LIFTED (proved, `PD`). This is the corpus's deepest currying anchor — an *adjunction* transpose,
  more general than the bare `B^A` exponential.

### 1.4 The committed floor ALREADY carries `F` as ρ-a-functor-on-arrows (LIFTED — the re-anchor surface)
`basicttl/primitives/` (SP1), which Directive 19 says "SP1's Frame/ρ/Yoneda apparatus re-anchors
onto":
- **Typed subtyping arrow** `prim:SubtypeArrow` (`prim:arrowDom`, `prim:arrowCod`) — the reified
  typed arrow `A⊂B`, 59 generators; `prim:IdentityArrow` (60), `prim:CompositeArrow` (45), thin
  category. `basicttl/primitives/README.md:45,96`; `formal.ttl:322-330`. This IS the arrow layer
  Curry's F types.
- **`ρ` as a functor on arrows** `prim:RealizationTransport` (`transportOf` a FormalArrow,
  `transportDom/Cod`, `isTransportIdentity`, `transportComposeFirst/Second/Into`) — the ρ-functor-
  on-subtyping-arrows the Directive-19 brief names as "the §4 variance carrier".
  `primitives.queries.sparql:261-278`; `README.md:54,98`. Curry §4 variance re-anchors here (§3).
- LIFTED (committed, teeth-green). **This is the primary re-anchor surface for the pillar.**

---

## 2. The closed-λ "Lambda"/Sparky engine (LIFTED — the combinatory substrate, but λ not CL)

The maintainer names "the closed lambda term", the "Lambda"/Lambda-Blotto engine, and "Sparky
map-shuffle-reduce". All authored:

### 2.1 The Lambda-Term Graph Ontology — typed λ with a unary-Frame β-step (LIFTED — proved)
`helios/srcy/papers/33_yoneda_generalized_ontology/chapters/08_lambda_term_graph_ontology.tex`:
- **Grammar** `t ::= g | x | λx.t | t t` (`:24-28`) — ground, variable, abstraction, application.
  "Makes lambda calculus the explicit **motion language** of the stateless graph machine" (`:16`).
- **The closed lambda term** = `ClosedTerm` = "terms paired with environments that resolve every
  free variable" (`:39-45`) — the maintainer's "closed lambda term". Re-stated in
  `lambda_blotto_model.tex:26-31` as `FV(close_ρ(t))=∅` (LIFTED).
- **The β-step IS Curry's functionality-shaped arrow (the unary Frame):**
  `β₁: LambdaStepInput → Frame(output: ClosedTerm×Fuel×StepReceipt, effect: TypedIssue)`
  (`:53-62`). Literally `T → Frame(output:X, effect:Y)` applied to λ-reduction — the strongest
  single confirmation that the corpus's λ-engine already types its arrows as Curry's `F`.
- **Capture-avoiding substitution** (α-rename before β), scope-graph freshness proof, trace edge
  (`:67-108`) — the disciplined substitution Curry's type discipline requires.
- **β-motion result-and-history monad** `T_β(X)=(X+I_β)×H_β`, Kleisli bind, three Kleisli laws
  proved (`thm:33-beta-result-history-monad`, `:220-285`); "extreme monad" = the extremal-epi
  specialization (`:341-361`). Ties the λ-engine to the ρ-monad/Kleisli layer (SP1
  `KleisliCompositionShape`). LIFTED (`PD`).
- **Fuel-bounded motion theorem** (`thm:33-fuel-bounded-motion`, `:436-464`): every β-run
  terminates in ≤n steps or returns `FuelExhausted` — the corpus's **quarantine of runaway
  self-application** (§4). "termination does not prove confluence, normalization without a fuel
  bound, or semantic equivalence" (`:466-471`) — honest teeth.

### 2.2 The Lambda-Blotto engine + Sparky map-shuffle-reduce (LIFTED)
`helios/srcy/shared/components/math/lambda_blotto_model.tex` (shared carrier for every occurrence):
- Header: "Discrete Colonel Blotto supplies its finite hard-budget state … eigenvalues/
  eigenvectors supply revision-bound modal coordinates … **typed lambda reduction advances that
  same game state**" (`:1-7`). So "Lambda" = the three-coordinate engine (Blotto game + spectral +
  typed-λ-reduction); the λ half is the functionality/typing motion. LIFTED.
- **Sparky map-shuffle-reduce**: `\LBSparkyGreenfieldMachine` = `(parse/chunk, CPG/AST, map,
  shuffle, reduce, plan, schedule, execute, refine, lift)` (`:629-638`); the **epochal
  map-shuffle-reduce motion law** `\LBSparkyEpochMotion` (`:640-652`); the Sparky chunker is itself
  a **unary Frame arrow** `chunk_Sp: ChunkInput_f → Frame(output:C_f, effect:Issue)` (`:619-627`).
  Sparky = the map-shuffle-reduce evaluator whose every stage is a Curry-F-typed arrow. LIFTED.
- The Frame carrier `𝔽=(F,⪯,succ,ρ,parent,kind,meta)` with a full lawful poset/lineage algebra
  (`:220-378`) — the native-Frame time carrier the β-step and Sparky stages live in. LIFTED.
- Named engine chapter: `base/00a_node_arrow_corpus_spine/chapters/08_lambda_blotto_node_arrow_engine/chapter.tex`
  — "Lambda Blotto as the Discrete Allocation Engine", Sparky's chunker as the internal entrance,
  map-shuffle-reduce epochs, Wingtip scheduler (`:10-48`). LIFTED (this is the "engine" the brief
  highlights).

### 2.3 Point-free / variable-free / combinators B,C,W,K,I / SKI — **GAP (the sharp one)**
- The unary law's "no free variables / closed terms" = **closed λ-terms** `FV=∅` (§2.1), which is
  *closure*, NOT *point-free-ness*. The corpus's engine uses **named variables + explicit
  environments + capture-avoiding α-renaming** (paper 33 §2.1) — this is named-variable λ-calculus,
  the OPPOSITE of Curry's variable-free combinatory logic.
- **Grep for `combinator`, `SKI`, `bracket abstraction`, `B,C,W,K` across all of `helios/srcy`:
  the combinators B/C/W/K/I are ABSENT from the authored 34 papers.** The ONLY combinator hits are
  the **Y combinator in the external appendix-39 mirror** (`.../self_reference_key_definition_v3.spec.yaml.tex:139-145`,
  `base_worlds_dump_definition_v1.spec.yaml.tex:139-145`: "The Y Combinator (Lambda Calculus Fixed
  Point) … produces self-reference from NON-self-referential parts") — a **copied external research
  artifact**, not authored theory — and one Elixir code path
  `.../telephone/effect/combinator/core.ex` in `references.bib:766` (a source-witness URL, not
  math). So:
  - **B/C/W/K/I, SKI, bracket/abstraction elimination = GAP** (no Helios authored basis).
  - **`F_n` (n-ary functionality, Def 2.1) and the `Γ_m·B…` compositor = GAP** as such; the corpus
    achieves multi-arg via curried λ / product carriers (`LambdaStepInput = ClosedTerm × Fuel`,
    the Frame product `O×E`), not via a combinator compositor.
  - **DECISION D-F1 (maintainer):** does v1 mint the B/C/W/K/I combinator basis + bracket
    abstraction as agnostic-progenitor atoms (Directive 17) grounding the λ-engine, or declare them
    honest-red and keep the **named-variable λ-calculus as the authored substrate**, with Curry's
    F lifted at the *functionality/exponential/transpose* level (§1) and the combinators recorded
    as a cite-only Curry reference (like the Curry PDF itself)? Präriehund read (inference, not the
    source's word): the authored substrate is λ not CL, so combinators are the pillar's largest
    genuine invention; the faithful path is to lift **F + variance + the λ-engine + the quarantine**
    (all authored) and treat B/C/W/K/I as a *cite-able Curry orientation*, minting only if a
    consumer needs point-free normal forms (none currently does — YAGNI, cf. `00_synthesis.md` D-B).

---

## 3. Subtyping variance (Curry §4) — LIFTED (contravariant domain / covariant codomain)

Curry §4: `FXY` with `U⊆X`, `Y⊆V` ⟹ `FUV` — contravariant in domain, covariant in codomain
(axioms `(FP)₁,(FP)₂` via inclusion `P*`/`⊃`). Directive 19: the function-type algebra MUST carry
this; it is what SP1's ρ-functor-on-subtyping-arrows re-anchors onto. Authored:

- **The variance is stated verbatim at the hom-iso:** "natural in `G` [contravariant] and `A`
  [covariant]" — `26/.../01_hom_iso_definition.tex:27` (`prin:26-c01-hom-iso`) and the naturality
  markers `:187-202`. `Hom(-,A)` contravariant, `Hom(A,-)` covariant. LIFTED (proved).
- **The two-sided Yoneda hom-profiles = the incoming/outgoing functionality profiles** (paper 13 +
  paper 33): `Hom(-,X)` (incoming, contravariant) and `Hom(X,-)` (outgoing, covariant); "to model
  an object categorically is to know it by admissible arrows" (paper 33, per `srcy_map.md:117`).
  `y(A)=Hom_C(-,A):C^op→Set` covariant embedding, `Nat(yA,B)≅Hom(A,B)` — the Yoneda point law
  (whitepaper §04, per `srcy_map.md:138`; `00_synthesis.md` 01 §1.6). The contravariant/covariant
  split is authored as the corpus's incoming-vs-outgoing sous-profile law (whitepaper §04 sous
  profile). LIFTED.
- **Committed floor:** `ρ` is a **functor on subtyping arrows** — `q_functor_identity` ("ρ
  preserves identities, ρ(id_A)=id on ρ(A)") + `q_functor_composition` ("ρ(g∘f)=ρ(g)∘ρ(f)") +
  `q_functor_composition_total` (coverage) via `prim:RealizationTransport`.
  `primitives.queries.sparql:288-289,312-313,524-548`; `README.md:154-174`. Directive 19 names this
  the §4 variance carrier: `RealizationTransport` transports each `SubtypeArrow` (a `⊆`/inclusion)
  and preserves identity + composition — **functoriality is the machine form of Curry's variance
  monotonicity**. LIFTED (committed, teeth-green).
- **Legacy glossary trace:** `basicttl/_verb/*/functor_antonym_contravariant_functor.ttl` (present
  in every paper's `_verb/`), `_verb/18_presheaf_semantics/covariant_antonym_contravariant.ttl`,
  `presheaf_synonym_contravariant_set_functor.ttl`, and a whole `03_contravariance_violation*`
  family — the corpus already carries contravariance/covariance as SP6-style glossary
  synonym/antonym atoms (legacy `_verb/`, not the green floor, but corpus-authored). LIFTED (as
  glossary material).
- **Präriehund note:** what is **LIFTED is functorial variance** (preserve id/∘, contravariant vs
  covariant hom); what is **SYNTHESIZED-FROM Curry** is the specific *subtyping* reading `U⊆X,Y⊆V ⟹
  FUV` as a **law on the function-type constructor** — the corpus has the ρ-functor on the subtyping
  poset (`SubtypeArrow`), so the variance law re-anchors additively, but "the exponential/`F`
  constructor is contravariant in A, covariant in B" as a *committed tooth* on `B^A` is not yet
  authored (the exponential is a single zoo entry with no variance tooth). SYN (additive).

---

## 4. Paradox quarantine by type discipline (Curry §6) — LIFTED (multiple authored realizations)

Curry §6: the Russell contradiction (`E≡WQ`; `χ≡[f]N(ff)`, `⊢χχ=N(χχ)`) rests on a tacit "not even
plausible" assumption about the functional character of negation — it arises ONLY from applying
functionality OUTSIDE its category; **type/functionality discipline is the quarantine.** Directive
19 ties this to ContractGate branching-quarantine + Präriehund provisional-naming + paper 41's
"category as dangerous master". Authored, four ways:

### 4.1 Ill-typed-object refusal = the object-admission quarantine (LIFTED — the closest analog)
- `helios/srcy/papers/09_minimal_category_theory/chapters/01_objects_and_arrows/sections/03_hom_sets_and_disjointness.tex:119-153`
  (`prop:mct-hom-disjointness-no-collapse`): a bare string (`catus`) is **ill-typed**, not an
  admitted hom-set — "a **typing failure**, not an inference" (`00_synthesis.md` 01 §2). This is
  EXACTLY Curry's move: the paradox is a category error; the type gate refuses the ill-typed term
  rather than deriving a contradiction from it. LIFTED (`PD`).
- The **Node-or-Arrow admission gate** `claim ↦ typed node | typed arrow | law-bearing diagram`
  (`09/.../03_olog_node_arrow_law.tex:19-32`) is the general form: nothing enters except as a typed
  arrow/node — a term outside its category is simply inadmissible. LIFTED. Directive-19's
  "self-application must be type-disciplined, never naively self-applicable" = this gate.

### 4.2 Fuel-bounded β + `Y` kept OUT = the runaway-self-application quarantine (LIFTED)
- Paper 33 §2.1's fuel-bounded β-reducer (`thm:33-fuel-bounded-motion`, `:436-471`) refuses
  unbounded reduction; the **Y combinator (unbounded fixed point) appears ONLY in the external
  appendix-39 mirror** (§2.3), never admitted into the authored engine. So the corpus **quarantines
  the fixed-point/self-application operator** exactly as Curry quarantines `χχ`: the disciplined
  engine cannot express the runaway self-application. LIFTED (by authored omission + fuel bound).

### 4.3 Institutional category machine + "rational mastery" = category-as-dangerous-master (LIFTED)
- `helios/srcy/papers/41_cheese_progenitor_topology/chapters/11_institutional_category_machine/chapter.tex:22-42`
  (`def:41-institutional-category-machine`): `I=(e,c,r,μ)` — an institution "evaluates an object
  through its **accepted categories**, retains [residue], and reuses" — with **fixed-point
  countermodels** proved ("institutional fixed-point countermodels" listed as proved-derivation,
  `chapters/12_progenitor_consolidation/chapter.tex:376-378`).
- The "dangerous master" framing: Leary **Circuit Three** = "language, logic, **categorization** …
  together with the **risk that compartmentalization becomes rational mastery**"
  (`paper.tex:31-33`; `chapters/11_.../chapter.tex:13`; `chapters/12_.../chapter.tex:119-121`
  "The Intellect as Master"). This IS the maintainer's "a category is a useful servant, dangerous
  master" (`srcy_map.md:119`) — a **synthesis** of paper 41's authored "compartmentalization →
  rational mastery" warning, not a literal quote (Präriehund: the exact phrase "dangerous master"
  is NOT in paper 41; the authored phrasing is "rational mastery" / "the Intellect as Master").
  The quarantine: the classifier that forces every object into its accepted categories becomes the
  master (the sycophant of the Präriehund doctrine); type discipline keeps the category a servant.
  LIFTED (as "rational mastery" + fixed-point countermodels; the gloss is SYN).

### 4.4 Prairie-Dog provisional naming = the Präriehund quarantine (LIFTED — cited by sha256)
- `base/00a_node_arrow_corpus_spine/chapters/08_lambda_blotto_node_arrow_engine/chapter.tex:60-89`:
  `\LBPrairieClassifier` "returns a **provisional revisable category** together with explicit
  witness obligations **instead of forcing an unknown object into a total taxonomy**" — and cites
  **`docs/praeriehund-demokratie-der-kategorien.md`** directly as source (sha256
  `ad9467664470…dbaebc`, `:68-70`), requiring inspectability/revisability/federation. The Lewis
  "barking squirrel" provisional-name observation is the worked anchor (`:74-89`). This IS Curry §6
  at the ontology level: an object that does not fit an existing category is **not forced** (which
  would be the paradox-inducing out-of-category application) — it is held provisional. LIFTED.
- The doctrine doc itself (`docs/praeriehund-demokratie-der-kategorien.md:24,68,92-94,122`) is the
  governing law: "*ich habe keinen Frame für dieses Ding, also mache ich einen provisorischen auf*"
  (I have no frame for this thing, so I open a provisional one); the functor to the existing
  taxonomy is declared **partial**, the gap **documented, not hidden**. This is the quarantine
  doctrine, verbatim. LIFTED (governing law).

### 4.5 The cheese-trap face closure + "presheaf ≠ set" = the collapse quarantine (LIFTED)
- Every paper carries a **cheese-trap face closure** section (the fixed publication spine,
  `srcy_map.md:74`); the most-exposed face is collapsing `P` into `P(c)` (functoriality → static
  labelling), the `X≡Hom(-,X)` shorthand into literal equality (`00_synthesis.md` 03 §D-SET-6;
  paper 18 `01_thesis.tex:65-68`; paper 14 `01_thesis.tex:90-102`). The `_verb/*_cheese_trap_immunity.ttl`
  family committed these as immunity atoms. This is the type-discipline quarantine applied to the
  presheaf/type layer: do not collapse a typed functor into an untyped set. LIFTED.

### 4.6 ContractGate `Accepted|Rejected` unary gate = the admission quarantine (LIFTED — governing law)
- `docs/unary-byte-frame-law.md:752-758`: "An admission gate remains a unary Frame arrow. Its
  output coordinate may be a closed admission-state ADT, but `Accepted|Rejected` never replaces the
  Frame product … A raw array, tuple, collection, constructor call, or pattern match cannot bypass
  this gate." Every term crosses a typed ContractGate; the ill-typed one is Rejected with typed
  effect evidence — Curry's quarantine as a runtime gate. LIFTED (governing law).

---

## 5. Functionality ↔ implication taiji (Curry §5, Curry-Howard) — **GAP (with one seam)**

Curry §5: `F` is DEFINABLE `F' ≡ [x,y,z](u)(xu ⊃ y(zu))` — a function type is a universally-
quantified implication; Thm 5.8 every F-theorem holds for `F'`. Directive 19: types-as-propositions
is ONE lexeme with two glossary senses (Directive 16 polysemy), the arrow pillar and the
logical-implication layer are the same object.

- **The exponential `B^A` seam:** the corpus authors `B^A` as internal-hom (§1.2) — the
  *categorical* half of Curry-Howard (types = objects, functions = exponentials). But it **NEVER
  identifies the exponential with logical implication**, has **no propositions-as-types**, no
  `⊃`/implication object, no proof-term reading. Grep for `implication`/`Curry-Howard`/`proposition`
  as a type: the hits are all "implication" in the informal-inference sense (evidence rules,
  rule-of-three promotion, paper 28) or LaTeX, **not** the functionality-as-implication identity.
- **GAP:** Curry §5's `F ≡ F'` (function-type = universally-quantified implication) and the
  Curry-Howard "types-as-propositions, one object two senses" are **NOT authored**. The corpus has
  the *arrow* half (exponential/transpose) but not the *logic* half (implication/proof).
- **DECISION D-F2 (maintainer):** does the pillar author the **functionality↔implication taiji**
  (an SP6 polysemy lexeme: `arrow`/`function-type` = `implication`/`proposition`, two
  glossary-scoped senses of one object, teeth = the `B^A ≅ (A⊃B)` correspondence), lifting the
  mathematics from Curry §5 as fact (like the Curry paper generally)? Or is types-as-propositions
  declared honest-red for v1 (no consumer: the corpus reasons categorically, not
  proof-theoretically)? Präriehund read (inference): this is the **cleanest place to honor
  Directive 19's "taiji" wording** — the exponential is already authored, so adding the
  implication sense is a *polysemy tooth on an existing object* (low invention, high Directive-16/
  19 coherence), NOT a new structure. Recommend authoring the taiji-lexeme, teeth-proving only the
  `B^A ↔ A⊃B` direction the exponential already supports, and marking the full Thm-5.8 equivalence
  a cite-only Curry reference.

---

## 6. Re-anchor surface — how SP1's Frame/ρ/Yoneda re-anchors onto the functionality pillar

Directive 19: "how SP1's Frame/ρ/Yoneda apparatus re-anchors onto [the arrow/typing layer]".
`00_synthesis.md` (05 §1.5) flagged this surface for this pillar. Concretely (all committed,
teeth-green — additive edges, nothing rebuilt):

| # | Committed structure (`file:line`) | Re-anchors as (functionality object) | Additive/Rebuild |
|---|---|---|---|
| F1 | `prim:Frame prim:isYonedaPoint true` + `q_yoneda_point` (`primitives.queries.sparql:471-496`) | **Curry's `F` applied** = the typed arrow's Yoneda point (`T→Frame(O,E)` = `F(x)→Frame(X,Y)`) | Additive |
| F2 | `prim:SubtypeArrow`/`IdentityArrow`/`CompositeArrow` (`formal.ttl:322-330`) | the **typed-arrow layer** Curry's `F` types (domain/codomain) | Additive |
| F3 | `prim:RealizationTransport` + `q_functor_identity`/`_composition`/`_total` (`primitives.queries.sparql:261-278,288-548`) | ρ = **functor on arrows** = the §4 **variance carrier** (contravariant dom / covariant cod) | Additive |
| F4 | `prim:RepresentablePresheaf`/`YonedaArrow`/`NaturalitySquare`, `q_yoneda_naturality` (`taiji.ttl`; README:66-88) | the **incoming/outgoing functionality profiles** `Hom(-,X)`/`Hom(X,-)` (§3) | Additive |
| F5 | `prim:KleisliCompositionShape`, Frame-monad unit/assoc (`realization.ttl`; README) | the **effect coordinate** of `F` = the ρ/β-motion monad (§1.1, §2.1) | Additive |
| F6 | `crs:CoordinateDerivation rdfs:subClassOf prim:Realization` ("Kleisli arrow extending ρ") (`crs/derivation.ttl:65`) | SP3 coordinatization = a **Curry-F-typed Kleisli arrow** | Additive |
| F7 | exponential `B^A` (whitepaper zoo, §1.2) — **NOT yet in `basicttl/`** | the **function-type / internal-hom atom** | MINT (SYN) |

**Edge mechanism** (same as `00_synthesis.md` 05 D6): prefer a dedicated
`funcfound:typesAsArrow` / `funcfound:functionalityOf` object property over bare `rdfs:subClassOf`
for the F-groundings (a callable *is typed by* `F`, it is not a *subtype* of it), reserving
`subClassOf` for genuine is-a (e.g. `prim:CompositeArrow rdfs:subClassOf funcfound:TypedArrow`).
Sequencing: land the functionality pillar as a co-equal strand of `basicttl/algfound/`, then add
edges — do not rebuild (15/16 SP re-anchor rows already additive per 05 §4; the functionality
edges are all additive too).

---

## 7. LIFTED / SYN / GAP ledger (the honest summary)

**LIFTED (authored in Helios and/or committed green — faithful, `DS`/`PD`):**
- Functionality `F` = the unary Frame `T→Frame(O,E)` = Yoneda point (governing law + `isYonedaPoint`).
- Exponential/internal-hom `B^A` + currying universal property + `eval` (whitepaper zoo — THIN).
- Adjoint transpose `Hom(LG,A)≅Hom(G,RA)`, `f↔f̄` (paper 26 — richly proved).
- The closed-λ engine: typed λ-term ontology with unary-Frame β-step, closed terms `FV=∅`,
  capture-avoiding substitution, β-motion Kleisli monad, fuel bound (paper 33 ch08).
- Sparky map-shuffle-reduce, the Frame carrier, the Lambda-Blotto engine (`lambda_blotto_model.tex`,
  base 00a ch08).
- §4 variance: contravariant/covariant hom-iso naturality + the two-sided Yoneda profiles +
  ρ-functor-on-subtyping-arrows (`RealizationTransport`, functor identity/composition, committed).
- §6 quarantine: ill-typed-object refusal, Node-or-Arrow gate, fuel bound + `Y` kept out,
  institutional-category-machine + "rational mastery", Prairie-Dog provisional naming (cites the
  Präriehund doc by sha256), cheese-trap collapse immunity, ContractGate `Accepted|Rejected`.

**SYNTHESIZED-FROM (extend a named source or the Curry extract — honest `SYN`):**
- The Frame's **effect coordinate** as an enrichment of Curry's bare `F` (ρ-monad Kleisli effect).
- The **subtyping** reading of variance `U⊆X,Y⊆V⟹FUV` as a committed tooth on `B^A` (the ρ-functor
  carries functorial variance; the exponential-constructor variance tooth is new).
- The "**category as dangerous master**" gloss (SYN of paper 41's authored "rational mastery").
- A first-class **function-type / `B^A` atom** in `basicttl/` (the zoo definition is liftable; the
  committed atom is new).

**GAP (no Helios authored basis → candidate honest-red non-goals, flagged hard):**
- **Combinators B/C/W/K/I, SKI, bracket abstraction / abstraction elimination** — the corpus is a
  named-variable λ-calculus corpus; combinatory logic is absent (`Y` only in the external
  appendix-39 mirror + one Elixir code URL). **The single largest gap** (D-F1).
- **`F_n` (n-ary functionality, Def 2.1) + the `Γ_m·B…` compositor** — absent as such; multi-arg is
  curried-λ / product carriers, not a combinator compositor.
- **Curry §5 functionality↔implication taiji / Curry-Howard / types-as-propositions** — the arrow
  half (`B^A`) is authored; the logic half (`⊃`, proof terms, `F≡F'`) is not (D-F2).
- Liftable as standard mathematical fact (Directive 19: "the mathematics is fact and liftable",
  cf. the Group inverse-law precedent in `00_synthesis.md` §2) — but from the **Curry paper as a
  cite**, not from any Helios paper.

---

## 8. Maintainer design decisions this pillar raises

- **D-F1 — combinatory-logic substrate: mint or cite-only?** The authored substrate is
  named-variable typed λ-calculus (paper 33), not Curry's variable-free combinatory logic. Does v1
  mint B/C/W/K/I + bracket abstraction as agnostic-progenitor atoms grounding the λ-engine, or keep
  the λ-calculus as the authored substrate and treat combinators as a cite-only Curry reference
  (no consumer needs point-free normal forms — YAGNI)? *Präriehund recommendation:* cite-only;
  lift `F` + variance + λ-engine + quarantine (all authored); record B/C/W/K/I as honest-red
  Curry orientation, minting only on a future point-free consumer.
- **D-F2 — the §5 functionality↔implication taiji: author the polysemy lexeme or defer?** The
  exponential `B^A` is authored; adding the implication sense is a *polysemy tooth on an existing
  object* (Directive 16/19 "one object two senses"), low invention. *Recommendation:* author the
  taiji-lexeme, teeth-prove only `B^A ↔ A⊃B`, mark full Thm-5.8 a cite. This is the cleanest way to
  honor Directive 19's "taiji" wording.
- **D-F3 — is `F` a NEW atom or the Frame recognized?** Directive 19 asserts "the Frame IS Curry's
  F". The committed `prim:Frame`/`isYonedaPoint` already carries it. Decide: does the pillar (a)
  *recognize/relabel* the Frame as the functionality object and add a `B^A`/typed-arrow atom + the
  variance tooth (low invention, faithful — mirrors `00_synthesis.md`'s set-floor Opt-1
  recognition), or (b) author a parallel functionality tower the Frame re-anchors onto?
  *Recommendation:* (a) — recognize the Frame as `F`, mint the `B^A` atom + the variance tooth, add
  the F-grounding edges; the ρ-functor-on-arrows already discharges §4.
- **D-F4 — variance tooth teeth-proven or edge-only?** The ρ-functor already teeth-proves
  identity/composition; a committed **variance tooth on the exponential constructor** (`B^A`
  contravariant in A, covariant in B) is new. Directive 19 says "the function-type algebra MUST
  carry this variance" — argues teeth-proven, mirroring `00_synthesis.md` D-G's load-bearing
  SealedGroup re-anchor.
- **D-F5 — placement.** The functionality pillar is Directive 19's co-equal fourth strand of
  `basicttl/algfound/`. Confirm it lands beside set-theory/algebra/space (not beneath), since it
  carries the ARROWS while set theory carries the CARRIERS and the algebra tower the
  OBJECTS/OPERATIONS (Directive 19: "Set theory carries the CARRIERS, the algebra tower the
  OBJECTS/OPERATIONS, this pillar the ARROWS").

---

## 9. Coverage statement (Präriehund)

- **Read IN FULL:** the 5 mandatory doctrine files (`design_constraints.md`, `JUNGLE_MAP.md`,
  `STRICTNESS_RULES.md`, `docs/unary-byte-frame-law.md`, `docs/praeriehund-demokratie-der-kategorien.md`);
  `00_synthesis.md` + all 5 pillar notes `01`-`05`; `srcy_map.md`; whitepaper
  `13_limit_colimit_zoo/20_exponential_object.tex`; paper 33 ch08 `lambda_term_graph_ontology.tex`;
  paper 26 ch01 `01_hom_iso_definition.tex` + `02_transpose_correspondence.tex`; paper 41
  `paper.tex` + ch12 `progenitor_consolidation`; base 00a ch08 `lambda_blotto_node_arrow_engine`
  (head); `lambda_blotto_model.tex` (lines 1-766 of 1715 — the game/Frame/Sparky carriers; the
  remaining ~950 lines are further Sparky/receipt macros, sampled by grep not read line-by-line).
- **Targeted grep + spot-read:** `basicttl/primitives/primitives.queries.sparql` (Frame/ρ-functor/
  Yoneda probes) + `README.md`; `basicttl/primitives/formal.ttl` arrow classes; `basicttl/_verb/`
  contravariance/functor-antonym/cheese-trap families; paper 41 ch11 institutional machine.
- **Whole-corpus grep sweeps** (helios/srcy + basicttl): `combinator|SKI|bracket abstraction|point-
  free|self-application|closed lambda`; `functionality|Curry|implication|typed arrow|Curry-Howard`;
  `exponential|internal-hom|currying|eval|cartesian closed`; `contravariant|covariant|variance`;
  `Russell|paradox|fixed-point|ill-typed|quarantine|category error`; `dangerous master|servant|
  rational mastery`. Negative findings (combinators absent from authored papers; `Y` only in
  external mirror; no Curry-Howard/implication identity; "dangerous master" not a literal quote)
  are **grep-verified, not assumed**.
- **NOT opened in full:** `lambda_blotto_model.tex:767-1715`; paper 33 chapters beyond ch08; the
  1,931 spec-atom + 271 `_aob_*` mirror files (appendix 39, characterized via grep — the `Y`
  combinator + `compass_artifact` hits located but the mirror is external, not authored source).
- **Honest limits:** the "combinators absent" and "no Curry-Howard" verdicts rest on corpus-wide
  greps + the papers read; I did not exhaustively read all 34 papers, so a hidden combinator/
  implication-taiji passage cannot be ruled out with certainty — flagged, not asserted away
  (same caveat as `00_synthesis.md` §6). The `_verb/` files are legacy/generated (JUNGLE_MAP:24),
  cited as corpus traces of variance/quarantine glossary, not as the green floor.
</content>
</invoke>
