def insertion_sort(lst: list):
    """
    loop over every element of the list
      move it back until it's in the right place
    """
    result = []
    for element in lst:
        insertion_index = len(result)
        while insertion_index > 0 and result[insertion_index - 1] > element:
            insertion_index = insertion_index - 1
        result.insert(insertion_index, element)
    return result
