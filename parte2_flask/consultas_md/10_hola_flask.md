# Primera aplicacion Flask — app.py y servidor de desarrollo

## Creación del obejto app

Para iniciar cualquier aplicación web en Flask, primero se debe crear una instancia de la clase **Flask**. Esto se hace pasando la variable especial \***\*name\*\*** como argumento.

## Definición de la ruta en la raíz

Las rutas en Flask actúan como mapeos entre una URL del navegador y una función de Python. Para crear una ruta en la raíz, se utiliza **@app.route('/')**.

## Ejecución del servidor con debug=True

Para arrancar el servidor, se utiliza el método **app.run()**. Al incluir la estructura condicional **if **name** == '**main**':**, nos aseguramos de que el servidor solo se encienda si ejecutamos este archivo directamente de forma intencional.

**debug=True** es super importante porque nos permite que el servidor se reinicie automáticamente cada vez que detectemos cambios en el código, además de proporcionar mensajes de error detallados en el navegador, lo cual es muy útil durante el desarrollo.
