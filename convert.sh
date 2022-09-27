#!/bin/bash
EXPORTDIR=$(cat EXPORT_DIRECTORY)
FLOWSIZE="--flow-size 80"
NOEPUBCOVER="--no-default-epub-cover"
if ! [ $TNK_BOOK_FORMAT = "epub" ]; then
	 FLOWSIZE=""
	 NOEPUBCOVER=""
fi
MARGINRL=1
MARGINTB=45

#PDF margins
if [ $TNK_BOOK_FORMAT = "pdf" ]; then
	 PDF_MARGIN_R="--pdf-page-margin-right $MARGINRL"
	 PDF_MARGIN_L="--pdf-page-margin-left $MARGINRL"
	 PDF_MARGIN_T="--pdf-page-margin-top $MARGINTB"
	 PDF_MARGIN_B="--pdf-page-margin-bottom $MARGINTB"
fi


echo -e " * Converting \033[1;37m$TNK_BOOK_HTMLDOC\033[0m to \033[1;35m$TNK_BOOK_FORMAT\033[0m..."

ebook-convert "$TNK_BOOK_HTMLDOC".html "$TNK_BOOK_HTMLDOC"."$TNK_BOOK_FORMAT" $FLOWSIZE $NOEPUBCOVER --level1-toc "//h:h2" --disable-font-rescaling  --embed-all-fonts --page-breaks-before "//h:h1|//h:h2|//h:hr" $PDF_MARGIN_B $PDF_MARGIN_L $PDF_MARGIN_R $PDF_MARGIN_T >/dev/null 2>>"ERROR_LOG"
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
