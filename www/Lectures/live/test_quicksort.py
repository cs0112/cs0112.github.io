from random import randint, choices
from quicksort import quick_sort, Record
from mergesort import merge_sort

# Note: this file illustrates _random testing_, and isn't a replacement 
# for a set of good manually-created test cases.

########################################################################
# Here's what we saw last time, more or less
########################################################################

def random_int_list(max_length: int, min_value: int, max_value: int) -> list:
  '''Produce a random list of ints within specified value ranges.'''
  length = randint(0, max_length)
  return [randint(min_value, max_value) for _ in range(length)]

MAX_LENGTH = 3
MIN_VALUE = 1
MAX_VALUE =  5
NUM_TRIALS = 100000
def test_quicksort_vs_mergesort_ints():
    for i in range(NUM_TRIALS):
        test_list = random_int_list(MAX_LENGTH, MIN_VALUE, MAX_VALUE)
        print(test_list)
        assert quick_sort(test_list) == merge_sort(test_list)

# ONE of the properties we would want to check! 
def prop_is_sorted(l: list):
  if len(l) <= 1: return True
  last = None
  for ele in l: 
    if last != None:
       if last > ele:
          return False
    last = ele
  return True 
         
    












# ##################################################################
# # What if we had lists of records, instead of lists of ints?
# ##################################################################

from string import ascii_uppercase
def random_uppercase_string(length: int):
  '''Generate a random string of the requested length using only uppercase letters'''
  return ''.join(choices(ascii_uppercase, k=length))

def random_record_list(max_length: int, min_value: int, max_value: int) -> list[Record]:
  '''Generate a list of random Record objects with a random age and random name'''
  length = randint(0, max_length)
  return [Record(randint(min_value, max_value), random_uppercase_string(5)) 
          for _ in range(length)]

# # What could go wrong here? After we switch to records (age, name) vs. just an integer.
def test_quicksort_vs_mergesort_records():
    for i in range(NUM_TRIALS):
        test_list = random_record_list(MAX_LENGTH, MIN_VALUE, MAX_VALUE)
        
        result1 = quick_sort(test_list)
        # result2 = merge_sort(test_list)
        # print(f'LIST: {test_list} R1: {result1} R2: {result2}')
        # assert result1 == result2
        assert prop_is_sorted(result1)
        #assert nothing_lost(test_list, result1)
        #assert nothing_added(test_list,result1)
           
        
        
        
        
        
        
        
        
        
#         # Instead: write a function to check whether the output (whatever it is) is right
#         #assert verify_sorter(test_list, quick_sort(test_list))

# def verify_sorter(input: list, output: list) -> bool: 
#     return True # if and only if output is a sorted version of input (TODO)
    












#     # (property 1) is the output sorted?
#     #   loop over output, making sure that every element is >= to its predecessor
#     # (property 2) is the output "the same as" the input
#     #   *NOT* set(input) == set(output)
#     #   count each element of input, check counts same in output
