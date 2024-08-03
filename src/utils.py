from pathlib import Path


def converts_book_to_string(book_path: str) -> str:
    """takes a project Gutenberg book and converts the book to a string.

    takes out new lines and (Byte order Mark BOM)
    """
    txt = Path(book_path).read_text()

    txt = txt.replace('\n', '')
    txt = txt.replace('\ufeff', '')

    return txt
