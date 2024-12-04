from insertion_sort import *

# sorting a list of numbers, or anything else where "<" is defined
def test_insertion_sort():
    # NO! insertion_sort doesn't return anything
    # assert insertion_sort([2,3,1]) == [1,2,3]
    
    list1 = []
    insertion_sort(list1)
    assert list1 == []

    # Help me write tests!

    list2 = ["a", "ab", "abc"]
    insertion_sort(list2)
    assert list2 == ["a", "ab", "abc"]

    # what is duplicates?
    list3 = [4, 2, 3, 2]
    insertion_sort(list3)
    assert list3 == [2, 2, 3, 4]

    list4 = [1,2,3]
    insertion_sort(list4)
    assert list4 == [1,2,3]

    # are negative numbers handled well?
    list5 = [-5, -4, 3, 2, 1]
    insertion_sort(list5)
    assert list5 == [-5, -4, 1, 2, 3]


    