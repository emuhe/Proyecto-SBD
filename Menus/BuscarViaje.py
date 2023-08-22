import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from SQL_conection.conector import Conection as CN

class BuscarViaje:
    def __init__(self,user_id):
        self.user_id = user_id
        self.rootBV = tk.Tk()
        self.Startup(self.rootBV)
        self.rootBV.mainloop()
    def Startup(self,root):
        def on_frame_configure(canvas, scroll_height=1000):
            '''Set the scroll region with a limit'''
            width, height = canvas.winfo_width(), scroll_height
            canvas.configure(scrollregion=(0, 0, width, height))
        width = 500
        height = 550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.conection = CN()
        self.TravelData()

    def TravelData(self):
        self.Travels = self.conection.Viajes(self.user_id)
        print(self.Travels)

    def CreateTravel(self,root,Nombre,Apellido,partida,llegada,pasajeros,asientos,precio,tiempo_salida,estado,valoracion):
        # Create outer frame
        outer_frame = tk.Frame(root, bg="blue", bd=5)
        outer_frame.pack(fill="both", expand=True)
        first_frame = tk.Frame(outer_frame,width=480,height=100,bg='white',bd=1, relief= 'solid')
        first_frame.pack(padx=10,pady=10)
        first_frame.grid_propagate(False)
        f_partida = tk.Label(first_frame, text=partida)
        tk.Label(first_frame,text='Punto de Partida:').grid(row=0,column=0,pady=5,padx=5)
        f_partida.grid(row=0,column=1,pady=5,padx=5)
        tk.Label(first_frame,text='--->').grid(row=0,column=2,pady=5,padx=10)
        tk.Label(first_frame,text='Punto de Llegada:').grid(row=0,column=3,pady=5,padx=5)
        f_llegada = tk.Label(first_frame, text=llegada)
        f_llegada.grid(row=0, column=4, pady=5, padx=5)
        cant_pasajeros = ''
        colour = ''
        if int(pasajeros) == asientos:
            cant_pasajeros = 'ASIENTOS COMPLETOS'
            colour = 'red'
        else:
            cant_pasajeros = str(pasajeros)+'/4 DISPONIBLES'
            colour = 'green'
        tk.Label(first_frame,text='Asientos disponibles', fg=colour).grid(row=1,column=0,pady=5,padx=5)
        f_pasajeros = tk.Label(first_frame)
        f_pasajeros.grid(row=1,column=1,padx=5,pady=5)
        tk.Label(first_frame,text='P. por asiento:').grid(row=1,column=3,pady=5,padx=5)
        f_precio = tk.Label(first_frame,text='$'+str(precio))
        f_precio.grid(row=1,column=4,pady=5,padx=5)
        tk.Label(first_frame,text='Conductor:').grid(row=2,column=0,pady=5,padx=5)
        f_conductor = tk.Label(first_frame,text= Nombre + ' ' + Apellido)
        f_conductor.grid(row=2,column=1,pady=5,padx=5)
        tk.Label(first_frame,text='Valoracion:').grid(row=2,column=0,pady=5,padx=5)
