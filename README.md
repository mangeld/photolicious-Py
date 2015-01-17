#Blog Parallax

This is an attempt to build a aesthetic blog ui

## Instalación

Lo mas recomendable es usar un entorno virtual de python.

Un entorno virtual de python nos permite tener una carpeta en el proyecto donde se encontrarán las dependencias de nuestra aplicación a la misma vez que la versión del interprete de python que estemos usando en nuestro proyecto.

Por motivos de orden, de ahorro de ancho de banda y de ahorro de tamaño del repositorio, el entorno virtual no es versionado junto con el resto de código, por lo que cuando hagamos un clone del repositorio tendremos que crear un nuevo entorno virtual.

Por suerte, si se versiona la lista con las dependencias necesarias para ejecutar y desarrollar el proyecto, las cuales estan situadas en el archivo 'requirements'.

###Creación de un entorno virtual

Necesitaremos el paquete `virtualenv`

```bash
pip install virtualenv
```
Nos movemos a la raíz del proyecto y ejecutamos el siguiente comando para crear una carpeta con el entorno virtual:

```bash
virtualenv venv
```
El parámetro _venv_ le indica al script que debe crear una carpeta con ese nombre para situar en su interior el entorno vitual.

Una vez hecho lo anterior ejecutamos el entorno virtual

```bash
./venv/activate
```
Esto nos logea en un intérprete de comandos situado en el entorno virtual, por lo que a partir de ahora todos los módulos que añadamos con `pip` quedarán confinados en el entorno virtual.

Debemos tener en cuenta que para que nuestro código funcione adecuadamente deberemos ejecutar el anterior comando cuando queramos ejecutar el código, ya que es el entorno virtual el que tiene en el `path` los módulos necesarios para que nuestra aplicación funcione.

### Instalación de dependencias

Estando logeados en el intérprete de comandos del entorno virtual ejecutamos el siguiente comando para obtener las dependencias necesarias:

```bash
pip install -r requirements
```
