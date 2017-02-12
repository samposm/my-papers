FILES = 1-top.html 2-papers.html 3-book-chapters-title.html \
4-book-chapters.html 7-bottom.html


all: index.html

index.html: $(FILES)
	cat $^ > $@

2-papers.html: process.py papers.txt
	python3 $< papers.txt > $@

4-book-chapters.html: process.py book-chapters.txt
	python3 $< book-chapters.txt > $@
