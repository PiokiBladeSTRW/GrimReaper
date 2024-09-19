#MainMenu
import tkinter as tk
import Auth.log_in as Auth
#from tkinter import simpledialog


def infoEntered(nameE, passE, event=None):
    global loggedIn
    usrname = nameE.get()
    usrpass = passE.get()
    if( Auth.LogIn(usrname, usrpass) ):
        loggedIn = True
        mainMenuW.destroy()
    
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
mainMenuW = tk.Tk()
mainMenuW.title("Main Menu")
mainMenuW.state('zoomed')
mainMenuW.config(bg='black')

#Global Variables
playPressed= False
loggedIn= False
usrnameEntry = None
usrpassEntry = None

#Basic Widgets
play_Frame = tk.Frame(mainMenuW, bg='black')

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


mainMenuW.mainloop()
