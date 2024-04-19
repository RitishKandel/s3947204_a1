

import json

config : dict = {}


for i in range(20):
    config = {}
    config["dataStructure"] = "adjlist"
    config["rowNum"] = 10
    config["colNum"] = 10
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,10],[10,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))

for i in range(20, 40):
    config = {}
    config["dataStructure"] = "adjlist"
    config["rowNum"] = 50
    config["colNum"] = 50
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,50],[50,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))


for i in range(40, 60):
    config = {}
    config["dataStructure"] = "adjlist"
    config["rowNum"] = 100
    config["colNum"] = 100
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,100],[100,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))


for i in range(60, 80):
    config = {}
    config["dataStructure"] = "adjmat"
    config["rowNum"] = 10
    config["colNum"] = 10
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,10],[10,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))


for i in range(80, 100):
    config = {}
    config["dataStructure"] = "adjmat"
    config["rowNum"] = 50
    config["colNum"] = 50
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,50],[50,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))

for i in range(100, 120):
    config = {}
    config["dataStructure"] = "adjmat"
    config["rowNum"] = 100
    config["colNum"] = 100
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,100],[100,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))


for i in range(120, 140):
    config = {}
    config["dataStructure"] = "array"
    config["rowNum"] = 10
    config["colNum"] = 10
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,10],[10,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))


for i in range(140, 160):
    config = {}
    config["dataStructure"] = "array"
    config["rowNum"] = 50
    config["colNum"] = 50
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,50],[50,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))


for i in range(160, 180):
    config = {}
    config["dataStructure"] = "array"
    config["rowNum"] = 100
    config["colNum"] = 100
    config["entrances"] = [[0,-1],[-1,1]]
    config["exits"] = [[3,100],[100,4]]
    config["generator"] = "recur"
    config["visualise"] = False

    with open("../sampleConfig" + str(i) + ".json", 'w') as f:
        f.write(json.dumps(config))
