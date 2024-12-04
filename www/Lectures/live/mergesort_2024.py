from merge_2024 import merge

def merge_sort(lst: list) -> list:
    '''Sort the input list in ascending order, returning the 
       sorted version as a new list object.'''
    print(f'merge_sort: {lst}') 
    if len(lst) <= 1: return lst[:] # enforce returning a NEW list
    mid = len(lst)//2  # double-slash = integer division, drops remainder
    left = lst[:mid]   # list "slicing": copy of lst from to mid (exclusive)
    right = lst[mid:]  # everything from mid (inclusive) to end of list
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

# print(merge_sort([5,4,3,2,1]))
#     [5,4,3,2,1]
# [5,4]       [3,2,1]
# [5] [4]    [3] [2,1]
#                [2] [1]
#                  [1,2]
#              [1,2,3]
#  [4,5]
#      [1,2,3,4,5]  
    