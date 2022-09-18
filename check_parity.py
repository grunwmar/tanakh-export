"""Check if file have same entry structure."""

import sys
import json
import os


def get_jsonfile_text_content(filepath):
    """Read 'text' content from json file."""
    try:
        json_data = {}
        with open(filepath, 'r') as fp:
            json_data['book'] = json.load(fp)

        with open(filepath, 'w') as fp:
            json.dump(json_data['book'], fp, ensure_ascii=False, indent=3)

        return json_data['book'].get('text')
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    not_failed = True
    merged_book = list()
    error_list  = list()
    books = [get_jsonfile_text_content(path) for path in sys.argv[1:]]

    if len(books) == 0:
        sys.exit(1)

    langs = [os.path.splitext(os.path.basename(path))[0] for path in sys.argv[1:]]
    basedir = os.path.dirname(sys.argv[1])
    last_verse = [None]
    print(books[0])
    for refindex_chapter in range(len(books[0])):
        try:
            chapters = [chapter[refindex_chapter] for chapter in books]
            merged_chapter = []
            for refindex_verse in range(len(chapters[0])):
                index = f"{refindex_chapter+1}:{refindex_verse+1}"
                try:
                    verses = [verse[refindex_verse] for verse in chapters]
                    merged_verse = []
                    print(index)

                    for n, version in enumerate(verses, start=1):
                        merged_verse.append(version)
                        print('\t',n, version)

                    merged_chapter.append(merged_verse)
                    last_verse[0] = (index, merged_verse)

                except Exception as e:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Error on", index, e, last_verse[0])
                    error_list.append((f'{index} # {e}', last_verse[0]))
                    not_failed &= False

                print('\n')

            merged_book.append(merged_chapter)
        except Exception as e:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("Error on", index, e)
            error_list.append((f'{index} # {e}', last_verse[0]))
            not_failed &= False

        print('\n')


    if not_failed:
        with open(os.path.join(basedir, 'MATCH['+'-'.join(langs) + ']'), 'w') as fp_check:
            fp_check.write('true')

    else:

        err_str = ""

        for err, (i,(a,b)) in error_list:
            err_str_item = f"ERR {err}\n\t--> {a}\n\t--> {b}\n"
            err_str += err_str_item
            print(err_str_item)


        with open(os.path.join(basedir, 'FAIL['+'-'.join(langs) + ']'), 'w') as fp_check:
            fp_check.write(err_str)
