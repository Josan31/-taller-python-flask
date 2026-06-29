from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mostrar_design():
    # Solo renderizamos la plantilla, ya que los archivos estáticos están dentro del html
    return render_template("15_archivos_estaticos.html")

if __name__ == '__main__':
    app.run(debug=True)