import mysql.connector

class Conection:
    def __init__(self):
        conection = mysql.connector.connect(
            host="proyecto-blablacar.mysql.database.azure.com",
            user="blablacar",
            password="Bl@bl4c4r",
            database="blablacar"
            )
