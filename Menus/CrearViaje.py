import tkinter as tk
from tkinter import ttk
from SQL_conection.conector import Conection as CN
from datetime import date
from tkcalendar import DateEntry


class MisViajes:
    def __init__(self,user_id):
        self.user_id = user_id
        self.conection = CN()
        self.rootBV = tk.Tk()
        self.Startup(self.rootBV)
        self.rootBV.mainloop()
        self.conection.CerrarConeccion()
    def Startup(self,root):
        scroll_max = 3 * 180

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
        CrearViaje = tk.Frame(root, width=495, height=150,bd= 1,relief= 'solid')
        CrearViaje.grid_propagate(False)
        CrearViaje.pack(pady= 10)
        self.CrearViajes(CrearViaje)
    def CrearViajes(self,frame):
        self.validate_cmd = frame.register(self.num_validation)
        tk.Label(frame,text = 'Crear Viaje').grid(column = 0, row = 0, columnspan = 5)
        pad = 1
        pady = 6
        f_partida = tk.Entry(frame)
        tk.Label(frame, text='Punto de Partida:').grid(row=1, column=0, pady=5, padx=pad)
        f_partida.grid(row=1, column=1, pady=pady, padx=pad)
        tk.Label(frame, text='Punto de Llegada:').grid(row=1, column=3, pady=5, padx=pad)
        f_llegada = tk.Entry(frame)
        f_llegada.grid(row=1, column=4, pady=pady, padx=pad)
        tk.Label(frame, text='Asientos disponibles:').grid(row=2, column=0, pady=pady, padx=pad)
        f_pasajeros = tk.Entry(frame)
        f_pasajeros.grid(row=2, column=1, padx=pad, pady=pady)
        tk.Label(frame, text='P. por asiento:').grid(row=2, column=3, pady=pady, padx=pad)
        f_precio = tk.Entry(frame,validate='key')
        f_precio['validate'] = "key"
        f_precio['validatecommand'] = (self.validate_cmd,'%S', '%P')
        f_precio.place(x=300, y=215, width=130, height=30)
        f_precio.grid(row=2, column=4, pady=5, padx=pad)
        tk.Label(frame, text='Fecha de Salida:').grid(row=3, column=0, pady=pady, padx=pad)
        tiempoframe = tk.Frame(frame)
        tiempoframe.grid(row=3, column=1, pady=pady, padx=pady)
        self.FechaSalida = DateEntry(tiempoframe, width=8,state='readonly')
        self.FechaSalida['date_pattern'] = 'DD/MM/YY'
        self.FechaSalida['mindate'] = date.today()
        self.FechaSalida.set_date(date.today())
        self.FechaSalida.grid(row=0, column=0)


        hour_spinbox = tk.Spinbox(tiempoframe, from_=0, to_=23, width=3, format="%02.0f",state='readonly')
        hour_spinbox.grid(row=0, column=1)
        minute_spinbox = tk.Spinbox(tiempoframe, from_=0, to_=59, width=3, format="%02.0f",state='readonly')
        minute_spinbox.grid(row=0, column=2)
        tk.Label(frame, text='Vehiculo:').grid(row=3, column=3, pady=pady, padx=pad)
        tk.Entry(frame).grid(row=3, column=4, pady=pady, padx=pad)
        Botones = tk.Frame(frame, width=460, height=30)
        Botones.pack_propagate(False)
        Botones.grid(row=4, column=0, columnspan=5)
        crear = tk.Button(Botones, text='Crear Viaje')
        crear.pack(side=tk.RIGHT, padx=40)

    def num_validation(self,char,value):
        if not char.isdigit() and char != ".":
            return False

            # Only allow one decimal point in the input.
        if char == "." and value.count(".") > 1:
            return False

        if "." in value:
            int_part, dec_part = value.split(".")
            if len(dec_part) > 2:
                return False
        return True