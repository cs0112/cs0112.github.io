from htmltree import *

def replace_text(tree: HTMLTree, find: str, replace: str):
    '''Modify an existing HTML tree to replace every instance of text "find" with "replace"
         - Doesn't modify tags, just text.
         - Doesn't return anything, because the tree gets modified in place. No new 
           tree objects get created when calling this function. 
         - recursively descend into all nodes in the tree
         - match _substrings_, not just full text of a node
         - replace _all_ matching strings, not just the first one
           '''        
    # base case: no recursion left to do
    tree.text = tree.text.replace(find, replace)
    # notes: you'll see if tree.tag == "text":
    # recursive case: node has children
    for child in tree.children:
        replace_text(child, find, replace)


# Dataclasses _are_ mutable unless they're declared frozen via @dataclass(frozen=true)

# A dataclass is super convenient, because Python auto-defines things like 
# how to create one (__init__), how to print one, etc. But a dataclass isn't
# flexible enough for all the kinds of object-oriented programming we're 
# going to use in 0112. 

class DJData:
  # Here's how to create a DJData object...
  def __init__(self):
    self.queue = []
    self.num_callers = 0

  # Here's how to provide the length of the object, as if it were a list...
  def __len__(self):
    return len(self.queue)

  # A "method" is a function that belongs to an object. 
  def request(self, caller: str, song: str) -> str:
    self.queue.append(song)
    self.num_callers += 1
    if self.num_callers % 1000 == 0:
      return "Congrats, " + caller + "! You get a prize!"
    else:
      return "Cool, " + caller

the_dj = DJData()
print(the_dj.request("Tim", "French Fries w/Pepper"))
print(len(the_dj))
print(str(the_dj))
