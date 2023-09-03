import tkinter as tk
from tkinter import ttk
from SQL_conection.conector import Conection as CN

class MisViajes:
    def __init__(self,user_id):
        self.user_id = user_id
        self.conection = CN()
        self.rootBV = tk.Tk()
        self.Startup(self.rootBV)
        self.rootBV.mainloop()
        self.conection.CerrarConeccion()
    def Startup(self,root):
        scroll_max = len(150) * 180

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
        Filtros = tk.Frame(root, width=500, height=100)
        Filtros.pack_propagate(False)
        Filtros.pack()
