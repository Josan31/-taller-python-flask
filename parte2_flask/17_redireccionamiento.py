# Importamos url_for
from flask import Flask, redirect, url_for

app = Flask(__name__)

# ruta inicial
@app.route('/')
def inicio():
    return "<h3>Página de Inicio</h3><p>¡Bienvenido al sistema!</p>"

# ruta de ejemplo que redirige
@app.route('/entrar')
def entrar():
    # aquí iría la lógica (ej. validar usuario)
    print("Usuario autenticado. Redireccionando...")
    
    # Redirige a la función 'inicio' en vez de escribir la URL "/" a mano
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)