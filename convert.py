import json
import sys

with open (sys.argv[1] + "mission.sqm", "r") as myfile:
    mission=myfile.read()
f = open(sys.argv[1] + "mission-backup.sqm", "w")
f.write(mission)

with open(sys.argv[2]) as json_file:
    conversionData = json.load(json_file)

for word, initial in conversionData.items():
    mission = mission.replace(word, initial)

f = open("mission.sqm", "w")
f.write(mission)
f.close()