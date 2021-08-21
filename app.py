# 1. IMPORTAR LAS LIBRERIAS
from flask import Flask # importamos la clase "Flask".
from flask_mysqldb import MySQL # importamos la clase "MySQL" para poder interactuar con MySQL Workbench.
from flask_restful import Api # importamos la clase "Api" para poder generar APIs REST.

# 2. CREAR EL SERVIDOR WEB
app = Flask(__name__)

# 3. CONECTAR EL SERVIDOR WEB CON MYSQL WORKBENCH
mysql = MySQL(app)

# 4. CREAR UNA INSTANCIA DE API A PARTIR DEL SERVIDOR WEB APP
api = Api(app)

# 5. CONFIGURAR LOS PARAMETROS DE ACCESO A LA BASE DE DATOS MYSQL
app.config["MYSQL_USER"] = "root" # ingresamos el usuario de nuestro MySQL Workbench.
app.config["MYSQL_PASSWORD"] = "Moodagent02061995YMLA" # ingresamos la contraseña de nuestro MySQL Workbench.
app.config["MYSQL_DB"] = "midbblog" # ingresamos el nombre de la base de datos de nuestro MySQL Workbench que queremos usar. 
app.config["MYSQL_CURSORCLASS"] = "DictCursor" # los datos se guardaran como diccionarios.

# 6. IMPORTAR LAS CLASES DE LA CARPETA "API"
from .api.articulo_by_categoria_api import ArticuloByCategoriaAPI
from .api.articulo_api import ArticuloAPI
from .api.categoria_api import CategoriaAPI

# 7. AGREGAR URL A LAS API DEFINIDAS COMO CLASES
api.add_resource(CategoriaAPI, "/categoria") # agregamos la ruta "/categoria" a la API "CategoriaAPI".
api.add_resource(ArticuloAPI, "/articulo") # agregamos la ruta "ArticuloAPI" a la API "ArticuloAPI".
api.add_resource(ArticuloByCategoriaAPI, "/categoria/<id>/articulo") # agregamos la ruta "/categoria/<id>/articulo" a la API "ArticuloByCategoriaAPI".


# 1. EJERCUTAR EL SERVIDOR WEB "FLASK"
# -Ir al entorno virtual donde se instalo la libreria, en este caso es el entorno virtual "blogenv", y luego entrar a la carpeta "Scripts".  
# -Seleccionar la entrada que muestra la ubicacion de la carpeta "Scripts" y escribir "cmd" y enter.
# -Escribir el comando "activate.bat" y enter (en el extremo izquierdo de la ventana "cmd" se mostrara, entre parentesis, el nombre de la carpeta "blogenv" lo que significa que el entorno virtual fue activado correctamente).
# -Sin salir de la ventana "cmd", ir a la carpeta donde se encuentra el archivo "app.py", en este caso es la carpeta "Blog API Flask". 
# -Escribir el comando "flask run" y enter.
# -Nos indica que el servidor esta corriendo en http://127.0.0.1:5000/ (el codigo "127.0.0.1" es la computadora local donde se esta ejecuando el servidor)
# -El procedimiento para hacer la peticion al servidor web es:
#  -Abrir el navegador y en la URL escribir "localhost:5000" (ruta "/") para ejecutar la funcion "index()" y retornar al navegador todas las columnas de
#   la tabla "producto" que pertenece a la base de datos "mydb" en formato texto.

