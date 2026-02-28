# Propuesta de Cambio: Opciones de Resaltado

## ¿Qué?

Esta propuesta describe la adición de opciones de resaltado a la interfaz de usuario y la corrección de un error crítico en la generación de estilos. Específicamente, se añadirá:

1.  Un menú desplegable (`<select>`) para que el usuario pueda elegir el estilo de resaltado de Pygments (p. ej., `monokai`, `dracula`).
2.  Una casilla de verificación (`<input type="checkbox">`) para habilitar o deshabilitar los números de línea.
3.  **Corrección de error:** Se modificará el formateador de Pygments para que genere CSS en línea (`inline styles`) en lugar de clases de CSS, cumpliendo con el requisito principal del proyecto.

## ¿Por qué?

La implementación de estas opciones es un requisito funcional definido en el `sdd/SPEC.md` original. La corrección del error es necesaria para que la herramienta sea funcional en entornos como Moodle, que es el caso de uso principal.

## ¿Cómo?

## Arquitectura de la Solución

El núcleo de la aplicación se extenderá mediante parametrización, manteniendo la arquitectura Hexagonal:

1.  **Evolución del Core (`core/formatter.py`):**
    * La función principal actualizará su firma (DTO) para recibir: `code_string` (str), `language` (str), `theme` (str) y `show_linenos` (bool).
    * Debe usar `pygments.lexers.get_lexer_by_name()` con un fallback seguro (ej. 'text' si el lenguaje no existe o falla).
    * Debe usar `pygments.formatters.HtmlFormatter` pasándole el `style=theme` y `linenos=show_linenos`.
    * Debe retornar tanto el código HTML formateado como el bloque de CSS correspondiente al tema elegido (usando `formatter.get_style_defs()`), para que el frontend pueda pintar los colores correctos.

2.  **Evolución del Frontend (`templates/index.html`):**
    * Agregar un `<select name="language">` con al menos 5 lenguajes comunes (C++, Python, JavaScript, HTML, JSON).
    * Agregar un `<select name="theme">` con temas nativos de Pygments (ej. monokai, github, dracula).
    * Agregar un `<input type="checkbox" name="linenos">` para alternar los números de línea.
    * El bloque `<style>` del HTML debe inyectar dinámicamente el CSS que devuelva el core.

3.  **Evolución del Adaptador (`app.py`):**
    * Capturar los nuevos campos del formulario (request.form).
    * Pasar estos argumentos limpios a la función del core.

## Impacto

El impacto de este cambio es bajo y se limita a los archivos del proyecto. No hay dependencias externas adicionales. La implementación es sencilla y alinea la aplicación con los requisitos fundamentales del `sdd/SPEC.md`.
