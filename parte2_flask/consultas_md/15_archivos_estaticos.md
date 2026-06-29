# Archivos estaticos — CSS, JS e imagenes

Así como flask te olbiga a meter los archivos HTML dentro de templates, los archivos estátcios **(CSS, IMG, JS)** debe ir en una carpeta propoia en la raiz del proyecto llamada **static**. Su nombre lo dice todo, son archivos que no cambian, que siempre van a ser los mismos.

Una buena práctica sería separarlos en subcarpetas como por ejemplo:

- **static/css/** Para los archivos de estilos (como estilos.css).
- **static/img/** Para todas las fotos, logos o iconos.
- **static/js/** Para el código de JavaScript.

## ¿Para qué sirve url_for() al cargar CSS e imágenes?

En archivos HTML es normal usar rutas relativas como **../static/css/estilos.css**. Pero en Flask esto NO es así, porque si una ruta URL cambia, la ruta del archivo se rompe y la página se queda sin diseño.

Para solucionar esto usamos **url_for()**, que es una función de Jinja2. En lugar de escribir la ruta a mano, le decimos a Flask: **"busca en la carpeta 'static' el archivo que está en la ruta tal"**.
