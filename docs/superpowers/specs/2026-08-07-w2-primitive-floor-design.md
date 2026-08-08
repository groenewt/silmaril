# W2 · Sub-project 1 — the Primitive Floor (design)

> **Brainstorming design doc** (superpowers:brainstorming). Design-first HARD GATE:
> no implementation until this spec is approved. Terminal step → superpowers:writing-plans.
> **This is THIS ITERATION's v1** — it will be fundamentally challenged and relaunched
> later (maintainer, 2026-08-07). Design for completeness-of-iteration + clean
> re-runnability, not permanence. Corpus-agnostic: zero live-corpus binding (that is W5).

**Goal:** author the shared primitive substrate that every other W2 sub-project (and the
basicttl depth remediation) grounds into — the twin-olog **colimit taiji** whose formal facet
is the type-towers and whose physical facet is the bit/byte-vector carriers, glued by a
**monadic realization** that is literally the unary law's Frame.

**Binding sources** (gospel): `docs/unary-byte-frame-law.md`,
`docs/praeriehund-demokratie-der-kategorien.md`, `ledger/W2/design_constraints.md`
Directives 1–13. Lifted, not invented, from the real `forge/base_agents` `tensor` block +
`drill_values.py` + the `forge/base` foundations skills (`kleisli`, `sheaf`, `semiring`,
`lens`, `coalgebra`, `compose`/`lift`/`parallel`).

---

## 1. Architecture — one colimit over two ologs and a monad

The AOB primitive is **not** two linked things; it is **one colimit object** over a small
diagram. Three ontology units:

```
   Formal olog  ──ρ (realization, Kleisli/Frame)──▶  Physical olog
        └────────────────── colimit ──────────────────┘
                    = the AOB primitive (taiji)
```

- **Formal olog** — the type-towers as a category (objects = types, arrows = subtyping =
  the *ISA of the mathematics*). Nothing bottoms out at a flat `xsd:` leaf.
- **Physical olog** — the byte-stream carrier closure + ISA/UEFI machine types.
- **Realization monad** `ρ: Formal → Physical` — a **Kleisli arrow of the Frame monad**;
  realizing a formal value yields `Frame(output: encoding, effect: rounding/loss/endianness)`.
- **The taiji = colimit** of `(Formal ─ρ→ Physical)`, **mutual**: the physical carrier's
  `interpret_as` points back to its formal type, so yin holds yang. That back-pointer is the
  reversibility seal, checked by the round-trip test (§6).

**Why a colimit, not a pair of fields:** a colimit *glues* — the atom simultaneously *is* its
formal type and its physical encoding, and the gluing morphism (`ρ`) carries the effect. This
is the same shape as the unary law's Atlas & Graph colimit and the OSSIE YIN/YANG taiji.

**Why monadic:** one formal type realizes as *many* encodings (ℝ → float32 | float64 |
decimal), and each realization carries an effect. That is exactly a Kleisli arrow into
`Frame(output, effect)`. Unit = trivial realization; join = compose byte-descents to the Bit
floor. **The realization monad ≡ the Frame monad** — the depth floor and the unary law's
Yoneda-point Frame are one structure, not an analogy.

**As delivered — ρ is a genuine functor on arrows, closed as literal Yoneda.** The colimit is not
merely two ologs and an object-map ρ: the formal olog is materialised as a genuine **thin category**
(subtyping made first-class arrows), ρ is materialised as a **functor on morphisms** (each formal
arrow's image is a `prim:RealizationTransport`, with the identity and composition laws as real edges
and teeth), and the whole is closed as the **literal Yoneda embedding** `yo: FormalOlog →
PSh(FormalOlog)`, `A ↦ Hom(−, A)`, with ρ promoted to a **natural transformation** `yo ⇒ R`. Per the
unary law the **Frame(output, effect) IS the Yoneda point**, so realization = Yoneda evaluation at the
representable; per Directive 2 each representable is itself an olog object ("ologs of ologs, turtles
all the way"). This turns the panel residual "X is also grounded through its ancestor" from prose into
a resolvable edge (`prim:AncestralGroundingPath`): a subtype is dual-grounded **two ways** — directly
on its own reflexive carrier and transported up into the realization of its ancestor. Delivered
detail is in §5 (on-arrows action) and §9h (as-delivered counts + teeth).

## 2. File layout

| file | responsibility |
|------|----------------|
| `basicttl/primitives/formal.ttl` | Formal olog **as a thin category**: type-towers + subtyping arrows, plus first-class `SubtypeArrow`/`IdentityArrow`/`CompositeArrow` morphisms and the `RepresentablePresheaf` hook (STEP A) |
| `basicttl/primitives/physical.ttl` | Physical olog: Bit→ByteVector, ISA/UEFI types, facets, encodings, RGB |
| `basicttl/primitives/realization.ttl` | `ρ` realizations as Frame-monad Kleisli arrows + effects, **and ρ as a functor on arrows** (`RealizationTransport` + `AncestralGroundingPath`) (STEP B) |
| `basicttl/primitives/taiji.ttl` | the colimit gluing (primitive = colimit(formal, physical); mutual back-pointer) **and the literal Yoneda layer** (`yonedaObject`, `YonedaArrow`, `RhoComponent`, `NaturalitySquare`, Frame = Yoneda point) (STEP C) |
| `basicttl/primitives/primitives.shapes.ttl` | SHACL law for the floor (§6) **+ `FunctorTransportShape` + `YonedaShape`** (STEP D) **+ `FrameYonedaPointShape` + `YonedaEvaluationShape` + `CompositeTransportCoverageShape`** (STEP E) — 13 `sh:NodeShape`s |
| `basicttl/primitives/primitives.queries.sparql` | monad-law + round-trip + "what's a number" queries **+ the 6 functor/Yoneda probes** (STEP D) **+ the 3 residual-teeth ASKs** (STEP E) — 21 EXPECT-TRUE ASKs |
| `basicttl/primitives/README.md` | the floor, its consumers, how to re-run |

One file per responsibility (STRICTNESS Rule 14) — the categorical enrichment (STEPS A–D) and the
residual-teeth pass (STEP E) added **no new file**: both land in the existing four data files plus the
shapes and queries files, so the layout above stays exactly seven entries. Namespace:
`urn:silmaril:prim:…` (full-lexical URN idiom, unary law).

## 3. Formal olog — the towers (this iteration)

Each tower is a poset of olog objects; the ⊂ arrows are subtyping morphisms.

1. **Number** — `Natural`(0-incl / 0-excl as two named sub-objects) ⊂ `Integer` ⊂
   `Rational`(numerator·denominator pair) ⊂ `Real` ⊂ `Complex`; `Imaginary` a facet of
   `Complex`; `Bignum`(arbitrary-precision) and `Decimal`(base-10 fixed-point) as siblings.
   *(Deferred: algebraic-vs-transcendental facets.)*
2. **Boolean** — `Bool`; `Kleene3`(true/false/unknown) for SQL-null / structured↔unstructured.
3. **Text** — `Codepoint`(Unicode scalar) → `Grapheme` → `String`(sequence-of-codepoint).
4. **Temporal** — `Instant`, `Duration`, `Interval`, `Date`, `Time`, `DateTime`(+timezone facet).
5. **Identifier** — `URN` ⊃ `URI` ⊃ `IRI`, `QName`/`CURIE`, `BlankNode`. **Load-bearing:**
   S/O/P are URN towers; the whole ontology is URN-coordinated (unary law URN→Uniform/Resource/Name).
6. **RDF-term** — `Literal`(typed / lang-tagged), `Triple`, `Quad`, `RDFGraph`; `Literal`
   grounds into towers 1/3/4 via its datatype (the `_specspec` W3C algebra).
7. **Aggregate** — `Tuple`/`Product`, `List`/`Sequence`, `Set`, `Bag`/`Multiset`, `Map`,
   `Vector`, `Tensor`(n-dim). Feeds the AOB `tensor` block.
8. **Algebraic constructors** — `Sum`/`Coproduct`(tagged union), `Optional`/`Maybe`,
   `Frame`(output, effect), `Unit`(terminal), `Void`(initial). Mirror the unary law directly.
9. **Quantity** — `Quantity` = magnitude × `Unit`; `Dimension`(length/mass/time/…); SI +
   derived `Unit`s; `Currency`(ISO 4217); `Measurement`(value + uncertainty).
10. **Geospatial** — `Coordinate`, `Point`/`Line`/`Polygon`(WKT/GeoJSON geometry),
    `CRS`(coordinate reference system), `Latitude`/`Longitude`. Feeds GeoSPARQL + the
    S/O/P-tower CRS sub-project.
11. **Enum/Ordinal** — `Enumeration`(finite named), `Ordinal`(ordered), `Categorical`
    (unordered). The 21-col Atlas ring ordinals.
12. **Binary/Opaque** — `Blob`(opaque byte content — the hexadecimal/serialized-binary),
    `Hash`/`Digest`(e.g. sha256) — grounds the z-coordinate (uint16 of first two sha256 octets).

## 4. Physical olog — the carriers

- **Ladder:** `Bit`(w1) → `Nibble`(w4) → `Octet`/`Byte`(w8; **Byte ≠ Octet**) → `ByteVector`
  (**width 1..128**, unary-law cap) → `Word`(arch 16/32/64) → `Block` → `Stream` → `Container`.
- **ISA/UEFI machine types:** `BOOLEAN`, `UINT8/16/32/64/128`, `INT8/16/32/64/128`,
  `CHAR8/16`, `Float16/32/64/80/128` (IEEE-754 half/single/double/x87-ext/quad). UEFI `EFI_*`
  exact-width naming precedent recorded on each.
- **Representation facets:** `signedness`; integer rep = two's-/one's-complement/sign-magnitude;
  IEEE-754 `sign`/`exponent`/`mantissa` fields for floats; **endianness** `LE`/`BE`
  *(mixed/PDP deferred)*; `alignment`/`padding`.
- **Per-carrier tensor block** (lifted from base_agents): `bit_width · byte_width ·
  byte_order · interpret_as` (`interpret_as` → the formal type = the mutual back-pointer).
- **Text encodings** (realization carriers): `ASCII`, `UTF-8`, `UTF-16`(LE/BE), `UTF-32`,
  `Latin-1` — Codepoint→byte.
- **Colour code space:** `RGB` → `Red`/`Green`/`Blue`, each an `Octet` (cardinality 256,
  ordinal 0..255) — the JEPA colour substrate (unary law).

## 5. Realization monad `ρ` — Kleisli/Frame

`ρ` maps each formal type to its physical encoding(s) as Frame-monad Kleisli arrows carrying
typed effects:

| formal | realization (example) | effect |
|--------|-----------------------|--------|
| `Real` | `Float64 · 8B · LE` / `Float32 · 4B · LE` / `Decimal` | IEEE754-rounding / rounding+narrowing / base-10-precision |
| `Integer` | `INT8..64 · LE\|BE` | overflow-domain (width-bounded) |
| `Natural` | `UINT8..64` | overflow-domain |
| `Bignum` | `ByteVector(≤128)` | unbounded→bounded → **may-overflow** |
| `Codepoint` | `UTF-8 · 1..4B` / `UTF-16` / `UTF-32` | encoding-loss (surrogate/normalization) |
| `Bool` | `UINT8`(0/1) / bit | none |
| `Instant` | `INT64`(epoch) / ISO-8601 string | epoch-precision / lexical |

- **Monad laws** hold: left/right unit + associativity of Kleisli composition.
- **Byte-descent** = Kleisli composition of realizations down to the `Bit` floor.
- **Polymorphism** — one formal type → many encodings is the whole point of the monad; the
  chosen realization is part of the colimit-taiji instance, the effect is its `Frame.effect`.

**As delivered — ρ's on-arrows action.** Above, ρ acts on *objects* (type → encoding). The
enrichment materialises ρ's action on *morphisms* so it is a **genuine functor**, not a bare object
map. `prim:rhoObject` pins each type's single canonical carrier (the reflexive carrier whose
`interpretAs` closes back to that type; the apex `FormalType` maps to the generic `ByteVector`). For
every arrow of the thin formal category, a `prim:RealizationTransport` records its image ρ(A) → ρ(B)
via `prim:transportDom`/`prim:transportCod` (= `rhoObject` of the arrow's dom/cod). The **functor
laws are real edges with teeth**: `ρ(id_A) = id` on ρ(A) (identity transports, `isTransportIdentity
true`, dom = cod — `q_functor_identity` + `FunctorTransportShape`), and `ρ(g ∘ f) = ρ(g) ∘ ρ(f)`
(composite transports reifying `transportComposeFirst`/`Second`/`Into` edge-for-edge from the formal
`CompositeArrow` — `q_functor_composition`). Because the category is thin, this composition is
associative on the nose. The panel residual "grounded through ancestor" is then the resolvable edge
`prim:AncestralGroundingPath` (one per realized-proper-ancestor pair): `ancestralViaTransport`
resolves via `transportCod` onto ρ(ancestor) = `ancestralLandsIn`, so a subtype is **dual-grounded
two ways** — its own direct grounding untouched, plus the transported path up the tower
(`q_ancestral_transport_resolves`, complete coverage). Counts and teeth: §9h.

## 6. Verification — the epistemology emerges from the checks

Evidence-first (`verification-before-completion`); each is RED before authoring, GREEN after.

- **SHACL** (`primitives.shapes.ttl`): every formal type has ≥1 realization; every physical
  encoding has `bit_width ≤ 128`, a `byte_order`, and an `interpret_as` closing the
  mutual-colimit; every tower has its subtyping arrows; no dangling type.
- **"What's a number" acceptance test** (`primitives.queries.sparql`): `ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ`+imaginary
  all resolve as a chain; each has a correct-width ISA/UEFI realization (`ℝ→float32/64`,
  `ℤ→int8..64`, `ℚ→pair`, `Bignum→bytevector`). This is the maintainer's litmus.
- **Monad-law check**: unit + associativity of realization composition, as SPARQL ASKs.
- **Colimit round-trip**: `physical → interpret_as → formal` is identity for every carrier
  (the mutual-colimit reversibility seal).
- **Depth gate**: every `owl:Class` in the floor carries an `rdfs:comment ≥ 200` chars
  (`scripts/ontology-depth-check.py`).
- All run under pyshacl + rdflib now; wired into the multi-engine CI in W4.

## 7. Interfaces produced (consumed by the other 8 sub-projects)

- **AOB meta-ontology (#2):** grounds each atom's `tensor`/byte field into the Physical olog +
  `ρ`; an AOB atom's value = a colimit-taiji instance over this floor.
- **S/O/P-tower CRS (#3):** grounds `z` (uint16 of first two `source_sha256` octets) into the
  Binary/Hash tower + byte descent; `CRS`/`Coordinate` formal objects seed the geometry.
- **Projection packet (#4):** the realization effects are the seed of the 5 loss classes.
- **File+format taxonomy (#5):** formats declare their leaf datatypes against these towers.
- **Depth remediation (#8):** every basicttl untyped individual / stub class dual-grounds here.
- **Render seal (#9):** the colimit round-trip is the per-primitive instance of the split↔
  consolidated reversibility.

## 8. Non-goals (this iteration)

No live-corpus binding (W5). No new corpuses (2 more gippidy / sparky / agent / BLS incoming).
No algebraic-vs-transcendental number facets, no mixed/PDP endianness, no non-IEEE float
formats — deferred until a concrete consumer needs them (YAGNI). The floor is expected to be
challenged and relaunched; it is built to be re-run, not to be final.

## 9. Panel-forced law corrections (2026-08-08)

The first SP1 build (`wf_77f87831-c4f`) was structurally sound (all 12 towers, all ladder carriers
and ISA/UEFI machine types present; every `owl:Class` carries a genuine ≥200-char comment) but the
between-sub-project adversarial triple panel returned **NO-GO**: the binding dual-grounding law was
met for only **9 of 59** formal-type classes, and the SHACL "teeth" targeted `prim:FormalType`
*instances* (9 punned nodes) rather than the 59 `rdfs:subClassOf+ prim:FormalType` *classes*, so
"green" was produced by scoping the teeth away from the cases that would bite. These corrections make
§1 and §6 **precise and enforceable** (they do not change scope — they close the gap between the
stated law and the delivered artifact). They are binding on the remediation.

- **9a. Dual-grounding is universal over the tower; the SHACL law accepts self-or-ancestor-or-descendant,
  but the delivered floor grounds all 59 classes DIRECTLY.**
  Every one of the 59 formal-type classes must be dual-grounded. The SHACL law is deliberately
  *permissive about where* the grounding sits: a class counts as dual-grounded if a `prim:Realization`
  is present on **itself**, on a **realized ancestor**, or on a **realized descendant**. The law MUST
  bite on the *class* form — a `sh:sparql` constraint that walks `rdfs:subClassOf*` and flags any tower
  class with no realization on itself, an ancestor, or a descendant. Probe of record: injecting
  `ex:Orphan a owl:Class ; rdfs:subClassOf prim:FormalType` (the form every real tower uses) MUST make
  `pyshacl` report `conforms=False`. **What the delivered floor actually does is the strong case, not the
  slack one:** the per-type build made grounding *fully direct*. Verified over the merged 4-file data
  graph — 59 tower classes (`rdfs:subClassOf+ prim:FormalType`), 59 direct-grounded, 0 transitive-only —
  **every one of the 59 carries its OWN** `prim:Realization` (a `prim:realizesFrom` that exact class), its
  OWN reflexive carrier (an encoding whose `prim:interpretAs` is that exact class), and its OWN
  `prim:Primitive` (a `prim:formalFacet` on that exact class). Concrete types (String, DateTime, Hash,
  Rational, Complex, Tensor, …) are directly realized, and so are the named sub-objects and the abstract
  supertypes: e.g. `NaturalWithZero` (a subtype of `Natural`) does **not** inherit `Natural`'s
  realization — it carries its own `prim:realize_NaturalWithZero_Canonical` onto its own reflexive carrier
  `prim:NaturalWithZeroCanonicalEncoding`, glued by its own `prim:primitive_NaturalWithZero`; the
  `⊂ Natural` relationship is taxonomic subtyping only (an additional coverage path the law would accept),
  **not** the grounding mechanism the graph relies on. The self/ancestor/descendant acceptance is retained
  in the SHACL law as headroom for future re-runs — an abstract supertype could in principle be covered by
  a realized descendant — but no class in this iteration's floor depends on ancestral or descendant
  coverage; all 59 stand on their own direct realization, reflexive carrier, and primitive.

- **9b. `Bignum → ByteVector(≤128 bytes)` is realized, not provisional.** It is named in §5/§6 and is
  not in §8; the `isProvisional`-dodge to `Uint128` is removed. `Rational → Product(numerator:Integer,
  denominator:Integer)`, `Complex → Product(real:Real, imaginary:Real)`, and `Imaginary → Real` are
  realized so the "what's a number" litmus reproduces in full (ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ + imaginary, each with a
  correct-width ISA/UEFI or composite realization). `isProvisional` is reserved for genuinely
  undecidable gaps (Praeriehund), never for resolvable in-scope work.

- **9c. Two distinct width caps.** Fixed-width **scalar** encodings are capped at **bitWidth ≤ 128**
  (`EncodingShape`). **ByteVector** encodings are capped at **byteCount ≤ 128** (= up to 1024 bits) by
  a separate `ByteVectorEncodingShape` on a `prim:byteCount` datatype property. `q_bytevector_cap` MUST
  test the *enforced* cap (a 129-byte vector, or a scalar bitWidth > 128, is caught); the README and
  the ASK comment are reconciled to these two caps. `Byte ≠ Octet` gets an explicit guard.

- **9d. The colimit round-trip is a true identity.** For **every** primitive,
  `physicalFacet → interpretAs` MUST equal `formalFacet` (reflexive). The three non-reflexive atoms
  are bugs, fixed at the source: `Bignum→ByteVector→Bignum`, `Instant→INT64(epoch)→Instant`,
  `Decimal→(decimal encoding)→Decimal`. A new `q_colimit_reflexive` ASK enforces identity, not mere
  non-danglingness.

- **9e. The monad is proven, not decorated.** A Kleisli composition operation (`prim:compose` /
  `prim:byteDescendsTo`) is modeled, and the monad laws are checked as real SPARQL ASKs: **left/right
  unit** and **associativity** (`(f >=> g) >=> h ≡ f >=> (g >=> h)`) over a concrete byte-descent
  chain. `q_monad_unit` tests the unit law, not a boolean flag.
  **The unit law is typed correctly.** For a Kleisli arrow `f: A ⤳ B`, the LEFT unit is
  `η_A >=> f ≡ f` where `η_A` is the Kleisli identity at the **domain** A, and the RIGHT unit is
  `f >=> η_B ≡ f` where `η_B` is the Kleisli identity at the **codomain** B — NOT at the domain. Every
  Kleisli arrow individual carries `prim:kDom`/`prim:kCod`, and there is one identity arrow
  `prim:k_id_<T>` (`prim:isMonadUnit true`, `kDom = kCod = T`) per object a unit witness needs — in
  particular `prim:k_id_Float64` so the right-unit witness of `f: Real ⤳ Float64` is well-typed
  (`f.kCod = Float64 = η_B.kDom`). A composition is well-typed exactly when
  `composeFirst.kCod = composeSecond.kDom`, `composeInto.kDom = composeFirst.kDom`, and
  `composeInto.kCod = composeSecond.kCod`; this is enforced by a `sh:sparql` **`KleisliCompositionShape`**
  (targeting `prim:Composition`, `conforms=False` on any ill-typed composition) and mirrored by the
  EXPECT-TRUE `q_kleisli_welltyped`. `q_monad_unit` witnesses BOTH unit laws over well-typed
  compositions, referencing `kDom`/`kCod`. (The originally shipped `prim:comp_rightUnit` was
  ill-typed — its `composeSecond` was `η` at the domain `Real` instead of the codomain `Float64` — so
  it was decorative; it is corrected here and the teeth now bite on that exact defect.)

- **9f. Honesty pass.** Every `formal.ttl` prose claim that asserts a realization must correspond to a
  real `prim:Realization` in the graph (or be hedged); the false universal enforcement claim is
  removed. `Void` (initial/uninhabited) is the one honest edge — realized as the empty (0-byte)
  encoding with a `uninhabited` effect, so universality stays total without a dodge.

- **9g. Minor physical additions** flagged by the panel and cheap to close now (were not in §8):
  IEEE-754 `Sign`/`Exponent`/`Mantissa` field breakdown, `Alignment`/`Padding` facets, and the
  `UTF-16 LE`/`UTF-16 BE` split.

- **9h. The categorical enrichment — ρ made a functor on arrows, closed as literal Yoneda (delivered
  2026-08-08).** The panel residual "X is also grounded through its ancestor" was true categorically
  but *unmaterialised*: ρ acted only on objects. The enrichment makes it a real, inspectable,
  teeth-proven graph fact — nothing stripped, structure ADDED. **STEP A (`formal.ttl`, thin category):**
  59 `prim:SubtypeArrow` generators (one per `rdfs:subClassOf` cover edge, each in exact agreement with
  a real triple), 60 `prim:IdentityArrow` id_T (59 tower classes + `FormalType` apex), 45
  `prim:CompositeArrow` reifying canonical left-nested decompositions; thin ⇒ associative on the nose.
  **STEP B (`realization.ttl`, ρ as functor on arrows):** `prim:rhoObject` pins the canonical carrier;
  164 `prim:RealizationTransport` (60 identity + 59 subtype + 45 composite) with matching
  `transportDom`/`transportCod`; functor identity (`isTransportIdentity true`) and composition
  (`transportComposeFirst/Second/Into`) laws as edges; 45 `prim:AncestralGroundingPath` resolving each
  realized-ancestor pair onto ρ(ancestor) — "dual-grounded two ways", both materialised and resolvable.
  **STEP C (`taiji.ttl`, literal Yoneda):** `yo: A ↦ Hom(−,A)` as 60 `prim:RepresentablePresheaf`
  linked by injective `prim:yonedaObject` (faithfulness); 59 `prim:YonedaArrow` giving the bijection
  Hom(A,B) ↔ Nat(yo A, yo B) in thin form (fullness); ρ made a natural transformation `yo ⇒ R` via 60
  `prim:RhoComponent` and 59 `prim:NaturalitySquare` (`natCommutes true`); the **Frame IS the Yoneda
  point** (realization = Yoneda evaluation at the representable), and per Directive 2 each representable
  is itself an olog object. **STEP D (teeth):** SHACL `prim:FunctorTransportShape` (every SubtypeArrow
  has a transport with dom/cod = ρ(arrowDom)/ρ(arrowCod)) and `prim:YonedaShape` (every tower class has
  a representable-with-Yoneda-point and a ρ-component); six EXPECT-TRUE probes `q_functor_identity`,
  `q_functor_composition`, `q_ancestral_transport_resolves`, `q_yoneda_faithful`, `q_yoneda_full`,
  `q_naturality_commutes`. **As-delivered verification (STEP-D milestone; superseded by §9i STEP E below,
  which brings the suite to 21 ASKs / 13 shapes):** the graph grew from 3,123 to **8,346 triples**
  and the ASK suite from 12 to **18**; `run-floor-checks.sh` exits 0 (parse OK 8346 triples · SHACL
  conforms=True · 18/18 ASKs PASS · depth gate PASSED, 5 files). Each new tooth was proven to **bite**
  (`True → False`) by injection — including the closed vacuous-match escape on `q_naturality_commutes`
  (a dangling `natComponentCod` is now caught by an added well-formedness conjunct), so green reflects
  the graph holding the law, never scoping the teeth away. The morphism/presheaf classes are
  deliberately NOT `rdfs:subClassOf prim:FormalType`, so the dual-grounding law never demands a physical
  realization of an arrow; only objects are dual-grounded. No new file was added (STRICTNESS Rule 14):
  the enrichment lands in the existing four data files plus shapes and queries.

- **9i. STEP E — the two decorative residuals given real teeth (delivered 2026-08-08).** STEP C
  *materialised* two facts that STEP D never *enforced*, so the floor stayed green even when they were
  broken. **RESIDUAL 1 — Frame = Yoneda-point / Yoneda-evaluation soundness:** `prim:Frame
  prim:isYonedaPoint true` and the 60 `prim:YonedaEvaluation` edges (`evalPresheaf`/`evalAtPoint`/
  `evalYields`/`evalComponent`) were read by no ASK and no shape, so injecting `isYonedaPoint=false` or a
  wrong `evalYields` left the floor GREEN. **RESIDUAL 2 — composite-transport existence/coverage:**
  `q_functor_composition` + `prim:FunctorTransportShape` catch a MIS-WIRED composite transport but not a
  MISSING one, and nothing forced a composable subtype pair to actually HAVE a composite arrow. STEP E
  closes both, ADDING structure and stripping none. **Three EXPECT-TRUE ASKs:** `q_yoneda_point` (holds
  iff `prim:Frame prim:isYonedaPoint true` and not `false`); `q_yoneda_evaluation_sound` (holds iff every
  `prim:YonedaEvaluation`'s `evalYields` equals ρ of the type whose representable it evaluates —
  `prim:rhoObject` of the `?t` with `?t prim:yonedaObject` = the evaluation's `evalPresheaf`);
  `q_functor_composition_total` (holds iff (a) every `prim:CompositeArrow` has a `prim:RealizationTransport`
  `transportOf` it AND (b) every composable `prim:SubtypeArrow` pair `f: A→B, g: B→C` has a
  `prim:CompositeArrow` with `composeArrowFirst = f`, `composeArrowSecond = g`). **Three SHACL shapes:**
  `prim:FrameYonedaPointShape` (targets `prim:Frame`, `sh:hasValue true` on `isYonedaPoint`),
  `prim:YonedaEvaluationShape` (every `prim:YonedaEvaluation` carries all four `eval*` coordinates AND
  `evalYields` = the type realization), `prim:CompositeTransportCoverageShape` (every `prim:CompositeArrow`
  is the target of a `transportOf` transport). **As-delivered verification (final):** STEP E added ASKs
  and shapes only — the data graph is unchanged at **8,346 triples**; the ASK suite grew from 18 to **21**
  and the SHACL law to **13 `sh:NodeShape`s**; `run-floor-checks.sh` exits 0 (parse OK 8346 triples · SHACL
  conforms=True · **21/21 ASKs PASS** · depth gate PASSED, 5 files). Each new tooth was proven to **bite**
  (`True → False`) by injection: (a) `isYonedaPoint=false` → `q_yoneda_point` + `prim:FrameYonedaPointShape`;
  (b) a wrong `evalYields` → `q_yoneda_evaluation_sound` + `prim:YonedaEvaluationShape`; (c) a deleted
  composite transport → `q_functor_composition_total` + `prim:CompositeTransportCoverageShape`; (d) a
  deleted composite arrow for a still-composable pair → `q_functor_composition_total` (coverage,
  ASK-enforced). The full prior teeth set was re-confirmed intact — **20/20** probes bite (16 prior + 4
  STEP E). No new file was added (STRICTNESS Rule 14): STEP E lands in the shapes and queries files only.
