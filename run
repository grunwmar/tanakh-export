#!/bin/bash
source venv/bin/activate

export TNK_BOOK_FORMAT=$1
export TNK_BOOK_PATH=$2
export TNK_BOOK_LANG1=$3
export TNK_BOOK_LANG2=$4

echo -e "\033[0m"
echo -e " * Creating book from \033[1;37m$TNK_BOOK_PATH\033[0m in languages \033[1;37m$TNK_BOOK_LANG1\033[0m, \033[1;37m$TNK_BOOK_LANG2\033[0m"
python3 make_html.py
echo ""
echo -e "Done.\033[0m"
echo ""
