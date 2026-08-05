from config.constants.morphism.codebase.volume.artifact.manifest.inventory.field.order.value import VALUE as ORDER

VIOLATION = "manifest_inventory_field_missing="


def ENTRY(inventory: dict) -> dict:
    missing = [field for field in ORDER if field not in inventory]
    if missing:
        raise ValueError(VIOLATION + ",".join(missing))
    return {field: inventory[field] for field in ORDER}
