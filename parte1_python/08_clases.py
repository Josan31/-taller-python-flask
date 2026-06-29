# Creamos la clase Personaje
class personaje:
    # Constructor 
    def __init__(self, nombre, nivel):
        # Atributos
        self.nombre = nombre
        self.nivel = nivel

    # Metodo
    def mostrar_info(self): # la función se llama mostrar_info y pertenece a la clase personaje
        print(f"Hola, soy {self.nombre} y tengo nivel {self.nivel}")

# Creamos los objetos
p1 = personaje("Némesis", 999)
p2 = personaje("Leon Kennedy", 999)

# Llamamos a los metodos
p1.mostrar_info()
p2.mostrar_info()