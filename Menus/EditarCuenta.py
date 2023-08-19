import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkcalendar import DateEntry
from datetime import datetime
import re


class EditarCuenta:
    def __init__(self):
        self.tim = True

        self.rootCC = tk.Tk()
        self.Startup(self.rootCC)
        self.rootCC.mainloop()


    def CreateVar(self):
        self.Nombre = tk.StringVar()
        self.Apellido = tk.StringVar()
        self.Correo = tk.StringVar()
        self.genero = tk.StringVar()
        self.direccion = tk.StringVar()
        self.telefono = tk.StringVar()
        self.ID = tk.StringVar()
        self.Pref_1 = tk.IntVar()
        self.Pref_2 = tk.IntVar()
        self.Pref_3 = tk.IntVar()
        self.Pref_4 = tk.IntVar()

    def Change(self): #Aqui hay que recoger los datos de la tabla y ponerlos para despues editarlos
        self.Nombre.set('')
        self.Apellido.set('')
        self.Correo.set('')
        self.genero.set('-Seleccionar-')
        self.direccion.set('')
        self.ID.set('')
        self.telefono.set('')
        self.Pref_4.set(2)
        self.Pref_3.set(2)
        self.Pref_2.set(2)
        self.Pref_1.set(2)

    def Startup(self,rootCC):
        if self.tim:

            self.CreateVar()
            self.tim = False
            self.Change()
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
        self.GDateEntry['maxdate'] = datetime.today().date()
        self.GDateEntry.place (x=170,y=125,width=90,height=35)


        GLabel_843=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_843["font"] = ft
        GLabel_843["fg"] = "#333333"
        GLabel_843["justify"] = "left"
        GLabel_843["text"] = "*Genero:"
        GLabel_843.place(x=265,y=120,width=70,height=45)

        GComboBox = ttk.Combobox(self.rootCC)
        GComboBox['textvariable'] = self.genero
        GComboBox['values'] = ['Hombre','Mujer','Otro']
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
        GLabel_846["text"] = "*Preferencias"
        GLabel_846.place(x=35, y=245, width=75, height=30)

        #######################################################
        #  ----------------- SEPARACION --------------------- #
        #######################################################

        GLabel_847 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_847["font"] = ft
        GLabel_847["fg"] = "#333333"
        GLabel_847["justify"] = "left"
        GLabel_847["text"] = "Fumar en el viaje:"
        GLabel_847.place(x=35, y=270, width=105, height=30)

        self.Pref_1.set(2)
        P1_Opt1 = tk.Radiobutton(self.rootCC)
        P1_Opt1['value'] = 1
        P1_Opt1['variable'] = self.Pref_1
        P1_Opt1.place(x=190,y=265)

        GLabel_848 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_848["font"] = ft
        GLabel_848["fg"] = "#333333"
        GLabel_848["justify"] = "left"
        GLabel_848["text"] = "En desacuerdo"
        GLabel_848.place(x=145, y=285, width=105, height=30)

        P1_Opt2 = tk.Radiobutton(self.rootCC)
        P1_Opt2['value'] = 2
        P1_Opt2['variable'] = self.Pref_1
        P1_Opt2.place(x=285, y=265)

        GLabel_848 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_848["font"] = ft
        GLabel_848["fg"] = "#333333"
        GLabel_848["justify"] = "left"
        GLabel_848["text"] = "Neutro"
        GLabel_848.place(x=245, y=285, width=105, height=30)

        P1_Opt3 = tk.Radiobutton(self.rootCC)
        P1_Opt3['value'] = 3
        P1_Opt3['variable'] = self.Pref_1
        P1_Opt3.place(x=385, y=265)

        GLabel_848 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_848["font"] = ft
        GLabel_848["fg"] = "#333333"
        GLabel_848["justify"] = "left"
        GLabel_848["text"] = "De Acuerdo"
        GLabel_848.place(x=345, y=285, width=105, height=30)

        #######################################################
        #  ----------------- SEPARACION --------------------- #
        #######################################################

        GLabel_849 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_849["font"] = ft
        GLabel_849["fg"] = "#333333"
        GLabel_849["justify"] = "left"
        GLabel_849["text"] = "Mascotas a bordo:"
        GLabel_849.place(x=35, y=320, width=105, height=30)

        P2_Opt1 = tk.Radiobutton(self.rootCC)
        P2_Opt1['value'] = 1
        P2_Opt1['variable'] = self.Pref_2
        P2_Opt1.place(x=190, y=315)

        GLabel_849 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_849["font"] = ft
        GLabel_849["fg"] = "#333333"
        GLabel_849["justify"] = "left"
        GLabel_849["text"] = "En desacuerdo"
        GLabel_849.place(x=145, y=335, width=105, height=30)

        P2_Opt2 = tk.Radiobutton(self.rootCC)
        P2_Opt2['value'] = 2
        P2_Opt2['variable'] = self.Pref_2
        P2_Opt2.place(x=285, y=315)

        GLabel_850 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_850["font"] = ft
        GLabel_850["fg"] = "#333333"
        GLabel_850["justify"] = "left"
        GLabel_850["text"] = "Neutro"
        GLabel_850.place(x=245, y=335, width=105, height=30)

        P2_Opt3 = tk.Radiobutton(self.rootCC)
        P2_Opt3['value'] = 3
        P2_Opt3['variable'] = self.Pref_2
        P2_Opt3.place(x=385, y=315)

        GLabel_851 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_851["font"] = ft
        GLabel_851["fg"] = "#333333"
        GLabel_851["justify"] = "left"
        GLabel_851["text"] = "De Acuerdo"
        GLabel_851.place(x=345, y=335, width=105, height=30)

        #######################################################
        #  ----------------- SEPARACION --------------------- #
        #######################################################

        GLabel_860 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_860["font"] = ft
        GLabel_860["fg"] = "#333333"
        GLabel_860["justify"] = "left"
        GLabel_860["text"] = "Musica a Bordo:"
        GLabel_860.place(x=35, y=370, width=105, height=30)


        P3_Opt1 = tk.Radiobutton(self.rootCC)
        P3_Opt1['value'] = 1
        P3_Opt1['variable'] = self.Pref_3
        P3_Opt1.place(x=190, y=365)

        GLabel_849 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_849["font"] = ft
        GLabel_849["fg"] = "#333333"
        GLabel_849["justify"] = "left"
        GLabel_849["text"] = "En desacuerdo"
        GLabel_849.place(x=145, y=385, width=105, height=30)

        P3_Opt2 = tk.Radiobutton(self.rootCC)
        P3_Opt2['value'] = 2
        P3_Opt2['variable'] = self.Pref_3
        P3_Opt2.place(x=285, y=365)

        GLabel_850 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_850["font"] = ft
        GLabel_850["fg"] = "#333333"
        GLabel_850["justify"] = "left"
        GLabel_850["text"] = "Neutro"
        GLabel_850.place(x=245, y=385, width=105, height=30)

        P3_Opt3 = tk.Radiobutton(self.rootCC)
        P3_Opt3['value'] = 3
        P3_Opt3['variable'] = self.Pref_3
        P3_Opt3.place(x=385, y=365)

        GLabel_851 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_851["font"] = ft
        GLabel_851["fg"] = "#333333"
        GLabel_851["justify"] = "left"
        GLabel_851["text"] = "De Acuerdo"
        GLabel_851.place(x=345, y=385, width=105, height=30)

        #######################################################
        #  ----------------- SEPARACION --------------------- #
        #######################################################

        GLabel_861 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#333333"
        GLabel_861["justify"] = "left"
        GLabel_861["text"] = "Charla a bordo:"
        GLabel_861.place(x=35, y=420, width=105, height=30)


        P4_Opt1 = tk.Radiobutton(self.rootCC)
        P4_Opt1['value'] = 1
        P4_Opt1['variable'] = self.Pref_4
        P4_Opt1.place(x=190, y=415)

        GLabel_862 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_862["font"] = ft
        GLabel_862["fg"] = "#333333"
        GLabel_862["justify"] = "left"
        GLabel_862["text"] = "En desacuerdo"
        GLabel_862.place(x=145, y=435, width=105, height=30)

        P4_Opt2 = tk.Radiobutton(self.rootCC)
        P4_Opt2['value'] = 2
        P4_Opt2['variable'] = self.Pref_4
        P4_Opt2.place(x=285, y=415)

        GLabel_862 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_862["font"] = ft
        GLabel_862["fg"] = "#333333"
        GLabel_862["justify"] = "left"
        GLabel_862["text"] = "Neutro"
        GLabel_862.place(x=245, y=435, width=105, height=30)

        P4_Opt3 = tk.Radiobutton(self.rootCC)
        P4_Opt3['value'] = 3
        P4_Opt3['variable'] = self.Pref_4
        P4_Opt3.place(x=385, y=415)

        GLabel_863 = tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_863["font"] = ft
        GLabel_863["fg"] = "#333333"
        GLabel_863["justify"] = "left"
        GLabel_863["text"] = "De Acuerdo"
        GLabel_863.place(x=345, y=435, width=105, height=30)


        GButton_749 = tk.Button(self.rootCC)
        GButton_749["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_749["font"] = ft
        GButton_749["fg"] = "#000000"
        GButton_749["justify"] = "center"
        GButton_749["text"] = "Confirmar Cambios"
        GButton_749["relief"] = "groove"
        GButton_749.place(x=200, y=480, width=120, height=30)
        GButton_749["command"] = self.CrearCuenta
    def CrearCuenta(self):
        self.popup()

    def num_validation(self,P):
        if (P.isdigit() or P == "") and len(P) <= 10:
            return True
        return False
    def popup(self):
        self.pop = tk.Toplevel(self.rootCC)
        self.pop.title('Cuenta Editada')
        width = 300
        height = 100
        screenwidth = self.pop.winfo_screenwidth()
        screenheight = self.pop.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.pop.geometry(alignstr)
        self.pop.resizable(width=False, height=False)
        label = tk.Label(self.pop, text= 'Cuenta Editada exitosamente!')
        label.pack(padx=20,pady=20)
        b2 = tk.Button(self.pop, text = 'Continuar',command=self.continuar)
        b2.place(x=100,y=50,width=100)
        self.pop.grab_set()

    def continuar(self):
        self.pop.destroy()
        self.rootCC.destroy()
