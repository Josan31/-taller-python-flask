# GitHub — Subir el proyecto al repositorio remoto

GitHub es una plataforma de alojamiento en la nube que permite almacenar, gestionar y compartir repositorios de Git. Mientras que Git funciona de forma local en el disco duro de tu computadora, GitHub actúa como el servidor remoto (en internet), lo que permite tener una copia de seguridad segura del código y colaborar con otros desarrolladores en cualquier parte del mundo.

## ¿Cómo conectar el repositorio local con el remoto?

Para conectar el repositorio local con el remoto, se deben seguir los siguientes pasos:

## 1. Crear el repositorio en GitHub

Se ingresa a la página web de GitHub, se da clic en el botón "New repository", se le asigna un nombre al proyecto y se crea completamente vacío.

## 2. Vincular los repositorios con git remote add origin

Una vez creado el repositorio en la nube, GitHub nos entrega una URL única.
Se pega la URL en el terminal y se ejecuta el comando: **git remote add origin <URL>** Por ejemplo: git remote add origin https://github.com/tu_usuario/tu_repositorio.git

## 3. Subir los cambios con git push

Con el puente construido, el comando **git push** toma todas las "fotos" (commits) guardadas en nuestro repositorio local y las envía a la nube. El parámetro **-u origin main** se utiliza la primera vez para indicarle a Git que, de ahí en adelante, la rama local "main" estará sincronizada directamente con la rama "main" de GitHub.
