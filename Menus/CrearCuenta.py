import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkcalendar import DateEntry
from datetime import datetime



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
        height=500
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
        GLabel_963.place(x=30,y=60,width=71,height=31)

        GLineEdit_554=tk.Entry(self.rootCC)
        GLineEdit_554["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_554["font"] = ft
        GLineEdit_554["fg"] = "#333333"
        GLineEdit_554["justify"] = "center"
        GLineEdit_554["text"] = ""
        GLineEdit_554.place(x=100,y=60,width=130,height=30)

        GLabel_6=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_6["font"] = ft
        GLabel_6["fg"] = "#333333"
        GLabel_6["justify"] = "left"
        GLabel_6["text"] = "*Apellido:"
        GLabel_6.place(x=230,y=60,width=72,height=30)

        GLineEdit_531=tk.Entry(self.rootCC)
        GLineEdit_531["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_531["font"] = ft
        GLineEdit_531["fg"] = "#333333"
        GLineEdit_531["justify"] = "center"
        GLineEdit_531["text"] = ""
        GLineEdit_531.place(x=300,y=60,width=131,height=30)

        GLabel_426=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "left"
        GLabel_426["text"] = "*Correo:"
        GLabel_426.place(x=30,y=110,width=72,height=35)

        GLineEdit_983=tk.Entry(self.rootCC)
        GLineEdit_983["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_983["font"] = ft
        GLineEdit_983["fg"] = "#333333"
        GLineEdit_983["justify"] = "center"
        GLineEdit_983["text"] = ""
        GLineEdit_983.place(x=100,y=110,width=331,height=30)

        GLabel_842=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_842["font"] = ft
        GLabel_842["fg"] = "#333333"
        GLabel_842["justify"] = "left"
        GLabel_842["text"] = "*Fecha de Nacimiento:"
        GLabel_842.place(x=30,y=150,width=135,height=45)

        GDateEntry = DateEntry(self.rootCC)
        GDateEntry['date_pattern'] = 'DD/MM/YYYY'
        GDateEntry['maxdate'] = datetime.today().date()
        GDateEntry.place (x=170,y=155,width=90,height=35)

        GLabel_843=tk.Label(self.rootCC)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_843["font"] = ft
        GLabel_843["fg"] = "#333333"
        GLabel_843["justify"] = "left"
        GLabel_843["text"] = "*Genero:"
        GLabel_843.place(x=265,y=150,width=70,height=45)

        genero = tk.StringVar()
        GComboBox = ttk.Combobox(self.rootCC)
        GComboBox['textvariable'] = genero
        GComboBox['values'] = ['Hombre','Mujer','Otro']
        GComboBox['state'] = 'readonly'
        GComboBox.place(x=335,y=155,width=75,height=35)




