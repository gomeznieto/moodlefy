# Especificación de Cambio: Opciones de Resaltado

## 1. User Stories

-   **Como usuario**, quiero poder elegir entre diferentes estilos de resaltado (como `monokai`, `dracula`) para personalizar la apariencia del código.
-   **Como usuario**, quiero poder activar o desactivar los números de línea para controlar la densidad de la salida.
-   **Como desarrollador**, quiero que la aplicación genere CSS en línea en lugar de clases de CSS para que sea compatible con Moodle.

## 2. Controles de la Interfaz de Usuario (`templates/index.html`)

-   **Selector de Estilo:**
    -   Se añadirá un menú desplegable (`<select name="style">`) al formulario.
    -   Este menú se poblará dinámicamente con los estilos disponibles en Pygments.
-   **Selector de Números de Línea:**
    -   Se añadirá una casilla de verificación (`<input type="checkbox" name="linenos" value="True">`) al formulario.

## 3. Lógica de la Aplicación

### `app.py`

-   La ruta `index` se modificará para:
    -   En peticiones `GET`, obtener la lista de estilos de Pygments (`pygments.styles.get_all_styles()`) y pasarla a la plantilla.
    -   En peticiones `POST`, obtener los valores de `style` y `linenos` del formulario.
    -   Pasar estos valores a la función de formateo en `core/formatter.py`.

### `core/formatter.py`

-   **Bug Fix:** La inicialización de `HtmlFormatter` se corregirá a `noclasses=True`.
-   La función `format_cpp_code` se renombrará a `format_code` para ser más genérica.
-   La función `format_code` aceptará los siguientes parámetros: `code_string`, `style`, y `linenos`.
-   Se usará `get_lexer_by_name("cpp")` para mantener la funcionalidad de C++.
-   El `HtmlFormatter` se instanciará con los parámetros `style` y `linenos` recibidos.

## 4. Flujo de Datos

1.  El usuario selecciona las opciones en la interfaz y envía el formulario.
2.  `app.py` recibe los datos del formulario (código, estilo, números de línea).
3.  `app.py` llama a `core.formatter.format_code()` con los datos recibidos.
4.  `core.formatter.format_code()` usa Pygments para formatear el código con las opciones especificadas, generando HTML con CSS en línea.
5.  `app.py` renderiza la plantilla `index.html` con el código formateado.
