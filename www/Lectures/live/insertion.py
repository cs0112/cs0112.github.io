
def insertion_sort(lst: list): 
    '''Sort the given list in ascending order. Modifies the given list, 
       and returns nothing. Does not use an extra list.'''
    if len(lst) == 0: return

    # for everything in the input list left-to-right 
    index = 1 # the next unsorted element
    # [         |         ]
    #  ^ sorted   ^ unsorted
    while index < len(lst):
        #   we need to put the element here in its proper place
        element = lst[index]
        print(f'list is: {lst}. moving element at {index}, which is {element}')
        insertion_index = index # start looking for the right place here
        while insertion_index > 0 and element < lst[insertion_index-1]:
            print(f'    swapping to move {element} left to index {insertion_index-1}')
            lst[insertion_index] = lst[insertion_index-1]
            lst[insertion_index-1] = element
            insertion_index = insertion_index - 1
        
        
        #   for everything in the sorted list so far (right to left?)
        #     if this is the place, insert the thing

        index = index + 1
    pass

############

# In "if" version:
x1 = ['e','d','c','b','a']  
insertion_sort(x1)
print(x1)

x2 = ['a', 'b', 'c', 'd', 'e']  
insertion_sort(x2)
print(x2)


def test_for_insertion_sort(on_list: list, expected: list):
    list_copy = list(on_list)
    insertion_sort(list_copy)
    assert list_copy == expected      
    
def test_insertion_sort_starter():
    test_for_insertion_sort([2,1,3], [1,2,3])
    test_for_insertion_sort([], [])
    test_for_insertion_sort([1,2,3,4,5], [1,2,3,4,5])
    test_for_insertion_sort([5,4,3,2,1], [5,4,3,2,1])

# duplicates
# fully sorted
# fully inverse sorted
# empty list 
# singleton list 
