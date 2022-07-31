#!/bin/bash

FLOWSIZE="--flow-size 30"

if ! [ $TNK_BOOK_FORMAT = "epub" ]; then
	 FLOWSIZE=""
fi

ebook-convert "$TNK_BOOK_HTMLDOC".html "$TNK_BOOK_HTMLDOC"."$TNK_BOOK_FORMAT" $FLOWSIZE --level1-toc "//h:h2" --disable-font-rescaling  --embed-all-fonts --page-breaks-before "//h:h1|//h:h2|//h:hr"
