import tkinter as tk
import tkinter.font as tkFont
from Menus.EditarCuenta import EditarCuenta as EC #Ignorar lo rojo, la linea funciona correctamente!

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

        GLabel_511 = tk.Label(rootCC)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_511["font"] = ft
        GLabel_511["fg"] = "#333333"
        GLabel_511["justify"] = "center"
        GLabel_511["text"] = "Viajes:"
        GLabel_511.place(x=40, y=120, width=121, height=30)

        GButton_248 = tk.Button(rootCC)
        GButton_248["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_248["font"] = ft
        GButton_248["fg"] = "#000000"
        GButton_248["justify"] = "center"
        GButton_248["text"] = "Buscar Viaje"
        GButton_248["relief"] = "groove"
        GButton_248.place(x=180, y=100, width=112, height=30)
        GButton_248["command"] = self.GButton_248_command

        GButton_804 = tk.Button(rootCC)
        GButton_804["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_804["font"] = ft
        GButton_804["fg"] = "#000000"
        GButton_804["justify"] = "center"
        GButton_804["text"] = "Crear Viaje"
        GButton_804["relief"] = "groove"
        GButton_804.place(x=310, y=100, width=112, height=30)
        GButton_804["command"] = self.GButton_804_command

        GLabel_763 = tk.Label(rootCC)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_763["font"] = ft
        GLabel_763["fg"] = "#333333"
        GLabel_763["justify"] = "center"
        GLabel_763["text"] = "Cuenta:"
        GLabel_763.place(x=60, y=230, width=84, height=30)

        GButton_171 = tk.Button(rootCC)
        GButton_171["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_171["font"] = ft
        GButton_171["fg"] = "#000000"
        GButton_171["justify"] = "center"
        GButton_171["text"] = "Vehiculos"
        GButton_171["relief"] = "groove"
        GButton_171.place(x=180, y=210, width=112, height=30)
        GButton_171["command"] = self.GButton_171_command

        GButton_809 = tk.Button(rootCC)
        GButton_809["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_809["font"] = ft
        GButton_809["fg"] = "#000000"
        GButton_809["justify"] = "center"
        GButton_809["text"] = "Datos de Cuenta"
        GButton_809["relief"] = "groove"
        GButton_809.place(x=310, y=210, width=112, height=30)
        GButton_809["command"] = self.GButton_809_command

        GButton_83 = tk.Button(rootCC)
        GButton_83["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_83["font"] = ft
        GButton_83["fg"] = "#000000"
        GButton_83["justify"] = "center"
        GButton_83["text"] = "Metodos de pago"
        GButton_83["relief"] = "groove"
        GButton_83.place(x=250, y=260, width=112, height=30)
        GButton_83["command"] = self.GButton_83_command

        GButton_923 = tk.Button(rootCC)
        GButton_923["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_923["font"] = ft
        GButton_923["fg"] = "#000000"
        GButton_923["justify"] = "center"
        GButton_923["text"] = "Historial"
        GButton_923["relief"] = "groove"
        GButton_923.place(x=250, y=140, width=112, height=30)
        GButton_923["command"] = self.GButton_923_command

    def GButton_248_command(self):
        print("command")

    def GButton_804_command(self):
        print("command")

    def GButton_171_command(self):
        print("command")

    def GButton_809_command(self):
        self.rootCC.destroy()
        EC()
        MenuUsuario()

    def GButton_83_command(self):
        print("command")

    def GButton_923_command(self):
        print("command")