#!/usr/bin/env python3

import os, datetime, json, collections
from jinja2 import Environment, FileSystemLoader, Template


filepath = os.path.dirname(os.path.abspath(__file__))

with open('papers.json') as data:
    d = json.load(data, object_pairs_hook=collections.OrderedDict)
    #d = json.load(data)
    html = ""
    for item in d["Headers"]:
        header = item
        papers = d["Headers"][item]
        html += Environment(loader=FileSystemLoader(filepath)).get_template('table.html').render(header=header, papers=papers)

with open("index.html", "w") as website:
    website.write(Environment(loader=FileSystemLoader(filepath)).get_template('template.html').render(date=datetime.date.today(), html=html))
