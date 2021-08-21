# --- --- --- --- --- SERVIDOR WEB HEROKU --- --- --- --- ---

# 1. ¿Que es Heroku?
# Heroku es un servidor web que nos permite subir un backend en la nube para su producción de forma
# gratuita (hasta 5 proyectos) resultando util para hacer demos.

# 2. CREAR UNA NUEVA APLICACION EN HEROKU
# -Ingresar a una cuenta de Heroku.
# -Seleccionar en el boton "New" y luego seleccionar en la opcion "Create new app".
# -En el campo "App name" ingresar el nombre de la aplicacion, por ejemplo "gato-resizer".
# -Seleccionar el boton morado "Create app".

# 3. CREAR UN ARCHIVO PARA LAS DEPENDENCIAS
# -Abrir la carpeta del proyecto en Visual Studio, por ejemplo proyecto "Pillow Mejorar Imagen".
# -Dentro de la carpeta "Pillow Mejorar Imagen" crear el archivo "requirements.txt".
# -Ingresar las librerias que requiere el proyecto para funcionar, en este ejemplo requiere las librerias "Flask", "Pillow" y "gunicorn".
# -Nota: La libreria "gunicorn" mantiene iniciado una aplicación que está en producción de modo que siempre estará listo para 
#  recibir peticiones y si la aplicación se cae, entonces, "gunicorn" automáticamente lo inicia.

# 4. CREAR EL ARCHIVO "PROCFILE" Y "GITIGNORE"
# -Abrir la carpeta del proyecto en Visual Studio, por ejemplo proyecto "Pillow Mejorar Imagen".
# -Dentro de la carpeta "Pillow Mejorar Imagen" crear el archivo "Procfile".
# -Ingresamos el comando "web: gunicorn app:app" en el archivo "Procfile".
# -Dentro de la carpeta "Pillow Mejorar Imagen" creamos el archivo ".gitignore" e ingresamos el nombre de los archivos o carpetas que no se quieran subir al repositorio de Github, por ejemplo __pycache__.

# 5. SUBIR UN PROYECTO A GITHUB
# -Ingresar a una cuenta de Github.
# -Seleccionar el boton verder "New".
# -En el campo "Repository name" ingresar el nombre del repositorio, por ejemplo "cat-resizer".
# -Seleccionar el boton verde "Create repository".
# -En el repositorio de Github seleccionamos el icono verde "Code" y copiamos la URL asegurándonos que este seleccionado en "HTTPS".
# -Abrir el proyecto de ejemplo "Pillow Mejorar Imagen" en Visual Studio.
# -Dentro de la carpeta "Pillow Mejorar Imagen" hacemos clic derecho en el área de "Explorer" y luego seleccionamos "Open in Integrated Terminal".
# -En la ventana "1:bash" escribimos el comando <git init> y enter (este comando se realiza una sola vez).
# -En la ventana "1:bash" escribimos el comando <git status> y enter (vemos los cambios realizados en el proyecto).
# -En la ventana "1:bash" escribimos el comando <git add .> y enter (agregamos los cambios realizados en el proyecto a la memoria temporal).
# -En la ventana "1:bash" escribimos el comando <git commit -m "primer commit"> y enter.
# -En la ventana "1:bash" escribimos el comando <git remote add origin "Pegar la URL del repositorio"> y enter (integramos el proyecto con el repositorio de Github. Este comando se realiza una sola vez).
# -En la ventana "1:bash" escribimos el comando <git branch -M main> y enter (creamos la rama "main" y nos movemos a ella).
# -En la ventana "1:bash" escribimos el comando <git branch> y enter (verificamos que nos encontramos en la rama "main").
# -En la ventana "1:bash" escribimos el comando <git push -u origin main> y enter (subimos lo cambios realizados en el proyecto al repositorio de Github).

# 6. INSTALAR HEROKU EN WINDOWS
# -Ingresar a una cuenta de Heroku.
# -Ingresar a la aplicacion creada en Heroku, en este ejemplo "gato-resizer".
# -Ir a la pagina de instalacion de Heroku haciendo clic en "Download and install the Heroku CLI".
# -Seleccionar el boton morado "64-bit installer" para Windows.
# -Instalar Heroku presionando solo "Next" e "Install".

# 7. CLONAR UNA APLICACION DE HEROKU
# -Usando la ventana "cmd" ingresar a la carpeta del proyecto, en este ejemplo "Pillow Mejorar Imagen".
# -En la ventana "cmd" escribirmos el comando <heroku git:remote -a gato-resizer> y enter.
# -Ingresamos a Heroku seleccionando el boton morado "Log in".

# 8. SUBIR EL PROYECTO A HEROKU
# -Dentro de la carpeta "Pillow Mejorar Imagen" hacemos clic derecho en el área de "Explorer" y luego seleccionamos "Open in Integrated Terminal".
# -En la ventana "1:bash" escribimos el comando <git branch master> y enter (copiamos los archivos de la rama "main" y lo pegamos en la nueva rama "master").
# -En la ventana "1:bash" escribimos el comando <git checkout master> y enter (nos movemos a la rama "master").
# -En la ventana "1:bash" escribimos el comando <git branch> y enter (verificamos que nos encontramos en la rama "master").
# -En la ventana "1:bash" escribimos el comando <git add .> y enter (agregamos los cambios realizados en el proyecto a la memoria temporal).
# -En la ventana "1:bash" escribimos el comando <git commit -m "deploy commit"> y enter
# -En la ventana "1:bash" escribimos el comando <git push heroku master> y enter (subimos lo cambios realizados en el proyecto a la aplicacion de Heroku).