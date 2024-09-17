Locations = ['A', 'B', 'C', 'D', 'E']

cl =Locations[1]

Map = {
    Locations[0] : [ Locations[1], Locations[2], Locations[3], Locations[4]],
    Locations[1] : [ Locations[0] ],
    Locations[2] : [ Locations[0] ],
    Locations[3] : [ Locations[0] ],
    Locations[4] : [ Locations[0] ]
    }

while True:
    print("You are at: ", cl)
    for i in range(len(Map[cl])):
        print(i, 'for', Map[cl][i])

    ch = int(input("-"))
    
    if(ch>len(Map[cl])-1):
        continue
    
    cl = Map[cl][ch]
