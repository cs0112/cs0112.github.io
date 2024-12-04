from dataclasses import dataclass
from random import choices
from string import ascii_letters, digits
from typing import TypeVar

# Recall dataclasses (link to 111 book's section in notes)
@dataclass
class Location:
    lat: float
    long: float

# Unhashable type: list
class_time_and_loc = tuple(['BH 141', '1:00pm'])
print(hash(class_time_and_loc))
# classes = {class_time_and_loc: 'CSCI 0112'}

# Tuples are hashable because they are immutable
# In a real app, we'd use Python's built in date/time utility, not a string
class_time = ('BH 141', '1:00pm')

classes = {class_time: 'CSCI 0112'}

my_classes = {'0112', '0320', '1710'}
# {} # this is a dictionary
# set() # this is a set

list1 = (1, 2, 3)
list2 = (1, 2, 3)
print(hash(list1))
print(hash(list2))


############ Setup ############

# Python provides us a nice hash() function. It's far better than our "% 10" version
# for a few reasons, one of which is that it works on most datatypes directly!
print(hash('Happy Friday!'))
# it's consistent within a single program run, but may change between runs


############ Exercise ############
    
# The table is a list and the element is a string
# def addToTable(table: list, element: str):
# The table is a list (of lists -- assuming we're fixing collisions with sublists)
# def addToTable(table: list[list], element: str):

# def searchTable(table: list, element: str):
#     '''search for an element in the hash-table set'''

# def demo(table_size: int, num_elements: int, element_length: int):
#     '''Add a large number of random elements to the hash-table set, then
#          show how well-distributed the random elements were'''


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




# def demo(table_size: int, num_elements: int, element_length: int):
#     '''Add a large number of random elements to the hash-table set, then
#          show how well-distributed the random elements were
#     '''
#     table = [[] for _ in range(table_size)]
#     for _ in range(num_elements):
#         random_element = ''.join(choices(ascii_letters + digits, k=element_length))
#         add(table, random_element)
#     print([len(sublist) for sublist in table])

# demo(1000, 10, 5)
