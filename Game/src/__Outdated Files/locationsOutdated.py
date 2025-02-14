import json

with open('locations.json', 'r') as LOC:
    Locations = json.load(LOC)

with open("currentDescription.json", 'r') as DESC:
    Description = json.load(DESC)

currentLocation = '0'

Map = {
    Locations["0"]: (Locations["4"], Locations["19"]),
    Locations["1"]: (Locations["12"],),
    Locations["2"]: (Locations["3"], Locations["12"]),
    Locations["3"]: (Locations["13"], Locations["2"], Locations["16"], Locations["4"]),
    Locations["4"]: (Locations["5"], Locations["3"], Locations["0"]),
    Locations["5"]: (Locations["4"], Locations["6"]),
    Locations["6"]: (Locations["5"], Locations["19"]),
    Locations["7"]: (Locations["11"], Locations["10"], Locations["18"]),
    Locations["8"]: (Locations["9"], Locations["11"]),
    Locations["9"]: (Locations["8"],),
    Locations["10"]: (Locations["7"], Locations["13"]),
    Locations["11"]: (Locations["8"], Locations["7"]),
    Locations["12"]: (Locations["2"], Locations["1"]),
    Locations["13"]: (Locations["10"], Locations["3"]),
    Locations["14"]: (Locations["19"], Locations["15"]),
    Locations["15"]: (Locations["14"], Locations["16"]),
    Locations["16"]: (Locations["3"], Locations["15"]),
    Locations["17"]: (Locations["18"], Locations["19"]),
    Locations["18"]: (Locations["7"], Locations["17"]),
    Locations["19"]: (Locations["6"], Locations["14"], Locations["17"])
}

while True:
    print("\nYou are at: ", Locations[currentLocation])
    
    for i in range(len(Map[Locations[currentLocation]])):
        print(i, 'for', Map[Locations[currentLocation]][i])

    ch = int(input("-"))
    
    if(ch>len(Map[Locations[currentLocation]])-1):
        continue
    
    currentLocation = str(ch)
