import socket
import SocketServer
from protoHelpers import decode_varint
from protobuf import hunter_pb2 as hunterxhunter 
from protobuf import CharacterContainer_pb2 as character_container


class tcp(SocketServer.BaseRequestHandler):
    def deserialize_data(self, data):
        character = character_container.CharacterContainer()
        character.ParseFromString(data)

        hunter = hunterxhunter.HunterxHunter()
        hunter.ParseFromString(character.character_data)

        return hunter

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
        character = self.deserialize_data(data)
        print(character)


def run_server(host, port, type):
    if type == tcp: 
        server = SocketServer.TCPServer((host, port), type)
        server.serve_forever()
    else:
        "-_(-_-)_-"

run_server('localhost', 40001, tcp)
        



        