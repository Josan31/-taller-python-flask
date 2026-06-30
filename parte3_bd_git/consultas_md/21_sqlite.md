# SQLite con Python sqlite3

## ¿Qué es SQLite?

SQLite es un gestor de bases de datos relacionales que está escrito en C y es de código abierto. Es una base de datos ligera, eficiente y que no requiere configuración. Por esta razón, es muy utilizada en aplicaciones de escritorio, aplicaciones móviles y aplicaciones web pequeñas. Además de ser buena para desarrollos rápidos y ligeros.

## ¿Cómo crear una conexión y realizr el cierre?

Para interactuar con la base de datos, el primer paso es importar el módulo y usar **sqlite3.connect()** pasando el nombre del archivo. Si el archivo no existe, Python lo creará automáticamente. Al finalizar es obligarotio poner la línea **.close()** para liberar el recurso.

## CREATE TABLE, INSERT y SELECT

Para realizar operaciones en la base de datos, utilizamos el cursor y su método **.execute()**. Cuando modificamos la estructura o los datos (con CREATE, INSERT, UPDATE o DELETE), se debe ejecutar **conexion.commit()** para confirmar y guardar los cambios de forma permanente en el archivo físico.
