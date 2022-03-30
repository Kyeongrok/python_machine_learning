import glob, json

with open(f'{"r"}.json') as f:
    jo = json.loads(f.read())

print(len(jo))
