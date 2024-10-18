from merge import *

def merge_sort(lst: list) -> list:
    if len(lst) <= 1: return lst[:] # make a new copy
    mid = len(lst) // 2 # or int(...)
    left = lst[:mid]
    right = lst[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)
