import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root2):
        #setting title
        root.title("undefined")
        #setting window size
        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_963=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_963["font"] = ft
        GLabel_963["fg"] = "#333333"
        GLabel_963["justify"] = "center"
        GLabel_963["text"] = "Nombre:"
        GLabel_963.place(x=30,y=60,width=71,height=31)

        GLineEdit_554=tk.Entry(root)
        GLineEdit_554["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_554["font"] = ft
        GLineEdit_554["fg"] = "#333333"
        GLineEdit_554["justify"] = "center"
        GLineEdit_554["text"] = ""
        GLineEdit_554.place(x=100,y=60,width=130,height=30)

        GLabel_6=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_6["font"] = ft
        GLabel_6["fg"] = "#333333"
        GLabel_6["justify"] = "center"
        GLabel_6["text"] = "Apellido:"
        GLabel_6.place(x=230,y=60,width=72,height=30)

        GLineEdit_531=tk.Entry(root)
        GLineEdit_531["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_531["font"] = ft
        GLineEdit_531["fg"] = "#333333"
        GLineEdit_531["justify"] = "center"
        GLineEdit_531["text"] = ""
        GLineEdit_531.place(x=300,y=60,width=131,height=30)

        GLabel_426=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "center"
        GLabel_426["text"] = "Correo:"
        GLabel_426.place(x=30,y=110,width=72,height=35)

        GLineEdit_983=tk.Entry(root)
        GLineEdit_983["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_983["font"] = ft
        GLineEdit_983["fg"] = "#333333"
        GLineEdit_983["justify"] = "center"
        GLineEdit_983["text"] = ""
        GLineEdit_983.place(x=100,y=110,width=331,height=30)

        GLabel_842=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_842["font"] = ft
        GLabel_842["fg"] = "#333333"
        GLabel_842["justify"] = "center"
        GLabel_842["text"] = "Fecha de Nacimiento:"
        GLabel_842.place(x=30,y=150,width=135,height=45)

        GListBox_731=tk.Listbox(root)
        GListBox_731["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_731["font"] = ft
        GListBox_731["fg"] = "#333333"
        GListBox_731["justify"] = "center"
        GListBox_731.place(x=160,y=160,width=55,height=30)
        GListBox_731["exportselection"] = "0"
        GListBox_731["listvariable"] = "Dia"
        GListBox_731["selectmode"] = "single"
def Execute():
    print('mex')
    if __name__ == "__main__":
        print('execute')
        root2 = tk.Tk()
        app = App(root2)
        root2.mainloop()
