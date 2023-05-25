def read():
  with open("flatlist.txt", "r") as f:
    lines = f.readlines()

  return [line.strip().split(":") for line in lines]


packs = dict()

for line in read():
    key = line[0] + ":" + line[1]
    if key in packs:
        version = packs[key]
        if len(line[2]) < len(version):
            packs[key] = line[2]
    else:
        packs[key] = line[2]

for k, v in packs.items():
   print (k + ":" + v)
