import json

ids = 0
while True:
    with open("fish.json") as f:
        ids+=1
        data = json.load(f)
        print(data["name"+str(ids)])