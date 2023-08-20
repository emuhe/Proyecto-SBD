import mysql.connector


class Conection:
    def __init__(self):
        a = open('datos_sensibles/sqlcontra.txt')
        data = []
        for i in a:
            data.append(i.strip())
        a.close()
        self.conection = mysql.connector.connect(
            host="proyecto-blablacar.mysql.database.azure.com",
            user=data[0],
            password=data[1],
            database="blablacar"
            )
        data = None
    def recopilar_viajes(self):
        query = ''

    def Cuentacrear(self,datos):
        #nombre,apellido,correo,genero,direccion,ID,telefono,fecha-nac
        print(datos)
        cursor = self.conection.cursor()
        cursor.execute("INSERT INTO usuario VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", datos)
        cursor.close()
    def InicioSesion(self,ID,NOMBRE):
        cursor = self.conection.cursor()
        cursor.execute('SELECT id,nombre from usuario where cedula = %s and nombre = %s', (ID,NOMBRE))
        resultado = cursor.fetchone()
        print(resultado)
        cursor.close()
        if resultado == None:
            return False,None
        else:
            return True,ID
    def Autos(self,ID):
        print(ID)
        cursor = self.conection.cursor()
        cursor.execute('SELECT v.MODELO,v.MARCA,v.FECHA_MATRICULA,v.TIPO_VEHICULO,v.COLOR,v.PLACA,v.ACTIVO FROM VEHICULO V JOIN vehiculo_conductor vd on v.id = vd.vehiculo_id JOIN usuario u on u.id = vd.conductor_id where u.cedula = %s', (ID,))
        datos = cursor.fetchall()
        cursor.close()
        return datos
