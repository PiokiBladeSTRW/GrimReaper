Locations = {
            0: "TownHall",
            1: "Forgotten Cemetery", 
            2:  "Shade Bridge",         
            3:  "Grim Gate",                
            4:  "Forsaken Mansion",
            5:  "The Lost Stories",
            6:  "Cursed Hollow",
            7:  "Forsaken Bay",
            8:  "The Cursed Lighthouse",
            9:  "Shadow Forest",
            10: "Creep Wood",
            11: "Lake",
            12: "En Hill",            
            13: "<A>",
            14: "<B>",
            15: "<C>",
            16: "<D>",
            17: "<E>",
            18: "<F>" ,
            19: "<G>"
                 }

currentLocation =Locations[0]

Map = {
    Locations[0] : ( Locations[4], Locations[19] ),
    Locations[1] : ( Locations[12], ),
    Locations[2] : ( Locations[3], Locations[12] ),
    Locations[3] : ( Locations[13], Locations[2], Locations[16], Locations[4] ),
    Locations[4] : ( Locations[5], Locations[3], Locations[0] ),
    Locations[5] : ( Locations[4], Locations[6] ),
    Locations[6] : ( Locations[5], Locations[19] ),
    Locations[7] : ( Locations[11], Locations[10], Locations[18] ),
    Locations[8] : ( Locations[9], Locations[11] ),
    Locations[9] : ( Locations[8], ),
    Locations[10]: ( Locations[7], Locations[13] ),
    Locations[11]: ( Locations[8], Locations[7] ),
    Locations[12]: ( Locations[2], Locations[1]),
    Locations[13]: ( Locations[10], Locations[3] ),
    Locations[14]: ( Locations[19], Locations[15] ),
    Locations[15]: ( Locations[14], Locations[16] ),
    Locations[16]: ( Locations[3], Locations[15] ),
    Locations[17]: ( Locations[18], Locations[19] ),
    Locations[18]: ( Locations[7], Locations[17] ),
    Locations[19]: ( Locations[6], Locations[14], Locations[17] )
    }

while True:
    print("\nYou are at: ", currentLocation)
    for i in range(len(Map[currentLocation])):
        print(i, 'for', Map[currentLocation][i])

    ch = int(input("-"))
    
    if(ch>len(Map[currentLocation])-1):
        continue
    
    currentLocation = Map[currentLocation][ch]
