class TextManager:
    import json
    import os
    import random
    import tkinter as tk

    loc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '../Travelling/locations.json')
    evnt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Travelling/currentEventDesc.json')
    map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Travelling/map.json')

    with open(loc_path, 'r') as LOC:
        Locations = json.load(LOC)

    with open(evnt_path, 'r') as EVNT:
        EventsDesc = json.load(EVNT)

    with open(map_path, 'r') as MAP:
        Map = json.load(MAP)
    
    del loc_path, evnt_path, map_path


    def __init__(self, root):            
        self.currentEventStr = ''' You are at the Town Hall.
 The walls look eroded and broken and there is a weird smell in the air.
 The door looks half jammed, and the garden is dead
 0 for Forsaken Mansion
 1 for <G>'''
        self.window = root
        self.currentLocation='0'
        self.currentEventLab = self.tk.Label(self.window,
                            text= self.currentEventStr,                            
                            justify= 'left',
                            bg='black',
                            fg='white',
                            font= ("StraightToHell Sinner BB", 20))
        self.currentEventLab.pack(side= 'top', pady=50, anchor= 'w')

        self.playerTravelled = True #Later to be made a Player Variable

    def currentEventUpdate(self):
        self.currentEventLab.config(text=self.currentEventStr)

        for i in range(len(self.Map[self.currentLocation])):
            self.window.bind(str(i), lambda event, val=i: self.Travelled(choice=val))        

    def Travelled(self, choice: int,):
        for i in range(len(self.Map[self.currentLocation])):
            self.window.unbind(str(i))
        
        self.currentLocation = self.Map[self.currentLocation][choice]

        currentOptions = ''
        for i in range(len(self.Map[self.currentLocation])):
            currentOptions+= str(i) +' for ' + self.Locations[self.Map[self.currentLocation][i]] +'\n '

        eventIndex = str(self.random.randint(0, len(self.EventsDesc[self.currentLocation])-1))

        self.currentEventStr = f''' You are at the {self.Locations[self.currentLocation]}\n ''' + self.EventsDesc[self.currentLocation][eventIndex] + '\n\n ' + currentOptions 

        self.playerTravelled = True


# import tkinter as tk
# #Main Window
# root = tk.Tk()
# root.state('zoomed')
# root.config(bg='black')

# text = TextManager(root)
# def update():
#     text.currentEventUpdate()
#     root.after(1000, update)

# update()

# root.mainloop()