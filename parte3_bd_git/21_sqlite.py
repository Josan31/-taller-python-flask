# Importamos la librerias sqlite3 que viene integrada en python
import sqlite3

conexion = sqlite3.connect('parte3_bd_git/bd/21_sena.db') # dentro de los () ponemos el nombre de nuestra bd
cursor = conexion.cursor()

# creamos el esquema o estructura de nuestra bd
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aprendices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL
    )
''')

conexion.commit() # Confirmamos la creación de la tabla

# Creamos una lista que contiene todas las tuplas de los aprendices
nuevos_aprendices = [
    ('José', 'jose@gmail.com'),
    ('Juan', 'juanito@gmail.com'),
    ('María', 'maria@gmail.com')
]

# Usamos executemany en lugar de execute
cursor.executemany(
    "INSERT INTO aprendices (nombre, correo) VALUES (?, ?)", 
    nuevos_aprendices
)
conexion.commit()

cursor.execute("SELECT * FROM aprendices")
resultados = cursor.fetchall() # Captura todas las filas que devolvió la consulta

# Hacemos un print con los datos que nos devolvió la consulta
print("--- Lista de Aprendices ---")
for fila in resultados:
    print(f"ID: {fila[0]} | Nombre: {fila[1]} | Correo: {fila[2]}")

# Cerramos conexiones OBLIGATORIO
cursor.close()
conexion.close()