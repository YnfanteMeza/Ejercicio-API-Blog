# 1. IMPORTAR LAS LIBRERIAS
from flask_restful import Resource
from flask import jsonify

# 2. CONECTAR EL SERVIDOR WEB CON MYSQL WORKBENCH
from ..app import mysql # con los dos puntos salimos de la carpeta "api", seleccionamos el archivo "app.py" y luego importamos el objeto "mysql".

# 3. CREAR LA API "CategoriaAPI" PARA RECIBIR UNA PETICION "GET" Y RETORNAR TODAS LAS CATEGORIAS DE LA BASE DE DATOS
class CategoriaAPI(Resource):
  def get(self):
    cur = mysql.connection.cursor() # creamos un cursos para conectarnos a la base de datos "midbblog" en MySQL Workbench.
    cur.execute("SELECT * FROM `categoria`") # hacemos una consulta a la base de datos "midbblog" para pedirle todas las columnas de la tabla "categoria".
    resultado = cur.fetchall() # traemos la respuesta de la consulta y lo almacenamos en la variable "resultado".
    return jsonify(resultado) # con la funcion "jsonify" convertimos la respuesta de la base de datos "midbblog" en un JSON y lo retornamos.