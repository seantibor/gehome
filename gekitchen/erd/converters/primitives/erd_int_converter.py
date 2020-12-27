from ..abstract import ErdReadWriteConverter

def erd_decode_int(value: str) -> int:
    """Decode an integer value sent as a hex encoded string."""
    return int(value, 16)
def erd_encode_int(value: any, length: int = 2) -> str:
    """Encode an integer value as a hex string."""
    value = int(value)
    return value.to_bytes(length, 'big').hex()

class ErdIntConverter(ErdReadWriteConverter[int]):
    def __init__(self, length: int = 2):
        self.length = length
    def erd_decode(self, value: str) -> int:
        """Decode an integer value sent as a hex encoded string."""
        return erd_decode_int(value)
    def erd_encode(self, value) -> str:
        """Encode an integer value as a hex string."""
        return erd_encode_int(value)
