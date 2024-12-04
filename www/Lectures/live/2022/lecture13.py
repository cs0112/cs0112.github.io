from htmltree import *

def count_tag(doc: HTMLTree, goal: str) -> int:    
    '''
    Counts the number of times the "goal" tag is present
    in the "doc" HTMLTree
    '''
    print(f'********** processing: {doc}')
    count = 0    
    for child in doc.children: 
        count = count + count_tag(child, goal)
    if goal == doc.tag:        
        count = count + 1    
    return count

tree = parse('<html><p>hello</p><strong><p>world</p></strong></html>')
count_tag(tree, 'p')

# def all_text(doc: HTMLTree) -> list:
#     '''
#     Return a list of all the "text" fields of everything in "doc".
#     '''
#     pass