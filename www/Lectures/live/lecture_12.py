from htmltree import *


example1 = HTMLTree('p', [
    HTMLTree('text', [], 'This is a paragraph.'),
    HTMLTree('text', [], 'This is another paragraph.'),
    ], '')

# print(example1)

#print_html(example1)

example2 = parse('<p>Some other text</p>')
print(example2)
print_html(example2)






def add1(x: int):
    return x + 1

def is_even(x: int):
    if x % 2 == 0:
        return True 
    else:
        return False