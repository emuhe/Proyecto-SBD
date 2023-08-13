import tkinter as tk
import tkinter.font as tkFont
from Menus.principal import MenuUsuario as MU
class MainMenu:
    def __init__(self,root):
        # setting title
        root.title("BlaBlaCar")
        # setting window size
        width = 498
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_551 = tk.Label(root)
        GLabel_551["anchor"] = "n"
        ft = tkFont.Font(family='Times', size=28)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = "Bienvenido a BlaBlaCar!"
        GLabel_551.place(x=50, y=40, width=373, height=47)

        GButton_760 = tk.Button(root)
        GButton_760["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_760["font"] = ft
        GButton_760["fg"] = "#000000"
        GButton_760["justify"] = "center"
        GButton_760["text"] = "Ingresar"
        GButton_760.place(x=160, y=260, width=120, height=30)
        GButton_760["command"] = self.GButton_760_command

        GLabel_238 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_238["font"] = ft
        GLabel_238["fg"] = "#333333"
        GLabel_238["justify"] = "center"
        GLabel_238["text"] = "Usuario:"
        GLabel_238.place(x=70, y=130, width=104, height=32)

        GLabel_410 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_410["font"] = ft
        GLabel_410["fg"] = "#333333"
        GLabel_410["justify"] = "center"
        GLabel_410["text"] = "Contraseña:"
        GLabel_410.place(x=40, y=190, width=130, height=33)

        GLineEdit_742 = tk.Entry(root)
        GLineEdit_742["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_742["font"] = ft
        GLineEdit_742["fg"] = "#333333"
        GLineEdit_742["justify"] = "center"
        GLineEdit_742["text"] = ""
        GLineEdit_742.place(x=210, y=130, width=179, height=31)

        GLineEdit_325 = tk.Entry(root)
        GLineEdit_325["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_325["font"] = ft
        GLineEdit_325["fg"] = "#333333"
        GLineEdit_325["justify"] = "center"
        GLineEdit_325["text"] = ""
        GLineEdit_325.place(x=210, y=190, width=179, height=30)

        GLabel_803 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_803["font"] = ft
        GLabel_803["fg"] = "#000000"
        GLabel_803["justify"] = "center"
        GLabel_803["text"] = "Todavia no tiene una cuenta?"
        GLabel_803.place(x=130, y=300, width=176, height=30)

        GButton_748 = tk.Button(root)
        GButton_748["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_748["font"] = ft
        GButton_748["fg"] = "#000000"
        GButton_748["justify"] = "center"
        GButton_748["text"] = "Crear Cuenta"
        GButton_748.place(x=160, y=330, width=120, height=30)
        GButton_748["command"] = self.GButton_748_command

    def GButton_760_command(self):
        print("command")

    def GButton_748_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()