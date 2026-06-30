# Entornos virtuales — venv

## ¿Qué es un entorno virtual?

Un engorno virtual o **venv** es un espacio aislado dentro de nuestro proyecto que nos permite instalar dependencias específicas sin alterar el almacenamiento del sistema operativo global ni afectar a otro proyecto por miedo que tengan otras versiones de dependencias instaladas.

## ¿Cómo se crea un entorno virtual?

Es muy senicllo crear un entorno virtual, para ello necesitamos usar el comando **python -m venv** y seguido del nombre que le queremos poner a la carpeta del entorno virtual. Normalmente se suele nombrar como **.venv** o **env**.

## ¿Cómo activarlo?

Para activarlo tenemos que irnos a Powershell y ejecutar el comando **.venv\Scripts\Activate.ps1**. Si se activa correctamente debemos de ver el nombre del entorno virtual entre paréntesis al inicio de la linea de comandos, por ejemplo: **(.venv) PS C:\Users\josem\taller-python-flask>** una vez dentro podemos instalar las dependencias deseadas como **pip install flask**, las cuales se instalarán únicamente dentro del entorno virtual.

## ¿Cómo desactivarlo?

Para desactivarlo lo único que tenemos que hacer es irnos a Powershell y ejecutar el comando **deactivate**.

## ¿Cómo se genere el documento requeriments.txt?

Este es un documento muy útil porque almacena todas las dependencias que hemos instalado en el entorno virtual. Para generarlo tenemos que irnos a Powershell y ejecutar el comando **pip freeze > requirements.txt**. De esta forma se nos creará el documento en nuestra carpeta raiz del proyecto.

Si queremos instalar esa dependias que hay dentro del requeriments.txt debemos ejecutar **pip install -r requirements.txt**. Esto es muy útil por que, al entorno trabajrse de manera local y al declararlo en el .gitignore y no subirlo de esta menra lo creamos en segundos desde cero. Este entorno es pesado por eso no se debe subir al repositorio.
