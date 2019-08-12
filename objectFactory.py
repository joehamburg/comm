from enums import Container
from creators import CharacterCreator

def factory(data, container_type = Container.UNKNOWN, proto_type = Container.UNKNOWN):
    if container_type == Container.CHARACTER : return CharacterCreator(proto_type, data)
    assert 0, "Bad ProtoCreator creation: " + container_type.name
