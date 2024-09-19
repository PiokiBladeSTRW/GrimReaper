#Game Screen

import tkinter as tk

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
currentEvent = ''' You are at the Town Hall.
The walls look eroded and broken and there is a weird smell in the air.
The door looks half jammed, and the garden is dead'''

currentEventDesc = tk.Label(root, text=currentEvent, bg='black', fg='white', font= 'Calibri 21')
currentEventDesc.pack(side= 'top', pady=50)


mapVisual = tk.Frame(root, bg='white', width=850, height=300)
mapVisual.pack(side='bottom', pady=75)

root.mainloop()
