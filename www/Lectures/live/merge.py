# How can I get list1, list2 sorted without calling a sorting 
# algorithm on them???
def merge(list1: list, list2: list) -> list:
    '''Given two sorted lists, combine them in a way that preserves
       contents such that the resulting list is sorted. If given 
       input lists that are not sorted, no guarantees are made.'''
    # No: 
    #return sorted(list1+list2)

    result = []
    position_in_list1 = 0 # next index in list1
    position_in_list2 = 0 # next index in list2
    # so long as we have something left to add, from EITHER list...
    # while position_in_list1 < len(list1) or position_in_list2 < len(list2):
    while len(result) < len(list1) + len(list2): 
        
        ### If I am here, I know there's some value(s) left to add

        # list1 is empty
        if position_in_list1 >= len(list1):
            result.append(list2[position_in_list2])
            position_in_list2 = position_in_list2 + 1

        # list2 is empty
        elif position_in_list2 >= len(list2): 
            result.append(list1[position_in_list1])
            position_in_list1 = position_in_list1 + 1

        # we want to pull from list1
        elif list1[position_in_list1] < list2[position_in_list2]: 
            result.append(list1[position_in_list1])
            position_in_list1 = position_in_list1 + 1

        # we want to pull from list2
        else: 
            result.append(list2[position_in_list2])
            position_in_list2 = position_in_list2 + 1
    return result 

