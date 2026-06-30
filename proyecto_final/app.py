# ===================================
# IMPORTACION DE LIBRERIAS NECESARIAS
# ===================================

import sqlite3 # Biblioteca que nos permite interactuar con bases de datos SQLite
import os # Biblioteca que nos permite interactuar con el sistema operativo
from flask import Flask, render_template, request, redirect, url_for # Biblioteca que nos permite crear aplicaciones web
from werkzeug.utils import secure_filename # Biblioteca que nos permite asegurar el nombre del archivo

# Creamos la instancia de la aplicacion flask
app = Flask(__name__)

# Creamos la carpeta de la base de datos
RUTA_BD = "proyecto_final/bd/tienda.db"

# Creamos la carpeta de subida de imagenes
CARPETA_UPLOADS = os.path.join('proyecto_final', 'static', 'img', 'productos')

# Definimos las extensiones de imagen permitidas
EXTENSIONES_PERMITIDAS = {'png', 'jpg', 'jpeg', 'webp'}

# Configuramos la carpeta de subida
app.config['UPLOAD_FOLDER'] = CARPETA_UPLOADS


# =============================================================
# FUNCION AUXILIAR. INICIALIZA LA BASE DE DATOS Y CREA LA TABLA
# =============================================================

def inicializar_bd():

    # Crea la carpeta de subida si no existe
    os.makedirs(os.path.dirname(RUTA_BD), exist_ok=True)

    # Nos conectamos a la base de datos
    conexion = sqlite3.connect(RUTA_BD)

    # Iniciamos el cursor
    cursor = conexion.cursor()

    # Ejecutamos la consulta para crear la tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre    TEXT    NOT NULL,
            precio    REAL    NOT NULL,
            categoria TEXT    NOT NULL,
            stock     INTEGER NOT NULL,
            imagen    TEXT
        )
    ''')

    # Guardamos los cambios
    conexion.commit()

    # Cerramos la conexion
    cursor.close()
    conexion.close()


def extension_permitida(nombre_archivo):

    # Devuelve True si el archivo tiene una extension de imagen valida
    return '.' in nombre_archivo and \
           nombre_archivo.rsplit('.', 1)[1].lower() in EXTENSIONES_PERMITIDAS # .png, .jpg, .jpeg, .webp (Variable declarada antes)


# ======================================================
# RUTA 1: INDEX. MUESTRA TODOS LOS PRODUCTOS COMO CARDS.
# ======================================================

@app.route('/')
def tienda():
    # Capturamos el termino de busqueda que viene por parametro GET (?q=...)
    # Si no hay nada escrito, busqueda queda como cadena vacia
    busqueda = request.args.get('q', '').strip()

    # Nos conectamos a la base de datos
    conexion = sqlite3.connect(RUTA_BD)
    
    # Permite acceder por nombre de columna
    conexion.row_factory = sqlite3.Row  

    # Creamos el cursor
    cursor = conexion.cursor() # cursor sirve para ejecutar consultas sql

    if busqueda:
        # Si hay termino de busqueda, filtramos con WHERE usando LIKE
        # El % antes y despues permite buscar la palabra en cualquier parte del nombre
        cursor.execute(
            "SELECT * FROM productos WHERE nombre LIKE ? ORDER BY id DESC",
            (f'%{busqueda}%',)
        )
    else:
        # Si no hay busqueda, traemos todos los productos normalmente
        cursor.execute("SELECT * FROM productos ORDER BY id DESC")

    # Obtenemos los productos
    productos = cursor.fetchall() # fetchall() devuelve todos los resultados

    # Cerramos la conexion
    cursor.close()
    conexion.close()

    # Renderizamos la plantilla index.html pasandole los productos y el termino buscado
    # busqueda se pasa para mantener el texto en el input despues de buscar
    return render_template("index.html", productos=productos, busqueda=busqueda)


# ==================================================================
# RUTA 2: AGREGAR. FORMULARIO POST PARA REGISTRAR UN PRODUCTO NUEVO.
# ==================================================================

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    # Si el metodo es POST, el usuario envio el formulario
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        nombre    = request.form['nombre']
        precio    = request.form['precio']
        categoria = request.form['categoria']
        stock     = request.form['stock']
        archivo   = request.files.get('imagen')

        # Guardamos la imagen si tiene y es valida
        nombre_imagen = None

        # Si archivo existe, tiene nombre y extension valida
        if archivo and archivo.filename != '' and extension_permitida(archivo.filename):

            # Creamos la carpeta de subida si no existe
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) # exist_ok=True evita error si la carpeta ya existe
            
            # Aseguramos que el nombre del archivo sea seguro
            nombre_imagen = secure_filename(archivo.filename) # secure_filename() convierte el nombre del archivo en un nombre seguro
            
            # Guardamos la imagen en la carpeta de subida
            archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen)) # os.path.join() une las carpetas de forma segura

        # Insertamos el producto en la base de datos
        conexion = sqlite3.connect(RUTA_BD)

        # Ejecutamos la consulta
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, categoria, stock, imagen) VALUES (?, ?, ?, ?, ?)",
            (nombre, precio, categoria, stock, nombre_imagen)
        )

        # Guardamos los cambios
        conexion.commit()

        # Cerramos la conexion
        cursor.close()
        conexion.close()

        # Redirigimos a la tienda despues de guardar
        return redirect(url_for('tienda'))

    return render_template("agregar.html")


# ================================================================
# RUTA 3: DETALLE. MUESTRA LA INFORMACION COMPLETA DE UN PRODUCTO.
# ================================================================

@app.route('/producto/<int:producto_id>')
def detalle(producto_id):
    # Nos conectamos a la base de datos
    conexion = sqlite3.connect(RUTA_BD)
    
    # Permite acceder por nombre de columna
    conexion.row_factory = sqlite3.Row
    
    # Creamos el cursor
    cursor = conexion.cursor()
    
    # Ejecutamos la consulta
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    
    # Obtenemos el producto
    producto = cursor.fetchone()
    
    # Cerramos la conexion
    cursor.close()
    conexion.close()

    # Si el id no existe devolvemos 404
    if producto is None:
        return "<h2>Producto no encontrado.</h2>", 404

    return render_template("detalle.html", producto=producto)


# ========================================================
# RUTA 4: ELIMINAR. BORRA UN PRODUCTO DE LA BASE DE DATOS.
# ========================================================

@app.route('/eliminar/<int:producto_id>', methods=['POST'])
def eliminar(producto_id):
    # Nos conectamos a la base de datos
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()

    # Ejecutamos la consulta
    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,)) # ? es un marcador de posicion
    
    # Guardamos los cambios
    conexion.commit() # commit() sirve para guardar los cambios en la base de datos
    
    # Cerramos la conexion
    cursor.close()
    conexion.close()

    # Redirigimos a la tienda despues de eliminar el producto
    return redirect(url_for('tienda'))


# ================================
# MANEJO DE ERRORES PERSONALIZADOS
# ================================

@app.errorhandler(404)
def pagina_no_encontrada(error):

    # Renderizamos la plantilla 404.html
    return render_template("404.html"), 404


# =====================
# ARRANCA EL APLICATIVO
# =====================

if __name__ == '__main__':
    inicializar_bd()

    # debug=True permite ver errores en tiempo real
    app.run(debug=True)
