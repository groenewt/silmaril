from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.python.stdlib.ast.library import DEPENDENCY as AST
from config.gate.external.python.stdlib.builtins.open.library import DEPENDENCY as OPEN
from config.gate.external.python.stdlib.importlib.util.library import DEPENDENCY as IMPORTLIB_UTIL

ERRORS = "surrogateescape"
LEXICON = ENCODING.decode()
MODE = "r"
RELATIVE = "."
UNNAMED = ""


def DEPENDENCIES(origin: str, package: str) -> list:
    with OPEN(origin, MODE, encoding=LEXICON, errors=ERRORS) as handle:
        body = AST.parse(handle.read()).body
    dependencies = []
    for node in body:
        if isinstance(node, AST.Import):
            dependencies.extend(alias.name for alias in node.names)
        elif isinstance(node, AST.ImportFrom):
            relative = RELATIVE * node.level + (node.module or UNNAMED)
            dependencies.append(IMPORTLIB_UTIL.resolve_name(relative, package))
    return dependencies
