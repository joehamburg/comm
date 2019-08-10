from enums import *
from protobuf import CharacterContainer_pb2 as c_con, hunter_pb2 as h
from . import ProtoCreator

def make_hunter():
    hunter = h.HunterxHunter();
    hunter.name = "Gon freecss"
    hunter.id = 23
    hunter.email = "gon.freecss@gmail.hunter.com"

    return hunter


class Character(ProtoCreator):
    def __init__(self, type):
        self.type = type
        if self.type == CharacterType.HUNTER:
            self.character_data = make_hunter()

    def serialize(self):
        self.character_data = self.character_data.SerializeToString()

        character = c_con.CharacterContainer()
        character.type = self.type.name
        character.data = self.character_data
        serialized_character = character.SerializeToString()

        return serialized_character


class CharacterType(Enum):
    HUNTER = 1
    PIRATE = 2
    NINJA = 3
    HERO = 4