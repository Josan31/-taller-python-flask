# creamos un archivo llamado mi_archivo.txt y escribimos en el

# "w" tambien sirve para, si el archivo no exite lo crea o lo reemplaza por mi_archivo.txt
with open("mi_archivo.txt", "w") as archivo: 
    archivo.write("Pasos para beber agua:\n")
    archivo.write("1. Toma un vaso\n")
    archivo.write("2. Llenalo de agua\n")
    archivo.write("3. Pon tu mano sobre el vaso\n")
    archivo.write("4. Bebe el agua\n")

# leemos el archivo
with open("mi_archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
    
# agregamos al final del texto
with open("mi_archivo.txt", "a") as archivo:
    archivo.write("5. Felicidades has terminado de beber agua\n")