















from dataclasses import dataclass, field

# Immutable, but also auto-generate <
@dataclass(frozen=True,order=True)
class Record:
    age: int
    # exclude "name" from use in <, >, etc.
    name: str = field(compare=False)






# I like divide and conquer sorting, but I dislike using "merge" 
# to combine sublists.
def quick_sort_first_try(l: list) -> list:
    if len(l) <= 1:
        return l[:] # fresh copy of the list
    # ??? what to do here?
    side1_sorted = quick_sort(side1)
    side2_sorted = quick_sort(side2)
    return side1_sorted + side2_sorted



# Key idea, by example:
# [3,2,13,1,7]
#   what's < vs. > than 3?
#   [1,2] and [13,7]. 
#     sort these, then combine with 3 in the middle

def quick_sort(l: list) -> list:
    if len(l) <= 1:
        return l[:]
    pivot = l[0] # many other choices possible
    smaller = [x for x in l if x < pivot]
    larger = [x for x in l if x > pivot]
    smaller_sorted = quick_sort(smaller)
    larger_sorted = quick_sort(larger)
    return smaller_sorted + [pivot] + larger_sorted



