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

## 2. File layout

| file | responsibility |
|------|----------------|
| `basicttl/primitives/formal.ttl` | Formal olog: all type-towers + subtyping arrows |
| `basicttl/primitives/physical.ttl` | Physical olog: Bit→ByteVector, ISA/UEFI types, facets, encodings, RGB |
| `basicttl/primitives/realization.ttl` | `ρ` realizations as Frame-monad Kleisli arrows + effects |
| `basicttl/primitives/taiji.ttl` | the colimit gluing (primitive = colimit(formal, physical); mutual back-pointer) |
| `basicttl/primitives/primitives.shapes.ttl` | SHACL law for the floor (§6) |
| `basicttl/primitives/primitives.queries.sparql` | monad-law + round-trip + "what's a number" queries |
| `basicttl/primitives/README.md` | the floor, its consumers, how to re-run |

One file per responsibility (STRICTNESS Rule 14). Namespace: `urn:silmaril:prim:…`
(full-lexical URN idiom, unary law).

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

- **9a. Dual-grounding is universal over the tower, direct-for-concrete + transitive-for-abstract.**
  Every one of the 59 formal-type classes must be dual-grounded. A **concrete** type (String,
  DateTime, Hash, Rational, Complex, Tensor, …) carries its **own** `prim:Realization`. A type is
  also dual-grounded if it inherits one from a **realized ancestor** (e.g. `NaturalWithZero ⊂ Natural`)
  or, for a genuine **abstract supertype**, is covered by a **realized descendant**. The SHACL law
  MUST bite on the *class* form: a `sh:sparql` constraint that walks `rdfs:subClassOf*` and flags any
  tower class with no realization on itself, an ancestor, or a descendant. Probe of record: injecting
  `ex:Orphan a owl:Class ; rdfs:subClassOf prim:FormalType` (the form every real tower uses) MUST make
  `pyshacl` report `conforms=False`.

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
  unit** (`η >=> f ≡ f ≡ f >=> η`) and **associativity** (`(f >=> g) >=> h ≡ f >=> (g >=> h)`) over a
  concrete byte-descent chain. `q_monad_unit` tests the unit law, not a boolean flag.

- **9f. Honesty pass.** Every `formal.ttl` prose claim that asserts a realization must correspond to a
  real `prim:Realization` in the graph (or be hedged); the false universal enforcement claim is
  removed. `Void` (initial/uninhabited) is the one honest edge — realized as the empty (0-byte)
  encoding with a `uninhabited` effect, so universality stays total without a dodge.

- **9g. Minor physical additions** flagged by the panel and cheap to close now (were not in §8):
  IEEE-754 `Sign`/`Exponent`/`Mantissa` field breakdown, `Alignment`/`Padding` facets, and the
  `UTF-16 LE`/`UTF-16 BE` split.
