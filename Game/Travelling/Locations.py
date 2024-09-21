#Location Demo

import json

with open('locations.json', 'r') as LOC:
    Locations = json.load(LOC)

Map = {
    Locations["0"] : ( Locations["1"], Locations["15"]),
    Locations["1"] : ( Locations["0"], Locations["6"], Locations["2"]),
    Locations["2"] : ( Locations["1"], Locations["7"], Locations["3"], Locations["19"]),
    Locations["3"] : ( Locations["2"], Locations["4"]),
    Locations["4"] : ( Locations["3"], Locations["5"]),
    Locations["5"] : ( Locations["4"] ,),
    Locations["6"] : ( Locations["16"], Locations["1"]),
    Locations["7"] : ( Locations["8"], Locations["2"]),
    Locations["8"] : ( Locations["9"], Locations["8"]),
    Locations["9"] : ( Locations["13"], Locations["10"], Locations["8"]),
    Locations["10"]: ( Locations["11"], Locations["9"]),
    Locations["11"]: ( Locations["12"], Locations["10"]),
    Locations["12"]: ( Locations["11"],),
    Locations["13"]: ( Locations["9"], Locations["14"]),
    Locations["14"]: ( Locations["13"], Locations["15"]),
    Locations["15"]: ( Locations["14"], Locations["16"], Locations["17"]),
    Locations["16"]: ( Locations["6"], Locations["15"]),
    Locations["17"]: (Locations["15"], Locations["18"]),
    Locations["18"]: (Locations["17"], Locations["19"]),
    Locations["19"]: (Locations["18"], Locations["2"])
    }

cl = '0'

while True:
    print("\nYou are At:", Locations[cl])
    for i in range(len(Map[Locations[cl]])):
        print(i, "for", Map[Locations[cl]][i])

    ch= int(input('-'))
    
    
    cl = ''.join([x for x in Locations.keys() if Locations[x] == Map[Locations[cl]][ch]])
    
    
