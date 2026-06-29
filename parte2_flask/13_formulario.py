# Importamos Flask, render_template y request para manejar formularios y peticiones
from flask import Flask, render_template, request

app = Flask(__name__)

# Le decimos a la ruta que acepte tanto cargar la página (GET) como recibir datos (POST)
@app.route('/formulario', methods=['GET', 'POST'])
def manejar_formulario():
    if request.method == 'POST':
        # Capturamos lo que el usuario escribió en el input cuyo name es "nombre"
        nombre_usuario = request.form['nombre']
        correo_usuario = request.form['correo']
        return f"¡Datos recibidos con éxito! Hola, {nombre_usuario}, tu correo es: {correo_usuario}."
    
    # Si la petición es GET, simplemente mostramos el formulario limpio
    return render_template("13_formulario.html")

if __name__ == '__main__':
    app.run(debug=True)