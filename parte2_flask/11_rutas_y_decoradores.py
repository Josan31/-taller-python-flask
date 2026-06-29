# Importmos Flask
from flask import Flask, request

app = Flask(__name__)

# Rutas independientes

# Cada ruta es independiente entre sí, creando páginas distintas
@app.route('/')
def inicio():
    return "Página de inicio."

# crea la ruta /tienda 
@app.route('/tienda')
def tienda():
    return "Bienvenido a la sección de productos."

# crea la ruta /ayuda
@app.route('/ayuda')
def ayuda():
    return "Centro de soporte técnico."

# Para rutas en una misma función

@app.route('/')
@app.route('/inicio')
def inicio():
    return "Página de inicio."

# Rutas usando GET Y POST

@app.route('/')

def index():
    return "Página principal."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # El usuario envió datos (ej. un formulario)
        usuario = request.form.get('username')
        password = request.form.get('password')
        return f"Usuario '{usuario}' registrado con éxito."
    
    # El usuario ve la página sin enviar datos (GET)
    return "Formulario de Registro (Método GET)"

if __name__ == '__main__':
    app.run(debug=True)