from enums import Container
from client import tcp_client_send
from Creators import CharacterCreator

from protobuf import CharacterContainer_pb2 as c_con, hunter_pb2 as h

def make_hunter():
    hunter = h.HunterxHunter()
    hunter.name = "Gon Freecss"
    hunter.id = 23
    hunter.email = "gon.freecss@gmail.hunter.com"

    return hunter

def factory(data, container_type = Container.UNKNOWN, proto_type = Container.UNKNOWN):
    if container_type == Container.CHARACTER : return CharacterCreator(proto_type, data)
    assert 0, "Bad ProtoCreator creation: " + container_type.name

hunter = factory(make_hunter(), Container.CHARACTER, Container.CHARACTER.value.HUNTER)
tcp_client_send("localhost", 40001, hunter)

