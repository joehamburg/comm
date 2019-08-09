import socket
import sys
from protoHelpers import encode_varint
from protobuf import hunter_pb2 as hunterxhunter
from protobuf import CharacterContainer_pb2 as character_container

def make_hunter():
    hunter = hunterxhunter.HunterxHunter();
    hunter.name = "Gon freecss"
    hunter.id = 23
    hunter.email = "gon.freecss@gmail.hunter.com"
    hunter = hunter.SerializeToString()

    character = character_container.CharacterContainer()
    character.character_type = "HunterxHunter"
    character.character_data = hunter
    character = character.SerializeToString()

    return character

def tcp_client_send(host, port, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, port))
        size = encode_varint(len(data))
        sock.sendall(size + data)
    finally:
        sock.close()


tcp_client_send("localhost", 40001, make_hunter())