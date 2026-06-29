# Ciclos — for y while

Los ciclos (o bucles) son estructuras de control fundamentales en programación que permiten repetir un bloque de código varias veces de forma automática.

De forma mas simple un bucle es una estructura que nos permite repetir un bloque de código muchas veces

## ¿Qué es el ciclo for?

El ciclo for se utiliza para repetir acciones sobre una secuencia o un grupo de elementos (iterar). Se ejecuta una cantidad fija y exacta de veces, la cual conoces desde que escribes el código.

por ejemplo:

dias = ["Lunes", "Martes", "Miercoles"]

for dia in dias:
print(f"Dia: {dia}")

# ¿Qué es el ciclo While?

El ciclo while repite un bloque de código mientras una condición específica sea verdadera.

por ejemplo:

numero = 1

while numero <= 5:
print(numero)
numero += 1

# ¿Cómo se usan break y continue?

- **break**: break sirve para detener por completo el ciclo de forma inmediata.
- **continue**: continue sirve para saltarse el resto del código de la repetición actual e ir directo a la siguiente.
