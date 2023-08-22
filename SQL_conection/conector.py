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
    def recopilar_viajes(self):
        query = ''

    def Cuentacrear(self,datos):
        print(datos)
        cursor = self.conection.cursor()
        cursor.execute("INSERT INTO tarjeta_credito (id,nombre_titular,fecha_expiracion,numero_tarjeta,codigo_ccv) VALUES (%s,%s,%s,%s,%s)",(0,None,None,None,'000'))
        Tarjet_credit = cursor.lastrowid
        cursor.execute("INSERT INTO cuenta_bancaria (id,numero_cuenta,titular_cuenta,cedula_titular) VALUES (%s,%s,%s,%s)",(0,'000000000','000000000','000000000'))
        Cuenta_ban = cursor.lastrowid
        datos.append(Cuenta_ban)
        datos.append(Tarjet_credit)
        cursor.execute("INSERT INTO usuario (id,nombre,apellido,preferencia,ruta_foto_perfil,minibiografia,cedula,genero,direccion,fecha_nacimiento,numero_movil,rol,correo_electronico,cuenta_banco_id,tarjeta_credito_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", datos)
        user_id = cursor.lastrowid
        self.conection.commit()
        cursor.close()
        return user_id
    def EditarCuenta(self,datos):
        cursor = self.conection.cursor()
        print(datos)
        cursor.execute(
            "UPDATE usuario SET nombre = %s,apellido= %s,preferencia= %s,minibiografia= %s,cedula= %s,genero= %s,direccion= %s,fecha_nacimiento= %s,numero_movil= %s,correo_electronico= %s where id = %s",
            datos)
        self.conection.commit()
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
    def AutosCrear(self,data,id):
        cursor = self.conection.cursor()
        cursor.execute('INSERT INTO VEHICULO (id,modelo,marca,fecha_matricula,tipo_vehiculo,color,placa,activo) values (%s,%s,%s,%s,%s,%s,%s,%s)', data)
        veh_id = cursor.lastrowid
        cursor.execute('INSERT INTO VEHICULO_CONDUCTOR (id,vehiculo_id,conductor_id) values (%s,%s,%s)',(0,veh_id,id))
        self.conection.commit()
        cursor.close()
    def AutoEditar(self,data):
        cursor = self.conection.cursor()
        cursor.execute('UPDATE VEHICULO SET modelo = %s, marca = %s, FECHA_MATRICULA = %s, TIPO_VEHICULO = %s, color = %s, placa = %s where id = %s', data)
        self.conection.commit()
        cursor.close()
    def EliminarAuto(self,id):
        cursor = self.conection.cursor()
        cursor.execute('DELETE FROM vehiculo_conductor where vehiculo_id = %s',(id,))
        cursor.execute('DELETE FROM vehiculo WHERE id = %s', (id,))
        self.conection.commit()

    def ConsultarDatosUser(self,user_id):
        cursor = self.conection.cursor()
        print(user_id)
        cursor.execute('SELECT nombre,apellido,preferencia,minibiografia,cedula,genero,direccion,fecha_nacimiento,numero_movil,correo_electronico from usuario where id = %s', (user_id,))
        values = cursor.fetchone()
        cursor.close()
        return values
    def TarjetaCredit(self,user_id):
        cursor = self.conection.cursor()
        cursor.execute(
            'Select tc.nombre_titular,MONTH(tc.fecha_expiracion) AS month, YEAR(tc.fecha_expiracion) AS year,tc.numero_tarjeta,tc.codigo_ccv from tarjeta_credito tc join usuario u on u.tarjeta_credito_id = tc.id where u.id = %s',
                       (user_id,))
        tarjeta = cursor.fetchone()
        cursor.execute('select tarjeta_credito_id from usuario u where u.id = %s',(user_id,))
        id_tar = cursor.fetchone()
        cursor.close()
        return tarjeta,id_tar
    def CrearTarjeta(self,values):
        cursor = self.conection.cursor()
        cursor.execute(
            'UPDATE tarjeta_credito SET numero_tarjeta = %s,nombre_titular = %s,codigo_ccv = %s, fecha_expiracion = %s where id = %s',
            values)
        self.conection.commit()
        cursor.close()
    def CuentaEditar(self,values):
        cursor = self.conection.cursor()
        cursor.execute(
            'UPDATE cuenta_bancaria SET numero_cuenta = %s,titular_cuenta = %s,cedula_titular = %s where id = %s',
            values)
        self.conection.commit()
        cursor.close()
    def CuentaDatos(self,user_id):
        cursor = self.conection.cursor()
        cursor.execute(
            'Select cb.numero_cuenta,cb.titular_cuenta,cb.cedula_titular from cuenta_bancaria cb join usuario u on u.cuenta_banco_id = cb.id where u.id = %s',
            (user_id,))
        cuenta = cursor.fetchone()
        cursor.execute('select cuenta_banco_id from usuario u where u.id = %s', (user_id,))
        id_cut = cursor.fetchone()
        cursor.close()
        return cuenta, id_cut