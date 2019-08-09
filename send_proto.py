from protobuf import hunter_pb2 as hunter 

gon = hunter.Hunterxhunter();
gon.name = "Gon freecss"
gon.id = 23
gon.email = "gon.freecss@gmail.hunter.com"

gon.SerializeToString(gon)
print(gon)


