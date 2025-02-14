#Game Screen

import tkinter as tk
import json
import os
from texts.baseText import TextManager
from graphics.mapVisuals import Map
from menuBar.optionsDisplays import Options

from clientVal.variables import uuid, selectedWorld

#Delocalize usrcolor to a seperate value later on
#Currently done this way cuz there's only one Player Variable 
from auth.logIn import ViewAcc

#Main Window
root = tk.Tk()
root.title("GAME")
root.state("zoomed")
root.config(bg = 'black')
root.minsize(1400,800)


#Frames to Organize the Display
textFrame = tk.Frame(root, width=600, height=450, bg='black')
choiceFrame = tk.Frame(root, width=600, height=450, bg='black')
chatFrame = tk.Frame(root, width=600, height=450, bg='black')
mapFrame= tk.Frame(root, width=600, height=450, bg='black')

textFrame.grid(row=0, column=0, sticky="nsew")
choiceFrame.grid(row=1, column=0, sticky="nsew")
chatFrame.grid(row=0, column=1, sticky="nsew")
mapFrame.grid(row=1, column=1, sticky='ew')

textFrame.grid_propagate(False)
choiceFrame.grid_propagate(False)
chatFrame.grid_propagate(False)
mapFrame.grid_propagate(False)

root.grid_rowconfigure(0, weight=1, minsize=450)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

#Obtaining World Info
worldDataPath = os.path.join(os.path.dirname(os.path.abspath(__file__)) , f'../worlds/{selectedWorld}/worldData.json')

with open(worldDataPath, 'r') as worldDataF:   
    worldData = json.load(worldDataF)

currentLocation = worldData['players'][uuid]['location']

#Save World Data
def save():
    worldData['players'][uuid]['location'] = eventText.currentLocation
    with open(worldDataPath, 'w') as worldDataF:
        json.dump(worldData, worldDataF, indent=4)
    root.destroy()
        

#Current Event Description & Current Map
eventText = TextManager(root, textFrame, choiceFrame, currentLocation)

mapCanvas = tk.Canvas(mapFrame,
                   width=600,
                   height=300,
                   bg='black',
                   highlightthickness=1,
                   highlightbackground='yellow'
                   )
mapCanvas.pack(side='bottom', anchor='se')
townMap = Map(mapCanvas, x1=0, y1=-25, x2=600, y2=360)
townMap.drawMap()


#Update Data Constantly
def updateWidgets():        
    if(eventText.playerTravelled):
        #currentEventLabel Update
        eventText.currentEventUpdate()
    
        #VisualMap Update [Player Markers]            
        townMap.playerMarker(eventText.currentLocation, ViewAcc()[uuid]['usrcolor'])

        #Update Travel Value
        eventText.playerTravelled = False

    #Reschedule    
    root.after(500, updateWidgets)

updateWidgets()


#MenuBar
menuBar = tk.Menu(root)
root.config(menu = menuBar)

#Create the Frame
optionsFrames = Options(root)

optionsMenu = tk.Menu(menuBar, tearoff=0)
optionsMenu.add_command(label= "Help", command= lambda: optionsFrames.Help())
optionsMenu.add_command(label= "Documentation", command= lambda: optionsFrames.Documentation())
optionsMenu.add_separator()
optionsMenu.add_command(label= "Accounts", command= lambda: optionsFrames.Accounts(uuid))

menuBar.add_cascade(label='Options', menu=optionsMenu)

root.protocol("WM_DELETE_WINDOW", save)

root.mainloop()