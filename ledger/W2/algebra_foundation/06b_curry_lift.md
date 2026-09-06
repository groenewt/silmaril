# 06b — THE CURRY LIFT: functionality / typing / combinatory-logic (Directive 19's fourth pillar)

> Präriehund honesty banner. This is a W2 brainstorming-gate RESEARCH note for **Directive 19**
> (`ledger/W2/design_constraints.md:263-299`) — the FOURTH, co-equal strand of the algebra ← set-theory
> ← space foundation (Directives 18/19). It turns the maintainer-supplied CURRY extract (H. B. Curry,
> *First Properties of Functionality in Combinatory Logic*, Tôhoku Math. J. **41** (1936) 371-401;
> jstage `tmj1911/41/0/41_0_371` — **CITE, never commit the PDF**) into the pillar's liftable STRUCTURE,
> as agnostic-progenitor atoms consistent with `00_synthesis.md`'s **taiji-via-engine** framing. It
> authors NOTHING in `basicttl/`, runs no state-changing git, decides nothing on the maintainer's behalf.
>
> **Tagging law.** Every structural claim is tagged:
> - **LIFTED** — present in a named source. Per the Directive-19 precedent (`:265-268`: "the mathematics
>   is fact and liftable"), **Curry is a maintainer source**, so "LIFTED from Curry §N" is a legitimate
>   lift, exactly as a Helios `file:line` lift is. Helios lifts carry their `file:line`; Curry lifts carry
>   the section of the extract.
> - **SYNTHESIZED-FROM** — extended by fusing a Curry structure with a named Helios/committed-floor
>   structure (honest `SYN`).
> - **GAP** — pure invention, in neither Curry nor Helios (flagged hard, Präriehund provisional-naming).
>
> Scope boundary: this pillar designs the ARROW/TYPING layer. The set-theory floor (03), the algebra
> tower (02), the space constructs (04), and the SP1/SP2/SP3 re-anchor surface (05) are the other strands;
> this note ties INTO them at the seams §7 names, and never redesigns them.

---

## 0. One-paragraph verdict

Set theory (03) carries the **carriers**; the algebra tower (02) carries the **objects and operations**;
this pillar carries the **typed arrows between them** — and Curry 1936 supplies that layer *whole*,
already in the corpus's own idiom. Curry's functionality operator **`F`** (`⊢ FXYZ` = "Z is a function
from category X to category Y") **IS the Unary Frame** the committed floor already ships as
`prim:Frame prim:isYonedaPoint true` (`basicttl/primitives/taiji.ttl:843`) with the law
`T → Frame(output:X, error|effect:Y)` (`docs/unary-byte-frame-law.md:28-38`). The combinators
**B/C/W/K/I + `F_n` + the compositor** are the point-free substrate of that arrow algebra, and they are
**the same closed-λ "Lambda"/Sparky engine the corpus already names** (Lambda-Blotto free-term engine,
`srcy_map.md:121-126`; Directive 19 `:277`). Curry §4's **subtyping variance** (contravariant domain /
covariant codomain) is the law SP1's ρ-functor-on-subtyping-arrows (`prim:RealizationTransport`,
`taiji.ttl:822`) re-anchors onto — but SP1 today carries only the covariant leg, so the contravariant-
domain leg is a genuine **new tooth**. Curry §5's **functionality ↔ implication** definability
(`F' ≡ [x,y,z](u)(xu ⊃ y(zu))`) is a textbook **taiji** in the Directive-16 sense: one lexeme, two
glossary senses (arrow-sense / implication-sense), the same object — the Curry-Howard ancestor. Curry §6's
**paradox quarantine** (Russell `χ≡[f]N(ff)` arises only from applying `F` OUTSIDE its category) IS the
corpus's ContractGate observation boundary (`docs/unary-byte-frame-law.md:314,327,451,685`) + Praeriehund
provisional-naming + the paper-41 "category as dangerous master" warning. **Net: this is the most
faithful of the four strands — almost everything is LIFTED (Curry is a source, and the Frame/ρ/Yoneda
apparatus it maps onto is already committed and green), with exactly three genuine builds: the
contravariant-domain variance tooth, the `F_n`/compositor arity ladder as agnostic-progenitor atoms, and
the self-application quarantine predicate.**

---

## 1. THE FUNCTIONALITY ATOM — Curry `F` = the Frame arrow

### 1.1 The identification (LIFTED — Curry §-intro/§1 ⊕ committed Frame)

Curry's primitive: **`⊢ FXYZ`** means "Z is a function from X to Y", with X, Y themselves
**categories/types** and `F` a **primitive typing/arrow operator** (Curry extract, functionality F).
Directive 19 states the identification verbatim: *"Curry's `⊢ FXYZ` … is exactly `F(x) → Frame(output:X,
effect:Y)`"* (`design_constraints.md:270-273`).

The committed floor already ships the target of that identification:
- **The Frame law itself** — `T → Frame(output: X, error|effect: Y)`, "the typed product required to
  construct a frame around a byte stream … The frame is the Yoneda point at which the callable's one
  observed input maps to its output and typed effect" (`docs/unary-byte-frame-law.md:28-38`). This is
  Curry's `F` with the three coordinates named: **T = the argument category (Curry's X, the domain)**,
  **output:X = the result category (Curry's Y, the codomain)**, and **error|effect:Y = the honest
  monadic cost** Curry's bare `F` does not carry (see §1.3).
- **`prim:Frame prim:isYonedaPoint true`** (`taiji.ttl:843`; the FrameEncoding taiji atom
  `taiji.ttl:371-376`) — the Frame is a first-class committed object, the mutual-colimit gluing of the
  formal `prim:Frame` and physical `prim:FrameEncoding` (`taiji.ttl:366-376`).
- **The Frame is `O × E`** — `Frame(O,E):=O×E`, output×effect, one of the six disjoint "frame" sorts
  (`srcy_map.md:147-153`, whitepaper `00_helios_foundation/06_frame_sort_separation.tex`). Curry's `F`
  applied at a point IS this product-with-typed-effect.

**Structure to mint (design sketch, NOT .ttl):** an agnostic progenitor **`fun:Functionality`** (Curry's
`F`) — the typed-arrow constructor — grounding nothing, whose canonical realization *is* the committed
`prim:Frame`. `fun:Functionality` has three role coordinates lifted straight from Curry: a **domain
category** (`fun:funDomain`, Curry's X = the Frame input `T`), a **codomain category** (`fun:funCodomain`,
Curry's Y = `frameOutput`), and — the SYNTHESIZED enrichment — an **effect category** (`fun:funEffect` =
`frameEffect`). `⊢ FXYZ` ("Z inhabits `FXY`") is the typing judgement `Z : fun:Functionality(X,Y)`, i.e.
`Z` is an admitted `prim:Realization` / Kleisli arrow. **This is the arrow the whole foundation was
missing:** set theory gives carriers, the tower gives objects, `fun:Functionality` types the maps between
them.

### 1.2 Tie to the algebra tower and set theory (LIFTED ⊕ SYNTHESIZED)

- **Set theory (03 §2.2) — function-as-morphism.** 03 flags "function-as-morphism object with
  dom/cod/graph" as a **GAP** (`03_set_theory.md:116-120`; the `prim:Map` data dictionary is not a
  Set-morphism object). **Curry's `F` fills exactly that gap**: `FXY` is precisely "the type of functions
  X→Y", the function-as-morphism object 03 could not lift from Helios. So the set-floor's missing
  function-object **is** `fun:Functionality` restricted to the enrichment where the effect is `NoEffect`
  (`realization.ttl:120-124`, the identity of effect composition). **SYNTHESIZED-FROM** Curry §1 ⊕ 03's
  gap-fill obligation ⊕ `prim:realize_unit` (`realization.ttl:19-21`).
- **Algebra tower (02 §1) — a Monoid IS a one-object category = endo-functionality (LIFTED, both
  sides).** Curry's `F` at a single fixed category `X` gives `FXX` = the endo-arrows on `X`. Helios
  authors precisely this: the **endomorphism monoid `End_C(X)` is "a monoid as a one-object category"**
  (`21/.../04_monoid_monad_yoneda_binders.tex:2,16-17`, cited in `02_algebra_tower.md:58-61`), and the
  **fixed-Frame history monoid `H_F = End_R(F)`** (`appendix 36 B/.../02_e_monad_morphism_strength.tex:46-114`,
  `02_algebra_tower.md:52-55`). So **`fun:Functionality(X,X)` = the monoid rung of 02** — the pillars meet
  at the one-object category: the algebra tower's single genuinely-lifted rung (Monoid) is the
  endo-case of this pillar's arrow constructor. **This is the load-bearing seam between strands 02 and 19.**
- **Groups act (LIFTED as usage / GAP as law).** "A group acts" = a monoid homomorphism into an
  endo-functionality `End(X)` — the worked length homomorphism `|·|: M_X → (ℕ₀,+,0)`
  (`31/02/03:8-10`, `02_algebra_tower.md:207-209`) is exactly a functionality-into-endo-functionality
  arrow. The group *action* is liftable as this arrow shape; the group *inverse law* remains the
  tower's one pure GAP (`02_algebra_tower.md:110-114`).

### 1.3 The honest divergence from Curry (SYNTHESIZED — the effect coordinate)

Curry's `F` is a **bare** two-place arrow (domain, codomain). The committed Frame is a **three**-place
arrow (domain, codomain, **effect**), because "a realization without an effect is not admitted"
(`realization.ttl:11-16`). This is not a contradiction of Curry but a **monadic enrichment** of it: the
realization monad ρ ≡ the Frame monad (`realization.ttl:9-21`), so `fun:Functionality` is Curry's `F`
*in the Kleisli category of the effect monad*. Präriehund pin: record this as the honest seam — Curry §5's
`F'` (§4 below) is the *pure* (`NoEffect`) fragment; the general `fun:Functionality` adds the effect leg.
**SYNTHESIZED-FROM** Curry §1 ⊕ `realization.ttl:9-36`.

---

## 2. THE COMBINATOR SUBSTRATE — B/C/W/K/I + `F_n` + compositor as an agnostic "Combinator" family

### 2.1 The combinators (LIFTED from Curry §-combinators ⊕ SYNTHESIZED onto the Lambda engine)

Curry's substrate under combinatory logic: **B (compose), C (swap), W (duplicate), K (constant),
I (identity)**, with axioms **(FB),(FC),(FW),(FK)** fixing `F`'s behavior on each (Curry extract,
combinators). Point-free / variable-free — which IS the unary law's **"no free variables, closed terms"**
(Directive 19 `:277`; `docs/unary-byte-frame-law.md:20-49` — one explicit input, no `$@/$*`, closed
callable frames).

The corpus already ships the engine these combinators run on:
- **The closed-λ "Lambda" engine** — the `contractbox` fixes **"Lambda" = the engine (eigen-towers +
  closed lambda term + Spark/Joern 'Sparky' map-shuffle-reduce machine)** (`srcy_map.md:121-126`;
  Directive 19 `:277` names it Lambda-Blotto).
- **The free-term engine with a universal property** — `26/.../08_lambda_blotto_free_term_engine.tex:24-44`
  gives the unique homomorphism `f̂: T_Σλ(X) → A` for every `Σλ`-algebra
  (`02_algebra_tower.md:178-181`), and `shared/components/math/olog_yoneda_monoid_monad.tex:193-213`
  the `LBFreeMonadUniversalLaw`. **This is the free-algebra machinery a combinator basis instantiates.**

**Structure to mint (design sketch):** an agnostic progenitor **`fun:Combinator`** grounding nothing
(the byte_order-progenitor pattern, Directive 17, `srcy_map.md:267-276`), with **five composable children
`fun:combinatorB / combinatorC / combinatorW / combinatorK / combinatorI`**, each carrying its Curry
functionality axiom `(FB)/(FC)/(FW)/(FK)` and — for `I` — the identity `F I` behavior. Each child's
`ancestry.via` points at the `fun:Combinator` parent, symmetric across the five (no combinator
privileged) — exactly the `byte_order → {little,big,host,none}` shape. **LIFTED** for the five combinators
and their axioms (Curry); **SYNTHESIZED-FROM** for the progenitor packaging (Curry combinators ⊕ Directive
17 pattern ⊕ the Lambda-Blotto free-term engine as the carrier they generate).

### 2.2 `F_n` and the compositor (LIFTED from Curry Def 2.1 — the arity ladder)

Curry Def 2.1: **n-ary functionality** `F_0 = I`, `F_1 = F`, `F_{n+1} = (C·BB_{n+1}) F_1 F_n`; the
**compositor `Γ_m · B…`** composes functionalities (Curry extract, `F_n` + compositor). This is a
**ladder of arities**, minted **one clause at a time** — which is precisely the corpus's own
"add one universal-property clause at a time / six obligations checked separately" discipline
(`26/03/04_free_versus_path_monoid.tex:24-50`, `02_algebra_tower.md:162-167`) and Directive 17's
"one law per child, never cram."

**Structure to mint (design sketch):** an agnostic progenitor **`fun:NaryFunctionality`** (Curry's `F_n`)
with children indexed by an SP1 `prim:Ordinal` / the unary-law `Count` authority (`docs/unary-byte-frame-
law.md:721-729`): `fun:F0` (= `fun:combinatorI`, the nullary/identity base), `fun:F1` (= the base
`fun:Functionality` of §1), and the recursive `fun:Fsucc(n)` built from `F1`, `F_n` and the compositor.
The **`fun:Compositor`** is the arrow that composes two functionalities — the corpus's `B` (compose)
promoted to the composition operation on the arrow algebra itself. **LIFTED** (Curry Def 2.1). Ties to set
theory: the arity index is the finite-counting ordinal 03 §2.7 lifts (`03_set_theory.md:174-195`,
finite/counting only, no transfinite) — the `F_n` ladder is countably-indexed but each rung finite, so it
sits inside 03's authored finite-ordinal floor with **no transfinite GAP incurred**.

### 2.3 Tie to the algebra tower and set theory

- **`fun:Compositor` = associative composition (LIFTED).** `B` composes; composition in the thin formal
  category is "associative on the nose" (`primitives/README.md`, `05_reanchor_surface.md:60-64`;
  `formal.ttl:322-330` the `SubtypeArrow/IdentityArrow/CompositeArrow` layer). So `fun:F1` under
  `fun:Compositor` with `fun:combinatorI` as unit is *itself* a **monoid** (the endo-functionality monoid
  of §1.2) — the combinator substrate re-anchors on 02's Monoid rung, not beside it.
- **`K` (constant) = the terminal/`Unit` map; `W` (duplicate) = the diagonal into a product (SYNTHESIZED).**
  `K X` ignores its second argument — a projection off a product; `W` duplicates — the diagonal
  `X → X×X`. Both re-anchor on 03's product floor (`prim:Tuple`/`prim:Unit`,
  `03_set_theory.md:130-141`). **SYNTHESIZED-FROM** Curry combinators ⊕ 03 §2.4 products. (Present as the
  standard categorical reading of K/W; not stated in Curry in those words → honest `SYN`, not `LIFTED`.)

---

## 3. THE SUBTYPING-VARIANCE LAW — contravariant domain / covariant codomain, as a tooth

### 3.1 The law (LIFTED from Curry §4)

Curry §4: **`⊢ FXY` with `U ⊆ X` and `Y ⊆ V` ⟹ `⊢ FUV`** — **CONTRAVARIANT in the domain,
COVARIANT in the codomain** (axioms `(FP)₁`, `(FP)₂` via inclusion `P*` / implication `⊃`; Curry
extract §4). Directive 19 restates it verbatim (`design_constraints.md:279-281`).

### 3.2 What SP1 already carries, and the honest gap (LIFTED ⊕ GENUINE-BUILD)

SP1 ships a **functor on arrows** that this law re-anchors onto:
- **`prim:RealizationTransport` = ρ made a genuine FUNCTOR ON ARROWS**, `rho(f): rho(A)→rho(B)` for each
  subtype arrow `f: A→B` (`taiji.ttl:822`, and the naturality-square construction `taiji.ttl:826-843`:
  "STEP B made ρ a genuine FUNCTOR ON ARROWS … materialised the ancestral grounding paths"). Functor
  identity/composition are the `RealizationTransport` teeth (05 §1.5, `05_reanchor_surface.md:112-118`).
- The base category is the **thin formal category** `prim:SubtypeArrow` (A ⊆ B), 59 generators
  (`formal.ttl:322-330`, `05_reanchor_surface.md:58-64`).

**The gap (Präriehund — do not overclaim):** `prim:RealizationTransport` is a **COVARIANT** functor
(`f: A→B` ↦ `rho(f): rho(A)→rho(B)`) — it transports realization *along* subtyping in one direction only.
Curry §4 is a **two-variance** law about the **function-type constructor `F` itself**: as you widen the
codomain (`Y ⊆ V`, covariant) OR **narrow the domain** (`U ⊆ X`, contravariant), `FXY ⊆ FUV`. SP1 has the
covariant machinery and the subtype-arrow base category, but it has **no contravariant leg and no
`F`-constructor-level variance tooth at all** — because SP1's ρ is a functor on *objects'* realizations,
not on the *arrow type* `FXY`. So:
- **LIFTED (the covariant half + the functor machinery):** `taiji.ttl:822`, the `RealizationTransport`
  functor and its identity/composition teeth are the covariant-codomain carrier.
- **GENUINE BUILD / SYNTHESIZED-FROM Curry §4 (the contravariant half):** a new **`fun:variance` tooth**
  on `fun:Functionality` — a SHACL/SPARQL check that `fun:funDomain` is **contravariant** (an inclusion
  `U ⊆ X` on the domain induces `FXY ⊑ FUY`) and `fun:funCodomain` is **covariant** (`Y ⊆ V` induces
  `FXY ⊑ FXV`), with the combined `FXY ⊑ FUV`. The inclusion relation `⊆` is SP1's existing
  `prim:SubtypeArrow`; the tooth is the biting law that the arrow constructor respects it with **opposite
  variance on the two coordinates**. This is the single largest *new law* the pillar contributes.

### 3.3 Tie to algebra / set theory

- Contravariance = the **`op` (opposite category)** construction; the domain coordinate of `F` lands in
  `C^op`. Helios authors `C^op` as the presheaf source `P: C^op → Set` (`18/.../01_thesis.tex:24-31`,
  `03_set_theory.md:56-68`). So the contravariant-domain leg re-anchors on the **already-committed
  presheaf/`C^op` apparatus** (`taiji.ttl` representables `prim:repr_<A> = Hom(-,A)`,
  `03_set_theory.md:220-227`) — **SYNTHESIZED-FROM** Curry §4 ⊕ the committed contravariant presheaf leg,
  NOT invented from nothing.
- Set-theoretic reading: `U ⊆ X` is set inclusion (03's inclusion chain `ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ`,
  `05_reanchor_surface.md:40-54`); the variance law is the statement that the **hom-set functor
  `Hom(-,-)` is contra/co-variant** — the one bijection-of-sets Yoneda already trades on
  (`03_set_theory.md:200-215`).

---

## 4. THE FUNCTIONALITY ↔ IMPLICATION TAIJI — one lexeme, two glossary senses (Directive 16)

### 4.1 The definability (LIFTED from Curry §5 — the Curry-Howard ancestor)

Curry §5: **`F` is DEFINABLE as `F' ≡ [x,y,z](u)(xu ⊃ y(zu))`** — a function type is a
**universally-quantified implication**; Thm 5.8: every `F`-theorem holds for `F'` given the K/C/W
implication laws (Curry extract §5). "Types-as-propositions is one object, two senses." Directive 19
restates it (`design_constraints.md:282-286`): *"the arrow pillar and the logical-implication layer are
the same object."*

### 4.2 This is a taiji in the committed sense (LIFTED ⊕ SYNTHESIZED — mutual colimit / polysemy)

`00_synthesis.md`'s framing is **taiji-via-engine**: two faces, one object, glued by the lifted engine
(D-A Opt 3, `00_synthesis.md:208-213`). Curry §5 is exactly that shape:
- **Face 1 (yin) — the arrow sense:** `fun:Functionality` = the Frame arrow (§1), the *how-you-compute*
  face. This is `prim:Frame` (`taiji.ttl:371-376`).
- **Face 2 (yang) — the implication sense:** `F'` = `(u)(xu ⊃ y(zu))`, the *what-it-proves* face — a
  proposition. This is a **logical-implication object** the corpus does not yet carry as such (GAP for
  the object; LIFTED for the definition).
- **The gluing:** Thm 5.8's theorem-preservation (`F`-theorems ≡ `F'`-theorems) IS the **reflexive seal**
  the taiji atoms already use (`taiji.ttl:366-368`, `physicalFacet → interpretAs == formalFacet`): the
  two faces prove the same theorems, so the colimit closes.

**Directive 16 polysemy (the exact mechanism, PINNED by 00_synthesis §5.7 as an SP6 tooth,
`00_synthesis.md:316-320`):** mint **one lexeme `functionality`** carried by the mole-of-glossaries with
**two glossary-scoped senses simultaneously** — *arrow-sense* (per-primitive/Frame glossary: it's a
`prim:Frame`) and *implication-sense* (logic glossary: it's `F' = (u)(xu ⊃ y(zu))`), with a **biting
polysemy tooth** that the two senses are theorem-equivalent (Thm 5.8). This is structurally identical to
the already-resolved `colimit` polysemy (Directive 16, `design_constraints.md:169-180`) and the
`coproduct/disjoint-union` polysemy (03 D-SET-5, `03_set_theory.md:303-308`). **LIFTED** (Curry §5 supplies
both senses and their equivalence); **SYNTHESIZED-FROM** for packaging it as a taiji atom + SP6 glossary
tooth (Curry §5 ⊕ `00_synthesis.md:208-213` taiji-via-engine ⊕ Directive 16).

### 4.3 Tie to algebra / set theory

- Implication `⊃` with the **K/C/W** laws (Curry §5) is exactly the combinator basis of §2 — so the
  implication face and the combinator substrate are the **same** structure (K = weakening, C = exchange,
  W = contraction — the structural rules of the implicational logic). **This unifies §2 and §4:** the
  combinator progenitor `fun:Combinator` IS the proof-term algebra of the implication face. **LIFTED**
  (Curry §5 explicitly invokes the K/C/W implication laws).
- Set-theoretic reading: `F' = (u)(xu ⊃ y(zu))` universally quantifies `u` over the domain — the
  function-type-as-dependent-product reading, grounding on 03's product floor (`prim:Tuple`,
  `03_set_theory.md:130-141`). The `⊃` is the internal-hom / exponential object; in the presheaf topos SP1
  carries (`03_set_theory.md:160-171`, the subobject classifier `Ω`), `⊃` is the Heyting implication — a
  **SYNTHESIZED** tie (03's `Ω` ⊕ Curry §5), honest-`SYN`, not claimed as authored.

---

## 5. THE PARADOX-QUARANTINE DISCIPLINE — self-application type-gated

### 5.1 The quarantine (LIFTED from Curry §6)

Curry §6: the self-application entity `E ≡ WQ`; `χ ≡ [f]N(ff)` gives `⊢ χχ = N(χχ)` (Russell). The
contradiction rests on a **tacit, "not even plausible" assumption (Hp iii)** about the functional
character of negation — it arises **ONLY from applying functionality OUTSIDE its category**. **Type
discipline is the quarantine** (Curry extract §6). Directive 19 restates it and names the corpus ties
(`design_constraints.md:288-293`): ContractGate branching-quarantine + Praeriehund provisional-naming +
paper-41 "a category is a useful servant, dangerous master."

### 5.2 The corpus already ships the quarantine machinery (LIFTED — three independent anchors)

- **ContractGate as the observation boundary (`docs/unary-byte-frame-law.md`).** "Every … frontend must
  project its syntax through a registered ContractGate observation into the same typed physical evidence"
  (`:313-316`); "explicit spelling alone is not external-dependency admission … must cross its registered
  typed ContractGate boundary" (`:324-328`); and critically **"An admission gate remains a unary Frame
  arrow. Its output coordinate may be a closed admission-state ADT, but `Accepted|Rejected` never replaces
  the Frame product"** (`:752-757`). This IS Curry's quarantine: a foreign / self-applying term is
  **rejected at the gate unless it crosses a typed boundary** — functionality applied outside its category
  does not type-check, so it never enters. **LIFTED.**
- **Praeriehund provisional-naming (`docs/praeriehund-demokratie-der-kategorien.md`).** Lewis's
  *barking squirrel* — "ich habe keinen Frame für dieses Ding, also mache ich einen provisorischen auf"
  (`:24`), a partial functor to the existing taxonomy declared *partial* not total (`:68`). The
  self-applying `χχ` is precisely "a thing with no Frame": the discipline is to mark it **provisional /
  `silm:isProvisional`** (the committed pattern, e.g. `aob:byteOrderHost`,
  `05_reanchor_surface.md:171-174`; the χ-obligation honest-red deferral `crs:chiComparisonObligation`,
  `05_reanchor_surface.md:266-267`), NOT to force it into a total type where it detonates. **LIFTED.**
- **Paper 41 — "category as dangerous master."** The cheese/progenitor warning: *a category is a useful
  servant, dangerous master* (`srcy_map.md:119`, Vol 41; byte-sealed cheese witness SHA-256-pinned). The
  cheese-trap face "analogy-as-identity collapse" is the same failure Curry §6 names — treating `F` as
  applicable to itself (`04_space_constructs.md:158-171`, the cell-complex analogy-as-identity collapse).
  **LIFTED.**

### 5.3 Structure to mint (design sketch — the one genuine build)

A **`fun:selfApplicationGuard`** predicate on `fun:Functionality`: a term `Z` may inhabit `F X Y` with
`X` mentioning `Z`'s own type **only** if it crosses a `fun:ContractGate` (re-using the committed
ContractGate shape) — i.e. **self-application is admitted only through a typed, provisional gate, never as
a bare total arrow.** The negative case (`χχ`, the ungated self-application) resolves to a
`silm:isProvisional` honest-red marker, never a committed total type. **SYNTHESIZED-FROM** Curry §6 ⊕ the
committed ContractGate (`unary-byte-frame-law.md:752-757`) ⊕ Praeriehund provisional-naming. The *guard's
existence* is LIFTED (Curry §6 says type discipline is the quarantine); the *specific predicate wiring* is
the build.

### 5.4 Tie to algebra / set theory

This is the pillar's contribution to the **Russell/size discipline** 03 leaves open: 03 keeps
local-smallness / size as an **honest hypothesis, never a modeled universe** (`03_set_theory.md:188-195,
293-295`). Curry §6's quarantine is the *arrow-layer* version of the same restraint: you do not form the
"type of all types" or the unrestricted self-application, exactly as 03 does not form the universe set.
**The two strands enforce the same discipline from two sides** (objects: no universe set; arrows: no
untyped self-application) — a genuine coherence between strand 03 and strand 19. **SYNTHESIZED-FROM**
Curry §6 ⊕ 03 D-SET-3.

---

## 6. SUMMARY TABLE — the five structures, tagged

| # | Structure (design sketch) | Curry source | Committed / Helios anchor | Tag |
|---|---|---|---|---|
| 1 | `fun:Functionality` atom (F = the Frame arrow; domain/codomain + effect enrichment) | F, §1 | `taiji.ttl:843,371-376`; `unary-byte-frame-law.md:28-38` | **LIFTED** (F↔Frame); effect leg **SYNTHESIZED** |
| 1b | function-as-morphism object (fills 03's set-floor GAP) | §1 | `03_set_theory.md:116-120` (the gap); `realization.ttl:120-124` (NoEffect) | **SYNTHESIZED-FROM** Curry §1 ⊕ 03 gap |
| 1c | `fun:Functionality(X,X)` = Monoid rung = one-object category | F at fixed X | `21/.../04:2,16-17`; `App36B/02:46-114`; `02_algebra_tower.md:52-61` | **LIFTED** (both sides) |
| 2 | `fun:Combinator` progenitor {B,C,W,K,I} + axioms (FB/FC/FW/FK) | combinators | Lambda engine `srcy_map.md:121-126`; free-term `26/.../08:24-44` | **LIFTED** (combinators); packaging **SYNTHESIZED** (Dir 17) |
| 2b | `fun:NaryFunctionality` `F_n` ladder + `fun:Compositor` | Def 2.1 | one-law-per-child `26/03/04:24-50`; ordinal `03_set_theory.md:174-195` | **LIFTED** (Def 2.1) |
| 2c | K = terminal/projection, W = diagonal into product | combinators | `03_set_theory.md:130-141` (product floor) | **SYNTHESIZED-FROM** Curry ⊕ 03 §2.4 |
| 3 | subtyping-variance TOOTH: contravariant domain / covariant codomain | §4 (FP)₁,(FP)₂ | covariant leg `taiji.ttl:822` (`RealizationTransport`); base cat `formal.ttl:322-330` | covariant **LIFTED**; contravariant leg **GENUINE BUILD / SYN-from §4 ⊕ C^op presheaf** |
| 4 | functionality↔implication TAIJI (`F' ≡ [x,y,z](u)(xu ⊃ y(zu))`) + SP6 polysemy tooth | §5, Thm 5.8 | taiji seal `taiji.ttl:366-368`; polysemy Dir 16 `design_constraints.md:169-180` | **LIFTED** (both senses + equivalence); taiji packaging **SYNTHESIZED** |
| 5 | `fun:selfApplicationGuard` (self-application type-gated) | §6 (`χ≡[f]N(ff)`) | ContractGate `unary-byte-frame-law.md:752-757`; Praeriehund `:24,68`; paper 41 `srcy_map.md:119` | quarantine **LIFTED**; predicate wiring **SYNTHESIZED** |

**Pure GAP (no Curry, no Helios) — none in this pillar.** Unlike strand 02 (the Group inverse law is a
pure GAP, `02_algebra_tower.md:110-114`) and strand 04 (point-set topology is refused,
`04_space_constructs.md:158-171`), **every structure here is either LIFTED from Curry (a maintainer
source) or SYNTHESIZED by fusing Curry with an already-committed floor.** The nearest thing to a GAP is the
contravariant-domain variance leg (§3.2) and the self-application predicate wiring (§5.3), and both are
SYNTHESIZED-FROM a named Curry section ⊕ a committed anchor, not invented. This is the most faithful of the
four strands.

---

## 7. THE SEAMS — where this pillar meets the other three strands (for the gate)

- **↔ Set theory (03):** `fun:Functionality` fills 03's **function-as-morphism GAP** (§1.2); the `F_n`
  ladder sits inside 03's finite-ordinal floor with no transfinite cost (§2.2); the variance law is the
  contra/co-variance of `Hom(-,-)` 03's Yoneda already trades on (§3.3); §6 quarantine is the arrow-side
  of 03's no-universe-set restraint (§5.4).
- **↔ Algebra tower (02):** `fun:Functionality(X,X)` **IS** 02's one genuinely-lifted rung, the Monoid /
  endomorphism monoid / one-object category (§1.2) — the two strands share their spine at the endo-case.
  `fun:Compositor` + `fun:combinatorI` re-make that monoid (§2.3). Group *action* = functionality into
  endo-functionality (§1.2).
- **↔ Space (04):** untouched directly; the effect monad (§1.3) is the same ρ the metric/enrichment route
  of 04 D4 uses (`04_space_constructs.md:260-266`), so `fun:Functionality`'s effect leg and 04's Lawvere
  enrichment over `([0,∞],≥,+)` share the CommutativeMonoid seam.
- **↔ Re-anchor surface (05):** the whole pillar re-anchors on **`realization.ttl`'s
  `RealizationTransport` + `taiji.ttl`'s Yoneda/Frame apparatus** — flagged by 05 §1.5 / D and §5.5 as
  "the Curry pillar's surface, not this note's to design" (`05_reanchor_surface.md:112-118, 342-346`).
  This note is that design. The re-anchor is **ADDITIVE**: `prim:Frame` gains a `subClassOf
  fun:Functionality` edge, `prim:RealizationTransport` gains the variance tooth, nothing is rebuilt.

---

## 8. MAINTAINER DECISIONS THIS PILLAR RAISES

- **D-CURRY-1 — the effect enrichment (§1.3).** Curry's `F` is a bare 2-arrow; the committed Frame is a
  3-arrow with an effect. Ruling wanted: is `fun:Functionality` **Curry's F in the Kleisli category of the
  effect monad** (recommended — matches the committed `realization.ttl:9-21` exactly, and Curry §5's `F'`
  is then the pure/`NoEffect` fragment), or a bare 2-arrow with effect bolted beside it? The former makes
  the pillar and SP1 the same object; the latter duplicates.
- **D-CURRY-2 — the contravariant-domain variance tooth (§3.2, the one genuine law-build).** SP1's ρ is
  covariant only. Does v1 **author the full Curry §4 two-variance tooth** on `fun:Functionality`
  (recommended — Directive 19 `:279-281` names §4 as load-bearing, and the contravariant leg re-anchors on
  the committed `C^op` presheaf apparatus, so it is SYN not invention), or ship covariant-only now and
  defer contravariance honest-red to W5? This is the single largest *new law* in the pillar.
- **D-CURRY-3 — combinator depth (§2).** Mint the **full B/C/W/K/I progenitor + the `F_n` arity ladder**
  as agnostic-progenitor atoms (recommended, Directive 17 + the corpus's own one-clause-at-a-time
  discipline), or only the rungs a consumer hangs on (`I`, `B`=compose, and `F_1`=Frame)? YAGNI vs
  Directive 17 "do all, no privilege." The Lambda-Blotto free-term engine is the lift-supported carrier
  either way.
- **D-CURRY-4 — the implication face as a first-class object (§4).** The arrow sense is committed
  (`prim:Frame`). Does v1 also **mint the implication-sense object `F'`** (making the Curry-Howard taiji a
  real two-faced colimit atom + SP6 polysemy tooth, recommended per Directive 16), or carry only the
  arrow sense and record the implication sense as a glossary annotation? The taiji framing
  (`00_synthesis.md:208-213`) argues for the two-faced atom.
- **D-CURRY-5 — self-application guard wiring (§5.3).** Is the quarantine a **teeth-proven
  `fun:selfApplicationGuard` predicate** (recommended — gate self-application through a typed
  ContractGate, resolve the ungated case to `silm:isProvisional`), or a documented discipline only?
  Directive 19 `:293` ("the foundation must make self-application type-disciplined, never naively
  self-applicable") argues teeth-proven.
- **D-CURRY-6 — the PDF citation surface.** Confirm the CITE-not-commit rule (Directive 19 `:265-268`):
  the Curry 1936 mathematics is lifted as fact with the jstage handle `tmj1911/41/0/41_0_371` in an
  `rdfs:seeAlso`/citation annotation; the journal scan is never committed. (Präriehund: this note already
  cites, never reproduces.)

---

## 9. Coverage statement (Präriehund)

- **Read IN FULL for this pillar:** Directives 18 + 19 (`design_constraints.md:228-299`); `00_synthesis.md`
  and the five pillar notes 01-05; `srcy_map.md`; `docs/unary-byte-frame-law.md` (the Frame law + ContractGate
  + Byte-Stream Carrier Closure + admission-gate-as-Frame-arrow); `docs/praeriehund-demokratie-der-kategorien.md`;
  `JUNGLE_MAP.md`. The **CURRY extract** (maintainer-supplied, read in full per the task header).
- **Committed floor inspected with `file:line`:** `taiji.ttl` (`:33-44,366-376,820-843,856-919` — the
  literal-Yoneda layer, `RealizationTransport` as functor-on-arrows, `isYonedaPoint`, naturality squares);
  `realization.ttl` (`:9-36,76,120-124` — the ρ Kleisli/Frame monad, `KleisliArrow`, `NoEffect` unit);
  `formal.ttl` (`:322-330` thin subtype category — via 05). `aob:SealedGroup`, `crs:*` re-anchor points
  carried from 05's `file:line` (not re-opened; cited via the note).
- **Curry sections mapped:** F/§1 (§1 here), combinators + Def 2.1 (§2), §4 variance (§3), §5 `F'` + Thm 5.8
  (§4), §6 `χχ` quarantine (§5) — all from the maintainer-supplied extract, cited by section not page.
- **Honest limits:** the Curry lift rests on the maintainer-supplied EXTRACT, not a re-read of the 1936
  scan (correct per CITE-not-commit). Helios has **no combinatory-logic paper** — grep of `srcy_map.md`
  surfaces the Lambda-Blotto *engine* and the free-term engine (the carrier the combinators run on) but no
  B/C/W/K/I axiomatization — so §2's combinator atoms are LIFTED-from-Curry onto a SYNTHESIZED Helios
  carrier, exactly as flagged; I did not exhaustively re-read all 34 papers to rule out a hidden
  combinator paper (Präriehund: flagged, not asserted away). The contravariance gap in
  `prim:RealizationTransport` (§3.2) is stated from `taiji.ttl:822` + the STEP-B comment; I did not
  walk every naturality-square individual to confirm no contravariant individual exists — the covariant
  framing is the authored one, and a hidden contravariant leg would only shrink, not enlarge, the build.
