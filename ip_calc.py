adress = "192.168.0.1"
bit_adress = ".".join([bin(int(_))[2:].zfill(8) for _ in adress.split('.')])
netmask = 24

print(f"IP Address: {bit_adress}")
bitmask = (".".join(["1" * (min(8, netmask - n)) + "0" * (n + 8 - netmask) for n in range(0, 32, 8)]))
print(f"netmask     {bitmask}")
print(f"Wildcard:   {".".join(["".join(["1" if x == "0" else "0" for x in n]) for n in bitmask.split(".")])}")
print()

root_adress = bit_adress[:26]+"."+"0"*8
print(f"Network:  {".".join([str(int(x, 2)) for x in root_adress.split(".")])}      {root_adress}")
broadcast_adress = bit_adress[:26]+"."+"1"*8
print(f"Broadcast:{".".join([str(int(x, 2)) for x in broadcast_adress.split(".")])}     {broadcast_adress}")
min_adress = bit_adress[:26]+"."+"0"*7+"1"
print(f"Host min: {".".join([str(int(x, 2)) for x in min_adress.split(".")])}       {min_adress}")
max_adress = bit_adress[:26]+"."+"1"*7+"0"
print(f"Host max: {".".join([str(int(x, 2)) for x in max_adress.split(".")])}       {max_adress}")
print(f"Host/Net: {2**8-2}")