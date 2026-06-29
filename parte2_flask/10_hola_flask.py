# importamos flask
from flask import Flask

# Pimero creamos el objeto app
app = Flask(__name__)

# Luego definimos la ruta en la raíz
@app.route('/')
def inicio():
    return "Mi primera página web con Flask!"

# Por último ejecutamos el servidor con debug=True
if __name__ == '__main__':
    app.run(debug=True)
