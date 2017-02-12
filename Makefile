FILES = 1-top.html 2-papers.html 7-bottom.html

all: index.html

index.html: $(FILES)
	cat $^ > $@

2-papers.html: papers.py papers.txt
	python3 $< > $@
