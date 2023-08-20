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
        frame.pack(pady=40,padx=20)
        frame.grid_propagate(False)

        label1 = tk.Label(frame,text='PLACA:')
        label1.grid(column=0,row=0,padx=5,pady=5)
        placa = tk.Entry(frame)
        placa.grid(column=1,row=0,padx=5,pady=5)
        placa.insert(0, "Holder")
        placa.bind("<Key>", block_input)
        flab = tk.Label(frame, text='')
        flab.grid(column=2, row=0, padx=1,pady=5)
        label2 = tk.Label(frame,text='MARCA:')
        label2.grid(column=3,row=0,padx=10,pady=5)


        marca = tk.Entry(frame)
        marca.grid(column=4, row=0,padx=5,pady=5)
        marca.insert(0, "Holder1")
        marca.bind("<Key>", block_input)

        label3 = tk.Label(frame, text='TIPO:')
        label3.grid(column=0,row=1,padx=5,pady=5)

        self.Tipo = tk.StringVar()
        self.Tipo.set('Otro')
        GComboBox = ttk.Combobox(frame)
        GComboBox['textvariable'] = self.Tipo
        GComboBox['values'] = ['SUV', 'Sedan', 'Camioneta', 'Deportivo', 'Crossover','Otro']
        GComboBox['state'] = 'disabled'
        GComboBox.grid(column = 1, row = 1, padx= 5, pady=10)

        label4 = tk.Label(frame, text = 'COLOR:')
        label4.grid(column=3,row=1,pady=5,padx=5)

        Color = tk.Entry(frame)
        Color.grid(column=4, row=1, padx=5, pady=5)
        Color.insert(0, "Holder2")
        Color.bind("<Key>", block_input)

        label5 = tk.Label(frame,text='F. MATRICULA:')
        label5.grid(column=0,row=2,padx=2,pady=5)


        Fmatricula = tk.Entry(frame)
        Fmatricula.grid(column=1, row=2,padx=5,pady=5)
        Fmatricula.insert(0, "Holder3")
        Fmatricula.bind("<Key>", block_input)

        label6 = tk.Label(frame, text='ESTADO:')
        label6.grid(column=3, row=2, padx=2, pady=5)
        EstdCol = 'red'
        Estad = 'ACTIVO'
        if Estad == 'ACTIVO':
            EstdCol = 'green'
        elif Estad == 'INACTIVO':
            EstdCol = 'red'

        Fmatricula = tk.Label(frame)
        Fmatricula.grid(column=4, row=2, padx=5, pady=5)
        Fmatricula['text'] = Estad
        Fmatricula['fg'] = EstdCol
        Fmatricula.bind("<Key>", block_input)