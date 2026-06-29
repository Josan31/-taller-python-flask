# Manejo de errores — 404 y 500

Por defecto, cuando una página no existe o el servidor se rompe, el navegador muestra pantallas genéricas muy feas al usuario. Flask nos permite capturar esos momentos para mostrar un diseño propio y personalizable usando el decorador **@app.errorhandler()**.

Los dos errores más importantes que se deben registrar son:

- **Error 404 (Not Found)**: Se dispara cuando el usuario intenta entrar a una URL que no existe en tu aplicación.

- **Error 500 (Internal Server Error)**: Se dispara cuando hay un problema grave en el código del backend de Python (por ejemplo, una variable mal declarada o un fallo al conectar la base de datos) y el servidor colapsa.
