import socket
import SocketServer
import json
from enums import Container
from helpers import decode_varint, import_mod


class tcp(SocketServer.BaseRequestHandler):
    def deserialize(self, data):
        #parse json with all the constructors for that container type
        with open('config/' + self.server.protoContainerType.name + '.json', 'r') as conf_file:
            json_file=conf_file.read()
        proto_dict = json.loads(json_file)

        #use json values to dnyamically import & make some proto objects
        proto_con =  import_mod('protobuf', proto_dict['package'], 
                                proto_dict['class'])()
        if( proto_con.ParseFromString(data) ):
            proto = import_mod('protobuf', proto_dict['types'][proto_con.type]['package'], 
                                proto_dict['types'][proto_con.type]['class'])()
            proto.ParseFromString(proto_con.data)
        else: 
            print("monkaS i dont know what this proto container is")

        return  proto

    def handle(self):
        while True:
            try:
                data = self.request.recv(1)
                size = decode_varint(data)
                break
            except IndexError:
                pass
        data = self.request.recv(size)
        character = self.deserialize(data)
        print(character)


def run_server(host, port, serverType, containerType):
    if serverType == tcp: 
        server = SocketServer.TCPServer((host, port), serverType)
        server.protoContainerType = containerType
        server.serve_forever()
    else:
        "-_(-_-)_-"

run_server('localhost', 40001, tcp, Container.CHARACTER)