from merge import merge
from mergesort import merge_sort

def test_merge():
    # lecture-notes example 
    assert merge([2,4,6], [3,5,7]) == [2,3,4,5,6,7]
    # corner cases (empty, singletons, ...)
    assert merge([], []) == [] 
    assert merge([1], []) == [1] 
    assert merge([], [1]) == [1] 
    assert merge([1], [2]) == [1,2]
    # single addition
    assert merge([1,2,3], [4]) == [1,2,3,4]
    assert merge([4], [1,2,3]) == [1,2,3,4]
    # single addition with duplication
    assert merge([1,2,3,4], [3]) == [1,2,3,3,4]
    assert merge([3], [1,2,3,4]) == [1,2,3,3,4]

    # ??? Should we write this?
    # No, because then we're "over-promising"
    #assert merge([3,2,1], [1,2,3,4]) == [1,1,2,2,3,3,4]

    # It's hard to know when to stop. This is always a problem! 
    # There are a few ways to _help_ boost confidence in testing;
    # more on this next week and in CSCI 1710.

# A few tests, which ideally we would add to.
def test_merge_sort():
    assert merge_sort([7,4,2,8,5,3]) == [2,3,4,5,7,8]
    assert merge_sort([]) == []
    assert merge_sort([2,5,7,8,2]) == [2,2,5,7,8]
    assert merge_sort([1,2,3,4,5]) == [1,2,3,4,5]
    assert merge_sort([1]) == [1]

