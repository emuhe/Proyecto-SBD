import tkinter as tk
from Menus.principal import MenuUsuario as MU
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(300,300)
        self.title('BlaBlaCar')
        self.label1 = tk.Label(self, text ='Bienvenido a BlaBlaCar!')
        self.label1.pack(pady=20)
        self.btn_is = tk.Button(self, text = 'Iniciar Sesion', command = self.InicioSesion)
        self.btn_is.pack(pady=20)
        self.btn_cc = tk.Button(self, text = 'Crear Cuenta', command = self.CrearCuenta)
        self.btn_cc.pack(pady=20)
        self.btn_quit = tk.Button(self, text="Cerrar", command=self.quit)
        self.btn_quit.pack(pady=20)

    def InicioSesion(self):
        self.destroy()
        IS = MU()
        IS.mainloop()
    def CrearCuenta(self):
        None

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()