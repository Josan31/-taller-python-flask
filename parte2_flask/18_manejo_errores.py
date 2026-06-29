from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h3>Página Principal</h3><p>Todo funciona bien.</p>"

# Capturamos el error 404 (Página no encontrada)
@app.errorhandler(404)
def pagina_no_encontrada(error):
    # Retornamos una plantilla personalizada y OBLIGATORIAMENTE el número 404 al final
    return "<h2>Error 404: La página que buscas no existe.</h2>", 404

# Capturamos el error 500 (Fallo del servidor)
@app.errorhandler(500)
def error_interno_servidor(error):
    # Lo mismo con el error 500, al final debe siempre ir el número 500
    return "<h2>Error 500: Algo salió muy mal en nuestros servidores.</h2>", 500

if __name__ == '__main__':
    app.run(debug=True)