#Game Screen

import tkinter as tk
import tkinter.font as tkFont

#Main Window
root = tk.Tk()
root.title("GAME")
root.state("zoomed")
root.config(bg = 'black')


#MenuBar
menuBar = tk.Menu(root)
root.config(menu = menuBar)

optionsMenu = tk.Menu(menuBar, tearoff=0)
optionsMenu.add_command(label= "Help")
optionsMenu.add_command(label= "Documentation")
optionsMenu.add_separator()
optionsMenu.add_command(label= "Accounts")


menuBar.add_cascade(label='Options', menu=optionsMenu)

#CurrentEvent Description
currentEvent = '''You are at the Town Hall.
The walls look eroded and broken and there is a weird smell in the air.
The door looks half jammed, and the garden is dead'''

currentEventDesc = tk.Label(root,
                            text=currentEvent,                            
                            justify= 'left',
                            bg='black',
                            fg='white',
                            font= ("StraightToHell Sinner BB", 21))
currentEventDesc.pack(side= 'top', pady=50, anchor= 'w')


mapVisual = tk.Frame(root, bg='white', width=500, height=400)
mapVisual.pack(side='bottom', pady=60)

###Map Design
canvas = tk.Canvas(mapVisual, width=500, height=400, bg='gray')
canvas.pack(anchor='w')
from mapp import draw_map
draw_map(canvas)

root.mainloop()
