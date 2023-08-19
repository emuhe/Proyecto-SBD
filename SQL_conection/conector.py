import mysql.connector

class Conection:
    def __init__(self):
        self.conection = mysql.connector.connect(
            host="proyecto-blablacar.mysql.database.azure.com",
            user="blablacar",
            password="Bl@bl4c4r",
            database="blablacar"
            )
    def recopilar_viajes(self):
        query = ''

    def Cuentacrear(self,datos):
        #nombre,apellido,correo,genero,direccion,ID,telefono,fecha-nac
        print(datos)
        cursor = self.conection.cursor()
        cursor.execute("INSERT INTO dates (nombre,apellido,correo_electronico,genero,cedula,numero_movil,fecha_nacimiento) VALUES (?)", datos)
