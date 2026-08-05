"""Pure artifact/process composition over ContractGate-admitted evidence."""
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

from . import artifact, jvm
from .artifact import Request, Response
from .contract import Contract
from .jvm import Process
from .locator import Locator
from .transport import Execution, McpTool, ReceiptReadback


def _command(process: Process, command: tuple[str, ...]) -> Process:
    return Process(
        capability=process.capability,
        runtime_shoe=process.runtime_shoe,
        working_directory=process.working_directory,
        main_class=process.main_class,
        scala_version=process.scala_version,
        bsp_registration=process.bsp_registration,
        bsp_registrations=process.bsp_registrations,
        sources=process.sources,
        dependencies=process.dependencies,
        evidence=process.evidence,
        command=command,
    )


@dataclass(frozen=True, slots=True)
class Client:
    """Bind exact artifacts to one registered JVM process occurrence."""

    contract: Contract
    process_evidence: Process

    @classmethod
    def process(cls, repository: Locator, command: tuple[str, ...]) -> "Client":
        contract = Contract.discover(repository)
        registered = jvm.require(repository, contract)
        contract.require_capability(registered.capability)
        if not command:
            raise ValueError("explicit process projection requires a command")
        return cls(contract=contract, process_evidence=_command(registered, command))

    @classmethod
    def jvm(cls, repository: Locator) -> "Client":
        """Compose the registered JVM shoe from exact BSP/SBT evidence."""

        contract = Contract.discover(repository)
        process = jvm.require(repository, contract)
        contract.require_capability(process.capability)
        return cls(contract=contract, process_evidence=process)

    @classmethod
    def readback(cls, repository: Locator) -> ReceiptReadback:
        contract = Contract.discover(repository)
        contract.require_capability(contract.receipt_readback.capability)
        from .contract_gate.readback import readback

        return readback(contract)

    @classmethod
    def mcp(cls, repository: Locator) -> McpTool:
        contract = Contract.discover(repository)
        registration = contract.mcp_tool
        contract.require_capability(registration.capability)
        return McpTool(
            capability=registration.capability,
            state=registration.state,
            tool=registration.tool,
            argument_field=registration.argument_field,
        )

    def request(self, locator: Locator) -> Request:
        return artifact.request(self.contract, locator)

    def response(self, locator: Locator) -> Response:
        return artifact.response(self.contract, locator)

    def invoke(self, request: Request, response: Response) -> Execution:
        if request != self.request(request.locator):
            raise ValueError("Lambda request artifact metadata differs from contract")
        if response != self.response(response.locator):
            raise ValueError("Lambda response artifact metadata differs from contract")
        from .contract_gate.process import invoke

        return invoke(self.contract, self.process_evidence, request, response)


def invoke(
    repository: Locator,
    command: tuple[str, ...],
    request: Request,
    response: Response,
) -> Execution:
    """Invoke the evaluator through one explicit registered process projection."""

    return Client.process(repository, command).invoke(request, response)


def invoke_jvm(
    repository: Locator,
    request: Request,
    response: Response,
) -> Execution:
    """Invoke Scala Lambda through its provisional JVM process shoe."""

    return Client.jvm(repository).invoke(request, response)
