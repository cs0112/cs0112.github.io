from htmltree import *
#from dataclasses import dataclass

# @dataclass
# class HTMLTree:
#     tag: str
#     children: list
#     text: str = ""

document = HTMLTree("p", [HTMLTree("text", [], "Text in a paragraph")])
print(document)

document2 = HTMLTree(tag='p', children=[HTMLTree(tag='text', children=[], text='Text in a paragraph')], text='')
print(document2)

print_html(document)