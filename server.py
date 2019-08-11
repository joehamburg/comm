import socket
import SocketServer
from protoHelpers import decode_varint, import_mod

# add new protobuf constuctors here
proto_constructors = {
    'CHARACTER': { 
        'class': 'CharacterContainer',
        'package': 'CharacterContainer_pb2', 
        'types': {
            'HUNTER': {
                'class':  'HunterxHunter', 
                'package': 'hunter_pb2', 
            }
        }
    }
}

class tcp(SocketServer.BaseRequestHandler):

    def deserialize(self, data, protoContainerType):
        proto_dict = proto_constructors[protoContainerType]
        proto_con =  import_mod('protobuf', proto_dict['package'], proto_dict['class'])()
        if( proto_con.ParseFromString(data) ):
            proto = import_mod('protobuf', proto_dict['types'][proto_con.type]['package'], proto_dict['types'][proto_con.type]['class'])()
            proto.ParseFromString(proto_con.data)
        else: 
            print("monkaS i dont know what this proto container is")

        return  proto

    def handle(self):
        data = b''
        while True:
            try:
                data += self.request.recv(1)
                size = decode_varint(data)
                break
            except IndexError:
                pass
        data = self.request.recv(size)
        character = self.deserialize(data, 'CHARACTER')
        print(character)


def run_server(host, port, type):
    if type == tcp: 
        server = SocketServer.TCPServer((host, port), type)
        server.serve_forever()
    else:
        "-_(-_-)_-"

run_server('localhost', 40001, tcp)