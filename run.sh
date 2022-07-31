#!/bin/bash
source venv/bin/activate

export TNK_BOOK_FORMAT=$1
export TNK_BOOK_PATH=$2
export TNK_BOOK_LANG1=$3
export TNK_BOOK_LANG2=$4

python3 make_html.py
