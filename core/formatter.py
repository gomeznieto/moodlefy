
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from dataclasses import dataclass

@dataclass
class FormatterResult:
    html: str

def format_code(code_string: str, language: str, theme: str, show_linenos: bool) -> FormatterResult:
    """
    Formatea una cadena de código a HTML con estilos en línea.
    
    Args:
        code_string: La cadena de código a formatear.
        language: El nombre del lenguaje de programación (ej. "cpp", "python").
        theme: El nombre del tema de Pygments a usar (ej. "default", "monokai").
        show_linenos: Booleano para indicar si se deben mostrar números de línea.

 Un objeto Formatter    Returns:
       Result conteniendo el código HTML formateado con estilos en línea.
    """
    try:
        lexer = get_lexer_by_name(language, stripall=True)
    except:
        # Fallback a 'text' si el lenguaje no es reconocido
        lexer = get_lexer_by_name("text", stripall=True)
        
    formatter = HtmlFormatter(
        style=theme,
        linenos=show_linenos,
        full=False,  # Retorna solo el bloque de código
        noclasses=True # Usar estilos en línea
    )
    
    formatted_html = highlight(code_string, lexer, formatter)
    
    return FormatterResult(html=formatted_html)
