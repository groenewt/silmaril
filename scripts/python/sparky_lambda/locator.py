"""Canonical IRI locators and their distinct host-path projections."""
#```python
#EXAMPLE OF OUR FUNCTIONAL RESTRICTION. LITERAL AND STRICT "ONE INPUT,One output"-> IF IT Cannot meet this criterion (this applies to any function anywhere where it receives ONE DEFINED TYPE PER iNPUT, THEN OUTPUT)< IF THIS CANNOT BE ACHIEVED WE CANNOT "CONSTRUCT A FRAME" AROUND OUR BYTE STREAM NOR CAN WE EVEN CLAIM "SUCCESS". PLEASE BE MINDFUL I HAVE FULL OVERVIEW OF THE CODEBASE AND ITS RATHER DISAPPOINT HOW MUCH LEXICAL, SEMANTIC AND TOPOLOGICAL RICHNESS WE LOSE BC THIS RULE IS NOT STRICTLY (and LIKE OUR CONFIG/{CONSTANTS,GATE *THERE ARE SO MANY JAVE VIOLATIONS!* } enforced. BAD RULE ENFORCE MENT IS WHAT GETS US KILLED
#T=Typevar('ANormalizedTypeUrn')
#X=Typevar('BNormalizedTypeUrn')
#Y=Typevar('CNormalizedTypeUrn')
#DEF somefunction(sometypekindbytestream:T)-> (someoutputsometypekindbytestream:X, someerroroutputsometypekindbytestream:Y):
#return SOMECALLABLE(sometypekindbytestream)
#T->(X,Y) IS A EXTREMELY STRICT HYGEINE RULE FOR IDK MAYBE 1) TO ACCOMPLISH MY FUCKING GOAL 2) TO FUCKING ENSURE PROPER SUBATOMIC MODELING 3) TO AVOID ANY AND ALL "BULLSHJT" bc like it has one parameter in, or it doesnt ;;;  It has only an effect (and implictly _error)( or it doesnt we are nto returning/workign with underfine sets. ARE URN TYPE DRIVE SWALLOWS ALL TO CREATE YONEDA POINTS (AGAIN SOMETHIGN YOU CAN SEARCH!)
#MORE AT /home/tristan/site_stage/cpg-highway/docs/campaigns/unary-byte-frame-law.md
#```

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FileLocationRegistration:
    adapter_identity: str
    atlas_type_identity: str
    substrate_identity: str
    lineage_predicate: str
    locator_predicate: str
    matched_scheme: str
    primary_scheme: str
    proof_status: str


@dataclass(frozen=True, slots=True)
class CanonicalIri:
    value: str
    atlas_type_identity: str

    def __post_init__(self) -> None:
        if not self.value or not self.atlas_type_identity:
            raise ValueError("canonical locator IRI and atlas type must not be empty")


@dataclass(frozen=True, slots=True)
class LexicalHostPathProjection:
    lexical: str
    source: CanonicalIri
    registration: FileLocationRegistration

    def __post_init__(self) -> None:
        if not self.lexical:
            raise ValueError("host-path projection must not be empty")


@dataclass(frozen=True, slots=True)
class Locator:
    canonical: CanonicalIri
    host_path: LexicalHostPathProjection

    def __post_init__(self) -> None:
        if self.host_path.source != self.canonical:
            raise ValueError("host-path projection does not reference its canonical IRI")
        if self.canonical.atlas_type_identity != self.host_path.registration.atlas_type_identity:
            raise ValueError("locator atlas type differs from its registered file adapter")
