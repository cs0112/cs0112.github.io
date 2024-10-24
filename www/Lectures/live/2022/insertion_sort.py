
def insertion_sort(lst: list):
    """
    loop over everything in the list and 
      move it into the right place in the sorted prefix
    """
    # for element in lst: 
    index = 1  # ???
    while index < len(lst):        
        element = lst[index]
        while index > 0 and element < lst[index-1]:
            print(f'index={index}; element={element}')
            # find correct place in sorted prefix + move            
            lst[index] = lst[index-1]
            lst[index-1] = element
            index = index - 1
        index = index + 1

testList = [300, 200, 100, 100]
insertion_sort(testList)
print(testList)