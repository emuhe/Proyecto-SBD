import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from SQL_conection.conector import Conection as CN

class MetodosPago:
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
        self.rootCC.title("BlaBlaCar - Metodos de pago")
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

        self.validate_cmd = self.rootCC.register(self.num_validation)
        frame = tk.Frame(rootCC, relief= 'solid',width= 500, height= 220, bd= 1)
        frame.pack(pady=20,padx=20)
        frame.grid_propagate(False)
        self.label0 = tk.Label(frame,text = 'TARJETA DE CREDITO')
        self.label0.grid(column=0,row=0,columnspan=5,pady=10)
        label1 = tk.Label(frame,text='NUMERO TARJETA:')
        label1.grid(column=0,row=1,padx=5,pady=5)
        self.Tarjeta = tk.Entry(frame,width=50)
        self.NTarjeta = tk.StringVar()
        self.Tarjeta.grid(columnspan=4,column=1,row=1,padx=5,pady=5)
        self.Tarjeta['validatecommand'] = (self.validate_cmd,'%P',16)
        self.Tarjeta['textvariable'] = self.NTarjeta
        self.Tarjeta.bind("<Key>", block_input)
        self.Tarjeta['validate'] = 'key'

        label3 = tk.Label(frame, text='NOMBRE TITULAR:')
        label3.grid(column=0,row=2,padx=5,pady=5)

        self.Titular = tk.StringVar()
        self.Titu = tk.Entry(frame,width=50)
        self.Titu['textvariable'] = self.Titular
        self.Titu.bind("<Key>", block_input)
        self.Titu.grid(column = 1,columnspan=4, row = 2, padx= 5, pady=10)

        label5 = tk.Label(frame,text='F. MATRICULA:')
        label5.grid(column=0,row=3,padx=2,pady=5)


        self.mes = tk.StringVar()
        self.mesbox = ttk.Combobox(frame, width=10)
        self.mesbox['textvariable'] = self.mes
        self.mesbox['values'] = ['1','2','3','4','5','6','7','8','9','10','11','12']
        self.mesbox.config(state='disable')
        self.mesbox.grid(column=1, row=3, padx=5, pady=5)

        self.year = tk.StringVar()

        self.yearbox = ttk.Combobox(frame, width=10)
        self.yearbox['textvariable'] = self.year
        self.yearbox['values'] = ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034']
        self.yearbox.config(state='disable')

        self.yearbox.grid(column=2, row=3, padx=5, pady=5)

        label6 = tk.Label(frame,text='CCV:')
        label6.grid(column=0,row=4,padx=5,pady=5)
        self.CCV = tk.StringVar()
        self.CCVentry = tk.Entry(frame)
        self.CCVentry.grid(column=1, row=4, padx=5)
        self.CCVentry['textvariable'] = self.CCV
        self.CCVentry['validate'] = 'key'
        self.CCVentry.bind("<Key>", block_input)
        self.CCVentry['validatecommand'] = (self.validate_cmd,'%P',4)

        frame3 = tk.Frame(frame,width=400,height=30)
        frame3.grid(column=0,row=5,columnspan=5)
        frame3.pack_propagate(False)
        self.editaract = tk.Button(frame3, text='Editar', width=10)
        self.editaract['command'] = self.Editar

        self.editaract.pack(side = 'right',padx=5)
        self.Guardar = tk.Button(frame3, text = 'Guardar', width=10, command= self.Guardar)
        self.Guardar.config(state="disabled")
        self.Guardar.pack(side = 'right',padx=5)
        self.AddValues()

    def Elimiar(self):
        self.ColorVar.set('')
        self.ModeloVar.set('')
        self.Fmatricula.set_date(date.today())
    def Editar(self):
        self._cache = False
        self.PermitirMod()
    def PermitirMod(self):
        self.Tarjeta.unbind('<Key>')
        self.Titu.unbind('<Key>')
        self.mesbox.config(state='readonly')
        self.yearbox.config(state = 'readonly')
        self.CCVentry.unbind('<Key>')
        self.Guardar.config(state="active")
    def Guardar(self):

        def block_input(event):
            return "break"
        self.editaract.config(state='active')
        self.Guardar.config(state="disabled")
        self.Tarjeta.bind("<Key>", block_input)
        self.Titu.bind("<Key>", block_input)
        self.CCVentry.bind("<Key>", block_input)
        self.mesbox.config(state='disable')
        self.yearbox.config(state='disable')
        if self._cache:
            datos = [self.NTarjeta.get(), self.Titular.get(), self.CCV.get(), self.mes.get(),
                     self.year.get(),self.id_tarjeta]
            print('editar')
            print(datos)
            self.conection.CrearTarjeta(datos)
        self.ConseguirDatos()
    def ConseguirDatos(self):
        #INSERT INTO tarjeta_credito (id,nombre_titular,fecha_expiracion,numero_tarjeta,codigo_ccv) VALUES (%s,%s,%s,%s,%s)",(0,None,None,None,'000'))
        #'tc.nombre_titular,tc.MONTH(fecha_expiracion) AS month, tc.YEAR(fecha_expiracion) AS year,tc.numero_tarjeta,tc.codigo_ccv
        self.user_tarjeta,self.id_tarjeta = self.conection.TarjetaCredit(self.ID)
        if self.user_tarjeta[0] == None:
            self.user_tarjeta = ['','','','','']
        print(self.user_tarjeta)
    def num_validation(self,P,x):
        if (P.isdigit() or P == "") and len(P) <= int(x):
            return True
        return False
    def AddValues(self):
        self.NTarjeta.set(self.user_tarjeta[3])
        self.Titular.set(self.user_tarjeta[0])
        self.CCV.set(self.user_tarjeta[4]),
        self.mes.set(str(self.user_tarjeta[1]))
        self.year.set(str(self.user_tarjeta[2]))