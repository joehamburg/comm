from enums import *
from protobuf import CharacterContainer_pb2 as c_con, hunter_pb2 as h

class ProtoCreator:
    def __init__(self, type, data):
        self.type = type
        self.data = data
    
    def serialize(self):
        raise ValueError('Need to implement ProtoCreator.serialize method.')
        pass

    @staticmethod
    def factory(data, container_type = Container.UNKNOWN, proto_type = Container.UNKNOWN):
        if container_type == Container.CHARACTER : return Character(proto_type, data)
        assert 0, "Bad ProtoCreator creation: " + container_type.name


class Character(ProtoCreator):
    def serialize(self):
        self.data = self.data.SerializeToString()

        character = c_con.CharacterContainer()
        character.type = self.type.name
        character.data = self.data
        serialized_character = character.SerializeToString()

        return serialized_character