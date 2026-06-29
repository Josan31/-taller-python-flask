# Redireccionamiento y url_for

## ¿Qué es redirect y url_for?

- **redirect():** Es una función de Flask que le ordena al navegador cambiar automáticamente de página. Por ejemplo, cuando un usuario inicia sesión con éxito, lo redireccionamos al panel de inicio.

- **url_for():** En lugar de escribir la ruta a mano (como /inicio), esta función genera la URL buscando el nombre de la función en Python. Si se escribe url_for('inicio'), Flask sabe exactamente qué ruta le pertenece a la función def inicio().

## ¿Por qué url_for() es mejor que escribir las URLs manualmente?

Porque es mucho más dinámico. Por ejemplo, si cambias la URL de una ruta, no tendrás que cambiarla en todos los lugares donde la uses.
