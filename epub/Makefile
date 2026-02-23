chapters = $(wildcard ../caibidlí/*.txt)

Manannán.epub: title.txt epub.css $(chapters)
	pandoc -o Manannán.epub -c epub.css title.txt \
	$(chapters)
