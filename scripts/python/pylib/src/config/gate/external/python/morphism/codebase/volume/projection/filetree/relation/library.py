from config.constants.morphism.codebase.volume.projection.filetree.relation.anchor.value import VALUE as ANCHOR
from config.constants.morphism.codebase.volume.projection.filetree.relation.direct.value import VALUE as DIRECT
from config.constants.morphism.codebase.volume.projection.filetree.relation.resolved.value import VALUE as RESOLVED
from config.gate.external.python.morphism.codebase.volume.projection.filetree.columns.library import DETAIL_INDEXES
from config.gate.external.python.morphism.codebase.volume.projection.filetree.columns.library import INDEX
from config.gate.external.python.morphism.codebase.volume.projection.filetree.element.library import ELEMENT
from config.gate.external.python.morphism.codebase.volume.projection.filetree.element.library import PADDED
from config.gate.external.python.morphism.codebase.volume.projection.filetree.element.library import VALUE
from config.gate.external.python.morphism.codebase.volume.projection.filetree.source.library import HEADER
from config.gate.external.python.morphism.codebase.volume.projection.filetree.source.library import SCAN
from silmaril.sparky.morphism.codebase.volume.projection.filetree.cell.value import Value as Cell
from silmaril.sparky.morphism.codebase.volume.projection.filetree.corpus.value import Value as Corpus
from silmaril.sparky.morphism.codebase.volume.projection.filetree.keyed.value import Value as Keyed
from silmaril.sparky.morphism.codebase.volume.projection.filetree.locate.value import Value as Locate
from silmaril.sparky.morphism.codebase.volume.projection.filetree.ordinal.value import Value as Ordinal
from silmaril.sparky.morphism.codebase.volume.projection.filetree.padding.value import Value as Padding
from silmaril.sparky.morphism.codebase.volume.projection.filetree.pair.value import Value as Pair
from silmaril.sparky.morphism.codebase.volume.projection.filetree.record.value import Value as Record
from silmaril.sparky.morphism.codebase.volume.projection.filetree.scanned.value import Value as Scanned
from silmaril.sparky.morphism.codebase.volume.projection.filetree.schema.value import Value as Schema
from silmaril.sparky.morphism.codebase.volume.projection.filetree.selection.value import Value as Selection
from silmaril.sparky.morphism.codebase.volume.projection.filetree.shape.value import Value as Shape
from silmaril.sparky.morphism.codebase.volume.projection.filetree.source.value import Value as Source

UNRESOLVED = {}


def LITERAL(locate: Locate) -> str:
    return locate.value


def LOOKUP(locate: Locate) -> str:
    return locate.resolution[locate.value]


PATHS = {ANCHOR: LITERAL, DIRECT: LITERAL, RESOLVED: LOOKUP}


def PATH(locate: Locate) -> str:
    return PATHS[locate.relation](locate)


def ANCHORS(records: tuple) -> tuple:
    return tuple(record for record in records if record.relation == ANCHOR)


def CONTRIBUTORS(records: tuple) -> tuple:
    return tuple(record for record in records if record.relation in PATHS)


def MAPPING(keyed: Keyed) -> tuple:
    return tuple((row[keyed.key_index], row[keyed.path_index]) for row in keyed.reader)


def INDEXED(schema: Schema) -> tuple:
    return MAPPING(
        Keyed(
            schema.reader,
            INDEX(Selection(schema.header, schema.source.record.key)),
            INDEX(Selection(schema.header, schema.source.record.column)),
        )
    )


def ANCHORED(scanned: Scanned) -> tuple:
    return INDEXED(Schema(scanned.source, scanned.reader, HEADER(scanned.reader)))


def KEYS(record: Record) -> tuple:
    return ANCHORED(Scanned(Source(record, UNRESOLVED), SCAN(record.locus)))


def RESOLUTION(records: tuple) -> dict:
    return dict(pair for record in ANCHORS(records) for pair in KEYS(record))


def ROW(cell: Cell) -> Pair:
    return Pair(PATH(Locate(cell.shape.record.relation, cell.shape.resolution, VALUE(cell))), ELEMENT(cell))


def ROWS(shape: Shape) -> tuple:
    return tuple(ROW(Cell(shape, PADDED(Padding(shape.header, row)))) for row in shape.reader)


def SHAPED(schema: Schema) -> tuple:
    return ROWS(
        Shape(
            schema.source.record,
            schema.source.resolution,
            schema.header,
            schema.reader,
            INDEX(Selection(schema.header, schema.source.record.column)),
            DETAIL_INDEXES(Ordinal(schema.header, INDEX(Selection(schema.header, schema.source.record.column)))),
        )
    )


def SCANNED(scanned: Scanned) -> tuple:
    return SHAPED(Schema(scanned.source, scanned.reader, HEADER(scanned.reader)))


def ELEMENTS(source: Source) -> tuple:
    return SCANNED(Scanned(source, SCAN(source.record.locus)))


def CONTRIBUTIONS(corpus: Corpus) -> tuple:
    return tuple(
        pair
        for record in CONTRIBUTORS(corpus.records)
        for pair in ELEMENTS(Source(record, corpus.resolution))
    )


def CORPUS(records: tuple) -> Corpus:
    return Corpus(records, RESOLUTION(records))
