#worldMenu
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from clientVal.variables import uuid, usrname
import os
import json

#Main_Window
mainMenuW = tk.Tk()
mainMenuW.title("Main Menu")
mainMenuW.state('zoomed')
mainMenuW.config(bg='black')

#Main Receivable Variable
import clientVal.variables as var

#Current Worlds
worldsDir = 'worlds'
currentWorlds = [w for w in os.listdir(worldsDir)]

def create_world():
    worldName= Entry1.get()

    if(not os.path.exists(f'worlds/{worldName}')):        
        os.makedirs(f'worlds/{worldName}')

        wD ={
             "worldName": worldName, 
             "difficulty": difficulty.get(), 
             "multiplayer": multiplayer.get(), 
             "players": { 
                 uuid: {
                     "usrname": usrname,
                     "location": '0'             
                    }
                }
            }


        with open(f'worlds/{worldName}/worldData.json', 'w') as worldData:              
            json.dump(wD, worldData, indent=4)

        var.selectedWorld = worldName
        mainMenuW.destroy()

    else:
        messagebox.showerror(title="Invalid Name", message="NAME ALREADY TAKEN")
        

def select_world(world):    
    var.selectedWorld = world
    mainMenuW.destroy()

#----------------------------


#Display for Selecting Pre Existing World
worldListCanvas = tk.Canvas(mainMenuW, bg='black', width=800, highlightthickness=0)
worldListCanvas.pack(side = tk.LEFT, fill=tk.Y)
scrollbar = tk.Scrollbar(mainMenuW, orient=tk.VERTICAL, command=worldListCanvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

worldListCanvas.configure(yscrollcommand=scrollbar.set)
worldListCanvas.bind('<Configure>', lambda e: worldListCanvas.configure(scrollregion=worldListCanvas.bbox("all")))

worldList = tk.Frame(worldListCanvas, bg='black')
window = worldListCanvas.create_window((0,0), window = worldList, anchor = 'n')

#Display for Creating New World
Label1 = tk.Label(mainMenuW, text="World Name: ", font='Calibri 16', bg='black', fg='white')
Label1.pack(side='top', pady=20)
Entry1 = tk.Entry(mainMenuW, width=50, font='Calibri 16')
Entry1.pack()

Label2 = tk.Label(mainMenuW, text="Difficulty: ", font='Calibri 16', bg='black', fg='white')
Label2.pack(side='top', pady=40)
difficulty = tk.StringVar()
Combo1= ttk.Combobox(mainMenuW, 
                     textvariable=difficulty, 
                     values=["Easy", "Medium", "Hard", "2020"], 
                     state='readonly')
Combo1.pack()

multiplayer = tk.IntVar()
Checkbox = tk.Checkbutton(mainMenuW,text="Multiplayer?", font='Calibri 16', variable=multiplayer, bg='gray')
Checkbox.pack(pady=50)

createButton = tk.Button(mainMenuW, text="CREATE WORLD", font='Calibri 21', command = create_world)
createButton.pack(pady=200)

#Worlds List with List
for world in currentWorlds:
    tk.Button(worldList,
              text=world, 
              font=("Arial", 30), 
              bg='black', 
              fg='white',
              command= lambda wrl = world: select_world(wrl)).pack(pady=5, padx=300  )

mainMenuW.mainloop()