import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkcalendar import DateEntry
from datetime import datetime
import re
from SQL_conection.conector import Conection

class Vehiculos:
    def __init__(self):
        self.rootCC = tk.Tk()
        self.Startup(self.rootCC)
        self.rootCC.mainloop()

    def Startup(self,rootCC):
        def block_input(event):
            return "break"
        #setting title
        self.rootCC.title("BlaBlaCar - Vehiculos")
        #setting window size
        width=500
        height=550
        screenwidth = self.rootCC.winfo_screenwidth()
        screenheight = self.rootCC.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.rootCC.geometry(alignstr)
        self.rootCC.resizable(width=False, height=False)

        frame = tk.Frame(rootCC, relief= 'solid',width= 500, height= 200, bd= 1)
        frame.pack(pady=20,padx=20)
        frame.grid_propagate(False)
        label0 = tk.Label(frame,text = 'VEHICULO 1')
        label0.grid(column=0,row=0,columnspan=5,pady=10)
        label1 = tk.Label(frame,text='PLACA:')
        label1.grid(column=0,row=1,padx=5,pady=5)
        self.placa = tk.Entry(frame)
        self.placa.grid(column=1,row=1,padx=5,pady=5)
        self.placa.insert(0, "Holder")
        self.placa.bind("<Key>", block_input)
        flab = tk.Label(frame, text='')
        flab.grid(column=2, row=1, padx=1,pady=5)
        label2 = tk.Label(frame,text='MARCA:')
        label2.grid(column=3,row=1,padx=10,pady=5)


        self.marca = tk.Entry(frame)
        self.marca.grid(column=4, row=1,padx=5,pady=5)
        self.marca.insert(0, "Holder1")
        self.marca.bind("<Key>", block_input)

        label3 = tk.Label(frame, text='TIPO:')
        label3.grid(column=0,row=2,padx=5,pady=5)

        self.Tipo = tk.StringVar()
        self.Tipo.set('Otro')
        self.GComboBox = ttk.Combobox(frame)
        self.GComboBox['textvariable'] = self.Tipo
        self.GComboBox['values'] = ['SUV', 'Sedan', 'Camioneta', 'Deportivo', 'Crossover','Otro']
        self.GComboBox['state'] = 'disabled'
        self.GComboBox.grid(column = 1, row = 2, padx= 5, pady=10)

        label4 = tk.Label(frame, text = 'COLOR:')
        label4.grid(column=3,row=2,pady=5,padx=5)

        self.Color = tk.Entry(frame)
        self.Color.grid(column=4, row=2, padx=5, pady=5)
        self.Color.insert(0, "Holder2")
        self.Color.bind("<Key>", block_input)

        label5 = tk.Label(frame,text='F. MATRICULA:')
        label5.grid(column=0,row=3,padx=2,pady=5)


        self.Fmatricula = tk.Entry(frame)
        self.Fmatricula.grid(column=1, row=3,padx=5,pady=5)
        self.Fmatricula.insert(0, "Holder3")
        self.Fmatricula.bind("<Key>", block_input)

        label6 = tk.Label(frame, text='ESTADO:')
        label6.grid(column=3, row=3, padx=2, pady=5)
        EstdCol = 'red'
        Estad = 'ACTIVO'
        if Estad == 'ACTIVO':
            EstdCol = 'green'
        elif Estad == 'INACTIVO':
            EstdCol = 'red'

        self.Estado = tk.Label(frame)
        self.Estado.grid(column=4, row=3, padx=5, pady=5)
        self.Estado['text'] = Estad
        self.Estado['fg'] = EstdCol
        self.Estado.bind("<Key>", block_input)
        self.label04 = tk.Label(frame, text=' ')
        self.label04.grid(column=0, row=4)
        frame3 = tk.Frame(frame,width=400,height=30)
        frame3.grid(column=0,row=5,columnspan=5)
        frame3.pack_propagate(False)
        self.Restablecer = tk.Button(frame3, text='Restablecer', width=10)
        self.Restablecer.config(state="disabled")
        self.Restablecer.pack(side = 'right',padx=5)
        self.Guardar = tk.Button(frame3, text = 'Guardar', width=10, command= self.Guardar)
        self.Guardar.config(state="disabled")
        self.Guardar.pack(side = 'right',padx=5)


        frame2 = tk.Frame(rootCC)
        frame2.pack()

        label01 = tk.Label(frame2,text=' ')

        label01.grid(column=0,row=0,padx=5)

        self.eliminaract = tk.Button(frame2)
        self.eliminaract['text'] = 'Eliminar'
        self.eliminaract.grid(column=1,row=0,padx=5)

        self.editaract = tk.Button(frame2)
        self.editaract['text'] = 'Editar'
        self.editaract.grid(column=2, row=0,padx=5)
        self.editaract['command'] = self.Editar

        self.nuevoact = tk.Button(frame2)
        self.nuevoact['text'] = 'Nuevo'
        self.nuevoact.grid(column=3, row=0, padx=5)

        label02 = tk.Label(frame2,text=' ')
        label02.grid(column=4,row=0,padx=50)

        self.botlef = tk.Button(frame2)
        self.botlef['text'] = '<-'
        self.botlef.grid(column=5,row=0,padx=1)

        self.botrig = tk.Button(frame2)
        self.botrig['text'] = '->'
        self.botrig.grid(column=6, row=0, padx=1)

    def Elimiar(self):
        None
    def Editar(self):
        self.placa.unbind('<Key>')
        self.Color.unbind('<Key>')
        self.marca.unbind('<Key>')
        self.Fmatricula.unbind('<Key>')
        self.editaract.config(state="disabled")
        self.nuevoact.config(state="disabled")
        self.eliminaract.config(state="disabled")
        self.botlef.config(state="disabled")
        self.botrig.config(state="disabled")


        self.Restablecer.config(state="active")
        self.Guardar.config(state="active")
    def Guardar(self):
        self.editaract.config(state='active')
        self.Guardar.config(state="disabled")
        self.Restablecer.config(state="disabled")
        self.nuevoact.config(state="active")
        self.eliminaract.config(state="active")
        self.botlef.config(state="active")
        self.botrig.config(state="active")


    def Crear(self):
        None