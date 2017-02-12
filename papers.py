#!/usr/bin/python3

papersfile = 'papers.txt'

class Paper:
    def __init__(self,s,n):
        ss = s.split('\n\n')
        self.n       = str(n)
        self.authors = ss[0].rstrip()
        self.title   = ss[1].rstrip()
        self.source  = ss[2].rstrip()
        self.link    = None
        self.pdf     = None
        if (len(ss) >= 4): self.link = ss[3].rstrip()
        if (len(ss) >= 5): self.pdf  = ss[4].rstrip()
    def html(self):
        s  = '<tr><td><div class=num>' + self.n + '</div>\n'
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

with open(papersfile, 'r') as f: p1 = f.read()
p2 = p1.split('\n\n\n')
l2 = len(p2)
p3 = [Paper(p,n) for p,n in zip(p2,range(l2,0,-1))]

[print(p.html()) for p in p3]
