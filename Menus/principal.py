import tkinter as tk
class MenuUsuario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesion")
        self.minsize(300,300)

        tk.Label(self, text="Inicio de Sesion").pack(pady=20)