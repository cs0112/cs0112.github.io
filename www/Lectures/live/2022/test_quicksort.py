from random import randint, choices
from quicksort import quick_sort, Record
from mergesort import merge_sort

def random_list(max_length: int, min_value: int, max_value: int) -> list:
  length = randint(0, max_length)
  return [randint(min_value, max_value) for _ in range(length)]

MAX_LENGTH = 5
MIN_VALUE = 0
MAX_VALUE =  10
NUM_TRIALS = 1000000
# def test_quicksort():
#     for i in range(NUM_TRIALS):
#         test_list = random_list(MAX_LENGTH, MIN_VALUE, MAX_VALUE)
#         print(test_list)
#         assert quick_sort(test_list) == merge_sort(test_list)


######################

# Hypothesis: "Any time there is a duplicate element, Tim's buggy 
#              quick_sort drops it, keeping only one copy."

def test_quicksort_hypothesis():
   for i in range(NUM_TRIALS):
        # assuming list->set->list doesnt have some bias in ordering
        test_list = list(set(random_list(MAX_LENGTH, MIN_VALUE, MAX_VALUE)))
        copy_list = list(test_list)
        # change copy_list TODO exactly one duplicate value
        
        if len(test_list) > 0:
          # option 1 (the quick way) -- follow QS's structure, dupe thing 1 
          # "If the duplicate is of the pivot, and exists at end of list"
          # e.g. [1,2,3] --> [1,2,3,1]
          copy_list.append(test_list[0]) # what pivot does in QS
          assert len(copy_list) == len(test_list) + 1






######################

from string import ascii_uppercase
def random_string(length: int):
  return ''.join(choices(ascii_uppercase, k=5))

def random_record(max_length: int, min_value: int, max_value: int) -> list[Record]:
  length = randint(0, max_length)
  return [Record(randint(min_value, max_value), random_string(5)) for _ in range(length)]
