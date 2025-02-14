class Options:
    import tkinter as tk
    from tkinter import messagebox
    menuOpened = False

    def __init__(self, root):
        self.window = root

    def Help(self):
        if(self.menuOpened):
            self.ManualDestroy()                            
            return
        
        helpFrame = self.tk.Frame(self.window, bg='red')
        helpFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        helpFrame.focus_set()
        helpFrame.bind("<Escape>", self.Destroy)
        self.menuOpened = True       

    def Documentation(self):
        if(self.menuOpened):
            self.ManualDestroy()                          
            return
        
        helpFrame = self.tk.Frame(self.window, bg='blue')
        helpFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        helpFrame.focus_set()
        helpFrame.bind("<Escape>", self.Destroy)
        self.menuOpened = True        

    def Accounts(self, uuid):
        if(self.menuOpened):
            self.ManualDestroy()                           
            return
        
        helpFrame = self.tk.Frame(self.window, bg='green')
        helpFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        helpFrame.focus_set()
        helpFrame.bind("<Escape>", self.Destroy)
        self.menuOpened = True    

        self.messagebox.showinfo(title="UUID", message=uuid)

    def Destroy(self, event):
        event.widget.destroy()
        self.menuOpened = False

    def ManualDestroy(self):
        self.window.focus_get().destroy()
        self.menuOpened = False   