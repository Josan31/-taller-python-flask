# Creamos la funcion celebracion mediante el uso de def
def celebracion(nombre, edad): # Dfinimos los parametros nombre y edad
    # Imprimimos el mensaje de felicitacion
    print(f"Feliz cumpleaños {nombre}, ya tienes {edad} años")

# Llamamos a la funcion y le enviamos los argumentos
celebracion("Pepe", 20) 
celebracion("Juanita", 22)

# Guardamos la funcion en una variable
felicitaciones = celebracion 

felicitaciones("Pedro", 33) # Llamamos a la funcion guardada en la variable

# Función sin parámetros

def saludar():
    return "Hola Mundo"

# Llamamos a la funcion
saludo = saludar()

print(saludo)