## PRD: C++ Code Formatter para Moodle (Hilite.me Clone)

### 1. Objetivo del Proyecto

Crear una herramienta local (self-hosted) que reciba fragmentos de código **C++** y genere un bloque de **HTML con CSS inline**. El resultado debe ser compatible con editores de foros (Moodle/Atto) que eliminan hojas de estilo externas o etiquetas `<style>`.

### 2. Stack Tecnológico

* **Backend:** Python 3.10+ con **Flask**.
* **Motor de Resaltado:** **Pygments** (Librería estándar de la industria).
* **Frontend:** HTML5 básico con **Bootstrap 5** (vía CDN) para una interfaz limpia y rápida.
* **Persistencia (Contexto):** SQLite vía Engram (para que la IA recuerde mis preferencias de estilo).

### 3. Requerimientos Funcionales

* **Input:** * Un `textarea` de gran tamaño para el código fuente.
* Un `dropdown` para elegir el estilo (monokai, friendly, dracula, zenburn).
* Un `checkbox` para habilitar/deshabilitar números de línea.


* **Procesamiento (El Core):**
* Uso de `HtmlFormatter(noclasses=True)` para forzar estilos inline.
* Uso de `CppLexer` para el análisis sintáctico de C++.


* **Output:**
* Una vista previa (Preview) del código formateado.
* Un `textarea` de solo lectura con el **código HTML generado** (listo para copiar).
* Botón "Copiar al Portapapeles".



### 4. Arquitectura de Archivos (Propuesta)

```text
/cpp-formatter
├── app.py              # Servidor Flask y lógica de Pygments
├── templates/
│   └── index.html      # Interfaz única (Single Page App)
├── static/
│   └── style.css       # Estilos mínimos para la UI
├── docs/
│   └── PRD-Formatter.md # Este archivo
└── requirements.txt    # flask, pygments

```

### 5. Features Implemented

- **Lector de Archivos (lector-archivos)**: Se ha implementado y verificado la funcionalidad para subir archivos de código C++ (`.cpp` o `.h`). Esto incluye el manejo de la carga, validación de extensión y formateo del código subido, así como la integración con el `textarea` existente para pegar código.