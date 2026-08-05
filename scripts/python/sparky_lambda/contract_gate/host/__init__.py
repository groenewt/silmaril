"""Host-specific mechanics confined to the Python ContractGate."""

from .octet import (
    DecodingAccepted,
    DecodingRejected,
    Encoding,
    EncodingEqual,
    EncodingUnequal,
    Projection,
    decode,
    equivalent,
    observe_encoding,
)

__all__ = (
    "DecodingAccepted",
    "DecodingRejected",
    "Encoding",
    "EncodingEqual",
    "EncodingUnequal",
    "Projection",
    "decode",
    "equivalent",
    "observe_encoding",
)
