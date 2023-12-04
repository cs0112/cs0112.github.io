from htmltree import *

# Start with a version that only works locally
def count_tag(doc: HTMLTree, goal: str) -> int:    
    count = 0
    if doc.tag == goal:
        count = count + 1
    for child in doc.children:
        count = count + count_tag(child, goal)
    return count

count_tag(parse("<html><table></table><table></table></html>"), "table")


# Start with a version that only works locally
def all_text(doc: HTMLTree) -> list:
    '''Descend into the tree and accumulate all text elements in a list'''
    text = []
    if doc.tag == "text":
        text.append(doc.text)    
    return text

