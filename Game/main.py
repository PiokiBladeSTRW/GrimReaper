#Main
import tkinter as tk
import Auth.log_in as Auth
#from tkinter import simpledialog


def infoEntered(nameE, passE, event=None):
    usrname = nameE.get()
    usrpass = passE.get()
    if( Auth.LogIn(usrname, usrpass) ):
        print("LOGGED IN")
    
def play_pressed():
    global playPressed
    
    if( not playPressed ):
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

        
root = tk.Tk()
root.title("GAME")

#_GEOMETRY
root.state('zoomed')
root.config(bg='black')

playPressed= False

#Widgets
play_Frame = tk.Frame(root, bg='black')

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


root.mainloop()
