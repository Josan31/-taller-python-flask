# Importamos Flask y render_template
from flask import Flask, render_template

app = Flask(__name__)

# Creamos la ruta principal en index
@app.route('/')
def inicio():
    # Flask renderiza 16_inicio.html, y Jinja2 se encarga de fusionarlo con 16_base.html
    return render_template("16_inicio.html")

if __name__ == '__main__':
    app.run(debug=True)