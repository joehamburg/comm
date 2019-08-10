from enums import *

class ProtoCreator:
    def __init__(self, type, data):
        self.type = type
        self.data = data
    
    def serialize(self):
        raise ValueError('Need to implement ProtoCreator.serialize method.')
        pass