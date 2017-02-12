FILES = 1-top.html 2-middle.html 3-bottom.html

all: index.html

index.html: $(FILES)
	cat $^ > $@
2-middle.html: process.py papers.txt book-chapters.txt reports.txt theses.txt
	python3 $< > 2-middle.html
