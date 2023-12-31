import tkinter as tk
import tkinter.font as tkFont
from Menus.CrearCuenta import App as CC
from Menus.principal import MenuUsuario as MU
from Menus.EditarCuenta import EditarCuenta as EC
from SQL_conection.conector import Conection as SQLC
from datetime import date,timedelta
import re
from tkcalendar import DateEntry
from datetime import date
import mysql.connector
from mysql.connector.locales.eng import client_error
import mysql.connector.plugins.mysql_native_password

class MainMenu:
    def __init__(self,root):
        self.conect = SQLC()
        # setting title
        root.title("BlaBlaCar")
        # setting window size
        width = 500
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_551 = tk.Label(root)
        GLabel_551["anchor"] = "n"
        ft = tkFont.Font(family='Times', size=28)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = "Bienvenido a BlaBlaCar!"
        GLabel_551.place(x=70, y=40, width=373, height=47)

        GButton_760 = tk.Button(root)
        GButton_760["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_760["font"] = ft
        GButton_760["fg"] = "#000000"
        GButton_760["justify"] = "center"
        GButton_760["text"] = "Ingresar"
        GButton_760["relief"] = "groove"
        GButton_760.place(x=190, y=250, width=120, height=30)
        GButton_760["command"] = self.GButton_760_command

        GLabel_238 = tk.Label(root)
        self.validate_cmd = root.register(self.num_validation)

        self.Cedula = tk.StringVar()
        ft = tkFont.Font(family='Times', size=18)
        GLabel_238["font"] = ft
        GLabel_238["fg"] = "#333333"
        GLabel_238["justify"] = "center"
        GLabel_238["text"] = "Cedula:"

        GLabel_238.place(x=80, y=130, width=104, height=32)

        GLabel_410 = tk.Label(root)
        self.Nombre = tk.StringVar()
        ft = tkFont.Font(family='Times', size=18)
        GLabel_410["font"] = ft
        GLabel_410["fg"] = "#333333"
        GLabel_410["justify"] = "center"
        GLabel_410["text"] = "Nombre:"

        GLabel_410.place(x=50, y=190, width=130, height=33)

        self.GLineEdit_742 = tk.Entry(root)
        self.GLineEdit_742["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=13)
        self.GLineEdit_742["font"] = ft
        self.GLineEdit_742["fg"] = "#333333"
        self.GLineEdit_742["justify"] = "center"
        self.GLineEdit_742["text"] = ""
        self.GLineEdit_742['validate'] = 'key'
        self.GLineEdit_742['validatecommand'] = (self.validate_cmd,'%P')
        self.GLineEdit_742['textvariable'] = self.Cedula
        self.GLineEdit_742.place(x=220, y=130, width=179, height=31)

        self.GLineEdit_325 = tk.Entry(root)
        self.GLineEdit_325["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=13)
        self.GLineEdit_325["font"] = ft
        self.GLineEdit_325["fg"] = "#333333"
        self.GLineEdit_325["justify"] = "center"
        self.GLineEdit_325["text"] = ""
        self.GLineEdit_325['textvariable'] = self.Nombre
        self.GLineEdit_325.place(x=220, y=190, width=179, height=30)

        GLabel_803 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_803["font"] = ft
        GLabel_803["fg"] = "#000000"
        GLabel_803["justify"] = "center"
        GLabel_803["text"] = "Todavia no tiene una cuenta?"
        GLabel_803.place(x=160, y=290, width=176, height=30)

        GButton_748 = tk.Button(root)
        GButton_748["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_748["font"] = ft
        GButton_748["fg"] = "#000000"
        GButton_748["justify"] = "center"
        GButton_748["text"] = "Crear Cuenta"
        GButton_748["relief"] = "groove"
        GButton_748.place(x=190, y=320, width=120, height=30)
        GButton_748["command"] = self.GButton_748_command

        self.GLabel_316 = tk.Label(root) #SA
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_316["font"] = ft
        self.GLabel_316["fg"] = "#000000"
        self.GLabel_316["justify"] = "center"
        self.GLabel_316["text"] = ""
        self.GLabel_316.place(x=100, y=220, width=313, height=30)

    def GButton_760_command(self): #Verificar si los datos ingresados son correctos
        _mcache,ID = self.conect.InicioSesion(self.Cedula.get(),self.Nombre.get())
        if _mcache:
            root.destroy()
            MU(ID)
        else:
            self.GLabel_316['text'] = 'Usuario y/o Contraseña incorrecta, intente otra vez '


    def GButton_748_command(self): #Abrir otra ventana para lo de crear cuenta
        root.destroy()
        self.conect.CerrarConeccion()
        CC()
    def num_validation(self,P):
        if (P.isdigit() or P == "") and len(P) <= 10:
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
