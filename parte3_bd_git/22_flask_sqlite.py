# importamos las librerias necesarias para trabajar con flask y sqlite
import sqlite3
from flask import Flask

# creamos la instancia de la aplicacion flask
app = Flask(__name__)
RUTA_BD = "parte3_bd_git/bd/22_flask_sqlite.db"

# Definimos la ruta / que nos permitira verificar la conexion a la base de datos
@app.route('/')
def verificar():
    # 1. Se abre la conexión ÚNICAMENTE para esta solicitud del navegador
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    
    # 2. Se realiza la consulta de prueba
    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()
    
    # 3. Se cierra el recurso inmediatamente antes de responderle al usuario
    cursor.close()
    conexion.close()
    
    return f"Conexión exitosa a SQLite. Versión: {version[0]}"

if __name__ == '__main__':
    app.run(debug=True)