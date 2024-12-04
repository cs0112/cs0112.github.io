from insertion_sort import insertion_sort, insertion_sorted, insertion_sorted_2

def test_insertion_sort():
    # This works great if the function returns a sorted list, 
    # rather than just changing the original list!
    # assert insertion_sort([7,4,2,8,5,3]) == [2,3,4,5,7,8]
    list1 = [7,4,2,8,5,3]
    insertion_sort(list1)
    assert list1 == [2,3,4,5,7,8]

    list2 = [] 
    insertion_sort(list2)
    assert list2 == []

    # from class:

    list3 = [2,5,7,8,2] 
    insertion_sort(list3)
    assert list3 == [2,2,5,7,8]

    list4 = [1,2,3,4,5]  # already sorted
    insertion_sort(list4)
    assert list4 == [1,2,3,4,5]

    list5 = [1] 
    insertion_sort(list5)
    assert list5 == [1]


# added after class, for demo
def test_insertion_sorted():
    assert insertion_sorted([7,4,2,8,5,3]) == [2,3,4,5,7,8]
    assert insertion_sorted([]) == []
    assert insertion_sorted([2,5,7,8,2]) == [2,2,5,7,8]
    assert insertion_sorted([1,2,3,4,5]) == [1,2,3,4,5]
    assert insertion_sorted([1]) == [1]

# also added after class
def test_insertion_sorted_2():
    assert insertion_sorted_2([7,4,2,8,5,3]) == [2,3,4,5,7,8]
    assert insertion_sorted_2([]) == []
    assert insertion_sorted_2([2,5,7,8,2]) == [2,2,5,7,8]
    assert insertion_sorted_2([1,2,3,4,5]) == [1,2,3,4,5]
    assert insertion_sorted_2([1]) == [1]
