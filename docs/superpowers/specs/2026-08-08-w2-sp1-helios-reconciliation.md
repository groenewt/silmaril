# W2 · SP1 ↔ Helios reconciliation note (design-only)

> Präriehund honesty banner. This note weighs the **committed, green** SP1 Primitive Floor
> (`basicttl/primitives/` — formal/physical/realization/taiji + shapes/queries + README) against the
> **authored Helios source-of-truth** it re-derives (`helios/srcy/`, git-ignored). It **does not edit
> the SP1 floor** (Directive: floor is committed; corrections are relaunch-items, not now-fixes).
> It records where SP1 is faithful, where it diverges from the authored structures and must be
> weighed, and a per-divergence verdict with the exact SP1 file/line and what would change. Every
> divergence is *flagged, not invented* — where a gap is defensible at SP1's altitude I say so.

---

## 1. Goal

Produce the reconciliation **verdict** the SP2–SP9 batch needs before it consumes SP1: a precise
statement of (a) which SP1 constructs are already-faithful liftings of Helios, (b) which SP1
constructs assert *more* than Helios authorizes (or read a Helios structure loosely) and must be
weighed, and (c) for each divergence, whether the honest disposition is **already-faithful**,
**now-fix-in-wording**, or **relaunch-item** — the last being the only lawful category for the
committed floor, since SP1 is frozen this iteration (Directive 13: "this iteration's v1 … will be
fundamentally challenged/relaunched later"). The verdict is corpus-agnostic (Directive 13) and
carries no authoring; it is a ledger the relaunch reads. (**D1's disposition is a fourth category the
maintainer's Directive 16 ruling introduces — polysemy-resolved:** the "colimit" divergence is
**dissolved, not deferred**, by scoping the word to a glossary sense — see §2b/§2c. D2/D3 stay
relaunch-items; D4 stays already-faithful.)

Authored sources lifted (read in full for this note):
`srcy/base/00_whitepaper/sections/00_helios_foundation/04_olog_yoneda_points.tex` (Yoneda point law),
`…/05_carrier_towers_triad.tex` (disjoint Atlas/Graph carriers + independent S/O/P towers),
`…/06_frame_sort_separation.tex` (the six disjoint frame-sorts), and
`srcy/node_arrow/Silmaril_NodeArrow_Corpus_Monograph_v12.md` §Introduction/Part-I (the honest-cocone
law `W = ObservedProjection(ColimCandidate(D))`).

---

## 2. Architecture — the reconciliation, structure by structure

### 2a. Where SP1 ALIGNS with Helios (already-faithful liftings)

Each of these is a genuine lift; no change is recommended.

| Helios authored structure (source) | SP1 realization (teeth-proven) | verdict |
|---|---|---|
| **Frame = Yoneda point.** unary law (`docs/unary-byte-frame-law.md` L36–38) "The frame is the Yoneda point at which the callable's one observed input maps to its output and typed effect"; §04 Yoneda point law `Nat(yA,F)≅F(A), η↦η_A(1_A)`. | `taiji.ttl` STEP-C fold: `prim:Frame prim:isYonedaPoint true`; ρ target tied to Yoneda evaluation at the representable (`q_yoneda_point`, `q_yoneda_evaluation_sound`). | **already-faithful** — SP1 lifts the exact identification the unary law authors, and backs it with an evaluation-soundness ASK (realization = Yoneda evaluation), not merely prose. |
| **Frame(O,E) := O×E** — output×typed-effect product, §06 sort #5 (L53). | `prim:Frame` with `prim:frameOutput` / `prim:frameEffect` (the `Realization → …` pair); `q_frame_effect` requires both on every `Realization`. | **already-faithful** — SP1 models exactly the `O×E` product, no other content smuggled into it. |
| **Monadic realization** — App B monad morphism/strength; Directive-3 refinement "twin ologs with realization functors, EXTREMELY MONADIC", ρ a Kleisli arrow. | `realization.ttl` ρ as Frame-monad Kleisli arrows; `prim:KleisliCompositionShape` + `q_kleisli_welltyped`; two-sided unit + associativity (`q_monad_unit`/`q_monad_assoc`) over reified well-typed compositions. | **already-faithful** — the monad is *proven* (well-typedness bites; the DEFECT-1 η-at-codomain fix is genuine), not decorated. |
| **Presented olog is a category; Yoneda fully faithful.** §04 def/prop (`Path(G)/∼R` is a category) + Cor (yoneda fully faithful, `yX≅yY ⇔ X≅Y`). | `formal.ttl` thin (poset) category: 59 `SubtypeArrow` + 60 `IdentityArrow` + 45 `CompositeArrow`; `taiji.ttl` literal Yoneda: 60 representables, 59 `YonedaArrow`, 59 `NaturalitySquare`; `q_yoneda_faithful` (injective) + `q_yoneda_full` (bijection Hom↔Nat). | **already-faithful** — SP1's faithful+full probes are exactly §04's Corollary made into biting graph facts in the thin case. |
| **RGB and S/O/P kept separate; no positional `S→R/O→G/P→B`.** §05 L21–23 (K_S,K_O,K_P independent) + Prop "TOWERS positional-collapse obstruction" (L88–109). | `q_rgb` asserts the code space is *exactly* Red/Green/Blue octets (ordinal 0..255), with **no** role assignment; SP1 carries no `S→R` map and seeds S/O/P geometry only as `CRS`/`Coordinate` formal objects handed to SP3. | **already-faithful** — SP1 neither collapses colour into roles nor asserts the forbidden maps; it correctly leaves the three tower categories to SP3's altitude. |
| **Functor / presheaf / naturality.** §04 (contravariant representable `yX=Hom(−,X)`; presheaf `F:C^op→Set`). | `taiji.ttl` `prim:RepresentablePresheaf` (`A↦Hom(−,A)`), ρ as natural transformation `yo⇒R` with pinned `RhoComponent` corners, `q_naturality_commutes` (vacuous-match escape closed). | **already-faithful.** |

### 2b. Where SP1 DIVERGES and must be weighed

Four divergences. Each names the authored source, the SP1 site, and the precise tension.

**D1 — "colimit" is POLYSEMOUS (Directive 16): the per-primitive sense SP1 earns vs the
corpus-artifact honest cocone `W = ObservedProjection(ColimCandidate(D))`.**
The monograph (`node_arrow/…v12.md` L35–38) states the *anti-cheating* honesty law verbatim:
> "The honest authority claim is **not** `W = colim(D)`, because this document is still a rendered
> artifact and not the substrate itself. The honest claim is `W = ObservedProjection(ColimCandidate(D))`."

SP1 names the atom a colimit: `README.md` L11 ("a **twin-olog colimit taiji**"); `taiji.ttl` L11 ("a
`prim:Primitive` **is the colimit object** over the small [twin-olog diagram]"), L87 (`prim:Primitive`
comment: "it is ONE thing glued from two facets … **Because the gluing is a colimit it is mutual**").
The maintainer's ruling (Directive 16, "Polysemy!") is that this is **NOT** an over-claim to be
earned-vs-renamed-vs-deferred: **"colimit" is a polysemous term whose sense is glossary-scoped**, and
the mole-of-glossaries (SP6) carries it reflexively — exactly Directive 1's "synonyms AND antonyms
across distinct epistemologies," applied to our OWN vocabulary:
- **LOCAL / per-primitive glossary sense (SP1's).** SP1's diagram is a *two-object* finite diagram
  (FormalType ─ρ→ PhysicalEncoding), whose colimit *can be constructed literally* — its **universal
  property is provable**. There the word "colimit" is **genuinely earned**, via a `q_colimit_universal`
  tooth (initiality among cocones as a biting ASK) *in addition to* the mutual **reflexive seal** SP1
  already proves (`physicalFacet → interpretAs → formalFacet` a true identity — `q_colimit_reflexive`,
  `prim:ColimitReflexivityShape`). Teeth-not-trust, enrich-not-strip: the word stays, the tooth is
  added — no ASK in the current 21-ASK suite yet tests universality, so the tooth is the SP1↔Helios
  relaunch-item that *earns* this sense.
- **CORPUS / artifact glossary sense (SP9's).** For the whole rendered artifact the same lexeme
  denotes `ObservedProjection(ColimCandidate(D))` — the monograph's honest cocone, "still a rendered
  artifact and not the substrate itself." SP9 keeps this sense; it does not claim the whole-graph
  render is literally a colimit.
- **SP6 holds "colimit" as ONE lexeme with BOTH glossary-scoped senses simultaneously**, with a
  biting polysemy tooth. SP2/SP6 reference "colimit" **through the glossary layer, not bare**; SP9
  keeps the honest-cocone sense.
So the earlier "over-claim" framing is superseded: the local sense is not stronger than the teeth show
once `q_colimit_universal` is added, and the corpus sense is a *different glossary entry* of the same
word, not a contradiction. **The whole-vs-per-primitive scope is settled by the glossary split, not by
a single global choice** (open question #1 below, now resolved by Directive 16).

**D2 — "frame" is ONE of six disjoint frame-sorts; SP1's `prim:Frame` is unmarked.**
§06 (def "Disjoint frame sorts", L6–66) makes "frame" **six disjoint sorts** with *no implicit map
between them*: `F_cap` (capture/provenance keys), `F_auth` (authoring/lens variants),
`𝔽_lin=(F,id,ρ,parent,kind,meta,≺,succ)` (native lineage/time), `P_I` (JEPA image regions),
`Frame(O,E):=O×E` (L53), `T_vid` (video time). SP1 correctly models **only** the `Frame(O,E)` sort —
but names it the bare `prim:Frame` with no sort-discriminator, and globally labels it "the Yoneda
point" (`taiji.ttl` L41–42; `q_yoneda_point`). The Yoneda-point *identification* is faithful (D-row
in §2a — the unary law authors it). The divergence is the **naming/sort collision risk**: §06's
whole point is that lexical reuse of "frame" induces no map; a downstream consumer (SP2's tensor/byte
`native_frame_urn`, SP4's projection frames) reading a bare `prim:Frame` could silently identify it
with `F_cap`, `𝔽_lin`, `P_I`, or `T_vid`. SP1 provides no `owl:disjointWith` fence and no
`prim:frameSort` marker naming this as the `O×E` sort.

**D3 — Atlas `Q_A` and Graph `Q_G` are STRICTLY DISJOINT; taiji.ttl leans on an "Atlas & Graph
colimit" that the source does not author.**
§05 (L11–23) constructs `Q_A={aTag}×RGB×Vec(Oct)`, `Q_G={gTag}×RGB×Vec(Oct)` with **`Q_A∩Q_G=∅`**
(L17) and states the relationship explicitly: "Erasing the outer tag is a **many-to-one forgetful
operation, not an equality of carriers**"; the five-factor carrier (def §05, L336–361) is a
**product** `K_A×K_G×K_S×K_O×K_P` with **no cross-tag hom-sets**. So Atlas and Graph are kept
**disjoint** (a product with a forgetful map *down* to a shared payload) — they are precisely **not**
glued/identified by a colimit. Yet `taiji.ttl` L16 justifies calling the per-primitive gluing a
colimit by analogy to "**the unary law's Atlas & Graph colimit**". `taiji.ttl` does not model
`Q_A`/`Q_G` at all (no carrier classes, no `owl:disjointWith`, no aTag/gTag; "Atlas" appears only in
prose at L16 and L239). Two weighing points: (i) the analogy at L16 **misreads** the source — §05
disjoins Atlas/Graph, it does not colimit them; (ii) not modeling `Q_A`/`Q_G` in SP1 is itself
**defensible** (disjoint byte-carriers are SP3's carrier-tower altitude, not the numeric floor's).

**D4 — the three S/O/P tower categories are INDEPENDENT with no maps to RGB.**
§05 L21–23: `K_S,K_O,K_P` are three independent role-tower categories; L88–109 proves colour
position cannot recover them. **SP1 is faithful and correctly silent** here — it models no
`K_S/K_O/K_P` (SP3 owns them) and asserts no colour→role map. Listed as a divergence only to record
that a reader might *expect* the towers in SP1 and find them absent; that absence is correct
altitude, not a gap.

### 2c. RECOMMENDATION per divergence

| # | verdict | exact SP1 site | what would change (relaunch-item unless noted) |
|---|---|---|---|
| **D1** | **polysemy-resolved** (Directive 16; the earn-vs-rename-vs-defer framing is superseded) | `README.md` L11; `taiji.ttl` L11, L87 (and every per-primitive `rdfs:comment` asserting "Because the gluing is a colimit it is mutual") | "colimit" is **glossary-scoped polysemous**. SP1 **earns the LOCAL / per-primitive sense** by adding a colimit **universal-property tooth** — a `q_colimit_universal` ASK / `prim:ColimitUniversalShape` witnessing that any cocone `(formalFacet→W←physicalFacet)` factors uniquely through the Primitive (the two-object diagram makes universality *actually provable*) — kept distinct from the `q_colimit_reflexive` seal it already proves. The **CORPUS / artifact sense** stays the monograph's honest cocone `ObservedProjection(ColimCandidate(D))` (SP9). **SP6 carries both senses of the one lexeme simultaneously** with a biting polysemy tooth; SP2/SP6 reference "colimit" through the glossary layer, SP9 keeps the cocone sense. Whether the `q_colimit_universal` tooth lands now or at relaunch is a build-time call (Directive 13); the polysemy itself is settled. |
| **D2** | **relaunch-item** (naming) — the Yoneda-point identification is **already-faithful** | `taiji.ttl` prim:Frame decl (STEP-C fold, ~L41); `physical.ttl`/`realization.ttl` where `prim:Frame` is referenced | Add a `prim:frameSort prim:FrameSort_OutputEffect` marker on `prim:Frame` and an `owl:disjointWith` fence against the other five §06 sorts (declare `prim:FrameSort_Capture`, `_Authoring`, `_NativeLineage`, `_ImageRegion`, `_VideoTime` as sibling sorts even if unpopulated this iteration), so a consumer cannot lexically identify `prim:Frame` with `𝔽_lin`/`F_cap`/`P_I`/`T_vid`. No change to the Frame=Yoneda-point content. |
| **D3** | **relaunch-item** (loose analogy) — non-modeling of `Q_A`/`Q_G` is **already-faithful** at SP1 altitude | `taiji.ttl` L16 (and the L239 "Atlas ring" aside) | Drop or correct the "unary law's Atlas & Graph **colimit**" analogy: §05 keeps Atlas/Graph a **disjoint product** with a tag-erasure **forgetful** map, not a colimit. Replace the justifying analogy with the correct one (OSSIE YIN/YANG twin, already cited alongside it at L16, which *is* a mutual-gluing shape). When SP3 lands `Q_A`/`Q_G`, model them with `owl:disjointWith` (`Q_A∩Q_G=∅`) + the many-to-one forgetful map to the shared `Vec(Oct)` payload — never a colimit that identifies them. |
| **D4** | **already-faithful** (no change) | n/a (SP1 correctly silent; SP3 `taiji.ttl` L220/L263 seeds `CRS`/`Coordinate`) | Record in the SP3 hand-off that `K_S/K_O/K_P` are independent tower categories with **no** RGB positional map; SP1's `q_rgb` + role-silence is the correct floor and SP3 must not add `S→R/O→G/P→B`. |

Secondary observation (low-priority relaunch note, not a numbered divergence): §04's closing law —
"a URN, file name, pixel patch, latent vector, or generated manifest does **not** become a Yoneda
point by being observable … only through a typed arrow with a declared probe domain" — means a bare
`prim:Frame prim:isYonedaPoint true` **flag** is the very "observable ⇒ Yoneda point" shortcut §04
warns against. SP1 largely escapes this because `q_yoneda_evaluation_sound` (60 evaluations, 0
mismatches) carries the real content (realization = Yoneda evaluation at the representable); the flag
is redundant. Relaunch could demote the flag and keep only the evaluation-soundness tooth.

---

## 3. File layout — which SP1 file each verdict touches

This note authors **no `.ttl`/`.sparql`**. It is one markdown verdict at
`docs/superpowers/specs/2026-08-08-w2-sp1-helios-reconciliation.md`. The verdicts *point at* (never
edit) committed floor files, one concern per pointer:

- `basicttl/primitives/README.md` — D1 wording ("twin-olog colimit taiji").
- `basicttl/primitives/taiji.ttl` — D1 (L11/L87 colimit assertion), D2 (`prim:Frame` sort marker),
  D3 (L16 Atlas/Graph-colimit analogy).
- `basicttl/primitives/realization.ttl`, `physical.ttl` — D2 (`prim:Frame` references to fence).
- `basicttl/primitives/primitives.shapes.ttl` / `primitives.queries.sparql` — D1 (where a
  `q_colimit_universal` / `prim:ColimitUniversalShape` would be added on relaunch).

Namespace unchanged: `prim: <urn:silmaril:prim:#>` (full-lexical URN, unary law).

---

## 4. Verification plan — how a relaunch would prove each verdict discharged

Design-only (no execution here); these are the probe shapes the relaunch would add, each **proven to
bite by injection** in the SP1 idiom (positive ASK false on empty graph; `FILTER NOT EXISTS`
universal flips false under a targeted violating triple):

- **D1** — `q_colimit_universal` (EXPECT-TRUE): for the two-object diagram, any cocone
  `formalFacet→W`, `physicalFacet→W` factors through a **unique** mediating arrow to `prim:Primitive`.
  Bite test: inject a second, non-isomorphic mediating arrow → ASK `True→False`. This tooth **earns
  the LOCAL / per-primitive glossary sense** of the polysemous "colimit" (Directive 16); the CORPUS /
  artifact sense stays SP9's honest cocone `ObservedProjection(ColimCandidate(D))`, and SP6 holds both
  senses of the lexeme with its own biting polysemy tooth.
- **D2** — `prim:FrameSortDisjointShape` (`sh:sparql`): every `prim:Frame` carries exactly one
  `prim:frameSort`, and the six sorts are pairwise `owl:disjointWith`. Bite test: a `prim:Frame` with
  two sorts, or a sort lacking the disjointness axiom → `conforms True→False`.
- **D3** — `q_atlas_graph_disjoint` (SP3-side, EXPECT-TRUE): `Q_A ∩ Q_G = ∅` materialized as
  `prim:AtlasCarrier owl:disjointWith prim:GraphCarrier`, plus the forgetful map to the shared
  payload is many-to-one (two distinct tagged carriers, one payload target). Bite test: assert
  `Q_A ≡ Q_G` or a cross-tag hom → `True→False`.
- **D4** — reuse SP1's existing `q_rgb` (already green) + an SP3 `q_no_role_colour_map` asserting no
  `prim:sRole prim:mapsTo prim:Red`-shaped triple exists. Bite test: inject `S→R` → `True→False`.

Depth gate unaffected (this note is markdown, not an `owl:Class` source).

---

## 5. Interfaces

**Consumes:**
- The committed SP1 floor: `basicttl/primitives/{README.md, formal.ttl, physical.ttl,
  realization.ttl, taiji.ttl, primitives.shapes.ttl, primitives.queries.sparql}` (21 ASKs, 13
  SHACL shapes, green run).
- Authored Helios source: `srcy/base/00_whitepaper/sections/00_helios_foundation/{04_olog_yoneda_points,
  05_carrier_towers_triad, 06_frame_sort_separation}.tex`; `srcy/node_arrow/Silmaril_NodeArrow_Corpus_Monograph_v12.md`
  (honest-cocone law §Intro/Part-I).
- `docs/unary-byte-frame-law.md` (Frame = Yoneda point; Frame(O,E)); `ledger/W2/design_constraints.md`
  (Directives 1, 3, 3-refinement, 13); the six `ledger/W2/helios/*_map.md` facet maps.

**Produces:**
- The reconciliation **verdict ledger** (§2c table): D1 polysemy-resolved (Directive 16 — "colimit"
  is glossary-scoped polysemous: SP1 earns the LOCAL / per-primitive sense via the `q_colimit_universal`
  tooth, SP9 keeps the CORPUS / artifact honest cocone, SP6 carries both senses of the one lexeme); D2
  relaunch-item (frame-sort marker + disjointness fence; Yoneda-point identification already-faithful);
  D3 relaunch-item (correct the Atlas/Graph-"colimit" analogy; Q_A/Q_G disjointness is SP3's to model);
  D4 already-faithful (RGB and S/O/P kept separate; no positional map).
- Two hand-offs the SP2–SP9 batch reads: (i) SP2/SP4 must treat `prim:Frame` as the `O×E` sort only,
  never as native-lineage/capture frame (D2); (ii) SP3 must model `Q_A`/`Q_G` as a **disjoint
  product** with a forgetful map, and the S/O/P towers with **no** RGB positional map (D3/D4).

---

## 6. Non-goals + genuine open questions (Präriehund — flagged, not invented)

**Non-goals.** Editing the committed, green SP1 floor (frozen this iteration; all four verdicts are
relaunch-items, not now-fixes). Re-deriving Helios (SP1 already did; this only reconciles). Any
live-corpus binding (W5). Authoring `Q_A/Q_G`, `K_S/K_O/K_P`, or the five extra frame-sorts (SP3 /
later — this note only says *how* they must relate).

**Open questions (genuinely undecidable this iteration; do not force-fit):**
1. **D1 depth — RESOLVED by Directive 16 (the polysemy ruling).** The question was whether the
   monograph's "not literally colim" hedge binds a finite, teeth-proven *per-primitive* colimit or
   only the *corpus-level* `W`. The maintainer's answer is "Polysemy!": neither sense overrides the
   other — "colimit" is **glossary-scoped polysemous**. The hedge governs the CORPUS / artifact
   glossary (`W = ObservedProjection(ColimCandidate(D))`, SP9's sense); the LOCAL / per-primitive
   glossary earns the literal colimit via the `q_colimit_universal` tooth (SP1's sense); SP6 holds
   both simultaneously with a biting polysemy tooth. Whole-vs-per-primitive scope is settled by the
   glossary split, not a single global choice. (No longer an open question — recorded here as the
   answer.)
2. **D2 scope:** should SP1 declare all six §06 frame-sorts (five unpopulated) purely to carry the
   `owl:disjointWith` fence, or is a single `prim:frameSort` marker on the populated `O×E` sort
   enough to block lexical collapse? Unresolved — depends on whether SP4/telephone frames will
   populate the other sorts this relaunch or a later one.
3. **D3 ownership:** does `Q_A/Q_G` disjoint-carrier modeling belong to SP3 (S/O/P CRS) or a distinct
   carrier-tower sub-project? The facet maps place Atlas/Graph byte carriers near the S/O/P towers
   (`00b` "independent S/O/P tower product and Atlas/Graph RGB byte pair"), suggesting SP3, but the
   render-layer maps also touch it. Flagged for the batch review, not decided here.
