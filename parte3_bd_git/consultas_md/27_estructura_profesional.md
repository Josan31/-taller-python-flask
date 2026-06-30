# Estructura profesional de un proyecto Flask

En el desarrollo de software profesional, mantener todos los archivos mezclados en una sola carpeta dificulta el mantenimiento del código, el trabajo en equipo y el despliegue en producción. Un proyecto de Flask bien estructurado sigue un patrón de diseño organizado por responsabilidades, asegurando que cada componente tenga un lugar único y lógico dentro del directorio.

La estructura recomendada para un proyecto Flask profesional es la siguiente:

aplicativo/
│
├── static/ # Archivos estáticos del proyecto
│ ├── css/ # Hojas de estilo (ej. estilos.css, main.css)
│ ├── js/ # Scripts de JavaScript (ej. main.js, validaciones.js)
│ └── img/ # Imágenes, logos e iconos del sistema (ej. logo.png)
│
├── templates/ # Plantillas HTML con motor Jinja2
│ ├── modulos/ # Fragmentos o secciones (ej. navbar.html, footer.html)
│ ├── base.html # Plantilla padre (herencia para el diseño global)
│ ├── index.html # Página de inicio o principal
│ └── login.html # Vista del formulario de acceso
│
├── app.py # Archivo principal (punto de entrada de la aplicación)
├── .gitignore # Archivos excluidos del control de versiones (ej. .venv/)
├── README.md # Documentación general y descripción del proyecto
└── requirements.txt # Lista de dependencias del entorno virtual (ej. Flask==3.0.0)

El propósito específico de cada elemento dentro de esta estructura es:

- **app.py:** Es el corazón de la aplicación. Aquí se inicializa el objeto Flask, se configuran las variables globales, se definen las rutas principales y se arranca el servidor de desarrollo.

- **templates/**: Carpeta obligatoria donde Flask busca los archivos HTML. Dentro de ella se procesa la lógica de Jinja2 para renderizar vistas dinámicas.

- **static/**: Carpeta dedicada a almacenar los recursos públicos que el navegador necesita descargar tal cual, como los estilos CSS, scripts de JavaScript, fuentes y logos o imágenes del sistema.

- **requirements.txt:** Archivo de texto plano que registra los nombres y versiones exactas de las librerías instaladas. Permite que cualquier otro desarrollador monte el proyecto en segundos ejecutando pip install -r requirements.txt.

- **.gitignore:** Archivo de configuración para Git. Le indica al sistema qué archivos o carpetas pesadas/secretas no debe subir a GitHub bajo ninguna circunstancia (por ejemplo: la carpeta .venv/)

- **README.md:** El documento de presentación escrito en formato Markdown. Es la portada del repositorio en GitHub; debe contener de forma obligatoria la descripción del proyecto, los requisitos previos, las instrucciones detalladas de instalación y los pasos para poner a ejecutar la aplicación.
