#Location Demo

import json

with open('locations.json', 'r') as LOC:
    Locations = json.load(LOC)

with open('currentDescription.json', 'r') as DESC:
    Descriptions = json.load(DESC)
    
def valueToKey(Dic, Value):
    return ''.join([ID for ID in Dic.keys() if Dic[ID] == Value])

Map = {
    '0' : ( Locations["1"], Locations["15"]),
    '1' : ( Locations["0"], Locations["6"], Locations["2"]),
    '2' : ( Locations["1"], Locations["7"], Locations["3"], Locations["19"]),
    '3' : ( Locations["2"], Locations["4"]),
    '4' : ( Locations["3"], Locations["5"]),
    '5' : ( Locations["4"] ,),
    '6' : ( Locations["16"], Locations["1"]),
    '7' : ( Locations["8"], Locations["2"]),
    '8' : ( Locations["9"], Locations["7"]),
    '9' : ( Locations["13"], Locations["10"], Locations["8"]),
    '10': ( Locations["11"], Locations["9"]),
    '11': ( Locations["12"], Locations["10"]),
    '12': ( Locations["11"],),
    '13': ( Locations["9"], Locations["14"]),
    '14': ( Locations["13"], Locations["15"]),
    '15': ( Locations["14"], Locations["16"], Locations["0"], Locations["17"]),
    '16': ( Locations["6"], Locations["15"]),
    '17': ( Locations["15"], Locations["18"]),
    '18': ( Locations["17"], Locations["19"]),
    '19': ( Locations["18"], Locations["2"])
    }

cl = '0'

while True:
    print("\nYou are At:", Locations[cl])
    print("Described As:", Descriptions[cl]['description'])
    for i in range(len(Map[cl])):
        print(i, 'for', Map[cl][i])              
    
    destination = Map[cl][int(input('-'))]
    
    cl = valueToKey(Locations, destination)
    
    
