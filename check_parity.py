"""Check if file have same entry structure."""

import sys
import json
import os


def get_jsonfile_text_content(filepath):
    """Read 'text' content from json file."""
    try:
        with open(filepath) as fp:
            return json.load(fp).get('text')
    except:
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

                except Exception as e:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Error on", index, e)
                    error_list.append(f'{index} # {e}')
                    not_failed &= False
    
                print('\n')

            merged_book.append(merged_chapter)
        except Exception as e:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("Error on", index, e)
            error_list.append(f'{index} # {e}')
            not_failed &= False
 
        print('\n')


    if not_failed:
        with open(os.path.join(basedir, 'MATCH['+'-'.join(langs) + ']'), 'w') as fp_check:
            fp_check.write('true')

    else:

        for err in error_list:
            print(err)

        err_str = json.dumps(error_list, ensure_ascii=False, indent=3)


        with open(os.path.join(basedir, 'FAIL['+'-'.join(langs) + ']'), 'w') as fp_check:
            fp_check.write(err_str)






