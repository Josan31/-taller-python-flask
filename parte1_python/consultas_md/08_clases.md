# Programacion Orientada a Objetos — Clases y Objetos

La Programacion Orientada a Objetos o POO es un paradigma o modelo de programación que organiza el código en "objetos". Permite modelar problemas del mundo real agrupando datos (atributos) y comportamientos (métodos).

En palabras sencillas nos ayuda a organizar mejor nuestro código, por ejemplo para no repetir código y para que sea más fácil de mantener.

# Conceptos Clave en POO

## Clase (Class)

Una clase es como un molde, plantilla o plano que define las características (atributos) y comportamientos (métodos) comunes que tendrán los objetos creados a partir de ella.

Por ejemplo, la clase **Coche** podría tener atributos como **color**, **marca**, **velocidad**.

## Objeto (Object)

Un objeto es una instancia concreta de una clase. Es una entidad individual con sus propios valores para los atributos definidos en la clase.

Un ejemplo seria **mi_coche_rojo** que seria un objeto de la clase **Coche**. Tendria su propio color **rojo**, su propia marca **Toyota** y su propia velocidad actual. Podrias tener varios objetos **Coche** diferentes creados a partir de la misma clase.

## Atributos (Attributes)

Los atributos son las características o propiedades de un objeto. Son variables que almacenan datos que describen el estado del objeto.
En nuestro ejemplo de **Coche**, los atributos serían: **color**, **marca**, **modelo**, **velocidad_actual**, **encendido**, etc.

## Métodos (Methods)

Los métodos son las acciones o comportamientos que un objeto puede realizar. Son funciones que están asociadas a una clase y operan sobre los atributos del objeto.
Los métodos de la clase **Coche** podrían ser: **arrancar()**, **acelerar()**, **frenar()**, **girar()**, **cambiar_marcha()**, etc.

## Constructor (Constructor)

El constructor es un método especial que se ejecuta automáticamente cuando se crea un nuevo objeto de una clase. Su principal función es inicializar el estado del objeto. Se define usando: **init()**.
