from htmltree import *

def fact(n: int): 
    if n <= 1: 
        return 1
    else:
        return fact(n-1) * n

# fact(1) = 1
# fact(2) = 2
# fact(3) = 6
# fact(4) = 24 
# fact(5) = 120 
# fact(6) = 720


# Start with a version that only works locally
def count_tag(doc: HTMLTree, goal: str) -> int:  
    '''Count the number of elements with tag equal to some goal value'''  
    counter = 0
    if doc.tag == goal:
        counter = counter + 1 
    for child in doc.children: 
        counter = counter + count_tag(child, goal)
    return counter
    
# class HTMLTree:  # this is a node in the overall tree!
#    tag: str
#    children: list
#    text: str = ""


print(count_tag(parse("<html><table><tr></tr></table><table></table></html>"), "table"))







# Start with a version that only works locally
def all_text(doc: HTMLTree) -> list[str]:
    '''Descend into the tree and accumulate all text elements in a list'''
    print(f'all_text: {to_html_string(doc)}')
    text = []
    if doc.tag == "text":
        text.append(doc.text)    
    for child in doc.children: 
        text = text + all_text(child)
    return text

two_tables = parse("<html><table><tr><td>Nim</td><td>Telson</td></tr><tr><td>Tim</td><td>Nelson</td></tr></table><tr><td>CSCI 0112</td></tr><table></table></html>")
#print(two_tables)
print(all_text(two_tables))
