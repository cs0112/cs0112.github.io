# Notice that there are many ways to implement "insertion sort". 
# In class, we built one of them that I said is probably the most 
# complex: working _entirely_ within the given list, rather than 
# creating another one. 

# Version 1: in-place, Python-style lists (manage insertion via swaps); 
# do everything at once without a helper function.
def insertion_sort(lst: list):
     """
     loop over everything in the list from left to right:
         move it into its proper place in the sorted prefix/sublist
     """
     index = 1 # because 0th element is "sorted" by itself
     while index < len(lst):
          print(f'starting: index={index}; lst={lst}')
          value_to_move = lst[index] 
          insertion_index = index
          while insertion_index > 0 and value_to_move < lst[insertion_index-1]:
             lst[insertion_index] = lst[insertion_index-1]
             lst[insertion_index-1] = value_to_move
             insertion_index = insertion_index - 1
          print(f'ending: index={index}; lst={lst}')
          index = index + 1
          
################################################################################

# Version 2: no longer in-place, but still built for Python-style lists
#   using swapping for insertion. 

# This version is a bit simpler, because of the helper function breaking 
# out the intuition of insertion sort. It's still quite tangled, though.
# Notice that most of the confusion (at least for me!) comes from the indexing.
def insertion_sorted(lst: list):
     '''Sort the given list and return a new list containing the same elements, but sorted in ascending order'''

     def insert(into: list, element):
          '''Insert an element into sorted position in a list.'''
          into.append(element) # like in the first version, start with the new element at the end of the list
          
          insertion_index = len(into) - 1 # where is the element we're inserting?
          # keep swapping to move the new element back until it's in place
          while insertion_index > 0 and into[insertion_index - 1] > element:
               into[insertion_index] = into[insertion_index - 1]
               into[insertion_index - 1] = element
               insertion_index = insertion_index - 1

     result = []
     for (index, item) in enumerate(lst): 
          insert(result, item)
     return result

################################################################################

# Version 3: Let's stop trying to optimize insertion. How would we implement this 
# just using Python's list library, rather than managing swapping around ourselves? 

# Notice how much more readable this one is! 
def insertion_sorted_2(lst: list):
     '''Sort the given list and return a new list containing the same elements, but sorted in ascending order'''

     def insert(into: list, element_to_insert):
          '''Insert an element into sorted position in a list.'''          
          for (position, item) in enumerate(into): 
               if item > element_to_insert: # this is a good place
                    into.insert(position, element_to_insert) # tell Python to do the insertion
                    return # don't continue further; we found the right spot
          # If we reach this point, everything in the list so far comes before the element; just append
          into.append(element_to_insert)

     result = []
     for (index, item) in enumerate(lst): 
          insert(result, item)
     return result
