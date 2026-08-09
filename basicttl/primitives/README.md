# The Primitive Floor (W2 · SP1)

> **This iteration's v1.** The floor is built to be re-run and relaunched, not to be permanent
> (maintainer, 2026-08-07). Corpus-agnostic: zero live-corpus binding — that is W5. Every claim
> here is evidence-backed by the runner; anything genuinely undecidable this iteration is marked
> `silm:isProvisional` with a documented gap rather than force-fit (Präriehund honesty).

The shared primitive substrate every other W2 sub-project (and the basicttl depth remediation)
grounds into: a **twin-olog colimit taiji** whose **formal** facet is the mathematical
type-towers and whose **physical** facet is the bit/byte-vector carriers, glued by a **monadic
realization** that is literally the unary law's **Frame**. The floor's dual-grounding invariant —
no formal type bottoms out at a bare `xsd:` leaf; each lives in a subtyping tower AND is realized
into ≥1 physical carrier that points back via `interpretAs` (the mutual-colimit seal) — is
**enforced universally over all 59 tower classes** after the panel-NO-GO remediation (spec §9).
The SHACL `prim:DualGroundingShape` is a `sh:sparql` constraint that walks `rdfs:subClassOf*` and
flags any tower class with no realization on itself, a realized ancestor, or a realized
descendant — so it bites on the **class form** every tower uses (the injected
`ex:OrphanB a owl:Class ; rdfs:subClassOf prim:FormalType` probe makes `pyshacl` report
`conforms=False`), not merely on the punned individuals the earlier decoy targeted. Every physical
encoding points back to its formal type, and every primitive's round-trip is a **true identity**
(`physicalFacet → interpretAs = formalFacet`) — enforced with teeth by `prim:ColimitReflexivityShape`,
not just checked by an ASK. `Byte ≠ Octet` has an explicit guard (`prim:ByteOctetDistinctionShape`). The realization **monad is
proven, not decorated**: `prim:KleisliCompositionShape` enforces that every reified Kleisli
`Composition` is well-typed (`composeFirst.kCod = composeSecond.kDom`, result spanning them), and the
left-unit (η_A >=> f ≡ f), right-unit (f >=> η_B ≡ f, η at the **codomain** B) and associativity laws
each have a genuine well-typed witness the checks bite on — the earlier ill-typed right-unit witness
(η taken at the domain instead of the codomain) is now caught.
The SHACL value-type checks are **defang-proof**: because `interpretAs`/`byteOrder`/`frameEffect`/
`formalFacet`/`physicalFacet`/`gluedBy` all carry an `rdfs:range`, a plain `sh:class` under
`inference="rdfs"` would be made vacuous by range-inference (which types whatever the property points
at), so those checks are done instead with `sh:in` (enumerated families) and `sh:sparql`
(`rdfs:subClassOf*` walks and structural-signature `FILTER NOT EXISTS`) that range-inference cannot
forge. There are **no** `silm:isProvisional` nodes in the floor: the two former proxy arrows
(`Real→Ascii`, `Decimal→Ascii`) were removed and Decimal is grounded by its own reflexive packed-BCD
carrier.

### The categorical enrichment — ρ as a genuine functor, closed as literal Yoneda

The panel residual finding "X is also grounded through its ancestor" was **true categorically but
unmaterialised**: ρ acted only on OBJECTS (type → carrier). The enrichment makes ρ a **genuine
functor on morphisms** and closes it as **literal Yoneda**, so ancestral/transitive grounding
becomes a real, inspectable, teeth-proven graph fact. Nothing was stripped — structure was ADDED.

- **The formal olog is now a genuine (thin) category** (`formal.ttl`). Each `rdfs:subClassOf` edge
  `A ⊂ B` is reified as a first-class `prim:SubtypeArrow` (`prim:arrowDom` A, `prim:arrowCod` B) —
  **59 generators**, one per cover edge, each in exact agreement with a real `rdfs:subClassOf`
  triple. Every object carries its identity arrow `prim:id_<T>` (`prim:IdentityArrow`, dom = cod) —
  **60**, over the 59 tower classes plus the `FormalType` apex. Every non-immediate ancestor pair
  `A <: C` carries a `prim:CompositeArrow` reifying its canonical left-nested decomposition
  (`prim:composeArrowFirst`/`Second`/`Into`) — **45**. Because each class has exactly one direct
  parent the Hasse diagram is a tree, so the induced category is **thin (a poset)**: at most one
  arrow per ordered pair, hence composition is associative on the nose (stated explicitly).
- **ρ is a functor on arrows** (`realization.ttl`). `prim:rhoObject` pins each type's single
  canonical carrier (the on-objects action). For every formal arrow, `prim:RealizationTransport`
  materialises its ρ-image `ρ(A) → ρ(B)` with matching `prim:transportDom`/`prim:transportCod` —
  **164 transports** (60 identity + 59 subtype + 45 composite). The **functor laws are real edges
  and teeth**: `ρ(id_A) = id` on `ρ(A)` (identity transports flagged `prim:isTransportIdentity
  true`, dom = cod), and `ρ(g ∘ f) = ρ(g) ∘ ρ(f)` (composite transports reify
  `prim:transportComposeFirst`/`Second`/`Into` edge-for-edge from the formal decomposition). The
  "grounded through ancestor" fact is then the real edge `prim:AncestralGroundingPath` — **45**, one
  per realized-proper-ancestor pair — carrying `prim:ancestralViaArrow` (the subtyping arrow A → B),
  `prim:ancestralViaTransport` (its ρ-image) and `prim:ancestralLandsIn` (= ρ(B)). So a subtype is
  **dual-grounded two ways, both materialised and resolvable**: directly on its own reflexive
  carrier, and transported up into the realization of its ancestor (Currency, URI, Categorical,
  Longitude, …).
- **Literal Yoneda** (`taiji.ttl`). The Yoneda embedding `yo: FormalOlog → PSh(FormalOlog)`,
  `A ↦ Hom(−, A)`, is materialised: a `prim:RepresentablePresheaf` `prim:repr_<A>` per object
  (**60**, the representable = the hom-set of arrows with codomain A) linked by `prim:yonedaObject`
  (injective — Yoneda faithfulness). `yo` on arrows is **59** `prim:YonedaArrow`s (one per generator,
  a bijection Hom(A,B) ↔ Nat(yo A, yo B) in this thin category — Yoneda fullness). ρ is made a
  **natural transformation** `yo ⇒ R`: **59** `prim:NaturalitySquare`s (one per subtype arrow) with
  corners pinned to `prim:RhoComponent`s (**60**) and `prim:natCommutes true`. Per the unary law the
  **Frame(output, effect) IS the Yoneda point**: the target of ρ is tied to Yoneda evaluation at the
  representable, so realization = Yoneda evaluation. Per Directive 2 ("ologs of ologs, turtles all
  the way"), each representable is itself an olog object.

These morphism/presheaf classes are deliberately **not** `rdfs:subClassOf prim:FormalType` — they
are arrows and presheaves, not tower objects — so the dual-grounding law (`prim:DualGroundingShape` /
`q_universality`) never demands a physical realization *of an arrow*; only objects are dual-grounded.
The enrichment adds two SHACL shapes (`prim:FunctorTransportShape`, `prim:YonedaShape`) and six
probes (`q_functor_identity`, `q_functor_composition`, `q_ancestral_transport_resolves`,
`q_yoneda_faithful`, `q_yoneda_full`, `q_naturality_commutes`), each proven to bite by injection
(see Verification). A later residual-teeth pass (**STEP E**) then enforces two facts that were
materialised but unread — the Frame = Yoneda-point identification / Yoneda-evaluation soundness, and
composite-transport existence/coverage — adding three more SHACL shapes (`prim:FrameYonedaPointShape`,
`prim:YonedaEvaluationShape`, `prim:CompositeTransportCoverageShape`) and three more ASKs
(`q_yoneda_point`, `q_yoneda_evaluation_sound`, `q_functor_composition_total`), bringing the floor to
**13 `sh:NodeShape`s and 21 EXPECT-TRUE ASKs** (see Verification).

Namespace: `prim: <urn:silmaril:prim:#>` (full-lexical URN idiom, unary law).

## File map

| file | responsibility | task |
|------|----------------|------|
| `formal.ttl` | Formal olog **as a thin category**: type-towers + `rdfs:subClassOf` subtyping arrows, plus first-class `prim:SubtypeArrow`/`prim:IdentityArrow`/`prim:CompositeArrow` morphisms and the `prim:RepresentablePresheaf` hook | Task 2 (+ STEP A) |
| `physical.ttl` | Physical olog: Bit→ByteVector ladder, ISA/UEFI machine types, facets, text encodings, RGB | Task 3 |
| `realization.ttl` | `ρ` realizations as Frame-monad Kleisli arrows + typed effects, **and ρ as a functor on arrows** (`prim:RealizationTransport` + `prim:AncestralGroundingPath`) | Task 4 (+ STEP B) |
| `taiji.ttl` | the colimit gluing — `Primitive` = colimit(formal, physical) with the mutual back-pointer — **and the literal Yoneda layer** (`prim:yonedaObject`, `prim:YonedaArrow`, `prim:RhoComponent`, `prim:NaturalitySquare`, Frame = Yoneda point) | Task 5 (+ STEP C) |
| `primitives.shapes.ttl` | SHACL law for the floor (dual-grounding, cap, Frame, colimit closure) **+ `prim:FunctorTransportShape` + `prim:YonedaShape`** (STEP D) **+ `prim:FrameYonedaPointShape` + `prim:YonedaEvaluationShape` + `prim:CompositeTransportCoverageShape`** (STEP E) — 13 shapes | Task 6 (+ STEP D/E) |
| `primitives.queries.sparql` | the EXPECT-TRUE ASK suite: "what's a number" litmus + monad-law + round-trip **+ the 6 functor/Yoneda probes** (STEP D) **+ the 3 residual-teeth ASKs** (STEP E) — 21 ASKs | Task 1 (+ STEP D/E) |
| `checks/run-floor-checks.sh` | the runner: parse + pyshacl + depth gate + every EXPECT-TRUE ASK | Task 1 |
| `README.md` | this file: the floor, its consumers, how to re-run | Task 1/7 |

The runner loads the **four data TTLs** (`formal.ttl`, `physical.ttl`, `realization.ttl`,
`taiji.ttl`) into one graph and validates them against `primitives.shapes.ttl` loaded **only** as
the shapes graph (never mixed into the data). The per-type `frags/*.ttl` were **removed** after
their content was integrated into `realization.ttl`/`taiji.ttl` — they were duplicate source that
could silently diverge; the four data files are now authoritative and the sole thing the SHACL/ASK
layer sees. SP1 is **remediated, green, and completed** (all checks pass with real teeth, evidence
below); the DAG `silm:phase_w2_sp1 silm:hasStatus "completed"` flip **has been performed**
(2026-08-08) with the green evidence recorded inline in `basicttl/dag/dag_instances.ttl`, and the DAG
re-parses (630 triples) and re-conforms after the flip.

## Fixed property-name contract

Stable across every floor file (do not rename):

- `realizesAs` : `FormalType → Realization`
- `encoding` : `Realization → PhysicalEncoding`
- `interpretAs` : `PhysicalEncoding → FormalType` (the mutual-colimit back-pointer)
- `frameOutput` / `frameEffect` : `Realization → …` (the Frame's output and typed effect)
- `formalFacet` / `physicalFacet` / `gluedBy` : `Primitive → …`

## The acceptance suite (`primitives.queries.sparql`)

Named EXPECT-TRUE ASKs; the runner requires every one to return true.

- `q_number_tower` — ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ (+ imaginary) resolve as a real subtyping chain. **Litmus #1.**
- `q_number_realized` — ℝ has 64-bit and 32-bit realizations, ℤ a 32-bit one, **and ℚ→Product,
  ℂ→Product, Imaginary→Real(Float64), Bignum→ByteVector** each realize (interpreting back to their
  own type). **Litmus #2**, extended per spec §9b.
- `q_universality` — **every** tower class (`rdfs:subClassOf+ prim:FormalType`) is grounded on
  itself, a realized ancestor, or a realized descendant. The class-level grounding litmus (§9a).
- `q_colimit_roundtrip` — every `PhysicalEncoding` `interpretAs` a `FormalType` (non-danglingness).
- `q_colimit_reflexive` — every `Primitive`'s `physicalFacet → interpretAs` **equals** its
  `formalFacet` (true-identity round-trip, §9d).
- `q_frame_effect` — every `Realization` carries a `frameOutput` and a `frameEffect`.
- `q_bytevector_cap` — the **two enforced caps**: no scalar `bitWidth > 128` and no
  `byteCount > 128` (spec §9c); tested against the enforced caps, not a decoy 1024-bit filter.
- `q_kleisli_welltyped` — **every** reified `Composition` is well-typed: `composeFirst.kCod =
  composeSecond.kDom` and the result spans them (`composeInto.kDom = composeFirst.kDom`,
  `composeInto.kCod = composeSecond.kDom`… i.e. `= composeSecond.kCod`). The EXPECT-TRUE mirror
  of SHACL `prim:KleisliCompositionShape`; the monad-law witnesses are read only over these
  well-typed compositions (§9e).
- `q_monad_unit` — the **two-sided unit law** η_A >=> f ≡ f ≡ f >=> η_B, over reified `Composition`
  witnesses (not a boolean flag), referencing `kDom`/`kCod`. Crucially the right-unit operand is
  η at the **codomain** (`prim:k_id_Float64` for f: Real ⤳ Float64), not η at the domain — the
  earlier ill-typed `prim:k_id_Real` right-unit witness is now caught by `q_kleisli_welltyped` /
  `prim:KleisliCompositionShape`. §9e.
- `q_monad_assoc` — the **associativity law** (f >=> g) >=> h ≡ f >=> (g >=> h), §9e.
- `q_byte_descent` — the carrier ladder byte-descends to the `prim:Bit` floor.
- `q_rgb` — the RGB code space is exactly Red/Green/Blue, each an Octet of ordinal 0..255.
- `q_functor_identity` — ρ preserves identities: every `prim:IdentityArrow` id_A has an identity
  `prim:RealizationTransport` at ρ(A) (`isTransportIdentity true`, dom = cod = ρ(A)). **STEP B.**
- `q_functor_composition` — ρ preserves composition: every `prim:CompositeArrow`'s ρ-image reifies
  `transportComposeFirst`/`Second`/`Into` = (ρ(f), ρ(g), itself), well-typed on the nose. **STEP B.**
- `q_ancestral_transport_resolves` — **complete coverage**: every realized-proper-ancestor pair
  (A, B) has a `prim:AncestralGroundingPath` whose transport resolves onto ρ(B) (45 pairs, 45 paths,
  0 uncovered) — "dual-grounded two ways" made a terminating fact. **STEP B.**
- `q_yoneda_faithful` — `A ↦ yo(A)` is injective: no two distinct types share a representable. **STEP C.**
- `q_yoneda_full` — Hom(A,B) ↔ Nat(yo A, yo B) is a bijection (finite thin form): endpoints
  functorial, `yonedaArrowOf` injective and surjective onto the 59 generators. **STEP C.**
- `q_naturality_commutes` — ρ: yo ⇒ R is natural: every `prim:NaturalitySquare` has pinned,
  well-formed corners and `natCommutes true` (vacuous-match escape closed). **STEP C.**
- `q_yoneda_point` — the Frame **is** the Yoneda point: `prim:Frame prim:isYonedaPoint true` (and not
  `false`). **STEP E.**
- `q_yoneda_evaluation_sound` — every `prim:YonedaEvaluation`'s `evalYields` equals ρ of the type whose
  representable it evaluates (`prim:rhoObject` of the `?t` with `?t prim:yonedaObject` = the
  evaluation's `evalPresheaf`) — realization = Yoneda evaluation at the representable. **STEP E.**
- `q_functor_composition_total` — composite transport **exists and is covered**: every
  `prim:CompositeArrow` has a `prim:RealizationTransport` (`transportOf` it), **and** every composable
  `prim:SubtypeArrow` pair (`f: A→B, g: B→C`) has a `prim:CompositeArrow` (`composeArrowFirst = f`,
  `composeArrowSecond = g`) — closing the existence/coverage gap `q_functor_composition` cannot see. **STEP E.**

Each ASK carries an inline **DATA CONTRACT** comment naming the exact triples the downstream
TTL must emit to turn it GREEN — the suite defines "done" precisely.

## Consumers (produced interfaces)

- **AOB meta-ontology (#2):** grounds each atom's `tensor`/byte field into the Physical olog + `ρ`.
- **S/O/P-tower CRS (#3):** grounds `z` (uint16 of first two `source_sha256` octets) into the
  Binary/Hash tower + byte descent; `CRS`/`Coordinate` formal objects seed the geometry.
- **Projection packet (#4):** the realization effects seed the 5 loss classes.
- **File+format taxonomy (#5):** formats declare leaf datatypes against these towers.
- **Depth remediation (#8):** every basicttl untyped individual / stub class dual-grounds here.
- **Render seal (#9):** the colimit round-trip is the per-primitive split↔consolidated reversibility.

## How to re-run

```bash
basicttl/primitives/checks/run-floor-checks.sh
```

Exits 0 iff: every TTL parses, pyshacl conforms (once `primitives.shapes.ttl` exists), the depth
gate passes (every `owl:Class` ≥ 200-char `rdfs:comment`), and every EXPECT-TRUE ASK returns true.
The depth gate alone:

```bash
python3 scripts/ontology-depth-check.py basicttl/primitives
```

Stack: rdflib 7.6.0 + pyshacl 0.40.1; Turtle + SHACL + SPARQL 1.1. Wired into the multi-engine
CI in W4.

## Verification (the green run — evidence-before-completion)

The floor is proven, not asserted. The **"what's a number" litmus** (`q_number_tower` +
`q_number_realized`) is visibly GREEN below alongside the full **21-ASK** suite (the original 12, the
6 functor/Yoneda probes, and the 3 STEP E residual-teeth ASKs), the SHACL law (now **13**
`sh:NodeShape`s), and the depth gate. Captured verbatim from
`basicttl/primitives/checks/run-floor-checks.sh`:

```
parse OK: 4 data ttl, 8346 triples
SHACL conforms: True
  PASS  q_number_tower
  PASS  q_number_realized
  PASS  q_universality
  PASS  q_colimit_roundtrip
  PASS  q_colimit_reflexive
  PASS  q_frame_effect
  PASS  q_bytevector_cap
  PASS  q_kleisli_welltyped
  PASS  q_monad_unit
  PASS  q_monad_assoc
  PASS  q_byte_descent
  PASS  q_rgb
  PASS  q_functor_identity
  PASS  q_functor_composition
  PASS  q_ancestral_transport_resolves
  PASS  q_yoneda_faithful
  PASS  q_yoneda_full
  PASS  q_naturality_commutes
  PASS  q_yoneda_point
  PASS  q_yoneda_evaluation_sound
  PASS  q_functor_composition_total
ASKs: 21 run, 0 failed
ONTOLOGY DEPTH CHECK PASSED
Files checked: 5
FLOOR CHECKS GREEN
```

Reading of the evidence — stated at the exact scope the machinery checks. The **four data TTL
bodies** (`formal`/`physical`/`realization`/`taiji`) parse to a single **8,346-triple** graph
(3,123 for the base floor plus the categorical enrichment: 59 SubtypeArrows + 60 IdentityArrows +
45 CompositeArrows in `formal.ttl`, 164 RealizationTransports + 45 AncestralGroundingPaths in
`realization.ttl`, and 60 representables + 59 YonedaArrows + 60 RhoComponents + 59 NaturalitySquares
in `taiji.ttl`);
`primitives.shapes.ttl` is loaded **only** as the shapes graph (not mixed into the data), and the
depth gate's "Files checked: 5" counts those four plus the shapes file (the `frags/` copies were
removed). The SHACL law conforms with **real teeth on the class form**: `prim:DualGroundingShape`
is a `sh:sparql` constraint targeting `owl:Class` that walks `rdfs:subClassOf*` and flags any tower
class ungrounded on its whole subClassOf* line — so all **59 tower classes** are proven grounded,
and after the per-type build that grounding is **fully DIRECT**: every one of the 59 — the abstract
supertypes (Number, FormalType-tower roots) and the named sub-objects (NaturalWithZero, URI/IRI, …)
no less than the concrete leaves — carries its OWN `prim:Realization` (`prim:realizesFrom` the class
itself), its OWN reflexive carrier (a `PhysicalEncoding` whose `prim:interpretAs` is the class
itself), and its OWN `prim:Primitive`, so each class is grounded on ITSELF (SPARQL: 59 tower classes,
59 direct-grounded, 0 transitive-only). The shape's `rdfs:subClassOf*` walk would additionally accept
ancestor- or descendant-grounding — that disjunctive tooth is retained on purpose so the class-form
orphan probe still bites — but no class in this floor relies on that fallback. The
injected class-form orphan `ex:OrphanB a owl:Class ; rdfs:subClassOf prim:FormalType` is CAUGHT
(`conforms=False`). `EncodingShape` caps scalar `bitWidth ≤ 128` and `ByteVectorEncodingShape` caps
`byteCount ≤ 128` — both proven by probe (a `bitWidth 900` scalar and a `byteCount 129` vector are
both caught). The value-type checks of `EncodingShape`/`RealizationShape`/`PrimitiveShape` are
**defang-proof** (sh:in + sh:sparql, not the range-inference-vacuous `sh:class`) and each was proven
to bite by probe: an `interpretAs` to a non-tower node, a bogus `byteOrder`, and a bogus `frameEffect`
are all caught. `prim:ColimitReflexivityShape` enforces the true-identity round-trip on the **class**
of primitives (a primitive whose `physicalFacet → interpretAs` differs from its `formalFacet` is
caught), and `prim:ByteOctetDistinctionShape` catches any `Byte`/`Octet` collapse (an injected
`prim:Byte rdfs:subClassOf prim:Octet` is caught). `prim:KleisliCompositionShape` enforces the
**well-typedness of every reified Kleisli `Composition`** — `composeFirst.kCod = composeSecond.kDom`
and the result spanning them — and is proven to bite by an injected ill-typed composition
(`composeFirst` = `k_Real_Float64` with codomain Float64, `composeSecond` = `k_id_Real` with domain
Real: `pyshacl conforms=True → False`, `q_kleisli_welltyped True → False`); this is exactly the defect
the earlier decorative right-unit witness carried, now closed at the source with `prim:k_id_Float64`
(η at the **codomain** Float64). All twenty-one EXPECT-TRUE ASKs return true: the ℕ⊂ℤ⊂ℚ⊂ℝ⊂ℂ + imaginary chain and its
correct-width/composite realizations (`q_number_realized`, extended to ℚ→Product, ℂ→Product,
Imaginary→Real, Bignum→ByteVector); the class-level grounding litmus (`q_universality`); the
non-dangling and **true-identity** colimit round-trips (`q_colimit_roundtrip` + `q_colimit_reflexive`,
the latter proven to bite by a wrong-`interpretAs` primitive probe); the Frame effect law; the
two-cap `q_bytevector_cap` (proven against the enforced caps, not a 1024-bit decoy); the
well-typedness of every Kleisli composition (`q_kleisli_welltyped`); the monad **two-sided unit and
associativity** laws over those well-typed reified `Composition` witnesses — left unit η_A >=> f ≡ f
(η at the domain A), right unit f >=> η_B ≡ f (η at the **codomain** B), and associativity — each with
a genuine well-typed witness (`q_monad_unit` + `q_monad_assoc`); the byte-descent to `prim:Bit`;
the RGB Octet triple; **and the six categorical-enrichment probes** — ρ's functor identity and
composition laws over the materialised `prim:RealizationTransport`s (`q_functor_identity` +
`q_functor_composition`), the complete resolution of every ancestral-grounding path onto ρ(ancestor)
(`q_ancestral_transport_resolves`, 45/45), and literal Yoneda faithfulness, fullness and naturality
(`q_yoneda_faithful` + `q_yoneda_full` + `q_naturality_commutes`); **and the three STEP E
residual-teeth probes** — the Frame = Yoneda-point identification (`q_yoneda_point`), Yoneda-evaluation
soundness (`q_yoneda_evaluation_sound`, 60 evaluations, 0 mismatches), and composite-transport
existence/coverage (`q_functor_composition_total`, 45 composites transported, every composable subtype
pair covered). The depth gate confirms
every `owl:Class` across the files carries a ≥200-char `rdfs:comment`, and — beyond the gate — every
`prim:PhysicalEncoding`, `prim:Realization`, `prim:Primitive`, `prim:KleisliArrow` and
`prim:Composition` individual now carries a genuine ≥200-char comment (no bare nodes remain). There
are **no** `silm:isProvisional` nodes anywhere in the floor (0 actual `silm:isProvisional` triples;
the string survives only inside comment prose that explains why a given atom needs none).

**DEFECT-1 monad right-unit remediation (2026-08-08).** The shipped `prim:comp_rightUnit`
was decorative: its `composeSecond` was `prim:k_id_Real` (η at the DOMAIN Real) instead of η at the
CODOMAIN of `f: Real ⤳ Float64`, so the right-unit witness was ILL-TYPED (`f.kCod = Float64 ≠ Real`)
and proved nothing. The fix: `prim:k_id_Float64` (η at Float64, `kDom = kCod = Float64`,
`isMonadUnit true`) was added and `prim:comp_rightUnit` rewritten to `composeFirst = f`,
`composeSecond = k_id_Float64` (η at the codomain), `composeInto = f` — well-typed on all three edges.
A `prim:KleisliCompositionShape` (`sh:sparql`, targeting `prim:Composition`) and `q_kleisli_welltyped`
(EXPECT-TRUE) now enforce well-typedness of every composition, and `q_monad_unit` was rewritten to
witness BOTH unit laws over well-typed compositions referencing `kDom`/`kCod` (left unit η_A >=> f,
right unit f >=> η_B). The `isMonadUnit` property's `rdfs:domain` was moved from `prim:Realization`
to `prim:KleisliArrow` so the identity-arrow flag does not (under `inference="rdfs"`) mis-type the
Kleisli identities as `Realization`s and trip `RealizationShape`.

**Final re-verify — STEP-D milestone, pre-STEP-E (2026-08-08).** A fresh run at the STEP-D milestone —
before the STEP E residual teeth (below) added the final three ASKs, so the suite stood at 18 — reproduced
the then-current green run: `run-floor-checks.sh` exit 0 (parse OK 8346 triples · SHACL conforms=True ·
18/18 ASKs PASS · depth gate PASSED, 5 files); `scripts/ontology-depth-check.py basicttl/primitives` exit 0; a standalone
`pyshacl` over the four data TTLs against `primitives.shapes.ttl` (`inference="rdfs"`) conforms=True
with **0** validation results; the scratch **ungrounded tower-class count = 0** over all **59** tower
classes. The four original mandated probe injections were each re-confirmed **CAUGHT** (pyshacl
`conforms=True → False`, and the matching ASK `True → False`): (1) class-form orphan
`ex:OrphanB a owl:Class ; rdfs:subClassOf prim:FormalType` → `prim:DualGroundingShape` /
`q_universality`; (2) over-wide ByteVector `prim:byteCount 129` → `prim:ByteVectorEncodingShape` /
`q_bytevector_cap`; (3) wrong-type `interpretAs` escaping the tower → `EncodingShape` `sh:sparql` /
`q_colimit_roundtrip` (plus a wrong-facet Primitive → `prim:ColimitReflexivityShape` /
`q_colimit_reflexive`); (4) ill-typed composition (`composeFirst = k_Real_Float64`,
`composeSecond = k_id_Real`, so `composeSecond.kDom = Real ≠ Float64 = composeFirst.kCod`) →
`prim:KleisliCompositionShape` / `q_kleisli_welltyped`.

**Categorical-enrichment teeth (2026-08-08).** The six enrichment probes and two enrichment shapes
were each proven to **bite** by injection (`True → False`), run over the merged 4-file data graph:
(5) an extra `prim:IdentityArrow` on a realized class with no matching identity transport →
`q_functor_identity` `True → False`; (6) rewiring a subtype transport's `prim:transportCod` (a leg of
a composite) to a wrong carrier → `q_functor_composition` `True → False` **and** `prim:FunctorTransportShape`
`conforms=True → False`; (7) deleting one `prim:AncestralGroundingPath` (leaving a realized-ancestor
pair uncovered) → `q_ancestral_transport_resolves` `True → False`; (8) colliding two distinct types
onto one representable (`prim:Bool prim:yonedaObject prim:repr_Bag`) → `q_yoneda_faithful` `True → False`;
(9) removing a `prim:YonedaArrow`'s `prim:yonedaArrowOf` (breaking surjectivity onto a generator) →
`q_yoneda_full` `True → False`; (10) dropping a square's `prim:natCommutes`, rewiring a
`prim:natComponentCod` to a different valid `prim:RhoComponent`, **and** pointing it at a dangling node
(the closed vacuous-match escape) → `q_naturality_commutes` `True → False` in all three; (11) an
injected orphan `ex:Orphan a owl:Class ; rdfs:subClassOf prim:FormalType` (no `yonedaObject`, no
`rhoComponentAt`) → `prim:YonedaShape` `conforms=True → False`; (12) a new `prim:SubtypeArrow` with
`rhoObject` endpoints but no transport → `prim:FunctorTransportShape` `conforms=True → False`. **No ASK
is vacuous**: the positive ASKs return false on an empty graph (they genuinely depend on the data), and
every `FILTER NOT EXISTS` ASK flips false under a targeted violating injection — so "green" is produced
by the graph actually holding the law, never by scoping the teeth away.

**STEP E residual teeth (2026-08-08).** Two residuals were materialised-but-UNENFORCED — the Frame =
Yoneda-point / Yoneda-evaluation facts (`prim:Frame prim:isYonedaPoint`, the 60 `prim:YonedaEvaluation`
edges) and the composite-transport EXISTENCE/COVERAGE guarantee — so injecting `isYonedaPoint=false`, a
wrong `evalYields`, a removed composite transport, or a removed composite arrow all left the floor GREEN.
Three EXPECT-TRUE ASKs (`q_yoneda_point`, `q_yoneda_evaluation_sound`, `q_functor_composition_total`) and
three SHACL shapes (`prim:FrameYonedaPointShape`, `prim:YonedaEvaluationShape`,
`prim:CompositeTransportCoverageShape`) close them, ADDING structure and stripping none. `q_yoneda_point`
holds iff `prim:Frame prim:isYonedaPoint true` (and not `false`); `q_yoneda_evaluation_sound` holds iff
every `prim:YonedaEvaluation`'s `prim:evalYields` equals `rho` of the type whose representable it evaluates
(`prim:rhoObject` of the `?t` with `?t prim:yonedaObject` = the evaluation's `prim:evalPresheaf`);
`q_functor_composition_total` holds iff (a) every `prim:CompositeArrow` has a `prim:RealizationTransport`
(`prim:transportOf` it) AND (b) every composable `prim:SubtypeArrow` pair `(f: A→B, g: B→C)` has a
`prim:CompositeArrow` with `composeArrowFirst = f`, `composeArrowSecond = g`. Each was proven to **bite** by
injection over the merged 4-file data graph (baseline True → after-injection False; `conforms=True → False`):
(a) replacing `prim:Frame prim:isYonedaPoint true` with `...false` → `q_yoneda_point` `True → False` **and**
`prim:FrameYonedaPointShape` `conforms=True → False`; (b) a wrong `evalYields` on one evaluation
(`prim:yeval_Bag prim:evalYields prim:Boolean`) → `q_yoneda_evaluation_sound` `True → False` **and**
`prim:YonedaEvaluationShape` `conforms=True → False`; (c) deleting the `prim:RealizationTransport` of a
composite arrow (`prim:rt_comp_Bignum_Rational`) → `q_functor_composition_total` `True → False` **and**
`prim:CompositeTransportCoverageShape` `conforms=True → False`; (d) deleting a composite arrow whose two
legs are still-present subtype generators (`prim:compArr_Bignum_Rational`, legs `sub_Bignum_Integer` /
`sub_Integer_Rational`) → `q_functor_composition_total` `True → False` (part (b), coverage — ASK-enforced,
so `conforms` stays True there, exactly as designed). None is vacuous: `q_yoneda_point` is false on an
empty graph, and the two `FILTER NOT EXISTS` universals flip false under their targeted injection. The
full prior teeth set was re-confirmed intact alongside these: all **16** prior probes still bite (the 4
mandated base probes + the 12 base/enrichment probes, e.g. class-form orphan → `DualGroundingShape` /
`q_universality`, `byteCount 129` → `ByteVectorEncodingShape` / `q_bytevector_cap`, bogus `byteOrder` /
`frameEffect` → `EncodingShape` / `RealizationShape`, `Byte ⊂ Octet` → `ByteOctetDistinctionShape`,
ill-typed composition → `KleisliCompositionShape` / `q_kleisli_welltyped`, rewired subtype `transportCod` →
`FunctorTransportShape` / `q_functor_composition`, deleted `AncestralGroundingPath` →
`q_ancestral_transport_resolves`, collided representable → `q_yoneda_faithful`, removed `yonedaArrowOf` →
`q_yoneda_full`, dropped `natCommutes` → `q_naturality_commutes`, new transport-less `SubtypeArrow` →
`FunctorTransportShape`), and all **18** prior ASKs still PASS in the green run above.

## Status in the rebuild DAG

SP1 is the first of W2's nine sub-projects. This floor now sets
`silm:phase_w2_sp1 silm:hasStatus "completed"` in `basicttl/dag/dag_instances.ttl` (flipped
2026-08-08 with the green evidence recorded inline; the DAG re-parses to 630 triples and re-conforms
after the flip); `silm:wf_w2` itself remains `in-progress` until SP2–SP9 land. The
between-sub-project adversarial panel (DAG Gate discipline) reviews this floor before SP2 (the AOB
meta-ontology, the first consumer above) opens its own brainstorming gate.
