# Herencia de plantillas — base.html y block

En lugar de copiar y pegar el mismo código una y otra vez por ejemplo el header y el footer en los archivos HTML del proyecto tan solo se necesita un solo archivo llamado base.html

Las demás páginas como inicio.html o contacto.html simplemente heredan ese molde vacío y solo rellenan la parte del contenido. básicament es una estrucutra modular, de forma que nos permite ahorrar código y repetirlo donde queramos, ya sea para una vista o para el proyecto en general.

## Para lograr esto usamos tres etiquetas clave de Jinja2:

- **{% extends "base.html" %}**: Va en la primera linea de las páginas que quieren heredar el contenido de la plantilla base.html.
- **{% block NOMBRE %} y {% endblock %}**: Son contenedores que dejas reservados en el molde principal para que las otras páginas metan su propio código ahí dentro.
- **{% block contenido %}**: Es el bloque estándar que se usa para meter el cuerpo principal de cada página.
