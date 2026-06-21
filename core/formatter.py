import re
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
        lexer = get_lexer_by_name("text", stripall=True)
    
    borderStyle = 'border-radius: 5px; margin:.2em .2em;'
    formatter = HtmlFormatter(
        style=theme,
        linenos=False,
        full=False,
        noclasses=True,
        cssstyles=borderStyle,
        prestyles='padding: .5em 1em; white-space: pre-wrap; word-wrap: break-word; color: #f1fa8c;'
    )
    
    formatted_html = highlight(code_string, lexer, formatter)

    if show_linenos:
        formatted_html = insert_line_numbers(formatted_html)
    
    return FormatterResult(html=formatted_html)

def insert_line_numbers(html):
    match = re.search('(<pre[^>]*>)(.*)(</pre>)', html, re.DOTALL)
    if not match: return html

    pre_open = match.group(1)
    pre = match.group(2)
    pre_close = match.group(3)

    html = html.replace(pre_close, '</pre></td></tr></table>')
    numbers = range(1, pre.count('\n') + 1)
    format = '%' + str(len(str(numbers[-1]))) + 'i'
    lines = '\n'.join(format % i for i in numbers)
    html = html.replace(pre_open, '<table><tr><td style="border-radius: 5px 0px 0px 5px; background-color: #44475a; padding-left: 5px; padding-right: 5px;">' + pre_open + lines + '</pre></td><td>' + pre_open)
    return html
