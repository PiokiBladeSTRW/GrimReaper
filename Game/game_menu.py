#Game Screen

import tkinter as tk
import tkinter.font as tkFont

#Main Window
root = tk.Tk()
root.title("GAME")
root.state("zoomed")
root.config(bg = 'black')

#Help
def Help():
    import Options.Options as Options
    Options.Help(root)


#MenuBar
menuBar = tk.Menu(root)
root.config(menu = menuBar)

optionsMenu = tk.Menu(menuBar, tearoff=0)
optionsMenu.add_command(label= "Help", command=Help)
optionsMenu.add_command(label= "Documentation")
optionsMenu.add_separator()
optionsMenu.add_command(label= "Accounts")


menuBar.add_cascade(label='Options', menu=optionsMenu)



#CurrentEvent Description
currentEvent = ''' You are at the Town Hall.
 The walls look eroded and broken and there is a weird smell in the air.
 The door looks half jammed, and the garden is dead'''

currentEventDesc = tk.Label(root,
                            text=currentEvent,                            
                            justify= 'left',
                            bg='black',
                            fg='white',
                            font= ("StraightToHell Sinner BB", 25))
currentEventDesc.pack(side= 'top', pady=50, anchor= 'w')


mapVisual = tk.Frame(root, bg='black', width=400, height=350)
mapVisual.pack(side='bottom', pady=60)

###Map Design
canvas = tk.Canvas(mapVisual,
                   width=555,
                   height=400,
                   bg='black',
                   highlightthickness=1,
                   highlightbackground='yellow')
canvas.pack()
from Graphics.mapVisuals import draw_map
draw_map(canvas, x1=0, y1=0, x2=600, y2=450, lineColor= 'white')

root.mainloop()
