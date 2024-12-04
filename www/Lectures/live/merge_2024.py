

def merge(list1: list, list2:list ) -> list:
    '''Accepts two sorted lists and combines them into a single sorted list
       with the same elements as list1+list2 would. Runs in worst-case 
       time proportional to the total list length overall.'''
    # "sorted" is worst-case O(n*log(n)). No!
    # return sorted(list1+list2)
    print(f'merge: {list1} with {list2}')
    result = []
    index1 = 0  # current position in list1
    index2 = 0  # current position in list2
    while index1 < len(list1) or index2 < len(list2):
        if index1 >= len(list1): 
            result.append(list2[index2])
            index2 = index2 + 1
        elif index2 >= len(list2):
            result.append(list1[index1])
            index1 = index1 + 1
        elif list1[index1] > list2[index2]:
            result.append(list2[index2])
            index2 = index2 + 1
        else:
            result.append(list1[index1])
            index1 = index1 + 1
    return result 

if __name__ == '__main__':
    assert merge([2,4,6], [3,5,7]) == [2,3,4,5,6,7]
    assert merge([1], [2,3,4]) == [1,2,3,4]
    assert merge([1,2,3], [4]) == [1,2,3,4]
    assert merge([], []) == []
    assert merge([1], []) == [1]
    assert merge([], [1]) == [1]
    assert merge([2], [1]) == [1,2]

# Should I write a test like this?
# assert merge([3,2,1], [10,11,12]) == ??? # [1,2,3,10,11,12]

# [2,4,6] [3,5,7] ~~~ []
# [ ,4,6] [3,5,7] ~~~ [2]
# [ ,4,6] [ ,5,7] ~~~ [2,3]
# [ , ,6] [ ,5,7] ~~~ [2,3,4]
# [ , ,6] [ , ,7] ~~~ [2,3,4,5]
# [ , , ] [ , ,7] ~~~ [2,3,4,5,6]
# [ , , ] [ , , ] ~~~ [2,3,4,5,6,7]

