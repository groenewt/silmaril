"""Pure typed JVM shoe values with ContractGate materialization."""
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
from .transport import RuntimeEvidence


@dataclass(frozen=True, slots=True)
class Process:
    capability: str
    runtime_shoe: str
    working_directory: Locator
    main_class: str
    scala_version: str
    bsp_registration: Locator
    bsp_registrations: tuple[Locator, ...]
    sources: tuple[Locator, ...]
    dependencies: tuple[Locator, ...]
    evidence: RuntimeEvidence
    command: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class Unavailable:
    capability: str
    runtime_shoe: str
    observations: tuple[str, ...]


class Requirement(RuntimeError):
    def __init__(self, observation: Unavailable) -> None:
        self.observation = observation
        super().__init__("; ".join(observation.observations))


def discover(repository: Locator, contract: Contract | None = None) -> Process | Unavailable:
    from .contract_gate.jvm import discover as materialize

    return materialize(repository, contract)


def require(repository: Locator, contract: Contract | None = None) -> Process:
    observation = discover(repository, contract)
    if isinstance(observation, Unavailable):
        raise Requirement(observation)
    return observation
