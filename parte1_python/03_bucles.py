# Ejemplo con Bucle for 

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] # Lista con los dias de la semana

for dia in dias_semana: # d es el nombre que le damos a cada elemento de la lista 
    print(f"Dia de la semana: {dia}")

# Ejemplo con break usando bucle for

for dia in dias_semana: 
    if dia == "Jueves": # Si el dia es Jueves
        break # Rompemos el ciclo
    print(f"Hoy es el dia de la semana: {dia}")

# Ejmeplo con continue usando bucle for

for dia in dias_semana:
    if dia == "Sabado" or dia == "Domingo":
        print(f"Es fin de semana: {dia}")
        continue
    print(f"Dia de trabajo: {dia}")    
    

#Ejemplo con Bucle while 

numero = 1 # Inicializamos la variable numero en 1

while numero <= 5: # Mientras la variable numero sea menor o igual a 5
    print(f"Numero: {numero}") # Imprimimos el numero
    numero += 1 # Incrementamos el valor de la variable numero en 1

# Ejemplo usando bucle while con break

numero = 1

while numero <= 5:
    if numero == 3: # Si numero igual a 3 rompe el bucle
        break
    print(numero)
    numero += 1

# Ejemplo usando bucle while con continue

numero = 1

while numero <= 5:
    if numero == 3:
        print(f"El numero es 3, lo salto")
        numero += 1
        continue
    print(numero)
    numero += 1    