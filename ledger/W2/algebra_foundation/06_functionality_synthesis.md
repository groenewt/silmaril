# 06 — SYNTHESIS: the FUNCTIONALITY / TYPING / COMBINATORY-LOGIC pillar (Directive 19 brainstorming gate)

> Präriehund honesty banner. This is the SYNTHESIS a brainstorming DESIGN GATE needs for the FOURTH,
> co-equal strand of the algebra ← set-theory ← space foundation (Directive 19,
> `ledger/W2/design_constraints.md:263-299`), built STRICTLY on the three pillar research notes
> (`06a_functionality_corpus.md`, `06b_curry_lift.md`, `06c_sp1_functionality_reanchor.md`, all read
> in full) and on `00_synthesis.md` (read in full). It authors NOTHING in `basicttl/`, runs no
> state-changing git, and DECIDES nothing on the maintainer's behalf. Every structural claim is
> tagged **LIFTED** (present in authored Helios source or the committed floor, with the note that
> carries the `file:line`), **LIFTED-FROM-CURRY** (present in the maintainer-supplied Curry 1936
> extract — a legitimate lift per Directive 19 `:265-268` "the mathematics is fact and liftable",
> but with the honest sub-tag of whether a Helios CARRIER exists for it), **SYNTHESIZED-FROM**
> (fused from a named source + the Curry extract — honest `SYN`), or **GAP** (no source at all →
> pure invention, flagged hard). Consistent with `00_synthesis.md`'s framing: taiji-via-engine,
> agnostic-progenitor (Directive 17), DS/PD/SYN + Node-or-Arrow honesty machinery. The Curry source
> (H. B. Curry, *First Properties of Functionality in Combinatory Logic*, Tôhoku Math. J. **41**
> (1936) 371-401; jstage `tmj1911/41/0/41_0_371`) is **CITED, never committed** (Directive 19).
> The other three strands (set theory 03, algebra tower 02, space 04) are referenced at the seams
> §3 names, never redesigned here.

---

## 0. The one-paragraph verdict the gate is being asked to rule on

This is the **most faithful of the four strands** — and the reason is structural, not lucky:
**Directive 18's stack (set theory → algebra tower → space) is a stack of CARRIERS and OBJECTS with
no first-class ARROW layer, and the arrow layer is the one thing the committed floor already ships
richest.** `prim:Frame` IS the typed-arrow codomain object the whole realization monad is the
Kleisli category of; `prim:Realization` IS a fully-coordinatised inhabitant of the arrow type (with
`realizesFrom` domain, `frameOutput` codomain, `frameEffect` effect); `prim:isYonedaPoint true`
materialises Directive 19's own identity "the Frame is the Yoneda point = the Frame is Curry's F
applied"; and `prim:RealizationTransport` is a **provable covariant functor on the subtype order**
with teeth-checked identity and composition laws. So Curry's functionality operator `F`, the §4
covariant-codomain variance, the §6 type-discipline quarantine, and the compositor's identity/binary
halves are all **already committed and green** — 3½ of the pillar's structures re-anchor as purely
ADDITIVE edges. The genuine work is **exactly three items, and the notes disagree about two of
them**: (1) the **combinatory substrate** B/C/W/K/I + `F_n` + the compositor — LIFTABLE-FROM-CURRY
but with **no Helios carrier** (the authored substrate is *named-variable* typed λ-calculus, the
opposite of Curry's variable-free combinatory logic), so whether to mint it or cite it is a real
fork the three notes split on; (2) the **§4 contravariant-domain variance tooth** — a hard build,
because the unary Frame law deliberately forbids an input coordinate for contravariance to live on,
colliding head-on with `docs/unary-byte-frame-law.md:686-687`; (3) the **§5 functionality↔implication
taiji** — the arrow face (`B^A`/`prim:Realization`) is authored, the logic face (`⊃`, proof terms)
is not, so it is a polysemy-tooth build. **Net for the gate: this is not a "lift combinatory logic"
project — the corpus is a λ-corpus, not a CL-corpus. It is a "RECOGNIZE the Frame as Curry's F,
re-anchor the already-committed arrow/variance/quarantine apparatus additively, and settle three
forks — how deep into combinators, how to materialise contravariant-domain variance against the
unary law, and whether to mint the implication face now" project.** Directive 19 itself PINS the
identification and several of the forks' answers; those are collected in §5, not offered as choices.

---

## 1. PROPOSED FUNCTIONALITY-PILLAR STRUCTURE (lifted / lifted-from-Curry / synth / gap)

The proposed pillar is `basicttl/funcfound/` (name illustrative), a co-equal fourth strand landing
**beside** set-theory/algebra/space under `basicttl/algfound/`, carrying the ARROWS while set theory
carries the CARRIERS and the algebra tower the OBJECTS/OPERATIONS (the division is Directive 19's
own, `:276` — pinned, §5). Five structures, each tagged; the shape of each (agnostic progenitor,
one-law-per-child) is itself LIFTED from Directive 17 + the corpus's one-clause-at-a-time discipline.

### 1.A The Functionality atom: Curry `F` = the Frame arrow (the anchor of the pillar)

| Element | Status | Source anchor (via pillar note) |
|---|---|---|
| `F` = the typed-arrow / functionality operator (`⊢FXYZ` = "Z is a function X→Y") | **LIFTED-FROM-CURRY** (§-intro/§1) + **carrier LIFTED** | 06b §1.1; 06c §1.1 |
| The Frame law `T → Frame(output:X, error\|effect:Y)` = `F` with three coordinates named | **LIFTED** (governing law) | 06a §1.1 (`docs/unary-byte-frame-law.md:28-38`); 06c §1.1 (`:29,689-694`) |
| `prim:Frame` = the typed product output×effect, Kleisli base of the realization monad | **LIFTED** (committed) | 06c §1.1 (`formal.ttl:206-208`) |
| `prim:Frame prim:isYonedaPoint true` = "Frame is Yoneda point = Curry's F applied" | **LIFTED** (committed triple `taiji.ttl:1994`; atom `957-959`) + **SYN** (the F-identification) | 06a §1.1; 06c §1.5 |
| `prim:Realization` = inhabitant `Z` of `FXY` w/ `realizesFrom`(dom)/`frameOutput`(cod)/`frameEffect` | **LIFTED** (committed, teeth `q_frame_effect`/`RealizationShape`) | 06c §1.2 (`realization.ttl:50-95`) |
| The **effect coordinate** as an enrichment of Curry's bare 2-place `F` (ρ-monad Kleisli effect) | **SYNTHESIZED-FROM** Curry §1 ⊕ `realization.ttl:9-36` | 06a §1.1; 06b §1.3 |
| `fun:Functionality(X,X)` = endo-arrows = **the Monoid rung = one-object category** (seam to 02) | **LIFTED** (both sides) | 06b §1.2 (`21/…/04:2,16-17`; `02_algebra_tower.md:52-61`) |
| function-as-morphism object (fills 03's set-floor GAP; `F` restricted to `NoEffect`) | **SYNTHESIZED-FROM** Curry §1 ⊕ 03's gap ⊕ `realization.ttl:120-124` | 06b §1.2 (`03_set_theory.md:116-120`) |

**Recommendation (see DF-A/DF-F3):** the pillar **RECOGNIZES `prim:Frame` as Curry's `F`** (mirrors
`00_synthesis.md`'s set-floor Opt-1 recognition/consolidation) rather than authoring a parallel
functionality tower — the identification is Directive 19's own wording (pinned), and the committed
`prim:Frame`/`isYonedaPoint`/`prim:Realization` already carry it teeth-green.

### 1.B The Combinator agnostic-progenitor family: B/C/W/K/I + `F_n` + compositor (the contested substrate)

| Element | Status | Source anchor (via pillar note) |
|---|---|---|
| Combinators **B (compose), C (swap), W (duplicate), K (constant), I (identity)** + axioms (FB)(FC)(FW)(FK) | **LIFTED-FROM-CURRY** (combinators) — but **NO Helios carrier** (`GAP` on the carrier side) | 06a §2.3 (grep-verified absent); 06b §2.1; 06c §1.4 |
| The closed-λ "Lambda"/Sparky/Lambda-Blotto engine (the substrate the combinators would run on) | **LIFTED** (authored, richly) | 06a §2.1-2.2 (`33/…/08_lambda_term_graph_ontology.tex`; `lambda_blotto_model.tex`); 06b §2.1 |
| The free-term engine's universal property `f̂: T_Σλ(X)→A` (the free-algebra machinery a basis instantiates) | **LIFTED** | 06b §2.1 (`26/…/08_lambda_blotto_free_term_engine.tex:24-44`) |
| `fun:NaryFunctionality` `F_n` ladder (Def 2.1: `F_0=I`, `F_1=F`, `F_{n+1}=(C·BB_{n+1})F_1F_n`) | **LIFTED-FROM-CURRY** (Def 2.1) — carrier **GAP** (multi-arg is curried-λ/product, not a compositor) | 06a §2.3; 06b §2.2; 06c §1.4 |
| `fun:Compositor` `Γ_m·B…` = composition on the arrow algebra; identity η↔`F_0=I`, Kleisli `>=>`↔Γ | **SYNTHESIZED-FROM** (η↔I, Kleisli-compose↔Γ; identity+binary halves LIFTED) | 06c §1.4 (`realization.ttl:82-89,2904-2920`; `formal.ttl:326-332`) |
| K = terminal/projection off a product; W = diagonal `X→X×X` (categorical reading of the combinators) | **SYNTHESIZED-FROM** Curry ⊕ 03 §2.4 product floor | 06b §2.3 (`03_set_theory.md:130-141`) |

**The honest divergence the gate must see (Präriehund).** The three notes **disagree** on this
structure, and the disagreement is real, not cosmetic:
- **06a recommends CITE-ONLY** (§2.3, §8 D-F1): the authored substrate is named-variable λ-calculus
  (paper 33 §2.1: named variables + explicit environments + capture-avoiding α-renaming) — the
  *opposite* of Curry's variable-free combinatory logic. B/C/W/K/I are grep-verified ABSENT from the
  34 authored papers (`Y` appears only in the external appendix-39 mirror + one Elixir URL). So
  combinators are the pillar's *largest genuine invention*; YAGNI (no consumer needs point-free
  normal forms) argues for cite-only.
- **06b recommends MINTING the full B/C/W/K/I progenitor + the `F_n` ladder** (§2, §8 D-CURRY-3):
  Curry is a maintainer SOURCE (Directive 19 `:265-268`), so "LIFTED from Curry §-combinators" is a
  legitimate lift; Directive 17 ("do all, no privilege") + the corpus's own one-clause-at-a-time
  discipline argue for the full family, on the Lambda-Blotto free-term engine as the carrier.
- **06c is neutral** (§1.4, D-3): SP1 supplies only `I` (`IdentityArrow`) and `B`-flavoured
  composition; `C`/`W`/`K`/`F_n` "lives in Lambda/Sparky" — a pillar-lift, not an SP1 re-anchor.

This is exactly the DF-B fork below. The resolution turns on **whether Curry-as-source makes the
combinators a LIFT or whether the absence of a Helios carrier makes them an INVENTION** — a framing
call only the maintainer settles (§4 DF-B). My own Präriehund lean sides with 06a for v1 (cite-only,
YAGNI, faithful to the λ-substrate) — but I flag that 06b's Directive-17 reading is equally defensible
and that the notes genuinely split.

### 1.C The subtyping-variance tooth (Curry §4) — contravariant domain / covariant codomain

| Element | Status | Source anchor (via pillar note) |
|---|---|---|
| The law `FXY`, `U⊆X`, `Y⊆V` ⟹ `FUV` (contravariant dom, covariant cod; axioms (FP)₁,(FP)₂) | **LIFTED-FROM-CURRY** (§4) | 06b §3.1; 06c §1.3 |
| **Covariant codomain** = `prim:RealizationTransport` covariant functor `ρ(A)→ρ(B)` + identity/composition teeth | **LIFTED** (committed, provable functor) + **SYN** (§4 identification) | 06c §1.3 (`realization.ttl:2865-2920`); 06a §3 (`q_functor_identity/_composition/_total`) |
| The subtype-arrow base category `prim:SubtypeArrow` (A⊆B, 59 generators) the variance rides on | **LIFTED** (committed) | 06a §1.4; 06c §1.3 (`formal.ttl:322-330`) |
| The two-sided Yoneda profiles `Hom(-,X)`(incoming/contravariant) / `Hom(X,-)`(outgoing/covariant) | **LIFTED** (authored) | 06a §3 (whitepaper §04 sous-profile; paper 33) |
| **Contravariant domain** variance tooth on the `F`-constructor itself | **GAP / NEEDS NEW TEETH** — SP1 has NO contravariant structure; the unary law forbids an input coordinate | 06c §1.3, D-1 (`docs/unary-byte-frame-law.md:686-687`; `formal.ttl:206-208`) |
| The subtyping *reading* of variance as a committed tooth on `B^A` (vs ρ's functorial variance) | **SYNTHESIZED-FROM** Curry §4 ⊕ the committed `C^op` presheaf apparatus | 06a §3; 06b §3.2-3.3 |

**The crux (06c's headline).** SP1's covariant machinery is a faithful, additive re-anchor for §4's
covariant codomain — but §4's **contravariant domain** has **nowhere to attach**: `prim:Frame` is a
*product* output×effect (covariant in both), and the callable's input is deliberately *not* a Frame
coordinate (unary law `:686-687,689-694`). So the contravariant leg is a **hard build that collides
with the governing law** — see DF-D and its sub-fork D-1 (Opt A separate constructor / Opt B Frame
input coordinate = law violation / Opt C ContractGate frontier).

### 1.D The functionality ↔ implication taiji (Curry §5, the Curry–Howard ancestor)

| Element | Status | Source anchor (via pillar note) |
|---|---|---|
| `F` DEFINABLE as `F' ≡ [x,y,z](u)(xu ⊃ y(zu))`; Thm 5.8 (F-theorems ≡ F'-theorems under K/C/W) | **LIFTED-FROM-CURRY** (§5) | 06b §4.1; 06a §5 |
| Face 1 (arrow sense) = `fun:Functionality`/`prim:Frame`/`prim:Realization` — the *how-you-compute* face | **LIFTED** (committed) | 06b §4.2 (`taiji.ttl:371-376`) |
| Face 2 (implication sense) = `F'` = `(u)(xu ⊃ y(zu))` — the *what-it-proves* face, a proposition | **GAP** (no `⊃` object, no proof-term reading, no propositions-as-types in the corpus) | 06a §5; 06c §1.6 |
| The exponential `B^A` = internal-hom + currying universal property + `eval` (the categorical half) | **LIFTED** (authored, THIN — one zoo entry) | 06a §1.2 (`…/13_limit_colimit_zoo/20_exponential_object.tex`) |
| The gluing = Thm 5.8 theorem-preservation ≡ the taiji reflexive seal (`physicalFacet→interpretAs==formalFacet`) | **SYNTHESIZED-FROM** Curry §5 ⊕ `taiji.ttl:366-368` ⊕ the taiji-via-engine framing | 06b §4.2 |
| SP6 polysemy: ONE lexeme `functionality` w/ arrow-sense + implication-sense simultaneously, biting tooth = `B^A↔A⊃B` | **SYNTHESIZED-FROM** Curry §5 ⊕ Directive 16 (`design_constraints.md:169-180`) | 06a §5, D-F2; 06b §4.2 |

**Note the unification (06b §4.3):** implication `⊃` with the **K/C/W** laws (Curry §5) *is* the
combinator basis of §1.B — K=weakening, C=exchange, W=contraction (the structural rules). So the
implication face and the combinator substrate are the SAME structure; DF-B and DF-C are coupled (if
you mint combinators you have most of the implication face's proof-term algebra for free, and vice
versa).

### 1.E The paradox-quarantine discipline (Curry §6) — self-application type-gated

| Element | Status | Source anchor (via pillar note) |
|---|---|---|
| Russell `E≡WQ`; `χ≡[f]N(ff)`, `⊢χχ=N(χχ)` arises ONLY from applying `F` OUTSIDE its category; type discipline = quarantine | **LIFTED-FROM-CURRY** (§6) | 06b §5.1; 06a §4 |
| Ill-typed-object refusal (a bare string is a *typing failure*, not an inference) + Node-or-Arrow admission gate | **LIFTED** (`PD`) | 06a §4.1 (`09/…/03_hom_sets_and_disjointness.tex:119-153`; `03_olog_node_arrow_law.tex:19-32`) |
| Fuel-bounded β-reducer + `Y` combinator kept OUT (runaway self-application quarantine) | **LIFTED** | 06a §4.2 (`33/…/08:436-471`; `Y` only in appendix-39 mirror) |
| Shape-category fencing (Yoneda/transport nodes NOT `subClassOf FormalType`, so shapes bite only in-category) + Frame self-seal (sealed `χχ`, not naive `N(χχ)`) | **LIFTED** + **SYN** (tie to §6) | 06c §1.6 (`taiji.ttl:848-852,371-376`; `realization.ttl:2848-2856`) |
| ContractGate `Accepted\|Rejected` unary gate = admission quarantine (governing law) | **LIFTED** | 06a §4.6 (`docs/unary-byte-frame-law.md:752-758`) |
| Präriehund provisional-naming (`silm:isProvisional`; the χ-obligation deferral) = the "no Frame for this thing" quarantine | **LIFTED** (governing law, cited by sha256) | 06a §4.4 (`docs/praeriehund-…:24,68`); 06b §5.2 |
| Institutional category machine + "rational mastery" = "category as dangerous master" | **LIFTED** ("rational mastery" + fixed-point countermodels) + **SYN** (the "dangerous master" gloss) | 06a §4.3 (`41/…/11:22-42`; the exact phrase is NOT in paper 41) |
| `fun:selfApplicationGuard` predicate (self-application admitted only through a typed gate; ungated `χχ`→provisional) | **SYNTHESIZED-FROM** Curry §6 ⊕ ContractGate ⊕ Präriehund (guard *existence* LIFTED; wiring is the build) | 06b §5.3, D-CURRY-5 |

---

## 2. GAP ANALYSIS — lifted vs synthesized vs pure-invention non-goal

The pillar's gap profile is **inverted** relative to strands 02/04: strand 02 has a pure GAP (the
Group inverse law, no Helios basis), strand 04 has an actively-refused GAP (point-set topology).
Here the honest picture is subtler and hinges on **whether Curry-as-source counts as a lift** —
which Directive 19 `:265-268` says it does. Under that pin, the taxonomy is:

**LIFTED (authored in Helios and/or committed green — faithful, `DS`/`PD`):**
- `F` = the unary Frame `T→Frame(O,E)` = Yoneda point (governing law + committed `isYonedaPoint`).
- `prim:Realization` = arrow inhabitant with dom/cod/effect (committed, teeth-green).
- The exponential `B^A` + currying + `eval`; the adjoint transpose `Hom(LG,A)≅Hom(G,RA)`, `f↔f̄`
  (paper 26, richly proved — the corpus's deepest currying anchor).
- The closed-λ engine: typed λ-term ontology with unary-Frame β-step, closed terms `FV=∅`,
  capture-avoiding substitution, β-motion Kleisli monad, fuel bound; Sparky map-shuffle-reduce;
  Lambda-Blotto free-term engine with its universal property.
- §4 **covariant** codomain: `prim:RealizationTransport` provable functor + identity/composition
  teeth; the two-sided Yoneda profiles.
- §6 quarantine (six independent authored anchors: ill-typed refusal, Node-or-Arrow gate, fuel
  bound + `Y`-out, shape-fencing + Frame self-seal, ContractGate, Präriehund provisional-naming).

**LIFTED-FROM-CURRY (a legitimate lift per Directive 19, but with NO Helios carrier — the honest
hybrid):**
- The **combinators B/C/W/K/I** and their axioms (FB)(FC)(FW)(FK).
- **`F_n`** (n-ary functionality, Def 2.1) and the **`Γ_m·B…` compositor** as a combinator ladder.
- Curry §5's **`F' ≡ [x,y,z](u)(xu ⊃ y(zu))`** and Thm 5.8 (the implication face's *definition*).
- §4's **contravariant-domain** variance law (the *law* is lifted; the *carrier* is a hard build).
- The mathematics is fact; what is missing is a Helios structure to hang it on. This is the pillar's
  characteristic gap-shape, and it is where 06a and 06b genuinely diverge (§1.B).

**SYNTHESIZED-FROM (fuse Curry + a committed floor — honest `SYN`, generated through a lifted
carrier, not hand-invented):**
- The Frame's **effect coordinate** as a monadic enrichment of Curry's bare `F` (ρ Kleisli effect).
- The **function-as-morphism** object filling 03's set-floor GAP (`F` at `NoEffect`).
- `fun:Functionality(X,X)` = the Monoid rung / endo-functionality (seam to 02 — LIFTED both sides,
  the *identification* is SYN).
- The **subtyping** reading of §4 as a committed tooth on `B^A` (ρ carries functorial variance; the
  exponential-constructor variance tooth is new).
- The **taiji packaging** of §5 (two-faced colimit atom + SP6 polysemy tooth).
- The `fun:selfApplicationGuard` predicate wiring.
- The "category as dangerous master" gloss (SYN of paper 41's authored "rational mastery").

**PURE INVENTION (no Curry, no Helios → candidate honest-red non-goals, flagged hard):**
- **None strictly** — 06b §6's claim that this pillar has no pure GAP holds *under the Curry-as-source
  pin*. The nearest things to invention are (i) the contravariant-domain variance *carrier* (§1.C —
  the law is Curry, but no Helios structure holds it, and materialising it may violate the unary
  law), and (ii) a first-class **implication object `F'`** (§1.D — the definition is Curry, the
  object is absent). Both are SYNTHESIZED-FROM a named Curry section ⊕ a committed anchor, so they
  are honest `SYN`/hard-build, not free invention. **Präriehund caveat:** if the maintainer declines
  the Curry-as-source pin for the combinators (treating "no Helios carrier" as decisive), then the
  combinator family, `F_n`, and the compositor **become pure invention** and the honest tag flips to
  GAP — which is precisely why DF-B is a genuine fork and not settled.

---

## 3. RE-ANCHOR PLAN (SP1 Frame/ρ/Yoneda → the pillar) + the tower/set-theory interlock

**Headline (06c §0, §2):** 3½ of the 4 load-bearing SP1 re-anchors are **ADDITIVE** (edges/
annotations onto committed, teeth-green structure); the 4th (Curry §4 contravariant domain) **NEEDS
NEW TEETH** and forces a governing-law decision. Concrete attach points (all `file:line` via 06c):

| # | Committed SP1 structure | Re-anchors as (functionality object) | Rating |
|---|---|---|---|
| F1 | `prim:Frame` product output×effect + `q_yoneda_point` (`formal.ttl:206-208`; `taiji.ttl:1994`) | Curry's `F` (codomain object) / Kleisli base — "Frame is F applied" | **ADDITIVE** (+ SP6 polysemy tooth: product-sense vs constructor-sense) |
| F2 | `prim:Realization` w/ `realizesFrom`/`frameOutput`/`frameEffect` (`realization.ttl:50-95`) | inhabitant `Z` of `FXY` (arrow w/ dom/cod/effect) | **ADDITIVE** (naming/annotation edge) |
| F3 | `prim:RealizationTransport` covariant functor + id/comp teeth (`realization.ttl:2865-2920`) | §4 **covariant codomain** variance carrier | **ADDITIVE** |
| F3′ | — (Frame has no input coordinate; `docs:686-687,689-694`) | §4 **contravariant domain** | **NEEDS NEW TEETH** (DF-D / D-1) |
| F4 | `prim:isYonedaPoint true` + `YonedaEvaluation` (`taiji.ttl:868-870,957-959`) | Frame = Yoneda point = F applied | **ADDITIVE** (annotation) |
| F5 | Kleisli unit η / `isMonadUnit` (`realization.ttl:82-89`); `IdentityArrow` (`formal.ttl:326-328`) | `F_0 = I` (compositor identity) | **ADDITIVE** |
| F6 | Kleisli `>=>` / transport / formal-arrow composition (`realization.ttl:2904-2920`; `formal.ttl:330-332`) | compositor `Γ`, `B` (compose) — binary half | **ADDITIVE** |
| F7 | shape-fencing + Frame self-seal (`taiji.ttl:848-852,371-376`; `realization.ttl:2848-2856`) | §6 type-discipline quarantine | **ADDITIVE** |
| F8 | `crs:CoordinateDerivation subClassOf prim:Realization` ("Kleisli arrow extending ρ") | SP3 coordinatization = a Curry-F-typed Kleisli arrow | **ADDITIVE** |
| F9 | exponential `B^A` (whitepaper zoo) — **NOT in `basicttl/`** | the function-type / internal-hom atom | **MINT (SYN)** |
| F10 | — (no B/C/W/K/`F_n`) | combinatory substrate | **pillar-lifts** (DF-B), not an SP1 re-anchor |
| F11 | — (no `⊃`/`F'`) | §5 implication face | **pillar-designs** (DF-C) |

**Edge mechanism** (same shape as `00_synthesis.md` 05 D6): prefer a dedicated
`funcfound:functionalityOf` / `funcfound:typesAsArrow` object property over bare `rdfs:subClassOf`
for the F-groundings (a callable *is typed by* `F`, it is not a *subtype* of it), reserving
`subClassOf` for genuine is-a (e.g. `prim:CompositeArrow rdfs:subClassOf funcfound:TypedArrow`).
Sequencing (consistent with `00_synthesis.md` D-C): **land the pillar as a strand of
`basicttl/algfound/`, then add edges — do not rebuild.** Every additive row above keeps SP1 green.

**Interlock with the algebra tower (02).** The load-bearing seam is `fun:Functionality(X,X)` = the
**endo-arrows on one object = a Monoid = a one-object category** — and Helios authors exactly this
(`End_C(X)` "a monoid as a one-object category", `21/…/04:2,16-17`; the fixed-Frame history monoid
`H_F=End_R(F)`, App36B). So the algebra tower's single genuinely-lifted rung (Monoid, `00_synthesis.md`
1.B) **is the endo-case of this pillar's arrow constructor** — the two strands share their spine, not
merely touch. A **Monoid = endo-functionality** (`fun:Functionality(X,X)` under `fun:Compositor` with
`fun:combinatorI`/η as unit); a **group action** = a monoid homomorphism into `End(X)` = a
functionality-into-endo-functionality arrow (the worked length homomorphism `|·|:M_X→(ℕ₀,+,0)`).

**Interlock with set theory (03).** `F` = `FXY` = "the type of functions X→Y" **fills 03's flagged
function-as-morphism GAP** (`03_set_theory.md:116-120`) exactly. The `F_n` arity index sits inside
03's finite-counting ordinal floor with **no transfinite cost** (each rung finite, countably indexed).
`U⊆X`/`Y⊆V` in §4 is 03's set-inclusion chain; the variance law is the contra/co-variance of
`Hom(-,-)` that Yoneda already trades on. And §6's quarantine is the **arrow-side of 03's
no-universe-set restraint** (03 keeps size an honest hypothesis, never a modeled universe; this pillar
keeps self-application type-gated, never a total arrow) — the two strands enforce one discipline from
two sides.

**Interlock with space (04):** the effect leg's ρ-monad is the same ρ 04's metric/enrichment route
uses (Lawvere enrichment over `([0,∞],≥,+)`), so the pillar's effect coordinate and 04's enriched
metric share the CommutativeMonoid seam (04 D4).

---

## 4. THE GENUINE MAINTAINER DECISIONS for THIS pillar (the forks only the maintainer settles)

Each fork is open *because the source genuinely leaves it open* (or, for DF-B, because the three
research notes genuinely disagree). Items Directive 19 or the Curry source already settles are in §5
as PINS, not offered as forks. These roll up the sub-decisions the notes raised (06a D-F1/D-F2/
D-F3/D-F4/D-F5; 06b D-CURRY-1…6; 06c D-1…D-4).

### DF-A — FRAMING: co-equal PILLAR, threaded LENS, or the primary anchor?
Since the Frame is *already everywhere* (`prim:Frame` is the base object the whole floor's realization
monad is the Kleisli category of), "where does functionality sit" is genuinely undetermined.
- **Opt 1 — Co-equal FOURTH PILLAR beside set/algebra/space (RECOMMENDED):** `basicttl/funcfound/`
  carries the ARROWS as a first-class strand of `basicttl/algfound/`. *Tradeoff:* matches Directive
  19's own division ("set theory the CARRIERS, algebra the OBJECTS/OPERATIONS, this pillar the
  ARROWS", `:276`) and its "co-equal fourth strand" wording (`:294-295`); clean seam story; but a
  strand-among-four understates how pervasively `F`=Frame already threads the floor.
- **Opt 2 — A LENS threaded through the other three (not its own floor):** functionality is an
  annotation layer (`funcfound:functionalityOf` edges) over set/algebra/space, no standalone atoms.
  *Tradeoff:* honest to "the Frame is already everywhere" and minimal invention, BUT loses the
  agnostic-progenitor home for the combinator family / variance tooth / taiji atom, and reads against
  Directive 19's "pillar"/"strand" language.
- **Opt 3 — The PRIMARY anchor (arrows-first, everything else hangs off `F`):** invert Directive 18's
  stack so the typed arrow is bedrock and carriers/objects are its dom/cod. *Tradeoff:* arguably the
  deepest truth (the Frame *is* the Yoneda point everything glues by), BUT directly contradicts
  Directive 18's "anchor on algebra `<<<<` set theory" ordering — a re-litigation of a settled
  directive, not this gate's to make.
- **Präriehund recommendation:** **Opt 1**, with an explicit acknowledgment (an SP6 note) that the
  pillar is *pervasive-but-co-equal* — it recognizes the already-committed Frame as `F` (§1.A) rather
  than building anew, so it is a strand in name and a spine in fact. Opt 3 is out (contradicts
  Directive 18); Opt 2 is the fallback if the maintainer wants zero new atoms in v1.

### DF-B — DEPTH for v1: how far into the combinator calculus? (the fork the notes SPLIT on)
Under corpus-agnostic v1 + YAGNI (`00_synthesis.md` D-B). This is the pillar's central open question,
and the three research notes give **different recommendations** (§1.B) — surfaced honestly.
- **Opt 1 — Minimal: `F` + §4 variance + the §5 implication-taiji + §6 quarantine, combinators
  CITE-ONLY (06a's recommendation):** mint the Functionality atom (recognize the Frame), the variance
  tooth, the taiji lexeme, the self-application guard; record B/C/W/K/I + `F_n` + compositor as a
  cite-only Curry orientation (like the Curry PDF itself). *Tradeoff:* faithful to the authored
  substrate (named-variable λ, not CL); no consumer needs point-free normal forms (YAGNI); lowest
  invention — everything minted is either LIFTED or SYNTHESIZED-onto-a-committed-carrier. BUT
  under-delivers on Directive 19's explicit listing of "the combinators B, C, W, K, I; `F_n`; the
  `Γ_m·B…` compositor" (`:273-274`).
- **Opt 2 — Full combinator calculus B/C/W/K/I (SKI/BCKW) as agnostic-progenitor atoms (06b's
  recommendation):** mint `fun:Combinator` progenitor + five composable children, each carrying its
  Curry axiom, on the Lambda-Blotto free-term engine. *Tradeoff:* honors Directive 17 ("do all, no
  privilege") and Directive 19's literal wording; and (via §4.3) buys most of the §5 implication
  face's proof-term algebra for free (K/C/W = the structural rules). BUT the combinators have NO
  Helios carrier — this is the pillar's largest genuine build, and treating it as a lift rests
  entirely on the Curry-as-source pin.
- **Opt 3 — Full spine + `F_n` n-ary ladder + the `Γ_m·B…` compositor, all teeth-proved:** Opt 2 plus
  the arity ladder as `prim:Ordinal`-indexed progenitor children and the compositor as a first-class
  arrow. *Tradeoff:* complete and maximally faithful to Directive 19's list, BUT most of `F_n`/the
  compositor is `LIFTED-FROM-CURRY`-onto-`GAP`-carrier with no v1 consumer — a YAGNI violation
  parallel to `00_synthesis.md` D-B Opt 3.
- **Präriehund recommendation:** **Opt 1 for v1**, with B/C/W/K/I + `F_n` + compositor recorded as
  honest-red cite-only Curry orientation, minted (Opt 2/3) only when a point-free consumer appears.
  Rationale: the authored substrate *is* λ not CL, so the faithful lift is `F` + variance + the
  λ-engine + the quarantine (all authored/committed); the combinators are the one place the pillar
  would invent-through-Curry with no carrier and no consumer. **I flag explicitly that 06b's Opt 2 is
  defensible on Directive-17 grounds** and that this is the sharpest maintainer call in the pillar —
  the notes do not agree, so the gate should treat it as fully open, not as my recommendation
  settling it. (Sub-decision 06a D-F1 / 06c D-3.)

### DF-C — the IMPLICATION / LOGIC layer: mint the §5 taiji now, or defer logic?
- **Opt 1 — Author the functionality↔implication taiji NOW (RECOMMENDED):** mint one SP6 lexeme
  `functionality` with two glossary senses — arrow-sense (`prim:Frame`/`prim:Realization`) and
  implication-sense (`F' = (u)(xu⊃y(zu))`) — teeth-proving only the `B^A ↔ A⊃B` direction the
  exponential already supports; mark full Thm-5.8 equivalence a cite. *Tradeoff:* this is the
  *cleanest* way to honor Directive 19's "taiji" wording (`:282-286`), and it is a *polysemy tooth on
  an existing object* (the exponential is authored), not a new structure — low invention, high
  Directive-16/19 coherence. BUT it introduces a logic sense (`⊃`, propositions-as-types) the corpus
  otherwise does not reason in.
- **Opt 2 — Mint a full proposition/negation/implication sub-floor per Curry §5-6 now:** a
  first-class `⊃` object, proof terms, propositions-as-types, negation (needed to state §6's Russell
  properly). *Tradeoff:* completes the Curry-Howard picture and gives §6's `χ≡[f]N(ff)` a real home,
  BUT is a substantial logic-layer build with no v1 consumer — over-reach, and it drags in the
  "functional character of negation" (Curry's Hp iii) the paradox turns on.
- **Opt 3 — Defer logic entirely; keep only the arrow sense now:** carry `prim:Frame`/`prim:Realization`
  as the arrow, record the implication sense as a glossary annotation only, defer the taiji to a later
  logic sub-project. *Tradeoff:* minimal, but leaves Directive 19's "taiji"/"same object" wording
  unhonored in v1.
- **Präriehund recommendation:** **Opt 1.** Author the taiji-lexeme (arrow-sense committed, implication-
  sense as the glued second face via the existing taiji reflexive seal `taiji.ttl:366-368`), teeth-prove
  only `B^A↔A⊃B`, cite Thm 5.8. This honors the "taiji" wording at polysemy-tooth cost. Note the
  coupling to DF-B: if Opt 2/3 of DF-B mints the combinators, the K/C/W proof-term algebra makes Opt 2
  here cheaper — so DF-B and DF-C should be settled together. (Sub-decision 06a D-F2 / 06b D-CURRY-4 /
  06c D-4.)

### DF-D — SP1 RE-ANCHOR: additive edges only, or add the §4 contravariant-domain variance teeth?
Directive 19 says the function-type algebra **MUST** carry §4 variance (`:279-281`) — so this is not
"whether" but **"how, given the unary law forbids an input coordinate for contravariance"** (06c D-1,
the load-bearing collision). The covariant leg is already committed (`RealizationTransport`); the
question is the contravariant leg.
- **Opt 1 — Additive edges only (covariant §4 leg + annotations), contravariant leg honest-red:**
  re-tag `RealizationTransport` as the §4 covariant-codomain functor, add the F-grounding edges, and
  defer the contravariant-domain tooth to W5 as an explicit honest-red deferral. *Tradeoff:* keeps
  every committed SP1 fact green, zero collision with the unary law, BUT ships an *incomplete* §4
  (covariant-only) against Directive 19's "MUST carry this variance."
- **Opt 2 — Separate arrow-type constructor object `F(dom,cod)` with the contravariant-domain teeth
  (06c D-1 Opt A, RECOMMENDED):** mint a pillar bifunctor `F` (contravariant `dom`, covariant `cod`)
  DISTINCT from `prim:Frame`-the-product; covariant half reuses `RealizationTransport`, contravariant
  half is new teeth; `prim:Frame` stays the covariant codomain-product it already is. *Tradeoff:*
  honors the unary law (input stays out of the Frame) AND delivers full §4, at the cost of a second
  arrow object + an SP6 "Frame" polysemy tooth (product-sense vs constructor-sense). Load-bearing,
  mirrors `00_synthesis.md` D-G's teeth-proven SealedGroup re-anchor.
- **Opt 3 — Give the Frame a contravariant input coordinate (`frameInput`/`frameDomain`)** (06c D-1
  Opt B): materialise §4 directly on `prim:Frame`. *Tradeoff:* cleanest single object, BUT
  **contradicts the unary law** (`docs:686-687`, "input never becomes an implicit fourth callable
  coordinate") — a violation to be realized-AS-violation, not a clean edge.
- **Opt 4 — Locate contravariance at the ContractGate frontier only** (06c D-1 Opt C): the input is
  typed at the ContractGate; carry the contravariant law there, off the Frame. *Tradeoff:* keeps the
  Frame unary/clean, but puts the §4 domain law outside SP1's committed floor entirely.
- **Präriehund recommendation:** **Opt 2** (separate `F(dom,cod)` constructor, teeth-proven). It keeps
  every committed SP1 fact green (additive), reuses the covariant functor already proved, delivers
  Directive 19's mandated full §4, and turns the unary-law collision into an honest SP6 polysemy tooth
  rather than a law violation (Opt 3) or an off-floor law (Opt 4). Formally the maintainer's call, and
  the single largest *new law* the pillar contributes. (Sub-decision 06c D-1/D-2; 06b D-CURRY-2.)

### DF-E (roll-up) — the effect enrichment and the self-application guard wiring
Two smaller forks the notes raised, folded here (each has a clear recommendation, low openness):
- **The effect coordinate (06b D-CURRY-1):** is `fun:Functionality` **Curry's F in the Kleisli
  category of the effect monad** (RECOMMENDED — matches `realization.ttl:9-21` exactly; Curry §5's
  `F'` is then the pure/`NoEffect` fragment; makes the pillar and SP1 *the same object*) or a bare
  2-arrow with effect bolted beside it (duplicates)? Recommend the Kleisli reading.
- **The self-application guard (06b D-CURRY-5 / 06c §1.6):** is §6 a **teeth-proven
  `fun:selfApplicationGuard`** (RECOMMENDED — gate self-application through a typed ContractGate,
  resolve the ungated `χχ` to `silm:isProvisional`) or a documented discipline only? Directive 19
  `:293` ("must make self-application type-disciplined, never naively self-applicable") argues
  teeth-proven.

---

## 5. PINS — what Directive 19 or the Curry source already SETTLES (not forks)

1. **The Frame IS Curry's `F`.** Directive 19 states the identification verbatim (`:270-273`:
   "Curry's `⊢FXYZ` … is exactly `F(x)→Frame(output:X, effect:Y)`"). The pillar RECOGNIZES the
   committed `prim:Frame`/`isYonedaPoint`/`prim:Realization` as `F`; it does not re-derive whether
   they are the arrow. Not open. (DF-A Opt 3 is foreclosed by this + Directive 18's ordering.)
2. **Curry is CITE-not-commit.** The 1936 mathematics is lifted as fact (`rdfs:seeAlso`/citation with
   jstage handle `tmj1911/41/0/41_0_371`); the journal scan is never committed (Directive 19
   `:265-268`). Not open.
3. **§4 variance MUST be carried.** Directive 19 `:279-281`: "the function-type algebra MUST carry
   this variance." So DF-D is *how/where* the contravariant leg attaches, never *whether*. Not open.
4. **Self-application MUST be type-disciplined, never naively self-applicable** (Directive 19 `:293`).
   The §6 quarantine is authored six ways (§1.E); only the guard's *wiring* (DF-E) is a call.
5. **The division of labor: set theory = CARRIERS, algebra tower = OBJECTS/OPERATIONS, this pillar =
   ARROWS** (Directive 19 `:276`). Fixes DF-A toward "co-equal strand" and the seam story (§3). Not open.
6. **Agnostic-progenitor, one-law-per-child, NEVER crammed** (Directive 17 + the corpus's
   one-clause-at-a-time discipline). Whatever DF-B mints uses this shape. Not open.
7. **DS/PD/SYN authority + Node-or-Arrow admission + render-artifact-as-violation** honesty machinery
   applies to every atom (inherited from `00_synthesis.md` §5 PINs 2-3). Not open.
8. **Polysemy is glossary-scoped (Directive 16), carried reflexively by SP6.** The pillar's polysemy
   teeth — `Frame` (product-sense vs F-constructor-sense), `functionality`/`arrow` (typed-arrow vs
   implication), `functionality` (arrow-sense vs implication-sense) — are teeth to CARRY, not
   decisions to make (06c D-4; `00_synthesis.md` §5 PIN 7). Not open.
9. **The seam to the algebra tower is fixed by the mathematics:** `fun:Functionality(X,X)` = the
   endo-functionality = a Monoid = a one-object category — both sides LIFTED (§3). The pillar and
   strand 02 SHARE their spine at the Monoid; this is not a design choice. Not open.
10. **`00_synthesis.md` §5 PIN 8 already reserved this pillar as the co-equal fourth strand** and
    named its re-anchor surface (SP1 ρ-functor + Frame/Yoneda). That reservation is honored here, not
    re-opened.

---

## 6. Coverage statement (Präriehund)

- **Read IN FULL for this synthesis:** the three pillar notes (`06a`, `06b`, `06c`) and
  `00_synthesis.md`; Directive 19 (`design_constraints.md:263-299`) and Directive 16/17/18 regions
  (`:160-199,225-261`) for the pin/framing boundaries.
- **Verified against the committed floor (spot-check, this session):** `prim:Frame prim:isYonedaPoint
  true` is the committed triple at `taiji.ttl:1994` (explanatory atom `957-959`); `prim:RealizationTransport
  a owl:Class` at `realization.ttl:2865`. This resolves a benign line-number divergence between the
  notes (06b cited `taiji.ttl:822/843` for the STEP-B/comment blocks; 06c's `realization.ttl:2865-2920`
  and `taiji.ttl:957-959,1994` are the accurate anchors and are the ones carried here).
- **Evidence provenance:** every `file:line` in §1-§3 is carried from the pillar note cited beside it;
  this synthesis re-cites via the notes rather than re-opening the corpus, per its synthesis scope
  (same discipline as `00_synthesis.md` §6).
- **The honest divergence surfaced, not smoothed:** the three notes genuinely DISAGREE on DF-B (06a:
  combinators cite-only; 06b: mint the full B/C/W/K/I + `F_n` progenitor; 06c: neutral pillar-lift).
  I report the split as an open fork with my lean (06a/Opt-1) clearly marked as *a lean, not a
  settlement* — the gate should treat DF-B as fully the maintainer's call. This is the pillar's
  sharpest genuine decision.
- **Honest limits inherited from the pillars:** the "combinators absent from the 34 authored papers /
  `Y` only in the external appendix-39 mirror" verdict, the "no Curry-Howard/implication identity"
  verdict, and the "§4 contravariant-domain has no SP1 carrier" verdict are the notes' grep-verified
  negatives (06a §9, 06b §9, 06c §4); no note exhaustively re-read all 34 papers or walked every
  per-object Yoneda/transport individual, so a hidden combinator/implication passage cannot be ruled
  out with certainty — flagged, not asserted away.
- **Decides nothing:** every §4 fork is left to the maintainer with options + tradeoffs + Präriehund-
  grounded recommendation (and, for DF-B, an explicit note that the recommendation is contested by the
  notes themselves); §5 pins only what Directive 19 / the Curry source already fixes.
