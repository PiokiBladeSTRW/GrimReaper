

import tkinter as tk
import json
import os
import random

loc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '../Travelling/locations.json')
evnt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Travelling/currentEventDesc.json')
map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Travelling/map.json')

with open(loc_path, 'r') as LOC:
    Locations = json.load(LOC)

with open(evnt_path, 'r') as EVNT:
    EventsDesc = json.load(EVNT)

with open(map_path, 'r') as MAP:
    Map = json.load(MAP)


def Travelled(index, event=None):
    global cl, currentOptions, currentEventStr

    for i in range(len(Map[cl])):
        root.unbind(str(i))
    
    cl = Map[cl][index]
    currentOptions = ''
    for i in range(len(Map[cl])):
        currentOptions+= str(i) +' for ' + Locations[Map[cl][i]] +'\n'

    eventIndex = str(random.randint(0, len(EventsDesc[cl])-1))

    currentEventStr = f''' You are at the {Locations[cl]}\n''' + EventsDesc[cl][eventIndex] + '\n\n' + currentOptions
    
    

def updateText():
    currentEventLab.config(text=currentEventStr)
    
    for i in range(len(Map[cl])):
        root.bind(str(i), lambda travel, val=i: Travelled(val))        

    root.after(100, updateText)



#Main Window
# root = tk.Tk()
# root.state('zoomed')
# root.config(bg='black')


cl='0'


currentEventStr = ''' You are at the Town Hall.
The walls look eroded and broken and there is a weird smell in the air.
The door looks half jammed, and the garden is dead'''

currentEventLab = tk.Label(root,
                            text=currentEventStr,                            
                            justify= 'left',
                            bg='black',
                            fg='white',
                            font= ("StraightToHell Sinner BB", 20))
currentEventLab.pack(side= 'top', pady=50, anchor= 'w')


updateText()


#root.mainloop()