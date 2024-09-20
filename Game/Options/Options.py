import tkinter as tk

def Destroy(event):
    event.widget.destroy()
        
def Help(root):
    helpF = tk.Frame(root, bg='red')
    helpF.place(relx=0, rely=0, relheight=1, relwidth=1 )
    helpF.focus_set()
    helpF.bind("<Escape>", Destroy)




# #Options Window
# optionsW = tk.Tk()
# optionsW.title("HELP")
# optionsW.state('zoomed')
# optionsW.config(bg='black')

# Help(optionsW)

# optionsW.mainloop()