# W2 · Algebra/Set-Theory Foundation — Pillar 03: SET THEORY (the bedrock algebra anchors on)

> Präriehund honesty banner. This is a brainstorming-gate RESEARCH note. It reports, with
> file:line evidence, what the authored Helios source-of-truth (papers 18 + 14, read IN FULL,
> plus corpus greps and the committed SP1/SP2/SP3 floors) provides toward an explicit
> **set-theory floor**, and where the genuine GAPS and DECISIONS are. It authors NOTHING under
> `basicttl/`. It does NOT force-fit a lift not in the source, and it does NOT invent structure.
> Where I sampled rather than read in full, I say so.

Directive served: **Directive 18** — *"we anchor on algebra … `<<<<` Set theory (magma → abelian
groups and all in between, as well as space constructs!)"*. Set theory (sets, elements, functions,
relations, products/coproducts/disjoint unions, power sets, ordinals/cardinals — **including the
space constructs**) is named the **deepest anchor**, beneath algebra, beneath SP1–SP3.

Coverage: papers/18_presheaf_semantics (all flat `sections/` + chapters 01/03/04/05/09 read in
full; chapters 02/06/07/08/10/11/12 read at thesis/structure depth) and papers/14_yoneda_lemma
(sections 01_thesis + 06_closure in full; chapters confirmed by structure). Corpus-wide greps for
Set / coproduct / disjoint-union / powerset / cardinal / ordinal / membership / space. Committed
floors `basicttl/primitives/{formal,realization,taiji}.ttl`, `basicttl/aob/group_law.ttl`,
`basicttl/crs/README.md` inspected for what set-theoretic structure already exists.

---

## 0. Headline finding (the honest lift-vs-synthesize verdict)

**The corpus is category-theory-FIRST and treats `Set` as an AMBIENT, ASSUMED background — it is
never CONSTRUCTED.** Every presheaf is a functor `P : C^op → Set`; `Set` is the fixed codomain in
which assertion populations, hom-sets, and restriction functions live. The corpus provides the
complete **categorical shadow** of set theory (elements of `P(A)`, functions `P(f)`, the category
of elements `∫P`, products, coproducts/disjoint unions, an initial and a terminal object, a
subobject classifier, hom-sets, size/local-smallness hypotheses) but it authors **no axiomatic
set-theory primitives** (membership as a first-class typed relation, extensionality, pairing,
union, power set, foundation/replacement, ordinals/cardinals-as-sets).

Consequently, for Directive 18's "set theory beneath algebra":
- **LIFTABLE (faithful, in the source):** a *structural* set-theory floor — `Set` as the codomain
  category with its accessed structure (elements, functions, function composition + identity,
  finite products, coproducts/disjoint unions, initial `Void` / terminal `Unit`, category of
  elements, hom-sets, subobject classifier). Much of this is **already materialized in SP1**
  (`prim:Set/Bag/Tuple/Sum/Map/List`, the thin formal category, representable presheaves, the
  Yoneda embedding + evaluation, `PresheafOlog = PSh(FormalOlog)`).
- **SYNTHESIS-REQUIRED (NOT in the source — do NOT invent):** a *material* / axiomatic (ZFC-style)
  set-theory floor with first-class `∈`, power set, transfinite ordinals/cardinals; and the
  *point-set* reading of "space constructs" (open sets, metrics, vector-space axioms). The corpus
  gives only the categorical/sheaf-theoretic reading of "space" (a site + Grothendieck topology +
  sheaf condition), never point-set topology/metric/normed/vector *spaces*.

This is itself the central maintainer decision (see §5): **structural (ETCS-flavored, liftable) vs
material (ZFC-flavored, synthesized)** set theory, and whether the "Set floor" is a NEW artifact or
a RECOGNITION/consolidation of structure SP1 already carries.

---

## 1. How "Set" appears — the presheaf codomain and the category of sets

### 1.1 `Set` as the fixed codomain of every presheaf
The page-thesis of paper 18 makes the assertional interpretation of an olog a functor into `Set`:

- `P : C^op → Set` — *"the assertional interpretation is a presheaf"*; for each schema object `A`,
  `P(A)` *"contains the assertions whose type is A"*; for each schema arrow `f:A→B`, the
  contravariant action `P(f):P(B)→P(A)` *"pulls assertions at B back to assertions at A."*
  `helios/srcy/papers/18_presheaf_semantics/sections/01_thesis.tex:24-31`
- Concept card **presheaf**: `P : C^op → Set` is *"a functor"*; `P(A)` is *"the set of admitted
  assertional elements of type A"*; admitted as a functor-category object in `[C^op, Set]`.
  `.../sections/01_thesis.tex:59-68`
- **Forbidden collapse (load-bearing for the gap):** *"the presheaf P is the same as the set of
  elements P(c)"* — dropping the contravariant action and *"collaps[ing] functoriality into static
  labelling"* — is named *"the cheese-trap face this volume is most exposed to."*
  `.../sections/01_thesis.tex:65-68`. I.e. **a presheaf is explicitly NOT a set**; the corpus
  polices the very identification a naive set-floor might make.

### 1.2 `Set` as an ambient category, used but never built
- Functoriality statement: *"A presheaf of observations is a functor `P : C^op → Set`"*, objects
  are typed contexts, arrows admissible context maps; the two functor laws
  `P(id_C)=id_{P(C)}` and `P(v∘u)=P(u)∘P(v)`.
  `.../chapters/01_functoriality_theorem/sections/01_statement.tex:12-34`
- The Kan-adjoints proof asserts `Set` **is complete and cocomplete** — used as a *background fact*
  to get pointwise left/right Kan extensions: *"Set is complete and cocomplete, so the pointwise
  left and right Kan extensions … exist."*
  `.../chapters/05_sieves_and_kan_restriction/sections/03_kan_restriction_adjunction.tex:38-40`
- The Yoneda failure-mode audit types every object *"in C, Set, or the presheaf category; no object
  of a separate category B enters without additional interface data."*
  `.../chapters/03_yoneda_lemma_for_presheaves/sections/04_failure_modes.tex:28-31`

**Reading (Präriehund):** `Set` is the metatheoretic ground the whole construction stands on, taken
as given (complete, cocomplete, locally small target). It is exactly the "deepest anchor" Directive
18 points at — but the corpus never descends *into* it. That descent is the foundation's job.

---

## 2. Set-theoretic primitives — available or implied, with evidence

### 2.1 Sets, elements, membership (∈)
- Elements + membership appear **operationally** as one of the six admissible Node-or-Arrow items:
  *"an assertional element `x ∈ P(A)`"*.
  `.../sections/03_olog_node_arrow_law.tex:10-11,40-41`
- Explicit set-builder + membership in the **category of elements**:
  `Ob(∫P) = {(c,x) | c ∈ Ob(C), x ∈ P(c)}`; a morphism `(c,x)→(d,y)` is an arrow `f:c→d` with
  `x = P(f)(y)`.
  `.../chapters/04_density_and_cocompletion/sections/01_category_of_elements.tex:10-20`
- **Verdict:** membership/element are *used* (the symbol `∈`, set-builder braces) but are **never
  first-class typed primitives** — no `prim:membership` edge, no `prim:Element` class. Grep of the
  floors for a membership/element/function/relation primitive returns **nothing** in
  `basicttl/primitives/*.ttl` (only `sh:in` list-membership inside SHACL, and prose `ℕ₀` "set
  theory" glosses). SP1's `prim:Set` is a *collection data type* (a `prim:Bag` with multiplicities
  capped at one), NOT the category `Set` and NOT axiomatic membership.
  `basicttl/primitives/formal.ttl:184-190` (Bag→Set), `formal.ttl:58` (`ℕ₀`, "the reading used by
  set theory").

### 2.2 Functions
- Presheaf actions **are** functions between sets: `P(f):P(B)→P(A)` (the restriction / pullback /
  lookup maps), with composition `P(g∘f)=P(f)∘P(g)` and `P(1_A)=1_{P(A)}`.
  `.../sections/01_thesis.tex:93-103`, `.../sections/03_olog_node_arrow_law.tex:52-64`
- SP1 has `prim:Map` — *"a finite set of key-to-value entries … a partial function from a key type
  to a value type"* — the nearest thing to a function primitive, but modeled as a data dictionary,
  not as a Set-morphism object. `basicttl/primitives/formal.ttl:192-196`
- **Verdict:** functions exist categorically (as `Set`-morphisms `P(f)`) and as a data map, but
  there is **no first-class "function = functional relation" set-theory primitive** with a
  domain/codomain/graph. This is a genuine gap.

### 2.3 Relations
- Relations are modeled as **typed arrows**, never as subsets of a product: e.g. the ownership
  relation `owns : Person → DomesticCat`, admitted only after its endpoints, the arrow, and the
  induced lookup `P(owns)` are declared; *"a mass measurement is not a scalar glued directly to the
  cat"*. `.../sections/03_olog_node_arrow_law.tex:19-30`
- **Verdict:** the classical "relation ⊆ A×B" primitive is **absent by design** — the corpus's
  Node-or-Arrow discipline *replaces* relations-as-subsets with typed arrows. Synthesizing a
  relation-as-subset primitive would run against the authored discipline; flag as a decision.

### 2.4 Products
- Data products: `prim:Tuple` (product), `prim:Unit` (*"the terminal object of the formal category
  … the empty product, the nullary Tuple"*), and the Frame `= O×E`.
  `basicttl/primitives/formal.ttl:168-171,218-222` (Unit), and the Frame class
  `formal.ttl:210-214`.
- Categorical products/pairs: ordered pairs `(c,x)` in `∫P`
  (`.../04_density_and_cocompletion/sections/01_category_of_elements.tex:11-16`); the SP3
  five-factor product `K = K_A×K_G×K_S×K_O×K_P` with its `π_j` joint-faithfulness seal
  (`basicttl/crs/README.md:37-38`).
- **Verdict:** products are **well-covered** (data Tuple + terminal Unit + Frame product + CRS
  product). Liftable as-is.

### 2.5 Coproducts / disjoint unions
- Data coproduct: `prim:Sum` — *"a sum type, coproduct, or tagged union … the categorical dual of
  the Tuple product"*; `prim:Void` — *"the initial object of the formal category … the empty
  coproduct, the nullary Sum"* (dual-grounded to a genuinely uninhabited 0-byte encoding).
  `basicttl/primitives/formal.ttl:198-201,216-217`
- **`colimit ≠ disjoint union` is authored explicitly.** Paper 19's whole thesis (mereology as
  colimit) distinguishes the *coproduct/disjoint union* from a general *colimit*
  (pushout/coequalizer that glues overlaps): `helios/srcy/papers/19_mereology_as_colimit/...`
  (srcy_map line 103: *"pushout/coequalizer as atomic gluing; colimit ≠ disjoint union"*). Paper 09's
  music colimit says the universal claim *"require[s] … a coproduct construction"* it does not
  supply. `.../09_minimal_category_theory/chapters/04_limits_and_colimits/sections/04_colimit_worked_example.tex:57-62`
- SP1's representable hom-set is described as *"the disjoint union over all objects X of Hom(X,A)"*.
  `basicttl/primitives/formal.ttl:381`
- **Verdict:** coproduct/disjoint-union is present in **two distinct senses** — the *data tagged
  union* (`prim:Sum`) and the *universal construction* (Set coproduct / disjoint union, explicitly
  held apart from a general colimit). This is a genuine **polysemy** (feeds SP6, see §5 D-SET-5).

### 2.6 Power sets
- **No classical power-set primitive.** The presheaf-topos analogue is the **subobject classifier**
  `Ω`: `Ω(C) = {sieves on C}`, with pullback action `u*S = {f:X→C | u∘f ∈ S}`, classifying every
  monomorphism `Q ↪ P` by a sieve-valued characteristic map `χ`.
  `.../chapters/05_sieves_and_kan_restriction/sections/02_subobject_classifier.tex:7-32`
- Crucial boundary: `Ω(C)` is *"generally a set of many sieves, not one Boolean truth value"*.
  `.../02_subobject_classifier.tex:50-52`. So subobjects are classified by **sieve-valued**
  (many-valued, intuitionistic) truth, NOT by the classical 2-element Boolean whose Sub(X) ≅ 2^X.
- Sieves are *"subfunctors of representables"*, `S ↪ yC`, closed under precomposition
  (`.../sections/01_sieves_as_subfunctors.tex:16-21`).
- **Verdict:** power set is present ONLY as the topos subobject classifier (sieve-valued). The
  classical `2^X` power set is **absent** and, in a presheaf topos, would be a different (Boolean)
  object. Do not silently mint `2^X`; decide (§5 D-SET-1).

### 2.7 Ordinals / cardinals
- `prim:Ordinal` is an **enum** ordinal — *"a finite named set of members that additionally carries
  a total order … modelled as a subclass of Enumeration"* — **NOT** a von Neumann set-theoretic
  ordinal. `basicttl/primitives/formal.ttl:276-279`; sibling `prim:Categorical`
  (`formal.ttl:280-282`).
- Natural-number sub-objects: `prim:NaturalWithZero` (`ℕ₀`, *"the reading used by set theory …
  and the recursive positive-count authority whose Unit denotes one and whose Successor(previous)
  denotes the next count"*) and `prim:NaturalWithoutZero` (`ℕ⁺`).
  `basicttl/primitives/formal.ttl:58,62`
- Cardinality at the byte floor (unary law): the 8-bit code space has **cardinality 256**, value
  **ordinal 0..255**, and a **recursive positive Count** authority `Unit`/`Successor(previous)`
  realized through 256 — with Count 256, ordinal 255, bit-width 128 kept as three distinct
  coordinates. `docs/unary-byte-frame-law.md:721-729`. Helios has a `cardinality` agnostic
  progenitor `{one,maybe,many,unresolved}` (srcy_map line 270).
- Size discipline: papers 14/18 require `C` **locally small** (hom-*sets*) and the free
  cocompletion carries explicit **declared size hypotheses** (`C` small, `E` locally small
  cocomplete). `.../papers/14_yoneda_lemma/sections/01_thesis.tex:42` (locally small);
  `.../18_.../chapters/04_density_and_cocompletion/sections/03_free_cocompletion.tex:10-13`
- **Verdict:** only **finite / counting** ordinals+cardinals exist (enum order + the Peano-style
  successor Count realized through 256). There is **no transfinite set theory** — no `ℵ`, no
  ordinal/cardinal-as-set, no universe object. Local-smallness/size is an honest *hypothesis*, never
  a modeled universe. Building transfinite cardinals would be **invention** for a corpus that never
  motivates them.

---

## 3. Yoneda's contribution (paper 14 + paper 18 ch03) to the set-theory reading

- The Yoneda lemma is authored as a **bijection of SETS**: `Φ_{A,P}: Nat(Hom(-,A),P) → P(A)`,
  `τ ↦ τ_A(id_A)`, inverse `a ↦ (f ↦ P(f)(a))`.
  `.../18_.../chapters/03_yoneda_lemma_for_presheaves/sections/01_statement.tex:19-33`; covariant
  `Nat(Hom(X,-),F)≅F(X)` and contravariant `Nat(Hom(-,X),F)≅F(X)` in
  `.../14_yoneda_lemma/sections/01_thesis.tex:42-57`.
- **Quantifier discipline** (directly relevant to a set floor): *"Yoneda gives a bijection of sets.
  Each natural transformation corresponds to exactly one element, but `P(A)` need not be a
  singleton."* `.../18_.../chapters/03_.../sections/01_statement.tex:48-52`; and the rejection test:
  Yoneda *preserves the cardinality of `P(A)`* rather than forcing it to one; does not make `P`
  representable; does not import an object of a separate category `B` without interface data.
  `.../chapters/03_.../sections/04_failure_modes.tex:6-32`
- The Yoneda embedding `y:C ↪ [C^op,Set]`, `X ↦ Hom(-,X)`, is **full and faithful** — the local
  "identity law": an object is known up to iso by its representable interface, and *"X ≡ Hom(-,X)"*
  is *"useful only as shorthand"*, NOT literal equality.
  `.../14_yoneda_lemma/sections/01_thesis.tex:75-102`
- Density + free cocompletion (paper 18 ch04): every presheaf is a **colimit of representables**,
  `P ≅ colim_{(c,x)∈∫P} y(c)`; `[C^op,Set]` is the **free cocompletion** of `C` under declared size
  hypotheses. `.../chapters/04_density_and_cocompletion/sections/02_density_theorem.tex:22-33`,
  `.../sections/03_free_cocompletion.tex:10-33`.

**This is exactly what SP1 already materializes** (`prim:repr_<A>=Hom(-,A)`, `prim:yonedaObject`,
`prim:yonedaPoint`, `prim:YonedaEvaluation`, `prim:PresheafOlog = PSh(FormalOlog)` whose *"objects
are ologs (a presheaf is a Set-valued diagram, i.e. an olog)"*).
`basicttl/primitives/taiji.ttl:870-899,937-955`. The set-theoretic content Yoneda needs — hom-sets,
elements of `P(A)`, cardinality preservation — is present and teeth-checked one level up.

---

## 4. What the committed floors ALREADY carry toward a set floor (recognition, not invention)

SP1 `basicttl/primitives/formal.ttl` already contains most of a **structural** set-theory floor,
typed as the *formal-type tower* rather than labeled "set theory":

| Set-theory notion | Present as (SP1) | file:line |
|---|---|---|
| collection / set | `prim:Bag` (multiset) → `prim:Set` (mult ≤ 1) | formal.ttl:184-190 |
| ordered tuple / product | `prim:Tuple`; terminal `prim:Unit` (empty product) | formal.ttl:168-171,218-222 |
| coproduct / disjoint union | `prim:Sum`; initial `prim:Void` (empty coproduct) | formal.ttl:198-201,216-217 |
| partial function / map | `prim:Map` | formal.ttl:192-196 |
| sequence / vector / tensor | `prim:List`/`prim:Vector`/`prim:Tensor` | formal.ttl:172-183 |
| ordinal / categorical (finite) | `prim:Enumeration`→`prim:Ordinal`/`prim:Categorical` | formal.ttl:270-282 |
| ℕ₀ / ℕ⁺ | `prim:NaturalWithZero` / `prim:NaturalWithoutZero` | formal.ttl:58,62 |
| hom-set, thin category | `prim:SubtypeArrow`/`IdentityArrow`/`CompositeArrow`, representable hom-sets | formal.ttl:381,497-524,681-710,891-922 |
| Yoneda / presheaf apparatus | `prim:repr_<A>`, `prim:yonedaObject/Point`, `prim:PresheafOlog=PSh` | taiji.ttl:870-955 |
| a genuine GROUP (algebra) | `aob:SealedGroup` with identity/compose/inverse/associativity teeth + a proven colimit universal property | aob/group_law.ttl:44-100,268-281,391-401 |

So Directive 18's "re-anchor SP1–SP3 onto a set floor" is, in large part, a **RE-LABEL + CONSOLIDATE
+ GAP-FILL** exercise over structure that already exists, not a from-scratch build. The genuine
gaps to fill are: first-class **membership** edge, **function-as-morphism** object (domain/codomain/
graph), and an explicit **coproduct/product-as-universal-construction** distinct from the data
`Sum`/`Tuple` (the aob group law already shows the pattern: a construction with a *proven* universal
property + teeth).

---

## 5. Space constructs (Directive 18 puts these IN the set-theory bedrock)

- The corpus's notion of "space" is **categorical / point-free**: a **site** = a category with a
  **Grothendieck topology `J`** (covering sieves), and the **sheaf condition** (every matching
  family over every covering sieve has exactly one amalgamation), expressed in representable form as
  a restriction bijection `Nat(yC,P) → Nat(S,P)`.
  `.../18_.../chapters/09_sheaves_and_sheafification/sections/02_sheaf_condition.tex:9-67`
- Sheaf gluing (local→global on overlap agreement) is authored in paper 25; JEPA "topology" (Vol 06)
  is a **patch-cover cocone**, again categorical (srcy_map lines 90, 316). `prim:Vector`/`prim:Tensor`
  exist as **data shapes**, NOT as vector *spaces* (no field, no axioms). `formal.ttl:172-183`.
- **Verdict:** the **site/sheaf** reading of "space" is fully liftable; the **point-set** readings
  (open-set topology, metric spaces, normed/inner-product/vector spaces as set-with-structure +
  axioms) are **NOT in the source** — synthesizing them would be invention. Decision below.

---

## 6. Design decisions this pillar raises for the maintainer

- **D-SET-1 (the central fork): structural vs material set theory.** The entire corpus is
  *structural* — `Set` is the codomain category, objects known by arrows (Yoneda), truth
  sieve-valued (topos `Ω`), membership used but never axiomatized. An **ETCS-flavored structural
  set floor** (an object `Set` = the codomain, with elements/functions/products/coproducts/terminal/
  initial/subobject-classifier) is **liftable and faithful**. A **ZFC-flavored material floor**
  (first-class `∈`, extensionality, power set `2^X`, transfinite ordinals/cardinals) is **NOT in the
  source** and would be invented. *Recommendation (Präriehund):* lift the structural floor; record
  the material floor as an explicit honest-red deferral, not a silent build.

- **D-SET-2: new artifact vs recognition/consolidation of SP1.** Most of a structural set floor
  already lives in `formal.ttl`/`taiji.ttl` (§4). Decide whether the foundation (a) *relabels +
  consolidates* those classes as the explicit set-theory floor beneath the formal tower and fills
  three gaps (membership edge, function-as-morphism object, universal-construction coproduct/product
  distinct from data `Sum`/`Tuple`), or (b) authors a parallel set floor SP1 then re-anchors onto.
  Option (a) is less invention and re-uses the proven teeth (the `aob` group-law universal-property
  pattern is the template).

- **D-SET-3: depth of ordinals/cardinals.** Only finite/counting exist (enum `Ordinal` + the byte
  floor's `Count`/256 successor authority + `ℕ₀`/`ℕ⁺`). *Recommendation:* v1 cardinal = finite
  counting cardinality anchored on the unary-law `Count` authority (Count 256 / ordinal 255 /
  width 128 kept distinct); keep **local-smallness / size** as an honest-red hypothesis marker
  (as papers 14/18 do); do **not** invent `ℵ`/transfinite/universe objects.

- **D-SET-4: scope of "space constructs".** Site/sheaf (liftable — paper 18 ch09, paper 25, Vol 06)
  vs point-set metric/topological/normed/vector spaces (synthesized). *Recommendation:* v1 "space"
  = the categorical site/sheaf reading, which also grounds SP3's CRS carriers; record point-set
  spaces as a deferred obligation; realize any hand-authored point-set assumption AS a violation
  (Directive 18 render-artifact clause) rather than legitimizing it.

- **D-SET-5: coproduct/disjoint-union polysemy (feeds SP6).** The lexeme has (at least) two authored
  senses that must be held simultaneously under the mole-of-glossaries: the **data tagged union**
  (`prim:Sum`) and the **universal construction** (Set coproduct / disjoint union, held distinct
  from a general colimit per paper 19). This is a genuine SP6 polysemy tooth, exactly parallel to
  the already-resolved `colimit` polysemy (Directive 16). The set floor must reference
  coproduct/disjoint-union *through* the glossary layer, never bare.

- **D-SET-6: the "presheaf ≠ set" guard is a law, not a caveat.** The corpus's most-exposed
  cheese-trap face is collapsing `P` into `P(c)` (functoriality → static labelling)
  (`.../18_.../sections/01_thesis.tex:65-68`) and Yoneda's `X ≡ Hom(-,X)` shorthand into literal
  equality (`.../14_.../sections/01_thesis.tex:90-102`). A set floor must NOT let "everything is a
  set" erase the functorial/typed distinctions the corpus polices — the floor sits BENEATH the
  category layer as its carrier, it does not flatten it.

---

## 7. Coverage statement (Präriehund)

- **Read IN FULL:** the 4 mandatory law files + Directive 18/19; `srcy_map.md`; paper 18 sections
  00_content/01_thesis/03_olog_node_arrow_law + chapters 01(stmt)/03(stmt+failure)/04(elements+
  density+free-cocompletion)/05(sieves+subobject-classifier+kan-adjunction)/09(sheaf-condition);
  paper 14 sections 01_thesis + 06_closure; paper 09 colimit worked example; paper 19 thesis.
- **Inspected (targeted):** committed floors `formal.ttl` (collection/algebraic/enum towers,
  hom-set/arrow layer), `taiji.ttl` (presheaf/Yoneda apparatus), `realization.ttl` (Set/Bag ρ),
  `aob/group_law.ttl` (the group + universal-property teeth), `crs/README.md` (the CRS product).
  Corpus-wide greps for coproduct/disjoint-union/powerset/cardinal/ordinal/membership/space (207
  hits characterized, not each read).
- **NOT opened in full:** paper 18 chapters 02/06/07/08/10/11/12 (thesis/structure depth only);
  paper 19 body past thesis; appendix A (notational summary) and appendix B (minimal categorical
  commitments) — the `Set` axioms most likely to refine D-SET-1/D-SET-3 live there and are flagged
  as the next read if the maintainer wants the size/universe discipline pinned before authoring.
