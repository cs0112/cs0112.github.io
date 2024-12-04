from merge import *
from mergesort import *

def test_merge():
    assert merge([], []) == []
    assert merge([1,3,5], [2,4,6,8]) == [1,2,3,4,5,6,8]
    assert merge([1,3,5], [6,7]) == [1,3,5,6,7]
    assert merge([2,4,6,8], [1,3,5]) == [1,2,3,4,5,6,8]
    assert merge([1,3,5], [3]) == [1,3,3,5]
    assert merge([1], [2]) == [1,2]
    assert merge([1], []) == [1]
    assert merge([], [2]) == [2]

def test_mergesort():
    assert merge_sort([]) == []
    assert merge_sort(["a", "ab", "abc"]) == ["a", "ab", "abc"]
    assert merge_sort([4, 2, 3, 2]) == [2, 2, 3, 4]
    assert merge_sort([1,2,3]) == [1,2,3]
    assert merge_sort([-5, -4, 3, 2, 1]) == [-5, -4, 1, 2, 3]


    





from random import randint
def random_list(max_length: int, min_value: int, max_value: int) -> list:
  length = randint(0, max_length)
  return [randint(min_value, max_value) for _ in range(length)]


#print(random_list(100, -100, 100))
MAX_LENGTH = 5
MIN_VALUE = 0
MAX_VALUE =  10
NUM_TRIALS = 10000
def test_mergesort_random():
    for i in range(NUM_TRIALS):
        test_list = random_list(MAX_LENGTH, MIN_VALUE, MAX_VALUE)
        #print(f'list {i} = {test_list}')
        merge_sort(test_list)


def test_mergesort_random_2():
    for i in range(NUM_TRIALS):
        test_list = random_list(MAX_LENGTH, MIN_VALUE, MAX_VALUE)
        assert merge_sort(test_list) == sorted(test_list)