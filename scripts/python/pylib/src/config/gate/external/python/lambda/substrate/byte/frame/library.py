from config.constants.substrate.bit.width.host.jvm.value import VALUE as OBSERVED_BIT_WIDTH
from config.constants.substrate.bit.width.maximum.value import VALUE as MAXIMUM_BIT_WIDTH
from config.constants.substrate.bit.width.minimum.value import VALUE as MINIMUM_BIT_WIDTH
from config.constants.substrate.byte.frame.field.bit.order.prefix.value import VALUE as BIT_ORDER_PREFIX
from config.constants.substrate.byte.frame.field.byte.order.prefix.value import VALUE as BYTE_ORDER_PREFIX
from config.constants.substrate.byte.frame.field.lexical.projection.gap.prefix.value import VALUE as LEXICAL_PROJECTION_GAP_PREFIX
from config.constants.substrate.byte.frame.field.lexical.projection.prefix.value import VALUE as LEXICAL_PROJECTION_PREFIX
from config.constants.substrate.byte.frame.field.lineage.prefix.value import VALUE as LINEAGE_PREFIX
from config.constants.substrate.byte.frame.field.maximum.bit.width.prefix.value import VALUE as MAXIMUM_BIT_WIDTH_PREFIX
from config.constants.substrate.byte.frame.field.minimum.bit.width.prefix.value import VALUE as MINIMUM_BIT_WIDTH_PREFIX
from config.constants.substrate.byte.frame.field.observed.bit.width.prefix.value import VALUE as OBSERVED_BIT_WIDTH_PREFIX
from config.constants.substrate.byte.frame.field.payload.prefix.value import VALUE as PAYLOAD_PREFIX
from config.constants.substrate.byte.frame.field.schema.prefix.value import VALUE as SCHEMA_PREFIX
from config.constants.substrate.byte.frame.field.state.prefix.value import VALUE as STATE_PREFIX
from config.constants.substrate.byte.frame.prefix.value import VALUE as PREFIX
from config.constants.substrate.byte.schema.bit.order.identity.value import VALUE as BIT_ORDER_IDENTITY
from config.constants.substrate.byte.schema.byte.order.identity.value import VALUE as BYTE_ORDER_IDENTITY
from config.constants.substrate.byte.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.substrate.byte.schema.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.substrate.byte.schema.state.provisional.identity.value import VALUE as STATE_IDENTITY
from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.constants.substrate.byte.vector.lexical.projection.host.jvm.octet.gap.identity.value import VALUE as LEXICAL_PROJECTION_GAP_IDENTITY
from config.constants.substrate.byte.vector.lexical.projection.host.python.octet.hex.identity.value import VALUE as LEXICAL_PROJECTION_IDENTITY
from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.base.builtins.str.value import VALUE as String

def PROJECT(value: Bytes) -> Bytes: return PREFIX + SCHEMA_PREFIX + SCHEMA_IDENTITY + LINEAGE_PREFIX + LINEAGE_IDENTITY + MINIMUM_BIT_WIDTH_PREFIX + String(MINIMUM_BIT_WIDTH).encode(ENCODING.decode()) + MAXIMUM_BIT_WIDTH_PREFIX + String(MAXIMUM_BIT_WIDTH).encode(ENCODING.decode()) + OBSERVED_BIT_WIDTH_PREFIX + String(OBSERVED_BIT_WIDTH).encode(ENCODING.decode()) + STATE_PREFIX + STATE_IDENTITY + BIT_ORDER_PREFIX + BIT_ORDER_IDENTITY + BYTE_ORDER_PREFIX + BYTE_ORDER_IDENTITY + LEXICAL_PROJECTION_PREFIX + LEXICAL_PROJECTION_IDENTITY + LEXICAL_PROJECTION_GAP_PREFIX + LEXICAL_PROJECTION_GAP_IDENTITY + PAYLOAD_PREFIX + value
