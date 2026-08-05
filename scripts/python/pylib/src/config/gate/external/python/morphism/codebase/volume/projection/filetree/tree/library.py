from config.constants.morphism.codebase.volume.projection.filetree.element.close.value import VALUE as ELEMENT_CLOSE
from config.constants.morphism.codebase.volume.projection.filetree.element.open.value import VALUE as ELEMENT_OPEN
from config.constants.morphism.codebase.volume.projection.filetree.heading.ladder.value import VALUE as LADDER
from config.constants.morphism.codebase.volume.projection.filetree.node.path.template.value import VALUE as NODE_PATH
from config.constants.morphism.codebase.volume.projection.filetree.register.anchor.value import VALUE as ANCHOR_PREFIX
from config.constants.morphism.codebase.volume.projection.filetree.register.base.value import VALUE as BASE
from config.constants.morphism.codebase.volume.projection.filetree.register.coordinate.value import VALUE as COORDINATE_SEPARATOR
from config.constants.morphism.codebase.volume.projection.filetree.register.depth.value import VALUE as DEPTH
from config.constants.morphism.codebase.volume.projection.filetree.register.level.value import VALUE as LEVEL_NAMES
from config.constants.morphism.codebase.volume.projection.filetree.register.ordinal.value import VALUE as START
from config.constants.morphism.codebase.volume.projection.filetree.register.point.value import VALUE as POINT
from config.constants.morphism.codebase.volume.projection.filetree.register.root.value import VALUE as ROOT
from config.constants.morphism.codebase.volume.projection.filetree.register.template.value import VALUE as REGISTER_TEMPLATE
from config.constants.morphism.codebase.volume.projection.filetree.scope.close.value import VALUE as SCOPE_CLOSE
from config.constants.morphism.codebase.volume.projection.filetree.scope.open.template.value import VALUE as SCOPE_OPEN
from config.constants.morphism.codebase.volume.projection.filetree.scope.step.value import VALUE as SCOPE_STEP
from config.constants.morphism.codebase.volume.projection.filetree.flush.interval.value import VALUE as INTERVAL
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.projection.inventory.lexical.path.separator.value import VALUE as SEPARATOR
from config.gate.external.python.morphism.codebase.volume.projection.filetree.lexical.cell.library import BREAKABLE
from config.gate.external.python.morphism.codebase.volume.projection.filetree.lexical.cell.library import CELL
from config.gate.external.python.stdlib.builtins.sorted.library import DEPENDENCY as SORT
from config.gate.external.python.stdlib.itertools.groupby.library import DEPENDENCY as GROUPBY
from silmaril.sparky.morphism.codebase.volume.projection.filetree.entry.value import Value as Entry
from silmaril.sparky.morphism.codebase.volume.projection.filetree.level.value import Value as Level
from silmaril.sparky.morphism.codebase.volume.projection.filetree.node.value import Value as Node
from silmaril.sparky.morphism.codebase.volume.projection.filetree.pair.value import Value as Pair

DESCENT = 1
LIMIT = len(LADDER) - DESCENT
ORIGIN = 0
SCOPE = SCOPE_OPEN % SCOPE_STEP


def UNWIND(depth: int) -> str:
    return SCOPE_CLOSE * depth + SCOPE * depth


def RELEASE(depth: int, ordinal: int) -> str:
    return UNWIND(depth) if ordinal % INTERVAL == ORIGIN else EMPTY


def LOCATION(pair: Pair) -> str:
    return pair.path


def ORDERED(pairs: tuple) -> tuple:
    return tuple(SORT(pairs, key=LOCATION))


def MERGED(pairs: tuple) -> tuple:
    return tuple(
        Pair(path, EMPTY.join(member.document for member in tuple(group)))
        for path, group in GROUPBY(pairs, LOCATION)
    )


def SEGMENTS(path: str) -> tuple:
    return tuple(path.split(SEPARATOR))


def ENTRIES(pairs: tuple) -> tuple:
    return tuple(Entry(SEGMENTS(pair.path), pair.document) for pair in pairs)


def LABELLED(level: Level) -> tuple:
    return tuple((entry.segments[level.depth], entry) for entry in level.entries)


def NAMED(label: tuple) -> str:
    return label[ORIGIN]


def GROUPED(level: Level) -> tuple:
    return tuple(
        Node(name, tuple(member for _, member in tuple(group)), level.depth)
        for name, group in GROUPBY(LABELLED(level), NAMED)
    )


def HEADING(node: Node) -> str:
    return LADDER[min(node.depth, LIMIT)] % CELL(node.name)


def PATH(node: Node) -> str:
    return SEPARATOR.join(node.entries[ORIGIN].segments[ORIGIN:node.depth + DESCENT])


def ANCHOR(node: Node) -> str:
    return ANCHOR_PREFIX + PATH(node)


def LOCATOR(node: Node) -> str:
    return NODE_PATH % BREAKABLE(PATH(node))


def COORDINATE(ordinals: tuple) -> str:
    return COORDINATE_SEPARATOR.join(POINT % ordinal for ordinal in ordinals)


def LEAVES(node: Node) -> str:
    return EMPTY.join(
        entry.document for entry in node.entries if len(entry.segments) == node.depth + DESCENT
    )


def BRANCHES(node: Node) -> tuple:
    return tuple(entry for entry in node.entries if len(entry.segments) > node.depth + DESCENT)


def REGISTERED(node: Node) -> bool:
    return len(BRANCHES(node)) > ORIGIN and node.depth < DEPTH


def REGISTER(node: Node, coordinate: tuple) -> str:
    return REGISTER_TEMPLATE % (
        ANCHOR(node),
        node.depth + BASE,
        ANCHOR(node),
        CELL(node.name),
        LEVEL_NAMES[node.depth],
        COORDINATE(coordinate),
        CELL(node.name),
        ANCHOR(node),
    )


def BLANK(node: Node, coordinate: tuple) -> str:
    return EMPTY


REGISTRY = {True: REGISTER, False: BLANK}


def NODES(node: Node, coordinate: tuple) -> str:
    return EMPTY.join(
        (
            HEADING(node),
            REGISTRY[REGISTERED(node)](node, coordinate),
            SCOPE,
            ELEMENT_OPEN,
            LOCATOR(node),
            LEAVES(node),
            ELEMENT_CLOSE,
            LEVEL(Level(BRANCHES(node), node.depth + DESCENT), coordinate),
            SCOPE_CLOSE,
        )
    )


def LEVEL(level: Level, coordinate: tuple) -> str:
    return EMPTY.join(
        NODES(node, coordinate + (ordinal,)) + RELEASE(level.depth, ordinal)
        for ordinal, node in enumerate(GROUPED(level), START)
    )


def TREE(pairs: tuple) -> str:
    return LEVEL(Level(ENTRIES(MERGED(ORDERED(pairs))), ORIGIN), ROOT)
