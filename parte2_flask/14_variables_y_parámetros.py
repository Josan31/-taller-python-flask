from flask import Flask, request

app = Flask(__name__)

# Ejemplo de Variable de Ruta con conversor INT
@app.route('/usuario/<int:id_usuario>')
def ver_usuario(id_usuario):
    # Flask ya convirtió 'id_usuario' a un entero de verdad
    return f"<h3>Perfil del Usuario</h3><p>Buscando en la base de datos al usuario con ID: {id_usuario}</p>"

# 2. Ejemplo de Parámetros de Consulta usando request.args
@app.route('/buscar')
def buscar_productos():
    # Capturamos lo que venga en '?articulo=...' y '?limite=...'
    # El segundo valor es lo que pondrá por defecto si el usuario no manda nada
    termino = request.args.get('articulo', 'Todo')
    limite = request.args.get('limite', '10')
    
    return f"<h3>Motor de Búsqueda</h3><p>Buscando: <b>{termino}</b> | Mostrando un máximo de: {limite} resultados.</p>"


# Para probar las variables de ruta: http://127.0.0.1:5000/usuario/45
# Para probar los parámetros de consulta: http://127.0.0.1:5000/buscar?articulo=computador&limite=5

if __name__ == '__main__':
    app.run(debug=True)