from merge import merge

def merge_sort(lst: list) -> list:
    '''Sort the input list using the merge sort algorithm. The result 
    will be a different list object than the input.'''
    # base case(s): 
    if len(lst) <= 1: return lst[:] # new list, same contents
    # divide (N time)
    mid = len(lst) // 2 # use integer division
    left = lst[:mid]   # elements 0 ... (mid-1)
    right = lst[mid:] # elements mid ... len(lst)-1
    
    # This is *CORRECT* but isn't *PERFORMANT*
    #left = lst[:1]  # first element only
    #right = lst[1:] # all but first element

    # recur (...)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # combine and return (N time)
    return merge(sorted_left, sorted_right)

merge_sort([5,4,3,2,1])