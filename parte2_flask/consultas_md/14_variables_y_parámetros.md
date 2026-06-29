# Variables de URL y parametros de consulta

## Variables de Ruta y Tipos de Conversor

Normalmente las URLs son fijas, pero en Flask podemos crear "variables de ruta" usando los picos **< >**. Esto sirve para que una sola ruta cambie dinámicamente según el dato que le mandemos.

Para asegurarnos de que el usuario no mande texto donde va un número, usamos los conversores. Los tres más comunes son:

**string**: Es el que viene por defecto si no pones nada. Acepta cualquier texto plano (sin barras /).

**int**: Obliga a que el dato de la URL sea un número entero positivo (como el ID de un usuario o un producto). Si alguien escribe letras, Flask saca un error 404 automáticamente.

**float**: Igual que el anterior, pero acepta números con decimales (por ejemplo, para filtrar por un precio exacto).

## ¿Qué son los parámetros de Consulta con request.args?

**request.args** es un diccionario especial que almacena los parámetros de consulta (query parameters) enviados en la URL. Se utilizan para enviar datos adicionales a una solicitud, identificándose en la URL después del signo de interrogación (ej. **?nombre=Ana&edad=25**)
