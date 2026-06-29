# API REST con Flask — respuestas JSON

Una **API REST** es un servicio que permite que diferentes aplicaciones se comuniquen entre sí intercambiando datos. Suelen usarse para por ejemplo mostrar los últimos productos de una tienda en otra web o app, o para que una app móvil se conecte con la base de datos de una empresa.

## El uso de jsonify() y definición de endpoints

Para devolver datos en formato JSON desde Flask, se utiliza la función **jsonify()**. Esta herramienta toma un diccionario, lista u objeto de Python, lo convierte automáticamente en una cadena de texto con formato JSON válido.
