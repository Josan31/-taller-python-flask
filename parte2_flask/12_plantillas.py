# Importamos Flask y la función render_template
from flask import Flask, render_template

# Creamos la instancia de Flask
app = Flask(__name__)

# Creamos la ruta /tienda que renderizará la plantilla inicio.html
@app.route('/')
def tienda():
    # Variables de prueba para pasar al HTML
    usuario_activo = True
    lista_productos = ["Laptop", "Mouse Gamer", "Teclado Mecánico"]
    
    # Enviamos los datos directamente a la plantilla
    return render_template("12_plantillas.html", activo=usuario_activo, productos=lista_productos)
    # inicio.html debe ser un documento .html ubicado en la carpeta templates. Al este ser creado la página se va a renderizar

if __name__ == '__main__':
    app.run(debug=True)