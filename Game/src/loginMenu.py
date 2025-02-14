#LoginMenu
import tkinter as tk
import auth.logIn as Auth
from tkinter import messagebox

import clientVal.variables


def infoEntered(nameE, passE, event=None):   
    global usrname, uuid 
    usrname = nameE.get()
    usrpass = passE.get()
    uuid = Auth.LogIn(usrname,usrpass)
    if( uuid ):        
        import clientVal.variables as var
        var.usrname = usrname
        var.uuid = uuid        
        loginMenuW.destroy()
    else:  
        messagebox.showwarning(title='!!', message='Invalid Username or Password')

   
def play_pressed():
    global playPressed, usrnameEntry, usrpassEntry
    
    if( not playPressed ):
        #UserEntry Widgets
        usrnameLabel = tk.Label(play_Frame, text="Enter Username", bg= 'black', fg='white', font= 'Calibri 16')
        usrnameEntry = tk.Entry(play_Frame, width = 25, font='Calibri 21')
        usrpassLabel = tk.Label(play_Frame, text="Enter Password", bg= 'black', fg='white', font= 'Calibri 16')
        usrpassEntry = tk.Entry(play_Frame, width = 25, font='Calibri 21')

        usrnameLabel.pack(side='top')
        usrnameEntry.pack(side='top', pady=20)

        usrpassEntry.pack(side='bottom', pady=20)
        usrpassLabel.pack(side='bottom')
        
        playPressed = True

        usrpassEntry.bind('<Return>', lambda event: infoEntered(usrnameEntry, usrpassEntry, event))
        
    else:
        infoEntered(usrnameEntry, usrpassEntry)



#Main_Window
loginMenuW = tk.Tk()
loginMenuW.title("Login Menu")
loginMenuW.state('zoomed')
loginMenuW.config(bg='black')

#Global Variables
playPressed= False
uuid= usrname= None
usrnameEntry = None
usrpassEntry = None

#Basic Widgets
play_Frame = tk.Frame(loginMenuW, bg='black')

play_button = tk.Button(play_Frame,
                        command = play_pressed,
                        height= "1",
                        width ="30",
                        bg='red',
                        activebackground = '#960000',
                        text='PLAY',
                        font= 'Calibri 21')
play_button.pack(side='bottom')
play_Frame.pack(side='bottom', pady=150)


loginMenuW.mainloop()