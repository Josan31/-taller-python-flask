from flask import Flask, jsonify

app = Flask(__name__)

# Definimos un endpoint que simula devolver los datos de un producto
@app.route('/api/producto', methods=['GET'])
def obtener_producto():
    # Creamos un diccionario normal de Python
    datos_moto = {
        'id': 1000,
        'marca': 'BMW',
        'modelo': 'S 1000 RR',
        'categoria': 'Superbike',
        'disponible': True
    }
    
    # jsonify transforma el diccionario a formato JSON de forma automática
    return jsonify(datos_moto)

if __name__ == '__main__':
    app.run(debug=True)