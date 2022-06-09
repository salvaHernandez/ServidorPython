import pymysql
import json

from Constantes import *
#La librería se instala con el comando: pip install pymysql
class Conexion:
    
    def __init__(self, usuario, passw, bd):
        self._usuario = usuario
        self._passw = passw
        self._bd = bd
        try:
            #Abrimos y cerramos la bd para dos cosas: comprobar que los datos de conexión son correctos y
            #dar el tipo adecuado a la variable self._conexion.
            self._conexion = pymysql.connect(host='localhost',
                                    user=self._usuario,
                                    password=self._passw,
                                    db=self._bd)
            self._conexion.close()
            print("Datos de conexión correctos.")
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error con los datos de conexión: ", e)
        
         
    def conectar(self):
        """Devuelve la variable conexion o -1 si la conexión no ha sido correcta."""
        try:
            self._conexion = pymysql.connect(host='localhost',
                                    user=self._usuario,
                                    password=self._passw,
                                    db=self._bd)
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return -1

    def cerrarConexion(self):
        self._conexion.close()
        
        

    #https://www.programcreek.com/python/example/104689/sklearn.datasets.fetch_20newsgroups
    #https://stackoverflow.com/questions/11280382/object-is-not-json-serializable
    def buscarUsuario(self, name):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT nombre, idRol, pass FROM usuario WHERE nombre = %s", (name))
#                cursor.execute("SELECT "+ID_USUARIO+","+ID_ROL+","+NOMBRE_USUARIO+","+PASS_USUARIO+" FROM "+TABLA_USUARIO+" WHERE "+NOMBRE_USUARIO+" = %s", (name))

                r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
                print(r)
                
                self.cerrarConexion()                
                
                if (r):
                    return r[0]
                else:
                    return []
                
                
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []



    def estadoEncuesta(self, name):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT * FROM "+TABLA_ESTADO_ENCUESTA+" WHERE "+NOMBRE_ENC+" = %s", (name))
#                cursor.execute("SELECT "+ID_USUARIO+","+ID_ROL+","+NOMBRE_USUARIO+","+PASS_USUARIO+" FROM "+TABLA_USUARIO+" WHERE "+NOMBRE_USUARIO+" = %s", (name))

                r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
                print(r)
                
                self.cerrarConexion()                
                
                if (r):
                    return r[0]
                else:
                    return []
                
                
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []            




    #https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python
    def listaUsuarios(self):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT * FROM "+TABLA_USUARIO)
                r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
                #print(r)
                self.cerrarConexion()
                return r
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []



    def rellenarEncuesta(self, seriePeli, saga, genero, numPelis, anime, valoracion, nombreUsu):
        try:
            self.conectar()
            cursor = self._conexion.cursor()
            consulta = f"INSERT INTO {TABLA_ENCUESTA}({SERIE_O_PELI}," \
                        f"{SAGA_PREFERIDA},{GENERO_FAV},{NUM_PELICULAS},{ANIME},{VALORACION_ENCUESTA}, {NOMRE_USU}) " \
                        f"values ('{seriePeli}','{saga}','{genero}',{numPelis},{anime},{valoracion},'{nombreUsu}')"
            cursor.execute(consulta)
            self._conexion.commit()
            self.cerrarConexion()
            return True
        except pymysql.err.IntegrityError as e:
            return False



    def registrarUsuario(self, nombre, idRol, contrasenia):
        try:
            self.conectar()
            cursor = self._conexion.cursor()
            consulta = f"INSERT INTO {TABLA_USUARIO}({NOMBRE_USUARIO},{ID_ROL},{PASS_USUARIO}) " \
                        f"values ('{nombre}',{idRol},'{contrasenia}')"
            cursor.execute(consulta)
            self._conexion.commit()
            self.cerrarConexion()
            return True
        except pymysql.err.IntegrityError as e:
            return False



    #https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python
    def listaEncuesta(self):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT * FROM "+TABLA_ENCUESTA)
                r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
                #print(r)
                self.cerrarConexion()
                return r
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []


    def borrarRegistrosEncuesta(self):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                consulta = f"DELETE FROM {TABLA_ENCUESTA}"
                cursor.execute(consulta)
                self._conexion.commit()
                self.cerrarConexion()
                return cursor.rowcount
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return -1
        

    def modificarEstadoEnc(self, nombre, estado):
        try:
            self.conectar()
            cursor = self._conexion.cursor()
            consulta = f"UPDATE {TABLA_ESTADO_ENCUESTA} SET {ENC_ACTIVADA} = '{estado}' " \
                       f"WHERE {NOMBRE_ENC} = '{nombre}'"
            cursor.execute(consulta)
            self._conexion.commit()
            self.cerrarConexion()
            return cursor.rowcount
        except (pymysql.err.IntegrityError) as e:
            return -1

        
    def buscarUsuario2(self, name, passs):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT idUser, idRol, nombre, pass FROM usuario WHERE nombre = %s AND pass = %s", (name, passs))
                
                r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
                print(r)
                
                self.cerrarConexion()                
                
                if (r):
                    return r[0]
                else:
                    return []
                
                
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []
        