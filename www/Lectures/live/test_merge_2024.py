from mergesort_2024 import merge_sort
from random import randint

def random_list(max_length: int, min_value: int, max_value: int) -> list:
  length = randint(0, max_length)
  return [randint(min_value, max_value) for _ in range(length)]



def test_mergesort_random():
  for _ in range(10000):
    r_list = random_list(20, 0, 100)
    sorted_random_list = merge_sort(r_list)
    sorted_random_list_2 = sorted(r_list)
    assert sorted_random_list == sorted_random_list_2
    
test_mergesort_random()