dia = "Lluvioso" # Declaramos variable de tipo texto (str)

if dia == "Caluroso": # Primera condición a evaluar
    print("Hermoso dia para ir a la playa")

elif dia == "Lluvioso": # Segunda condición a evaluar
    print("Dia para quedarse en casa")

elif dia == "Nublado": # Tercera condición a evaluar
    print("Dia ideal para leer")

else: # Si ninguna de las anteriores es verdadera, se ejecuta esta
    print("Es un dia normal")


edad = 20 # Varibale tipo (int)

if edad >= 18: # Primera condición
    print("Es mayor de edad")

elif edad < 18 and edad >= 0: # Segunda condición 
    print("No eres mayor de edad")

else: # Si las anteriores no se cumplen
    print("Ingresa una edad válida")
