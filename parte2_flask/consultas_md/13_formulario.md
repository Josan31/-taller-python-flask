# Formularios HTML y metodo POST

## Diferencia entre GET y POST

Estos son los dos métodos principales que usa el navegador para comunicarse con el servidor HTTP:

**GET (Para pedir información):** Es el método por defecto. Cuando entras a una URL o buscas algo en Google, usas GET.

**POST (Para enviar información):** Se usa cuando quieres guardar, registrar o mandar datos al servidor (como un formulario de registro o login).

## ¿Cómo se reciben los datos en Flask con request.form?

Cuando el usuario llena los campos del formulario HTML y le da al botón de enviar, el navegador empaqueta toda esa información y la manda al servidor a través de una petición POST.

Para atrapar esos datos tenemos **request.form** que es ofrecida por flask y nos permite hacer formularios funcionales y dinámicos.
