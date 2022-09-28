#!/bin/bash
EXPORTDIR=$(cat EXPORT_DIRECTORY)
FLOWSIZE="--flow-size 80"
NOEPUBCOVER="--no-default-epub-cover"
if ! [ $TNK_BOOK_FORMAT = "epub" ]; then
	 FLOWSIZE=""
	 NOEPUBCOVER=""
fi
MARGINRL=1
MARGINTB=20

#PDF margins
if [ $TNK_BOOK_FORMAT = "pdf" ]; then
		 BOOK_MARGIN_R="--pdf-page-margin-right $MARGINRL"
		 BOOK_MARGIN_L="--pdf-page-margin-left $MARGINRL"
		 BOOK_MARGIN_T="--pdf-page-margin-top $MARGINTB"
		 BOOK_MARGIN_B="--pdf-page-margin-bottom $MARGINTB"
 	else
		 BOOK_MARGIN_R="--margin-right 1"
	 	 BOOK_MARGIN_L="--margin-left 1"
	 	 BOOK_MARGIN_T="--margin-top 1"
	 	 BOOK_MARGIN_B="--margin-bottom 1"
fi

BASE_FONTSIZE="--disable-font-rescaling --paper-size a5"
if [ $TNK_BOOK_FORMAT = "epub" ]; then
	BASE_FONTSIZE="--disable-font-rescaling"

fi

echo -e " * Converting \033[1;37m$TNK_BOOK_HTMLDOC\033[0m to \033[1;35m$TNK_BOOK_FORMAT\033[0m..."

ebook-convert "$TNK_BOOK_HTMLDOC".html "$TNK_BOOK_HTMLDOC"."$TNK_BOOK_FORMAT" $FLOWSIZE $NOEPUBCOVER $BASE_FONTSIZE --level1-toc "//h:h2" --embed-all-fonts --page-breaks-before "//h:h1|//h:h2|//h:hr" $BOOK_MARGIN_B $BOOK_MARGIN_L $BOOK_MARGIN_R $BOOK_MARGIN_T >/dev/null 2>>"ERROR_LOG"
echo -e "\n\n">>"ERROR_LOG"
MVPATH="$TNK_BOOK_HTMLDOC"."$TNK_BOOK_FORMAT"
BSNAME=$(basename "$MVPATH")

TARGETDIR="$EXPORTDIR/$(basename $(dirname $MVPATH))"

if ! [[ -d $TARGETDIR ]]; then
	mkdir $TARGETDIR
fi

TARGET="$TARGETDIR/$BSNAME"
cp "$MVPATH" "$TARGET"

DIRNAME=$(dirname "$MVPATH")
cd "$DIRNAME"
echo ""
echo -e " [\033[1;32m$DIRNAME\033[0m]"
echo -e "\033[1;36m"
ls
echo -e "\033[0m"
echo " * Cleaning source directory..."
rm *.epub 2> /dev/null
rm *.pdf 2> /dev/null
rm *.html 2> /dev/null
echo -e "\033[0m"
echo -e " [\033[1;32m$DIRNAME\033[0m]"
echo -e "\033[1;36m"
ls
echo -e "\033[0m"
echo "..."
