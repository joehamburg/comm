from enums import Container
from client import tcp_client_send
from objectFactory import factory
from protobuf import hunter_pb2 as h, ninja_pb2 as n, pirate_pb2 as p

#make a sample hunter for testing
def make_hunter():
    hunter = h.HunterxHunter()
    hunter.name = "Gon Freecss"
    hunter.nen = "Enhancer"
    hunter.hunter_license = True

    return hunter

def make_ninja():
    ninja = n.Naruto()
    ninja.name = "Naruto Uzumaki"
    ninja.move = "Shadow clone jutsu"
    ninja.village = "hidden leaf"

    return ninja

def make_pirate():
    pirate = p.OnePiece()
    pirate.name = "Monkey D Luffy"
    pirate.position = "Captain"
    pirate.gumgumfruit = True

    return pirate

hunter = factory(make_hunter(), Container.CHARACTER, Container.CHARACTER.value.HUNTER)
ninja = factory(make_ninja(), Container.CHARACTER, Container.CHARACTER.value.NINJA)
pirate = factory(make_pirate(), Container.CHARACTER, Container.CHARACTER.value.PIRATE)

characters = [hunter, ninja, pirate]

for character in characters: 
    tcp_client_send("localhost", 40001, character)
