from config.constants.morphism.codebase.volume.artifact.manifest.inventory.header.count.value import VALUE as HEADER

VIOLATION = "inventory_csv_document_has_no_header_row="


def ROW_COUNT(document: list, locus: str) -> int:
    if len(document) < HEADER:
        raise ValueError(VIOLATION + locus)
    return len(document) - HEADER
