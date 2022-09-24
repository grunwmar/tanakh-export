#!/bin/bash

FLOWSIZE="--flow-size 30"

if ! [ $TNK_BOOK_FORMAT = "epub" ]; then
	 FLOWSIZE=""
fi
MARGINRL=1
MARGINTB=45
ebook-convert "$TNK_BOOK_HTMLDOC".html "$TNK_BOOK_HTMLDOC"."$TNK_BOOK_FORMAT" $FLOWSIZE --level1-toc "//h:h2" --disable-font-rescaling  --embed-all-fonts --page-breaks-before "//h:h1|//h:h2|//h:hr" --pdf-page-margin-bottom $MARGINTB --pdf-page-margin-left $MARGINRL --pdf-page-margin-right $MARGINRL --pdf-page-margin-top $MARGINTB

MVPATH="$TNK_BOOK_HTMLDOC"."$TNK_BOOK_FORMAT"
BSNAME=$(basename "$MVPATH")
TARGET="/home/zeleny/Dokumenty/Tanakh.ex/$BSNAME"

cp "$MVPATH" "$TARGET"
