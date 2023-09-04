import tkinter as tk
from tkinter import ttk
from SQL_conection.conector import Conection as CN
from datetime import date,datetime,timedelta
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
        self.f_partida = tk.Entry(frame,width=20)
        tk.Label(frame, text='Punto de Partida:').grid(row=1, column=0, pady=5, padx=pad)
        self.f_partida.grid(row=1, column=1, pady=pady, padx=pad)
        tk.Label(frame, text='Punto de Llegada:').grid(row=1, column=3, pady=5, padx=pad)
        self.f_llegada = tk.Entry(frame,width=15)
        self.f_llegada.grid(row=1, column=4, pady=pady, padx=pad)
        tk.Label(frame, text='Asientos disponibles:').grid(row=2, column=0, pady=pady, padx=pad)
        self.f_pasajeros = tk.Spinbox(frame, from_=0, to_=10, width=5, format="%02.0f",state='readonly')
        self.f_pasajeros.grid(row=2, column=1, padx=pad, pady=pady)
        tk.Label(frame, text='P. por asiento:').grid(row=2, column=3, pady=pady, padx=pad)
        self.f_precio = tk.Entry(frame,validate='key',width=10)
        self.f_precio.insert(0, '00.00')
        self.f_precio.bind('<FocusIn>', self.on_entry_click)
        self.f_precio.bind('<FocusOut>',self.out_focus)
        self.f_precio['validate'] = "key"
        self.f_precio['validatecommand'] = (self.validate_cmd,'%S', '%P')
        self.f_precio.place(x=300, y=215, width=130, height=30)
        self.f_precio.grid(row=2, column=4, pady=5, padx=pad)
        tk.Label(frame, text='Fecha de Salida:').grid(row=3, column=0, pady=pady, padx=pad)
        tiempoframe = tk.Frame(frame)
        tiempoframe.grid(row=3, column=1, pady=pady, padx=pady)
        self.FechaSalida = DateEntry(tiempoframe, width=8,state='readonly')
        self.FechaSalida['date_pattern'] = 'DD/MM/YY'
        self.FechaSalida['mindate'] = date.today() + timedelta(days=1)
        self.FechaSalida.set_date(date.today())
        self.FechaSalida.grid(row=0, column=0)

        self.ObtenerAutos(self.user_id)

        self.hour_spinbox = tk.Spinbox(tiempoframe, from_=0, to_=23, width=3, format="%02.0f",state='readonly')
        self.hour_spinbox.grid(row=0, column=1)
        self.minute_spinbox = tk.Spinbox(tiempoframe, from_=0, to_=55, width=3, format="%02.0f",state='readonly',increment=5)
        self.minute_spinbox.grid(row=0, column=2)

        tk.Label(frame, text='Vehiculo:').grid(row=3, column=3, pady=pady, padx=pad)
        self.Vehiculos = ttk.Combobox(frame,values=[self.format_plate(plate) for plate in self.NombresAutos],width=15,state='readonly')
        self.Vehiculos.grid(row=3, column=4, pady=pady, padx=pad)
        self.Vehiculos.bind("<<ComboboxSelected>>", self.conseguirVehiculo)

        Botones = tk.Frame(frame, width=460, height=30)
        Botones.pack_propagate(False)
        Botones.grid(row=4, column=0, columnspan=5)
        crear = tk.Button(Botones, text='Crear Viaje',command=self.CrearV)

        crear.pack(side=tk.RIGHT, padx=40)

    def num_validation(self,char,value):
        if value == '00.00' or '':
            return True

        if not char.isdigit() and char != ".":
            return False

        if char == "." and value.count(".") > 1:
            return False

        if "." in value:
            int_part, dec_part = value.split(".")
            if len(dec_part) > 2:
                return False
        return True
    def ObtenerAutos(self,user_id):
        self.NombresAutos = self.conection.placas(user_id)
        print(self.NombresAutos)

    def format_plate(self,plate):
        return plate[:-4] + '-' + plate[-4:]

    def CrearV(self):

        self.conseguirVehiculo(None)
        tiempo = datetime.combine(self.FechaSalida.get_date(),datetime.min.time()).replace(hour=int(self.hour_spinbox.get()),minute=int(self.minute_spinbox.get()))
        datos = [self.user_id,self.selected,int(self.f_pasajeros.get()),float(self.f_precio.get()),self.f_partida.get(),self.f_llegada.get(),tiempo]#usuario_id,placa,cantidad,precio,partida,llegada,tiempo
        if '' not in datos or datos[2] > 0:
            self.conection.CrearViaje(datos)
    def conseguirVehiculo(self,event):
        self.selected = self.Vehiculos.get().replace('-', '')
    def on_entry_click(self,event):
        self.f_precio.configure(validate='none')
        if self.f_precio.get() == '00.00':
            self.f_precio.delete(0, tk.END)
        self.f_precio.configure(validate='key', validatecommand= (self.validate_cmd, '%S','%P'))
    def out_focus(self,event):
        print('out')
        if not self.f_precio.get():
            self.f_precio.insert(0,'00.00')