import glob, json


fileList = glob.glob('result/'+"*.json")

r = []
for fileName in fileList:
    with open(fileName) as f:
        jo = json.loads(f.read())
        print(jo['contents'])
        r += jo['contents']

with open(f'{"r"}.json', 'w+') as f:
    f.write(json.dumps(r))
