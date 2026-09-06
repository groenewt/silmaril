# `basicttl/foundation/` — the four-pillar Foundation floor (W2 · SP0)

The **bedrock** floor — the deepest layer of the ontology, a **taiji of four co-equal pillars**:
(1) **set theory** (structural / ETCS carriers), (2) the **algebra tower** (the full
magma→abelian-group spine + two-operation line + quasigroup/loop + module/vector, every rung a
`(Σ,E)` presented algebra minted through the LIFTED free⊣forgetful engine), (3) **space constructs**
(LIFTED Site/sheaf + `𝔗_f`; SYN point-set Top/Metric/Vector/Normed), and (4) **functionality/typing**
(Curry's `F` = the Frame arrow; B/C/W/K/I + `F_n` + Γ; the variance bifunctor; the implication taiji)
plus a **logic sub-floor** (P/N/⊃ + proof terms). SP1 (`basicttl/primitives/`), SP2 (`basicttl/aob/`)
and SP3 (`basicttl/crs/`) **re-anchor additively** onto this floor (design §7).

This is **this iteration's v1** — corpus-agnostic (Directive 13; zero corpus instances), built to be
re-run and relaunched, never for permanence. Namespace `fnd: <urn:silmaril:fnd:#>`.

**Governing law:** `docs/superpowers/specs/2026-08-31-w2-sp0-foundation-design.md` (the four pillars +
the §0 honesty ledger + the §7 re-anchor plan) and `docs/superpowers/plans/2026-08-31-w2-sp0-foundation-plan.md`.

## Honesty ledger (design §0 — load-bearing)

Every foundation atom carries an authority tag:

- **`DS`** — direct-source, verbatim Helios lift.
- **`PD`** — proof-derived from Helios.
- **`SYN`** — synthesized as cited standard-mathematical fact (the Directive-19 Curry precedent: math
  is fact and liftable; cite the source; do NOT pretend it is a Helios lift).

**LIFTED from Helios (DS/PD, each cited to an exact `helios/srcy/…/*.tex` file:line):** structural
`Set` / `Presheaf` / the topos `Ω`, the **Monoid** rung + the endomorphism-monoid seam vocabulary
(`21/05/04`), the **minting engine** `F_E(X)=T_Σ(X)/≡_E` + the free⊣forgetful adjunction (`26`),
**Site/sheaf + `𝔗_f`** + the non-Riemannian partition theorem (`25`/`19`/whitepaper `05`), the
DS/PD/SYN + Node-or-Arrow honesty machinery (appendix `37`:240), and the Frame/ρ/Yoneda apparatus the
arrow pillar recognizes. **SYN — cited standard math OR a maintainer-directive pattern, NEVER a
paper lift:** the **agnostic-progenitor pattern** (grep-verified ABSENT from `helios/srcy`; it is
Directive 17 + the maintainer `byte_order` worked example, the appendix-39 mirror reference-only), the
universal-object terminal `Unit` / initial `Void` (standard CT gap-fill), every rung above Monoid, the
two-operation line, quasigroup/loop, module/vector, ALL point-set spaces, the combinators / `F_n` / Γ,
the group **inverse law**, the entire logic sub-floor, and every worked-example witness individual —
teeth-proved per the maximal choice, honest-red where no v1 consumer exists. The corpus's explicit **refusal of
point-set topology** (`helios/srcy/papers/19/.../05/03_cell_complex_pasting.tex:11-13,69-74`) is the
recorded reason those space atoms are SYN, not LIFTED. Curry 1936 (*First Properties of Functionality
in Combinatory Logic*, Tôhoku Math. J. **41** 371–401) is **cited, never committed**.

The ledger is a MACHINE-CHECKED graph fact, not prose: `fnd:AuthorityTagShape` + `q_honesty_ledger`
(T11) prove that **every** fnd `owl:Class` / `owl:ObjectProperty` / `owl:DatatypeProperty` carries
**exactly one** tag from `{fnd:DS, fnd:PD, fnd:SYN}`, so no atom is left silently unclassified; and
`fnd:AuthorityHonestyShape` + `q_authority_honest` (T11, the self-enforcing tooth) prove the STRONGER
invariant that **every `fnd:DS`/`fnd:PD` atom carries an exact `helios/srcy/…/*.tex` file:line in its
comment**, so no SYN-grade synthesis can masquerade as a Helios lift merely by wearing a DS/PD tag.

### DS / PD / SYN breakdown (recounted on disk, rdflib — after the H1 honesty sweep)

| scope | DS | PD | SYN | total |
|-------|----|----|-----|-------|
| **all fnd subjects** | 52 | 11 | 545 | **608** |
| of which fnd `owl:Class` | 17 | 1 | 62 | **80** |
| fnd `owl:ObjectProperty` | — | — | — | **129** (all tagged) |
| fnd `owl:DatatypeProperty` | — | — | — | **23** (all tagged) |

Plus **one** non-fnd atom carries a tag: `aob:witnessGroup` (SYN) — the SP2 sealed-group witness the
T10 re-anchor models foundation-side. The heavy SYN majority is the honest ledger. The **H1 honesty
sweep** retagged the dishonest DS/PD atoms to their true SYN: the agnostic `fnd:AlgebraicStructure`
progenitor (a Directive-17 pattern, not a paper lift), the universal-object `fnd:Unit`/`fnd:Void`, and
every worked-example witness individual (`fnd:endoObjectX`/`fnd:idEndoX`/`fnd:oneObjectCat`/
`fnd:endoMonoidWitness`; the sheaf-gluing witnesses `fnd:regionU…`/`fnd:secA…`/`fnd:siteWitness`/
`fnd:sheafWitness`/`fnd:matchingFamilyWitness`) — all now SYN, matching `fnd:monoidModel` /
`fnd:metricSpaceWitness`. Every remaining DS/PD atom (structural Set, Monoid + the endomorphism seam
vocabulary, the minting engine, Site/sheaf + `𝔗_f`, the honesty machinery) now carries a real
`helios/srcy/` file:line, machine-enforced by `fnd:AuthorityHonestyShape`.

## Status

**T1–T11 — COMPLETE.** The four-pillar floor is authored, teeth-proved, and GREEN. Reproduce on disk:

```
bash basicttl/foundation/checks/run-foundation-checks.sh   # exit 0, GREEN
```

That runner proves (over the single merged **SP0 + SP1 + SP2 + SP3** graph, `inference="rdfs"`):

- **Prior floors untouched + green:** `run-crs-checks.sh` re-runs SP1 (21 ASKs) + SP2 (13 ASKs)
  standalone AND the merged SP1+SP2+SP3 graph — all green.
- **Parse OK:** SP0 = 9 data TTLs + SP1 = 4 + SP2 = 7 + SP3 = 5 → merged SP0+SP1+SP2+SP3 = **15541
  triples** (SP0-only = **3909 triples**).
- **SHACL conforms = True** for `foundation.shapes.ttl` (the SP0 law, **45 `sh:NodeShape` teeth**),
  AND for the prior-floor laws re-run over the SP0-augmented merge: `primitives.shapes.ttl`
  (the dual-grounding tooth), `crs.shapes.ttl`, and `aob.shapes.ttl` (full re-validation over the
  merge, because the T10 re-anchor edges touch aob focus nodes).
- **Every EXPECT-TRUE ASK true:** foundation **42** EXPECT-TRUE ASKs + SP1 21 + SP2 13 + SP3 10, 0 failed.
- **Depth gate PASSED** (10 files; every `owl:Class` ≥ 200-char `rdfs:comment` of real content).
- **Register self-check PASSED:** the **45** `sh:NodeShape` count in `foundation.shapes.ttl` == the
  tooth-register header rows == the `phase_w2_sp0` DAG figure — stale-register drift is itself teeth-caught,
  and README's own `sh:NodeShape` and EXPECT-TRUE ASK figures are gated against disk the same way.

Real counts, all freshly recounted on disk (rdflib / grep — Fix-B) and machine-gated so no figure here
can drift again: **80** fnd `owl:Class`, **129** fnd `owl:ObjectProperty`, **23** fnd
`owl:DatatypeProperty`, **608** distinct fnd subjects (every one honesty-tagged; **52** DS / **11** PD /
**545** SYN, subject-level — plus the one non-fnd `aob:witnessGroup` (also SYN, the sole tagged non-fnd
atom); class-level **17**/**1**/**62** of the 80); merged SP0+SP1+SP2+SP3 = **15541 triples**
(SP0-only = **3909 triples**); **45** SHACL `sh:NodeShape`; **42** EXPECT-TRUE ASKs; **19** named
`fnd:probe*` injection identifiers on disk (the remaining teeth use in-place perturbation probes documented
per row below). Every one of these figures is asserted EQUAL to its recomputed disk value against BOTH
this README and the `silm:phase_w2_sp0` DAG node by the runner's **count self-check** (step 5d of
`run-foundation-checks.sh`); any drift in either surface → runner RED. Every DS/PD atom carries an exact
`helios/srcy/…/*.tex` file:line, self-enforced by `fnd:AuthorityHonestyShape` / `q_authority_honest` — no
SYN atom masquerades as a Helios lift.

## Files

| file | concern |
|---|---|
| `engine.ttl` | §1 the minting engine (Signature / EquationSet / PresentedAlgebra / freeForgetful / GovAlg) + the DS/PD/SYN honesty machinery |
| `set_theory.ttl` | §2 structural Set floor (Set / element / Function / Relation / product / coproduct / Ω / Cardinality) |
| `algebra_spine.ttl` | §3 one-operation spine Magma…AbelianGroup + Quasigroup / Loop |
| `algebra_rings.ttl` | §3 two-operation line Semiring / Ring / Field + Module / VectorSpace |
| `spaces.ttl` | §4 Site / sheaf / `𝔗_f` (LIFTED) + Topological / Metric / Normed / Inner (SYN) |
| `functionality.ttl` | §5 Curry `F` + variance bifunctor + `F(X,X)`=Monoid seam + selfApplicationGuard |
| `combinators.ttl` | §5 B / C / W / K / I + `F_n` ladder + Γ compositor |
| `logic.ttl` | §5 `P_r` / N / ⊃ + proof terms + the Curry–Howard taiji |
| `reanchor.ttl` | §7 the `fnd:groundsIn*` edges from SP1 / SP2 / SP3 (additive) + `aob:SealedGroup ⊑ fnd:Group` |
| `foundation.shapes.ttl` | all 45 `sh:NodeShape` SHACL teeth (one shapes graph; loaded ONLY as the shapes graph) |
| `foundation.queries.sparql` | all 42 EXPECT-TRUE ASKs (inline DATA CONTRACT + PROBE OF RECORD each) |
| `checks/run-foundation-checks.sh` | the runner (below) |

## The runner (`checks/run-foundation-checks.sh`)

Being the bedrock, SP0 is green only when every floor above it stays green. The runner:

1. Re-runs the committed SP3 floor (`run-crs-checks.sh`), which itself transitively re-runs the SP1
   floor (`run-floor-checks.sh`) and SP2 floor (`run-aob-checks.sh`) standalone **and** the merged
   SP1 + SP2 + SP3 graph — this single call is the SP1 + SP2 + SP3 invariant.
2. Parses the merged **SP0 + SP1 + SP2 + SP3** graph and validates `foundation.shapes.ttl` (the SP0
   law) over it.
3. Re-runs the prior-floor laws — `primitives.shapes.ttl` (the dual-grounding tooth) and
   `crs.shapes.ttl` — over the SP0-augmented merged graph, and transfers (or fully re-validates)
   `aob.shapes.ttl` the same way the SP3 runner does, so the prior floors stay green **with SP0 mixed
   in**.
4. Requires every EXPECT-TRUE ASK of all four suites (foundation / SP1 / SP2 / SP3) true over the
   merged graph.
5. Runs the depth gate (every `owl:Class` under `basicttl/foundation` carries a ≥ 200-char
   `rdfs:comment`).

The SP0 data TTLs and the foundation ASK suite are **auto-discovered** (every `foundation/*.ttl`
except the shapes graph; every `# EXPECT-TRUE <name>` marker), so each later task's new file wires
itself in with no edit to the runner. Value-type checks use `sh:in` / `sh:sparql`, never a
range-inference-vacuous `sh:class` (the SP1 defang discipline).

Never run state-changing git from this floor. Author only under `basicttl/foundation/` (plus, in
Task T11 only, the additive `silm:phase_w2_sp0` node in `basicttl/dag/dag_instances.ttl`).

## Re-anchor (design §7 — additive, no prior triple removed)

SP1/SP2/SP3 re-anchor onto SP0 by NEW `fnd:groundsInSet` / `fnd:groundsInAlgebra` /
`fnd:groundsInSpace` / `fnd:functionalityOf` edges (`reanchor.ttl`), reserving `rdfs:subClassOf` for
genuine is-a. `q_reanchor_additive` proves every prior-floor grounding is an EDGE and no prior triple
was rewritten; the ONE real build is `aob:SealedGroup rdfs:subClassOf fnd:Group` (the SP2 sealed group
becomes a child of the fresh agnostic `fnd:Group`), teeth-proved by `q_sealedgroup_is_group` /
`fnd:SealedGroupIsGroupShape` over the T10 foundation-side model (`aob:witnessGroup`, a closed abelian
ℤ/4 Cayley table).

## Probe register (teeth proven by injection, conforms/ASK True→False)

Teeth are proven by PROBE INJECTION, never by absence of violations. Each row's probe flips its shape
`conforms=True→False` and (where a mirror ASK exists) that ASK `True→False`. Named `fnd:probe*` atoms
live on disk; the rest are in-place perturbations of the authored witness.

| task | tooth (+ mirror ASK) | probe of record (CAUGHT: True→False) |
|------|----------------------|--------------------------------------|
| T1 | the merged-graph runner genuinely re-validates the floors | break the SP3 (or any prior) load path (rename `basicttl/crs/*.ttl`) → the prior runner fails AND the SP0 merged parse fails → runner exits non-zero (RED) |
| T2 | `fnd:PresentedAlgebraShape` + `q_engine_presents` (5 clauses; the E-COVERAGE strengthening added clause 5) | remove `fnd:witnessCarrier fnd:mintedVia fnd:engineAdjunction` (carrier not `F_E`-produced, clause 3), add `fnd:witnessPresentedAlgebra fnd:satisfiesLaw fnd:foreignLaw` (a law outside its `E`, clause 4, the E-must-not-EXCEED direction), or delete `fnd:Semiring fnd:satisfiesLaw fnd:lawAddAssoc` while `fnd:Semiring fnd:rungRequiresLaw fnd:lawAddAssoc` and `fnd:RingAddAssocShape` still enforces additive associativity on every `fnd:Semiring` (clause 5, the E-must-COVER direction: a rung whose presentation OMITS an enforced law) → shape bites |
| T3 | `fnd:SetCarrierShape` + `q_set_carrier` | `fnd:probeUngroundedCarrier a fnd:FreeAlgebra` with no `fnd:groundsInSet` edge → shape bites |
| T3 | `fnd:MembershipTypedShape` + `q_membership_typed` | `fnd:probeUntypedElement fnd:elementOf fnd:witnessSetA` with no `fnd:hasDomain fnd:Unit` (not a `1→A` global element) → shape bites |
| T3 | `fnd:UniversalProductShape` + `q_universal_product` | `fnd:probeBadProduct a fnd:Product` with no projections and no factoriser → shape bites |
| T3 | `fnd:PresheafNotSetShape` + `q_presheaf_not_set` (PIN guard) | `fnd:witnessPresheaf owl:sameAs fnd:witnessPresheafElemSet` (the forbidden `P ≡ P(c)` collapse) → shape bites |
| T4/M1 | `fnd:MagmaClosureShape` + `q_magma_closure` (the base Magma rung's closure/totality tooth, CLASS-GENERAL over `fnd:Magma`, reusing the SealedGroup closure idiom; parity for the one rung that had a law but no tooth/witness) | `fnd:probeMagmaOpenResult a fnd:Magma` enumerating carrier `{A,B}` (`fnd:hasElement`) with an op row whose `fnd:opResult` is `fnd:elemC` (outside the enumerated carrier) → closure clause bites (`conforms True→False`, `q_magma_closure True→False`); the closed order-2 NON-associative witness `fnd:magmaModel` (a bare magma, not accidentally a semigroup) and the closed ℤ/4 `aob:witnessGroup` stay GREEN; `q_magma_closure` False on the empty graph (non-vacuous) |
| T4 | `fnd:SemigroupAssocShape` + `q_semigroup_assoc` | change `fnd:appSgAC fnd:opResult` so `(A·B)·C ≠ A·(B·C)` → shape bites |
| T4 | `fnd:MonoidIdentityShape` + `q_monoid_identity` | change `fnd:appMonEA fnd:opResult` from `A` to `E`, so `e·A ≠ A` → shape bites |
| T4 | `fnd:CommMonoidCommShape` + `q_commmonoid_comm` | change `fnd:appCmBA fnd:opResult` so `B·A ≠ A·B` → shape bites |
| T4 | `fnd:GroupInverseShape` + `q_group_inverse` (genuineness + inverse-COMPLETENESS, W1b) | **(genuineness)** change `fnd:appGrAB fnd:opResult` from `E` to `A`, so the declared inverse does not undo → constraint A bites; **(completeness, W1b)** a `fnd:Group` over `{E,A}` with `A` non-invertible and an `fnd:InversePairing` only for `E` (`fnd:hasGroupElement A` carries no pairing) → constraint B bites |
| T4 | `fnd:AbelianCommShape` + `q_abelian_comm` | change `fnd:appAbBA fnd:opResult` so a "non-commutative abelian" pair exists → shape bites |
| T4 | `fnd:QuasigroupDivisionShape` + `q_quasigroup_division` (generalised over the `fnd:Quasigroup` family: `fnd:quasigroupModel` + `fnd:loopModel`) | change `fnd:appQgAC fnd:opResult` so the quasigroup A-row breaks the Latin-square (unique division) property → shape bites (still biting after generalisation; the loop's 25-row Latin square stays GREEN) |
| T4/A2 | `fnd:QuasigroupTotalityShape` + `q_quasigroup_total` (the EXISTENCE half `fnd:QuasigroupDivisionShape` never checked: every `(a,b)` has a left AND right division solution) | DELETE the row `fnd:appQgAC` (`A·C=C`) from `fnd:quasigroupModel` so `A·x` never reaches `C` (a partial table) → the pair `(A,C)` has no left-division solution → the left-totality branch bites (`conforms True→False`, `q_quasigroup_total True→False`); `fnd:QuasigroupDivisionShape` (uniqueness) stays GREEN (a deleted row adds no duplicate); the real `fnd:quasigroupModel`/`fnd:loopModel` (full Latin squares) stay GREEN |
| T4 | `fnd:LoopIdentityShape` + `q_loop_identity` (L1 close: Loop's added-law tooth) | `fnd:probeLoopNoIdentity a fnd:Loop` — a genuine 3-element Latin square (a quasigroup) with **no** `fnd:hasIdentityElement` → branch 1 bites (a Loop with no two-sided unit); the non-associative order-5 `fnd:loopModel` (identity `E`, verified Latin square) stays GREEN; `q_loop_identity` False on the empty graph (non-vacuous) |
| T4 | `fnd:AlgebraProgenitorShape` (grounds-nothing + exactly-one-law) | **(A)** `fnd:AlgebraicStructure fnd:addsLaw fnd:lawInverse` (the progenitor grounding a law), **(B)** a rung cramming two `fnd:addsLaw` (≤1 upper bound), or **(C, H3)** delete `fnd:Semigroup fnd:addsLaw fnd:lawAssociativity` (a concrete rung stripped of its sole law — the ≥1 lower bound; the agnostic progenitor with zero `fnd:addsLaw` stays GREEN) → shape bites |
| T4 | `fnd:MonoidIsEndoShape` + `q_monoid_is_endo` (Pillar-4 seam) | change `fnd:endoMonoidWitness fnd:hasIdentityElement` to a non-`id_X` element → monoid identity ≠ object identity arrow → shape bites |
| T5 | `fnd:RingDistribShape` + `q_ring_distrib` | change `fnd:appRingMul_1_2` so `x·(y+z) ≠ (x·y)+(x·z)` on `(1,1,1)` → shape bites |
| T5/A1 | `fnd:RingAddAssocShape` + `q_ring_add_assoc` (additive associativity over every `fnd:Semiring`; the reified `fnd:ringStructure` table the spine `fnd:SemigroupAssocShape` never reaches) | change `fnd:appRingAdd_2_2 fnd:ringResult` from `fnd:ringOne` to `fnd:ringZero` (`2+2=0`), so on `(2,2,1)`: `(2+2)+1 = 0+1 = 1 ≠ 2 = 2+(2+1)` → shape bites (a `fnd:Ring` with non-associative addition); the real `fnd:ringModel`/`fnd:fieldModel` stay GREEN |
| T5/A1 | `fnd:RingAddCommShape` + `q_ring_add_comm` (additive commutativity over every `fnd:Semiring`; the `fnd:ringStructure` table the spine `fnd:CommMonoidCommShape`/`fnd:AbelianCommShape` never reach) | change `fnd:appRingAdd_0_2 fnd:ringResult` from `fnd:ringTwo` to `fnd:ringZero`, so `0+2 = 0 ≠ 2 = 2+0` → shape bites (a `fnd:Semiring` with non-commutative addition); the real models stay GREEN |
| T5/A1 | `fnd:RingMultAssocShape` + `q_ring_mult_assoc` (multiplicative associativity over every `fnd:Semiring`) | change `fnd:appRingMul_2_1 fnd:ringResult` from `fnd:ringTwo` to `fnd:ringZero` (`2·1=0`), so on `(2,1,2)`: `(2·1)·2 = 0·2 = 0 ≠ 1 = 2·(1·2) = 2·2` → shape bites (a `fnd:Ring` with non-associative multiplication); the real models stay GREEN |
| T5/R7-2 | `fnd:RingAddIdentityShape` + `q_ring_add_identity` (additive IDENTITY `0+x=x=x+0` over every `fnd:Semiring`, genuineness + EXISTENCE; the reified `fnd:ringStructure`/`fnd:hasZeroElement` the spine `fnd:MonoidIdentityShape` never reaches) | **(genuineness)** change `fnd:appRingAdd_0_1` (`0+1=1`) `fnd:ringResult` from `fnd:ringOne` to `fnd:ringZero`, so `0+1 = 0 ≠ 1` — the declared zero fails the left-unit law → constraint A bites (a non-additive-identity ring); **(EXISTENCE)** a fresh `fnd:Semiring` with NO `fnd:hasZeroElement` → constraint B bites; the real `fnd:ringModel`/`fnd:fieldModel` (`0+x=x`, `x+0=x`) stay GREEN, `q_ring_add_identity` FALSE on the empty graph |
| T5/R7-2 (Fix-B) | `fnd:RingMultIdentityShape` + `q_ring_mult_identity` (multiplicative IDENTITY `1*x=x=x*1` over every `fnd:Semiring`, genuineness + EXISTENCE; the reified `fnd:ringStructure`/`fnd:hasOneElement` the spine `fnd:MonoidIdentityShape` never reaches; **Fix-B** broadens the EXISTENCE scope from `fnd:Ring` to `fnd:Semiring` — a semiring is a monoid under multiplication and needs a two-sided 1 — mirroring the additive `fnd:RingAddIdentityShape`) | **(genuineness)** change `fnd:appRingMul_1_0` (`1·0=0`) `fnd:ringResult` from `fnd:ringZero` to `fnd:ringOne`, so `1·0 = 1 ≠ 0` — the declared one fails the left-unit law → constraint A bites (a non-mult-identity ring); **(EXISTENCE, Fix-B)** a fresh unit-less `fnd:Semiring` with NO `fnd:hasOneElement` → constraint B bites; the real models `fnd:ringModel`/`fnd:fieldModel` (`1·x=x`, `x·1=x`, both `fnd:Semiring` by subclass) stay GREEN, `q_ring_mult_identity` FALSE on the empty graph |
| T5/W1a | `fnd:RingAdditiveInverseShape` + `q_ring_additive_inverse` (genuineness + completeness) | a Boolean-OR "ring" on `{0,1}` with `1+1=1` (so `1` has no additive inverse), carrying an `fnd:AdditiveInversePairing` only for `0` → completeness constraint B bites (a semiring masquerading as a ring); the real `fnd:ringModel`/`fnd:fieldModel` (inverses `0↔0, 1↔2, 2↔1`) stay GREEN |
| T5 | `fnd:FieldMultInverseShape` + `q_field_mult_inverse` | change `fnd:appFieldMul_2_2` so `2·2 = 2 ≠ 1` — a nonzero element with no multiplicative inverse → shape bites |
| T5/R7-1 | `fnd:FieldMultCommShape` + `q_field_mult_comm` (field MULTIPLICATIVE-COMMUTATIVITY `a*b=b*a` over every `fnd:Field`; the multiplicative mirror of `fnd:RingAddCommShape`, scoped to `fnd:Field` — the Field rung's defining upgrade, since noncommutative rings/semirings are legitimate) | change `fnd:appFieldMul_1_2` (`1·2=2`) `fnd:ringResult` from `fnd:fieldTwo` to `fnd:fieldOne`, so `1·2 = 1` while `2·1 = 2` (`fnd:appFieldMul_2_1`) — the pair `(1,2)` is non-commutative → shape bites (a `fnd:Field` with non-commutative multiplication); the real `fnd:fieldModel` (GF(3), `1·2 = 2 = 2·1`) stays GREEN, `q_field_mult_comm` FALSE on the empty graph |
| T5 | `fnd:ModuleScalarShape` + `q_module_scalar` | `fnd:probeEscapingScalarAction` whose result is a ring element that is not a `fnd:hasModuleVector` (scalar action escaping the module) → shape bites |
| T5/W2 | `fnd:VectorSpaceAxiomsShape` + `q_vectorspace_axioms` (ALL EIGHT axioms) | **(axiom 5)** `fnd:saUnitLaw fnd:saResult` `A→B` (`1·A=B≠A`); **(axiom 6)** `fnd:appAbBB fnd:opResult` `A→E` (`a(u+v)≠au+av` on `a=2,u=v=A`); **(axiom 7)** `fnd:appFieldAdd_1_1 fnd:ringResult` `2→1` (`(a+b)v≠av+bv` on `a=b=1,v=A`); **(axiom 8)** `fnd:appFieldMul_2_1 fnd:ringResult` `2→1` (`(ab)v≠a(bv)` on `a=2,b=1,v=A`); axioms 1-4 via the `fnd:vectorAdditiveGroup a fnd:AbelianGroup` typing — each flips its own clause |
| T6 | `fnd:SheafGluesShape` + `q_sheaf_glues` | repoint `fnd:secGlobal fnd:glueRestrictsToA` so an agreeing family has no valid unique gluing → shape bites |
| T6 | `fnd:TopologyAxiomsShape` + `q_topology_axioms` | repoint `fnd:ixAB fnd:intersectResult` to a set not in τ (τ not closed under finite intersection) → shape bites |
| T6 | `fnd:MetricTriangleShape` + `q_metric_triangle` (identity / identity-of-indiscernibles / symmetry / triangle) | **(triangle)** raise `fnd:distAC` so `d(A,C) > d(A,B)+d(B,C)` → shape bites; **(indiscernibles, W2-FIXB)** a pseudometric with two DISTINCT zero-distance points (`d(x,y)=0, x≠y`) typed `fnd:MetricSpace` → the identity-of-indiscernibles clause bites (a pseudometric masquerading as a metric → RED); the real `fnd:metricSpaceWitness` (no off-diagonal zeros) stays GREEN |
| T7 | `fnd:FrameRecognitionShape` + `q_frame_is_functionality` | `fnd:probeBadFunctionality fnd:recognizesFrameCarrier fnd:probeNotAFrame` (a carrier with no `prim:isYonedaPoint`) → shape bites (recognition is onto the real Frame, not a rebuilt F) |
| T7 | `fnd:FunctorVarianceShape` + `q_functor_variance` | `fnd:probeVarStep` claiming `F(Dog,Dog) <: F(Animal,Dog)` (domain-widening) → shape bites |
| T7 | `fnd:SelfApplicationGuardShape` + `q_no_untyped_self_apply` (Fix-C: exemption requires a GENUINE resolution — the `fnd:passedGuard` target must be a `fnd:ContractGate`/`fnd:QuarantineResolution` that `fnd:marksProvisional` it while it carries `silm:isProvisional true`) | `fnd:chiSelfApplication fnd:passedGuard fnd:propA` (an arbitrary UNCONSTRAINED node) + `fnd:admittedAsProposition true`, drop `silm:isProvisional true` (an ungated `χχ` admitted as a proposition behind an arbitrary passedGuard — not genuinely resolved) → shape bites; the genuinely-resolved `fnd:gatedSelfApplication` (passedGuard → `fnd:typedSelfAppGate`, a `fnd:ContractGate` marking it provisional) and the ungated-but-provisional `fnd:chiSelfApplication` stay GREEN |
| T8 | `fnd:CombinatorReducesShape` + `q_combinator_reduces` | change `fnd:redK fnd:reducesTo` from `x` to `y` (`Kxy=y`, the wrong projection) → shape bites |
| T8 | `fnd:FnLadderShape` + `q_fn_ladder` | change `fnd:fnRung2 fnd:fnPredecessor` to `fnd:fnRung0` (predecessor+1 ≠ own index, a broken rung) → shape bites |
| T8 | `fnd:CombinatorProgenitorShape` (grounds-nothing) | (a) `fnd:Combinator fnd:combinatorArity 2` (the progenitor grounding an arity), or (b) a child cramming two arities → shape bites |
| T9 | `fnd:ImplicationKCWShape` + `q_implication_kcw` | `fnd:probeLawK` typing `K` as `A ⊃ B` (consequent atomic, not the required implication shape) → shape bites |
| T9 | `fnd:CurryHowardShape` + `q_curry_howard` | `fnd:probeCh` pairing `F(Animal,Dog)` with `Dog ⊃ Animal` (arrow-sense and implication-sense diverge on the witness) → shape bites |
| T9 | `fnd:ProofTermTypedShape` + `q_proof_term_typed` | `fnd:probeProof` claiming to prove `Animal ⊃ Dog` but typed `F(Dog,Animal)` → shape bites |
| T10 | `fnd:ReanchorAdditiveShape` + `q_reanchor_additive` | **(algebra)** `fnd:probeBadAlgebraGrounding fnd:groundsInAlgebra fnd:setBit2` (a re-anchor onto a `fnd:Set` with no `fnd:hasSignature`) → algebra branch bites; **(space, H2)** delete the sole `crs:GeographicPlaneGeometer fnd:groundsInSpace fnd:metricSpaceWitness` edge → `q_reanchor_additive` FALSE, or `crs:CoordinateDerivation fnd:groundsInSpace fnd:setBit2` (a `fnd:Set` with no space-structure edge) → space branch bites |
| T10 | `fnd:SealedGroupIsGroupShape` + `q_sealedgroup_is_group` | change `fnd:sgApp_a_c fnd:opResult` from `e` to `b` (`a·c = b ≠ e`) so the `aob:retracts` inverse pairing no longer two-sidedly undoes → inverse-universal branch (and `fnd:GroupInverseShape`) bite |
| T10/H2 | `fnd:ReanchorLandingParityShape` | **(set, POSITIVE test)** `fnd:probeSubj fnd:groundsInSet fnd:witnessPresheaf` (a `fnd:Presheaf`, not a `fnd:Set`) — or the same onto `fnd:witnessProduct` / `fnd:card256` (a `fnd:Cardinality`) / `fnd:B` (a `fnd:Combinator`) / `fnd:Monoid` → set branch bites; **(functionality)** `prim:Frame fnd:functionalityOf fnd:Monoid` (an algebra with no `fnd:recognizesFrameCarrier`) → functionality branch bites. Brings all FOUR re-anchor edges to POSITIVE landing-type parity (no negative blacklist); every real `fnd:groundsInSet` target is typed `fnd:Set` (incl. the countably-infinite free-algebra `fnd:witnessUnderlyingSet`) so the real floor stays GREEN. |
| **T11** | **`fnd:AuthorityTagShape` + `q_honesty_ledger`** | **(a)** `fnd:probeUntaggedClass a owl:Class` with NO `fnd:authority` (silent-unclassified) → branch (a) bites; **(b)** `fnd:probeDoubleTag fnd:authority fnd:SYN, fnd:DS` (a SYN masquerading as a Helios lift via a double-tag) → branch (b) bites. Both flip `q_honesty_ledger True→False` and `conforms True→False`; the ASK is non-vacuous (FALSE on an empty graph). |
| **T11** | **`fnd:AuthorityHonestyShape` + `q_authority_honest` (H1, self-enforcing; W2-FIXB exact-line strengthening)** | **(a)** retag `fnd:AlgebraicStructure fnd:authority fnd:DS` (a SYN progenitor whose comment cites only Directive 17 + the ledger, no `helios/srcy/` — the exact masquerade-as-DS dodge), **(b)** `fnd:probeUncitedDS a owl:Class ; fnd:authority fnd:DS` with a comment carrying no `helios/srcy/` file:line, or **(c, W2-FIXB)** STRIP the `:line` off any real DS atom's sole `helios/srcy/…/*.tex` citation (e.g. `fnd:soleObject` `:36-39` → bare file) → constraint 1 (no lined citation left) AND constraint 2 (a bare-file citation now present) both bite (`q_authority_honest True→False`, `conforms True→False`). The tooth was STRENGTHENED from `CONTAINS("helios/srcy/")` (which a bare file with no `:line` passed) to a REGEX requiring an exact `:START(-END)?` line on EVERY `helios/srcy` citation of a DS/PD atom; the runner citation gate carries the load-bearing per-citation, DS/PD-scoped sweep. The ASK is non-vacuous. |

## Non-goals (design §9, honest-red deferrals)

Material/ZFC set theory (first-class `2^X`, transfinite cardinals, universe objects — structural floor
only); the appendix-39 `compass_artifact` classical-space tower (reference-only, not authored); corpus
instances (zero corpus binding — W5); live proof-checking of the logic floor (the teeth check the laws,
not a full proof assistant). Built to be relaunched (Directive 13).
