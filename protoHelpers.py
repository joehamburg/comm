from google.protobuf.internal.encoder import _VarintEncoder
from google.protobuf.internal.decoder import _DecodeVarint

def encode_varint(value):
    data = []
    _VarintEncoder()(data.append, value, False)
    return b''.join(data)

def decode_varint(data):
    return _DecodeVarint(data, 0)[0]


def import_mod(mod, package, class_name):
    return getattr(import_module(mod, package), class_name)