# 1. ENTORNO VIRTUAL

# 1.1. CREAR ENTORNO VIRTUAL
# -Seleccionar la entrada que muestra la ubicacion de la carpeta "Blog API Flask" y escribir "cmd" y enter.
# -Escribir el comando "python -m venv blogenv" y enter.
# -Se creara un entorno virtual llamando "blogenv" (el entorno virtual puede tener otro nombre) dentro de la carpeta "Blog API Flask".
# -Agregamos la carpeta "blogenv" al archivo ".gitignore" para que no se suba el entorno virtual al repositorio de Github.

# 1.2. ACTIVAR UN ENTORNO VIRTUAL
# -Ir a la carpeta del entorno virtual que se quiere activar, por ejemplo "blogenv", y luego entrar a la carpeta "Scripts".  
# -Seleccionar la entrada que muestra la ubicacion de la carpeta "Scripts" y escribir "cmd" y enter.
# -Escribir el comando "activate.bat" y enter.
# -A partir de ahora el proyecto solo cargara las librerias y la version de python que hay en el entorno virtual "blogenv".

# 1.3. DESACTIVAR UN ENTORNO VIRTUAL
# -Ir a la carpeta del entorno virtual que se quiere desactivar, por ejemplo "blogenv", y luego entrar a la carpeta "Scripts".  
# -Seleccionar la entrada que muestra la ubicacion de la carpeta "Scripts" y escribir "cmd" y enter.
# -Escribir el comando "deactivate.bat" y enter.

# Nota: Para poder navegar por la ventana "cmd" usar los siguientes atajos:
# -cd .. = salir una carpeta
# -mkdir env1 = crear la carpeta "env1"
# -cd Scripts = ir a la carpeta "Scripts"
# -dir = ver la informacion de la carpeta

# 2. DEPENDENCIAS

# 2.1. CREAR UN ARCHIVO PARA LAS DEPENDENCIAS
# -Dentro de la carpeta "Blog API Flask" crear el archivo "requirements.txt".
# -Ingresar las librerias que requiere el proyecto para funcionar, en este caso requiere las librerias "Flask" y "flask-mysqldb".

# 2.2. INSTALAR LAS DEPENDENCIAS EN EL ENTORNO VIRTUAL
# -Ir al entorno virtual donde se instalaran las librerias, en este caso es el entorno virtual "blogenv", y luego entrar a la carpeta "Scripts".  
# -Seleccionar la entrada que muestra la ubicacion de la carpeta "Scripts" y escribir "cmd" y enter.
# -Escribir el comando "activate.bat" y enter.
# -Sin salir de la ventana "cmd", ir a la carpeta donde se encuentra el archivo "requirements.txt, en este caso es la carpeta "Blog API Flask". 
# -Escribir el comando "pip install -r requirements.txt" y enter.
# -Se instalan todas las librerias del archivo "requirements.txt" en el entorno virtual "blogenv".

# 3. USAR EL PYTHON DEL ENTORNO VIRTUAL
# -Seleccionar en "Python 3.9.5 64-bit" ubicado en la parte inferior izquierda del Visual Studio.
# -Seleccionar en la opcion "Enter interpreter path".
# -Seleccionar en la opcion "Find".
# -Ingresar a la carpeta del entorno virtual "blogenv".
# -Ingresar a la carpeta "Scripts".
# -Seleccionar el archivo "python".
# -Seleccionar el boton "Seleccionar Interprete".

# 4. CLONAR UN REPOSITORIO DE GITHUB
# -Crear la carpeta del proyecto "Blog API Flask".
# -Abrir la carpeta "Blog API Flask" en Visual Studio.
# -Dentro de Visual Studio hacemos clic derecho en el área de "Explorer" y luego seleccionamos "Open in Integrated Terminal" 
#  para que aparezca la ventana de comandos "1:bash".
# -En la ventana de comandos "1:bash" escribimos el comando <git init> y enter (este comando se realiza una sola vez).
# -Creamos un repositorio en Github, en este ejemplo creamos el repositorio "Ejercicio-API-Blog".
# -En el repositorio de Github seleccionamos el boton verde "Code" y copiamos la URL asegurándonos que este seleccionado en "HTTPS".
# -En la ventana "1:bash" escribimos el comando <git remote add origin "Pegar la URL del repositorio"> y enter (integramos el proyecto con el repositorio de Github. Este comando se realiza una sola vez).
# -En la ventana "1:bash" escribimos el comando <git pull origin main> y enter (actualizamos el proyecto con los últimos cambios almacenados en el repositorio de Github).
# -Se crean los archivos ".gitignore" y "LICENSE".

# 5. SUBIR LOS CAMBIOS AL REPOSITORIO DE GITHUB
# -Dentro de Visual Studio hacemos clic derecho en el área de "Explorer" y luego seleccionamos "Open in Integrated Terminal" 
#  para que aparezca la ventana de comandos "1:bash".
# -En la ventana "1:bash" escribimos el comando <git status> y enter (vemos los cambios realizados en el proyecto).
# -En la ventana "1:bash" escribimos el comando <git add .> y enter (agregamos los cambios realizados en el proyecto a la memoria temporal).
# -En la ventana "1:bash" escribimos el comando <git commit -m "primer commit"> y enter.
# -En la ventana "1:bash" escribimos el comando <git checkout main> y enter (nos movemos a la rama "main").
# -En la ventana "1:bash" escribimos el comando <git branch> y enter (verificamos que nos encontramos en la rama "main").
# -En la ventana "1:bash" escribimos el comando <git merge master> y enter (copiamos los archivos de la rama "master" y lo pegamos en la rama "main").
# -En la ventana "1:bash" escribimos el comando <git push origin main> y enter (subimos lo cambios realizados en el proyecto al repositorio de Github).
# -El commit se sube al repositorio "Ejercicio-API-Blog" en Github.