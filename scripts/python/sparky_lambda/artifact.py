"""Pure typed artifact locators for the Lambda boundary."""
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

from __future__ import annotations

from dataclasses import dataclass

from .contract import Contract
from .locator import Locator


@dataclass(frozen=True, slots=True)
class Request:
    locator: Locator
    schema_identity: str
    framing_identity: str


@dataclass(frozen=True, slots=True)
class Response:
    locator: Locator
    schema_identity: str
    framing_identity: str


def request(contract: Contract, locator: Locator) -> Request:
    return Request(
        locator=locator,
        schema_identity=contract.artifact.request_schema_identity,
        framing_identity=contract.artifact.framing_identity,
    )


def response(contract: Contract, locator: Locator) -> Response:
    return Response(
        locator=locator,
        schema_identity=contract.artifact.response_schema_identity,
        framing_identity=contract.artifact.framing_identity,
    )
