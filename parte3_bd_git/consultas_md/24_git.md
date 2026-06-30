# Git — Control de versiones basico

Para entender realmente cómo funciona Git, necesitamos comprender que Git divide nuestro proyecto en diferentes áreas de estados por las que viaja el código antes de quedar guardado de forma permanente en el historial. No basta con aprenderse los comandos de memoria, si no que es necesario comprender el flujo de trabajo.

## Diferencia entre el área de trabajo y el repositorio

A diferencia de un guardado tradicional, Git maneja tres zonas principales por las que transitan los archivos, esas son:

1. **Área de Trabajo (Working Directory):** Es la carpeta física en tu computadora donde estás viendo, editando y creando tus archivos en tiempo real con tu editor de código.

2. **Área de Preparación (Staging Area):** Es una zona de transición intermedia. Aquí es donde colocas los archivos usando **git add .**, empaquetando los cambios que planeas guardar en la siguiente **"foto"**, pero que aún no se han registrado formalmente.

3. **El Repositorio (Local Repository / .git):** Es la base de datos oculta donde Git almacena de forma definitiva todas las versiones y fotos (commits) autorizadas de tu proyecto. Una vez que el código llega aquí, ya forma parte del historial inmutable.

## Comandos básicos del flujo de trabajo

El ciclo de vida para registrar una nueva versión del código se controla a través de los siguientes comandos en la consola:

**git init**: Convierte una carpeta común en un repositorio de Git local.

**git status**: Revisa qué archivos han cambiado en el Área de Trabajo y si están o no en el Staging Area.

**git add .**: Mueve todos los cambios del Área de Trabajo hacia el Staging Area, dejándolos listos para el commit.

**git commit -m "First Commit"**: Toma la bolsa del Staging Area y la guarda permanentemente en el Repositorio local con una etiqueta descriptiva.

**git log**: Muestra la lista cronológica de todos los commits que se han realizado en el proyecto, detallando quién hizo el cambio, en qué fecha y el mensaje descriptivo.
