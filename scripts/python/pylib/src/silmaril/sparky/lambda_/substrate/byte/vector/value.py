from config.constants.substrate.bit.width.host.jvm.value import VALUE as OBSERVED_BIT_WIDTH
from config.constants.substrate.bit.width.maximum.value import VALUE as MAXIMUM_BIT_WIDTH
from config.constants.substrate.bit.width.minimum.value import VALUE as MINIMUM_BIT_WIDTH
from config.constants.substrate.byte.schema.bit.order.identity.value import VALUE as BIT_ORDER_IDENTITY
from config.constants.substrate.byte.schema.byte.order.identity.value import VALUE as BYTE_ORDER_IDENTITY
from config.constants.substrate.byte.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.substrate.byte.schema.lineage.identity.value import VALUE as SCHEMA_LINEAGE_IDENTITY
from config.constants.substrate.byte.schema.state.provisional.identity.value import VALUE as SCHEMA_STATE_IDENTITY
from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    payload: Bytes
    schema_identity = SCHEMA_IDENTITY
    schema_lineage_identity = SCHEMA_LINEAGE_IDENTITY
    schema_state_identity = SCHEMA_STATE_IDENTITY
    minimum_bit_width = MINIMUM_BIT_WIDTH
    maximum_bit_width = MAXIMUM_BIT_WIDTH
    observed_host_bit_width = OBSERVED_BIT_WIDTH
    bit_order_identity = BIT_ORDER_IDENTITY
    byte_order_identity = BYTE_ORDER_IDENTITY
