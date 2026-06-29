# Sesiones en Flask — flask.session

Por defecto, las webs son olvidadizas, cada vez que recargas o cambias de pestaña, el servidor te ve como un completo desconocido. Las sesiones (session) solucionan esto guardando datos del usuario de forma encriptada en el navegador usando una cookie.

Para trabajar con sesiones necesitamos 3 cosas:

- **app.secret_key**: Es una clave secreta (una contraseña larga) que usa Flask para firmar y encriptar las cookies.

- **Guardar y Leer datos**: Funciona igual a un diccionario de Python. Para guardar se escribe session['usuario'] = 'Carlos' y para leerlo en cualquier otra ruta simplemente lo llamas con **session.get('usuario')**.

- **Cerrar sesión**: Para borrar los datos y que la aplicación olvide al usuario, usamos **session.pop('usuario', None)** o **session.clear()**.
