import socket
import sys
from helpers import encode_varint


def tcp_client_send(host, port, proto):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serialized_proto = proto.serialize()
    try:
        sock.connect((host, port))
        size = encode_varint(len(serialized_proto))
        sock.sendall(size + serialized_proto)
    finally:
        sock.close()

