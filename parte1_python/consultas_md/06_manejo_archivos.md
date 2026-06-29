# Manejo de Archivos — open, read, write

El manejo de archivos en programación es el proceso mediante el cual tu código interactúa con el sistema de almacenamiento para crear, modificar, leer o borrar datos

En palabras sencillas es el proceso de abrir, leer o escribir en archivos usando código. las tres fundamentales son:

- **Open (Abrir)**: Conecta el programa con el archivo físico y define los permisos (ej. lectura o escritura).

- **Read (Leer)**: Extrae la información contenida en el archivo para que el programa pueda procesarla.

- **Write (Escribir)**: Guarda nueva información dentro del archivo, ya sea agregándola al final o reemplazando el contenido existente.

- **Append (Agregar)**: Añade información al final del archivo sin borrar lo que ya existía.

## ¿Qué es with?

antes, no existía una herramienta para ayudarnos a cerrar archivos, habia que poner una linea de código extra para cerrar el archivo, eso llevaba a errores donde el archivo se corrompía porque se olvidaba y no se cerraba, hasta que se inventó el 'with' que cierra el archivo automaticamente, y es la manera recomendada para manejar archivos en Python.
