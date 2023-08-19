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
        flab = tk.Label(frame, text='  ')
        flab.grid(column=2, row=0, padx=5,pady=5)
        label2 = tk.Label(frame,text='MARCA:')
        label2.grid(column=3,row=0,padx=20,pady=5)


        marca = tk.Entry(frame)
        marca['text'] = 'PLACEHOLDER'
        marca.grid(column=4, row=0,padx=5,pady=5)
        marca.insert(0, "Holder2")
        marca.bind("<Key>", block_input)

        label3 = tk.Label(frame, text='TIPO:')
        label3.grid(column=0,row=1,padx=5,pady=5)

