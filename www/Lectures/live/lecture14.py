from dataclasses import dataclass
from htmltree import HTMLTree

### RECURSION EXERCISE ###

# Start with something local and incomplete...
def replace_text_full(tree: HTMLTree, find: str, replace: str):
    ''' Replace all text occurrences of find with replace, 
        if the _full_ text of the text element matches find '''
    if tree.tag == 'text':
        if tree.text == find:
            tree.text = replace 
    for child in tree.children:
            replace_text_full(child, find, replace)
        
def replace_text_partial(tree: HTMLTree, find: str, replace: str):
    ''' Replace all text occurrences of find with replace 
        if there is a _partial_ match of the text, replace'''
    if tree.tag == 'text':
        tree.text = tree.text.replace(find, replace)
    for child in tree.children:
            replace_text_partial(child, find, replace)








### STARTING POINT ###

class Station:
    def request(self, caller: str, song: str) -> str:
        '''Request a song of the current radio DJ'''
        self.queue.append(song)
        self.num_callers += 1
        if self.num_callers % 1000 == 0:
            return "Congrats, " + caller + "! You get a prize!"
        else:
            return "Cool, " + caller
        
    def __init__(self):
         self.queue = []
         self.num_callers = 0

# the_dj = Station(0, [])
# request(the_dj, "Tim", "French Fries w/Pepper")
the_station = Station()
the_station.request("Tim", "Whirling-In-Rags 8PM")


