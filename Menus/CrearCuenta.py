import tkinter as tk
from tkinter import ttk
import re
import tkinter.font as tkFont
from tkcalendar import DateEntry
from datetime import date,timedelta
from SQL_conection.conector import Conection
from Menus.principal import MenuUsuario as MU

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class App:
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

        GLabel_963=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_963["font"] = ft
        GLabel_963["fg"] = "#333333"
        GLabel_963["justify"] = "left"
        GLabel_963["text"] = "*Nombre:"
        GLabel_963.place(x=30,y=30,width=70,height=31)

        self.Nombre = tk.StringVar()

        GLineEdit_554=tk.Entry(self.rootCC)
        GLineEdit_554["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_554["font"] = ft
        GLineEdit_554["fg"] = "#333333"
        GLineEdit_554["justify"] = "center"
        GLineEdit_554["text"] = ""
        GLineEdit_554["textvariable"] = self.Nombre
        GLineEdit_554.place(x=100,y=30,width=130,height=30)

        GLabel_6=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_6["font"] = ft
        GLabel_6["fg"] = "#333333"
        GLabel_6["justify"] = "left"
        GLabel_6["text"] = "*Apellido:"
        GLabel_6.place(x=230,y=30,width=70,height=30)

        self.Apellido = tk.StringVar()


        GLineEdit_531=tk.Entry(self.rootCC)
        GLineEdit_531["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_531["font"] = ft
        GLineEdit_531["fg"] = "#333333"
        GLineEdit_531["justify"] = "center"
        GLineEdit_531["text"] = ""
        GLineEdit_531["textvariable"] = self.Apellido
        GLineEdit_531.place(x=300,y=30,width=131,height=30)

        GLabel_426=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "left"
        GLabel_426["text"] = "*Correo:"
        GLabel_426.place(x=30,y=80,width=70,height=35)

        self.Correo = tk.StringVar()

        GLineEdit_983=tk.Entry(self.rootCC)
        GLineEdit_983["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_983["font"] = ft
        GLineEdit_983["fg"] = "#333333"
        GLineEdit_983["justify"] = "center"
        GLineEdit_983["text"] = ""
        GLineEdit_983["textvariable"] = self.Correo
        GLineEdit_983.place(x=100,y=80,width=331,height=30)

        GLabel_842=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_842["font"] = ft
        GLabel_842["fg"] = "#333333"
        GLabel_842["justify"] = "left"
        GLabel_842["text"] = "*Fecha de Nacimiento:"
        GLabel_842.place(x=30,y=120,width=135,height=45)


        self.GDateEntry = DateEntry(self.rootCC)
        self.GDateEntry['date_pattern'] = 'DD/MM/YYYY'
        self.GDateEntry['maxdate'] = date.today()- timedelta(days=18*365.25)
        self.GDateEntry.set_date(date.today()- timedelta(days=18*365.25))
        self.GDateEntry.place (x=170,y=125,width=90,height=35)


        GLabel_843=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_843["font"] = ft
        GLabel_843["fg"] = "#333333"
        GLabel_843["justify"] = "left"
        GLabel_843["text"] = "*Genero:"
        GLabel_843.place(x=265,y=120,width=70,height=45)

        self.genero = tk.StringVar()
        GComboBox = ttk.Combobox(self.rootCC)
        GComboBox['textvariable'] = self.genero
        GComboBox['values'] = ['-Seleccionar-','Masculino','Femenino']
        GComboBox['state'] = 'readonly'
        self.genero.set('-Seleccionar-')
        GComboBox.place(x=335,y=125,width=100,height=35)

        GLabel_844=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_844["font"] = ft
        GLabel_844["fg"] = "#333333"
        GLabel_844["justify"] = "left"
        GLabel_844["text"] = "*Direccion:"
        GLabel_844.place(x=30,y=170,width=75,height=30)

        self.direccion = tk.StringVar()

        GLineEdit_984=tk.Entry(self.rootCC)
        GLineEdit_984["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_984["font"] = ft
        GLineEdit_984["fg"] = "#333333"
        GLineEdit_984["justify"] = "center"
        GLineEdit_984["text"] = ""
        GLineEdit_984['textvariable'] = self.direccion
        GLineEdit_984.place(x=100,y=170,width=331,height=30)

        GLabel_845 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_845["font"] = ft
        GLabel_845["fg"] = "#333333"
        GLabel_845["justify"] = "left"
        GLabel_845["text"] = "*Telefono:"
        GLabel_845.place(x=30, y=215, width=75, height=30)

        self.telefono = tk.StringVar()
        self.validate_cmd = self.rootCC.register(self.num_validation)
        GLineEdit_985=tk.Entry(self.rootCC)
        GLineEdit_985["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_985["font"] = ft
        GLineEdit_985["fg"] = "#333333"
        GLineEdit_985["justify"] = "center"
        GLineEdit_985["text"] = ""
        GLineEdit_985['textvariable'] = self.telefono
        GLineEdit_985['validate'] = 'key'
        GLineEdit_985['validatecommand'] = (self.validate_cmd,'%P')
        GLineEdit_985.place(x=100,y=215,width=150,height=30)

        GLabel_846 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_846["font"] = ft
        GLabel_846["fg"] = "#333333"
        GLabel_846["justify"] = "left"
        GLabel_846["text"] = "*I.D:"
        GLabel_846.place(x=240, y=215, width=75, height=30)

        self.ID = tk.StringVar()

        GLineEdit_986 = tk.Entry(self.rootCC)
        GLineEdit_986["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_986["font"] = ft
        GLineEdit_986["fg"] = "#333333"
        GLineEdit_986["justify"] = "center"
        GLineEdit_986["text"] = ""
        GLineEdit_986['textvariable'] = self.ID
        GLineEdit_986['validate'] = "key"
        GLineEdit_986['validatecommand'] = (self.validate_cmd,'%P')
        GLineEdit_986.place(x=300, y=215, width=130, height=30)

        GLabel_846 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_846["font"] = ft
        GLabel_846["fg"] = "#333333"
        GLabel_846["justify"] = "left"
        GLabel_846["text"] = "*Mini-Biografia:"
        GLabel_846.place(x=30, y=250)

        self.text_entry = tk.Text(self.rootCC,width = 50, height= 3)
        self.text_entry.place(x= 30, y = 270)

        #######################################################
        #  ----------------- SEPARACION --------------------- #
        #######################################################

        GLabel_847 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_847["font"] = ft
        GLabel_847["fg"] = "#333333"
        GLabel_847["justify"] = "left"
        GLabel_847["text"] = "Cual es su preferencia:"
        GLabel_847.place(x=30, y=330, height=30)

        self.preferencia = tk.StringVar()
        Preferenc = ttk.Combobox(self.rootCC)
        Preferenc['textvariable'] = self.preferencia
        Preferenc['values'] = ['Fumar', 'Mascotas', 'Musica', 'Conversacion']
        Preferenc['state'] = 'readonly'
        self.preferencia.set('-Seleccionar-')
        Preferenc.place(x=160, y=333)



        GButton_748 = tk.Button(self.rootCC)
        GButton_748["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_748["font"] = ft
        GButton_748["fg"] = "#000000"
        GButton_748["justify"] = "center"
        GButton_748["text"] = "Limpiar"
        GButton_748["relief"] = "groove"
        GButton_748.place(x=100, y=480, width=120, height=30)
        GButton_748["command"] = self.LimpiarDatos

        GButton_749 = tk.Button(self.rootCC)
        GButton_749["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_749["font"] = ft
        GButton_749["fg"] = "#000000"
        GButton_749["justify"] = "center"
        GButton_749["text"] = "Crear Cuenta"
        GButton_749["relief"] = "groove"
        GButton_749.place(x=260, y=480, width=120, height=30)
        GButton_749["command"] = self.CrearCuenta
    def CrearCuenta(self):
        print('hi')
        self.ValidarCont()
        if self.Valid:
            self.popup()
            list = [0,self.Nombre.get(),self.Apellido.get(),self.preferencia.get(),None,
                    self.text_entry.get("1.0", "end-1c"),self.ID.get(),
                    self.genero.get(),self.direccion.get(),
                    self.GDateEntry.get_date(),self.telefono.get(),'pasajero',self.Correo.get()]
            Bab = Conection()
            self.user_id = Bab.Cuentacrear(list)

    def LimpiarDatos(self):
        self.preferencia.set('-Seleccionar-')
        self.Nombre.set('')
        self.Apellido.set('')
        self.Correo.set('')
        self.genero.set('-Seleccionar-')
        self.direccion.set('')
        self.ID.set('')
        self.telefono.set('')
        self.GDateEntry.set_date(date.today()- timedelta(days=18*365.25))
        self.text_entry.delete("1.0", "end")

    def num_validation(self,P):
        if (P.isdigit() or P == "") and len(P) <= 10:
            return True
        return False
    def popup(self):
        self.pop = tk.Toplevel(self.rootCC)
        self.pop.title('Cuenta Creada')
        width = 300
        height = 100
        screenwidth = self.pop.winfo_screenwidth()
        screenheight = self.pop.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.pop.geometry(alignstr)
        self.pop.resizable(width=False, height=False)
        label = tk.Label(self.pop, text= 'Cuenta creada exitosamente!')
        label.pack(padx=20,pady=20)
        b2 = tk.Button(self.pop, text = 'Continuar',command=self.continuar)
        b2.place(x=100,y=50,width=100)
        self.pop.grab_set()
    def MenuPrincipal(self):
        self.pop.destroy()
        self.rootCC.destroy()

    def continuar(self):
        self.rootCC.destroy()
        MU(self.user_id)

    def ValidarCont(self):
        print(self.Nombre.get())
        if (self.Nombre.get() == '' or any(char.isdigit() for char in self.Nombre.get()))\
                or (self.Apellido.get() == '' or any(char.isdigit() for char in self.Apellido.get()))\
                or (self.Correo.get() == '' or not bool(re.match(pattern, self.Correo.get())))\
                or self.preferencia.get() == '-Seleccionar-':
            print('invalid')
            self.Valid = False
        else:
            self.Valid = True
