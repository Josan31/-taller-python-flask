# Plantillas HTML con Jinja2

## ¿Qué es jinja2?

Jinja 2 es un motor de plantillas para python, básciamente nos ayuda a generar HTML dinámico. Es super utilizado con el framework Flask o FastAPI.

## ¿Qué es la carpeta templates y cómo funciona?

Por defecto, flask busca las plantillas en la carpeta **templates** que se encuentra en el mismo nivel que nuestro archivo app.py.

Por ejemplo, si queremos cargar la plantilla index.html, Flask la buscará en la carpeta templates y la cargará.

El contenido HTML SIEMPRE debe de ir en una carpeta llamada templates.

## ¿Para qué sirve render_template()?

Es una función propia de Flask que importamos al principio del código. Su trabajo es **renderizar**, osea, tomar un archivo HTML de la carpeta templates y combinarlo con la lógica que tengamos en Python y enviárselo al navegador del usuario para que pueda ver la página web final.

## Sintaxis de jinja2

**{{ variable }}** (Dos llaves): Se usan para imprimir o mostrar texto directo que viene desde Python. Por ejemplo, si pasas el nombre de un usuario, pones {{ nombre }} y ahí se pintará en la pantalla.

**{% if %}** (Estructura condicional): Sirve para tomar decisiones dentro del HTML. Por ejemplo, si el usuario inició sesión, le muestras el botón de "Cerrar Sesión"; si no, le muestras el de "Ingresar". Al final siempre se debe cerrar con un **{% endif %}**.

**{% for %}** (Ciclo): Es útil para recorrer listas. Si tienes una lista de 10 productos en Python, con este ciclo puedes hacer que se cree una lista o una tarjeta HTML para cada producto automáticamente, sin tener que escribir el HTML 10 veces. Se cierra con **{% endfor %}**.
