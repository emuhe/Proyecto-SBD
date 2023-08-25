import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from SQL_conection.conector import Conection as CN

class BuscarViaje:
    def __init__(self,user_id):
        self.firsttime = True
        self.user_id = user_id
        self.conection = CN()
        self.TravelData()
        self.rootBV = tk.Tk()
        self.Startup(self.rootBV)
        self.rootBV.mainloop()

    def Startup(self,root):
        scroll_max = len(self.Travels) *180
        def on_frame_configure(canvas, scroll_height=scroll_max):
            width, height = canvas.winfo_width(), scroll_height
            canvas.configure(scrollregion=(0, 0, width, height))
        width = 500
        height = 550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        Filtros = tk.Frame(root,width=500,height=100)
        Filtros.pack_propagate(False)
        Filtros.pack()
        partida_values =  ['-Todos-'] + self.conection.ObtenerPartidas()
        self.Partida = ttk.Combobox(Filtros,values = partida_values,state='readonly')
        self.Partida.set('-Todos-')
        self.Partida.bind('<<ComboboxSelected>>', self.DestinoSelection)
        tk.Label(Filtros,text='Partida:').grid(row=0,column=0,pady=5,padx=5)
        self.Partida.grid(row=0,column=1,pady=5,padx=5)
        tk.Label(Filtros,text='Destino:').grid(row=0,column=2,pady=5,padx=5)
        self.Destino = ttk.Combobox(Filtros,state='readonly')
        self.Destino.set('-Todos-')
        self.Destino.bind('<<ComboboxSelected>>', self.PartidasSeleccion)
        self.Destino.grid(row=0,column=3,pady=5,padx=5)

        canvas = tk.Canvas(root, bd=0, highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scroll = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=v_scroll.set)
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: on_frame_configure(canvas))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.DestinoSelection(None)
        self.PartidasSeleccion(None)

    def TravelData(self):
        self.Travels = self.conection.Viajes()

    def CreateTravel(self,root,Nombre,Apellido,partida,llegada,pasajeros,asientos,precio,tiempo_salida,estado,valoracion,vehiculo,numero):
        pad = 2
        first_frame = tk.Frame(self.scrollable_frame,width=465,height=160,bd=1, relief= 'solid')
        first_frame.pack(padx=10,pady=10)
        first_frame.grid_propagate(False)
        f_partida = tk.Label(first_frame, text=partida)
        tk.Label(first_frame,text='Punto de Partida:').grid(row=0,column=0,pady=5,padx=pad)
        f_partida.grid(row=0,column=1,pady=5,padx=pad)
        tk.Label(first_frame,text='Punto de Llegada:').grid(row=0,column=3,pady=5,padx=pad)
        f_llegada = tk.Label(first_frame, text=llegada)
        f_llegada.grid(row=0, column=4, pady=5, padx=pad)
        cant_pasajeros = ''
        colour = ''
        if int(pasajeros) == asientos:
            cant_pasajeros = 'ASIENTOS COMPLETOS'
            colour = 'red'
        else:
            cant_pasajeros = str(4-pasajeros)+'/4 DISPONIBLES'
            colour = 'green'
        tk.Label(first_frame,text='Asientos disponibles:').grid(row=1,column=0,pady=5,padx=pad)
        f_pasajeros = tk.Label(first_frame,text=cant_pasajeros,fg=colour)
        f_pasajeros.grid(row=1,column=1,padx=pad,pady=5)
        tk.Label(first_frame,text='P. por asiento:').grid(row=1,column=3,pady=5,padx=pad)
        f_precio = tk.Label(first_frame,text='$'+str(precio))
        f_precio.grid(row=1,column=4,pady=5,padx=pad)
        tk.Label(first_frame,text='Conductor:').grid(row=2,column=0,pady=5,padx=pad)
        f_conductor = tk.Label(first_frame,text= Nombre + ' ' + Apellido)
        f_conductor.grid(row=2,column=1,pady=5,padx=pad)
        tk.Label(first_frame,text='Valoracion:').grid(row=2,column=3,pady=5,padx=pad)
        if valoracion is None:
            valorac = 'N/C'
        else:
            valorac = round(valoracion,2)
        tk.Label(first_frame,text=valorac).grid(row=2,column=4,pady=5,padx=pad)
        tk.Label(first_frame,text='Fecha de Salida:').grid(row=3,column=0,pady=5,padx=pad)
        salida = tk.Label(first_frame,text=tiempo_salida)
        salida.grid(row=3,column=1,pady=5,padx=5)
        tk.Label(first_frame,text='Vehiculo:').grid(row=3,column=3,pady=5,padx=pad)
        tk.Label(first_frame,text=vehiculo).grid(row=3,column=4,pady=5,padx=pad)
        Botones = tk.Frame(first_frame,width=460,height=30)
        Botones.pack_propagate(False)
        Botones.grid(row=4,column=0,columnspan=5)
        reserva = tk.Button(Botones,text='Reservar')
        reserva.pack(side=tk.RIGHT,padx=40)
        reserva['command'] = lambda numero=numero :self.reserva(numero)
    def reserva(self,num):
        print(self.Viaje[num][-1])


    def DestinoSelection(self,event):
        self.partida = self.Partida.get()
        Destinos = ['-Todos-'] + self.conection.FiltrarViajes(self.partida)
        self.Destino['values'] = Destinos
        self.Destino.set(Destinos[0])
        self.PartidasSeleccion(None)
    def PartidasSeleccion(self,event):
        self.Viaje = self.conection.MostrarViajes(self.partida,self.Destino.get())
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.scrollable_frame.update()
        for Viaje, num in zip(self.Viaje, range(len(self.Travels))):
            self.CreateTravel(self.scrollable_frame, Viaje[0], Viaje[1], Viaje[2], Viaje[3], Viaje[4], Viaje[5],
                              Viaje[6], Viaje[7], Viaje[8], Viaje[9], Viaje[10], num)

