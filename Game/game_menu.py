#Game Screen

import tkinter as tk
from Texts.baseText import TextManager
from Graphics.mapVisuals import Map
from MenuBar.optionsDisplays import Options
import MenuBar.optionsControls as optionControls

#Main Window
root = tk.Tk()
root.title("GAME")
root.state("zoomed")
root.config(bg = 'black')


#Current Event Description & Current Map
eventText = TextManager(root)

mapCanvas = tk.Canvas(root,
                   width=550,
                   height=300,
                   bg='black',
                   highlightthickness=1,
                   highlightbackground='yellow')
mapCanvas.pack(side='bottom', pady=40)


townMap = Map(mapCanvas, x1=0, y1=-25, x2=600, y2=360)
townMap.drawMap()

#Update Data Constantly
def updateWidgets():        
    if(eventText.playerTravelled):
        #currentEventLabel Update
        eventText.currentEventUpdate()
    
        #VisualMap Update [Player Markers]    
        townMap.playerMarker(eventText.currentLocation)

        #Update Travel Value
        eventText.playerTravelled = False

    #Reschedule    
    root.after(500, updateWidgets)

updateWidgets()



#MenuBar
menuBar = tk.Menu(root)
root.config(menu = menuBar)

optionsMenu = tk.Menu(menuBar, tearoff=0)
optionsMenu.add_command(label= "Help", command= lambda: optionControls.Help(optionsFrames))
optionsMenu.add_command(label= "Documentation", command= lambda: optionControls.Documentation(optionsFrames))
optionsMenu.add_separator()
optionsMenu.add_command(label= "Accounts", command= lambda: optionControls.Account(optionsFrames))

menuBar.add_cascade(label='Options', menu=optionsMenu)

#Create the Frame
optionsFrames = Options(root)

root.mainloop()