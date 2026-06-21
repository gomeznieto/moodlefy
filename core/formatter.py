import re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from dataclasses import dataclass

@dataclass
class FormatterResult:
    html: str

def format_code(code_string: str, language: str, theme: str, show_linenos: bool) -> FormatterResult:
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
        prestyles='padding: .5em 1em; white-space: pre; overflow-x: auto; margin: 0; line-height: 1.5; color: #f1fa8c;'
    )
    
    formatted_html = highlight(code_string, lexer, formatter)

    if show_linenos:
        formatted_html = insert_line_numbers(formatted_html)
    
    return FormatterResult(html=formatted_html)

def insert_line_numbers(html):
    match = re.search('(<pre[^>]*>)(.*)(</pre>)', html, re.DOTALL)
    if not match: 
        return html

    pre_open = match.group(1)
    pre_content = match.group(2)
    pre_close = match.group(3)

    num_lines = pre_content.count('\n') + 1
    numbers = range(1, num_lines + 1)
    
    format_str = '%' + str(len(str(numbers[-1]))) + 'i'
    lines = '\n'.join(format_str % i for i in numbers)

    start, end = match.span()
    
    table_html = (
        f'<table style="border-collapse: collapse; margin: 0; padding: 0; width: 100%;"><tr>'
        f'<td style="border-radius: 5px 0px 0px 5px; background-color: #44475a; padding: 0; margin: 0; vertical-align: top; width: 1%;">'
        f'{pre_open}{lines}{pre_close}'
        f'</td>'
        f'<td style="padding: 0; margin: 0; vertical-align: top;">'
        f'{pre_open}{pre_content}{pre_close}'
        f'</td>'
        f'</tr></table>'
    )

    return html[:start] + table_html + html[end:]
