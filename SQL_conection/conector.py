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
        print(datos)
        cursor = self.conection.cursor()
        cursor.execute("INSERT INTO tarjeta_credito (id,nombre_titular,fecha_expiracion,numero_tarjeta,codigo_ccv) VALUES (%s,%s,%s,%s,%s)",(0,None,None,None,'000'))
        cursor.execute("INSERT INTO usuario (id,nombre,apellido,preferencia,ruta_foto,perfil,minibiografia,cedula,genero,direccion,fecha_nacimiento,numero_movil,rol,correo_electronico,cuenta_banco_id,tarjeta_credito_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", datos)

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
            return True,resultado[0]
    def Autos(self,ID):
        cursor = self.conection.cursor()
        cursor.execute('SELECT v.MODELO,v.MARCA,v.FECHA_MATRICULA,v.TIPO_VEHICULO,v.COLOR,v.PLACA,v.ACTIVO,v.ID FROM VEHICULO V JOIN vehiculo_conductor vd on v.id = vd.vehiculo_id where vd.conductor_id = %s', (ID,))
        datos = cursor.fetchall()
        cursor.close()
        return datos
