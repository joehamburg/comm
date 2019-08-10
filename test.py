from enums import *
from client import tcp_client_send
from Creators.protoCreator import *

def make_hunter():
    hunter = h.HunterxHunter();
    hunter.name = "Gon Freecss"
    hunter.id = 23
    hunter.email = "gon.freecss@gmail.hunter.com"

    return hunter

hunter = ProtoCreator.factory(make_hunter(), Container.CHARACTER, Container.CHARACTER.value.HUNTER)
tcp_client_send("localhost", 40001, hunter)

