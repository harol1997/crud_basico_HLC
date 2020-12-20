from mysql.connector import connect

class Connector:

    def __init__(self):#constructor de la clase
        self.cnx = connect(host="localhost",user='root', database='datos',password="aquicolocaslacontraseña")

    def registrar(self,*data):
        resultado = "El usuario ha sido registrado"
        try:

            cursor = self.cnx.cursor()

            instruccion_sql = "insert into usuario(identificacion,nombres,centro) values(%s,%s,%s)"

            cursor.execute(instruccion_sql,data)

            self.cnx.commit()

            cursor.close()
        except Exception as e:
            resultado = str(e)

        return resultado

    def editar(self,*data):
        resultado = "El usuario ha sido actualizado"
        try:
            cursor = self.cnx.cursor()

            instruccion_sql = "update usuario set centro=%s where identificacion=%s"

            cursor.execute(instruccion_sql,data)

            self.cnx.commit()

            cursor.close()
        except Exception as e:
            resultado = str(e)

        return resultado

    def eliminar(self,*data):

        resultado = "El usuario ha sido eliminado"
        try:
            cursor = self.cnx.cursor()

            instruccion_sql = "delete from usuario where identificacion=%s"

            cursor.execute(instruccion_sql,data)

            self.cnx.commit()

            cursor.close()
        except Exception as e:
            resultado = str(e)

        return resultado  
        
    def buscar(self,*data):
        cursor = self.cnx.cursor()

        instruccion_sql = "select * from usuario where identificacion=%s"

        cursor.execute(instruccion_sql,data)

        datos = cursor.fetchall()

        cursor.close()

        return datos

    def close_connection(self):
        self.cnx.close()