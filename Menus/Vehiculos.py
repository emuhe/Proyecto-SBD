import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from SQL_conection.conector import Conection as CN

class Vehiculos:
    def __init__(self,ID):
        self.ID = ID
        self.rootCC = tk.Tk()
        self.Startup(self.rootCC)
        self.rootCC.mainloop()
    def Startup(self,rootCC):
        self.Car_count = 0
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
        self.conection = CN()
        self.ConseguirDatos()
        frame = tk.Frame(rootCC, relief= 'solid',width= 500, height= 200, bd= 1)
        frame.pack(pady=20,padx=20)
        frame.grid_propagate(False)
        self._text_cache = 'VEHICULO ' + str(self.Car_count+1)
        self.label0 = tk.Label(frame,text = 'VEHICULO 1')
        self.label0.grid(column=0,row=0,columnspan=5,pady=10)
        label1 = tk.Label(frame,text='PLACA:')
        label1.grid(column=0,row=1,padx=5,pady=5)
        self.placa = tk.Entry(frame)
        self.PlacaVar = tk.StringVar()
        self.PlacaVar.set(self.CarrosAct[5])
        self.placa.grid(column=1,row=1,padx=5,pady=5)
        self.placa['textvariable'] = self.PlacaVar
        self.placa.bind("<Key>", block_input)
        flab = tk.Label(frame, text='')
        flab.grid(column=2, row=1, padx=1,pady=5)
        label2 = tk.Label(frame,text='MARCA:')
        label2.grid(column=3,row=1,padx=10,pady=5)

        self.MarcaVar = tk.StringVar()
        self.MarcaVar.set(self.CarrosAct[1])

        self.marca = tk.Entry(frame)
        self.marca.grid(column=4, row=1,padx=5,pady=5)
        self.marca.insert(0, "Holder1")
        self.marca['textvariable'] = self.MarcaVar

        self.marca.bind("<Key>", block_input)

        label3 = tk.Label(frame, text='TIPO:')
        label3.grid(column=0,row=2,padx=5,pady=5)

        self.Tipo = tk.StringVar()
        self.Tipo.set(self.Carros[0][3])
        self.GComboBox = ttk.Combobox(frame)
        self.GComboBox['textvariable'] = self.Tipo
        self.GComboBox['values'] = ['SUV', 'Sedán', 'Camioneta', 'Deportivo', 'Crossover','Otro']
        self.GComboBox['state'] = 'disabled'
        self.GComboBox.grid(column = 1, row = 2, padx= 5, pady=10)

        label4 = tk.Label(frame, text = 'COLOR:')
        label4.grid(column=3,row=2,pady=5,padx=5)

        self.ColorVar = tk.StringVar()
        self.ColorVar.set(self.CarrosAct[4])

        self.Color = tk.Entry(frame)
        self.Color.grid(column=4, row=2, padx=5, pady=5)
        self.Color['textvariable'] = self.ColorVar
        self.Color.bind("<Key>", block_input)

        label5 = tk.Label(frame,text='F. MATRICULA:')
        label5.grid(column=0,row=3,padx=2,pady=5)

        self.Fmatricula = DateEntry(frame)
        self.Fmatricula['date_pattern'] = 'DD/MM/YYYY'
        self.Fmatricula['maxdate'] = date.today()
        self.Fmatricula.set_date(self.CarrosAct[2])
        self.Fmatricula.config(state='disable')
        self.Fmatricula.grid(column=1, row=3, padx=5, pady=5)

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
        self.label04 = tk.Label(frame, text='MODELO:')
        self.label04.grid(column=0, row=4)

        self.ModeloVar = tk.StringVar()
        self.ModeloVar.set(self.CarrosAct[0])
        self.Modelo = tk.Entry(frame)
        self.Modelo = tk.Entry(frame)
        self.Modelo.grid(column=1, row=4, padx=5)
        self.Modelo['textvariable'] = self.ModeloVar
        self.Modelo.bind("<Key>", block_input)


        frame3 = tk.Frame(frame,width=400,height=30)
        frame3.grid(column=0,row=5,columnspan=5)
        frame3.pack_propagate(False)
        self.Restablecer = tk.Button(frame3, text='Restablecer', width=10)
        self.Restablecer.config(state="disabled")
        self.Restablecer.pack(side = 'right',padx=5)
        self.Guardar = tk.Button(frame3, text = 'Guardar', width=10, command= self.Guardar,state='disabled')
        self.Guardar.pack(side = 'right',padx=5)

        frame2 = tk.Frame(rootCC)
        frame2.pack()
        label = tk.Label(frame2,text=' ').grid(column=0,row=0,padx=5)
        self.eliminaract = tk.Button(frame2)
        self.eliminaract['text'] = 'Eliminar'
        self.eliminaract['command'] = self.Delete
        self.eliminaract.grid(column=1,row=0,padx=5)
        self.editaract = tk.Button(frame2,text='Editar',command=self.Editar).grid(column=2, row=0,padx=5)
        self.nuevoact = tk.Button(frame2,text='Nuevo',command=self.Crear).grid(column=3, row=0, padx=5)
        tk.Label(frame2,text=' ').grid(column=4,row=0,padx=50)
        self.botlef = tk.Button(frame2,text='<-',command=self.Atras)
        self.botlef.grid(column=5,row=0,padx=1)
        self.botrig = tk.Button(frame2,text='->',command=self.Siguiente)
        self.botrig.grid(column=6, row=0, padx=1)

    def Elimiar(self):
        self.PlacaVar.set('')
        self.ColorVar.set('')
        self.MarcaVar.set('')
        self.ModeloVar.set('')
        self.Fmatricula.set_date(date.today())
    def Editar(self):
        self._cache = False
        self.PermitirMod()
    def PermitirMod(self):
        self.placa.unbind('<Key>')
        self.Color.unbind('<Key>')
        self.marca.unbind('<Key>')
        self.Modelo.unbind('<Key>')
        self.Fmatricula.config(state='active')
        self.GComboBox.config(state = 'active')
        self.editaract.config(state="disabled")
        self.nuevoact.config(state="disabled")
        self.eliminaract.config(state="disabled")
        self.botlef.config(state="disabled")
        self.botrig.config(state="disabled")
        self.Restablecer.config(state="active")
        self.Guardar.config(state="active")
    def Guardar(self):

        def block_input(event):
            return "break"
        self.GComboBox.config(state = 'disabled')
        self.Fmatricula.config(state='disabled')
        self.editaract.config(state='active')
        self.Guardar.config(state="disabled")
        self.Restablecer.config(state="disabled")
        self.nuevoact.config(state="active")
        self.eliminaract.config(state="active")
        self.botlef.config(state="active")
        self.botrig.config(state="active")
        self.Modelo.bind("<Key>", block_input)
        self.placa.bind("<Key>", block_input)
        self.Color.bind("<Key>", block_input)
        self.marca.bind("<Key>", block_input)
        if self._cache:
            datos = [0, self.ModeloVar.get(), self.MarcaVar.get(), self.Fmatricula.get_date(), self.Tipo.get(),
                     self.ColorVar.get(), self.PlacaVar.get(), 1]
            self.conection.AutosCrear(datos,self.ID)
        else:
            edited_data = [self.ModeloVar.get(), self.MarcaVar.get(), self.Fmatricula.get_date(), self.Tipo.get(),
                     self.ColorVar.get(), self.PlacaVar.get(), self.CarrosAct[7]]
            self.conection.AutoEditar(edited_data)
        self.ConseguirDatos()

    def Crear(self):
        self.PermitirMod()
        self._cache = True
        self.Elimiar()

    def Atras(self):
        if self.Car_count-1 > -1:
            if self.botrig.cget('state') == 'disabled':
                self.botrig.config(state='active')
            #SELECT v.MODELO,v.MARCA,v.FECHA_MATRICULA,v.TIPO_VEHICULO,v.COLOR,v.PLACA,v.ACTIVO,v.ID FROM VEHICULO V JOIN vehicul
            self.Car_count -= 1
            self._text_cache = 'VEHICULO ' + str(self.Car_count + 1)
            self.label0.config(text=self._text_cache)
            self.CarrosAct = self.Carros[self.Car_count]
            self.ModeloVar.set(self.CarrosAct[0])
            self.MarcaVar.set(self.CarrosAct[1])
            self.Fmatricula.config(state='active')
            self.Fmatricula.set_date(self.CarrosAct[2])
            self.Fmatricula.config(state='disabled')

            self.Tipo.set(self.CarrosAct[3])
            self.ColorVar.set(self.CarrosAct[4])
            self.PlacaVar.set(self.CarrosAct[5])
            if self.Car_count-1 == -1:
                self.botlef.config(state='disabled')
        else: self.botlef.config(state='disabled')
    def Siguiente(self):
        if self.Car_count+1 < self.CantCarr:
            if self.botlef.cget('state') == 'disabled':
                self.botlef.config(state='active')
            #SELECT v.MODELO,v.MARCA,v.FECHA_MATRICULA,v.TIPO_VEHICULO,v.COLOR,v.PLACA,v.ACTIVO,v.ID FROM VEHICULO V JOIN vehicul
            self.Car_count += 1
            self._text_cache = 'VEHICULO ' + str(self.Car_count + 1)
            self.label0.config(text=self._text_cache)
            self.CarrosAct = self.Carros[self.Car_count]
            self.ModeloVar.set(self.CarrosAct[0])
            self.MarcaVar.set(self.CarrosAct[1])
            self.Fmatricula.config(state='active')
            self.Fmatricula.set_date(self.CarrosAct[2])
            self.Fmatricula.config(state='disabled')
            self.Tipo.set(self.CarrosAct[3])
            self.ColorVar.set(self.CarrosAct[4])
            self.PlacaVar.set(self.CarrosAct[5])
            if self.Car_count+1 == self.CantCarr:
                self.botrig.config(state='disabled')
        else: self.botrig.config(state='disabled')

    def ConseguirDatos(self):
        self.Carros = self.conection.Autos(self.ID)
        self.CantCarr = len(self.Carros)

        if self.CantCarr == 0:
            self.Carros.append(['','',date.today(),'','','','',''])
        self.CarrosAct = self.Carros[0]
        self.CantCarr = len(self.Carros)

    def Delete(self):
        if self.CantCarr == 0:
            None
        else:
            self.conection.EliminarAuto(self.CarrosAct[-1])
            self.ConseguirDatos()