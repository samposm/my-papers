FILES = \
1-top.html 2-papers.html \
3-book-chapters-title.html 4-book-chapters.html \
5-reports-title.html 6-reports.html \
7-theses-title.html 8-theses.html \
9-bottom.html

all: index.html

index.html: $(FILES)
	cat $^ > $@
2-papers.html: process.py papers.txt
	python3 $< papers.txt > $@
4-book-chapters.html: process.py book-chapters.txt
	python3 $< book-chapters.txt > $@
6-reports.html: process.py reports.txt
	python3 $< reports.txt > $@
8-theses.html: process.py theses.txt
	python3 $< theses.txt > $@
