import textwrap
from traceback import format_exception_only


def get_indented_exception_text(exception: Exception) -> str:
    exception_text = "".join(format_exception_only(exception))
    return textwrap.indent(exception_text, " " * 4)
