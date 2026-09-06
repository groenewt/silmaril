# 06c — SP1's Frame/ρ/Yoneda apparatus RE-ANCHORED onto the FUNCTIONALITY pillar (Directive 19)

> Präriehund honesty banner. This is brainstorming-gate RESEARCH for the functionality / typing /
> combinatory-logic pillar (Directive 19, `ledger/W2/design_constraints.md:263-299`), the co-equal
> FOURTH strand of the algebra ← set-theory foundation. It authors NOTHING in `basicttl/`, runs no
> state-changing git, and DECIDES nothing on the maintainer's behalf. Every structural claim is
> tagged **LIFTED** (present verbatim in a committed SP1 file, with `file:line`), **SYNTHESIZED-FROM**
> (a faithful extension of a named SP1 structure or the Curry (1936) extract), or **GAP** (no SP1
> anchor — pure invention, flagged hard). Stays consistent with `00_synthesis.md` (the taiji-via-engine,
> agnostic-progenitor, DS/PD/SYN honesty machinery) and its §5 PIN 8 (this pillar is the fourth strand).
>
> Curry source (maintainer-supplied, cite-not-commit): H. B. Curry, *First Properties of Functionality
> in Combinatory Logic*, Tôhoku Math. J. **41** (1936) 371–401, jstage `tmj1911/41/0/41_0_371`.

---

## 0. One-paragraph verdict the gate is being asked to rule on

SP1 already carries **three of the four load-bearing functionality structures as committed, teeth-checked
graph facts**, and it carries them at exactly the tightness Directive 19 wants: `prim:Frame` IS the typed
arrow object the whole floor's realization monad is the Kleisli category of (LIFTED); `prim:Realization`
IS the F-inhabitant `T ⤳ Frame(output:X, effect:Y)` with an explicit domain (`realizesFrom`), codomain
(`frameOutput`) and effect (`frameEffect`) (LIFTED); `prim:isYonedaPoint true` on `prim:Frame` is the
"Frame = Yoneda point = Curry's F applied" identification, materialised through `prim:YonedaEvaluation`
(LIFTED). The ONE place SP1 does **not** already match Curry is the **§4 subtyping-variance law**. SP1's
`prim:RealizationTransport` is a **genuine, provable COVARIANT functor** on the subtype order
(`A⊆B ⟹ ρ(A)→ρ(B)`, with a materialised identity law and composition law) — this is a faithful re-anchor
for Curry's **covariant-codomain** half. But SP1 has **no contravariant-domain structure at all**, and
this is not an oversight the pillar can patch with an edge: the unary Frame law deliberately makes the
callable's *input* NOT a Frame coordinate (`docs/unary-byte-frame-law.md:686-687,689-694`), so there is
no domain slot for contravariance to live on, and `prim:Frame` is a *product* (`output × effect`,
covariant in both) rather than a function-type constructor with a contravariant argument. **Net for the
gate:** 3 of 4 re-anchors are ADDITIVE (edges/annotations onto committed structure); the 4th (Curry §4
contravariant domain) NEEDS NEW TEETH and forces a genuine maintainer decision about whether to give the
Frame an input/domain coordinate at all — a decision that collides head-on with the unary law's
"input is never a fourth callable coordinate."

---

## 1. THE ATTACH POINTS (file:line), each tagged and rated ADDITIVE / NEEDS-NEW-TEETH

### 1.1 `prim:Frame` → Curry's functionality operator `F` ("Frame is Curry F applied")

**Evidence.** `prim:Frame a owl:Class ; rdfs:subClassOf prim:FormalType` — "the unary law's Yoneda point:
the typed product of an output coordinate and exactly one error-or-effect coordinate that a callable
returns around a byte stream. Frame is the formal type that the realization monad ρ is the Kleisli
category of … It is a product like Tuple but with the two coordinates fixed as output and effect."
(`basicttl/primitives/formal.ttl:206-208`). The unary law: `T -> Frame(output: X, error|effect: Y)`
(`docs/unary-byte-frame-law.md:29`); "The Frame remains the physical Yoneda point for one such input
stream. Its one output and one error/effect coordinate separately descend through the same identified
byte-carrier system." (`docs/unary-byte-frame-law.md:689-694`).

**Curry map.** Curry `⊢ FXYZ` = "Z is a function from X to Y". Directive 19: this IS
`F(x) → Frame(output:X, effect:Y)`. So the corpus callable = Curry's `Z`; the input byte-stream = Curry's
domain `X`; and the `Frame(output, effect)` result = Curry's codomain `Y`. `prim:Frame` is the **codomain
object** of the callable and the base object of the arrow's monad.

**Rating: ADDITIVE at the identification level, but note the polysemy.** — **LIFTED** that `prim:Frame`
is the typed product output×effect and the Kleisli base. **SYNTHESIZED-FROM** (pillar) the identification
`prim:Frame = Curry F applied`. **Präriehund pin (SP6 glossary tooth):** `prim:Frame` is authored as a
**product** (`formal.ttl:206-208`, "a product like Tuple"), which is COVARIANT in both coordinates; Curry's
`F` is an **arrow/function-type constructor**, which is CONTRAVARIANT in its domain. These are two glossary
senses of one lexeme "Frame": *Frame-as-codomain-product* (SP1's committed sense) vs *Frame-as-F-arrow-
constructor* (the pillar's sense). The re-anchor must carry both senses, not silently equate them.

### 1.2 `prim:Realization` → the F-inhabitant / typed arrow `T ⤳ Frame(X,Y)`

**Evidence.** `prim:Realization a owl:Class` — "a Kleisli arrow of the Frame monad … it IS a Frame, the
unary law's Yoneda point T -> Frame(output: X, error|effect: Y), so it declares prim:realizesFrom (its
source formal type), prim:encoding / prim:frameOutput (its target encoding = the Frame output X), and
prim:frameEffect (the typed cost Y)" (`basicttl/primitives/realization.ttl:93-95`). The three coordinates:
`realizesFrom : Realization -> FormalType` (the arrow's source/domain, `realization.ttl:50-56`);
`frameOutput : Realization -> PhysicalEncoding` (= Curry codomain output X, `realization.ttl:68-74`);
`frameEffect : Realization -> Effect` (= Curry codomain effect Y, `realization.ttl:76-80`).

**Curry map.** A realization ρ carries a **domain** (`realizesFrom` = the formal type T being realized)
and a **codomain** (`frameOutput` + `frameEffect`). This is a fully-coordinatised inhabitant of the arrow
type — Curry's `Z` in `⊢FXYZ`, given as a first-class object with dom/cod/effect. The monad's
**polymorphism** (one T `realizesAs` many arrows) is the type-theoretic fact that a domain admits many
typed maps.

**Rating: ADDITIVE.** — **LIFTED** (the arrow object with dom/cod/effect exists and is teeth-checked by
`q_frame_effect` / `RealizationShape`). The pillar's re-anchor is a naming/annotation edge (mark ρ an
F-inhabitant); no new teeth.

### 1.3 `prim:RealizationTransport` → Curry §4 subtyping variance — **THE crux; check performed**

**Evidence.** `prim:RealizationTransport a owl:Class` — "The image under the realization functor rho of
ONE arrow of the thin formal category … a genuine morphism rho(arrowDom) -> rho(arrowCod) in the physical
carrier category … it promotes rho from a bare object map (type -> carrier) to a real FUNCTOR ON MORPHISMS"
(`basicttl/primitives/realization.ttl:2865-2867`). For every `prim:SubtypeArrow f: A ⊆ B` there is a
transport `ρ(f): ρ(A) → ρ(B)` (`realization.ttl:2829-2831`). The **functor identity law** is a real edge:
`prim:isTransportIdentity true` with `transportDom = transportCod = ρ(A)`, one per object
(`realization.ttl:2898-2902`, teeth `q_functor_identity`). The **functor composition law** is a real edge:
`prim:transportComposeFirst / …Second / …Into` reifying `ρ(g∘f) = ρ(g)∘ρ(f)`
(`realization.ttl:2904-2920`, teeth `q_functor_composition`). `prim:rhoObject` pins the single canonical
carrier per type so the transport is well-typed (`realization.ttl:2874-2878`).

**Curry §4 map.** Curry: `⊢FXY`, `U⊆X`, `Y⊆V` ⟹ `⊢FUV` — **contravariant** in the domain X,
**covariant** in the codomain Y (axioms `(FP)₁`,`(FP)₂` via inclusion `P*`/`⊃`). Under the Frame map
(§1.1): Curry codomain Y = the Frame output carrier; Curry domain X = the callable's input stream.

- **COVARIANT CODOMAIN — SP1 ALREADY HAS IT.** `A ⊆ B ⟹ ρ(A) → ρ(B)` is exactly the covariant direction:
  a value of the subtype A is a value of B, so its output carrier `ρ(A)` embeds/widens into `ρ(B)`. SP1
  materialises this as a **provable functor**, not prose — identity + composition laws are teeth-checked
  edges (`realization.ttl:2898-2920`). This is a faithful, ADDITIVE re-anchor for Curry §4's covariant
  codomain. **SYNTHESIZED-FROM** `prim:RealizationTransport` (the direction and functor laws are LIFTED;
  the identification with §4 covariant-codomain is the pillar's synthesis). *Honest caveat:*
  `RealizationTransport` is the covariance of the realization functor ρ over the WHOLE subtype poset, not
  literally the covariance of an F-constructor in its second argument — the two coincide in direction and
  content (subtype widens → carrier widens), which is why the re-anchor is faithful, but the equation
  "RealizationTransport = §4 covariant-codomain functor" rests on the §1.1 `Frame = F` identification.

- **CONTRAVARIANT DOMAIN — SP1 HAS NOTHING; NEEDS NEW TEETH (hard GAP).** Curry §4 requires the arrow
  type to be **contravariant in the domain** (`U⊆X ⟹ FXY-inhabitants restrict to FUV`). SP1 has **no
  structure carrying this**: (a) the Frame is a *product* output×effect (`formal.ttl:206-208`), covariant
  in both coordinates — there is no contravariant argument; (b) the callable's *input/domain* is **not a
  Frame coordinate at all** — the unary law states the host input "never becomes an implicit fourth
  callable coordinate" (`docs/unary-byte-frame-law.md:686-687`) and the Frame is "the physical Yoneda
  point for one such input stream" with only "one output and one error/effect coordinate"
  (`docs/unary-byte-frame-law.md:689-694`); (c) `RealizationTransport` transports covariantly and is the
  only variance-bearing arrow in SP1. **There is no place for contravariant-domain variance to attach.**
  This is a hard GAP, not an additive edge — see decision D-1.

**Rating: SPLIT. Covariant codomain = ADDITIVE (already a provable functor). Contravariant domain =
NEEDS NEW TEETH / hard GAP.**

### 1.4 The Kleisli monad → Curry's functionality COMPOSITION (`F_n`, the `Γ_m·B…` compositor)

**Evidence.** The realization monad ≡ the Frame monad; realizations compose by Kleisli composition, unit
`prim:realize_unit` is the identity Kleisli arrow (`realization.ttl:9-36`); `prim:isMonadUnit` flags the
identity/unit η with `kDom = kCod` and `prim:NoEffect`, witnessing the two-sided unit law
(`realization.ttl:82-89`). On the transport (functor-on-arrows) side, composition is reified edge-for-edge
(`transportComposeFirst/Second/Into`, `realization.ttl:2904-2920`), and the formal-olog side has its own
`prim:CompositeArrow` composition (`formal.ttl:330-332`), with `prim:IdentityArrow id_T` the unit
(`formal.ttl:326-328`).

**Curry map.** Curry Def 2.1: `F_0 = I`, `F_1 = F`, `F_{n+1} = (C.BB_{n+1})F_1F_n`; the compositor
`Γ_m·B…` composes functionalities. SP1's **monad unit η** re-anchors onto `F_0 = I` (the identity arrow
`prim:IdentityArrow` / `k_id_*`); SP1's **Kleisli `>=>` composition** re-anchors onto the compositor Γ
(composition of functionalities); SP1's **single F** is `prim:Frame` / `F_1`.

**Rating: PARTIAL — identity + binary composition ADDITIVE; n-ary `F_n` and the B/C/W/K compositor = GAP.**
— **SYNTHESIZED-FROM** (η↔I, Kleisli-compose↔Γ). **GAP:** the combinatory substrate proper (B compose,
C swap, W duplicate, K constant; the graded `F_n` family) is **not in SP1's primitive floor** — it lives
in the corpus's closed-λ "Lambda"/Sparky engine (Lambda-Blotto, `ledger/W2/helios/srcy_map.md:121-124,
227-228`; "Lambda-Blotto combinators", `docs/unary-byte-frame-law.md:670`). SP1 supplies only `I`
(identity arrow) and `B`-flavoured composition (Kleisli/transport/formal-arrow composition, all three
materialised); `C`, `W`, `K` and `F_n` have no SP1 anchor. This is the pillar's own substrate to lift,
not an SP1 re-anchor — flagged so the gate does not mistake SP1's monad for the full compositor.

### 1.5 `prim:isYonedaPoint` → Frame = Yoneda point = functionality applied

**Evidence.** `prim:Frame prim:isYonedaPoint true` — "Marks the formal type that IS the Yoneda point of
the unary law … tying the categorical Yoneda point (the identity element at which representables are
evaluated to yield realization carriers) to the physical Frame the whole floor's realization monad is the
Kleisli category of" (`basicttl/primitives/taiji.ttl:957-959`). The evaluation machinery:
`prim:YonedaEvaluation` evaluates `yo(A)` at its Yoneda point `id_A` and yields `ρ(A)` = "the byte-carrier
that is the frameOutput of A's realization Frame" (`taiji.ttl:868-870`); each `prim:RhoComponent` "IS
realization-as-Yoneda-evaluation" (`taiji.ttl:860-862`); the naturality square's bottom edge
`prim:natTransport` IS the `prim:RealizationTransport ρ(f)` (`taiji.ttl:921-923`, `864-866`).

**Curry map.** "Frame is Curry's F applied" (Directive 19) = evaluating the representable at its Yoneda
point yields the Frame output = **F applied at the identity point gives the codomain carrier**. The Yoneda
evaluation at `id_A` (`taiji.ttl:868-870,957-959`) is the "F applied" step; the realization = evaluation
identity (`prim:evalComponent`, `taiji.ttl:949-951`) is the point-free content of "the arrow IS its value
at the universal element."

**Rating: ADDITIVE.** — **LIFTED** (the Frame-is-Yoneda-point identification and the evaluation machinery
are committed and teeth-checked). The pillar edge is annotation only (Yoneda point = functionality-applied).

### 1.6 (touch points, not the task's focus) Curry §5 implication-taiji and §6 quarantine

- **§5 (functionality ↔ implication, Curry–Howard ancestor).** SP1's ρ `T ⤳ Frame(X,Y)` is the concrete
  "function type" object; SP1 carries **no explicit implication `⊃` object** and no `F' ≡ [x,y,z](u)(xu ⊃
  y(zu))` definitional equality. **GAP** for the implication face; the arrow object it must be glued to is
  LIFTED (`prim:Realization`). This is a genuine polysemy taiji (one arrow, two senses: typed-arrow vs
  universally-quantified implication), an SP6 glossary tooth, designed by the pillar not here.

- **§6 (paradox quarantine by type discipline).** SP1 already materialises a **type-discipline quarantine**:
  the Yoneda/transport nodes are deliberately NOT `rdfs:subClassOf prim:FormalType`, so
  `DualGroundingShape` / `RealizationShape` / `KleisliCompositionShape` never fire on them
  (`taiji.ttl:848-852`; `realization.ttl:2848-2856`) — a shape only "bites" inside its proper category,
  exactly Curry §6's "the contradiction arises only from applying functionality OUTSIDE its category."
  SP1's self-reference is likewise type-disciplined, not naively self-applicable: `prim:prim_Frame` is
  "the carrier of the realization monad by which EVERY other primitive on this floor is glued (each
  prim:gluedBy arrow is itself a Frame), so sealing Frame's own taiji closes the floor's self-reference"
  (`taiji.ttl:371-376`) — a sealed, category-respecting `χχ`, not the naive `N(χχ)`. **SYNTHESIZED-FROM**
  (the quarantine machinery is LIFTED; the tie to Curry §6 is the pillar's synthesis). Ties to
  ContractGate branching-quarantine + Präriehund provisional-naming (Directive 19, `:288-293`).

---

## 2. SUMMARY TABLE — re-anchor status

| SP1 structure (file:line) | Curry / functionality object | Status | Rating |
|---|---|---|---|
| `prim:Frame` product output×effect, Kleisli base (`formal.ttl:206-208`) | `F` = functionality operator (codomain object) | LIFTED + SYN (F-id) | ADDITIVE (w/ polysemy tooth) |
| `prim:Realization` w/ `realizesFrom`/`frameOutput`/`frameEffect` (`realization.ttl:50-95`) | inhabitant `Z` of `FXY` (arrow w/ dom/cod/effect) | LIFTED | ADDITIVE |
| `prim:RealizationTransport` covariant functor `ρ(A)→ρ(B)` + identity/composition laws (`realization.ttl:2865-2920`) | §4 **covariant codomain** | LIFTED (functor) + SYN (§4 id) | ADDITIVE |
| — (Frame has no input coordinate; `docs:686-687,689-694`) | §4 **contravariant domain** | **GAP** | **NEEDS NEW TEETH** |
| Kleisli unit η / `isMonadUnit` (`realization.ttl:82-89`); `IdentityArrow` (`formal.ttl:326-328`) | `F_0 = I` | SYN | ADDITIVE |
| Kleisli `>=>` / transport / formal-arrow composition (`realization.ttl:2904-2920`, `formal.ttl:330-332`) | compositor `Γ`, `B` (compose) | SYN | ADDITIVE |
| — (no B/C/W/K combinators, no `F_n`) | combinatory substrate B/C/W/K, `F_n` | **GAP** (lives in Lambda/Sparky, `srcy_map.md:121-124`) | pillar-lifts, not SP1 |
| `prim:isYonedaPoint true` + `YonedaEvaluation` (`taiji.ttl:868-870,957-959`) | Frame = Yoneda point = F applied | LIFTED | ADDITIVE |
| — (no explicit `⊃` / `F'` equality) | §5 implication taiji | GAP (arrow LIFTED) | pillar-designs |
| shape-category fencing + Frame self-seal (`taiji.ttl:371-376,848-852`; `realization.ttl:2848-2856`) | §6 type-discipline quarantine | SYN | ADDITIVE |

---

## 3. MAINTAINER DECISIONS THIS RAISES (brainstorming forks)

**D-1 (the load-bearing one) — how to materialise Curry §4 CONTRAVARIANT DOMAIN, given the unary law
forbids an input coordinate.** Curry §4 needs the arrow type to be contravariant in its domain, but the
unary Frame law states the callable input "never becomes an implicit fourth callable coordinate"
(`docs/unary-byte-frame-law.md:686-687`) and the Frame is output×effect only (`formal.ttl:206-208`).
Options:
- **Opt A — separate arrow-type constructor object.** Mint a pillar object `F(dom, cod)` (a genuine
  bifunctor: contravariant `dom`, covariant `cod`) DISTINCT from `prim:Frame`-the-product, with the
  contravariant-domain teeth on it; keep `prim:Frame` as the covariant codomain-product it already is.
  Covariant half re-uses `RealizationTransport` (`realization.ttl:2865-2920`); contravariant half is new.
  Honours the unary law (input stays out of the Frame) at the cost of a second arrow object + an SP6
  "Frame" polysemy tooth (product-sense vs constructor-sense).
- **Opt B — give the Frame a contravariant input coordinate.** Add `frameInput`/`frameDomain` to the Frame
  product and a contravariant transport on it. Directly materialises §4 on `prim:Frame`, but **contradicts
  the unary law** (`docs:686-687`) — likely a violation to be realised-as-violation, not a clean edge.
- **Opt C — locate contravariance at the ContractGate frontier only.** The input is typed at the
  ContractGate frontier (`docs:685-686`); carry the contravariant-domain law there, off the Frame.
  Keeps the Frame unary and clean, but puts the §4 domain law outside SP1's committed floor entirely.
- *Präriehund lean:* **Opt A** — it keeps every committed SP1 fact green (additive), reuses the covariant
  functor already proved, and turns the collision into an honest polysemy tooth rather than a law violation.
  Formally the maintainer's call.

**D-2 — is `prim:RealizationTransport` re-tagged as the §4 covariant-codomain functor (an additive
`prim:isCovariant`-style annotation / `subClassOf` edge onto the pillar's variance law), or left as-is
with the pillar carrying the §4 law separately and merely citing the transport as its witness?** Both are
additive; the question is whether the variance law is authored ON the transport or beside it.

**D-3 — where does the combinatory substrate (B/C/W/K/I, `F_n`) come from?** SP1 supplies only `I`
(`IdentityArrow`) and `B`-flavoured composition. `C`/`W`/`K`/`F_n` are absent from the primitive floor and
present in the closed-λ Lambda/Sparky engine (`srcy_map.md:121-124,227-228`). Decision: lift the substrate
from that engine and glue SP1's identity/composition into it, or author a fresh combinator floor under the
foundation. (Consistent with `00_synthesis.md` D-A: lift the ENGINE, don't hand-invent.)

**D-4 — the §5 implication taiji and the `Frame`/`F` polysemy.** Confirm that "Frame" (product vs
F-constructor), "arrow" (Realization-as-typed-arrow vs Realization-as-implication), and the §4 variance
carry as SP6 glossary-scoped polysemy teeth (per `00_synthesis.md` §5 PIN 7), designed by the pillar's own
synthesis note, not resolved here.

---

## 4. Coverage statement (Präriehund)

- **Read for this note:** `design_constraints.md` (Directives 18/19 in full) and `algebra_foundation/
  00_synthesis.md` in full; `basicttl/primitives/taiji.ttl` (header §8-55, colimit atoms incl.
  `prim_Frame` §371-376, the full STEP C literal-Yoneda layer §815-971); `basicttl/primitives/
  realization.ttl` (header §9-36, the monad properties §44-95, the full STEP B functor-on-arrows layer
  §2820-2999); `basicttl/primitives/formal.ttl` (`prim:Frame` §206-208, the FormalArrow/SubtypeArrow/
  IdentityArrow/CompositeArrow layer §318-381); `docs/unary-byte-frame-law.md` (§29, §660-699);
  `ledger/W2/helios/srcy_map.md` (Lambda/Sparky/Blotto §121-124,174-228,304-310).
- **NOT exhaustively read:** the full 1994-line taiji.ttl and 4058-line realization.ttl bodies (per-atom
  rows and the ~60 per-object Yoneda/transport individuals) were sampled by targeted grep, not line-by-line;
  a hidden variance annotation somewhere in the individuals cannot be ruled out with 100% certainty —
  flagged, not asserted away. The §4 contravariant-domain GAP is asserted on the *shape/class* layer
  (no `frameInput`, no contravariant transport class exists), which the greps did cover.
- **Decides nothing:** §3 forks are left to the maintainer with options + Präriehund lean; the covariant
  half is reported as already-committed fact, the contravariant half as a hard GAP needing new teeth.
