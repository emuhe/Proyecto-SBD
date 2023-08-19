import tkinter as tk
class MenuUsuario:
    def __init__(self):
        self.rootCC = tk.Tk()
        self.Startup(self.rootCC)
        self.rootCC.mainloop()

    def Startup(self,rootCC):
        #setting title
        self.rootCC.title("BlaBlaCar - Crear Cuenta")
        #setting window size
        width=500
        height=550
        screenwidth = self.rootCC.winfo_screenwidth()
        screenheight = self.rootCC.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.rootCC.geometry(alignstr)
        self.rootCC.resizable(width=False, height=False)