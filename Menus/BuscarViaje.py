import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from SQL_conection.conector import Conection as CN

class BuscarViaje:
    def __init__(self,user_id):
        self.user_id = user_id
        self.conection = CN()
        self.TravelData()
        self.rootBV = tk.Tk()
        self.Startup(self.rootBV)
        self.rootBV.mainloop()
    def Startup(self,root):
        scroll_max = len(self.Travels)*160+20
        def on_frame_configure(canvas, scroll_height=scroll_max):
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

        Filtros = tk.Frame(root,width=500,height=100,background='red')
        Filtros.pack_propagate(False)
        Filtros.pack()

        canvas = tk.Canvas(root, bd=0, highlightthickness=0,background='green')
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        v_scroll = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=v_scroll.set)


        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: on_frame_configure(canvas))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        #self.CreateTravel(self.scrollable_frame,'Nombre','Apellido','Partida','Llegada',3,4,2.5,'11:50',0,4,'Kia Picanto')
        #self.CreateTravel(self.scrollable_frame,'Nombre','Apellido','Partida','Llegada',4,4,2.5,'11:50',0,4,'Kia Picanto')
        for Viaje in self.Travels:
            self.CreateTravel(self.scrollable_frame,Viaje[0],Viaje[1],Viaje[2],Viaje[3],Viaje[4],Viaje[5],Viaje[6],Viaje[7],Viaje[8],Viaje[9],Viaje[10])

    def TravelData(self):
        self.Travels = self.conection.Viajes(self.user_id)
        print(self.Travels)

    def CreateTravel(self,root,Nombre,Apellido,partida,llegada,pasajeros,asientos,precio,tiempo_salida,estado,valoracion,vehiculo):
        # Create outer frame
        print('1')
        first_frame = tk.Frame(self.scrollable_frame,width=465,height=160,bg='white',bd=1, relief= 'solid')
        first_frame.pack(padx=10,pady=10)
        first_frame.grid_propagate(False)
        f_partida = tk.Label(first_frame, text=partida)
        tk.Label(first_frame,text='Punto de Partida:').grid(row=0,column=0,pady=5,padx=5)
        f_partida.grid(row=0,column=1,pady=5,padx=5)
        tk.Label(first_frame,text='Punto de Llegada:').grid(row=0,column=3,pady=5,padx=5)
        f_llegada = tk.Label(first_frame, text=llegada)
        f_llegada.grid(row=0, column=4, pady=5, padx=5)
        cant_pasajeros = ''
        colour = ''
        if int(pasajeros) == asientos:
            cant_pasajeros = 'ASIENTOS COMPLETOS'
            colour = 'red'
        else:
            cant_pasajeros = str(4-pasajeros)+'/4 DISPONIBLES'
            colour = 'green'
        tk.Label(first_frame,text='Asientos disponibles:').grid(row=1,column=0,pady=5,padx=5)
        f_pasajeros = tk.Label(first_frame,text=cant_pasajeros,fg=colour)
        f_pasajeros.grid(row=1,column=1,padx=5,pady=5)
        tk.Label(first_frame,text='P. por asiento:').grid(row=1,column=3,pady=5,padx=5)
        f_precio = tk.Label(first_frame,text='$'+str(precio))
        f_precio.grid(row=1,column=4,pady=5,padx=5)
        tk.Label(first_frame,text='Conductor:').grid(row=2,column=0,pady=5,padx=5)
        f_conductor = tk.Label(first_frame,text= Nombre + ' ' + Apellido)
        f_conductor.grid(row=2,column=1,pady=5,padx=5)
        tk.Label(first_frame,text='Valoracion:').grid(row=2,column=3,pady=5,padx=5)
        tk.Label(first_frame,text='Fecha de Salida:').grid(row=3,column=0,pady=5,padx=5)
        salida = tk.Label(first_frame,text=tiempo_salida)
        salida.grid(row=3,column=1,pady=5,padx=5)
        tk.Label(first_frame,text='Vehiculo:').grid(row=3,column=3,pady=5,padx=5)
        tk.Label(first_frame,text=vehiculo).grid(row=3,column=4,pady=5,padx=5)
        Botones = tk.Frame(first_frame,width=465,height=40,background='purple')
        Botones.pack_propagate(False)
        Botones.grid(row=4,column=0,columnspan=5)
        reserva = tk.Button(Botones,text='Reservar')


