# Intentamos ejecutar el bloque de código que podría fallar
try:
    # Pedimos las variables al usuario
    nombre = str(input("Ingresa tu nombre: "))
    edad = int(input("Ingresa tu edad: "))
    
    # Verificamos si el nombre esta vacio
    if nombre == "":
        raise ValueError("El nombre no puede estar vacío")
        # raise sirve para forzar la aparicion voluntaria de un error
        
    # Verificamos si la edad esta vacia
    if edad == 0:
        raise ValueError("La edad no puede ser cero")

# Si ocurre un error, se ejecuta este bloque
except ValueError as e:
    print(f"Error: {e}")

finally:
    print("Fin del programa")