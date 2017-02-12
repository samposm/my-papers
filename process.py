#!/usr/bin/python3

# file,title,numbering tag
files = [('papers.txt','Articles in Refereed Journals',''),
         ('book-chapters.txt','Book Chapters','c'),
         ('reports.txt','Reports','r'),
         ('theses.txt','Theses','t')]

class Paper:
    def __init__(self,s,n,tag):
        ss = s.split('\n\n')
        self.n       = str(n)
        self.tag     = tag
        self.authors = ss[0].rstrip()
        self.title   = ss[1].rstrip()
        self.source  = ss[2].rstrip()
        self.link    = None
        self.pdf     = None
        if (len(ss) >= 4): self.link = ss[3].rstrip()
        if (len(ss) >= 5): self.pdf  = ss[4].rstrip()
    def html(self):
        s  = '<tr><td><div class=num>' + self.tag + self.n + '</div>\n'
        if self.link != None:
            s += '<a href="' + self.link + '">link</a><br>\n'
        if self.pdf != None:
            s += '<a href="' + self.pdf + '">pdf</a><br>\n'
        s += '</td><td>\n'
        s += self.authors + ':<br>\n'
        s += self.title + '<br>\n'
        s += self.source + '\n'
        s += '</td></tr>\n'
        return s

def process_file(x):
    filename,title,tag = x
    with open(filename, 'r') as f: p1 = f.read()
    p2 = p1.split('\n\n\n')
    numbering = range(len(p2),0,-1) # from len down to 1
    p3 = [Paper(p,n,tag) for p,n in zip(p2,numbering)]
    header = '<tr><th colspan=2><h2>' + title + '</h2></th></tr>\n'
    print(header)
    [print(p.html()) for p in p3]

[process_file(x) for x in files]
