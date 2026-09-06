# W2 · SP1 Primitive Floor — remediation plan (panel NO-GO → GREEN)

> Fixes the CONFIRMED adversarial-panel findings against `wf_77f87831-c4f` so the floor actually
> satisfies its own binding law before any commit. Governing docs (read IN FULL first, every agent):
> `docs/praeriehund-demokratie-der-kategorien.md`, `docs/unary-byte-frame-law.md`,
> `docs/superpowers/specs/2026-08-07-w2-primitive-floor-design.md` **including the new §9 law
> corrections**, `ledger/W2/design_constraints.md` Directives 1–14, and the panel record in
> `.superpowers/sdd/2026-08-07-w2-sp1-primitive-floor/progress.md`.

## Global Constraints (apply to every task)
- **Namespace** `prim: <urn:silmaril:prim:#>`. Keep the fixed property contract:
  `realizesAs`, `realizesFrom`, `encoding`, `interpretAs`, `frameOutput`, `frameEffect`,
  `formalFacet`, `physicalFacet`, `gluedBy`, plus the harness-contract auxiliaries already minted by
  T1 (`bitWidth`, `byteWidth`/`byteCount`, `byteOrder`, `signedness`, `isMonadUnit`, `byteDescendsTo`,
  `hasChannel`, `ordinalMin`, `ordinalMax`). Do **not** rename existing individuals/properties.
- **Depth gate:** every new/edited `owl:Class` and every `prim:Realization`/`prim:PhysicalEncoding`
  individual that is a class carries an `rdfs:comment ≥ 200 chars` of real content (subtyping
  rationale + physical realization + typed effect), not filler.
- **Dual-grounding is universal (spec §9a):** after remediation, all 59 tower classes are grounded
  (self / ancestor / realized-descendant). Concrete leaves get their OWN realization.
- **No PROVISIONAL-dodge (Directive; spec §9b):** `isProvisional` only for genuinely undecidable gaps.
  Bignum/Rational/Complex/Imaginary are resolvable and MUST be realized.
- **Corpus-agnostic:** zero live-corpus binding (that is W5). No `gippidy`/`sparky`/sha256-literal data.
- **Evidence-first (RED→GREEN):** before authoring each task, run `run-floor-checks.sh` (and the
  task's probe) and capture the RED; after, capture GREEN. Subagents never run state-changing git.
- **Teeth are proven by probe injection**, not by absence of violations on the happy path.

## Interfaces
- **Consumes:** the 7 existing floor files under `basicttl/primitives/` (formal/physical/realization/
  taiji/primitives.shapes/primitives.queries + checks + README), and the class inventory (59 tower
  classes; 50 currently ungrounded — enumerated in the ledger).
- **Produces:** the same 7 files, corrected so all checks are GREEN **with real teeth**, ready for a
  clean re-audit panel. No new files unless a carrier genuinely needs one.

---

## Task R1 — Physical carriers + full realization coverage
**Files:** `basicttl/primitives/physical.ttl`, `basicttl/primitives/realization.ttl`
**RED:** `run-floor-checks.sh` currently green only because 50 classes are unchecked; a scratch query
`?c rdfs:subClassOf+ prim:FormalType FILTER NOT EXISTS realization-on-self-or-ancestor-or-descendant`
returns 50. Capture that count as RED.
**Do:**
1. `physical.ttl`: add a `prim:ByteVector`-typed `prim:PhysicalEncoding` individual carrying a
   `prim:byteCount` (variable, ≤128); add `Product`/pair composite encodings needed by Rational/
   Complex/Interval/Quantity/Measurement/Coordinate/Tuple; add IEEE-754 `Sign`/`Exponent`/`Mantissa`
   field facets, `Alignment`/`Padding`, and split `UTF16LE`/`UTF16BE` (spec §9c/§9g).
2. `realization.ttl`: author a `prim:Realization` (Kleisli/Frame arrow: `realizesFrom` <formal>,
   `encoding` <physical>, `frameOutput`, `frameEffect`) for **every concrete ungrounded class**:
   - Number tower: `Rational→Product(INT,INT)`, `Complex→Product(Float64,Float64)`, `Imaginary→Float64`,
     `Bignum→ByteVector(≤128)` (**remove the Uint128 isProvisional dodge**).
   - Text: `String→UTF-8`, `Grapheme→UTF-8`.
   - Temporal: `Date→INT32(days)`, `Time→INT64(nanos)`, `DateTime→INT64(epoch)+tz`, `Duration→INT64`,
     `Interval→Product(Instant,Instant)`.
   - Identifier: `URN/URI/IRI/QName/BlankNode → UTF-8` (realize the base, inherit down).
   - RDF term: `Literal→UTF-8(lexical)+datatype`, `Triple/Quad→N-Triples/N-Quads UTF-8`,
     `RDFGraph→Turtle bytes`.
   - Aggregate: `Tuple→concat`, `List→len-prefixed`, `Set→sorted len-prefixed`, `Bag→len+counts`,
     `Map→len kv-pairs`, `Vector→fixed array`, `Tensor→shape+row-major` (the AOB tensor block).
   - Quantity: `Quantity→Product(Real,Unit)`, `Dimension→UINT8 index`, `UnitOfMeasure→URN/index`,
     `Currency→ISO-4217 (UINT16/3×CHAR8)`, `Measurement→Product(Real,Real)`.
   - Geospatial: `Coordinate→Product(Real…)`, `Point/Line/Polygon→WKB`, `CRS→EPSG UINT16/32`,
     `Latitude/Longitude→Float64`.
   - Enum: `Enumeration/Ordinal/Categorical→UINT index`.
   - Other: `Kleene3→UINT8(0/1/2)`, `Blob→ByteVector`, `Hash→ByteVector(fixed)` (grounds the
     z-coordinate for SP3), `Sum→tag(UINT8)+payload`, `Optional→presence-bit+payload`,
     `Frame→Product(output,effect)`, `Void→empty 0-byte encoding (effect: uninhabited)`.
   Each realization's `frameEffect` states the real effect (rounding / narrowing / encoding-loss /
   ordering-canonicalization / overflow-domain / none / uninhabited).
**GREEN:** the scratch ungrounded-count query returns **0**; `run-floor-checks.sh` still exit 0.
**Review (spec+quality+depth):** every concrete class realized; no isProvisional-dodge remains;
effects accurate; comments ≥200 chars real.

## Task R2 — Taiji colimit atoms + monad laws
**Files:** `basicttl/primitives/taiji.ttl` (+ `realization.ttl`/`physical.ttl` if composition needs a home)
**RED:** SELECT of primitives where `physicalFacet→interpretAs ≠ formalFacet` returns 3
(Bignum/Instant/Decimal); no `prim:compose` / associativity ASK exists. Capture as RED.
**Do:**
1. Author a colimit `prim:Primitive` atom (`formalFacet`, `physicalFacet`, `gluedBy` <realization>)
   for each newly-realized concrete type, mirroring the existing 9.
2. **Fix the 3 non-reflexive round-trips** to identity: `Bignum→ByteVector→interpretAs Bignum`,
   `Instant→INT64(epoch)→interpretAs Instant`, `Decimal→(decimal/BCD encoding)→interpretAs Decimal`.
3. Model **Kleisli composition**: `prim:compose` (or reuse `prim:byteDescendsTo`) as the monad's
   `>=>`; define the byte-descent chain Real→Float64→ByteVector→Octet→Bit as a composed arrow.
4. Add **transitive-grounding gluing** for abstract supertypes (a supertype's atom points to the
   realized descendant that grounds it) so §9a holds structurally, not just by SHACL.
**GREEN:** reflexive-roundtrip SELECT returns 0 non-identities; composition arrow exists and is
navigable. **Review** as R1.

## Task R3 — SHACL teeth + queries + honesty
**Files:** `primitives.shapes.ttl`, `primitives.queries.sparql`, `formal.ttl`, `README.md`
**RED (proves the current teeth are a decoy):** with the pre-R3 shapes, inject
`ex:OrphanB a owl:Class ; rdfs:subClassOf prim:FormalType` → `pyshacl(inference=rdfs)` reports
`conforms=True` (uncaught). Inject `prim:Sneaky a prim:PhysicalEncoding ; prim:bitWidth 900` → the
old `q_bytevector_cap` returns True. Capture both as RED.
**Do:**
1. **Rewrite `FormalTypeShape`** as a `sh:sparql` constraint (node shape targeting `owl:Class`) that
   selects `?c rdfs:subClassOf* prim:FormalType` and flags any `?c` with no realization on itself, an
   ancestor, or a realized descendant. It MUST catch the class-form orphan (spec §9a probe of record).
2. Add **`ByteVectorEncodingShape`** (`prim:byteCount ≤ 128`) and keep `EncodingShape` scalar
   `bitWidth ≤ 128`; add a **`Byte ≠ Octet`** guard; add a **colimit-reflexivity** shape
   (`physicalFacet→interpretAs = formalFacet`). Fix the `sh:class` **defang** (range-inference makes
   value-type checks vacuous) — use `sh:sparql` or `sh:node` where `sh:class` can't independently fail.
3. **Queries:** extend `q_number_realized` to include ℚ→pair, Complex→pair, Imaginary→Real,
   Bignum→ByteVector; rewrite `q_bytevector_cap` to test the enforced cap (byteCount>128 OR scalar
   bitWidth>128 → fail; prove with the 900-bit probe); add `q_colimit_reflexive` (identity round-trip);
   add `q_universality` (every tower class grounded directly-or-transitively — the class-level litmus);
   rewrite `q_monad_unit` to test the left/right unit law; add `q_monad_assoc` (associativity of
   `>=>`). All EXPECT-TRUE, none vacuous.
4. **Honesty (`formal.ttl` + `README.md`):** remove the false universal enforcement claim; make every
   prose "realized as …" claim correspond to a real realization (now they do) or hedge it; reconcile
   the README ByteVector cap wording to the two-cap model (§9c); state coverage truthfully.
**GREEN:** `run-floor-checks.sh` exit 0 with the expanded ASK suite; the OrphanB class probe now yields
`conforms=False`; the 900-bit probe now fails `q_bytevector_cap`. **Review** as R1.

## Task R4 — Integration + teeth proof + DAG
**Files:** `README.md`, `basicttl/dag/dag_instances.ttl`
**Do:** run the full `run-floor-checks.sh` fresh; run the depth gate; run pyshacl over the floor;
run the three probe injections (class-form orphan, over-wide ByteVector, wrong-type interpretAs) and
show each is now CAUGHT; confirm all litmus ASKs green and none vacuous. Update the README verification
section to the true state. Flip `silm:phase_w2_sp1` `hasStatus` back to `"completed"` **only** with the
green evidence inline in the report. **Review (spec+quality+depth):** confirms teeth bite, no overclaim.

## Re-audit — adversarial triple panel (must return CLEAN)
Three adversaries (completeness / honesty / doctrine), each spawning two ontology-grounded
sub-subagents that re-verify on disk. They must specifically re-check: (a) all 59 classes grounded;
(b) SHACL catches the class-form orphan; (c) litmus reproduces ℚ→pair + Bignum→ByteVector; (d) every
round-trip is identity; (e) both width caps have teeth; (f) monad unit+assoc are real ASKs; (g) no
new overclaim or PROVISIONAL-dodge introduced by the expansion. Any surviving Critical/Important →
another fix round before commit.
