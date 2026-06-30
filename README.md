# Taller de Desarrollo Web con Python y Flask — SENA

Este repositorio contiene el desarrollo completo del taller académico de Python y Flask. Está organizado en tres partes progresivas y un proyecto final que integra todo lo aprendido.

---

**`parte1_python/`** — fundamentos del lenguaje: variables, condicionales, bucles, funciones, tipos de datos, manejo de archivos, excepciones y clases. Cada tema tiene su archivo `.py` y su documentación en `consultas_md/`.

**`parte2_flask/`** — introducción al framework Flask paso a paso: rutas, plantillas Jinja2, formularios, archivos estáticos, herencia de plantillas, redirecciones, manejo de errores, sesiones y API REST. Igual, cada concepto tiene su archivo y su `.md`.

**`parte3_bd_git/`** — integración con SQLite, entornos virtuales y flujo de trabajo con Git y GitHub. Incluye scripts funcionales y guías en Markdown.

**`proyecto_final/`** — aplicación web de una tienda construida con Flask y SQLite. Permite registrar productos con imagen, buscarlos por nombre y ver el detalle de cada uno.

---

## Cómo clonar el repositorio

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/taller-python-flask.git
cd taller-python-flask

# 2. Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac / Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar el proyecto final
python proyecto_final/app.py
```

Abrir `http://127.0.0.1:5000` en el navegador. La base de datos se crea automáticamente en `proyecto_final/bd/tienda.db`.
