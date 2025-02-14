class TextManager:
    import json
    import os
    import random
    import tkinter as tk

    loc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '../../assets/Values/locations.json')
    evnt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../assets/Values/currentEventDesc.json')
    con_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../assets/Values/connectors.json')

    with open(loc_path, 'r') as LOC:
        Locations = json.load(LOC)

    with open(evnt_path, 'r') as EVNT:
        EventsDesc = json.load(EVNT)

    with open(con_path, 'r') as MAP:
        Connectors = json.load(MAP)
    
    del loc_path, evnt_path, con_path


    def __init__(self, root, textFrame, choiceFrame, currentLocation):   

        self.currentEventStr = ''' You are at the Town Hall.
 The walls look eroded and broken and there is a weird smell in the air.
 The door looks half jammed, and the garden is dead'''
        
        self.currentChoiceStr = ''' 0 for Forsaken Mansion
 1 for <G>'''
        
        self.window = root
        self.textFr = textFrame
        self.choiceFr = choiceFrame
        self.currentLocation= currentLocation

        self.currentEventLab = self.tk.Label(self.textFr,
                            text= self.currentEventStr,                            
                            justify= 'left',
                            bg='black',
                            fg='white',
                            wraplength=700,
                            font= ("StraightToHell Sinner BB", 20))
        self.currentEventLab.grid(row= 0, column=0, pady=50, sticky= 'nw')

        self.currentChoiceLab = self.tk.Label(self.choiceFr,
                            text= self.currentChoiceStr,                            
                            justify= 'left',
                            bg='black',
                            fg='white',
                            font= ("StraightToHell Sinner BB", 20))
        self.currentChoiceLab.grid(row= 0, column=0, pady=50, sticky= 'nw')

        self.playerTravelled = True #Later to be made a Player Variable, maybe?
        if(self.currentLocation != '0'):
            self.Travel(self.currentLocation, False)

    def currentEventUpdate(self):
        self.currentEventLab.config(text=self.currentEventStr)
        self.currentChoiceLab.config(text=self.currentChoiceStr)

        for i in range(len(self.Connectors[self.currentLocation])):
            self.window.bind(str(i), lambda event, val=i: self.Travel(val, True))        

    def Travel(self, destination: int, bound):
        #Remove Binding of all Previous Options
        if bound:
            for i in range(len(self.Connectors[self.currentLocation])):
                self.window.unbind(str(i))
        
            self.currentLocation = self.Connectors[self.currentLocation][destination]
        else:
            self.currentLocation = destination
    

        currentOptions = ''
        for i in range(len(self.Connectors[self.currentLocation])):
            currentOptions+= str(i) +' for ' + self.Locations[self.Connectors[self.currentLocation][i]] +'\n '

        eventIndex = str(self.random.randint(0, len(self.EventsDesc[self.currentLocation])-1))

        self.currentEventStr = f''' You are at the {self.Locations[self.currentLocation]}\n ''' + self.EventsDesc[self.currentLocation][eventIndex] 
        self.currentChoiceStr = currentOptions 

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