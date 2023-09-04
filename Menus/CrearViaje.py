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
        botones = tk.Frame(root,width=500,height=40)
        botones.pack_propagate(False)
        botones.pack()
        Opt1 = tk.Button(botones,text='Viajes Creados')
        Opt1.pack(pady=5,padx=30,side ='left',anchor = 'center',expand = True)
        Opt2 = tk.Button(botones,text='Viajes Unidos')
        Opt2.pack(pady=5,padx=30,side ='left',anchor = 'center',expand = True)
        canvas = tk.Canvas(root, bd=0, highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scroll = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=v_scroll.set)
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: on_frame_configure(canvas))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.ViajesUnidos()
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
        if len(self.NombresAutos) == 0:
            crear['state'] = 'disabled'
        crear.pack(padx=5,anchor = 'center')
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
    def CreateTravel(self,root,Nombre,Apellido,partida,llegada,pasajeros,asientos,precio,tiempo_salida,estado,valoracion,vehiculo):
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
            cant_pasajeros = str(asientos-pasajeros)+'/'+str(asientos)+' DISPONIBLES'
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
        tk.Label(first_frame,text='Estado:').grid(row=4,column=0,pady=5,padx=pad)
        if estado == 0:
            textado = 'En progreso'
        else:
            textado = 'Finalizado'
        tk.Label(first_frame,text = textado).grid(row=4,column=1,pady=5,padx=pad)

    def ViajesUnidos(self):
        self.Valores = self.conection.ViajesUnidos(self.user_id)
        for Viaje in self.Valores:
            self.CreateTravel(self.scrollable_frame, Viaje[0], Viaje[1], Viaje[2], Viaje[3], Viaje[4], Viaje[5],
                              Viaje[6], Viaje[7], Viaje[8], Viaje[9], Viaje[10])