import json
import os
from bs4 import BeautifulSoup
from hebrew_numbers import  int_to_gematria
from filters import fix_yiddish_letters, replace_brackets, unescape_angle_brackets


LETTER_INDICES = 'abcdefghijklmnopqrstuvwxyz'


def convert_index(lang, int):
    if lang in ['he', 'yi']:
        return int_to_gematria(int, gershayim=False)
    else:
        return str(int)


def main():

    BOOK_PATH = os.environ['TNK_BOOK_PATH']
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


    html_doc = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{title}</title>
  <link rel="stylesheet" type="text/css" href="../../../book_style.css" />
  <link rel="stylesheet" type="text/css" href="../../../book_languages.css" />
</head>
<body>

</body>
</html>
"""

    html_soup = BeautifulSoup(html_doc, 'html.parser')

    html_headline = html_soup.new_tag('h1')
    html_headline.string = str(title)
    html_headline['lang'] = languages[0]

    html_soup.append(html_headline)

    merged_book_text = []

    for i in range(len(books[0])):

        chapter = i + 1

        html_chapter_title = html_soup.new_tag('h2')
        html_chapter_title['lang'] = languages[0]

        html_chapter_title.string = convert_index(languages[0], chapter)

        html_break = html_soup.new_tag('hr')

        html_soup.append(html_break)
        html_soup.append(html_chapter_title)


        for j in range(len(books[0][i])):

            verse = j + 1

            html_verse = html_soup.new_tag('div')
            html_verse['class'] = 'verse'

            for n, b in enumerate(books):

                lang = languages[n]

                html_verse_lang = html_soup.new_tag('p')

                verse_item = b[i][j]

                if isinstance(verse_item, list):
                    verse_item = '<br /><span class="arrow">»</span> '.join(verse_item)


                if lang in ['he', 'yi']:
                    text = replace_brackets(verse_item, new=('<sup>', '</sup>'))
                else:
                    text = replace_brackets(verse_item, old=('[', ']'))
                    


                if lang == "yi":
                    html_verse_lang.string = fix_yiddish_letters(text)
                else:
                    html_verse_lang.string = text

                html_verse_lang['class'] = 'lang'
                html_verse_lang['lang'] = lang
                html_verse_lang['title'] = convert_index(lang, verse)

                html_verse.append(html_verse_lang)

            html_soup.append(html_verse)

        

    with open(os.path.join(BOOK_PATH, output_filename+'.html'), 'w') as f:
        string = html_soup.prettify()
        f.write(unescape_angle_brackets(string))

    os.system('bash convert.sh')




main()
