from dataclasses import dataclass        # for early example
from random import choices               # help with demo
from string import ascii_letters, digits # help with demo
from typing import TypeVar  # not needed except for advanced type-hint use
# ^ I'll explain how we're using these as we go





############ Prelude, reminders ############

# Unhashable type: list
# class_time_and_loc = ['BH 141', '1:00pm']
# classes = {class_time_and_loc: 'CSCI 0112'}
# print(hash(class_time_and_loc))

# Tuples are hashable because they are immutable
# In a real app, we'd use Python's built in date/time utility, not a string
# class_time = ('BH 141', '1:00pm')
# classes = {class_time: 'CSCI 0112'}


# my_classes = {'0112', '0320', '1710'}
# {} # this is an empty dictionary
# set() # this is an empty set   (avoid ambiguity about type of {})







# Recall dataclasses (link to 111 book's section in notes)
@dataclass
class Geolocation:
    lat: float
    long: float
# To use as a key in a set/dict: add @dataclass(frozen=True)








############ Setup ############

# Python provides us a nice hash() function. It's far better than our 
# "% 10" for a few reasons, one of which is that it works on most 
# datatypes directly! Like strings (but also others)
print(hash('Happy Friday!'))
# it's consistent within a single program run, but may change between runs


# hashes differ by object (usually -- collisions are extremely rare)
list1 = (1, 2, 3)
list2 = (1, 2, 3)
# print(f'list1: {hash(list1)}')
# print(f'list2: {hash(list2)}')



############ Exercise ############
# Let's write a hash table together!

# The table is a list and the element is a string
#def addToTable(table: list, element: str):
# The table is a list (of lists -- assuming we're fixing collisions with sublists)
def addToTable(table: list[list], element: str) -> bool:
    '''Add a given value to a hash table; duplicates are ignored.'''
    idx = hash(element) % len(table)
    bucket = table[idx]
    if element not in bucket: 
        bucket.append(element)
        return True
    else:
        return False


def searchTable(table: list[list], element: str) -> bool:
    '''search for an element in the hash-table set'''
    idx = hash(element) % len(table)
    bucket = table[idx]
    if element in bucket:  ## not 
        #bucket.append(element)
        return True
    else:
        return False









# Left for the reader, optionally :-)
#   - removeFromTable   (might want to take an element out)
#   - resizeTable       (increase size to reduce collision rate)




# If we want to use type hints more deeply (you aren't required to):
#ELEMENT_TYPE = TypeVar('ELEMENT_TYPE')
#def addToTable(table: list[list[ELEMENT_TYPE]], element: ELEMENT_TYPE):
#    pass



############ Solution ############

# def add(table: list, element: str):
#     '''Add an element to the hash-table set'''
#     idx = hash(element) % len(table)
#     if element not in table[idx]:
#         table[idx].append(element)

# def search(table: list, element: str):
#     '''search for an element in the hash-table set'''
#     idx = hash(element) % len(table)
#     return element in table[idx]




def demo(table_size: int, num_elements: int, element_length: int):
    '''Add a large number of *random* elements to a hash table, then
       show how well-distributed the random elements were. 
         table_size: how many elements in the table list?
         element_length: generate random strings how long?
         num_elements: how many random elements to add?
    '''
    table = [[] for _ in range(table_size)]
    for _ in range(num_elements):
        random_element = ''.join(choices(ascii_letters + digits, k=element_length))
        addToTable(table, random_element)
    print([len(sublist) for sublist in table])

# size 1000, add 10 random elements of length 5
demo(1000, 500, 5)
