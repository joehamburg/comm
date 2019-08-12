import enums
from protobuf import CharacterContainer_pb2 as c_con
from protoCreator import ProtoCreator


class CharacterCreator(ProtoCreator):
    def serialize(self):
        self.data = self.data.SerializeToString()

        character = c_con.CharacterContainer()
        character.type = self.type.name
        character.data = self.data

        serialized_character = character.SerializeToString()

        return serialized_character