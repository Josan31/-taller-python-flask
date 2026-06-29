# Rutas y Decoradores — @app.route

## ¿Qué es un dercorador como @app.route y como define múltiples rutas?

En python un decorador es una función especial que modifica o mejora el comportamiento de otra función sin alterar su código fuente de forma permanente.

El decorador @app.route() se encarga de registrar en Flask todas las direcciones URL que queremos manejar.

Este decorador es el más importante de todos, sin el no hay rutas en una página web.

## ¿Cómo se definen múltiples rutas?

Para hacer esto hay dos caminos, o se crean rutas independientes para diferentes funciones, o se asignan varias rutas a una misma función.

### Rutas independientes

@app.route('/')
def inicio():
return "Página de inicio."

@app.route('/tienda')
def tienda():
return "Bienvenido a la sección de productos."

### Rutas múltiples para una misma función

@app.route('/')
@app.route('/inicio')
def inicio():
return "Página de inicio."

## Métodos GET y POST

estas son las peticiones más importantes en la web, siendo

- **GET**: Se utiliza para solicitar información, por defecto así funcionan todas las rutas en Flask.
- **POST**: Se utiliza para enviar información, por ejemplo, datos de un formulario.

Podemos especificar estos métodos en @app.route() de la siguiente manera:

@app.route('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
return "Petición POST"
else:
return "Petición GET"
