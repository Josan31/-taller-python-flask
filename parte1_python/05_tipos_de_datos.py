# Listas

frutas = ["Manzana", "Pera", "Uva", "Sandia"] # mutable

for fruta in frutas:
    print(fruta)

# Tuplas

frutas = ("Manzana", "Pera", "Uva", "Sandia") # inmutable

for fruta in frutas:
    print(fruta)

# Diccionarios

persona = {"nombre": "Juan", "edad": 25, "profesion": "Programador"} # par clave valor

# Recorrer solo las claves

for clave in persona.keys():
    print(clave)

# Recorrer solo los valores

for valor in persona.values():
    print(valor)

# Recorrer las claves y los valores a la vez

for clave, valor in persona.items():
    print(clave, valor)