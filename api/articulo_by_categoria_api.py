# 1. IMPORTAR LAS LIBRERIAS
from flask_restful import Resource
from flask import jsonify

# 2. CONECTAR EL SERVIDOR WEB CON MYSQL WORKBENCH
from ..app import mysql # con los dos puntos salimos de la carpeta "api", seleccionamos el archivo "app.py" y luego importamos el objeto "mysql".

# 3. CREAR LA API "ArticuloByCategoriaAPI" PARA RECIBIR UNA PETICION "GET" Y RETORNAR EL TITULO, NOMBRE Y CATEGORIA DE UN ARTICULO EN ESPECIFICO DE LA BASE DE DATOS
class ArticuloByCategoriaAPI(Resource):
  def get(self, id):
    cur = mysql.connection.cursor() # creamos un cursos para conectarnos a la base de datos "midbblog" en MySQL Workbench.
    cur.execute('''
      SELECT art.titulo, c.nombre AS categoria
      FROM `midbblog`.`articulo` AS art
      LEFT JOIN `midbblog`.`categoria` AS c
      ON art.idCategoria = c.idCategoria
      WHERE art.idCategoria =''' + id
    ) # hacemos una consulta a la base de datos "midbblog" para pedirle las columnas: titulo del articulo y nombre de la categoria de ese articulo. Ver Nota 1.
    resultado = cur.fetchall() # traemos la respuesta de la consulta y lo almacenamos en la variable "resultado".
    return jsonify(resultado) # con la funcion "jsonify" convertimos la respuesta de la base de datos "midbblog" en un JSON y lo retornamos.

    # Nota 1: Seleccionar el "titulo" de la tabla articulo y el "nombre" de la tabla categoria
    # de la base de datos "midbblog.articulo" renombrado como "art" y unirlo de izquierda a derecha con la base de datos
    # "midbblog.categoria" renombrado como "c" donde el "idCategoria" de las tablas articulo y categoria deben ser iguales.