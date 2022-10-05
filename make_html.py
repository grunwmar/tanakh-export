import json
import os
import sys
from bs4 import BeautifulSoup
from hebrew_numbers import  int_to_gematria
from filters import fix_yiddish_letters, replace_brackets, unescape_angle_brackets
from jinja2 import Environment, FileSystemLoader
from jinja2.filters import FILTERS
from langcodes import Language


LETTER_INDICES = 'abcdefghijklmnopqrstuvwxyz'


def open_file(path):
    with open(path, "r") as f:
        return f.read()


def convert_index(lang, int):
    if lang in ['he', 'yi']:
        return int_to_gematria(int, gershayim=False)
    else:
        return str(int)


def langname(isocode):
    return  Language.get(isocode).display_name(isocode)

def hebrew_index(integer):
    return convert_index("he", integer)

def subs_brackets(string):
    return replace_brackets(string, new=('<i>', '</i>'))

def subs_brackets_he(string):
    return replace_brackets(string, old=("(", ")"), new=('<span class="note_1">', '</span>'))


FILTERS["hebrew_index"] = hebrew_index
FILTERS["subs_brackets"] = subs_brackets
FILTERS["subs_brackets_he"] = subs_brackets_he
FILTERS["langname"] = langname
FILTERS["yiddish_letters"] = fix_yiddish_letters

def main():

    BOOK_PATH = os.environ['TNK_BOOK_PATH'][:-1] if os.environ['TNK_BOOK_PATH'].endswith("/") else os.environ['TNK_BOOK_PATH']
    LANG_1 = os.environ['TNK_BOOK_LANG1'] if len(os.environ['TNK_BOOK_LANG1']) > 0 else None
    LANG_2 = os.environ['TNK_BOOK_LANG2'] if len(os.environ['TNK_BOOK_LANG2']) > 0 else None

    paths = []

    languages = [LANG_1, LANG_2]
    languages = list(filter(lambda x: x is not None, languages))

    lang_signature = "-".join(languages)
    output_filename = os.path.basename(BOOK_PATH) + "_" + lang_signature

    os.environ['TNK_BOOK_HTMLDOC'] = os.path.join(BOOK_PATH, output_filename)


    if LANG_1 is not None:
        paths.append(os.path.join(BOOK_PATH, LANG_1 + '.json'))

    if LANG_2 is not None:
        paths.append(os.path.join(BOOK_PATH, LANG_2 + '.json'))

    books = []
    title = []

    for path in paths:

        with open(path, 'r') as f:
            book = json.load(f)

            if output_filename is None:
                output_filename = book.get('title')

            if LANG_1 in ['he', 'yi']:
                title_ = book.get('heTitle')
            else:
                title_ = book.get('title')

            if title_ is not None:
                title.append(title_)

            books.append(book.get('text'))

    title = title[0]

    environment = Environment(loader=FileSystemLoader("."))
    template = environment.get_template("book_template.html.j2")

    book_length = len(books[0])

    books_ = [[], []]

    for h in range(len(books)):
        for i in range(book_length):

            if len(books[h][i]) != 0:
                books_[h].append(books[h][i])


    book_length_ = len(books_[0])

    styles = [
         open_file("style.css"),
    #    open_file("book_style.css"),
    #    open_file("book_languages.css")
    ]

    img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "star-of-david.png")

    for h in books_[0]:

        rendered = template.render(title=title, book_length=book_length_, books=books_, languages=languages, styles=styles, img_src=img_src)

    with open(os.path.join(BOOK_PATH, output_filename+'.html'), 'w') as f:
        string = rendered
        f.write(unescape_angle_brackets(string))

    os.system('bash ./calibre')


main()
